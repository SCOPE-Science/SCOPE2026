#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

def padd(a,b):
    n=max(len(a),len(b)); out=[F(0) for _ in range(n)]
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def pmul(a,b):
    out=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def pscale(a,c): return [c*x for x in a]

def parity(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def charpoly(J):
    n=len(J); M=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append([-J[i][j], F(1)] if i==j else [-J[i][j]])
        M.append(row)
    out=[F(0)]
    for perm in permutations(range(n)):
        t=[F(1)]
        for i,j in enumerate(perm): t=pmul(t,M[i][j])
        out=padd(out,pscale(t,F(parity(perm))))
    return out

def mv(J,v): return [sum(J[i][j]*v[j] for j in range(len(v))) for i in range(len(J))]
def vm(v,J): return [sum(v[i]*J[i][j] for i in range(len(v))) for j in range(len(J[0]))]
def dot(a,b): return sum(x*y for x,y in zip(a,b))

alpha=F(1,7); p=F(1,5)
J0=[
    [F(0),alpha,F(0),F(0)],
    [F(-10),F(0),F(1),F(0)],
    [F(0),F(0),F(0),F(1)],
    [F(0),F(1),F(0),F(0)],
]
assert charpoly(J0)==[F(0),F(-1),F(10,7),F(0),F(1)]
v=[F(1),F(0),F(10),F(0)]
ell=[F(1),F(0),F(0),-alpha]
assert mv(J0,v)==[F(0)]*4
assert vm(ell,J0)==[F(0)]*4
assert dot(ell,v)==1
Bvv=[20*p,F(-20),F(2),F(0)]
assert F(1,2)*dot(ell,Bvv)==F(2)

J1=[
    [F(-1),F(1),F(-1,5),F(0)],
    [F(-5),F(-1),F(2),F(0)],
    [F(-2),F(-20),F(0),F(1)],
    [F(0),F(1),F(0),F(0)],
]
assert charpoly(J1)==[F(-3),F(308,5),F(228,5),F(2),F(1)]
print('VERIFY_OK')
