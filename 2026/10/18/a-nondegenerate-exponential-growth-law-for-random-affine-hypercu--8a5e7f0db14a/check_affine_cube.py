"""Reproducible checks for the asymptotic affine-cube section vertex theorem.

Requires only Python 3 standard library. Finite enumeration is diagnostic,
not a substitute for the analytic large-deviation proof.
"""
import math
import random
from itertools import product


def counts(w, t):
    # Return number of vertices of Boolean upper level set and edge crossings.
    n = len(w)
    vals = [sum(e[i]*w[i] for i in range(n)) for e in product((-1,1), repeat=n)]
    upper = sum(v>t for v in vals)
    crossings = 0
    # Binary count with coordinate 0 as highest bit in product enumeration.
    for v in range(1 << n):
        for j in range(n):
            neighbor = v ^ (1 << j)
            if v < neighbor and ((vals[v] > t) != (vals[neighbor] > t)):
                crossings += 1
    return upper, crossings


def exact_average(w):
    n=len(w)
    radius=sum(w)
    vals=sorted(set(sum(e[i]*w[i] for i in range(n)) for e in product((-1,1),repeat=n)))
    # Symmetric normal offsets and step-function vertex count integrated exactly.
    area=0.
    prev=-radius
    for nxt in vals[1:]:
        midpoint=(prev+nxt)/2
        _, k=counts(w,midpoint)
        area += k*(nxt-prev)
        prev=nxt
    return area/(2*radius)


def integrate(f, top=12.0, segments=4000):
    # Composite Simpson; sufficient for numerical diagnostics.
    if segments%2: segments+=1
    h=top/segments
    z=f(0.)+f(top)
    for i in range(1,segments):
        z+=(4 if i%2 else 2)*f(i*h)
    return z*h/3


def halfnorm_expect(fun):
    r=math.sqrt(2/math.pi)
    return integrate(lambda v:r*math.exp(-v*v/2)*fun(v),top=10.,segments=2000)


def lcosh(x):
    return abs(x) + math.log1p(math.exp(-2*abs(x))) - math.log(2)


def rate(y):
    mu=math.sqrt(2/math.pi)
    target=mu*y
    if y==0: return 0.
    lo,hi=0.,50.
    for _ in range(48):
        mid=(hi+lo)/2
        slope=halfnorm_expect(lambda x:x*math.tanh(mid*x))
        if slope<target: lo=mid
        else: hi=mid
    x=(lo+hi)/2
    return x*target - halfnorm_expect(lambda v:lcosh(x*v))


def run():
    rng=random.Random(8675309)
    comparisons=0
    for n in range(3,9):
        for _ in range(4):
            w=[abs(rng.gauss(0,1)) for i in range(n)]
            wtot=sum(w)
            for f in (.05,.18,.37,.64,.9):
                a,ed=counts(w,f*wtot)
                assert 0<a<=2**(n-1), (n,a)
                assert a<=ed<=n*a, (n,a,ed)
                comparisons+=1
            mean=exact_average(w)
            assert abs(mean - 2**(n-1))<1e-7,(n,mean)
            comparisons+=1
    # Gaussian rate monotonicity, strict support, and both sharp endpoint constants.
    uvals=[.05,.125,.25,.5,.75,.875,.95,.99]
    yy=[math.log(2)-rate(u) for u in uvals]
    assert all(a>b for a,b in zip(yy,yy[1:])), yy
    assert all(0<x<math.log(2) for x in yy)
    assert abs((math.log(2)-yy[0])/(uvals[0]**2)-1/math.pi)<.005
    # Asymptotic lower endpoint is sqrt(pi/3)*sqrt(1-u), approached from below.
    assert abs(yy[-1]/math.sqrt(1-uvals[-1]) - math.sqrt(math.pi/3)) < .045
    comparisons += len(uvals)+3
    print('AFFINE_CUBE_RANDOM_EXPONENT_OK comparisons='+str(comparisons))
    print('rate_midpoint='+format(rate(.5),'.10f'))
    print('limiting_median_exponent='+format(yy[3],'.10f'))

if __name__=='__main__':
    run()
