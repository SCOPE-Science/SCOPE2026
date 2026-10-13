import cmath
import math
import random

C=0.7

def matrix(kappa,xi,s):
    e=C*C*xi/kappa
    L=1-kappa*s/C
    return ((C*(1-s)+e*e*L)/(C+e), e*(1-e)/(C+e), e*L, 1-e)

def roots(M):
    a,b,c,d=M
    T=a+d
    D=a*d-b*c
    disc=cmath.sqrt(T*T-4*D)
    return ((T+disc)/2,(T-disc)/2)

def radius(M):
    return max(abs(z) for z in roots(M))

def ceiling(kappa,xi):
    return 2*(200*kappa+21*xi)/(200*kappa+49*xi*xi-49*xi)

random.seed(350085)

for _ in range(5000):
    kappa=10**random.uniform(0,4)
    xi=random.uniform(1e-5,math.sqrt(kappa))
    sm=ceiling(kappa,xi)
    for frac,stable in ((0.2,True),(0.999999,True),(1.000001,False),(1.3,False)):
        assert (radius(matrix(kappa,xi,frac*sm))<1)==stable

for kappa in (1,2,10,100,1e5):
    for xi in (0.2,min(1.0,math.sqrt(kappa)),math.sqrt(kappa)):
        sm=ceiling(kappa,xi)
        assert min(abs(z+1) for z in roots(matrix(kappa,xi,sm)))<2e-9

cross=10/7
for kappa in (3,10,100):
    assert ceiling(kappa,0.9*cross)>2
    assert abs(ceiling(kappa,cross)-2)<2e-14
    assert ceiling(kappa,1.1*cross)<2

lower=400/249
for kappa in (1,2,10,100,1e4,1e8):
    for xi in (1e-5,0.1*math.sqrt(kappa),0.5*math.sqrt(kappa),math.sqrt(kappa)):
        assert ceiling(kappa,xi)>lower
assert abs(ceiling(1e12,1e6)-lower)<1e-6

for kappa in (1,4,100,1e6):
    for xi in (0.1,min(1.0,math.sqrt(kappa)),math.sqrt(kappa)):
        if xi<=math.sqrt(kappa):
            assert radius(matrix(kappa,xi,1.0))<1

print("verification passed")
