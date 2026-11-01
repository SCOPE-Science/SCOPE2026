"""Supplementary finite checks for the two-exceptional-axis shadow law.
Requires Python 3.10+, numpy, scipy; run: python verify_projection.py.
Finite tests corroborate, but do not replace, the proof in RESULT.md.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(20261030)
exact_checks = 0
for ia in range(2, 9):
    for ib in range(1, ia):
        A, B = Fraction(ia), Fraction(ib)
        for it in range(1, 11):
            t = B + (A-B)*Fraction(it, 11)
            for j in range(1, 8):
                x, y = Fraction(j, 17), Fraction(1, 5)
                trace = A+B-A*x-B*y
                det = A*B*(1-x-y)
                poly = t*t-t*trace+det
                form = -(A-t)*(t-B)+A*(t-B)*x-B*(A-t)*y
                assert poly == form
                exact_checks += 1

def cdf_integral(d,A,B,t):
    if t <= B: return 0.
    if t >= A: return 1.
    alpha=A*(t-B); beta=B*(A-t); gamma=(A-t)*(t-B)
    theta0=math.atan(math.sqrt((t-B)/(A-t)))
    def integrand(theta):
        z=alpha*math.cos(theta)**2-beta*math.sin(theta)**2
        return max(0.,1-gamma/z)**((d-2)/2)
    return (2/math.pi)*quad(integrand,0,theta0,epsabs=2e-11,epsrel=2e-11)[0]

def cdf_four(A,B,t):
    if t<=B:return 0.
    if t>=A:return 1.
    return (2/math.pi)*(math.atan(math.sqrt((t-B)/(A-t)))
      - math.sqrt((A-t)*(t-B)/(A*B))*math.atanh(math.sqrt(B/A)))

quad_checks=0
for A,B in [(3.,1.), (8.,2.), (10.,9.), (2.,0.1)]:
    for t in np.linspace(B+0.001*(A-B),A-0.001*(A-B),19):
        fc=cdf_four(A,B,t)
        fq=cdf_integral(4,A,B,t)
        assert abs(fc-fq)<2e-9,(A,B,t,fc,fq)
        assert 0<fc<1
        quad_checks+=1

# Separate geometric numerical check: restrict the ellipsoid support quadratic
# form to a random (d-1)-dimensional subspace constructed from QR.
linear_checks=0
for d in [3,4,5,8]:
    A,B,b2=3.,1.1,0.6
    Q=np.diag([b2+A,b2+B]+[b2]*(d-2))
    for _ in range(175):
        u=rng.normal(size=d);u/=np.linalg.norm(u)
        basis=np.linalg.svd(u.reshape(1,-1),full_matrices=True)[2][1:].T
        lam_direct=np.linalg.eigvalsh(basis.T@Q@basis)[-1]-b2
        x,y=u[0]**2,u[1]**2
        tr=A+B-A*x-B*y
        determinant=A*B*(1-x-y)
        lam_formula=(tr+math.sqrt(max(0.,tr*tr-4*determinant)))/2
        assert abs(lam_direct-lam_formula)<3e-12,(d,lam_direct,lam_formula)
        linear_checks+=1

# Check predicted distribution against independent random directions.
mc_checks=0
for d in [3,4,6,9]:
    A,B=3.,1.
    nn=90000
    U=rng.normal(size=(nn,d));U/=np.linalg.norm(U,axis=1)[:,None]
    tr=A+B-A*U[:,0]**2-B*U[:,1]**2
    det=A*B*(1-U[:,0]**2-U[:,1]**2)
    L=(tr+np.sqrt(np.maximum(0.,tr**2-4*det)))/2
    for t in [1.05,1.25,1.7,2.2,2.65,2.95]:
        predicted=cdf_integral(d,A,B,t)
        observed=float(np.mean(L<=t))
        assert abs(predicted-observed)<0.015,(d,t,predicted,observed)
        mc_checks+=1
for t in [1.1,1.4,1.8,2.1,2.6,2.9]:
    vals=[cdf_integral(d,3.,1.,t) for d in [3,4,6,9]]
    assert all(vals[k]>vals[k+1] for k in range(3)),(t,vals)

print('PASS: exact algebra',exact_checks,
      '| quadrature/closed law',quad_checks,
      '| independent matrix compression',linear_checks,
      '| simulation CDF comparisons',mc_checks,
      '| strict dimension ordering',6)
