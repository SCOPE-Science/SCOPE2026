from fractions import Fraction
from itertools import product

V=[(a,b) for a in range(2) for b in range(2)]

def madd(A,B):
    return tuple((A[i][j]^B[i][j]) for i in range(2) for j in range(2))
def mat(t): return ((t[0],t[1]),(t[2],t[3]))
def tup(A): return (A[0][0],A[0][1],A[1][0],A[1][1])
def mm(A,B):
    return tuple(sum(A[i][k]*B[k][j] for k in range(2))%2 for i in range(2) for j in range(2))
def det(A): return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%2
H=[mat(t) for t in product(range(2), repeat=4) if det(mat(t))==1]
I=((1,0),(0,1))
def inv(A):
    # GL2(F2): brute
    return next(B for B in H if mm(A,B)==tup(I) and mm(B,A)==tup(I))
def act(A,v): return ((A[0][0]*v[0]+A[0][1]*v[1])%2,(A[1][0]*v[0]+A[1][1]*v[1])%2)
def va(a,b): return (a[0]^b[0],a[1]^b[1])

def hmul(A,B): return mat(mm(A,B))
def heq(A,B): return A==B

B=[(u,h) for u in V for h in H]

def plus(x,y):
    u,h=x; v,g=y
    return (va(u,v),hmul(h,g))
def pinv(x):
    u,h=x
    hi=inv(h)
    # direct product, u inverse=u
    return (u,hi)
def circ(x,y):
    u,h=x; v,g=y
    return (va(u,act(inv(h),v)), hmul(h,g))
def lamb(x,y):
    u,h=x; v,g=y
    hi=inv(h)
    return (act(hi,v), hmul(hmul(hi,g),h))
def star(x,y):
    # lambda_x(y) - y in additive group
    return plus(lamb(x,y), pinv(y))

e=( (0,0), I )
def comm_plus(x,y): return plus(x,y)==plus(y,x)
def comm_circ(x,y): return circ(x,y)==circ(y,x)
def brace_comm(x,y):
    return comm_plus(x,y) and circ(x,y)==plus(x,y) and circ(y,x)==plus(y,x)
def plambda_pair(x,y): return star(x,y)==e
def pt_pair(x,y):
    return star(x,x)==e and star(x,y)==e and star(y,x)==e and star(y,y)==e

npb=sum(brace_comm(x,y) for x in B for y in B)
nlam=sum(plambda_pair(x,y) for x in B for y in B)
npt=sum(pt_pair(x,y) for x in B for y in B)
nap=sum(comm_plus(x,y) for x in B for y in B)
nmp=sum(comm_circ(x,y) for x in B for y in B)
print(len(H),len(B),npb,nlam,npt,nap,nmp)
print('Pb',Fraction(npb,len(B)**2))
print('P_lambda',Fraction(nlam,len(B)**2))
print('Pt',Fraction(npt,len(B)**2))
print('Pr_plus',Fraction(nap,len(B)**2))
print('Pr_circ',Fraction(nmp,len(B)**2))
assert (npb,nlam,npt,nap,nmp)==(96,168,60,288,120)
assert Fraction(npb,576)==Fraction(1,6)
assert Fraction(nlam,576)==Fraction(7,24)
assert Fraction(npt,576)==Fraction(5,48)
assert Fraction(nap,576)==Fraction(1,2)
assert Fraction(nmp,576)==Fraction(5,24)
print('CHECK_OK')
