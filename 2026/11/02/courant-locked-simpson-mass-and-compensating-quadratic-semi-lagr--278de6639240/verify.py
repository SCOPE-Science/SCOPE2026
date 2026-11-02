"""Independent exact-rational and Fourier checks for periodic quadratic interpolation.

Run: python3 verify.py
Requires only Python's standard library. The symbolic proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, sin, pi, sqrt


def lagrange(t):
    return ((t-1)*(t-2)/2, t*(2-t), t*(t-1)/2)


def update(n, f):
    f = F(f)
    size = 2*n
    a = [[F(0) for _ in range(size)] for _ in range(size)]
    for j in range(size):
        departure = F(j) + f
        cell = departure//2
        t = departure - 2*cell
        for k, coeff in enumerate(lagrange(t)):
            a[j][(2*cell+k)%size] += coeff
    return a


def conserved_weights(n, f):
    f = F(f)
    d = min(f, 2-f)
    return [(d/2 if j%2==0 else 1-d/2)/n for j in range(2*n)]


def matmul(a,b):
    size=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(size)) for j in range(size)] for i in range(size)]


def left(w, a):
    return [sum(w[i]*a[i][j] for i in range(len(w))) for j in range(len(w))]


def schur_symbol(f, theta):
    t=complex(cos(theta),sin(theta))
    l0,l1,l2=lagrange(f)
    m0,m1,m2=lagrange(1+f)
    a=l0+t*l2
    b=l1
    c=m0+t*m2
    d=m1
    tau=a+d
    Delta=a*d-b*c
    residual=(1-abs(Delta)**2)**2-abs(tau-tau.conjugate()*Delta)**2
    target=4*f**4*(2-f)*(1-f)**2*sin(theta/2)**4
    return Delta,residual,target


checks=0
for n in (2,3,4,5,7):
    for f in (F(1,10),F(1,4),F(1,3),F(1,2),F(2,3),F(9,10),F(1),F(11,10),F(4,3),F(3,2),F(7,4),F(19,10)):
        a=update(n,f)
        w=conserved_weights(n,f)
        assert all(sum(row)==1 for row in a)
        assert left(w,a)==w
        simpson=[(F(1,3*n) if j%2==0 else F(2,3*n)) for j in range(2*n)]
        assert (left(simpson,a)==simpson)==(f in (F(2,3),F(4,3)))
        checkerboard=[F(j%2==0) for j in range(2*n)]
        asymptotic=sum(x*y for x,y in zip(w,checkerboard))
        physical=sum(x*y for x,y in zip(simpson,checkerboard))
        d=min(f,2-f)
        assert abs(asymptotic-physical)==abs(d/2-F(1,3))
        checks+=5

for n in (2,3,5):
    a=update(n,F(1,4))
    b=update(n,F('0.8985274985937725'))
    product=matmul(b,a)
    simpson=[(F(1,3*n) if j%2==0 else F(2,3*n)) for j in range(2*n)]
    assert max(abs(float(x-y)) for x,y in zip(left(simpson,product),simpson))<1e-14
    checks+=1

# Exact quadratic compensation polynomial at first displacement 1/4.
def F_poly(a,b):
    return 3*a*a+3*(1-2*a)*b*b+(1-2*a)*(1-2*b)-1
for b in [F(k,11) for k in range(12)]:
    assert F_poly(F(1,4),b)==(24*b*b-16*b-5)/16
    checks+=1
root=(4+sqrt(46))/12
assert abs(float(F_poly(F(1,4),root)))<1e-14
checks+=1

for f in (0.05,0.17,0.33,0.57,0.81,0.99):
    for k in range(1,120):
        theta=2*pi*k/121
        Delta, residual, target=schur_symbol(f,theta)
        assert abs(Delta)<1
        assert residual>0
        assert abs(residual-target)<1e-9
        checks+=3

print('VERIFIED',checks,'exact and supplementary checks')
