#!/usr/bin/env python3
"""Exact polynomial certificate over GF(11) for a nodal realization germ.
Only the Python standard library is required. Coordinates of points are homogeneous.
"""
from itertools import combinations
from math import comb
P = 11

def poly(data=None):
    return {e: c % P for e, c in (data or {}).items() if c % P}

def const(n):
    return poly({(0, 0): n})

X, Z, ONE = poly({(1, 0): 1}), poly({(0, 1): 1}), const(1)
ZERO = {}

def add(a, b):
    out = dict(a)
    for e, c in b.items(): out[e] = (out.get(e, 0) + c) % P
    return poly(out)

def neg(a): return poly({e: -v for e, v in a.items()})
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    out = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            t = (i+k, j+l)
            out[t] = (out.get(t, 0) + v*w) % P
    return poly(out)

def scale(a, n): return poly({e: n*v for e, v in a.items()})
def sum_poly(*args):
    result = {}
    for arg in args: result = add(result, arg)
    return result

def cross(a, b):
    return (sub(mul(a[1],b[2]),mul(a[2],b[1])),
            sub(mul(a[2],b[0]),mul(a[0],b[2])),
            sub(mul(a[0],b[1]),mul(a[1],b[0])))

def det(a,b,c):
    q = cross(b,c)
    return sum_poly(*(mul(aa,bb) for aa,bb in zip(a,q)))

def intersection(a,b,c,d):
    return cross(cross(a,b),cross(c,d))

def eval_poly(a,x,z):
    return sum(c*pow(x,i,P)*pow(z,j,P) for (i,j),c in a.items())%P

def point(*args): return tuple(const(a) if isinstance(a,int) else a for a in args)

v={0:point(0,1,0),1:point(1,1,1),2:point(2,1,8),
   3:point(3,1,5),4:point(X,ONE,Z)}
for i,(a,b,c,d) in ((8,(0,3,1,2)), (7,(1,3,0,4)),
                      (6,(2,3,1,4)), (5,(0,6,2,4)),
                      (10,(0,1,4,8)), (9,(0,2,5,8))):
    v[i]=intersection(v[a],v[b],v[c],v[d])

G=sum_poly(mul(X,mul(X,X)),scale(mul(mul(X,X),Z),3),
           scale(mul(X,X),2),scale(mul(X,mul(Z,Z)),-5),
           scale(mul(X,Z),3),neg(X),scale(mul(Z,mul(Z,Z)),-5),
           mul(Z,Z),Z)
residuals=((3,9,10),(5,7,10),(6,7,9))
assert det(*(v[i] for i in residuals[0])) == scale(G,3)
assert det(*(v[i] for i in residuals[1])) == mul(G,add(scale(Z,2),scale(X,-2)))
assert det(*(v[i] for i in residuals[2])) == mul(G,sum_poly(scale(X,-2),scale(Z,5),const(-3)))

for i in range(11):
    yi=eval_poly(v[i][1],4,9)
    assert yi != 0, ('y-coordinate vanishes',i)
    target=(i,1,pow(i,3,11))
    assert all((eval_poly(v[i][j],4,9)*target[1] - yi*target[j])%11==0 for j in (0,2)),i

# A distinct triple is dependent precisely when its indices sum to zero.
nonbasis=[]
for a,b,c in combinations(range(11),3):
    q=[(j,1,pow(j,3,11)) for j in (a,b,c)]
    d=(q[0][0]*(q[1][1]*q[2][2]-q[1][2]*q[2][1])
       -q[0][1]*(q[1][0]*q[2][2]-q[1][2]*q[2][0])
       +q[0][2]*(q[1][0]*q[2][1]-q[1][1]*q[2][0])) % 11
    assert (d==0) == ((a+b+c)%11==0),(a,b,c,d)
    if d==0: nonbasis.append((a,b,c))
assert len(nonbasis)==15
assert set(nonbasis)-set(residuals) == {
 (0,1,10),(0,2,9),(0,3,8),(0,4,7),(0,5,6),
 (1,2,8),(1,3,7),(1,4,6),(2,3,6),(2,4,5),
 (4,8,10),(5,8,9)}
# The six intersection steps impose precisely the twelve non-residual incidences.
for tri in set(nonbasis)-set(residuals):
    assert not det(*(v[i] for i in tri)),tri

assert eval_poly(G,4,9)==0
# The gradient at (4,9) vanishes and the homogeneous quadratic initial form is 3u(v-u).
def shifted(f):
    out={}
    for (i,j),c in f.items():
        for a in range(i+1):
            for b in range(j+1):
                t=(a,b)
                out[t]=(out.get(t,0)+c*comb(i,a)*comb(j,b)
                        *pow(4,i-a,11)*pow(9,j-b,11))%11
    return poly(out)
local=shifted(G)
expected=poly({(2,0):-3,(1,1):3,(3,0):1,(2,1):3,(1,2):-5,(0,3):-5})
assert local==expected,(local,expected)
assert local.get((0,0),0)==local.get((1,0),0)==local.get((0,1),0)==0
print('NODE_CERTIFICATE_OK')
print('characteristic=11, points=11, nonbases=15, bases=150')
print('local_equation=G(x,z), cusp=(4,9)')
print('residual_relations=3G,(-2x+2z)G,(-2x+5z-3)G')
print('quadratic_initial_form=3u(v-u), ordinary_split_node')
