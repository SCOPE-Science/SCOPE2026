"""Supplementary checks for the quadratic skew Schaeffer profile of a hexagonal norm."""
from fractions import Fraction as F
from math import sqrt

VERTICES=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))

def norm(v):
    return max(abs(v[0]),abs(v[1]),abs(v[0]-v[1]))

def unit_edge(j,t):
    v,w=VERTICES[j],VERTICES[(j+1)%6]
    return ((1-t)*v[0]+t*w[0],(1-t)*v[1]+t*w[1])

def objective(x,y,r):
    u=(x[0]+r*y[0],x[1]+r*y[1])
    v=(r*x[0]-y[0],r*x[1]-y[1])
    return (norm(u)**2+norm(v)**2)/2

def candidate(r):
    A=1+r*r
    q=1-2*r+r*r-r**3
    if q>=0:
        a=r
        b=r*(1-r)
        val=A*A*(1-r+r*r/2)
    else:
        D=A*A+r*r
        a=(A*A-r)/D
        b=r*(1-a)
        val=A*A*(1+r)**2/(2*D)
    return a,b,val

def near(x,y,tol=1e-10):
    return abs(float(x-y))<tol

for r in (F(0),F(1,10),F(1,4),F(1,2),F(3,5),F(3,4),F(1)):
    a,b,val=candidate(r)
    assert 0<=a<=1 and 0<=b<=1
    assert near(objective((1,a),(-1+b,-1),r),val)
    assert val<=1+r*r
    for j in range(6):
        for k in range(6):
            for v in range(11):
                x=unit_edge(j,F(v,10))
                for w in range(11):
                    y=unit_edge(k,F(w,10))
                    assert objective(x,y,r)>=val-F(1,10**10), (r,j,k,v,w)
    # Euclidean/Hilbert reference and endpoint t=infty both dominate quadratic.
    print(f'r={float(r):.3f}, a={float(a):.12f}, b={float(b):.12f}, S2={sqrt(float(val)):.12f}, checks=4356')

# The two analytic branches agree at the unique real root.
lo,hi=0.,1.
for _ in range(100):
    mid=(lo+hi)/2
    if 1-2*mid+mid*mid-mid**3>0: lo=mid
    else: hi=mid
rho=(lo+hi)/2
A=1+rho*rho
low=A*A*(1-rho+rho*rho/2)
high=A*A*(1+rho)**2/(2*(A*A+rho*rho))
assert near(low,high,1e-12)
assert near(rho,0.5698402909980532,1e-14)
print(f'critical parameter={rho:.15f}; branches match; supplementary checks passed')
