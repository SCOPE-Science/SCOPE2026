#!/usr/bin/env python3
"""Exact checks of cut-rank formulas and direct small graph-state spectra."""
from itertools import combinations, product
from random import Random
import math

def rank_mod(a, p):
    if not a: return 0
    A=[list(map(lambda x:x%p,row)) for row in a]
    m=len(A); n=len(A[0]); r=0
    for j in range(n):
        t=next((i for i in range(r,m) if A[i][j]),None)
        if t is None: continue
        A[r],A[t]=A[t],A[r]
        inv=pow(A[r][j],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][j]:
                a0=A[i][j]
                A[i]=[(x-a0*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def components_and_signatures(n, edges, p):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    vis=[False]*n
    vectors=[]
    for x in range(n):
        if vis[x]: continue
        st=[x]; vis[x]=True; sign={x:1}; good=True
        while st:
            u=st.pop()
            for v in adj[u]:
                if v not in sign:
                    sign[v]=-sign[u];vis[v]=True;st.append(v)
                elif sign[v]!=-sign[u]: good=False
        if good or p==2:
            vec=[0]*n
            for v,s in sign.items():vec[v]=s%p
            vectors.append(vec)
    return vectors

def predict(n,A,B,p):
    U=components_and_signatures(n,A,p)
    V=components_and_signatures(n,B,p)
    overlap=[[sum(u[i]*v[i] for i in range(n))%p for v in V] for u in U]
    return n-len(U)-len(V)+rank_mod(overlap,p),len(U),len(V),rank_mod(overlap,p)

def direct(A,B,p):
    C=[[int(bool(set(e)&set(f))) for f in B] for e in A]
    return rank_mod(C,p)

def check(n,A,B,p):
    actual=direct(A,B,p)
    theoretical=predict(n,A,B,p)[0]
    assert actual==theoretical,(n,p,A,B,actual,theoretical)

N=0
for n in range(1,6):
    edge_list=list(combinations(range(n),2))
    for part in product((0,1,2),repeat=len(edge_list)):
        A=[e for e,s in zip(edge_list,part) if s==1]
        B=[e for e,s in zip(edge_list,part) if s==2]
        for p in (2,3,5): check(n,A,B,p);N+=1
print('exhaustive (graph, edge bipartition, prime) cases:',N)
rng=Random(911704)
for it in range(5000):
    n=rng.randrange(6,16)
    A=[];B=[]
    for e in combinations(range(n),2):
        t=rng.randrange(3)
        if t==1:A.append(e)
        if t==2:B.append(e)
    for p in (2,3,5,7):check(n,A,B,p)
print('random prime-characteristic checks:',20000)
for n in range(4,32):
    edges=list(combinations(range(n),2))
    A=[(i,i+1) for i in range(n-1)]
    aset=set(A)
    B=[e for e in edges if e not in aset]
    for p in (2,3,5,7):
        d=direct(A,B,p)
        goal=(n-2+(n%2)) if p==2 else (n-1 if n>=5 else 2)
        assert d==goal,(n,p,d,goal)
print('complete graph Hamilton-path cuts:',28*4)

# direct state construction and partial traces, independent of rank-based spectrum
try:
    import numpy as np
except ImportError:
    print('numpy unavailable: optional direct-state checks skipped')
else:
    cases=[(4,[(0,1),(1,2),(2,3),(3,0)],2),
           (4,[(0,1),(0,2),(0,3),(1,2),(1,3)],3),
           (5,[(0,1),(1,2),(2,3),(3,4),(4,0)],2),
           (5,[(0,1),(1,2),(2,3),(3,4),(0,2),(1,4)],3),
           (4,list(combinations(range(4),2)),3)]
    direct_count=0; max_err=0.
    for n,edges,na in cases:
        A=edges[:na];B=edges[na:]
        M=len(edges)
        for p in (2,3):
            if p**M>20000:continue
            psi=np.empty((p**na,p**(M-na)),dtype=complex)
            omega=np.exp(2j*np.pi/p)
            for ai in range(p**na):
                x=[];q=ai
                for i in range(na):x.append(q%p);q//=p
                for bi in range(p**(M-na)):
                    z=x[:];q=bi
                    for i in range(M-na):z.append(q%p);q//=p
                    exponent=sum(z[i]*z[j] for i in range(M) for j in range(i+1,M) if len(set(edges[i])&set(edges[j]))==1)
                    psi[ai,bi]=omega**(exponent%p)/math.sqrt(p**M)
            eig=np.linalg.eigvalsh(psi@psi.conj().T)
            r=predict(n,A,B,p)[0]
            expect=np.array([0.]*(p**na-p**r)+[p**(-r)]*(p**r))
            err=float(np.max(abs(eig-expect)))
            max_err=max(err,max_err)
            assert err<2e-12,(n,p,err)
            direct_count+=1
    print('independent direct reduced-state spectra:',direct_count,'max_abs_error:',format(max_err,'.3g'))
