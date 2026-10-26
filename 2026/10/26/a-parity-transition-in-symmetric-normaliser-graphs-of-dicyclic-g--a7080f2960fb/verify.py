#!/usr/bin/env python3
"""Exact adjacency and Laplacian checks for dicyclic symmetric-normaliser graphs."""
from fractions import Fraction

def product(x,y,m):
    i,e=x; j,f=y
    return ((i+(-1 if e else 1)*j+(m if e and f else 0))%(2*m),(e+f)%2)

def inv(x,m):
    i,e=x
    return ((-i if not e else i+m)%(2*m),e)

def subgroup(x,m):
    unit=(0,0); current=unit; s=set()
    while current not in s:
        s.add(current); current=product(current,x,m)
    assert current==unit
    return s

def graph(m):
    vs=[(i,e) for e in range(2) for i in range(2*m)]
    subs={v:subgroup(v,m) for v in vs}
    adj={v:set() for v in vs}
    for ai,x in enumerate(vs):
        for y in vs[ai+1:]:
            xyx=product(product(x,y,m),inv(x,m),m)
            yxy=product(product(y,x,m),inv(y,m),m)
            if xyx in subs[y] and yxy in subs[x]:
                adj[x].add(y);adj[y].add(x)
    return vs,adj

def predicted(x,y,m):
    i,e=x;j,f=y
    if e==f==0: return True
    if e!=f:
        ri=i if not e else j
        return (2*ri)%(2*m) in (0,m%(2*m))
    return (2*(i-j))%(2*m) in (0,m%(2*m))

def verify(m):
    vs,adj=graph(m)
    for x in vs:
        for y in vs:
            if x!=y: assert (y in adj[x])==predicted(x,y,m),(m,x,y)
    u=2 if m%2 else 4
    if m==2: u=8
    if m==1: u=4
    universal=[x for x in vs if len(adj[x])==4*m-1]
    assert len(universal)==u, (m,len(universal),u)
    nonuniversal=set(vs)-set(universal)
    components=[]
    while nonuniversal:
        root=nonuniversal.pop(); st=[root];cc={root}
        while st:
            z=st.pop()
            for w in adj[z]&nonuniversal:
                nonuniversal.remove(w);cc.add(w);st.append(w)
        components.append(cc)
    observed=sorted(map(len,components))
    if m==1: target=[]
    elif m==2: target=[]
    elif m%2: target=sorted([2*m-2]+[2]*m)
    else: target=sorted([2*m-4]+[4]*(m//2))
    assert observed==target,(m,observed,target)
    for comp in components:
        assert all(len(adj[z]&comp)==len(comp)-1 for z in comp)
    for v in universal:
        assert len(adj[v])==len(vs)-1
    if 2<=m<=6:
        import sympy as sp
        A=sp.zeros(len(vs))
        for k,x in enumerate(vs):
            A[k,k]=len(adj[x]);
            for j,y in enumerate(vs):
                if y in adj[x]:A[k,j]=-1
        eig=A.eigenvals()
        if m==2: expected={sp.Integer(0):1,sp.Integer(8):7};tau=8**6
        elif m%2:
            expected={sp.Integer(0):1,sp.Integer(4*m):2,sp.Integer(2*m):2*m-3,sp.Integer(4):m,sp.Integer(2):m}
            tau=(4*m)*(2*m)**(2*m-3)*8**m
        else:
            expected={sp.Integer(0):1,sp.Integer(4*m):4,sp.Integer(2*m):2*m-5,sp.Integer(8):3*m//2,sp.Integer(4):m//2}
            tau=(4*m)**3*(2*m)**(2*m-5)*8**(3*m//2)*4**(m//2)
        reduced={k:v for k,v in expected.items() if v>0}
        # Collisions of eigenvalues at small m are added by collecting multiplicities.
        coll={}
        for k,v in reduced.items():coll[k]=coll.get(k,0)+v
        # Correct collisions for parameters where 2m = 8 etc.
        if m==4: coll={sp.Integer(0):1,sp.Integer(16):4,sp.Integer(8):9,sp.Integer(4):2}
        assert eig==coll, (m,eig,coll)
        assert A[:len(vs)-1,:len(vs)-1].det()==tau,(m,'spanning tree')
    return len(vs),len(components)+1

if __name__=='__main__':
    for m in range(2,13):
        v,c=verify(m)
        print('m',m,'vertices',v,'cliques_after_removing_universals',c-1)
    print('VERIFY_OK')
