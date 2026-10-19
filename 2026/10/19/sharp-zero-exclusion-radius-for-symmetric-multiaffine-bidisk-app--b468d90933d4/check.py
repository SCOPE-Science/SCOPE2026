"""Reproduce coefficient identities and test the sharp zero-exclusion theorem.

Uses only the Python standard library; finite checks supplement its analytic proof.
"""
from fractions import Fraction
from math import sqrt, isclose
from random import Random


def gram(u, a, b, alpha):
    """Return (||Mf||^2, <f,Mf>), M=z+w; linear in second slot."""
    v = 2.0 ** alpha
    w = 3.0 ** alpha
    norm = 2*v*abs(u)**2 + (2*w+4*v*v)*abs(a)**2 + 2*v*w*abs(b)**2
    corr = 2*v*u*a.conjugate() + 2*v*v*a*b.conjugate()
    return norm, corr


def eta(alpha):
    v = 2.0**alpha
    w = 3.0**alpha
    return sqrt((w+v*v)/(w*(w/v+2*v)))


def exact_integer_tests():
    for alpha in range(0, 11):
        v=Fraction(2)**alpha
        w=Fraction(3)**alpha
        c=w/v+2*v
        E=(w+v*v)/(c*w)
        # eigenvalues of D^{-1/2} B D^{-1/2}: 0, +/-sqrt(E)
        assert E==(Fraction(1,c)+v*v/(c*w))
        # normalized equality-vector equations with x=1, y=eta, z=v/w
        assert 1+v*(v/w)==E*c
        assert E<=Fraction(2,3)*(v/w)
        assert 3*(1+v/w)**2>Fraction(8)*(v/w) # sharp-f stabilizes
    return 11


def sampled_tests():
    rng=Random(20261015)
    n=0
    for alpha in (0, 0.01, 0.2, 0.5, 1, 2, 4, 8):
        t=eta(alpha)
        v=2**alpha
        w=3**alpha
        for _ in range(1500):
            u=complex(rng.uniform(-3,3),rng.uniform(-3,3))
            a=complex(rng.uniform(-3,3),rng.uniform(-3,3))
            b=complex(rng.uniform(-3,3),rng.uniform(-3,3))
            den,cor=gram(u,a,b,alpha)
            if den==0:continue
            ratio=2*abs(cor)/den
            assert ratio<=t+2e-12,(alpha,ratio,t)
            n+=1
        u=1+0j
        a=t+0j
        b=v/w+0j
        den,cor=gram(u,a,b,alpha)
        assert isclose(2*abs(cor)/den,t,rel_tol=2e-12)
        # exact affine OPA root of normalized polynomial 1 + (B/A)(z+w)
        B_over_A=-cor/den
        assert isclose(abs(1/(2*B_over_A)),1/t,rel_tol=2e-12)
        # stable extremizer: no root on closed bidisk for alpha>0
        if alpha>0:
            assert b.real<1 and t<1 and 2*t<1+b.real
        n+=1
    return n


def verify_phases():
    n=0
    from cmath import exp
    for alpha in (0,1,3,6):
        v=2**alpha
        w=3**alpha
        t=eta(alpha)
        for j in range(25):
            phi=j/9
            rot=exp(1j*phi)
            den,cor=gram(1+0j,t*rot,(v/w)*rot**2,alpha)
            assert isclose(2*abs(cor)/den,t,rel_tol=2e-12)
            n+=1
    return n


def independent_coefficients(alpha):
    rng=Random(112358)
    cases=0
    for _ in range(600):
        u=complex(rng.uniform(-2,2),rng.uniform(-2,2))
        a=complex(rng.uniform(-2,2),rng.uniform(-2,2))
        b=complex(rng.uniform(-2,2),rng.uniform(-2,2))
        f={(0,0):u,(1,0):a,(0,1):a,(1,1):b}
        mf={}
        for (i,j),c in f.items():
            for key in ((i+1,j),(i,j+1)):
                mf[key]=mf.get(key,0)+c
        direct=sum(((i+1)*(j+1))**alpha*abs(c)**2 for (i,j),c in mf.items())
        directcorr=sum(((i+1)*(j+1))**alpha * f.get((i,j),0).conjugate()*c for (i,j),c in mf.items())
        norm,corr=gram(u,a,b,alpha)
        assert abs(direct-norm)<1e-8*max(1,direct)
        assert abs(directcorr-corr)<1e-8*max(1,abs(directcorr))
        cases+=1
    return cases


if __name__=='__main__':
    e=exact_integer_tests()
    r=sampled_tests()
    p=verify_phases()
    k=sum(independent_coefficients(alpha) for alpha in (0,0.3,1,4))
    print(f'PASS: {e} exact rational identities, {r} random/equality tests, {p} phase-extremizer tests, {k} independently expanded coefficient checks')
