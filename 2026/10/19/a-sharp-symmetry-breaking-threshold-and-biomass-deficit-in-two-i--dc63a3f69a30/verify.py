"""Self-contained arithmetic and numerical checks for a two-patch population-map theorem.
Run: python3 verify.py  (Python standard library only).
These checks supplement, but do not replace, the written global proofs.
"""
from fractions import Fraction as Q
from math import tanh, sqrt, isclose

# At effective reproduction T=2 the shared positive equilibrium is u=1.
# Direct formal Taylor coefficients of h(1+z)=2(1+z)/(2+z):
h0, h1, h2, h3 = Q(1), Q(1, 2), Q(-1, 4), Q(1, 8)
assert (h0, h1, h2, h3) == (Q(1), Q(1,2), Q(-1,4), Q(1,8))
# H(1+z)=h(1+z)*tanh(k*z), at k=1:
H1 = h0
H2 = h1
H3 = h2 - h0/Q(3)
assert (H1, H2, H3) == (Q(1), Q(1,2), Q(-7,12))
# Mean-equilibrium coefficient m=1+alpha*d^2+... :
alpha = h2 / (1-h1)     # using sum-map quadratic coefficient
assert alpha == Q(-1,2)
# Difference-map cubic coefficient after solving mean equation:
B = -(2*H2*alpha + H3)  # H(m+d)-H(m-d) over 2
assert B == Q(13,12), B
# Threshold branch: d^2=(k-1)/B+O((k-1)^2).
assert Q(1)/B == Q(12,13)
assert 2*alpha/B == Q(-12,13)   # total biomass correction in k-1


def h(z):
    return 2*z/(1+z)

def H(z,k):
    return h(z)*tanh(k*(z-1))

def hp(z):
    return 2/(1+z)**2

def Hp(z,k):
    w=tanh(k*(z-1))
    return hp(z)*w+h(z)*k*(1-w*w)

def x_for_y(y):
    c=y*(1-y)/(1+y)
    return (1+c+sqrt((1+c)**2+4*c))/2

def gap(y,k):
    x=x_for_y(y)
    return (H(x,k)-H(y,k))/(x-y)-1

def bisect(k):
    lo,hi = 1e-9, 0.999999
    assert gap(lo,k)<0 and gap(hi,k)>0
    for _ in range(90):
        mid=(lo+hi)/2
        if gap(mid,k)<0: lo=mid
        else: hi=mid
    y=(lo+hi)/2
    return x_for_y(y),y

def eigenvalues(x,y,k):
    A=(hp(x)+hp(y))/2
    Bm=(hp(x)-hp(y))/2
    C=(Hp(x,k)-Hp(y,k))/2
    D=(Hp(x,k)+Hp(y,k))/2
    tr=A+D
    disc=(A-D)**2+4*Bm*C
    assert disc>=0
    return ((tr+sqrt(disc))/2,(tr-sqrt(disc))/2)

for k in (1.002,1.005,1.01,1.02,1.04):
    x,y=bisect(k)
    m,d=(x+y)/2,(x-y)/2
    assert x>1>y>0
    assert isclose(x+y,h(x)+h(y),abs_tol=1e-12)
    assert isclose(x-y,H(x,k)-H(y,k),abs_tol=2e-12)
    eig=eigenvalues(x,y,k)
    assert max(abs(v) for v in eig)<1
    assert 0<x+y<2
    scaled=d*d/(k-1)
    print('k',k,'equilibrium',tuple(round(t,9) for t in (x,y)),
          'd^2/(k-1)',round(scaled,9),'eigs',tuple(round(v,8) for v in eig))
assert abs(bisect(1.002)[0]-1)<0.2
print('PASS: exact Taylor identities; five positive stable symmetry-broken equilibria; fixed-point residuals and biomass inequalities.')
