"""Exact finite-perturbation checks for one-step Hybrid LSLU on isometries."""
import sympy as s


def first_step(A, b, mu):
    """Source pivoted rectangular Hessenberg stage and projected ridge solve."""
    m, n = A.shape
    assert m > n >= 2
    assert s.simplify(A.T * A - s.eye(n)) == s.zeros(n)
    p = max(range(m), key=lambda j: abs(float(b[j])))
    beta = b[p]
    d1 = b / beta
    q = A.T * d1
    g = max(range(n), key=lambda j: abs(float(q[j])))
    assert q[g] != 0
    l1 = q / q[g]
    v = A * l1
    h1 = v[p]
    residual = s.simplify(v - h1 * d1)
    i = max([j for j in range(m) if j != p], key=lambda j: abs(float(residual[j])))
    h2 = residual[i]
    assert h2 != 0
    y = s.simplify(beta * h1 / (h1*h1 + h2*h2 + mu*mu))
    return s.simplify(l1*y), s.simplify(h1), s.simplify(h2)


def check():
    t = s.symbols('t', positive=True)
    mu = s.symbols('mu', positive=True)
    half = s.Rational(1,2)
    A_hi = s.Matrix([[half,half],[half,-half],[half,half],[half,-half]])
    u_hi = s.Matrix([1,0])
    b_hi = A_hi*u_hi+t*s.Matrix([1,0,-1,0])
    # At t in (0,1/4), the first (positive) coordinate is the unique pivot.
    for tv in [s.Rational(1,100),s.Rational(1,10),s.Rational(1,5)]:
        x,h1,h2 = first_step(A_hi,b_hi.subs(t,tv),s.Integer(1))
        beta=half+tv
        assert x == s.Matrix([s.simplify(beta*half/(half**2+(tv/beta)**2+1)),0])
        assert h1==half and abs(h2)==tv/beta
    alpha_hi=s.simplify((half+t)*half/(half**2+(t/(half+t))**2+mu**2))
    assert s.simplify(s.limit(alpha_hi,t,0,dir='+')-1/(1+4*mu**2))==0

    invsqrt2=1/s.sqrt(2)
    A_lo=s.Matrix([[invsqrt2,invsqrt2],[invsqrt2,-invsqrt2],[0,0],[0,0]])
    u_lo=s.Matrix([invsqrt2,invsqrt2]); e=s.Matrix([0,0,1,0])
    assert s.simplify(A_lo*u_lo)==s.Matrix([1,0,0,0])
    for tv in [s.Rational(1,100),s.Rational(1,10),s.Rational(1,2)]:
        x,h1,h2=first_step(A_lo,A_lo*u_lo+tv*e,s.Integer(1))
        assert s.simplify(x-u_lo*(2/(3+2*tv**2)))==s.zeros(2,1)
        assert h1==s.sqrt(2) and h2==-s.sqrt(2)*tv
    low_limit=2/(2+mu**2)
    assert s.simplify(low_limit-1/(1+mu**2/s.Integer(2)))==0

    # Exact minimax balancing when reference Tikhonov parameter is 1.
    n,m=s.symbols('n m',positive=True)
    z=s.sqrt(n/m)
    hlo=s.simplify(1/(1+z/n))
    hhi=s.simplify(1/(1+m*z))
    assert s.simplify(hlo+hhi-1)==0
    gap=s.simplify(hlo-s.Rational(1,2))
    assert s.simplify(gap-(s.sqrt(m*n)-1)/(2*(s.sqrt(m*n)+1)))==0

    # Complete-run pivoted updates: projected and direct formulas agree.
    for k in range(2,18):
        tv=s.Rational(1,k+10)
        for mv in (s.Rational(1,2),s.Integer(1),s.Integer(2),s.Integer(3)):
            x,_,_=first_step(A_hi,b_hi.subs(t,tv),mv)
            beta=half+tv
            expect=s.Matrix([s.simplify(beta*half/(half**2+(tv/beta)**2+mv**2)),0])
            assert s.simplify(x-expect)==s.zeros(2,1)
            x2,_,_=first_step(A_lo,A_lo*u_lo+tv*e,mv)
            expect2=u_lo*2/(2+2*tv**2+mv**2)
            assert s.simplify(x2-expect2)==s.zeros(2,1)
    print('PASS: exact pivot reconstruction, two sharp orientations, noise limits, minimax identity, 128 rational step tests')

if __name__=='__main__':
    check()
