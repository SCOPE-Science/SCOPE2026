#!/usr/bin/env python3
"""Independent finite-field subgroup and maximal-chain checks for a theorem on c-normal flags."""
from itertools import product
from math import comb, prod, factorial

def matvec(T,x,p):
    return tuple(sum(a*b for a,b in zip(row,x))%p for row in T)

def matmul(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(A)))%p for j in range(len(A))) for i in range(len(A)))

def eye(d):return tuple(tuple(int(i==j) for j in range(d)) for i in range(d))

def order(T,p):
    A=eye(len(T)); k=0
    while True:
        k+=1;A=matmul(A,T,p)
        if A==eye(len(T)):return k
        assert k<=1000

def all_linear_subspaces(p,d):
    vecs=list(product(range(p), repeat=d)); z=(0,)*d
    def span_basis(basis):
        s={z}
        for v in basis:
            s={tuple((u[i]+t*v[i])%p for i in range(d)) for u in s for t in range(p)}
        return frozenset(s)
    sub={frozenset({z})};queue=list(sub)
    while queue:
        s=queue.pop()
        for v in vecs:
            if v not in s:
                t=frozenset(tuple((w[i]+a*v[i])%p for i in range(d)) for w in s for a in range(p))
                if t not in sub:sub.add(t);queue.append(t)
    return sorted(sub,key=lambda v:(len(v),sorted(v)))

def flags(subs,p,d):
    bydim={k:[x for x in subs if len(x)==p**k] for k in range(d+1)}
    out=[]
    def rec(chain):
        if len(chain)==d+1:out.append(tuple(chain));return
        for nxt in bydim[len(chain)]:
            if chain[-1]<=nxt:rec(chain+[nxt])
    rec([bydim[0][0]])
    return out

def gaussian(d,u,p):
    a=prod(p**(d-i)-1 for i in range(u));b=prod(p**(u-i)-1 for i in range(u))
    return a//b

def fullflags(n,p):return prod((p**k-1)//(p-1) for k in range(1,n+1))

def eigendims(T,p):
    d=len(T);X=list(product(range(p),repeat=d));dims=[]
    for v in range(2,p):
        E=[x for x in X if matvec(T,x,p)==tuple(v*y%p for y in x)]
        z=0
        while p**(z+1)<=len(E):z+=1
        if z:dims.append((v,z))
    return dims

def theoretical(T,p):
    d=len(T);X=list(product(range(p), repeat=d))
    U={tuple((matvec(T,v,p)[i]-v[i])%p for i in range(d)) for v in X}
    u=0
    while p**(u+1)<=len(U):u+=1
    f=d-u;dims=eigendims(T,p)
    if sum(n for lam,n in dims)!=u:return 0
    inv=factorial(u)*prod(fullflags(n,p) for lam,n in dims)//prod(factorial(n) for lam,n in dims)
    return inv*fullflags(f,p)*gaussian(d,u,p)

def group_cnormal_for_small(T,p,subs,limit=20):
    d=len(T);m=order(T,p);vectors=list(product(range(p),repeat=d));elements=[(v,k) for v in vectors for k in range(m)]
    if len(elements)>limit:return None
    zz=(0,)*d;zero=(zz,0)
    powers=[eye(d)]
    for _ in range(1,m):powers.append(matmul(powers[-1],T,p))
    def mul(a,b):
        v,k=a;w,l=b;tw=matvec(powers[k],w,p)
        return (tuple((v[i]+tw[i])%p for i in range(d)),(k+l)%m)
    def inverse(a):
        v,k=a;ik=(-k)%m;tw=matvec(powers[ik],v,p)
        return (tuple(-x%p for x in tw),ik)
    def closure(gens):
        S={zero}; todo=[zero]
        gens=list(gens)+[inverse(g) for g in gens]
        while todo:
            a=todo.pop()
            for b in gens:
                c=mul(a,b)
                if c not in S:S.add(c);todo.append(c)
        return frozenset(S)
    subgroups={frozenset({zero})};queue=list(subgroups)
    while queue:
        H=queue.pop()
        for g in elements:
            if g not in H:
                K=closure(list(H)+[g]);
                if K not in subgroups:subgroups.add(K);queue.append(K)
    normal=[K for K in subgroups if all(mul(mul(g,k),inverse(g)) in K for g in elements for k in K)]
    def cnormal(W):
        H=frozenset((v,0) for v in W)
        core=frozenset(h for h in H if all(mul(mul(g,h),inverse(g)) in H for g in elements))
        for N in normal:
            if H & N <=core and len(H)*len(N)//len(H&N)==len(elements):return True
        return False
    return {W:cnormal(W) for W in subs},len(subgroups),len(normal)

cases=[
  ('C2 trivial',2, ((1,0),(0,1))),
  ('C2 irreducible C3',2,((0,1),(1,1))),
  ('C3 one fixed one -1',3,((1,0),(0,2))),
  ('C3 scalar -1',3,((2,0),(0,2))),
  ('C3 identity',3,((1,0),(0,1))),
  ('C3 dim3 mixed',3,((1,0,0),(0,2,0),(0,0,2))),
  ('C5 dim3 two moving eigenspaces',5,((2,0,0),(0,3,0),(0,0,1))),
  ('C5 dim3 repeated eigenvalue',5,((2,0,0),(0,2,0),(0,0,1))),
  ('C2 dim3 one trivial plus irreducible',2,((1,0,0),(0,0,1),(0,1,1))),
]
for label,p,T in cases:
    d=len(T);sub=all_linear_subspaces(p,d);Fs=flags(sub,p,d)
    X=list(product(range(p),repeat=d))
    U=frozenset(tuple((matvec(T,v,p)[i]-v[i])%p for i in range(d)) for v in X)
    allowed={W:(frozenset(W&U)==frozenset(matvec(T,x,p) for x in W&U)) for W in sub}
    measured=sum(all(allowed[W] for W in f) for f in Fs)
    expected=theoretical(T,p)
    brute=group_cnormal_for_small(T,p,sub)
    if brute is not None:
        independent,groups,normals=brute
        assert independent==allowed, f'c-normal subgroup lemma failed: {label}'
    assert measured==expected,(label,measured,expected)
    print(f'{label}: p={p}, d={d}, |C_m|={order(T,p)}, subspaces={len(sub)}, total_flags={len(Fs)}, cnormal_flags={measured}, formula={expected}, brute_group={brute is not None}')
print('VERIFY_OK')
# Additional non-cyclic complement tests: the commuting diagonal generators
# generate Klein-four (p=3) and C4 x C4 (p=5) actions.
def multiaction_count(generators,p):
    d=len(generators[0]);subs=all_linear_subspaces(p,d);Fs=flags(subs,p,d)
    vectors=list(product(range(p),repeat=d));z=(0,)*d
    U=frozenset({z})
    # [V,H] is the sum of the spans of images (h-I)V of the generators.
    delta=[tuple((matvec(g,v,p)[i]-v[i])%p for i in range(d)) for g in generators for v in vectors]
    U=frozenset({z})
    for vec in delta:
        U=frozenset(tuple((w[i]+a*vec[i])%p for i in range(d)) for w in U for a in range(p))
    allow={W: all(frozenset(matvec(g,x,p) for x in W&U)==W&U for g in generators) for W in subs}
    empirical=sum(all(allow[W] for W in F) for F in Fs)
    return empirical,len(Fs),len(U)
for label,p,gens,expected in [
 ('Klein action on 2 coordinates',3,[((2,0),(0,1)),((1,0),(0,2))],2),
 ('Klein action + 1 fixed coordinate',3,[((2,0,0),(0,1,0),(0,0,1)),((1,0,0),(0,2,0),(0,0,1))],26),
 ('C4 x C4 diagonal action + 1 fixed',5,[((2,0,0),(0,1,0),(0,0,1)),((1,0,0),(0,3,0),(0,0,1))],62),
]:
    count,total,usize=multiaction_count(gens,p)
    assert count==expected,(label,count,expected)
    print(f'{label}: cnormal_flags={count}, total_flags={total}, |[V,H]|={usize}')
print('MULTI_VERIFY_OK')
