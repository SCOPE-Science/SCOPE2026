#!/usr/bin/env python3
"""Reproduce Gaussian-quadrature Gramian identities by independent calculations."""
from fractions import Fraction
from math import cos, sin, sqrt, pi, exp, isclose

TESTS = 0

def check(truth, message):
    global TESTS
    TESTS += 1
    if not truth:
        raise AssertionError(message)


def nodes_weights(order):
    if order == 1:
        return [0.5], [1.0]
    if order == 2:
        d = 1.0 / (2.0 * sqrt(3.0))
        return [0.5-d, 0.5+d], [0.5, 0.5]
    if order == 3:
        d = sqrt(15.0) / 10.0
        return [0.5-d, 0.5, 0.5+d], [5/18, 4/9, 5/18]
    if order == 4:
        x1 = sqrt((15 + 2*sqrt(30))/35)
        x2 = sqrt((15 - 2*sqrt(30))/35)
        c = [(1-x1)/2, (1-x2)/2, (1+x2)/2, (1+x1)/2]
        # Gauss-Legendre weights on [-1,1]: (18 +/- sqrt(30))/36.
        w = [(18-sqrt(30))/72, (18+sqrt(30))/72,
             (18+sqrt(30))/72, (18-sqrt(30))/72]
        return c, w
    raise ValueError(order)


def weighted_gram(order, theta, gamma):
    c,w = nodes_weights(order)
    a=b=d=0.0
    for ci,wi in zip(c,w):
        amp = wi*exp(-2*gamma*ci)
        x,y=cos(theta*ci),sin(theta*ci)
        a += amp*x*x
        b += amp*x*y
        d += amp*y*y
    return a,b,d


def determinant_cb(order, theta, gamma):
    c,w = nodes_weights(order)
    return sum(w[i]*w[j]*exp(-2*gamma*(c[i]+c[j])) *
               sin(theta*(c[j]-c[i]))**2
               for i in range(len(c)) for j in range(i+1,len(c)))


def eigenmin(order,theta,gamma):
    a,b,d=weighted_gram(order,theta,gamma)
    return ((a+d)-sqrt(max(0,(a-d)**2+4*b*b)))/2

for order in range(1,5):
    c,w=nodes_weights(order)
    check(all(0<ci<1 for ci in c), 'node location')
    check(all(wi>0 for wi in w), 'positive weights')
    check(isclose(sum(w),1,rel_tol=0,abs_tol=2e-15), 'weight sum')
    for p in range(2*order):
        check(abs(sum(wi*ci**p for wi,ci in zip(w,c)) - 1/(p+1))<1e-12,
              'Gauss polynomial moment')
    for gamma in [0,0.1,1.0]:
        for theta in [0.2,1.0,2.3,3.14159265358979,7.9,11.2,17.1]:
            a,b,d=weighted_gram(order,theta,gamma)
            check(abs((a*d-b*b)-determinant_cb(order,theta,gamma))<1e-12,
                  'independent Gram/Cauchy-Binet determinant')

for j in range(1,10):
    # Two- and three-node exact resonance formulas.
    th2=pi*sqrt(3)*j
    th3=10*pi/sqrt(15)*j
    check(abs(determinant_cb(2,th2,0))<1e-23,
          'two-node resonance')
    check(abs(determinant_cb(3,th3,0))<1e-23,
          'three-node resonance')

r1=sqrt((15+2*sqrt(30))/35)
r2=sqrt((15-2*sqrt(30))/35)
alpha=r1/r2
check(abs(alpha**2-(23+4*sqrt(30))/7)<1e-13,'irrational ratio identity')

# Continued-fraction convergents for alpha; each satisfies |m*alpha-p|<1/m.
a=alpha
ps=[0,1]
qs=[1,0]
conv=[]
for _ in range(13):
    z=int(a)
    p=z*ps[-1]+ps[-2]
    q=z*qs[-1]+qs[-2]
    ps.append(p);qs.append(q)
    conv.append((p,q))
    rest=a-z
    if rest==0: break
    a=1.0/rest

for p,q in conv[2:9]:
    if q>100_000: break
    check(abs(q*alpha-p)<1/q,'convergent Diophantine approximation')
    theta=2*pi*q/r2
    Gmin=eigenmin(4,theta,0)
    # Floating cancellation is only safe while theta is moderate.
    check(Gmin>=-1e-12,'four-node positivity within floating tolerance')
    check(Gmin<=pi*pi/(q*q)+1e-10,'quantitative near-singular eigenvalue')
    a,b,d=weighted_gram(4,theta,0)
    check(abs(a+d-1)<1e-12,'unit normalized Gram trace')

# Verify the exact continuum eigenvalue expression in the undamped case.
for theta in [0.1,0.3,1.1,3.7,7.2,15.3]:
    z=abs(sin(theta))/(2*theta)
    check(0.5-z>0,'exact continuous Gramian positive')
    check(abs((0.5-z)*(0.5+z) -
              (0.25 - sin(theta)**2/(4*theta**2)))<1e-14,
          'continuous determinant identity')

print('VERIFIED',TESTS,'assertions')
print('Legendre P4 positive roots:',r1,r2,'ratio:',alpha)
print('Convergents:',conv[:9])
print('s=4 first displayed near-resonance:',[(q,eigenmin(4,2*pi*q/r2,0)) for p,q in conv[2:7]])
