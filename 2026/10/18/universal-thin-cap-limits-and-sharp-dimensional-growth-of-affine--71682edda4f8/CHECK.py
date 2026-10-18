"""Independent finite checks of explicit affine-cap projector identities.

Run with Python 3: python CHECK.py.  The numerical checks do not replace
any quantified proof or establish historical priority.
"""
import math


def simpson(func, left, right, panels=12000):
    if panels % 2:
        raise ValueError('panels must be even')
    step = (right-left)/panels
    total = func(left)+func(right)
    for j in range(1,panels):
        total += (4 if j % 2 else 2)*func(left+j*step)
    return total*step/3


def model_tip(d):
    b = (d+1)/2
    return 2*(b+1)*((b+1)/(b+2))**b-1


def model_kernel(d, x, v, u, V):
    b = (d+1)/2
    mu = b/(b+1)
    beta = (b+1)**2*(b+2)/b
    return 1+(d+3)*x*u+beta*(v-mu)*(V-mu)


checks=0
for d in (2,3,4,5,8,12,30,100):
    b=(d+1)/2
    mu=b/(b+1)
    variance=b/((b+1)**2*(b+2))
    beta=(b+1)**2*(b+2)/b
    assert abs(beta*variance-1)<1e-12
    checks+=1
    assert abs(mu/(d+1)-1/(d+3))<1e-12
    checks+=1
    v0=(b+1)/(b+2)
    tip_numeric=simpson(lambda V:b*V**(b-1)*abs(model_kernel(d,0,0,0,V)),0,1,12000)
    assert abs(tip_numeric-model_tip(d))<1e-4
    checks+=1
    assert model_tip(d)>=1
    checks+=1

# At the exposed rim in dimension two, integrate the absolute affine kernel
# exactly in the tangent coordinate, then numerically in the height.
def planar_rim_integrand(v):
    s=math.sqrt(v)
    m=35*v/6-2.5
    if abs(m)>=5*s:
        return 0.75*2*s*abs(m)
    return 0.75*(5*s*s+m*m/5)

rim_numeric=simpson(planar_rim_integrand,0,1,12000)
rim_exact=69907/43218+300*math.sqrt(30)/2401
assert abs(rim_numeric-rim_exact)<1e-6
checks+=1
assert rim_exact>model_tip(2)
checks+=1

# The large dimension statement is analytic; these are scaling sanity checks.
for d in (100,1000,10000):
    assert abs(model_tip(d)/d-1/math.e)<0.015
    checks+=1

print(f'PASS: {checks} independent finite algebraic and quadrature checks')
print(f'planar rim witness {rim_exact:.13f}; tip in dimension two {model_tip(2):.13f}')
