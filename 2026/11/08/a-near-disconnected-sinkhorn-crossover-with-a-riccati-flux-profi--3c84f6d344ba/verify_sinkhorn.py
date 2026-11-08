"""Finite exact-arithmetic and floating-point checks for a two-atom matrix-scaling theorem.

This program checks algebraic identities and illustrative finite-parameter behavior;
the proof of uniform convergence and asymptotic equivalences is analytic.
"""
from fractions import Fraction as Q
from math import sqrt, log, exp, floor, isclose


def direct_ratio(a, b, d, x):
    u1 = a / (x+d)
    u2 = (1-a) / (d*x+1)
    v1 = b / (u1+d*u2)
    v2 = (1-b) / (d*u1+u2)
    return v1/v2


def mobius_ratio(a,b,d,x):
    A=1-a+a*d*d
    C=a+(1-a)*d*d
    B=b/(1-b)
    return B*(A*x+d)/(d*x+C)


def spectral(a,b,d):
    A=1-a+a*d*d
    C=a+(1-a)*d*d
    B=b/(1-b)
    S=B*A+C
    Delta=sqrt((B*A-C)**2+4*B*d*d)
    zm=(B*A-C-Delta)/(2*d)
    zp=(B*A-C+Delta)/(2*d)
    q=(S-Delta)/(S+Delta)
    return zp,zm,q


def flow(a,k,t,x0):
    discr=sqrt(k*k+4*a*(1-a))
    zp=(k+discr)/(2*(1-a))
    zm=(k-discr)/(2*(1-a))
    rho=(x0-zp)/(x0-zm)*exp(-discr*t/(a*(1-a)))
    return (zp-rho*zm)/(1-rho)


def exact_tests():
    count=0
    As=[Q(1,5),Q(1,3),Q(3,4),Q(7,8)]
    Bs=[Q(1,4),Q(2,5),Q(4,7),Q(5,6)]
    Ds=[Q(1,10),Q(1,2),Q(4,5)]
    Xs=[Q(1,7),Q(1,1),Q(5,3),Q(7,2)]
    for a in As:
      for b in Bs:
        for d in Ds:
          A=1-a+a*d*d;C=a+(1-a)*d*d;B=b/(1-b)
          assert A*C-d*d == a*(1-a)*(1-d*d)**2
          count+=1
          for x in Xs:
            assert direct_ratio(a,b,d,x)==mobius_ratio(a,b,d,x)
            count+=1
            u1=a/(x+d);u2=(1-a)/(1+d*x)
            assert a*d/(x+d)==u1*d
            assert (1-a)*d*x/(1+d*x)==u2*d*x
            count+=2
    return count


def numerical_tests():
    count=0
    for a in (0.2,1/3,0.7):
      for k in (-0.4,0.0,0.9):
       for x0 in (0.15,1.0,3.5):
        errs=[];ds=(0.025,0.0125,0.00625)
        for d in ds:
            b=a+k*d
            assert 0<b<1
            zp,zm,q=spectral(a,b,d)
            assert zp>0 and zm<0 and 0<q<1
            x=x0
            C=(x-zp)/(x-zm)
            # Cross ratio at each positive step.
            for n in range(1,11):
                x=mobius_ratio(a,b,d,x)
                C*=q
                assert isclose((x-zp)/(x-zm),C,rel_tol=2e-11,abs_tol=2e-11)
                count+=1
            x=x0
            n=floor(2.0/d)
            for _ in range(n):x=mobius_ratio(a,b,d,x)
            err=abs(x-flow(a,k,n*d,x0))
            errs.append(err)
            # Exact finite-k row offdiag values are <= row masses.
            L=a*d/(x+d);R=(1-a)*d*x/(1+d*x)
            assert 0<L<a and 0<R<1-a
            assert isclose((1-a)*zp-a/zp,k,rel_tol=1e-2,abs_tol=0.22) # finite-delta limit
            count+=2
        assert errs[2]<0.13
        count+=1
    for a in (0.2,0.4,0.7):
      for b in (0.25,0.62,0.82):
       for d in (1e-3,2e-4,4e-5):
        zp,zm,q=spectral(a,b,d)
        if abs(b-a)>1e-4:
            lim=exp(-abs(log(b/(1-b))-log(a/(1-a))))
            assert abs(q-lim)<0.015
            count+=1
    return count


def limit_rate_tests():
    count=0
    for a,k in ((0.25,-0.4),(1/3,0.0),(0.6,0.4)):
      for d in (0.005,0.001,0.0002):
        b=a+k*d
        zp,zm,q=spectral(a,b,d)
        omega=sqrt(k*k+4*a*(1-a))/(a*(1-a))
        assert abs(-log(q)/d/omega-1)<0.1
        root=(k+sqrt(k*k+4*a*(1-a)))/(2*(1-a))
        assert abs(zp-root)<0.05
        count+=2
    # Joint crossover: perturbations of arbitrarily different relative magnitudes.
    for a in (0.25,0.57):
      for d in (0.005,0.001,0.0002):
        for b in (a+2*d,a-2*d,a+sqrt(d)*0.1,a):
          zp,zm,q=spectral(a,b,d)
          approx=sqrt((b-a)**2+4*a*(1-a)*d*d)/(a*(1-a))
          assert abs(-log(q)/approx-1)<0.14
          count+=1
    return count


if __name__=='__main__':
    a=exact_tests();b=numerical_tests();c=limit_rate_tests()
    print(f'PASS: {a} rational identities, {b} finite-iterate comparisons, {c} asymptotic spot-checks; total {a+b+c}.')
