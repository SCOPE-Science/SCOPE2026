"""Reproducibility checks for a high-order cardinal-spline Zak asymptotic.
Requires only the Python standard library. Run: python CHECKER.py
"""
import cmath
import math

BASE = 2.0 / math.pi


def bspline(m, t):
    # Centered m-fold convolution of the unit box; suitable at modest m.
    a = t + m / 2.0
    return sum((-1)**k * math.comb(m, k) * max(0.0, a-k)**(m-1)
               for k in range(m+1)) / math.factorial(m-1)


def zak_time(m, x, w):
    L = (m+3)//2+2
    return sum(bspline(m, x-k) * cmath.exp(2j*math.pi*k*w)
               for k in range(-L, L+1))


def zak_freq(m, x, w):
    # Two dozen aliases suffice for the displayed finite m>=6 tests.
    z = 0j
    for n in range(-14, 15):
        v = n+w
        b = math.sin(math.pi*v)/(math.pi*v) if abs(v)>1e-13 else 1.0
        z += b**m * cmath.exp(2j*math.pi*v*x)
    return z


def profile(x, s):
    return cmath.exp(-2*s+1j*math.pi*x)+cmath.exp(2*s-1j*math.pi*x)


def exact_derivative_ratios(m):
    # Finite tail is below 1e-13 for m>=10.
    sx = sum((-1)**(j*(m+1))*(2*j+1)**(1-m) for j in range(200))
    sw = sum((-1)**(j*(m+1))*(2*j+1)**(-m-1) for j in range(200))
    return sx,sw


def integral_A(tau, N=25000):
    # Midpoint quadrature of the derived one-dimensional profile area.
    acc = 0.0
    for j in range(N):
        x = (j+0.5)/N
        v = tau*tau/4-math.cos(math.pi*x)**2
        if v>0:
            acc += math.asinh(math.sqrt(v))
    return acc/N


def scaled_sublevel_area(m, tau, nx=201, ns=401, bound=0.42):
    # Integrate in (x,s), s=m(w-1/2); the result equals m times physical area.
    hits = 0
    for ix in range(nx):
        x=(ix+0.5)/nx
        for js in range(ns):
            s=-bound+(js+0.5)*(2*bound/ns)
            if abs(zak_freq(m,x,0.5+s/m))/BASE**m <= tau:
                hits += 1
    return hits*(2*bound)/(nx*ns)


def main():
    tests=0
    for m in (6,8):
        for x in (0.11,0.39,0.64):
            for w in (0.12,0.33,0.50):
                diff=abs(zak_time(m,x,w)-zak_freq(m,x,w))
                assert diff<2e-8,(m,x,w,diff)
                tests+=1
    print('Poisson/time-domain comparisons:',tests,'passed')

    errs=[]
    for m in (60,120,240):
        err=max(abs(zak_freq(m,x,0.5+s/m)/BASE**m-profile(x,s))
                for x in (0.10,0.31,0.50,0.76,0.92)
                for s in (-0.8,-0.3,0,0.4,0.8))
        errs.append(err)
        print('Profile max error at order',m,':',format(err,'.9f'))
    assert errs[0]>errs[1]>errs[2] and errs[2]<0.2

    # Differentiate the independently evaluated time-domain spline sum.
    for m in (6,8):
        h=1e-5
        sx,sw=exact_derivative_ratios(m)
        dx=(zak_time(m,0.5+h,0.5)-zak_time(m,0.5-h,0.5))/(2*h)
        dw=(zak_time(m,0.5,0.5+h)-zak_time(m,0.5,0.5-h))/(2*h)
        assert abs(dx+2*math.pi*BASE**m*sx)<5e-6
        assert abs(dw+4j*m*BASE**m*sw)<5e-6
    print('Time-domain finite-difference derivative comparisons: 4 passed')

    for m in (10,20,40,80):
        sx,sw=exact_derivative_ratios(m)
        assert sx>0 and sw>0
        assert abs(sx-1)<4*3**(1-m)
        assert abs(sw-1)<4*3**(-m-1)
    print('Exact derivative sums and positive real Jacobian: 4 passed')

    area=integral_A(1.0)
    print('Limit area A(1):',format(area,'.10f'))
    assert abs(area-0.12566521685664614)<3e-5
    results=[]
    for m in (40,80,160):
        measure=scaled_sublevel_area(m,1.0)
        results.append(measure)
        print('m * sublevel-area estimate at order',m,':',format(measure,'.9f'))
        assert abs(measure-area)<0.008
    assert abs(results[-1]-area)<abs(results[0]-area)
    print('All reproducibility checks passed. Infinite claims rest on analysis, not grids.')

if __name__=='__main__':
    main()
