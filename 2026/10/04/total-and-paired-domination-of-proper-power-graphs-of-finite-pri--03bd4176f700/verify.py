#!/usr/bin/env python3
from itertools import combinations, product

# Finite groups are represented by an element list, identity, and multiplication.
def cyclic_product(moduli):
    elems=list(product(*[range(n) for n in moduli]))
    e=tuple(0 for _ in moduli)
    def mul(x,y): return tuple((a+b)%n for a,b,n in zip(x,y,moduli))
    return elems,e,mul

def dihedral8():
    elems=[(a,b) for a in range(4) for b in (0,1)]
    e=(0,0)
    def mul(x,y):
        a,b=x; c,d=y
        return ((a + (-c if b else c))%4,(b+d)%2)
    return elems,e,mul

def quaternion8():
    # element=(sign,basis), basis 0=1,1=i,2=j,3=k
    elems=[(s,b) for s in (1,-1) for b in range(4)]
    e=(1,0)
    # positive basis products: value = sign * basis
    tab={
      (0,0):(1,0),(0,1):(1,1),(0,2):(1,2),(0,3):(1,3),
      (1,0):(1,1),(1,1):(-1,0),(1,2):(1,3),(1,3):(-1,2),
      (2,0):(1,2),(2,1):(-1,3),(2,2):(-1,0),(2,3):(1,1),
      (3,0):(1,3),(3,1):(1,2),(3,2):(-1,1),(3,3):(-1,0),
    }
    def mul(x,y):
        sx,bx=x; sy,by=y
        s,b=tab[(bx,by)]
        return (sx*sy*s,b)
    return elems,e,mul

def powers(x,e,mul):
    out=[]; y=e
    while True:
        y=mul(y,x)
        if y==e: break
        out.append(y)
    return out

def order(x,e,mul): return len(powers(x,e,mul))+1

def graph(group):
    elems,e,mul=group
    V=[x for x in elems if x!=e]
    cyc={x:set(powers(x,e,mul))|{e} for x in elems}
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if y in cyc[x] or x in cyc[y]:
                adj[i].add(j); adj[j].add(i)
    return V,adj,cyc

def comps(adj):
    seen=set(); out=[]
    for v in range(len(adj)):
        if v in seen: continue
        st=[v]; seen.add(v); C=[]
        while st:
            u=st.pop(); C.append(u)
            for w in adj[u]:
                if w not in seen: seen.add(w); st.append(w)
        out.append(C)
    return out

def total_dom(S,adj):
    S=set(S); return all(adj[v]&S for v in range(len(adj)))

def perfect_matching(S,adj):
    S=set(S)
    if not S: return True
    if len(S)%2: return False
    v=next(iter(S))
    for u in list(adj[v]&S):
        if perfect_matching(S-{v,u},adj): return True
    return False

def minima(adj):
    if any(not N for N in adj): return None,None
    N=len(adj); gt=gp=None
    for k in range(2,N+1):
        if gt is None:
            for S in combinations(range(N),k):
                if total_dom(S,adj): gt=k; break
        if gp is None and k%2==0:
            for S in combinations(range(N),k):
                if total_dom(S,adj) and perfect_matching(S,adj): gp=k; break
        if gt is not None and gp is not None: return gt,gp
    return gt,gp

def subgroup_p(x,p,e,mul):
    H={e}; y=e
    for _ in range(p-1):
        y=mul(y,x); H.add(y)
    return frozenset(H)

def analyze(name,group,p,exhaustive=True):
    elems,e,mul=group
    V,adj,cyc=graph(group)
    ords={x:order(x,e,mul) for x in elems}
    Hp={subgroup_p(x,p,e,mul) for x in V if ords[x]==p}
    t=len(Hp)
    Cs=comps(adj)
    assert len(Cs)==t, (name,len(Cs),t)
    # Each component has exactly one order-p subgroup and every nonidentity
    # element of it is universal within that component.
    for C in Cs:
        cverts=[V[i] for i in C]
        hs={subgroup_p(x,p,e,mul) for x in cverts if ords[x]==p}
        assert len(hs)==1, (name,hs)
        H=next(iter(hs))
        for h in H-{e}:
            hi=V.index(h)
            assert all(j==hi or j in adj[hi] for j in C)
    if p%2:
        expect=2*t
        exists=True
    else:
        invol=[x for x in V if ords[x]==2]
        square_all=all(any(mul(y,y)==h for y in elems) for h in invol)
        exists=square_all
        expect=2*t if exists else None
        assert (not any(not adj[i] for i,x in enumerate(V) if ords[x]==2))==square_all
    if exhaustive and len(V)<=15:
        gt,gp=minima(adj)
        assert gt==expect and gp==expect, (name,gt,gp,expect)
    else:
        gt=gp='not_exhaustive'
    return name,len(V),t,exists,expect,gt,gp

cases=[
 ('C3',cyclic_product([3]),3),
 ('C9',cyclic_product([9]),3),
 ('C3xC3',cyclic_product([3,3]),3),
 ('C4',cyclic_product([4]),2),
 ('C8',cyclic_product([8]),2),
 ('C4xC4',cyclic_product([4,4]),2),
 ('C2xC4',cyclic_product([2,4]),2),
 ('C2xC2',cyclic_product([2,2]),2),
 ('D8',dihedral8(),2),
 ('Q8',quaternion8(),2),
]
rows=[analyze(name,g,p,True) for name,g,p in cases]
# A larger odd-p profile is checked structurally without subset enumeration.
rows.append(analyze('C9xC3',cyclic_product([9,3]),3,False))
print('VERIFY_OK')
for row in rows:
    print('group=%s vertices=%s order_p_subgroups=%s exists=%s predicted=%s gamma_t=%s gamma_pr=%s'%row)
