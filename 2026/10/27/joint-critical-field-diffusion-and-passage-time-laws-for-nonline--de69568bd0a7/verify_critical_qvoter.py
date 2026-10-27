"""Finite-state reproducibility checks for a critical nonlinear voter model."""
import math
import numpy as np
from scipy.integrate import quad


def rates(n, s, zp, zm, q):
    up = (s-n)*((n+zp)/(s+zp+zm-1))**q if n<s else 0.0
    down = n*((s-n+zm)/(s+zp+zm-1))**q if n>0 else 0.0
    return up,down


def parameters(N,q,theta,eta):
    S = min(N-2, max(2, round(N/q+theta*math.sqrt(N))))
    d = round(eta*N**0.25)
    if (N-S-d)%2: d += 1
    zp,zm=(N-S+d)//2,(N-S-d)//2
    assert min(zp,zm)>0
    return S,zp,zm


def exact_prob(N,S,zp,zm,q):
    lw=np.zeros(S+1)
    for k in range(1,S+1):
        lw[k]=lw[k-1]+math.log(S-k+1)-math.log(k)+q*(math.log(k-1+zp)-math.log(S-k+zm))
    w=np.exp(lw-np.max(lw));return w/w.sum()


def limiting_moments(q,theta,eta):
    A=2*q*q*theta;B=2*q*eta;C=4*q*(q*q-1)/3
    shift=lambda x: A*x*x+B*x-C*x**4
    def integ(fn):return quad(lambda x:fn(x)*math.exp(shift(x)),-6,6,epsabs=1e-11)[0]
    z=integ(lambda x:1)
    return np.array([integ(lambda x:x)/z,integ(lambda x:x*x)/z,integ(lambda x:x**3)/z]),z


def finite_moments(N,q,theta,eta):
    S,zp,zm=parameters(N,q,theta,eta)
    k=np.arange(S+1);x=(k-S/2)/N**0.75
    p=exact_prob(N,S,zp,zm,q)
    return np.array([sum(p*x),sum(p*x*x),sum(p*x**3)]), (S,zp,zm)


def check_exact():
    tests=0
    for N in (8,12,17,21):
      for q in (2,3):
       for zp in (1,2):
        for zm in (1,2):
         if zp+zm>=N-1:continue
         S=N-zp-zm;p=exact_prob(N,S,zp,zm,q)
         assert abs(p.sum()-1)<2e-13
         for k in range(S):
          u,_=rates(k,S,zp,zm,q)
          _,d=rates(k+1,S,zp,zm,q)
          assert abs(p[k]*u-p[k+1]*d)<3e-12
          tests+=1
    print('exact detailed-balance identities:',tests)


def check_generators():
    tests=0
    for q,theta,eta in ((2,0,0),(2,0.3,0.75),(3,-0.4,-0.6),(4,0.2,0.5)):
      for N in (20000,80000,320000):
       S,zp,zm=parameters(N,q,theta,eta)
       for x in (-1.2,-0.5,0,0.5,1.2):
        k=max(1,min(S-1,round(S/2+x*N**0.75)))
        xx=(k-S/2)/N**0.75
        u,d=rates(k,S,zp,zm,q)
        drift=(u-d)/N**0.25
        vari=(u+d)/N
        drift_inf=(2**(1-q)*q*theta*xx+2**(-q)*eta-2**(3-q)*(q*q-1)*xx**3/3)
        var_inf=2**(-q)/q
        err=abs(drift-drift_inf)+abs(vari-var_inf)
        assert err<0.08, (q,N,xx,err,drift,drift_inf)
        tests+=1
    print('generator drift/diffusion numerical comparisons:',tests)


def check_density():
    tests=0
    for q,theta,eta in ((2,0,0),(2,0.3,0.75),(3,-0.4,-0.6),(4,0.2,0.5)):
      limit,_=limiting_moments(q,theta,eta)
      errors=[]
      for N in (2000,8000,32000):
        m,_=finite_moments(N,q,theta,eta)
        err=max(abs(m-limit));errors.append(err)
        assert err<0.08,(q,N,err)
        tests+=1
      print('q theta eta',q,theta,eta,'moment max errors',errors)
      assert errors[-1]<0.06,(q,errors)
    print('critical density moment comparisons:',tests)


if __name__=='__main__':
    check_exact();check_generators();check_density()
    print('ALL_CHECKS_PASS')


def finite_mean_up(N,q,theta,eta,a,b):
    S,zp,zm=parameters(N,q,theta,eta)
    lo=round(S/2+a*N**.75);hi=round(S/2+b*N**.75)
    lo=max(0,min(S-1,lo));hi=max(lo+1,min(S,hi))
    p=exact_prob(N,S,zp,zm,q)
    F=np.cumsum(p)
    out=0.0
    for j in range(lo,hi):
        u,_=rates(j,S,zp,zm,q)
        out+=F[j]/(u*p[j])
    return out/N**.5


def limiting_mean_up(q,theta,eta,a,b):
    A=2*q*q*theta;B=2*q*eta;C=4*q*(q*q-1)/3
    g=lambda x:math.exp(A*x*x+B*x-C*x**4)
    sigma2=2**(-q)/q
    # Normalization cancels between F and f.
    def ratio(x):
        left=quad(g,-7,x,epsabs=1e-11)[0]
        return left/g(x)
    return 2/sigma2*quad(ratio,a,b,epsabs=1e-10)[0]


def check_passage():
    cases=[(2,0.,0.,-.35,.35),(2,.3,.75,-.35,.35),(3,-.4,-.6,-.3,.3)]
    for q,th,eta,a,b in cases:
        pred=limiting_mean_up(q,th,eta,a,b)
        got=[finite_mean_up(N,q,th,eta,a,b) for N in (4000,12000,36000)]
        errs=[abs(t-pred)/pred for t in got]
        print('mean passage',q,th,eta,'limit',pred,'values',got,'relative errors',errs)
        assert errs[-1]<0.15
    print('mean passage checks: 9; ALL_PASS')

if __name__=='__main__':
    check_passage()


def finite_mean_down(N,q,theta,eta,a,b):
    S,zp,zm=parameters(N,q,theta,eta)
    lo=max(0,min(S-1,round(S/2+a*N**.75)))
    hi=max(lo+1,min(S,round(S/2+b*N**.75)))
    p=exact_prob(N,S,zp,zm,q)
    F=np.cumsum(p[::-1])[::-1]
    result=0.0
    for j in range(lo+1,hi+1):
        _,d=rates(j,S,zp,zm,q)
        result+=F[j]/(d*p[j])
    return result/N**.5


def limiting_mean_down(q,theta,eta,a,b):
    A=2*q*q*theta;B=2*q*eta;C=4*q*(q*q-1)/3
    g=lambda x:math.exp(A*x*x+B*x-C*x**4)
    sigma2=2**(-q)/q
    def ratio(x):
        right=quad(g,x,7,epsabs=1e-11)[0]
        return right/g(x)
    return 2/sigma2*quad(ratio,a,b,epsabs=1e-10)[0]


def check_down_passage():
    tests=0
    for q,th,eta in ((2,0.,0.),(2,.3,.75),(3,-.4,-.6)):
        a,b=-.35,.35
        goal=limiting_mean_down(q,th,eta,a,b)
        got=[finite_mean_down(N,q,th,eta,a,b) for N in (4000,12000,36000)]
        errs=[abs(v-goal)/goal for v in got]
        print('down passage',q,th,eta,'limit',goal,'finite',got,'relerror',errs)
        assert errs[-1]<0.15,(q,errs)
        tests+=len(got)
    print('downward mean passage comparisons:',tests,'ALL_PASS')

if __name__=='__main__':
    check_down_passage()
