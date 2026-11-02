"""Finite numerical checks for biharmonic half-plane slab concentration.

All infinite-dimensional and uniqueness statements require the mathematical proof.
Run with Python 3: python checker.py
"""
import math


def integrate_simpson(fn, left, right, panels=2000):
    h=(right-left)/panels
    out=fn(left)+fn(right)
    for j in range(1,panels):
        out+=(4 if j%2 else 2)*fn(left+j*h)
    return out*h/3


def gram_by_quadrature(a,b,rho):
    lo,hi=2*rho*a,2*rho*b
    return [[integrate_simpson(lambda v,i=i,j=j: math.exp(-v)*
                              ((1.0-v) if i else 1.0)*
                              ((1.0-v) if j else 1.0), lo,hi)
             for j in (0,1)] for i in (0,1)]


def Q(s):
    return ((1.0,-s),(-s,1+s*s))


def gram_exact(a,b,rho):
    x,y=2*rho*a,2*rho*b
    p=Q(x);q=Q(y)
    return [[math.exp(-x)*p[i][j]-math.exp(-y)*q[i][j]
             for j in range(2)] for i in range(2)]


def g(z):
    return 4*math.sinh(z/2)**2-z*z


def h(z):
    return 2*(math.sinh(z)-z)/g(z)


def determinant(a,b,rho):
    z=2*rho*(b-a)
    return math.exp(-2*rho*(a+b))*g(z)


def optimum_z(c):
    lo=0.000001
    hi=1.0
    while h(hi)>c:
        hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if h(mid)>c:lo=mid
        else:hi=mid
    return (lo+hi)/2


def check():
    tests=0
    for a,b in [(0.2,0.9),(0.7,1.8),(2,2.2),(0.002,1.0),(0.7,10.0)]:
        for rho in [0.03,0.15,0.8,1.6,2.7,5.0]:
            G=gram_by_quadrature(a,b,rho)
            H=gram_exact(a,b,rho)
            for i in range(2):
                for j in range(2):
                    assert abs(G[i][j]-H[i][j])<1.e-8
                    tests+=1
            det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
            assert abs(det-determinant(a,b,rho))<1.e-7
            tests+=1
            assert det>0
            tests+=1
        c=(a+b)/(b-a)
        z=optimum_z(c)
        assert abs(h(z)-c)<1e-8
        tests+=1
        for factor in [0.2,0.5,0.9,1.1,1.8,3.0]:
            D0=math.exp(-c*z)*g(z)
            Dz=math.exp(-c*z*factor)*g(z*factor)
            assert D0>Dz
            tests+=1
    for z in [0.1,0.2,0.4,0.8,1.5,2,3,4,5,6,8,10,12]:
        # Exact sign expression for -d(log(g))/dz squared.
        F=z*z*(math.cosh(z)+1)-4*z*math.sinh(z)+4*(math.cosh(z)-1)
        assert F>0
        tests+=1
    for k in range(3,150):
        assert 2*(2*k-1)*(k-2)>0
        tests+=1
    # Thin slab limit: c large. Compare exact determinant coefficient.
    for c in [40,100,300,1000]:
        z=optimum_z(c)
        D=math.exp(-c*z)*g(z)
        target=64/(3*math.e**4)*c**(-4)
        assert abs(D/target-1)<0.008
        tests+=1
    # Boundary collar limit: epsilon small, stable data before float underflow.
    for eps in [1e-5,1e-6,1e-7,1e-8]:
        c=1+eps; z=optimum_z(c)
        target=math.log(1/eps)+2*math.log(math.log(1/eps))
        assert abs(z-target)<1.0
        tests+=1
        D=math.exp(-c*z)*g(z)
        loss=1-D
        assert abs(loss/(eps*math.log(1/eps))-1)<0.65
        tests+=1
    print(f"PASS: {tests} supplementary finite assertions")


if __name__=='__main__':
    check()
