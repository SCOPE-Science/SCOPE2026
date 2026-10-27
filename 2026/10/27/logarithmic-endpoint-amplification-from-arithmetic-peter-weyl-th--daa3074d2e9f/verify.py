"""Independent finite checks for arithmetic Peter--Weyl endpoint projections."""
import cmath
import math


def direct(q, r, m, theta):
    return sum((q*k+r)*math.sin((q*k+r)*theta) for k in range(m))


def geometric(q, r, m, theta):
    z = cmath.exp(1j*q*theta)
    den = 1-z
    if abs(den) < 1e-6:
        return direct(q, r, m, theta)
    a = cmath.exp(1j*r*theta)
    val = a*(-q*m*z**m/den + q*z*(1-z**m)/den**2 + r*(1-z**m)/den)
    return val.imag


def endpoint_norm(q, r, m, n=120000):
    acc=0.0
    for j in range(n):
        theta=(j+0.5)*math.pi/n
        acc+=abs(geometric(q,r,m,theta))*math.sin(theta)
    return 2*acc/n


def test():
    checks=0
    for q in (2,3,4,5,7):
        for r in range(1,q+1):
            for m in (1,2,3,9,24):
                for j in range(1,80):
                    theta=(j+0.31871)*math.pi/80
                    if abs(1-cmath.exp(1j*q*theta))<0.025:
                        continue
                    x=direct(q,r,m,theta)
                    y=geometric(q,r,m,theta)
                    assert abs(x-y)<2e-8*(1+abs(x)),(q,r,m,j,x,y)
                    checks+=1
    # Positive logarithmic resonance for all q>=3, whereas q=2 lacks an interior pole.
    for q in (3,4,5):
        predicted=8/math.pi**2*sum(math.sin(2*math.pi*h/q) for h in range(1,(q-1)//2+1))
        ns=[220,460,940]
        norms=[endpoint_norm(q,1,m) for m in ns]
        # Finite differences suppress the unknown O(M) intercept.
        slopes=[(norms[i+1]/ns[i+1]-norms[i]/ns[i]) / math.log(ns[i+1]/ns[i]) for i in (0,1)]
        print('q',q,'predicted slope',predicted,'empirical slopes',slopes)
        assert abs(slopes[1]-predicted)<0.40
        checks+=2
    n2a=endpoint_norm(2,1,220)
    n2b=endpoint_norm(2,1,940)
    assert n2a/220<2 and n2b/940<2
    checks+=2
    print('finite checks:',checks)

if __name__=='__main__':
    test()
