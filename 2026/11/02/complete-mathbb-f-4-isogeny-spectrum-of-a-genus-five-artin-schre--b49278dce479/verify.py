#!/usr/bin/env python3
"""Exact finite-field census for a four-parameter family of genus-five curves.

This program uses only Python's standard library and includes all arithmetic
needed to reproduce the table of Hasse--Weil numerators over F_4.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import csv
from itertools import product

# Irreducible polynomials over F_2 defining F_{2^(2*m)}, 1 <= m <= 5.
IRREDUCIBLES = {2: 0b111, 4: 0b10011, 6: 0b1000011,
                8: 0x11b, 10: 0b10000001001}

# Each row: (multiplicity, c_1,...,c_5, supersingular flag).
# The remaining coefficients follow from c_{10-j}=4^{5-j}c_j.
EXPECTED = [
 (36, (8,32,92,216,448), False),
 (24, (4,8,16,32,64), True),
 (24, (4,8,20,40,64), False),
 (24, (4,8,12,8,0), False),
 (18, (8,32,92,224,480), False),
 (12, (4,8,28,64,96), False),
 (12, (4,8,4,-32,-96), False),
 (12, (0,0,4,-8,0), False),
 (9, (8,32,96,256,576), True),
 (6, (0,0,4,0,32), False),
 (6, (4,8,16,48,128), True),
 (3, (4,8,16,16,0), True),
 (3, (12,72,288,848,1920), True),
 (3, (0,0,0,0,64), True),
]

def gf2_rem(a, b):
    assert b > 0
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def test_irreducible(poly, n):
    assert poly.bit_length() == n+1 and poly & 1
    for d in range(1,n//2+1):
        for tail in range(1 << d):
            if gf2_rem(poly,(1 << d) | tail) == 0:
                return False
    return True

def field_mul(x,y,n):
    modulus = IRREDUCIBLES[n]
    out = 0
    while y:
        if y & 1: out ^= x
        y >>= 1
        x <<= 1
        if x & (1 << n): x ^= modulus
    assert 0 <= out < (1 << n)
    return out

def coefficient_embedding(n):
    cardinality = 1 << n
    omega = next(i for i in range(cardinality)
                 if field_mul(i,i,n)^i^1 == 0)
    values = (0,1,omega,omega^1)
    assert len(set(values)) == 4
    return values

def count_all_parameters(m, params):
    n=2*m
    cardinality=1 << n
    sq = [field_mul(v,v,n) for v in range(cardinality)]
    emb=coefficient_embedding(n)
    trace=[]
    for v in range(cardinality):
        t=0
        w=v
        for _ in range(n):
            t ^= w
            w=sq[w]
        assert t in (0,1)
        trace.append(t)
    y_solutions=defaultdict(list)
    for y in range(cardinality):
        y_solutions[sq[y]^y].append(y)
    # Artin--Schreier map is two-to-one on the trace-zero subspace.
    assert all(len(y_solutions.get(v,())) == 2*(trace[v]==0)
               for v in range(cardinality))
    tw = [[trace[field_mul(c,x,n)] for c in emb]
          for x in range(cardinality)]
    counts={p:1 for p in params} # unique point at infinity
    for x in range(cardinality):
        x2=sq[x]
        x3=field_mul(x2,x,n)
        for y in y_solutions[x3]:
            tr_x=tw[x]
            tr_xy=tw[field_mul(x,y,n)]
            tr_x2y=tw[field_mul(x2,y,n)]
            tr_y=tw[y]
            for a,b,c,d in params:
                if tr_x[a]^tr_xy[b]^tr_x2y[c]^tr_y[d] == 0:
                    counts[(a,b,c,d)] += 2
    return counts

def weil_polynomial(point_counts, q=4, genus=5):
    # Newton identities: n c_n = - sum_{i=1}^n c_{n-i} S_i,
    # S_i = q^i + 1 - #C(F_{q^i}).
    c=[1]
    S=[0]+[q**n+1-point_counts[n-1] for n in range(1,genus+1)]
    for n in range(1,genus+1):
        v=-sum(c[n-i]*S[i] for i in range(1,n+1))
        assert v % n == 0
        c.append(v//n)
    return tuple(c+[q**(j-genus)*c[2*genus-j]
                    for j in range(genus+1,2*genus+1)])

def valuations_and_slopes(c):
    def v2(x):
        return 100000 if x==0 else (x & -x).bit_length()-1
    pts=[(i,v2(a)) for i,a in enumerate(c)]
    hull=[]
    for pt in pts:
        while len(hull)>=2 and ((hull[-1][0]-hull[-2][0]) *
              (pt[1]-hull[-1][1]) <= (hull[-1][1]-hull[-2][1]) *
              (pt[0]-hull[-1][0])):
            hull.pop()
        hull.append(pt)
    slope=[]
    for (i,vi),(j,vj) in zip(hull,hull[1:]):
        slope += [Fraction(vj-vi, 2*(j-i))]*(j-i)
    assert len(slope)==10
    return tuple(slope)

def independently_count(n,params):
    # A separate enumeration of all triples (x,y,u), not using traces.
    q=1 << n
    sq=[field_mul(v,v,n) for v in range(q)]
    embedded=coefficient_embedding(n)
    a,b,c,d=[embedded[k] for k in params]
    aff=0
    for x in range(q):
        x2=sq[x]
        x3=field_mul(x2,x,n)
        for y in range(q):
            if sq[y]^y != x3:
                continue
            value=(field_mul(a,x,n)^field_mul(b,field_mul(x,y,n),n)
                   ^field_mul(c,field_mul(x2,y,n),n)
                   ^field_mul(d,y,n))
            for u in range(q):
                if sq[u]^u == value:
                    aff+=1
    return aff+1

def main():
    for n,poly in IRREDUCIBLES.items():
        assert test_irreducible(poly,n),n
    params=list(product(range(4),range(4),range(1,4),range(4)))
    assert len(params)==192
    point_counts={p:[] for p in params}
    for m in range(1,6):
        c=count_all_parameters(m,params)
        for p in params:
            point_counts[p].append(c[p])
    polynomials={p:weil_polynomial(point_counts[p]) for p in params}
    multiplicities=Counter(polynomials.values())
    assert len(multiplicities)==14
    observed=Counter()
    for poly,num in multiplicities.items():
        par=next(p for p,v in polynomials.items() if v==poly)
        supersingular = (par[2]==field_mul(par[1],par[1],2))
        for p,v in polynomials.items():
            if v==poly:
                assert (p[2]==field_mul(p[1],p[1],2))==supersingular
        sl=valuations_and_slopes(poly)
        expected_sl = ((Fraction(1,2),)*10 if supersingular
                       else (Fraction(1,3),)*3+(Fraction(1,2),)*4+
                         (Fraction(2,3),)*3)
        assert sl==expected_sl,(poly,sl)
        observed[(num,poly[1:6],supersingular)] += 1
    assert observed==Counter(EXPECTED),(observed,Counter(EXPECTED))
    # Also compare the independently delivered machine-readable table.
    with Path(__file__).with_name('zeta_table.csv').open(newline='',encoding='utf-8') as fp:
        listed=list(csv.DictReader(fp))
    tabulated=Counter()
    for row in listed:
        cs=tuple(int(row[f'c{i}']) for i in range(1,6))
        tabulated[(int(row['parameter_quadruples']),cs,bool(int(row['supersingular'])))]+=1
    assert tabulated==observed,(tabulated,observed)
    assert sum(num for num,cc,sp in EXPECTED if sp)==48
    assert sum(num for num,cc,sp in EXPECTED if not sp)==144
    for n in (2,4,6):
        m=n//2
        for p in ((0,0,1,0),(1,1,1,0),(0,1,2,1)):
            assert independently_count(n,p)==point_counts[p][m-1],(n,p)
    print('VERIFY_OK: 192 parameter quadruples, 14 Weil polynomials,')
    print('48 supersingular and 144 (1/3,1/2,2/3)-Newton cases;')
    print('independent direct-triple checks through F_64.')

if __name__=='__main__':
    main()
