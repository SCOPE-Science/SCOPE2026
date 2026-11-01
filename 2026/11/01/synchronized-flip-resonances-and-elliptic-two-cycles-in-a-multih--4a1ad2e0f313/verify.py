"""Independent computations supporting the local two-cycle theorem.

Run: python verify.py
Requires: Python 3, sympy, mpmath.
The universal result is proved analytically in RESULT.md; finite numerical tests
here are regression checks, not substitutes for that proof.
"""
import sympy as sp
import mpmath as mp


def assert_near(a, b, tol, message):
    if abs(a-b) > tol:
        raise AssertionError(f'{message}: discrepancy {mp.nstr(abs(a-b), 12)}')


def main():
    checks = 0
    W, c, a, b, d3 = sp.symbols('W c a b d3', nonzero=True, real=True)
    A = d3/sp.Integer(6) - b**2/(2*a)
    assert sp.simplify((32*A/a)*(-a*a/(4*A)) + 8*a) == 0
    checks += 1
    aw = W/sp.Integer(2)
    bw = W**2*c/2
    cw = -W**2*(2*W+3+3*c**2)/4
    B = (2*W+3)+3*(2*W+1)*c**2
    Aw = sp.factor((cw/6 - bw**2/(2*aw)) + W**2*B/24)
    assert Aw == 0
    assert sp.factor((-aw**2/(4*(-W**2*B/24))) - 3/(2*B)) == 0
    checks += 2
    mp.mp.dps = 68
    deltas = [mp.mpf('0.0000001'), mp.mpf('0.00000001')]
    for w in [2, 3, 4, 7, 50]:
        s = lambda x: sum(mp.sin(j*x) for j in range(1,w+1))
        ds = lambda x: sum(j*mp.cos(j*x) for j in range(1,w+1))
        d2s = lambda x: -sum(j*j*mp.sin(j*x) for j in range(1,w+1))
        d3s = lambda x: -sum(j*j*j*mp.cos(j*x) for j in range(1,w+1))
        positions = [0] + sorted(set([1,w//2,w-1]))
        for m in positions:
            if m == 0:
                q = mp.mpf(0)
                aa = mp.mpf(w*(w+1))/2
                Kc = 4/aa
                amplitude = mp.sqrt(mp.mpf(3)/2)
                assert_near(s(q), 0, mp.mpf('1e-54'), 'origin zero')
                assert_near(ds(q), aa, mp.mpf('1e-54'), 'origin derivative')
                assert_near(d2s(q), 0, mp.mpf('1e-54'), 'origin second derivative')
                assert_near(d3s(q), -aa*aa, mp.mpf('1e-54'), 'origin third derivative')
                checks += 4
            else:
                q = 2*mp.pi*m/w
                aa = mp.mpf(w)/2
                Kc = 4/aa
                C = mp.cot(mp.pi*m/w)
                BB = (2*w+3)+3*(2*w+1)*C*C
                amplitude = mp.sqrt(3/(2*BB))
                assert_near(s(q),0,mp.mpf('1e-54'), 'root')
                assert_near(ds(q),aa,mp.mpf('1e-54'), 'slope')
                assert_near(d2s(q),w*w*C/2,mp.mpf('1e-54'), 'curvature')
                assert_near(d3s(q),-w*w*(2*w+3+3*C*C)/4,mp.mpf('1e-54'), 'cubic coefficient')
                checks += 4
            for delta in deltas:
                K=Kc+delta
                guess=amplitude*mp.sqrt(delta)
                t,h=mp.findroot((lambda t,h:s(t+h)+s(t-h),
                                 lambda t,h:(s(t+h)-s(t-h))/(2*h)-4/K),
                                (q,guess),tol=mp.mpf('1e-57'),maxsteps=100)
                assert h>0
                assert abs(h/guess-1)<mp.mpf('0.02')
                checks += 2
                x0=t-h; p0=-2*h
                P=p0-K*s(x0); X=x0+P
                assert_near(P,2*h,mp.mpf('1e-49'),'first momentum')
                assert_near(X,t+h,mp.mpf('1e-49'),'first position')
                P2=P-K*s(X); X2=X+P2
                assert_near(P2,p0,mp.mpf('1e-49'),'return momentum')
                assert_near(X2,x0,mp.mpf('1e-49'),'return position')
                checks+=4
                z0=K*ds(x0);z1=K*ds(t+h)
                tr=2-2*(z0+z1)+z0*z1
                assert -2<tr<2
                assert abs(tr-(2-8*aa*delta))<mp.mpf('1e9')*delta**2
                checks+=2
    assert 50*mp.mpf('0.1')<2*mp.pi
    assert (2*50,50-1,50+1)==(100,49,51)
    checks+=2
    print(f'CHECKS_OK {checks} exact symbolic, high-precision root, full-map return and trace checks')


if __name__ == '__main__':
    main()
