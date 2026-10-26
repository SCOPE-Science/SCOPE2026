"""Independent rational and symbolic checks for star/clique bi-SIS coexistence.

Run: python verify.py
Dependencies: Python >=3.9; sympy.
"""
from fractions import Fraction
from itertools import product
import math
import sympy as S


def derived(m, a, b):
    """Compute four equilibrium coordinates from susceptibility equations.

    The calculation uses the linear equations after eliminating s_L,s_C.
    This is deliberately distinct from a direct nonlinear-system solve.
    """
    m, a, b = int(m), Fraction(a), Fraction(b)
    sl = (a*a-b*b)/(a*a*b*(m-1))
    sc = b*(m-1)/(m*(a*a-b*b))
    u, v = a*sl, m*b*sc
    det = 1-u*v
    xc = ((1-sc)-v*(1-sl))/det
    yl = ((1-sl)-u*(1-sc))/det
    return sl, sc, xc, u*xc, yl, v*yl


def full_system(m, a, b, state):
    """Return all 2(m+1) RHS values of ORIGINAL vertexwise equations."""
    x, y = state
    one = Fraction(1)
    rx, ry = [], []
    for i in range(m+1):
        si = one-x[i]-y[i]
        star_x = sum(x[1:], Fraction(0)) if i == 0 else x[0]
        clique_y = sum((y[j] for j in range(m+1) if j != i), Fraction(0))
        rx.append(-x[i]+a*si*star_x)
        ry.append(-y[i]+b*si*clique_y)
    return rx, ry


def admissible(m, a, b):
    if a <= b:
        return False
    r = a/b
    F = 1+(m-1)*r-r*r
    if r*r <= m or F <= 0:
        return False
    H = (m*r*r-(m-1)*r-m)/(m*r*F)
    return b > H


def check_one(m, a, b):
    m, a, b = int(m), Fraction(a), Fraction(b)
    if a == b:
        return False
    sl, sc, xc, xl, yl, yc = derived(m, a, b)
    x = [xc]+[xl]*m
    y = [yc]+[yl]*m
    res = full_system(m,a,b,(x,y))
    assert all(z == 0 for row in res for z in row), (m,a,b,res)
    positive = (sl>0 and sc>0 and all(0<z<1 for z in x+y)
                and all(x[i]+y[i]<1 for i in range(m+1)))
    expected = admissible(m,a,b)
    if positive != expected:
        raise AssertionError(('phase',m,a,b,positive,expected,(sl,sc,xc,xl,yl,yc)))
    return positive


def symbolic():
    m,a,b,r = S.symbols('m a b r',positive=True)
    sl=(a*a-b*b)/(a*a*b*(m-1))
    sc=b*(m-1)/(m*(a*a-b*b))
    u=a*sl
    v=m*b*sc
    xc=S.factor(((1-sc)-v*(1-sl))/(1-u*v))
    yl=S.factor(((1-sl)-u*(1-sc))/(1-u*v))
    assert S.simplify(1-u*v-(1-b/a)) == 0
    assert S.simplify(xc-(a*a-m*b*b)*(m*a*a+b)/(a*m*(a-b)**2*(a+b))) == 0
    F=1+(m-1)*r-r*r
    Q=m*r*r-(m-1)*r-m
    assert S.simplify(yl.subs(a,r*b)-(b*m*r*F-Q)/(b*m*r*(m-1)*(r-1))) == 0
    H=Q/(m*r*F)
    lower_L=(r*r-1)/(r*r*(m-1))
    lower_C=(m-1)/(m*(r*r-1))
    excess=(r*r-m)*(m*r*r-1)
    assert S.simplify(H-lower_L-excess/(m*r*r*(m-1)*F)) == 0
    assert S.simplify(H-lower_C-excess/(m*r*(r*r-1)*F)) == 0
    # Direct symbolic original fixed-point substitution.
    s0=1-xc-v*yl
    s1=1-u*xc-yl
    for expr in (s0-sc,s1-sl,
                 -xc+a*m*s0*(u*xc),
                 -u*xc+a*s1*xc,
                 -v*yl+b*s0*(m*yl),
                 -yl+b*s1*((m-1)*yl+v*yl)):
        assert S.cancel(expr) == 0
    print('symbolic identities: PASS')


def demonstrate():
    for m,a,b in [(2,3,2),(3,2,1),(3,5,2)]:
        if admissible(m,Fraction(a),Fraction(b)):
            print('example',m,a,b,tuple(map(str,derived(m,a,b))))


def grid():
    cases=0
    positive=0
    for m in range(2,13):
        for a,b in product([Fraction(k,6) for k in range(1,50)], repeat=2):
            if a==b: continue
            cases+=1
            positive+=check_one(m,a,b)
    print('exact-rational cases:',cases,'positive coexistence:',positive)


if __name__=='__main__':
    symbolic()
    demonstrate()
    grid()
    print('VERIFIED')
