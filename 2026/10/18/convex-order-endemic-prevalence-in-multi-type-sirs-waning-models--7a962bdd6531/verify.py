"""Standalone checks for convex-order epidemic-equilibrium comparison.

Run: python verify.py
Only standard-library modules and SymPy (for symbolic derivatives) are needed.
The theorem is proved in RESULT.md; the checks below are finite supplements.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt


def kernel(x, h, death, recovery):
    return (1 + death*h)/(1 + x + (death + (death + recovery)*x)*h)


def zero_derivative_populations(p, h, x, death, recovery):
    f = sum((w*kernel(x,z,death,recovery) for w,z in zip(p,h)), Q(0))
    R0 = 1/f
    beta = R0*(death+recovery)
    S = [w*kernel(x,z,death,recovery) for w,z in zip(p,h)]
    I = [x*s for s in S]
    R = [recovery*z/(1+death*z)*i for z,i in zip(h,I)]
    total_I = sum(I)
    assert total_I == x/R0
    for w,z,s,i,r in zip(p,h,S,I,R):
        omega=1/z
        assert s+i+r == w
        assert death*w-beta*s*total_I+omega*r-death*s == 0
        assert beta*s*total_I-(recovery+death)*i == 0
        assert recovery*i-(omega+death)*r == 0
    return R0


def root_of_equilibrium(p,h,death,recovery,R0):
    def eq(x):
        return sum(w*kernel(x,z,death,recovery) for w,z in zip(p,h)) - 1/R0
    lo,hi = 0.0,float(R0)
    assert eq(lo)>0 and eq(hi)<0
    for _ in range(150):
        mid=(lo+hi)/2
        if eq(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/(2*R0)


def main():
    count=0
    try:
        import sympy as sp
        h,x,mu,gamma=sp.symbols('h x mu gamma', positive=True)
        B=mu+(mu+gamma)*x
        G=(1+mu*h)/(1+x+B*h)
        assert sp.simplify(sp.diff(G,h)+gamma*x/(1+x+B*h)**2)==0
        assert sp.simplify(sp.diff(G,h,2)-2*gamma*x*B/(1+x+B*h)**3)==0
        assert sp.simplify(sp.diff(G,x)+(1+mu*h)*(1+(mu+gamma)*h)/(1+x+B*h)**2)==0
        count+=3
    except ImportError:
        print('SymPy unavailable: symbolic checks skipped; rational checks proceed')

    proportions=(Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10))
    t_values=(Q(0),Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10))
    for p,mu,gamma,m,x in product(proportions,(Q(1,80),Q(1,2),Q(2)),(Q(1,10),Q(1),Q(50)),(Q(1,5),Q(1),Q(4)),(Q(1,25),Q(1,2),Q(5))):
        prev=None
        for t in t_values:
            # t parameterizes a two-atom mean-preserving spread.
            q=1-p
            h1=m*(1-t)
            h2=m*(1+p*t/q)
            F=p*kernel(x,h1,mu,gamma)+q*kernel(x,h2,mu,gamma)
            assert F > 0
            if prev is not None:
                assert F > prev
                count+=1
            prev=F
            R0=zero_derivative_populations((p,q),(h1,h2),x,mu,gamma)
            assert R0>1
            count+=1
    for p in (0.01,0.04,0.1,0.2,0.35,0.5,0.8,0.95,0.99):
        for m in (0.25,1.,3.):
            for mu,gamma,R0 in ((.0125,50.,5.),(.5,.7,1.2),(2.,1.,8.)):
                upper=sqrt(p/(1-p))
                previous=None
                for sigma in (0.,.01,.05,.1,.2,.4,.65,.8,.95):
                    sigma*=upper
                    h1=m*(1-sigma*sqrt((1-p)/p))
                    h2=m*(1+sigma*sqrt(p/(1-p)))
                    val=root_of_equilibrium((p,1-p),(h1,h2),mu,gamma,R0)
                    if previous is not None:
                        assert val > previous
                        count+=1
                    previous=val
    p=.1;mu=.0125;gamma=50.;R0=5.;m=1.
    vals=[]
    for sigma in (0.,.1,.2):
        h1=m*(1-sigma*sqrt((1-p)/p))
        h2=m*(1+sigma*sqrt(p/(1-p)))
        vals.append(root_of_equilibrium((p,1-p),(h1,h2),mu,gamma,R0))
    assert abs(vals[0]-.015878461161480027)<1e-12
    assert abs(vals[1]-.016033396184)<1e-11
    assert abs(vals[2]-.016775975596)<1e-11
    count+=3
    print(f'PASS: {count} symbolic, exact-rational, equilibrium, and numerical checks')
    print('Example: p=0.1, mean duration=1, mortality=1/80, recovery=50, R0=5')
    for sigma, prevalence in zip((0.,.1,.2),vals):
        print(f'  sigma={sigma:.1f}: endemic infected fraction={prevalence:.12f}')


if __name__=='__main__':
    main()
