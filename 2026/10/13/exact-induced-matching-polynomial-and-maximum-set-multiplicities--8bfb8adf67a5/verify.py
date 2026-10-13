#!/usr/bin/env python3
"""Exact reproducibility checks for induced matching enumeration of cycle prisms.
Uses Python 3 standard library only. Run: python3 verify.py
"""
from collections import Counter
from itertools import product, permutations

ALPHABET = '0RTB'
COMPATIBLE_GAP2 = {('R','R'), ('R','T'), ('R','B'), ('T','B'), ('B','T')}
STATES = [(a,b) for a in ALPHABET for b in ALPHABET if a == '0' or b == '0']


def locally_valid(word):
    n = len(word)
    return all(
        (word[(i-1)%n] == '0' or word[i] == '0') and
        (word[(i-2)%n] == '0' or word[i] == '0' or
         (word[(i-2)%n], word[i]) in COMPATIBLE_GAP2)
        for i in range(n)
    )


def directly_valid(word):
    n = len(word)
    edges = []
    chosen = []
    for i in range(n):
        rung = (2*i,2*i+1)
        top = (2*i,2*((i+1)%n))
        bottom = (2*i+1,2*((i+1)%n)+1)
        edges.extend((rung,top,bottom))
        if word[i] != '0':
            chosen.append({'R':rung,'T':top,'B':bottom}[word[i]])
    adjacency = {frozenset(e) for e in edges}
    return all(
        all(u != v and frozenset((u,v)) not in adjacency for u in e for v in f)
        for j,e in enumerate(chosen) for f in chosen[j+1:]
    )


def matrix():
    m = [[Counter() for _ in STATES] for _ in STATES]
    for i,(a,b) in enumerate(STATES):
        for c in ALPHABET:
            if (b != '0' and c != '0') or (
                a != '0' and c != '0' and (a,c) not in COMPATIBLE_GAP2
            ):
                continue
            m[i][STATES.index((b,c))][int(c!='0')] += 1
    return m


def poly_add(a,b):
    c=Counter(a)
    for k,v in b.items(): c[k]+=v
    return Counter({k:v for k,v in c.items() if v})


def poly_mult(a,b):
    c=Counter()
    for i,v in a.items():
        for j,w in b.items(): c[i+j]+=v*w
    return Counter({k:v for k,v in c.items() if v})


def matmult(A,B):
    d=len(A)
    C=[[Counter() for _ in range(d)] for _ in range(d)]
    for i in range(d):
        for k in range(d):
            if not A[i][k]: continue
            for j in range(d):
                if B[k][j]: C[i][j]=poly_add(C[i][j],poly_mult(A[i][k],B[k][j]))
    return C


def traces(limit):
    T=matrix(); P=[[Counter({0:1}) if i==j else Counter() for j in range(7)] for i in range(7)]
    output={}
    for n in range(1,limit+1):
        P=matmult(P,T)
        output[n]=Counter()
        for i in range(7): output[n]=poly_add(output[n],P[i][i])
    return output


def det_check():
    # Bivariate exact polynomial in (time,marking), stored by (i,j) exponents.
    T=matrix()
    A=[]
    for i in range(7):
        row=[]
        for j in range(7):
            p=Counter({(0,0):1}) if i==j else Counter()
            for power,weight in T[i][j].items(): p[(1,power)]-=weight
            row.append(Counter({k:v for k,v in p.items() if v}))
        A.append(row)
    def times(p,q):
        r=Counter()
        for (i,j),v in p.items():
            for (k,l),w in q.items():r[(i+k,j+l)]+=v*w
        return Counter({k:v for k,v in r.items() if v})
    det=Counter()
    for sigma in permutations(range(7)):
        sign=(-1)**sum(sigma[i]>sigma[j] for i in range(7) for j in range(i+1,7))
        p=Counter({(0,0):sign})
        for i,j in enumerate(sigma):p=times(p,A[i][j])
        det.update(p)  # Counter.update sums the coefficients, including negatives.
    det=Counter({k:v for k,v in det.items() if v})
    f=Counter({(0,0):1,(2,1):1})
    g=Counter({(0,0):1,(1,0):-1,(2,1):-2,(3,1):-1,(4,2):1})
    assert det==times(f,g),(det,times(f,g))
    return len(det)


def main():
    assert len(STATES)==7
    determinant_monomials=det_check()
    traces_by_n=traces(44)
    checked=0
    for n in range(3,10):
        direct=Counter()
        for s in product(ALPHABET,repeat=n):
            local=locally_valid(s)
            graph=directly_valid(s)
            assert local==graph,(n,s)
            if graph: direct[sum(x!='0' for x in s)]+=1
            checked+=1
        assert direct==traces_by_n[n],(n,direct,traces_by_n[n])
    for n in range(3,45):
        p=traces_by_n[n]
        assert max(p)==n//2,(n,p)
        target=n*n if n%2 else (6 if n%4==0 else 2)
        assert p[n//2]==target,(n,p,target)
    assert traces_by_n[3]==Counter({0:1,1:9})
    assert traces_by_n[4]==Counter({0:1,1:12,2:6})
    assert traces_by_n[5]==Counter({0:1,1:15,2:25})
    print('VERIFY_OK cyclic_orders=3..9 patterns=',checked,
          'trace_orders=1..44 determinant_terms=',determinant_monomials,
          'max_and_counts=3..44')


if __name__=='__main__':main()
