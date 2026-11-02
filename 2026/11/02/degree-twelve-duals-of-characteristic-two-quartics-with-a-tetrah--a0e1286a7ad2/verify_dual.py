#!/usr/bin/env python3
"""Exact polynomial and finite-field checks for a characteristic-two quartic dual.

Run with Python 3; no third-party dependencies.  This verifies symbolic identities
in F_2[b_1,...,b_4,a_12,...,a_34,u_1,...,u_4] and one finite-field model.
"""
from itertools import combinations, product

N=14 # four coordinate variables, four diagonal, six off-diagonal coefficients
pairs=list(combinations(range(4),2))
zero=(0,)*N

def term(entries):
    v=[0]*N
    for idx,e in entries.items():v[idx]=e
    return tuple(v)

def plus(*polys):
    p=set()
    for poly in polys:p.symmetric_difference_update(poly)
    return p

def mult(a,b):
    out=set()
    for x in a:
        for y in b:
            z=tuple(t+s for t,s in zip(x,y))
            if z in out:out.remove(z)
            else:out.add(z)
    return out

def pow_poly(a,n):
    z={zero}
    for _ in range(n):z=mult(z,a)
    return z

def diff(poly,i):
    out=set()
    for e in poly:
        if e[i]%2:
            f=list(e);f[i]-=1
            f=tuple(f)
            if f in out:out.remove(f)
            else:out.add(f)
    return out

# p(u)=product u_i; Cremona C_i(u)=prod_{j != i}u_j.
u=[{term({i:1})} for i in range(4)]
p=mult(mult(u[0],u[1]),mult(u[2],u[3]))
c=[]
for i in range(4):
    c_i={zero}
    for j in range(4):
        if j!=i:c_i=mult(c_i,u[j])
    c.append(c_i)
# The source quadric Q(T) has independent universal coefficients.
Q=set()
for i in range(4):
    Q=plus(Q,mult({term({4+i:1})},pow_poly(c[i],2)))
for idx,(i,j) in enumerate(pairs):
    Q=plus(Q,mult({term({8+idx:1})},mult(c[i],c[j])))
G=plus(pow_poly(p,3),pow_poly(Q,2))
assert len(G)==11 and all(sum(e[:4])==12 for e in G)
for i in range(4):
    assert diff(G,i)==mult(pow_poly(p,2),diff(p,i))
    plane={e for e in G if e[i]==0}
    assert plane=={term({4+i:2, **{j:4 for j in range(4) if j!=i}})}
    # e_i is an isolated coordinate vertex in the singular arrangement.
    assert min(sum(e[j] for j in range(4) if j!=i) for e in G)==8
for i,j in pairs:
    assert min(e[i]+e[j] for e in G)==4

# Independently check the double-Cremona identity with formal coordinates.
q_x=set()
for i in range(4):q_x=plus(q_x,mult({term({4+i:1})},pow_poly(u[i],2)))
for idx,(i,j) in enumerate(pairs):
    q_x=plus(q_x,mult({term({8+idx:1})},mult(u[i],u[j])))
F=plus(p,pow_poly(q_x,2))
# Replacing u_i by C_i(x) in G (including coefficient variables unchanged).
def substitute_u(poly,new):
    result=set()
    for e in poly:
        m={term({i:e[i] for i in range(4,14) if e[i]})}
        for i in range(4):m=mult(m,pow_poly(new[i],e[i]))
        result=plus(result,m)
    return result
assert substitute_u(G,c)==mult(pow_poly(p,8),F)

# F_4 = F_2[t]/(t^2+t+1), encoded as a+bt.
def mul(a,b):
    x=(a&1)*(b&1); y=((a&1)*((b>>1)&1) ^ ((a>>1)&1)*(b&1));z=((a>>1)&1)*((b>>1)&1)
    return (x^z) | ((y^z)<<1)
def power(a,n):
    b=1
    for _ in range(n):b=mul(b,a)
    return b

def quad(v):
    r=0
    for x in v:r^=mul(x,x)
    for i,j in pairs:r^=mul(v[i],v[j])
    return r

def prod(v):
    r=1
    for x in v:r=mul(r,x)
    return r

def phi(v):
    return tuple(prod([v[j] for j in range(4) if j!=i]) for i in range(4))

def f(v):return prod(v)^power(quad(v),2)
def g(v):return power(prod(v),3)^power(quad(phi(v)),2)

def norm(v):
    for x in v:
        if x:
            inv=power(x,2)
            return tuple(mul(z,inv) for z in v)
    raise ValueError('zero tuple')

points=set()
for v in product(range(4),repeat=4):
    if any(v):points.add(norm(v))
sings=set()
for v in points:
    if f(v)==0 and all(prod([v[j] for j in range(4) if j!=i])==0 for i in range(4)):
        sings.add(v)
assert len(sings)==12
assert all(sum(x==0 for x in v)==2 for v in sings)
T={v for v in points if all(v)}
xt={v for v in T if f(v)==0}
gt={v for v in T if g(v)==0}
assert {norm(phi(v)) for v in xt}==gt
assert {norm(phi(v)) for v in gt}==xt
for v in points:
    if g(v)==0 and prod(v)==0:
        assert sum(x==0 for x in v)>=2
    if sum(x==0 for x in v)>=2: assert g(v)==0
print('CHAR2_DUAL_CREMONA_DEGREE12_SIX_QUADRUPLE_EDGES_FOUR_OCTUPLE_VERTICES_PASS')
print('universal_terms',len(G),'projective_F4_points',len(points),'F4_nodes',len(sings),'torus_X_points',len(xt),'torus_dual_points',len(gt))
