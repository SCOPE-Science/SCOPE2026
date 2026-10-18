"""Reproduce Fourier coefficients and independent numerical Hessian checks."""
from fractions import Fraction
from math import sin, cos, pi, hypot

# Represent real trigonometric polynomials as complex Fourier coefficients.
def mul(x,y):
    out={}
    for k,a in x.items():
        for j,b in y.items():
            out[k+j]=out.get(k+j,0)+a*b
    return {k:v for k,v in out.items() if v}

def mean(x):
    return x.get(0,0)

c4={4:Fraction(1,2),-4:Fraction(1,2)}
f={2:Fraction(1,2),-2:Fraction(1,2)}
fp={2:1j,-2:-1j}  # derivative of cos(2 phi): -2 sin(2 phi).
assert mean(mul(f,f))==Fraction(1,2)
assert mean(mul(fp,fp))==2
assert mean(mul(c4,mul(f,f)))==Fraction(1,4)
assert mean(mul(c4,mul(fp,fp)))==-1
linear_hessian_coeff=(-36)*mean(mul(c4,mul(f,f)))-3*mean(mul(c4,mul(fp,fp)))
assert linear_hessian_coeff == -6

# Direct independently evaluated 1-D integrals (the integral is the actual
# polar angle integral via the change of variables in the mathematical proof).
def curvature_hessian(b, count=65536):
    J=Jp=Jpp=0.0
    for i in range(count):
        a=2*pi*i/count
        h=1+b*cos(4*a)
        hd=-4*b*sin(4*a)
        curvature=1-15*b*cos(4*a)
        r=hypot(h,hd)
        test=cos(2*a)
        testd=-2*sin(2*a)
        J+=h*curvature*r**3
        Jp+=5*test*r**3*curvature
        Jpp+=5*(r**3*(test**2-testd**2)+3*r*h*curvature*test**2)
    J/=count;Jp/=count;Jpp/=count
    F=J**(1/5)
    return F*(Jpp/(5*J)-4*Jp*Jp/(25*J*J))

# Verify sign and limiting slope independently of exact rational coefficient.
for b in [-0.01,-0.004,-0.001]:
    v=curvature_hessian(b)
    assert v>0, (b,v)
    assert abs(v/b+6)<(50*abs(b)),(b,v)
for b in [0.001,0.004,0.01]:
    v=curvature_hessian(b)
    assert v<0,(b,v)
assert abs(curvature_hessian(0))<1e-11

# Full disc Hessian spectrum, even Fourier degrees, in normalization avg.
for q in [0.1,2,3.8,4.6,4.99,5,5.01,5.7]:
    coefficients=[(q-1-n*n)/2 for n in range(2,42,2)]
    if q<5:
        assert max(coefficients)<0
    elif q==5:
        assert coefficients[0]==0 and max(coefficients[1:])<0
    else:
        assert coefficients[0]>0

print('PASS: four exact Fourier moments, endpoint coefficient -6, numerical Hessians and disk spectrum')
