#!/usr/bin/env python3
"""Direct finite checks of commuting retractions of generalized dihedral groups.
Requires Python 3 standard library only. Run: python verify_dihedral.py
"""
import itertools
import math


def matmul(A,B,n,p):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%p for i in range(n) for j in range(n))

def mv(A,v,n,p):
    return tuple(sum(A[i*n+j]*v[j] for j in range(n))%p for i in range(n))

def add(u,v,p):return tuple((a+b)%p for a,b in zip(u,v))

def negate(u,p):return tuple((-a)%p for a in u)

def gauss(n,r,p):
    if r<0 or r>n:return 0
    k=min(r,n-r)
    numer=denom=1
    for i in range(k):
        numer*=p**(n-i)-1
        denom*=p**(k-i)-1
    return numer//denom

def projection_total(n,p):
    return sum(gauss(n,r,p)*p**(r*(n-r)) for r in range(n+1))

def image_rank(A,n,p):
    m=[list(A[i*n:(i+1)*n]) for i in range(n)]
    rank=0
    for j in range(n):
        k=next((t for t in range(rank,n) if m[t][j]%p),None)
        if k is None:continue
        m[k],m[rank]=m[rank],m[k]
        inverse=pow(m[rank][j],-1,p)
        m[rank]=[(x*inverse)%p for x in m[rank]]
        for i in range(n):
            if i==rank:continue
            scalar=m[i][j]
            m[i]=[(m[i][c]-scalar*m[rank][c])%p for c in range(n)]
        rank+=1
    return rank

def gl(n,p):return math.prod(p**n-p**j for j in range(n))

def all_retractions(n,p):
    zero=(0,)*n
    vectors=list(itertools.product(range(p),repeat=n))
    matrices=list(itertools.product(range(p),repeat=n*n))
    I=tuple(1 if i==j else 0 for i in range(n) for j in range(n))
    projectors=[(M,image_rank(M,n,p)) for M in matrices if matmul(M,M,n,p)==M]
    maps=[(None,None,-1)]
    for M,rank in projectors:
        for u in vectors:
            if mv(M,u,n,p)==zero:maps.append((M,u,rank))
    expected=2+sum(gauss(n,r,p)*p**((r+1)*(n-r)) for r in range(n))
    assert len(maps)==expected, (n,p,len(maps),expected)
    assert sum(M==I for M,u,r in maps if M is not None)==1
    counts={r:sum(s==r for M,u,s in maps) for r in range(n+1)}
    assert counts=={r:gauss(n,r,p)*p**((r+1)*(n-r)) for r in range(n+1)}
    return maps,vectors

def group_mul(g,h,p):
    x,e=g;y,f=h
    return (add(x,y if e==0 else negate(y,p),p),(e+f)%2)

def eval_map(F,g,p):
    A,u,_=F;x,e=g
    if A is None:return ((0,)*len(x),0)
    return (add(mv(A,x,len(x),p),u if e else ((0,)*len(x)),p),e)

def affine_commute(F,H,n,p):
    if F[0] is None or H[0] is None:return True
    A,u,_=F;B,v,_=H
    return matmul(A,B,n,p)==matmul(B,A,n,p) and add(u,mv(A,v,n,p),p)==add(v,mv(B,u,n,p),p)

def connected_maximal_cliques(adjs):
    out=[]
    def search(R,P,X):
        if not P and not X:
            out.append(frozenset(R));return
        pivot=max(P|X,key=lambda v: len(P&adjs[v])) if P or X else None
        for v in list(P-(adjs[pivot] if pivot is not None else set())):
            search(R|{v},P&adjs[v],X&adjs[v]);P.remove(v);X.add(v)
    search(set(),set(range(len(adjs))),set())
    return out

def exercise(n,p,check_cliques):
    F,V=all_retractions(n,p)
    C=[]
    for M,u,r in F:
        if M is None:C.append(len(F));continue
        Ar=sum(gauss(r,i,p)*p**(i*(r-i)+r-i) for i in range(r+1))
        C.append(1+Ar*projection_total(n-r,p))
    adj=[set() for _ in F]
    actual=[0]*len(F)
    for i in range(len(F)):
        for j in range(i,len(F)):
            comm=affine_commute(F[i],F[j],n,p)
            if comm:
                actual[i]+=1
                if i!=j:
                    actual[j]+=1
                    adj[i].add(j);adj[j].add(i)
    assert actual==C, (n,p,[(i,a,b) for i,(a,b) in enumerate(zip(actual,C)) if a!=b][:5])
    assert sum(actual)==len(F)+2*sum(len(x) for x in adj)//2
    if check_cliques:
        cliques=connected_maximal_cliques(adj)
        target=p**n*gl(n,p)//((p-1)**n*math.factorial(n))
        assert len(cliques)==target,(n,p,len(cliques),target)
        assert {len(clique) for clique in cliques}=={2**n+1},(n,p, {len(c) for c in cliques})
    if n==2 and p==3:
        el=[(v,e) for v in V for e in (0,1)]
        for f in F:
            for g in el:
                assert eval_map(f,eval_map(f,g,p),p)==eval_map(f,g,p)
                for h in el:
                    assert eval_map(f,group_mul(g,h,p),p)==group_mul(eval_map(f,g,p),eval_map(f,h,p),p)
        for i,f in enumerate(F):
            for j,h in enumerate(F):
                comm=all(eval_map(f,eval_map(h,g,p),p)==eval_map(h,eval_map(f,g,p),p) for g in el)
                assert comm==(j==i or j in adj[i]),(i,j)
    print('PASS',p,n,'idempotents',len(F),'commuting ordered pairs',sum(actual),'maximal cliques checked',check_cliques)

if __name__=='__main__':
    for args in [(1,3,True),(2,3,True),(2,5,True),(3,3,False)]:exercise(*args)
    print('VERIFY_OK')
