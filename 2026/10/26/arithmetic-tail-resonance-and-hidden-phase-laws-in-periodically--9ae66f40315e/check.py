"""Numerical consistency checks for the phase-randomized Cox-walk theorem.

Run with Python 3 (standard library only). Finite tests corroborate but do
not replace the analytic singularity and conditioning arguments.
"""
from math import sqrt, log, exp, acosh, isclose


def simpson(fun, a, b, steps=4000):
    assert steps % 2 == 0
    h = (b-a)/steps
    total = fun(a)+fun(b)
    for i in range(1,steps):
        total += (4 if i % 2 else 2)*fun(a+h*i)
    return total*h/3


def qc(t, B=1.0):
    if t == 0:
        return 0.0, 1.0
    bt=B*t
    return bt/(1+bt+sqrt(1+2*bt)), 1/sqrt(1+2*bt)


def prob_two_given_phase(m, u, B=1.0):
    qa,ca=qc(1-u,B)
    qb,cb=qc(u,B)
    if m<0:m=-m
    if abs(qa-qb)<1e-9:
        ss=(m+1)*qa**m
    else:
        ss=(qa**(m+1)-qb**(m+1))/(qa-qb)
    z=qa*qb
    return ca*cb*(ss+(qa**m+qb**m)*z/(1-z))


def exact_one_mass(m,B=1.0):
    return simpson(lambda u:prob_two_given_phase(m,u,B),0,1)


def one_mass_scaled(m,B=1.0):
    q,_=qc(1,B)
    # Normalize inside the integrand, avoiding underflow for rare masses.
    def f(u):
        qa,ca=qc(1-u,B); qb,cb=qc(u,B)
        if abs(qa-qb)<1e-9:
            s=(m+1)*(qa/q)**m
        else:
            s=((qa/q)**m*qa-(qb/q)**m*qb)/(qa-qb)
        z=qa*qb
        return ca*cb*(s+((qa/q)**m+(qb/q)**m)*z/(1-z))
    return simpson(f,0,1)


def block_mgf(t,z,B=1.0):
    return 1/(1+B*t*(1-(z+1/z)/2))


def assert_close(a,b,tol=1e-9):
    assert abs(a-b) <= tol*max(1,abs(a),abs(b)), (a,b)


def run():
    checks=0
    for B in (0.2,1.0,5.0):
        q,c=qc(1,B)
        s=acosh(1+1/B)
        assert_close(q,exp(-s)); checks+=1
        assert_close(c,(1-q)/(1+q)); checks+=1
        assert_close(1/(B*__import__('math').sinh(s)),c);checks+=1
        for z in (1.03,1.15,0.87):
            h=1+B*(1-(z+1/z)/2)
            # Distinct derivation: integrate independently over a uniform phase.
            numeric=simpson(lambda u:block_mgf(1-u,z,B)*block_mgf(u,z,B),0,1)
            closed=2*log(h)/(h*h-1)
            assert_close(numeric,closed,3e-8);checks+=1
            for n in (1,2,4):
                assert_close(numeric*block_mgf(1,z,B)**(n-1),
                             2*log(h)/((h*h-1)*h**(n-1)),3e-8)
                checks+=1
    # Full lattice distribution, independent exact two-sided-geometric convolution.
    B=1.;q,c=qc(1,B)
    for m in (15,30,60,120):
        scaled=one_mass_scaled(m,B)
        assert abs(scaled*m/2-1) < 1.1/m, (m,scaled*m/2)
        checks+=1
    # An independent two-period convolution of the one-period phase mixture.
    # Negative and positive geometric tail terms are included explicitly.
    for m in (20,40,80):
        K=18
        a=[one_mass_scaled(j,B) for j in range(m+K+1)]
        scaled2=c*(sum(a[:m+1])+
                   sum(q**(2*j)*(a[j]+a[m+j]) for j in range(1,K+1)))
        assert abs(scaled2/(2*c*log(m))-1)<0.035, (m,scaled2)
        checks+=1
    # Noninteger full-block prefactor, checked by direct elementary quadrature.
    for a in (.15,.4,.8):
        direct=simpson(lambda u:1/(u*(2-a-u)),1-a,1)
        assert_close(direct,2*log(1/(1-a))/(2-a));checks+=1
    # The fixed-phase spatial increment is normalized at each rate-duration.
    for B in (.2,1.,3.):
        for t in (.1,.6,1.):
            q,c=qc(t,B)
            assert_close(c*(1+q)/(1-q),1);checks+=1
    print('PASS:',checks,'deterministic consistency assertions')

if __name__=='__main__':run()
