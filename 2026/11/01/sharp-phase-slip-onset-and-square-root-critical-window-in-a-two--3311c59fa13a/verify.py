"""Reproducible finite checks for the two-cluster no-slip phase boundary.

Run: python3 verify.py. Standard library only. Numerical tests are not a
substitute for the universal trigonometric proof in RESULT.md.
"""
import math

PI = math.pi


def bisect_decreasing_root(fn, lo, hi, steps=120):
    assert fn(lo) > 0 and fn(hi) < 0
    for _ in range(steps):
        mid = (lo + hi) / 2
        if fn(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def critical_at_A(A):
    assert 0 <= A < 1
    t = bisect_decreasing_root(lambda t: t / math.tan(t / 2) - (1 + A), 1e-5, PI)
    b = (t - A * math.sin(t)) / (1 - math.cos(t))
    return t, b


def critical_gain(beta, d):
    assert 0 < beta < PI / 2 and 0 < d < 1
    c, s = math.cos(beta), math.sin(beta)
    lo, hi = 0.0, (1-1e-10) / c
    for _ in range(100):
        m = (lo + hi) / 2
        A = m*c
        if m*d*s < critical_at_A(A)[1]:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def lift(delta, A, B):
    return delta - A*math.sin(delta) + B*(1-math.cos(delta))


def original_step(theta, beta, gain):
    n = len(theta)
    # direct oscillator sum, not the reduced scalar expression
    return [
        (theta[i] + gain / n * sum(math.sin(theta[j]-theta[i]-beta) for j in range(n))) % (2*PI)
        for i in range(n)
    ]


def circular_distance(x, y):
    return abs((x-y+PI)%(2*PI)-PI)


def bisection_two_roots(A, B, t, K, beta, d, margin):
    # Solve G(y; K)=0 near the tangency on opposite sides.
    def G(y): return y - K*math.cos(beta)*math.sin(y) - K*d*math.sin(beta)*(1-math.cos(y))
    assert G(t) < 0
    a=t-margin; b=t; c=t+margin
    assert a>0 and c<PI and G(a)>0 and G(c)>0
    for _ in range(90):
        m=(a+b)/2
        if G(m)>0:a=m
        else:b=m
    left=(a+b)/2
    for _ in range(90):
        m=(b+c)/2
        if G(m)<0:b=m
        else:c=m
    right=(b+c)/2
    return left,right


def main():
    diagnostics=0
    for p,q in [(3,1),(5,2),(9,1),(7,5)]:
        d=(p-q)/(p+q)
        for beta in [PI/9, PI/6, PI/4, 1.2]:
            gain=critical_gain(beta,d)
            A=gain*math.cos(beta)
            B=gain*d*math.sin(beta)
            t, bc=critical_at_A(A)
            assert abs(B-bc)<3e-12
            assert 0<A<1 and 0<t<PI
            stationary=1+A-(t/math.tan(t/2))
            assert abs(stationary)<4e-13
            delta_star=2*math.atan(A/B)
            assert abs(lift(delta_star,A,B)-delta_star)<2e-14
            assert abs(1-A*math.cos(delta_star)+B*math.sin(delta_star)-(1+A))<1e-13
            assert abs(lift(2*PI-t,A,B)-2*PI)<3e-13
            diagnostics+=5
            for i in range(1,2500):
                delta=2*PI*i/2500
                val=lift(delta,A,B)
                assert 0<val<2*PI+4e-12, (p,q,beta,delta,val)
                if delta<delta_star:
                    assert val<delta
                elif delta>delta_star:
                    assert val>delta
                diagnostics+=1
            # Compare exact one-step N-body update to scalar reduction.
            for i in range(1,50):
                x=2*PI*i/51
                u=0.713
                th=[u]*p+[u+x]*q
                full=original_step(th,beta,gain)
                obs=(full[p]-full[0])%(2*PI)
                pred=lift(x,A,B)%(2*PI)
                assert circular_distance(obs,pred)<5e-14
                diagnostics+=1
            # Just above the threshold, a nonempty open interval crosses 2pi.
            gainplus=gain+0.0001
            Ap=gainplus*math.cos(beta)
            Bp=gainplus*d*math.sin(beta)
            assert lift(2*PI-t,Ap,Bp)>2*PI
            diagnostics+=1
            # Square-root law for the two new crossing points.
            D=(A-math.cos(t))/math.sin(t)
            assert D>0
            for eps in [1e-5,1e-6,1e-7]:
                ak=(gain+eps)*math.cos(beta)
                bk=(gain+eps)*d*math.sin(beta)
                w=(2*t/(gain*D))**0.5 *eps**0.5
                def g(y):return y-ak*math.sin(y)-bk*(1-math.cos(y))
                assert g(t)<0
                # bracket roots using a generous width around critical t
                lefta=t-3*w; rightb=t+3*w
                assert lefta>0 and rightb<2*PI
                assert g(lefta)>0 and g(rightb)>0
                # find left and right zeros by bisection
                lo,hi=lefta,t
                for _ in range(80):
                    mid=(lo+hi)/2
                    if g(mid)>0:lo=mid
                    else:hi=mid
                left=(lo+hi)/2
                lo,hi=t,rightb
                for _ in range(80):
                    mid=(lo+hi)/2
                    if g(mid)<0:lo=mid
                    else:hi=mid
                right=(lo+hi)/2
                ratio=(right-left)/(2*w)
                assert abs(ratio-1)<0.04, (p,q,beta,ratio)
                diagnostics+=1
    # End-point cusp coefficient B_c(A) / sqrt(1-A).
    for A in [0.99,0.999,0.9999]:
        t,b=critical_at_A(A)
        assert abs(b/math.sqrt(1-A)-math.sqrt(8/3))<0.03
        diagnostics+=1
    # External parameter example, independent direct update.
    g=critical_gain(PI/4, 0.5)
    assert abs(g-1.29948735520173)<1e-10
    diagnostics+=1
    print('VERIFIED', diagnostics, 'finite diagnostics; Kcrit(pi/4, 1/2)=', format(g,'.14f'))

if __name__=='__main__':
    main()
