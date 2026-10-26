"""Independent numerical checks of the permeable-interface restart theorem.
Requires Python 3.9+ standard library only. Run: python check.py
Analytical continuum assertions are proved in RESULT.md, not certified by tests.
"""
import math
import random


def laplace_closed(z, b, eta):
    # L=D=1; eta=D/(2*kappa*L), b=barrier/target-reset distance
    return math.exp(-z) / (1 + eta*z*(1+math.exp(-2*b*z)))


def laplace_boundary(z, b, eta):
    # Direct solve for the two interval solutions u_- and u_+ of u''=z^2 u.
    kappa=1/(2*eta)
    c=1/(math.sinh(z*b) + (1+z/kappa)*math.cosh(z*b))
    return c*math.exp(-z*(1-b))


def mean_fpt(z,b,eta):
    a=1-2*b
    return math.expm1(z)/z**2+eta*(math.exp(z)+math.exp(a*z))/z


def renewed_mean(z,b,eta):
    p=laplace_closed(z,b,eta)
    return (1-p)/(z*z*p)


def first(z,b,eta):
    a=1-2*b
    return (math.exp(z)*(z-2)+2)/z**3 + eta*(math.exp(z)*(z-1)+math.exp(a*z)*(a*z-1))/z**2


def second(z,b,eta):
    a=1-2*b
    # F_0'' from integral rep (numerically stable formula for z >= .1)
    term0=(math.exp(z)*(z*z-4*z+6)-6)/z**4
    term1=(math.exp(z)*((z-1)**2+1)+math.exp(a*z)*((a*z-1)**2+1))/z**3
    return term0+eta*term1


def optimum(b,eta):
    lo=0.03; hi=16
    assert first(lo,b,eta)<0 and first(hi,b,eta)>0
    for j in range(85):
        mid=(lo+hi)/2
        if first(mid,b,eta)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def assert_close(x,y,tol=1.e-10):
    assert abs(x-y)<tol*max(1,abs(x),abs(y)),(x,y)


def main():
    random.seed(8240031)
    count=0
    for i in range(180):
        b=random.uniform(.01,.99)
        eta=10**random.uniform(-3,2)
        z=random.uniform(.1,7)
        assert_close(laplace_closed(z,b,eta),laplace_boundary(z,b,eta)); count+=1
        assert_close(mean_fpt(z,b,eta),renewed_mean(z,b,eta)); count+=1
        h=1e-5
        assert_close(first(z,b,eta),(mean_fpt(z+h,b,eta)-mean_fpt(z-h,b,eta))/(2*h),tol=1e-6);count+=1
        assert_close(second(z,b,eta),(first(z+h,b,eta)-first(z-h,b,eta))/(2*h),tol=1e-5);count+=1
        assert second(z,b,eta)>0;count+=1
        root=optimum(b,eta)
        assert abs(first(root,b,eta))<1e-7; count+=1
        assert root>0 and mean_fpt(root,b,eta)<mean_fpt(root*.75,b,eta) and mean_fpt(root,b,eta)<mean_fpt(root*1.3,b,eta);count+=1
        assert mean_fpt(z,b+.001,eta)<mean_fpt(z,b,eta) if b+.001<1 else True;count+=1
    for eta in (.001,.03,.1,.3,1.,3.,30.,300.):
        xs=[optimum(b,eta) for b in (.01,.05,.15,.25,.35,.45,.5,.55,.65,.75,.85,.95,.99)]
        assert all(xs[j]<xs[j+1] for j in range(6)) and all(xs[j]>xs[j+1] for j in range(6,12));count+=1
        assert xs.index(max(xs))==6;count+=1
    for b in (.05,.25,.5,.75,.95):
        vals=[optimum(b,eta) for eta in (0.001,.01,.1,1,10,100)]
        assert all(vals[j]>vals[j+1] for j in range(5));count+=1
    print(f'PASS: {count} deterministic tests; direct boundary, renewal, derivatives, convexity, midpoint and resistance monotonicity')

if __name__=='__main__': main()
