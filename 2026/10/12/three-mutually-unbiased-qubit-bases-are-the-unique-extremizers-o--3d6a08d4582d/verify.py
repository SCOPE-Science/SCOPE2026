#!/usr/bin/env python3
import itertools, math, random

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def unit(a):
    n=norm(a); return [x/n for x in a]
def mat_vec(A,x): return [dot(row,x) for row in A]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def inv3(A):
    d=det3(A)
    if abs(d)<1e-12: raise ValueError('singular')
    C=[
      [ A[1][1]*A[2][2]-A[1][2]*A[2][1], A[0][2]*A[2][1]-A[0][1]*A[2][2], A[0][1]*A[1][2]-A[0][2]*A[1][1]],
      [ A[1][2]*A[2][0]-A[1][0]*A[2][2], A[0][0]*A[2][2]-A[0][2]*A[2][0], A[0][2]*A[1][0]-A[0][0]*A[1][2]],
      [ A[1][0]*A[2][1]-A[1][1]*A[2][0], A[0][1]*A[2][0]-A[0][0]*A[2][1], A[0][0]*A[1][1]-A[0][1]*A[1][0]]]
    return [[x/d for x in row] for row in C]
def h_from_x(x):
    x=max(-1.0,min(1.0,x)); p=(1+x)/2
    if p<=0 or p>=1: return 0.0
    return -p*math.log(p)-(1-p)*math.log(1-p)
def avg_entropy(A,r): return sum(h_from_x(dot(n,r)) for n in A)/3

beta=h_from_x(1/math.sqrt(3))
beta_closed=0.5*math.log(6)-math.log(2+math.sqrt(3))/(2*math.sqrt(3))
assert abs(beta-beta_closed)<1e-14
floor=2*math.log(2)/3

# Strict concavity sign, sampled only as a consistency check of the displayed analytic derivative.
for k in range(1,1000):
    x=k/1000
    assert x/(1-x*x)-math.atanh(x)>0

# MUB frame sampled over the sphere.
I=[[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]
rng=random.Random(20261007)
seen_max=-1; seen_min=10
for _ in range(20000):
    r=unit([rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1)])
    e=avg_entropy(I,r)
    seen_max=max(seen_max,e); seen_min=min(seen_min,e)
    assert e<=beta+1e-12 and e>=floor-1e-12
assert seen_max>beta-1e-4 and seen_min<floor+1e-4

# Exact equality directions for the MUB frame.
r=unit([1,1,1]); assert abs(avg_entropy(I,r)-beta)<1e-14
r=[1.,0.,0.]; assert abs(avg_entropy(I,r)-floor)<1e-14

# Sign-vector inverse-frame construction on several nonsingular nonorthogonal frames.
frames=[
 [unit([1,0,0]),unit([1,1,0]),unit([0,1,2])],
 [unit([1,2,3]),unit([-2,1,1]),unit([1,-1,2])],
 [unit([1,0.2,0.1]),unit([0.1,1,0.3]),unit([0.2,0.4,1])],
]
for A in frames:
    inv=inv3(A)
    vals=[]
    witnesses=[]
    for eps in itertools.product((-1.,1.), repeat=3):
        x=[e/math.sqrt(3) for e in eps]
        v=mat_vec(inv,x)
        vals.append(dot(v,v)); witnesses.append((dot(v,v),v))
    # The theorem proves the average is at least one; numerical frames must reflect it.
    assert sum(vals)/8>=1-1e-12
    q,v=max(witnesses)
    assert q>1+1e-10
    r=unit(v)
    ovs=[abs(dot(n,r)) for n in A]
    assert max(ovs)<1/math.sqrt(3)-1e-10
    assert avg_entropy(A,r)>beta+1e-10
    # Lower-bound witness r=n_1.
    assert avg_entropy(A,A[0])<=floor+1e-12

# Singular frame: a common orthogonal direction gives three maximal binary entropies.
A=[[1.,0.,0.],[0.,1.,0.],unit([1,1,0])]
r=[0.,0.,1.]
assert abs(avg_entropy(A,r)-math.log(2))<1e-14
assert math.log(2)>beta

print('VERIFY_OK')
