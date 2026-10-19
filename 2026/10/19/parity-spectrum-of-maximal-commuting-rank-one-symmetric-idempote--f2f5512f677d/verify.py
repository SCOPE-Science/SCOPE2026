"""Standalone finite-field verifier for rank-one symmetric idempotent clique formulas.
Runs with standard Python only. Usage: python verify.py
"""
from itertools import product
from math import factorial

def mul(a,b,q):
    irr={2:0b11,4:0b111,8:0b1011}[q]
    z=0; xx=a; yy=b
    while yy:
        if yy&1: z ^= xx
        yy>>=1; xx<<=1
        if xx&q: xx^=irr
    return z

def dot(u,v,q):
    z=0
    for a,b in zip(u,v): z ^= mul(a,b,q)
    return z

def sp_order(d,q):
    assert d>=0 and d%2==0
    m=d//2
    z=q**(m*m)
    for j in range(1,m+1):z*=q**(2*j)-1
    return z

def iso_order(d,q):
    assert d>=1
    if d%2: return sp_order(d-1,q)
    return q**(d-1)*sp_order(d-2,q)

def expected(n,q):
    g=iso_order(n,q)
    total=[]; terminal=[]
    for k in range(1,n+1):
        d=n-k
        t=(g//sp_order(d,q)//factorial(k)) if d%2==0 else 0
        nt=(g//iso_order(d,q)//factorial(k)) if d>0 else 0
        assert (g%sp_order(d,q)==0) if d%2==0 else True
        total.append(t+nt)
        terminal.append(t)
    return total,terminal

def check(n,q,check_product=False):
    units=[v for v in product(range(q),repeat=n) if __import__('functools').reduce(lambda a,b:a^b,v,0)==1]
    assert len(units)==q**(n-1)
    N=len(units)
    adj=[set() for i in range(N)]
    for i in range(N):
        assert dot(units[i],units[i],q)==1
        for j in range(i+1,N):
            if dot(units[i],units[j],q)==0:
                adj[i].add(j);adj[j].add(i)
            if check_product:
                v=units[i];w=units[j]
                p=[[mul(v[a],v[b],q) for b in range(n)] for a in range(n)]
                r=[[mul(w[a],w[b],q) for b in range(n)] for a in range(n)]
                pr=[[__import__('functools').reduce(lambda t,h:t^h,(mul(p[a][h],r[h][b],q) for h in range(n)),0) for b in range(n)] for a in range(n)]
                rp=[[__import__('functools').reduce(lambda t,h:t^h,(mul(r[a][h],p[h][b],q) for h in range(n)),0) for b in range(n)] for a in range(n)]
                assert (pr==rp)==(j in adj[i])
                if j in adj[i]:assert all(z==0 for row in pr for z in row)
    bysize=[0]*(n+1); maximal=[0]*(n+1)
    bysize[0]=1
    omega=(1,)*n
    def recurse(S,candidates):
        k=len(S)
        if k: bysize[k]+=1
        # orthogonal complement alternating iff omega is in linear span of S; alternatively no extension.
        possible=set.intersection(*(adj[i] for i in S)) if S else set(range(N))
        if S and not possible:
            maximal[k]+=1
        for ii,i in enumerate(candidates):
            recurse(S+(i,),[j for j in candidates[ii+1:] if j in adj[i]])
    recurse((),list(range(N)))
    formula,term=expected(n,q)
    assert bysize[1:]==formula,(n,q,bysize,formula)
    assert maximal[1:]==term,(n,q,maximal,term)
    print(f'CHECK_OK q={q} n={n} vertices={N} clique_coeff={bysize} maximal={maximal}')

if __name__=='__main__':
    for q,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(4,2),(4,3),(4,4),(8,2),(8,3)]:
        check(n,q,check_product=(n<=4 and q<=4))
    print('VERIFY_OK_SYMMETRIC_IDEMPOTENT_PARITY_CLIQUES')
