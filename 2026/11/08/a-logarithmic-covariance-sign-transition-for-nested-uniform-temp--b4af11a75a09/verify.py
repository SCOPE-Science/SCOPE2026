"""Reproducible algebra, finite-depth and Monte Carlo checks for the temporal-tree covariance theorem.
Standard library only; finite tests are diagnostics, not an infinite proof.
"""
from fractions import Fraction as Q
from math import exp, expm1, log, sqrt
from random import Random


def moment_covariance(n,p,q):
    a=exp(n*p); b=exp(n*q)
    moment2=(2-2/n)*a*a+(2*p-1+2/n)*a
    variance=moment2-a*a
    return variance-(a-1)*(b-a)/n


def factorized_covariance(n,p,q):
    v=n-1+2*n*p/expm1(n*p)
    return exp(2*n*p)*(-__import__('math').expm1(-n*p))/n*(v-exp(n*(q-p)))


def normalized_covariance(n,p,q):
    gap=n*(q-p)
    return (-__import__('math').expm1(-n*p))/n*((n-1+2*n*p/expm1(n*p))*exp(-gap)-1)

def normalized_variance(n,p):
    return 1-2/n+(2*p-1+2/n)*exp(-n*p)

def crossing(n,p):
    return p+log(n-1+2*n*p/expm1(n*p))/n


def add(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c


def scale(a,c): return [c*x for x in a]
def integral(a): return [Q(0)]+[x/Q(i+1) for i,x in enumerate(a)]

def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def val(a,z):
    s=Q(0)
    for x in a[::-1]:s=s*z+x
    return s


def depth_covariance(n,p,q,depth):
    # Independent polynomial recursion for trees restricted to depth <= depth.
    # The normalized source has exactly n independent root-child contributions.
    m=[Q(1)]; second=[Q(1)]
    for d in range(depth):
        old_m=integral(m);old_second=integral(second)
        m=add([Q(1)],scale(old_m,n))
        second=add(add(mul(m,m),scale(old_second,n)),scale(mul(old_m,old_m),-n))
    # Previous generation moment needed for pair's disjoint root interval;
    # ∫ mean_sub = (m(p)-1)/n at this truncated depth.
    var=val(second,p)-val(m,p)**2
    low=(val(m,p)-1)/n
    high=(val(m,q)-val(m,p))/n
    return float(var-n*low*high)


def sample(n,p,q,rng):
    a=b=1
    stack=[]
    for _ in range(n):
        u=rng.random()
        if u<q:
            flag=u<p
            a+=flag;b+=1
            stack.append((u,flag))
    while stack:
        parent,flag=stack.pop()
        for _ in range(n):
            u=rng.random()
            if u<parent:
                a+=flag;b+=1
                stack.append((u,flag))
    return a,b


def run():
    tests=0
    for n in [1,2,3,5,8]:
        for p in [.12,.28,.4,.64,.85]:
            for q in [p,(p+1)/2,1.]:
                a=moment_covariance(n,p,q);b=factorized_covariance(n,p,q)
                assert abs(a-b)<=3e-11*(1+abs(a)+abs(b)),(n,p,q,a,b)
                tests+=1
                star=crossing(n,p)
                assert star>p
                tests+=1
                if star<=1:
                    assert moment_covariance(n,p,star*.5+p*.5)>0
                    assert moment_covariance(n,p,(1+star)/2)<0
                    tests+=2
    n,p,q=2,Q(2,5),Q(9,10)
    exact=moment_covariance(n,float(p),float(q))
    errors=[]
    for d in [5,8,11,14,17]:
        c=depth_covariance(n,p,q,d)
        errors.append(abs(c-exact))
        assert errors[-1]<10 if d==5 else errors[-2],(d,errors)
        tests+=1
    assert errors[-1]<1e-8,(errors,exact)
    tests+=1
    for p in [.2,.4,.7]:
        for x in [-1.,0.,1.]:
            n=600
            q=p+(log(n)+x)/n
            assert q<=1
            norm=normalized_covariance(n,p,q)*exp(n*(q-p))
            assert abs(norm-(1-exp(x)))<.02,(p,x,norm)
            tests+=1
        for t in [0.,.5,2.,5.]:
            n=600;q=p+t/n
            norm=normalized_covariance(n,p,q)
            varp=normalized_variance(n,p)
            varq=normalized_variance(n,q)
            corr=norm/sqrt(varp*varq)
            assert abs(corr-exp(-t))<.01,(p,t,corr)
            tests+=1
    rng=Random(20261102)
    for n,p,q in [(1,.35,.95),(2,.4,.9),(3,.3,.95),(3,.4,.6)]:
        trials=14000
        draws=[sample(n,p,q,rng) for _ in range(trials)]
        ap=sum(a for a,b in draws)/trials
        aq=sum(b for a,b in draws)/trials
        avg=sum(a*b for a,b in draws)/trials
        cov=avg-ap*aq
        # An empirically estimated uncertainty from the centered product.
        z=[(a-ap)*(b-aq) for a,b in draws]
        se=sqrt(max(0.,sum((x-cov)**2 for x in z)/(trials-1))/trials)
        expected=moment_covariance(n,p,q)
        assert abs(cov-expected)<8*se+.05,(n,p,q,cov,expected,se)
        tests+=1
    print('PASS',tests,'assertions; finite-depth errors',errors)

if __name__=='__main__':run()
