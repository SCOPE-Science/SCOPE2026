#!/usr/bin/env python3
"""Exact certificate for four-bit pair-hole escape-rate spectrum.
No third-party dependencies. All spectral comparisons use rational Sturm isolation.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict

# Perron-root rational isolators in increasing order, denominators 10^6.
# Each open interval contains one spectral radius and no other class.
LOW = (1465571,1618033,1695620,1704902,1716672,1722083,1730508,1734691,
       1754877,1778479,1784598,1788539,1794309,1805094,1812403,1839286)
MULT = (2,22,10,4,6,8,4,4,28,4,4,2,4,4,6,8)

def trim(p):
    p=list(p)
    while len(p)>1 and p[0]==0: p.pop(0)
    return p

def derivative(p):
    n=len(p)-1
    return trim([p[i]*(n-i) for i in range(n)]) if n else [Q(0)]

def divmod_poly(a,b):
    a=trim(a);b=trim(b)
    if b==[0]: raise ZeroDivisionError
    if len(a)<len(b):return [Q(0)],a
    quo=[Q(0)]*(len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b)
        lead=a[0]/b[0]
        quo[len(quo)-1-k]=lead
        a=trim([v-lead*b[i] if i<len(b) else v for i,v in enumerate(a)])
    return trim(quo),a

def normalized(p):
    p=trim(p)
    if p==[0]:return p
    return trim([v/p[0] for v in p])

def squarefree(p):
    a=trim([Q(x) for x in p]);b=derivative(a)
    while b!=[0]:
        _,r=divmod_poly(a,b);a,b=b,r
    g=normalized(a)
    q,r=divmod_poly([Q(x) for x in p],g)
    assert r==[0]
    return normalized(q)

def sturm(p):
    p=squarefree(p)
    if len(p)==1: return [p]
    ans=[p,derivative(p)]
    while True:
        _,r=divmod_poly(ans[-2],ans[-1])
        if r==[0]:break
        ans.append([-v for v in r])
    return ans

def eval_poly(p,x):
    v=Q(0)
    for a in p:v=v*x+a
    return v

def changes(signs):
    signs=[x for x in signs if x]
    return sum(a*b<0 for a,b in zip(signs,signs[1:]))

def variation(seq,at=None):
    if at is None: vals=[p[0] for p in seq]
    else: vals=[eval_poly(p,at) for p in seq]
    return changes([(v>0)-(v<0) for v in vals])

def charpoly(A):
    # Faddeev-LeVerrier on an integer 8x8 matrix, no floating point.
    n=len(A)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    coeff=[1]
    for k in range(1,n+1):
        C=[[sum(A[i][r]*B[r][j] for r in range(n))
            for j in range(n)] for i in range(n)]
        trace=sum(C[i][i] for i in range(n))
        assert trace%k==0
        c=-(trace//k)
        coeff.append(c)
        for i in range(n): C[i][i]+=c
        B=C
    return tuple(coeff)

def adjacency(pair):
    A=[[0]*8 for _ in range(8)]
    for state in range(8):
        for bit in (0,1):
            w=(state<<1)|bit
            if w not in pair:A[state][w&7]=1
    return A

def classify(cp):
    S=sturm(cp);v_inf=variation(S)
    candidates=[]
    for i,L in enumerate(LOW):
        lo=Q(L,10**6);hi=Q(L+1,10**6)
        assert eval_poly(cp,lo)!=0 and eval_poly(cp,hi)!=0
        vlo=variation(S,lo);vhi=variation(S,hi)
        if vlo-vhi==1 and vhi-v_inf==0:
            candidates.append(i)
    assert len(candidates)==1, (cp,candidates)
    return candidates[0]


def crosscheck_counts():
    # Independent symbolic check of exact finite-time survivor counts.
    checks=0
    for pair in combinations(range(16),2):
        A=adjacency(pair)
        vec=[1]*8
        for n in range(8):
            matrix_count=sum(vec)
            brute_count=0
            for w in range(1 << (n+3)):
                if all(((w >> k)&15) not in pair for k in range(n)):
                    brute_count+=1
            assert matrix_count==brute_count, (pair,n,matrix_count,brute_count)
            checks+=1
            vec=[sum(A[i][j]*vec[j] for j in range(8)) for i in range(8)]
    return checks

def main():
    classes=defaultdict(list); cps={}
    for pair in combinations(range(16),2):
        cp=charpoly(adjacency(pair))
        if cp not in cps:cps[cp]=classify(cp)
        i=cps[cp]
        classes[i].append(pair)
    assert len(cps)==26, ('number characteristic polynomials',len(cps))
    assert len(classes)==16
    assert tuple(len(classes[i]) for i in range(16))==MULT
    assert sum(MULT)==120
    checks=crosscheck_counts()
    assert checks==960
    expected_min=((3,5),(10,12))
    expected_max=((0,1),(0,8),(0,15),(1,8),(5,10),(7,14),(7,15),(14,15))
    assert tuple(sorted(classes[0]))==expected_min
    assert tuple(sorted(classes[15]))==expected_max
    print('CERTIFIED: 120/120 pairs; 26 characteristic polynomials; 16 distinct Perron radii; 960 independent finite-time counts.')
    print('Class | rational isolator | multiplicity | representative | characteristic polynomial')
    for i in range(16):
        pair=classes[i][0]
        print('%2d | (%d,%d)/1000000 | %2d | %s,%s | %s' %
              (i+1,LOW[i],LOW[i]+1,len(classes[i]),format(pair[0],'04b'),format(pair[1],'04b'),charpoly(adjacency(pair))))
    print('MIN pairs:', [format(a,'04b')+'/'+format(b,'04b') for a,b in sorted(classes[0])])
    print('MAX pairs:', [format(a,'04b')+'/'+format(b,'04b') for a,b in sorted(classes[15])])
    return classes

if __name__=='__main__':main()
