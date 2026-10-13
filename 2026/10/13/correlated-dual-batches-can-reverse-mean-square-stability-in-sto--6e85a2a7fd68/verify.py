#!/usr/bin/env python3
"""Exact arithmetic verification of a two-block SPDHG sampling contrast."""
from fractions import Fraction as F
from itertools import product

Z=F(0)
I=lambda n:[[F(i==j) for j in range(n)] for i in range(n)]

def trans(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum((a*b for a,b in zip(row,col)),Z) for col in trans(B)] for row in A]
def add(A,B): return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def mul(t,A): return [[t*x for x in row] for row in A]
def mv(A,v): return [sum((a*b for a,b in zip(row,v)),Z) for row in A]
def det(A):
    A=[row[:] for row in A]; n=len(A); out=F(1)
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]!=0),None)
        if k is None:return Z
        if k!=j:A[k],A[j]=A[j],A[k];out=-out
        v=A[j][j];out*=v
        for k in range(j+1,n):
            r=A[k][j]/v
            for t in range(j+1,n):A[k][t]-=r*A[j][t]
    return out

def update_matrix(pair):
    j1,j2=pair
    a=F(10,11); b=F(1,2)
    M=[[Z for _ in range(4)] for _ in range(4)]
    M[0]=[a,Z,Z,-a]
    delta=[]
    for i,j in enumerate((j1,j2)):
        d=[Z]*4
        if j:
            d= [b*v for v in M[0]]
            d[i+1]+=b-1
        M[i+1][i+1]=F(1)
        M[i+1]=[x+y for x,y in zip(M[i+1],d)]
        delta.append(d)
    M[3]=[M[1][k]+M[2][k]+2*(delta[0][k]+delta[1][k]) for k in range(4)]
    return M
M00,M10,M01,M11=[update_matrix(e) for e in ((0,0),(1,0),(0,1),(1,1))]
P=mul(F(1,933),[[7233,620,620,-6300],
                   [620,13303,-7233,-620],
                   [620,-7233,13303,-620],
                   [-6300,-620,-620,7233]])
C=lambda M:mm(trans(M),mm(P,M))

def slack(q):
    return add(P,mul(-1,add(mul(q,add(C(M00),C(M11))),
                                mul(F(1,2)-q,add(C(M10),C(M01))))))

def positive(A):
    return [det([row[:k] for row in A[:k]]) for k in range(1,len(A)+1)]

assert P==trans(P)
assert all(d>0 for d in positive(P))
assert slack(Z)==I(4)
S=slack(F(1,100))
assert all(d>0 for d in positive(S))
assert S==[[F(28607,37631),F(2256,17105),F(2256,17105),F(9024,37631)],
          [F(2256,17105),F(1),-F(1128,7775),-F(2256,17105)],
          [F(2256,17105),-F(1128,7775),F(1),-F(2256,17105)],
          [F(9024,37631),-F(2256,17105),-F(2256,17105),F(28607,37631)]]
# Any q in [0,1/100] has an SPD slack by convexity of the SPD cone.
assert all(d>0 for d in positive(slack(F(1,200))))

# On repeated full-batch events the exact 3D reduction acts on (x, y1+y2, zbar).
B=[[F(10,11),Z,-F(10,11)],
   [F(10,11),F(1,2),-F(10,11)],
   [F(30,11),-F(1,2),-F(30,11)]]
assert mm(mm(B,add(B,mul(F(2),I(3)))),add(B,mul(-F(15,22),I(3)))) == [[Z]*3 for _ in range(3)]
eigdata=[(-F(2),[F(5,16),F(1,4),F(1)]),
         (Z,[F(1),Z,F(1)]),
         (F(15,22),[F(4),F(15),F(1)])]
for val,v in eigdata:
    assert mv(B,v)==[val*t for t in v]
assert [sum((c*v[j] for c,(_,v) in zip((-F(80,59),F(4,3),F(4,177)),eigdata)),Z) for j in range(3)] == [F(1),Z,Z]
state=[F(1),Z,Z]
for k in range(1,31):
    state=mv(B,state)
    target=-F(25,59)*(-2)**k + F(16,177)*F(15,22)**k
    assert state[0]==target
    assert abs(state[0])>=F(25,118)*2**k

# Verify direct scalar update and matrix action on rational sample states.
for x,y1,y2,z in product((F(-1),Z,F(2)), repeat=4):
    v=[x,y1,y2,z]
    xp=F(10,11)*(x-z)
    for (b1,b2),M in zip(((0,0),(1,0),(0,1),(1,1)),(M00,M10,M01,M11)):
        d1=F(b1)*(F(1,2)*(y1+xp)-y1)
        d2=F(b2)*(F(1,2)*(y2+xp)-y2)
        direct=[xp,y1+d1,y2+d2,y1+y2+3*(d1+d2)]
        assert mv(M,v)==direct

print('PASS exact update matrices, P and slack positivity, full-batch polynomial and path formula, 324 update tests')
print('P leading minors:',positive(P))
print('slack q=1/100 leading minors:',positive(S))
