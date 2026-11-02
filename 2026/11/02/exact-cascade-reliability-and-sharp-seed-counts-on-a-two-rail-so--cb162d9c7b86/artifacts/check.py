#!/usr/bin/env python3
"""Independent finite checks and polynomial algebra for a two-rail threshold-two cascade.

Requires Python >=3.9 and sympy for the exact matrix resolvent step.
Run from any directory: python artifacts/check.py
"""
from collections import Counter
from itertools import product
from math import comb
import sympy as S

STATES = ((0,0),(1,0),(1,1),(2,0),(2,2),(3,0),(3,3))

def pop(k):
    return k.bit_count()

def transfer_coeffs(N):
    # Complement-weight polynomial for all successful initial adopter sets.
    cur = {(0,0): {0:1}, (1,1):{1:1}, (2,2):{1:1}}
    out = {}
    for n in range(1,N+1):
        c=Counter()
        for (v,r),poly in cur.items():
            if r==0 and v!=3:
                for d,k in poly.items():c[d]+=k
        out[n]=dict(c)
        new={}
        for (v,r),poly in cur.items():
            for w in range(4):
                if v==w==3: continue
                nr=w if r&w else 0
                p=new.setdefault((w,nr),Counter())
                for d,k in poly.items(): p[d+pop(w)]+=k
        cur=new
    return out

def graph_adj(n):
    adj=[0]*(2*n)
    for j in range(n):
        a,b=2*j,2*j+1
        adj[a]|=1<<b;adj[b]|=1<<a
        if j+1<n:
            for r in (0,1):
                u,w=2*j+r,2*(j+1)+r
                adj[u]|=1<<w;adj[w]|=1<<u
    return adj

def contagious(seed,adj):
    whole=(1<<len(adj))-1
    while seed!=whole:
        nxt=seed
        for k,nb in enumerate(adj):
            if not (seed>>k)&1 and pop(nb&seed)>=2: nxt|=1<<k
        if nxt==seed:break
        seed=nxt
    return seed==whole

def brute(n):
    a=graph_adj(n); result=Counter()
    for mask in range(1<<(2*n)):
        if contagious(mask,a):result[2*n-pop(mask)]+=1
    return dict(result)

def obstruction(n,seed):
    # Independently reject stable vacant squares, end-rungs, or left-right crossings.
    v=[sum((1<<row) for row in (0,1) if not (seed>>(2*j+row))&1) for j in range(n)]
    if v[0]==3 or v[-1]==3:return True
    if any(v[j]==v[j+1]==3 for j in range(n-1)):return True
    r=v[0]
    for w in v[1:]:r=w if r&w else 0
    return r!=0

def finite():
    tr=transfer_coeffs(25);tested=0
    for n in range(2,10):
        expected=tr[n];actual=brute(n)
        assert actual==expected,(n,actual,expected)
        for mask in range(1<<(2*n)):
            assert contagious(mask,graph_adj(n)) != obstruction(n,mask),(n,mask)
            tested+=1
    for n in range(2,26):
        p=tr[n]; N=n//2
        minseeds= n//2+1 if n%2==0 else (n+3)//2
        assert 2*n-max(p)==minseeds,(n,p)
        coefficient=p[max(p)]
        if n%2==0:
            assert coefficient==N*(2**N)
        else:
            assert coefficient==(N+1)*(3*N+2)*2**(N-1)
    return tested,tr

def symbolic():
    v,z=S.symbols('v z')
    idx={state:i for i,state in enumerate(STATES)}
    M=S.zeros(7)
    for i,(old,r) in enumerate(STATES):
        for w in range(4):
            if old==w==3:continue
            reach=w if r&w else 0
            M[i,idx[(w,reach)]]+=v**pop(w)
    i=S.zeros(1,7);i[0,0]=1;i[0,idx[(1,1)]]=v;i[0,idx[(2,2)]]=v
    f=S.zeros(7,1)
    for j,(w,r) in enumerate(STATES):
        if r==0 and w!=3:f[j,0]=1
    target=z*(1+(v+2*v*v)*z)/((1-v*z-2*v**3*z*z)*(1-(1+2*v)*z-(v*v+2*v**3)*z*z))
    # Exact resolvent identity, over Q[v,z]; not finite interpolation.
    got=S.cancel(z*(i*(S.eye(7)-z*M).inv()*f)[0]);assert S.cancel(got-target)==0
    at_one=S.factor(target.subs(v,1));l=(3+S.sqrt(21))/2
    assert S.simplify(S.limit((1-l*z)*at_one,z,1/l)-S.sqrt(21)/7)==0
    return str(S.factor(got))

if __name__=='__main__':
    count,tr=finite()
    algebra=symbolic()
    print('INDEPENDENT_FINITE_CONFIGURATIONS',count)
    print('TOTALS_N_2_TO_9',[sum(tr[n].values()) for n in range(2,10)])
    print('SYMBOLIC_RESOLVENT_IDENTITY_PASS',algebra)
    print('MINIMAL_SEED_COUNTS_N_2_TO_25_PASS')
    print('DOMINANT_POLE_AND_COEFFICIENT_PASS')
    print('VERIFY_OK')
