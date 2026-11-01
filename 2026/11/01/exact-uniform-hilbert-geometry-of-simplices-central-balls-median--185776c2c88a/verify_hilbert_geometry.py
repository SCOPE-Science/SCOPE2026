"""Reproduce exact and numerical checks for Hilbert geometry of uniform simplices.

Python 3 standard library only. No external data or randomness required.
The analytic proof in the accompanying RESULT.md covers all dimensions.
"""
import math
from fractions import Fraction


def centered_ball_prob(m, t):
    assert m >= 2 and t >= 0
    z = math.expm1(t)
    p = 1.0
    for j in range(1, m):
        p *= j * z / (m + j * z)
    return p


def pair_prob(m, t, steps=12000):
    assert m >= 2 and t >= 0 and steps % 2 == 0
    z = math.expm1(t)
    if t > 6:
        # Logit coordinate avoids a boundary layer of width exp(-t) in u.
        lo,hi = -t-24,24
        def logit(x):
            if x > 0: return 1/(1+math.exp(-x))
            e=math.exp(x)
            return e/(1+e)
        def f(x):
            f0=logit(x)
            return m*f0*(1-f0)*(logit(x+t)-f0)**(m-1)
        h=(hi-lo)/steps
        return h/3*(f(lo)+f(hi)+sum((4 if j%2 else 2)*f(lo+j*h) for j in range(1,steps)))
    def f(u):
        return (z * u * (1-u) / (1+z*u))**(m-1)
    h = 1/steps
    s = f(0.0) + f(1.0)
    for k in range(1,steps):
        s += (4 if k%2 else 2)*f(k*h)
    return m*h*s/3


def exact_center(m, q):
    z = Fraction(q-1)
    p = Fraction(1)
    for j in range(1,m):
        p *= Fraction(j)*z/(m+j*z)
    return p


def exact_center_independent(m, q):
    # Inclusion-exclusion from the exponential-minimum integration.
    z = Fraction(q-1)
    return sum((Fraction((-1)**k * math.comb(m-1,k) * m, m + k*z)
                for k in range(m)), Fraction(0))


def mean_pair(m):
    return 2*sum(1/j for j in range(1,m))


def mean_center(m):
    return math.log(m)-sum(((-1)**(k-1))*math.comb(m,k)*math.log(k) for k in range(1,m+1))


def simpson(f, low, hi, n=20000):
    h=(hi-low)/n
    return h/3*(f(low)+f(hi)+sum((4 if j%2 else 2)*f(low+h*j) for j in range(1,n)))


def exp_samples_deterministic(m, n):
    # Deterministic low-discrepancy-like sequence for numerical diagnostics only.
    # Each coordinate avoids 0, 1 and spans a different irrational rotation.
    g=(math.sqrt(5)-1)/2
    for k in range(n):
        yield [-math.log(1-((k+1)*((j+1)*g)%1)) for j in range(m)]


def strict_symmetric_jensen_witness(a):
    # Explicit positive-measure strict Jensen witness for a nonconstant vector.
    i=min(range(len(a)),key=lambda k:a[k]); j=max(range(len(a)),key=lambda k:a[k])
    assert a[i]<a[j]
    mid=(a[i]+a[j])/2
    z=[a[k]-mid for k in range(len(a))]
    z[i]=z[j]=0
    b=list(a); b[i],b[j]=b[j],b[i]
    def spread(vals): return max(vals)-min(vals)
    f1=spread([a[k]-z[k] for k in range(len(a))])
    f2=spread([b[k]-z[k] for k in range(len(a))])
    fm=spread([.5*(a[k]+b[k])-z[k] for k in range(len(a))])
    assert f1>0 and f2>0 and fm<.5*(f1+f2)
    return f1,f2,fm


def run():
    checks=0
    for m in range(2,16):
        for q in (2,3,4,7,11):
            a=exact_center(m,q); b=exact_center_independent(m,q)
            assert a==b,(m,q,a,b)
            checks+=1
    assert abs(centered_ball_prob(2,math.log(3))-0.5)<1e-13
    checks+=1
    # Direct integrate expectation of C from exact CDF and compare alternating sum.
    for m in range(2,9):
        val=simpson(lambda t: 1-centered_ball_prob(m,t),0,50,20000)
        assert abs(val-mean_center(m))<1e-6,(m,val,mean_center(m))
        checks+=1
    # Pair CDF is a logistic order-statistic range distribution.
    # m=2 has independently integrated expression E|Z1-Z2|=2.
    for m in range(2,8):
        cdf=pair_prob(m,2.0)
        assert 0<cdf<1
        integ=simpson(lambda t: 1-pair_prob(m,t,600),0,35,1600)
        assert abs(integ-mean_pair(m))<0.00015,(m,integ,mean_pair(m))
        checks+=1
    for m in (2,3,4,7,12,20):
        a=[j/3 for j in range(m)]
        strict_symmetric_jensen_witness(a)
        checks+=1
    # Independent numerical integral for two-point CDF via conditional range of logistic law.
    for m in (2,3,6,9):
        for t in (0.3,1.0,2.4):
            a=pair_prob(m,t,12000)
            def fz(z):
                l=lambda v: 1/(1+math.exp(-v))
                F=l(z); Fc=l(z+t)
                pdf=F*(1-F)
                return m*pdf*(Fc-F)**(m-1)
            b=simpson(fz,-20,20,16000)
            assert abs(a-b)<3e-8,(m,t,a,b)
            checks+=1
    # Exact endpoint at t->0 agrees with coefficient and fixed-m upper tail.
    for m in range(2,8):
        t=1e-5
        p=centered_ball_prob(m,t)
        coeff=math.factorial(m-1)/m**(m-1)
        assert abs(p/t**(m-1)/coeff-1)<0.0001,(m,p)
        t=25
        tail=1-centered_ball_prob(m,t)
        expected=m*sum(1/j for j in range(1,m))*math.exp(-t)
        assert abs(tail/expected-1)<0.0001,(m,tail,expected)
        checks+=2
    # Verify projective metric agrees with an independent barycentric formula.
    for m in range(2,10):
        for shift in (0.1,0.4,1.1):
            v=[0.1+(k+1)*shift for k in range(m)]
            w=[0.2+(m-k)*shift*shift for k in range(m)]
            ps=sum(v); qs=sum(w)
            p=[x/ps for x in v]; q=[x/qs for x in w]
            a=[math.log(x/y) for x,y in zip(p,q)]
            b=[math.log(x/y) for x,y in zip(v,w)]
            assert abs((max(a)-min(a))-(max(b)-min(b)))<1e-12
            checks+=1
    # In dimension one the translated Hilbert ball is a logit interval;
    # its Euclidean length decreases strictly away from the centroid.
    for t in (0.1,0.7,2.0,5.0):
        logistic=lambda z:1/(1+math.exp(-z))
        length=lambda y:logistic(y+t)-logistic(y-t)
        for y in (0.2,0.6,1.0,2.0,5.0):
            assert length(y)<length(0.0)
            checks+=1
    # Check limit CDF of C_m with centering log(m)+log(log m).
    for m in (500,5000,100000):
        for x in (-1.0,0.0,1.0):
            p=centered_ball_prob(m,math.log(m)+math.log(math.log(m))+x)
            target=math.exp(-math.exp(-x))
            assert abs(p-target)<(0.18 if m==500 else 0.09),(m,x,p,target)
            checks+=1
    print('ALL CHECKS PASSED:',checks)
    print('Center mean m=2:',mean_center(2),'expected 2log2:',2*math.log(2))
    print('Pair mean m=5:',mean_pair(5))
    print('Representative P(C_5<=log 3):',centered_ball_prob(5,math.log(3)))
    print('Representative P(D_5<=2):',pair_prob(5,2))

if __name__=='__main__': run()
