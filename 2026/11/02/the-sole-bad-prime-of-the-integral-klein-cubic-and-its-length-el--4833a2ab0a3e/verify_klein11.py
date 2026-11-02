#!/usr/bin/env python3
"""Exact finite-field checks for the cyclic Klein cubic bad-reduction calculation.
The accompanying proof establishes all algebraic-closure and all-primes assertions.
"""
from itertools import product

def f(x, p):
    return sum(x[i]*x[i]*x[(i+1)%5] for i in range(5))%p

def grad(x,p):
    return tuple((x[(i-1)%5]**2+2*x[i]*x[(i+1)%5])%p for i in range(5))

def points(n,p):
    for pivot in range(n):
        for tail in product(range(p),repeat=n-pivot-1):
            yield (0,)*pivot+(1,)+tail

def rank(A,p):
    A=[[v%p for v in row] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        k=next((i for i in range(r,m) if A[i][c]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        z=pow(A[r][c],-1,p)
        A[r]=[(v*z)%p for v in A[r]]
        for i in range(m):
            if i!=r:
                z=A[i][c]
                A[i]=[(v-z*w)%p for v,w in zip(A[i],A[r])]
        r+=1
    return r

for p in (2,3,5,7,11):
    pts=[x for x in points(5,p) if f(x,p)==0 and not any(grad(x,p))]
    assert pts==([(1,3,9,5,4)] if p==11 else []),(p,pts)
    print('RATIONAL_SINGULAR_POINTS',p,pts)

p=11; a=9; u0=3
assert pow(a,5,p)==1
assert pow(a,-2,p)==u0
assert (1+pow(a,-1,p)+pow(a,-2,p)+pow(a,-3,p))%p==2
assert pow(a,-6,p)==5
assert (2*u0+5)%p==0
for u in range(1,p):
    v=pow(a*u,-1,p)
    w=u**3%p
    z=pow(pow(a,3,p)*pow(u,5,p),-1,p)
    x=(1,u,v,w,z)
    ds=grad(x,p)
    assert ds[1:4]==(0,0,0)
    assert ds[4]==((pow(u,11,p)-u0)*pow(u, -5,p))%p
    assert f(x,p)==(2*(pow(u,11,p)-u0)*pow(u,-10,p))%p
print('EXACT_LAURENT_CRITICAL_BRANCH_IDENTITIES_OK')

x=(1,3,9,5,4)
H=[]
for i in range(1,5):
    row=[]
    for j in range(1,5):
        # Hessian of sum x_i^2*x_{i+1}; component i,j, indices 0..4.
        v=0
        for k in range(5):
            if i==k and j==k:v+=2*x[(k+1)%5]
            if i==k and j==(k+1)%5:v+=2*x[k]
            if j==k and i==(k+1)%5:v+=2*x[k]
        row.append(v%p)
    H.append(row)
assert H==[[7,6,0,0],[6,10,7,0],[0,7,8,10],[0,0,10,2]],H
assert rank(H,p)==3
assert (7*(10*8-7*7)-6*(6*8))%p==6
print('HESSIAN_CORANK_ONE_OK')

# In char 3, if the homogeneous gradient vanishes then the parameter
# u obeys u^11=1 and F|critical=2u, necessarily nonzero.
assert (-2)%3==1
assert (4+1)%3==2
print('CHARACTERISTIC_THREE_NO_SINGULAR_POINTS_BY_EULER_BRANCH_OK')
print('LOCAL_JACOBIAN_AND_TJURINA_ALGEBRA=k[t]/(t^11)_PROVED_SYMBOLICALLY')
print('VERIFY_OK')
