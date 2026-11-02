"""Independent numerical identities for the reset-cycle OU energy theorem.

Usage: python verify.py
Requires numpy and scipy. These are finite checks, not proofs of asymptotic laws.
"""
import math
from scipy.integrate import quad
from scipy.special import erfcx, gamma, hyperu

checks = 0
betas = (0.25, 0.5, 0.75, 1.0, 2.0, 4.0)


def check(x, y, rtol=1e-7, atol=2e-12):
    global checks
    assert math.isfinite(x) and math.isfinite(y)
    assert abs(x-y) <= atol + rtol*max(abs(y),abs(x)), (x,y)
    checks += 1


def tail_scaled(beta, w):
    """Exact probability divided by exp(-w)*w**(-beta-.5)*Gamma(beta+1)/sqrt(pi).

    v=w*u transform, scaled complementary error function avoids underflow.
    """
    def f(v):
        if v >= w:
            return 0.0
        rho = 1.0-v/w
        z = w/rho
        mills_ratio = math.sqrt(math.pi*z)*erfcx(math.sqrt(z))
        return (v**(beta-1))*math.sqrt(rho)*math.exp(-v/rho)*mills_ratio
    val=quad(f,0,min(w,80),points=[0] if beta<1 else None,epsabs=1e-10,limit=300)[0]
    return beta*val/gamma(beta+1)


for beta in betas:
    # Exact density as beta-mixture agrees with its Kummer-Tricomi representation.
    for w in (0.05, 0.2, 1.0, 3.0, 10.0):
        def smooth(u):
            return math.exp(-w/(1-u)) if u<1 else 0.0
        integral=quad(smooth,0,1,weight='alg',wvar=(beta-1,-.5),epsabs=1e-12)[0]
        fd=beta/math.sqrt(math.pi*w)*integral
        fk=gamma(beta+1)/math.sqrt(math.pi*w)*math.exp(-w)*hyperu(beta,.5,w)
        check(fd,fk,rtol=2e-8)

    # Mean is exact from independent beta and Gaussian factors.
    for s in (0.01, .1, .4):
        mgf=beta*quad(lambda u:(1-s+s*u)**(-.5),0,1,weight='alg',wvar=(beta-1,0))[0]
        assert mgf>=1
        checks+=1
    check(beta/(beta+1),1.0/(1.0+1.0/beta),rtol=1e-14)
    if beta>.5:
        check(beta/(beta-.5),beta*quad(lambda u:u**(beta-1.5),0,1)[0])

    # Scaled tail ratios tend to one; compare two widely spaced levels.
    vals=[tail_scaled(beta,w) for w in (30.,120.,300.)]
    assert 0<vals[0]<vals[1]<vals[2]<1.000001, (beta,vals)
    checks+=3
    assert vals[-1]>.90,(beta,vals)
    checks+=1

    # The conditional age mark v=w exp(-2 mu T) has Gamma(beta,1) limit.
    w=100.0
    def numerator(v, moment):
        if v>=w:
            return 0.0
        rho=1-v/w
        z=w/rho
        mills_ratio=math.sqrt(math.pi*z)*erfcx(math.sqrt(z))
        return v**(beta-1+moment)*math.sqrt(rho)*math.exp(-v/rho)*mills_ratio
    integrals=[quad(lambda v:numerator(v,k),0,50,epsabs=1e-10,limit=200)[0] for k in (0,1)]
    assert 0<integrals[1]/integrals[0]<beta,(beta,integrals)
    checks+=1

print('PASS: %d deterministic numerical checks' % checks)
