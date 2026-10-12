"""Exact finite-horizon sanity checks for scalar without-replacement gradient epochs.

The infinite-horizon theorem uses an analytical spectral-measure argument,
not finite enumeration. This program independently enumerates update histories.
"""
from fractions import Fraction as Q
from itertools import product

def epoch(x, a, b, c, h, s):
    # s=+1 uses component 1 then 2; s=-1 uses 2 then 1.
    if s == 1:
        x -= h * (a*x+c)
        x -= h * (b*x-c)
    else:
        x -= h * (b*x-c)
        x -= h * (a*x+c)
    return x

def moments_direct(k, a, b, c, h, r, x0):
    total_m = Q(0); total_sq = Q(0); mass = Q(0)
    for signs in product((1,-1), repeat=k):
        p = Q(1,2)
        for i in range(1,k):
            p *= (1+r)/2 if signs[i] == signs[i-1] else (1-r)/2
        x = x0
        for s in signs:
            x = epoch(x,a,b,c,h,s)
        mass += p
        total_m += p*x
        total_sq += p*x*x
    assert mass == 1
    return total_m,total_sq

def moments_formula(k,a,b,c,h,r,x0):
    g=(1-h*a)*(1-h*b)
    m=h*h*c*(b-a)/2
    d=h*h*c*(a+b)/2
    mean=g**k*x0 + m*(1-g**k)/(1-g)
    var = d*d*sum((g**(i+j)*r**abs(i-j) for i in range(k) for j in range(k)),Q(0))
    return mean, mean*mean+var

def stationary(a,b,c,h,r):
    g=(1-h*a)*(1-h*b)
    m=h*h*c*(b-a)/2
    d=h*h*c*(a+b)/2
    assert abs(g)<1
    return (m/(1-g))**2 + d*d*(1+g*r)/((1-g*g)*(1-g*r))

def sharp_bounds(a,b,c,h):
    g=(1-h*a)*(1-h*b)
    m=h*h*c*(b-a)/2
    d=h*h*c*(a+b)/2
    bias=(m/(1-g))**2
    return bias + (d/(1+abs(g)))**2, bias + (d/(1-abs(g)))**2

def main():
    n=0
    for h in (Q(1,4),Q(3,4),Q(5,4)):
        a,b=Q(2),Q(1)
        g=(1-h*a)*(1-h*b)
        assert abs(g)<1
        for c in (Q(1),Q(-2)):
          for x0 in (Q(0),Q(3)):
            for r in (Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)):
              for k in range(1,9):
                assert moments_direct(k,a,b,c,h,r,x0)==moments_formula(k,a,b,c,h,r,x0), (h,c,x0,r,k)
                n+=1
              lo,hi=sharp_bounds(a,b,c,h)
              assert lo<=stationary(a,b,c,h,r)<=hi
              assert stationary(a,b,c,h, -1 if g>0 else 1)==lo
              assert stationary(a,b,c,h, 1 if g>0 else -1)==hi
              n+=4
    # The sign transition is not an artifact of simulations: these are exact identities.
    for h,g in ((Q(1,4),Q(3,8)),(Q(3,4),Q(-1,8)),(Q(5,4),Q(3,8))):
        assert (1-2*h)*(1-h)==g
        n+=1
    # Exact strong-convexity/stable-single-step family with a growing policy gap.
    for N in (3, 5, 10, 25, 100):
        a,b,c=Q(N),Q(1),Q(1)
        h=Q(2*N-1,N*N)
        g=(1-h*a)*(1-h*b)
        assert 0 < abs(1-h*a) < 1 and 0 < abs(1-h*b) < 1
        assert g == -(1-Q(1,N))**3
        lo,hi=sharp_bounds(a,b,c,h)
        v=(Q(N-1,N+1))**2
        r=(1-Q(1,N))**3
        ratio=(v+((1+r)/(1-r))**2)/(1+v)
        assert hi/lo==ratio and ratio>1
        n+=1
    # Equality classification follows analytically from spectral support at theta=0 or pi.
    print(f"PASS: {n} exact rational comparisons; infinite-horizon bounds proved analytically.")

if __name__=='__main__':
    main()
