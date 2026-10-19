"""Reproducibility checks for the H^4 degree-one geometric-sum OPA.

Dependencies: Python 3 standard library only.
All norms use normalized Haar measure.
"""
from fractions import Fraction as F
from cmath import exp, pi
from math import isclose

def quartic(m,t):
    e=(1+t)/2
    return 6*e**4+12*m*e**2*t**2+4*m*(m-1)*e*t**3 + F(m*(2*m*m+1),3)*t**4

def derivative(m,t):
    # Derivative of expanded exact fourth moment.
    return (F(3,2) + (6*m+F(9,2))*t
          + (6*m*m+12*m+F(9,2))*t*t
          + (F(8,3)*m**3+8*m*m+F(16,3)*m+F(3,2))*t**3)

def minroot(m):
    lo,hi=-1.,0.
    assert derivative(m,lo)<0<derivative(m,hi)
    for _ in range(75):
        mid=(lo+hi)/2
        if derivative(m,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def directly_from_coefficients(m,t):
    e=(1+t)/2
    arr=[e]+[t]*m+[e]
    corr=[sum(arr[j]*arr[j+k] for j in range(len(arr)-k)) for k in range(len(arr))]
    return corr[0]**2+2*sum(z*z for z in corr[1:])

def grid_quadrature(m,t):
    e=(1+t)/2
    arr=[e]+[t]*m+[e]
    n=2**(max(12, (4*(m+2)-1).bit_length()))
    return sum(abs(sum(c*exp(2j*pi*k*j/n) for j,c in enumerate(arr)))**4 for k in range(n))/n

def g(u):return 1.5-6*u+6*u*u-F(8,3)*u**3

def q1(u):return u*(4*u**3-12*u*u+18*u-9)/6
lo,hi=0.,1.
for _ in range(80):
    c=(lo+hi)/2
    if g(c)>0:lo=c
    else:hi=c
c=(lo+hi)/2
assert 0.3574<c<0.3576
assert g(.3574)>0>g(.3576)
print('c=', format(c,'.15f'), 'kappa=', format(-q1(c),'.15f'))
print('m, t, optimal_real_a, zero, min_norm_fourth, max_difference_from_exact_correlation')
for m in [1,2,3,4,7,12,30,100,256]:
    t=minroot(m)
    d=float(quartic(m,t))
    c2=directly_from_coefficients(m,t)
    assert isclose(d,c2,rel_tol=4e-11,abs_tol=4e-11)
    assert derivative(m,t)>-1e-8 and derivative(m,t)<1e-8
    a=(1-t)/2
    w=(1-t)/(1+t)
    assert .5<a<1 and w>1
    if m in [1,2,4,12,30]:
        integration=grid_quadrature(m,t)
        assert isclose(d,integration,rel_tol=2e-12,abs_tol=2e-12),(m,d,integration)
    print(f'{m:3d} {t:+.12f} {a:.12f} {w:.12f} {d:.12f} {abs(d-c2):.3g}')
for m in [50,100,256,500,1000,10000]:
    t=minroot(m)
    u=-m*t
    d=float(quartic(m,t))
    print('asympt',m,'u',f'{u:.10f}','m*(E4^4-3/8)',f'{m*(d-.375):.10f}')
assert g(0)>0 and g(1)<0
print('All checks passed.')
