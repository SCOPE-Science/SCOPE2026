"""Independent numerical checks of finite-path sharp interpolation formulas.
Requires only the Python standard library. This does not prove infinite claims.
"""
from math import cos, pi, sqrt, sinh, cosh, asinh, exp

def solve_tridiagonal(n, x, column):
    # Thomas elimination for x^2 I + path Laplacian, solve at a unit vertex.
    d=[x*x+(1 if i in (0,n-1) else 2) for i in range(n)]
    y=[1.0 if i==column else 0.0 for i in range(n)]
    for i in range(1,n):
        w=-1/d[i-1]
        d[i]+=w
        y[i]-=w*y[i-1]
    y[-1]/=d[-1]
    for i in range(n-2,-1,-1):
        y[i]=(y[i]+y[i+1])/d[i]
    return y

def diagonal_closed(n,j,x):
    e=2*asinh(x/2)
    return cosh((j+.5)*e)*cosh((n-j-.5)*e)/(sinh(e)*sinh(n*e))

def green_spectrum(n,j,x):
    return 2/n*sum(cos(pi*k*(j+.5)/n)**2/(x*x+2-2*cos(pi*k/n)) for k in range(1,n))

def endpoint_variational(n,x):
    e=2*asinh(x/2)
    if n*e>18:
        return sqrt(4+x*x)-x-2/(n*x) # exponential correction < 1e-14
    return (sqrt(4+x*x)-x)*(1+exp(-(2*n-1)*e))/(-__import__('math').expm1(-2*n*e))-2/(n*x)

def max_constant(n):
    # First bracket globally by a log-spaced scan; then refine by golden section.
    pts=[10**(-5+7*k/500) for k in range(501)]
    i=max(range(len(pts)),key=lambda k:endpoint_variational(n,pts[k]))
    lo=pts[max(0,i-1)]; hi=pts[min(500,i+1)]
    a=(sqrt(5)-1)/2
    c=hi-a*(hi-lo); d=lo+a*(hi-lo)
    for _ in range(120):
        if endpoint_variational(n,c)<endpoint_variational(n,d):
            lo=c;c=d;d=lo+a*(hi-lo)
        else:
            hi=d;d=c;c=hi-a*(hi-lo)
    x=(lo+hi)/2
    return x,endpoint_variational(n,x)

def checks():
    for n in range(2,13):
        for x in (.21,.65,1.3,2.4):
            for j in range(n):
                a=solve_tridiagonal(n,x,j)[j]
                b=diagonal_closed(n,j,x)
                c=green_spectrum(n,j,x)+1/(n*x*x)
                assert abs(a-b)<2e-10,(n,j,x,a,b)
                assert abs(a-c)<2e-10,(n,j,x,a,c)
                assert b<=diagonal_closed(n,0,x)+1e-11
            assert abs(endpoint_variational(n,x)-2*x*(diagonal_closed(n,0,x)-1/(n*x*x)))<1e-10
    previous=0
    for n in (2,3,4,5,10,20,50,100,1000,10000):
        x,k=max_constant(n)
        assert previous<k<2,(n,k)
        previous=k
        if n>=100:
            expansion=2-2*sqrt(2/n)+1/(2*n)+sqrt(2)/(8*n**1.5)
            assert abs(k-expansion)<.5/n**2,(n,k,expansion)
        print(f'N={n}  x={x:.10g}  sharp={k:.12f}')
    assert abs(max_constant(2)[1]-1/(2*sqrt(2)))<1e-10
    print('All direct tridiagonal, Fourier, extremal-position and asymptotic checks passed.')

if __name__=='__main__': checks()
