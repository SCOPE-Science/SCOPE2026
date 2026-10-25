from fractions import Fraction as F
from itertools import combinations

def legendre_pair(m, x):
    p0,p1=F(1),x
    if m == 0: return F(1),F(0)
    if m == 1: return x,F(1)
    for k in range(1,m):
        p2=((2*k+1)*x*p1-k*p0)/(k+1)
        p0,p1=p1,p2
    return p1,p0

def normalized(l,x):
    m=l+1
    p,pm=legendre_pair(m,x)
    return F(2)*(m*(pm-x*p)/(1-x*x))/(m*(m+1))

def sectors(l):
    u,v=normalized(l,F(1,2)),normalized(l,F(0))
    if l%2:return (1+4*u,1-2*u)
    return (1+8*u+6*v,1+2*u-3*v,1-2*u+v)

minv=(F(100),None,None)
for l in range(3,64):
    for j,z in enumerate(sectors(l)):
        if z<minv[0]:minv=(z,l,j)
        assert z>=F(21,64),(l,j,z)
assert minv==(F(21,64),4,1),minv
assert sectors(1)==(F(3),F(0))
assert sectors(2)[0]==0
print('EXACT_FINITE_PASS', 'degrees=3..63', 'smallest=21/64', 'degree=4', 'sector=standard_even')
print('LOW_DEGREES', str(sectors(0)),str(sectors(1)),str(sectors(2)))
print('DEGREE_3', str(sectors(3)))
print('DEGREE_4', str(sectors(4)))
print('TAIL_BOUND', 'ell>=64: 1-44/(ell+2) >= 1-44/66 > 21/64')
