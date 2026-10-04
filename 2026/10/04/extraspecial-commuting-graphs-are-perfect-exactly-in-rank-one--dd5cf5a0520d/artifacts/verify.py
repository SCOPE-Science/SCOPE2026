from itertools import product
from collections import deque

def form(v,w,p):
    s=0
    for i in range(0,len(v),2):
        s += v[i]*w[i+1]-v[i+1]*w[i]
    return s%p

def nonzero_vectors(p,r):
    d=2*r
    return [v for v in product(range(p), repeat=d) if any(v)]

def quotient_graph(p,r):
    V=nonzero_vectors(p,r)
    adj={v:set() for v in V}
    for i,v in enumerate(V):
        for w in V[i+1:]:
            if form(v,w,p)==0:
                adj[v].add(w); adj[w].add(v)
    return V,adj

def components(adj):
    unseen=set(adj)
    out=[]
    while unseen:
        s=unseen.pop()
        q=[s]; C={s}
        while q:
            u=q.pop()
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v); C.add(v); q.append(v)
        out.append(C)
    return out

def group_blowup_rank1(p):
    V,adj=quotient_graph(p,1)
    # Noncentral elements are pairs (v,z), z in F_p.
    GV=[(v,z) for v in V for z in range(p)]
    gadj={x:set() for x in GV}
    for i,x in enumerate(GV):
        v,z=x
        for y in GV[i+1:]:
            w,t=y
            # commutation iff quotient vectors are orthogonal
            if form(v,w,p)==0:
                gadj[x].add(y); gadj[y].add(x)
    cs=components(gadj)
    assert len(cs)==p+1
    assert all(len(C)==p*(p-1) for C in cs)
    # Each component is complete.
    assert all(all(len(gadj[x] & C)==len(C)-1 for x in C) for C in cs)
    return sorted(len(C) for C in cs)

def c5_witness(p,r):
    assert r>=2
    # coordinates (e1,f1,e2,f2,e3,f3,...)
    d=2*r
    def vec(vals):
        a=[0]*d
        for idx,val in vals.items():
            a[idx]=val%p
        return tuple(a)
    V=[
        vec({0:1}),             # e1
        vec({2:1}),             # e2
        vec({1:1}),             # f1
        vec({1:1,3:1}),         # f1+f2
        vec({0:1,2:-1,3:1}),    # e1-e2+f2
    ]
    # target edges are cycle 0-1-2-3-4-0
    target=set()
    for i in range(5):
        a,b=i,(i+1)%5
        target.add(tuple(sorted((a,b))))
    actual=set()
    vals={}
    for i in range(5):
        for j in range(i+1,5):
            x=form(V[i],V[j],p)
            vals[(i,j)]=x
            if x==0:
                actual.add((i,j))
    assert actual==target,(p,actual,vals)
    return V,vals

for p in (2,3,5,7):
    sizes=group_blowup_rank1(p)
    V,vals=c5_witness(p,2)
    print({"p":p,"rank1_components":sizes,"rank2_C5_pairings":vals})
print("VERIFY_OK")
