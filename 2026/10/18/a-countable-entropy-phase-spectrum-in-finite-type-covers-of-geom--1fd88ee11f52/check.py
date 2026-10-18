#!/usr/bin/env python3
"""Numerical and combinatorial checks for geometric-return S-gap shifts.
Requires only Python's standard library.
"""
from math import log

def powers(b,cap):
    out=[];v=1
    while v<=cap:
        out.append(v);v*=b
    return out

def series(root,b,upto=512):
    total=0.; k=1
    while k<=upto:
        term=root**(-k)
        total+=term
        if term<1e-17:break
        k*=b
    return total

def root(b,n=None):
    p=powers(b,n-1) if n else None
    def F(x):
        if n is None:return series(x,b)
        return sum(x**(-r) for r in p)+x**(-n)/(1-1/x)
    lo=1.00000001; hi=2.00000001
    assert F(lo)>1 and F(hi)<1 or abs(F(hi)-1)<1e-10
    for _ in range(100):
        md=(lo+hi)/2
        if F(md)>1:lo=md
        else:hi=md
    return (lo+hi)/2

def adjacency(b,n):
    M=[[0]*n for _ in range(n)]
    allowed=set(powers(b,n))
    for j in range(n):
        M[j][min(j+1,n-1)]+=1
        if j==n-1 or j+1 in allowed:M[j][0]+=1
    return M

def automaton_language(b,n,t):
    allowed=set(powers(b,n))
    out=set()
    for start in range(n):
        states={(start,'')}
        for _ in range(t):
            nxt=set()
            for j,w in states:
                nxt.add((min(j+1,n-1),w+'0'))
                if j==n-1 or j+1 in allowed:
                    nxt.add((0,w+'1'))
            states=nxt
        out.update(w for j,w in states)
    return out

def raw_language(b,n,t):
    p=set(powers(b,t+2))
    out=set()
    for x in range(1<<t):
        s=f'{x:0{t}b}'
        if all((k+1 in p) or (k+2>n) for k in range(t-1) if '1'+'0'*k+'1' in s):
            out.add(s)
    return out

def next_power(b,n):
    q=1
    while q<n:q*=b
    return q

def check():
    cases=0
    for b in (2,3,4,5):
        lam=root(b)
        S=sum(p*lam**(-p) for p in powers(b,2048) if p*lam**(-p)>1e-17)
        assert 1<lam<2 and S>0
        for n in range(1,25):
            ln=root(b,n)
            M=adjacency(b,n)
            # Perron eigen-equation from right eigenvector approximated by Collatz bounds.
            v=[1.]*n
            for _ in range(1000):
                w=[sum(M[i][j]*v[j] for j in range(n)) for i in range(n)]
                sc=max(w);w=[x/sc for x in w]
                if max(abs(a-c) for a,c in zip(v,w))<1e-14:break
                v=w
            ratios=[sum(M[i][j]*v[j] for j in range(n))/v[i] for i in range(n)]
            assert min(ratios)-1e-7 <= ln <= max(ratios)+1e-7,(b,n,ln,min(ratios),max(ratios))
            if n<=9:
                for t in range(1,9):
                    assert automaton_language(b,n,t)==raw_language(b,n,t),(b,n,t)
            q=next_power(b,n)
            predicted=(1/(1-1/lam)-lam**(-(q-n)))/S
            scaled=lam**n*(log(ln)-log(lam))
            if n>=12:
                # Uniform Taylor asymptotics permit an n*lam^{-n} discrepancy.
                assert abs(scaled-predicted)<50*n*lam**(-n),(b,n,scaled,predicted)
            cases+=1
        print('base',b,'lambda',format(lam,'.14f'),'S',format(S,'.14f'),
              'scaled limits t=0,1,infty',*[round((1/(1-1/lam)-lam**(-t))/S,12) for t in (0,1)],round(1/((1-1/lam)*S),12))
    print('PASS',cases,'automata/root cases and exact short-word cases')
if __name__=='__main__':check()
