#!/usr/bin/env python3
"""Independent exact-rational checks for a layered diffusion first-passage theorem."""
from fractions import Fraction as Q

B = [Q(0), Q(1,3), Q(2,3), Q(1)]
S = [Q(1), Q(1), Q(128)]
M = [Q(1), Q(1,32), Q(1,32)]

# Integrate the scale-speed moment identities directly, with exact rational data.
TAIL = [Q(0)] * 4
K = [Q(0)] * 4
for i in reversed(range(3)):
    TAIL[i] = TAIL[i+1] + M[i]*(B[i+1]-B[i])
for i in reversed(range(3)):
    K[i] = K[i+1] + S[i]*(TAIL[i]**3-TAIL[i+1]**3)/(3*M[i])

assert TAIL == [Q(17,48),Q(1,48),Q(1,96),Q(0)]
assert K == [Q(1363,82944),Q(5,3072),Q(1,648),Q(0)]

def moments(x):
    x=Q(x)
    u=v=Q(0)
    for i in range(3):
        delta=max(Q(0),min(x,B[i+1])-B[i])
        if not delta: break
        si,mi,ma,mb=S[i],M[i],TAIL[i],TAIL[i+1]
        u += si*(ma*delta-mi*delta**2/2)
        v += 2*si*(K[i+1]-si*mb**3/(3*mi))*delta
        v += si**2*(ma**4-(ma-mi*delta)**4)/(6*mi**2)
    return u,v

def polynomial(x):
    x=Q(x)
    if x <= Q(1,3):
        return x*(17280*x**3-24480*x**2+10404*x-1363)/41472
    if x <= Q(2,3):
        return (405*x**4-1620*x**3+270*x**2-348*x+341)/995328
    return (6635520*x**4-26542080*x**3+38658816*x**2-24233472*x+5527381)/995328

# A second construction: transfer of (phi, phi'/s) solving L phi = r phi.
# Truncated power series in r to quadratic order, using rational hyperbolic expansions.
Z=(Q(0), Q(0), Q(0)); O=(Q(1),Q(0),Q(0))
def add(a,b): return tuple(a[i]+b[i] for i in range(3))
def mul(a,b): return tuple(sum(a[j]*b[i-j] for j in range(i+1)) for i in range(3))
def mm(a,b): return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def eye(): return [[O if i==j else Z for j in range(2)] for i in range(2)]
def transfer(s,m,d):
    z=s*m
    c=(Q(1),z*d*d/2,z*z*d**4/24)
    a=(s*d,s*z*d**3/6,s*z*z*d**5/120)
    b=(Q(0),m*d,m*z*d**3/6)
    return [[c,a],[b,c]]

def laplace_moments(x):
    full=eye()
    for i in range(3):
        full=mm(transfer(S[i],M[i],B[i+1]-B[i]),full)
    # phi(0)=1, phi'(1)/s(1)=0; solve boundary condition formally.
    j1=-full[1][0][1]
    j2=-full[1][0][2]+full[1][0][1]*full[1][1][1]
    part=eye()
    for i in range(3):
        d=max(Q(0),min(x,B[i+1])-B[i])
        if d: part=mm(transfer(S[i],M[i],d),part)
    series=add(part[0][0],mul(part[0][1],(Q(0),j1,j2)))
    return -series[1], 2*series[2]

samples=[Q(k,60) for k in range(1,61)] + [Q(1,3),Q(2,3)]
for x in samples:
    u,v=moments(x)
    assert u*u-v == polynomial(x), ('polynomial',x)
    u2,w2=laplace_moments(x)
    assert u2==u and w2==u*u+v, ('transfer',x)

witnesses={Q(1,4):Q(-11,82944), Q(2,5):Q(18961,124416000),
           Q(7,10):Q(-496831,124416000), Q(4,5):Q(1326209,124416000)}
for x,expected in witnesses.items():
    assert polynomial(x)==expected

assert polynomial(Q(0)) == 0
assert polynomial(Q(1,3))==Q(25,124416)
assert polynomial(Q(2,3))==Q(-19,110592)
assert polynomial(Q(1))==Q(46165,995328)

roots=[]
for lo,hi in [(Q(1,4),Q(1,3)),(Q(1,2),Q(3,5)),(Q(7,10),Q(4,5))]:
    assert polynomial(lo)*polynomial(hi)<0
    for _ in range(80):
        mid=(lo+hi)/2
        if polynomial(lo)*polynomial(mid) <= 0: hi=mid
        else: lo=mid
    roots.append(float((lo+hi)/2))
print('PASS: exact rational identities, 62 first/second-moment transfer checks, four signed witnesses')
print('Approximate three interior zeros:', *(f'{r:.12f}' for r in roots))
print('Mathematical uniqueness is proved by derivative signs in RESULT.md, not numerics.')
