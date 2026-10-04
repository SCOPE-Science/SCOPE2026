#!/usr/bin/env python3
from collections import Counter

def layer_sizes(q, ell, s):
    return [s*(q-1)*q**(ell-i-1) for i in range(1,ell)]

def degree_profile(q, ell, s):
    ns=layer_sizes(q,ell,s)
    deg=[]
    for i in range(1,ell):
        total=sum(ns[j-1] for j in range(ell-i,ell))
        eps=1 if 2*i>=ell else 0
        deg.append(total-eps)
    return ns,deg

def reconstruct_from_counter(C):
    ds=sorted(C)
    ell=len(ds)+1
    sizes=[C[d] for d in ds]
    if ell<3:
        raise ValueError("length-two case is intentionally non-rigid")
    qs=[]
    for a,b in zip(sizes,sizes[1:]):
        assert a%b==0
        qs.append(a//b)
    assert qs and all(q==qs[0] for q in qs)
    q=qs[0]
    assert sizes[-1]%(q-1)==0
    s=sizes[-1]//(q-1)
    return q,ell,s,sizes,ds

profiles=0
for q in [2,3,4,5,7,8,9,11,13,16]:
    for ell in range(3,9):
        for s in range(1,7):
            ns,ds=degree_profile(q,ell,s)
            assert all(ds[i]<ds[i+1] for i in range(len(ds)-1))
            C=Counter({d:n for n,d in zip(ns,ds)})
            qr,er,sr,sizes,degs=reconstruct_from_counter(C)
            assert (qr,er,sr)==(q,ell,s)
            assert sizes==ns
            profiles+=1

def zmod_graph(p,N,ell):
    mod=p**N
    step=p**ell
    I={x for x in range(mod) if x%step==0}
    V=[]
    for x in range(mod):
        if x in I:
            continue
        a=x%step
        if a!=0 and a%p==0:
            V.append(x)
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if (x*y)%step==0:
                adj[i].add(j); adj[j].add(i)
    return V,adj,len(I)

def reconstruct_actual(V,adj):
    C=Counter(len(N) for N in adj)
    return reconstruct_from_counter(C)[:3]

actual=[]
for p,N,ell in [(2,3,3),(2,4,3),(2,5,4),(3,3,3),(3,4,3),(3,4,4)]:
    V,adj,s=zmod_graph(p,N,ell)
    rec=reconstruct_actual(V,adj)
    assert rec==(p,ell,s), (p,N,ell,s,rec)
    actual.append((p,N,ell,len(V),s,rec))

V1,A1,s1=zmod_graph(3,2,2)
V2,A2,s2=zmod_graph(2,3,2)
assert len(V1)==len(V2)==2
assert all(len(N)==1 for N in A1)
assert all(len(N)==1 for N in A2)
assert (s1,s2)==(1,2)

print("VERIFY_OK")
print(f"symbolic_profiles_checked={profiles}")
for row in actual:
    print("actual_Zmod_case="+repr(row))
print("length_two_collision=Gamma_0(Z9)=Gamma_(4)(Z8)=K2")
