#!/usr/bin/env python3
"""Independent finite-field census for natural-basis lines and algebra automorphisms.
All computations use modular arithmetic, never a search over prospective results.
"""
from itertools import product

def run(q):
    S=range(q)
    def dot(v,w,a,b): return (a*v[0]*w[0]+b*v[1]*w[1])%q
    def standard(v):
        v=tuple(x%q for x in v)
        if v==(0,0): return None
        k=next(x for x in v if x)
        return tuple(x*pow(k,-1,q)%q for x in v)
    V=[(x,y) for x in S for y in S if (x,y)!=(0,0)]
    mat=[((a,b),(c,d)) for a,b,c,d in product(S,repeat=4) if (a*d-b*c)%q]
    def act(T,v): return ((T[0][0]*v[0]+T[0][1]*v[1])%q,(T[1][0]*v[0]+T[1][1]*v[1])%q)
    def pair(v,w):return tuple(sorted([standard(v),standard(w)]))
    def leg(a):
        a%=q
        if not a:return 0
        return 1 if pow(a,(q-1)//2,q)==1 else -1
    for a,b,u in [(1,1,(1,0)),(1,(2%q if leg(2)==-1 else next(t for t in S if t and leg(t)==-1)),(1,0)),(1,-1,(1,1))]:
        b%=q
        delta=dot(u,u,a,b)
        natural={pair(v,w) for v in V for w in V if dot(v,w,a,b)==0 and (v[0]*w[1]-v[1]*w[0])%q}
        aut=[]
        for T in mat:
            tu=act(T,u)
            c=next((t for t in range(1,q) if (t*u[0]%q,t*u[1]%q)==tu),None)
            if c is None:continue
            if all(dot(act(T,v),act(T,w),a,b)==c*dot(v,w,a,b)%q for v in [(1,0),(0,1)] for w in [(1,0),(0,1)]):
                aut.append(T)
        remaining=set(natural);orbit_sizes=[]
        while remaining:
            p=next(iter(remaining))
            o={pair(act(T,p[0]),act(T,p[1])) for T in aut}
            assert o<=natural
            remaining-=o
            orbit_sizes.append(len(o))
        N=(q-leg(-a*b))//2
        O=(q-leg(-a*b)+3+leg(a*b))//4 if delta else 1
        assert len(natural)==N,(q,a,b,u,N,len(natural))
        assert len(aut)==(2 if delta else q-1),(q,a,b,u,len(aut))
        assert len(orbit_sizes)==O,(q,a,b,u,O,len(orbit_sizes))
        print('OK',dict(q=q,a=a,b=b,u=u,delta=delta,natural_bases=N,aut=len(aut),orbits=O,orbit_sizes=sorted(orbit_sizes)))
for q in [3,5,7,11,13]:run(q)
print('VERIFY_OK')
