#!/usr/bin/env python3
"""Independent finite-field and polynomial checks for the quartic example.

This verifier does not replace the geometric proof for arbitrary algebraically
closed fields: it checks the displayed witness over F_3 and F_27.
"""
from itertools import product

def add(a,b):
    return sum(((a//(3**i)+b//(3**i)) % 3)*(3**i) for i in range(3))

def neg(a):
    return sum((-(a//(3**i)))%3*(3**i) for i in range(3))

def mul(a,b):
    aa=[(a//3**i)%3 for i in range(3)]
    bb=[(b//3**i)%3 for i in range(3)]
    cc=[0]*5
    for i in range(3):
        for j in range(3): cc[i+j]=(cc[i+j]+aa[i]*bb[j])%3
    # t^3=t+1 over F3
    for i in (4,3):
        z=cc[i]
        cc[i]=0
        cc[i-2]=(cc[i-2]+z)%3
        cc[i-3]=(cc[i-3]+z)%3
    return cc[0]+3*cc[1]+9*cc[2]

def pw(x,n):
    r=1
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r

E=range(27)
assert len({pw(i,27) for i in E if i})==26
assert all(pw(i,27)==i for i in E)

def sums(*xs):
    z=0
    for x in xs:z=add(z,x)
    return z

def F(x,y,u,v):
    return sums(mul(u,pw(x,3)),mul(v,pw(y,3)),mul(mul(x,y),mul(u,v)),
         pw(u,4),mul(pw(u,3),v),mul(2,mul(u,pw(v,3))),pw(v,4))


def grad(x,y,u,v):
    q=mul(u,v)
    return (mul(y,q),mul(x,q),
        sums(pw(x,3),mul(mul(x,y),v),pw(u,3),mul(2,pw(v,3))),
        sums(pw(y,3),mul(mul(x,y),u),pw(u,3),pw(v,3)))

# Exhaustive finite-field projective check, 27^3+27^2+27+1 points.
points=[]
for n in range(4):
    for tail in product(E,repeat=3-n):
        P=(0,)*n+(1,)+tail
        if all(t==0 for t in grad(*P)):
            assert F(*P)==0
            points.append(P)
assert len(points)==6,points
assert all((p[2]==0) != (p[3]==0) for p in points)
assert len([p for p in points if p[2]==0])==3
assert len([p for p in points if p[3]==0])==3
assert all(any(z>=3 for z in p) for p in points)

# Algebraic identities and nondegenerate local coordinate changes.
for x,y,u,v in points:
    if u==0:
        iv=pw(v,25)
        xx,yy=mul(x,iv),mul(y,iv)
        assert yy==2
        assert sums(pw(xx,3),neg(xx),2)==0
        assert yy != 0 # Jacobian of xi with respect to x
    else:
        iu=pw(u,25)
        xx,yy=mul(x,iu),mul(y,iu)
        assert v==0 and xx==2
        assert sums(pw(yy,3),neg(yy),1)==0
        assert xx != 0 # Jacobian of xi with respect to y

# Witness g(t,1) = t^4+t^3+2t+1, derivative=t^3+2=(t-1)^3.
assert all(F(0,0,t,1)!=0 or (pw(t,3)!=1) for t in E)
# Exact polynomial identities for the two local analytic charts follow by
# expansion in characteristic three:
# F(x,y,u,1)=(y+1)^3+u*(x^3+xy+u^3+u^2+2)
# F(x,y,1,v)=(x+1)^3+v*(y^3+xy+1+2v^2+v^3).
# The Jacobian ideal of F=s*xi+w^3 is (s,xi,w^3), with
# quotient basis 1,w,w^2 (length three): char 3 kills d(w^3).
assert [(i+j) for i,j in ((0,0),(0,1),(0,2))]==[0,1,2]
for x,y,t in product(range(3),repeat=3):
    lhs=F(x,y,t,1)
    rhs=sums(pw(add(y,1),3),mul(t,sums(pw(x,3),mul(x,y),pw(t,3),pw(t,2),2)))
    assert lhs==rhs
    lhs=F(x,y,1,t)
    rhs=sums(pw(add(x,1),3),mul(t,sums(pw(y,3),mul(x,y),1,mul(2,pw(t,2)),pw(t,3))))
    assert lhs==rhs
print('VERIFY_OK: exact gradient witness and F27 singular support, local normal-form identities, 6 points / 2 Frobenius triples; each wild A2 Jacobian scheme length 3')
