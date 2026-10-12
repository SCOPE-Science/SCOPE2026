"""Exact polynomial identity for the bounded-run two-spectrum census at h=2."""

def add(a,b):
    r=[0]*max(len(a),len(b))
    for i,v in enumerate(a):r[i]+=v
    for i,v in enumerate(b):r[i]+=v
    while r and r[-1]==0:r.pop()
    return r

def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    while r and r[-1]==0:r.pop()
    return r

def scale(a,k):return [k*x for x in a]

def z(k,coef=1):return [0]*k+[coef]

def geom(period):
    assert 12%period==0
    r=[0]*12
    for i in range(0,12,period):r[i]=1
    return r

one_minus_z=[1,-1]
p1=mul(add(z(1),z(2,2)),geom(2))
p2=mul(add(z(3,-2),z(4,-4)),geom(3))
p3=mul(add(add(z(3,-1),z(4,2)),z(6,2)),geom(4))
lhs=scale(mul(one_minus_z,add(add(p1,p2),p3)),24)
c=[48,1,44,33,16,17,60,1,32,33,28,17]
periodic=[0]+c[1:]+[c[0]]
assert len(periodic)==13
rhs=add(mul(add(add(z(1,3),z(2,3)),mul(z(1,20),one_minus_z)),add(z(0),z(12,-1))),
        mul(periodic,mul(mul(one_minus_z,one_minus_z),one_minus_z)))
assert lhs==rhs, (lhs,rhs)
print('IDENTITY_OK rational_GF_h2_equals_exact_period12_quasipolynomial')
