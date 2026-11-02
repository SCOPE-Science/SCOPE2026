"""Reproduce the prime-two-cycle threshold for a two-branch cosine interval map.
All assertions are finite numerical checks; uniqueness for all parameters is proved separately.
Requires Python 3.9+ standard library only.
"""
from math import pi, sin, cos, acos, sqrt


def bisect(f, lo, hi, n=90):
    flo, fhi = f(lo), f(hi)
    assert flo * fhi < 0, (flo, fhi, lo, hi)
    for _ in range(n):
        mid = (lo + hi) / 2
        fm = f(mid)
        if fm == 0: return mid
        if fm * flo < 0: hi, fhi = mid, fm
        else: lo, flo = mid, fm
    return (lo + hi) / 2


def data(a):
    k = pi*(1-a)
    theta = acos(pi/(2*k))/pi
    C = lambda x: cos(k*cos(pi*x))
    Cp = lambda x: k*pi*sin(pi*x)*sin(k*cos(pi*x))
    Cpp = lambda x: k*pi*pi*cos(pi*x)*sin(k*cos(pi*x)) - k*k*pi*pi*sin(pi*x)**2*cos(k*cos(pi*x))
    xstar = bisect(lambda x: C(x)-x*Cp(x),theta+1e-10, .5)
    cstar = xstar/C(xstar)
    assert 0 < theta < xstar < .5
    assert 0 < cstar < .5
    assert Cpp(xstar) < 0
    assert abs(cstar*Cp(xstar)-1) < 5e-12
    return theta, xstar, cstar, C, Cp, Cpp


def test(a):
    theta,xstar,cstar,C,Cp,Cpp=data(a)
    print(f'a={a:.4f}, theta={theta:.12f}, x*={xstar:.12f}, c*={cstar:.12f}')
    def L(x): return 1-(1-a)*cos(pi*x)
    for c in (cstar*.9, cstar, (cstar+.5)/2, cstar+.75*(.5-cstar)):
        def R(x): return -c*cos(pi*x)
        def F(x): return L(x) if x<=.5 else R(x)
        def eq(x): return c*C(x)-x
        roots=[]
        if c>cstar+1e-12:
            roots=[bisect(eq,theta+1e-10,xstar), bisect(eq,xstar,.5)]
        elif c>=cstar-1e-12:
            roots=[xstar]
        for x in roots:
            y=F(x)
            assert .0 < x < .5 < y < 1.0
            assert abs(F(y)-x) < 3e-12
            multiplier=c*Cp(x)
            assert abs((1-a)*pi*sin(pi*x)*c*pi*sin(pi*(1-y))-multiplier)<1e-11
            if c>cstar+1e-12:
                if x<xstar: assert multiplier>1
                else: assert 0<multiplier<1
            else: assert abs(multiplier-1)<5e-12
        # Locate every zero of return function on the admissible branch independently.
        xs=[theta+1e-9+(.5-theta-2e-9)*j/10000 for j in range(10001)]
        changes=[(u,v) for u,v in zip(xs,xs[1:]) if eq(u)*eq(v)<0]
        assert len(changes) == (2 if c>cstar+1e-12 else 0), (a,c,len(changes))
        if c<cstar-1e-12:assert all(eq(x)<0 for x in xs)
    # Square-root fold and multipliers (two independent offsets).
    D=sqrt(-2*C(xstar)/(cstar*Cpp(xstar)))
    for d in (1e-5, 1e-6):
        c=cstar+d
        lo=bisect(lambda x: c*C(x)-x,theta+1e-10,xstar)
        hi=bisect(lambda x: c*C(x)-x,xstar,.5)
        assert abs((hi-lo)/(2*sqrt(d))/D-1) < 0.05
        assert abs((c*Cp(lo)-1)/sqrt(d) + cstar*Cpp(xstar)*D) < .07
        assert abs((1-c*Cp(hi))/sqrt(d) + cstar*Cpp(xstar)*D) < .07
    print('  fold coefficient',D,'stable / unstable verified')


for a in (.25,.30,.37,.45,.49):test(a)
print('PASS: 5 parameter slices, 20 finite graph scans, 10 local fold tests')
