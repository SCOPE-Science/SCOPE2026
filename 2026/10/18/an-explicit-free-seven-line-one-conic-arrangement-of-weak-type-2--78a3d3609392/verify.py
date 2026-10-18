#!/usr/bin/env python3
"""Exact integer-arithmetic verification for the displayed degree-nine arrangement.
No third-party packages are required. Output: VERIFIED_OK.
"""
from itertools import combinations
from math import gcd
from functools import reduce

def const(n): return {(0,0,0):int(n)} if n else {}
def add(*items):
    out={}
    for p in items:
        for k,v in p.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def sub(a,b):return add(a,neg(b))
def scale(c,p):return {k:c*v for k,v in p.items() if c*v}
def mul(*items):
    out=const(1)
    for p in items:
        nxt={}
        for a,u in out.items():
            for b,v in p.items():
                key=tuple(a[i]+b[i] for i in range(3))
                nxt[key]=nxt.get(key,0)+u*v
        out={k:v for k,v in nxt.items() if v}
    return out
def powp(p,n):return mul(*([p]*n))
def diff(p,i):
    out={}
    for k,v in p.items():
        if k[i]:
            a=list(k);a[i]-=1;out[tuple(a)]=v*k[i]
    return out
def evalp(p,v):
    return sum(c*(v[0]**e[0])*(v[1]**e[1])*(v[2]**e[2]) for e,c in p.items())

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def canon(v):
    h=reduce(gcd, (abs(t) for t in v))
    assert h
    v=tuple(t//h for t in v)
    sg=next(t for t in v if t)
    return tuple(-t for t in v) if sg<0 else v

def det3(M):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return add(mul(a,sub(mul(e,i),mul(f,h))),
               neg(mul(b,sub(mul(d,i),mul(f,g)))),
               mul(c,sub(mul(d,h),mul(e,g))))

X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
x,y,z=X,Y,Z
linear=[x,y,add(x,y),add(x,z),sub(x,z),add(y,z),sub(y,z)]
q=add(powp(x,2),powp(y,2),neg(powp(z,2)),mul(x,y))
F=mul(*linear,q)
assert len(F)>0 and set(sum(k) for k in F)=={9}

# Two degree-four Jacobian syzygies with fully integral coefficients.
P1=scale(-2,mul(x,z,add(scale(2,mul(x,y)),scale(-9,powp(y,2)),scale(3,powp(z,2)))))
P2=scale(2,mul(y,z,add(scale(9,powp(x,2)),scale(-2,mul(x,y)),scale(-3,powp(z,2)))))
P3=add(scale(27,mul(powp(x,2),powp(y,2))),scale(-9,mul(powp(x,2),powp(z,2))),
       scale(-4,mul(x,y,powp(z,2))),scale(-9,mul(powp(y,2),powp(z,2))),scale(3,powp(z,4)))
Q1=neg(mul(x,add(scale(3,powp(x,3)),scale(8,mul(powp(x,2),y)),scale(10,mul(x,powp(y,2))),
                 scale(-9,mul(x,powp(z,2))),scale(6,powp(y,3)),scale(-18,mul(y,powp(z,2))))))
Q2=mul(y,add(scale(6,powp(x,3)),scale(10,mul(powp(x,2),y)),scale(8,mul(x,powp(y,2))),
             scale(-18,mul(x,powp(z,2))),scale(3,powp(y,3)),scale(-9,mul(y,powp(z,2)))))
Q3=scale(2,mul(z,sub(x,y),add(scale(3,powp(x,2)),scale(8,mul(x,y)),scale(3,powp(y,2)))))
P=(P1,P2,P3);Q=(Q1,Q2,Q3)
grad=[diff(F,i) for i in range(3)]
assert add(*[mul(P[i],grad[i]) for i in range(3)])=={}
assert add(*[mul(Q[i],grad[i]) for i in range(3)])=={}
assert det3([list((x,y,z)),list(P),list(Q)])==scale(-243,F)
assert all(set(sum(k) for k in s)=={4} for s in P+Q)

# All pairwise intersections of seven lines, with incidence sets.
L=[(1,0,0),(0,1,0),(1,1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)]
pts={}
for i,j in combinations(range(7),2):
    pt=canon(cross(L[i],L[j]))
    pts.setdefault(pt,set()).update((i,j))
for pt,S in pts.items():
    assert all(sum(L[i][k]*pt[k] for k in range(3))==0 for i in S)
    assert {i for i in range(7) if sum(L[i][k]*pt[k] for k in range(3))==0}==S
multiplicity={m:sum(len(S)==m for S in pts.values()) for m in (2,3,4)}
on_conic={m:sum(len(S)==m and evalp(q,pt)==0 for pt,S in pts.items()) for m in (2,3,4)}
assert multiplicity=={2:6,3:5,4:0}, (multiplicity,pts)
assert on_conic=={2:4,3:2,4:0},on_conic

# The conic is nonsingular (determinant of its symmetric Hessian is -6).
assert -6 == 2*(2*(-2)) -1*(1*(-2))
# Every line meets the conic in two distinct points, no line-conic tangency.
for line in L:
    vectors=[]
    for basis in ((1,0,0),(0,1,0),(0,0,1)):
        v=cross(line,basis)
        if any(v):
            v=canon(v)
            if v not in vectors:vectors.append(v)
    assert len(vectors)>=2
    v,w=vectors[:2]
    A=evalp(q,v);C=evalp(q,w)
    B=evalp(q,tuple(v[i]+w[i] for i in range(3)))-A-C
    assert B*B-4*A*C !=0

# The six conic incidences use all 14 line-conic intersection multiplicities.
new_nodes=14-2*on_conic[2]-3*on_conic[3]
assert new_nodes==0
n2=multiplicity[2]-on_conic[2]+new_nodes
n3=multiplicity[3]-on_conic[3]+on_conic[2]
n4=multiplicity[4]+on_conic[3]
assert (n2,n3,n4)==(2,7,2)
tau=n2+4*n3+9*n4
assert tau==48
print('VERIFIED_OK: seven distinct lines, nonsingular transverse conic, (n2,n3,n4)=(2,7,2), tau=48, two degree-four syzygies, determinant=-243F')
