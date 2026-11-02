#!/usr/bin/env python3
"""Independent exhaustive tests for affine Frobenius graph strata; Python 3 stdlib only.
This is a supplementary finite check, not a proof of the unrestricted theorem.
"""
from collections import Counter
from math import gcd
from itertools import product

def mobius(n):
    count=0; d=2
    while d*d<=n:
        if n%d==0:
            n//=d;count+=1
            if n%d==0: return 0
            while n%d==0:n//=d
        d+=1
    if n>1:count+=1
    return -1 if count%2 else 1

def irreducible(coeff,p):
    m=len(coeff)-1
    for degree in range(1,m//2+1):
        for base in product(range(p),repeat=degree):
            divisor=list(base)+[1]
            v=list(coeff)
            for j in range(m,degree-1,-1):
                lead=v[j]
                if lead:
                    for k in range(degree+1):v[j-degree+k]=(v[j-degree+k]-lead*divisor[k])%p
            if not any(v[:degree]):return False
    return True

def phi(n):
    return sum(gcd(i,n)==1 for i in range(1,n+1))

def divs(n): return [d for d in range(1,n+1) if n%d==0]

def field(p,m):
    q=p**m
    coeff=None
    for c in product(range(p),repeat=m):
        if irreducible(tuple(c)+(1,),p):
            coeff=tuple(c);break
    assert coeff is not None
    digits=[tuple((k//p**j)%p for j in range(m)) for k in range(q)]
    add=[[sum(((digits[a][j]+digits[b][j])%p)*p**j for j in range(m)) for b in range(q)] for a in range(q)]
    mul=[[0]*q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            c=[0]*(2*m-1)
            for i in range(m):
                for j in range(m):c[i+j]=(c[i+j]+digits[a][i]*digits[b][j])%p
            for k in range(2*m-2,m-1,-1):
                z=c[k]
                if z:
                    for j in range(m):c[k-m+j]=(c[k-m+j]-z*coeff[j])%p
            mul[a][b]=sum(c[j]*p**j for j in range(m))
    one=1
    def powr(a,n):
        v=one
        while n:
            if n&1:v=mul[v][a]
            a=mul[a][a];n//=2
        return v
    return q,add,mul,powr

def cycles(f):
    seen=set();c=Counter()
    for x in range(len(f)):
        if x in seen:continue
        y=x;ln=0
        while y not in seen:
            seen.add(y);y=f[y];ln+=1
        assert y==x
        c[ln]+=1
    return c

def fixed_prediction(q,Q,h,t,n,zero_trace=None):
    d=gcd(n,h)
    if t>1:return 1+(Q**d-1 if (n//d)%t==0 else 0)
    return Q**d if (zero_trace or ((n//d)%p_global==0)) else 0

def run_case(p,m,r):
    global p_global
    p_global=p
    q,add,mul,powr=field(p,m)
    g=gcd(m,r);Q=p**g;h=m//g
    s=[powr(x,p**r) for x in range(q)]
    norm=[0]*q
    for a in range(1,q):
        z=1;aa=a
        for i in range(h):
            z=mul[z][aa];aa=s[aa]
        norm[a]=z
        assert powr(z,Q-1)==1 and powr(z,Q)==z
    bynorm={z:next(t for t in divs(Q-1) if powr(z,t)==1) for z in set(norm[1:])}
    actual_byclass=Counter()
    actual_bycyc={}
    for a in range(1,q):
        base=[mul[a][s[x]] for x in range(q)]
        t=bynorm[norm[a]]
        for b in range(q):
            f=[add[v][b] for v in base]
            # The translation after h iterations detects trace-zero at A=1.
            y=0
            for _ in range(h):y=f[y]
            tr0=(y==0)
            label=('N',t) if t>1 else (('T',0) if tr0 else ('T',1))
            actual_byclass[label]+=1
            C=cycles(f)
            order=h*t if t>1 else h*(p if not tr0 else 1)
            assert all(order%d==0 for d in C)
            assert sum(d*v for d,v in C.items())==q
            predfixed={n:fixed_prediction(q,Q,h,t,n,tr0) for n in divs(order)}
            predcycle={n:sum(int(mobius(n//d))*predfixed[d] for d in divs(n))//n for n in divs(order)}
            assert all(sum(int(mobius(n//d))*predfixed[d] for d in divs(n))%n==0 for n in divs(order))
            predcycle={n:v for n,v in predcycle.items() if v}
            assert C==predcycle,(p,m,r,a,b,label,C,predcycle)
            if label in actual_bycyc: assert actual_bycyc[label]==C
            else: actual_bycyc[label]=C
    expected={('T',0):((q-1)//(Q-1))*(q//Q),('T',1):((q-1)//(Q-1))*q*(Q-1)//Q}
    for t in divs(Q-1):
        if t>1: expected[('N',t)]=q*((q-1)//(Q-1))*phi(t)
    assert actual_byclass==expected,(p,m,r,actual_byclass,expected)
    assert len(set(tuple(sorted(x.items())) for x in actual_bycyc.values()))==len(expected)
    print('CASE_OK',p,m,r,'q',q,'Q',Q,'h',h,'maps',q*(q-1),'classes',len(expected))
    return sum(actual_byclass.values())

if __name__=='__main__':
    total=0;cases=0
    for p,m,r in [(2,1,1),(2,2,1),(2,3,1),(2,4,1),(2,4,2),(3,1,1),(3,2,1),(3,2,2),(3,3,1),(5,1,1),(5,2,1),(7,1,1),(2,6,3),(3,4,2),(5,3,1)]:
        total+=run_case(p,m,r);cases+=1
    print('VERIFY_OK all_cases=',cases,'all_affine_maps=',total)
