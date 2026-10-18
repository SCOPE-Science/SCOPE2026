"""Reproduce numerical checks for a telegraph adsorption protocol comparison.
Requires Python 3.10+ standard library. The analytic proof is in RESULT.md.
"""
import math

def expressions(alpha, reset_rate, speed, x0, s, orient, p, wall_laplace):
    u = reset_rate + s
    root = math.sqrt(u * (u + 2 * alpha))
    theta = alpha / (alpha + u + root)
    E = math.exp(-x0 * root / speed)
    a = theta if orient == '+' else 1.0
    f = u * a * E / (s + reset_rate * a * E)
    g = theta + reset_rate * (1 - theta) * f / u
    b = (1 - p) * wall_laplace
    numerator = p * wall_laplace * f
    L_N = numerator / (1 - b * g)
    L_R = numerator / (1 - b * f)
    fact = s * (theta - a * E) / (s + reset_rate * a * E)
    return f, g, L_N, L_R, fact, root, theta, E

def boundary_residual(alpha, reset_rate, speed, x0, s, orient, x):
    u = reset_rate + s
    q = math.sqrt(u * (u + 2 * alpha)) / speed
    theta = alpha / (alpha + u + math.sqrt(u * (u + 2 * alpha)))
    E = math.exp(-q*x0)
    a = theta if orient == '+' else 1.0
    f = u * a * E / (s + reset_rate * a * E)
    constant = reset_rate * f / u
    A = 1 - constant
    def F(x, sign):
        return constant + (theta if sign == '+' else 1) * A * math.exp(-q*x)
    h = 1e-5
    for sign in ('+', '-'):
        numerical_deriv = (F(x+h, sign)-F(x-h, sign))/(2*h)
        lhs = (1 if sign=='+' else -1) * speed*numerical_deriv + alpha*(F(x, '-' if sign=='+' else '+')-F(x,sign)) + reset_rate*(f-F(x,sign)) - s*F(x,sign)
        assert abs(lhs) <= 2e-7*(1+alpha+reset_rate+s), (orient,sign,lhs)
    assert abs(F(0,'-') - 1) < 1e-13
    assert abs(F(x0,orient) - f) < 1e-13
    return 4

def threshold(alpha, c):
    lo, hi = 1e-9, 1.0
    while hi / math.sinh(hi) > c:
        hi *= 2
    for _ in range(140):
        m = (lo + hi)/2
        if m / math.sinh(m) > c:
            lo=m
        else:
            hi=m
    t=(lo+hi)/2
    return alpha*(math.cosh(t)-1), t

def main():
    total = 0
    for c in (0.08,0.15,0.37,0.51,0.83,0.975,1.0,1.2,2.4):
        alpha, speed = 1.7, 2.9
        x0 = c * speed/alpha
        if c<1:
            rc,tc=threshold(alpha,c)
            assert abs(tc/math.sinh(tc)-c)<5e-15
            total+=1
            resets=(0.11*rc,0.56*rc,rc*1.1,rc*3)
        else:
            resets=(0.02,0.5,2.0,15)
        for r in resets:
            for s in (0.001, 0.04,0.3, 1, 4, 10, 70):
                for orient in ('+', '-'):
                    for p in (0.21,0.65):
                        for wall in (math.exp(-0.27*s), 1/(1+0.27*s)):
                            f,g,LN,LR,fac,root,theta,E=expressions(alpha,r,speed,x0,s,orient,p,wall)
                            assert 0 < f < 1 and 0 < g < 1
                            assert abs((g-f)-fac) < 3e-14
                            pred = 1 if orient=='+' or c>=1 or r+s>(rc if c<1 else 0) else -1
                            actual = LN-LR
                            if abs(actual)>1e-14:
                                assert actual*pred>0, (c,r,s,orient,p,actual)
                            assert 0<LN<1 and 0<LR<1
                            total += 5
                    total += boundary_residual(alpha,r,speed,x0,s,orient,max(0.12,x0*0.75))
    # Sharp sign reversal on both sides of the predicted frequency for 4 values.
    for c in (0.15,0.4,0.6,0.95):
        rc,_=threshold(1,c); r=0.37*rc; sc=rc-r
        diffs=[]
        for s in (0.4*sc, 0.9*sc, 1.1*sc, 2*sc):
            result=expressions(1,r,2.0,2*c,s,'-',0.4,1/(1+s))[2:4]
            diffs.append(result[0]-result[1])
        assert diffs[0]<0 and diffs[1]<0 and diffs[2]>0 and diffs[3]>0
        total+=4
    print(f'{total} deterministic numerical checks passed')

if __name__=='__main__': main()
