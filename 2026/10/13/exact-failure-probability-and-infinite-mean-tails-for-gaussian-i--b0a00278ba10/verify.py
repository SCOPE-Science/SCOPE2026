"""Reproducible arithmetic and sampling checks of the signed Nyström Schur model."""
from fractions import Fraction as F
from math import atan, pi, sqrt
from random import Random

def parameters(r):
    return r/(1-r), r/(1+r)

def low_eigen(r, gamma, u, v, eps=0):
    a,c=parameters(r)
    den=a*u*u-c*v*v+eps
    assert den!=0
    return gamma+(a*a*u*u+c*c*v*v)/den

def fail_event(r,gamma,u,v):
    a,c=parameters(r)
    return low_eigen(r,gamma,u,v)<0

def probability(r,gamma):
    a,c=parameters(r)
    t0=sqrt(c/a)
    ti=sqrt(c*(gamma-c)/(a*(gamma+a)))
    assert 0<ti<t0
    return 2/pi*(atan(t0)-atan(ti))

def exact_rational_test():
    r=F(1,2); g=F(2); u=F(1,2); v=F(1)
    a,c=parameters(r)
    d=a*u*u-c*v*v
    Q=[[g+a*a*u*u/d, -a*c*u*v/d], [-a*c*u*v/d,g+c*c*v*v/d]]
    assert Q==[[F(-1),F(2)],[F(2),F(2,3)]]
    assert Q[0][0]*Q[1][1]-Q[0][1]**2==F(-14,3)
    assert a==1 and c==F(1,3)
    assert low_eigen(r,g,u,v)==F(-7,3)
    for eps in (F(0),F(1,3),F(1,2)):
        for u in [F(-3,4),F(-1,2),F(1,4),F(2,3),F(2)]:
          for v in [F(1,3),F(1),F(2)]:
            d=a*u*u-c*v*v+eps
            if d:
              D=low_eigen(r,g,u,v,eps)
              trace=(g+a*a*u*u/d)+(g+c*c*v*v/d)
              determinant=(g+a*a*u*u/d)*(g+c*c*v*v/d)-(a*c*u*v/d)**2
              assert trace==g+D and determinant==g*D
    # Negative denominator under positive ridge 
    eps=F(1,10); u=F(0);v=F(7,12)
    assert low_eigen(r,g,u,v,eps)==F(-71,87)
    return Q

def sample_check():
    rng=Random(824526)
    cases=0
    for r,g in [(0.1,1.01),(0.5,2),(0.9,1.15),(0.6,12)]:
      n=120000
      count=0
      for j in range(n):
        u=rng.gauss(0,1); v=rng.gauss(0,1)
        count+=fail_event(r,g,u,v)
      p=probability(r,g)
      empirical=count/n
      assert abs(empirical-p)<0.013,(r,g,p,empirical)
      print('case',r,g,'analytic',p,'sample',empirical)
      cases+=1
    for r in [.1,.3,.5,.75,.9]:
      a,c=parameters(r)
      x0=sqrt(c/a)
      rr=lambda x:(a*a*x*x+c*c)/(a*x*x-c)
      constant=2*sqrt(a*c)/pi
      for M in [10000.,300000.]:
        # solve for two positive |R|=M intervals around pole via bisection
        def bisect(lo,hi,fun):
          flo=fun(lo)
          for _ in range(110):
            md=(lo+hi)/2
            if (fun(md)>0)==(flo>0):lo=md;flo=fun(lo)
            else:hi=md
          return (lo+hi)/2
        xl=bisect(x0*.01,x0*(1-1e-9),lambda x:-rr(x)-M)
        xr=bisect(x0*(1+1e-9),x0*1.8,lambda x:rr(x)-M)
        tail=2/pi*(atan(xr)-atan(xl))
        assert abs(M*tail/constant-1)<0.003,(r,M,M*tail/constant)
        print('tail',r,M,'numerical',M*tail,'constant',constant)
        # Nonattained sharp supremum over the admissible parameters.
    def poly(x): return x**4-2*x**3-2*x+1
    lo,hi=0.,1.
    for _ in range(100):
        m=(lo+hi)/2
        if poly(m)>0:lo=m
        else:hi=m
    x=(lo+hi)/2
    rr=(1-x*x)/(1+x*x)
    supremum=2/pi*(atan(x)-atan(x*x))
    assert abs(rr-0.6812500386332132)<1e-11
    assert abs(supremum-0.14215497612600075)<1e-11
    for gamma in (1.0000001,1.00001,1.01,2,10):
        assert probability(rr,gamma)<supremum
    print('supremum',rr,supremum)
    return cases

if __name__=='__main__':
    print('exact',exact_rational_test())
    print('cases',sample_check())
    print('VERIFY_OK exact_fraction_identity=true gaussian_trials=480000 tail_formula_cases=10 global_supremum_verified=true')
