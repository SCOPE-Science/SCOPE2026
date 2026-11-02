"""Reproduce exact-moment and minimax checks using only Python's standard library.

This checker is supplementary: the infinite parameter theorem is proved analytically
in RESULT.md, not by finite grids.
"""
import math


def formula(q, r, phase):
    z = math.exp(-q)
    c = 0.5 * (1-z)**2 + z * (math.cosh(q*r)-1)
    s = 0.5 * (1-z*z) + z * math.sinh(q*r)
    return 0.5 * (c * math.cos(phase)**2 + s * math.sin(phase)**2)


def optimum(q):
    z = math.exp(-q)
    return -math.log(2-z)/q, (1-z)**2 / (2*(2-z))


def legendre(n, a, b):
    # Gauss-Legendre nodes/weights via Newton iteration; no external packages.
    xs = [0.0]*n
    ws = [0.0]*n
    for i in range((n+1)//2):
        x = math.cos(math.pi * (i+0.75)/(n+0.5))
        for j in range(30):
            p0,p1 = 1.,x
            for k in range(2,n+1):
                p0,p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
            deriv = n*(x*p1-p0)/(x*x-1)
            dx=p1/deriv
            x-=dx
            if abs(dx)<1e-15:break
        w=2./((1.-x*x)*deriv*deriv)
        xs[i], xs[n-1-i] = (a+b)/2 - (b-a)/2*x,(a+b)/2 + (b-a)/2*x
        ws[i]=ws[n-1-i]=(b-a)/2*w
    return xs,ws


def direct_integral(q,r,phase, normal):
    xs, ws = normal
    mean = 0.0
    second=0.0
    for x, wx in zip(xs, ws):
        u=math.sqrt(q)*x
        f=math.cos(phase+u)
        for y,wy in zip(xs,ws):
            v=math.sqrt(q)*(r*x+math.sqrt(1-r*r)*y)
            estimate=(f+math.cos(phase+v))/2
            weight=wx*wy
            mean+=weight*estimate
            second+=weight*estimate**2
    return mean,second-mean**2


def main():
    count=0
    for q in [0.0002, 0.005, 0.05, 0.1, 0.5, math.log(3), 1, 2, 5, 10, 30]:
        r,v=optimum(q)
        z=math.exp(-q)
        assert -1 < r < 0
        assert abs(formula(q,r,0)-v) < 2e-14
        assert abs(formula(q,r,math.pi/2)-v) < 2e-14
        assert v < (1-z*z)/4
        assert v < (1-z)**2/2
        for i in range(601):
            test_r=-1+2*i/600
            worst=max(formula(q,test_r,0),formula(q,test_r,math.pi/2))
            assert worst >= v - 2e-14
            count+=1
    # Compare the characteristic-function proof independently to direct
    # bivariate Gaussian quadrature in the two independent normal coordinates.
    x,w=legendre(96,-9,9)
    wn=[wi*math.exp(-xi*xi/2)/math.sqrt(2*math.pi) for xi,wi in zip(x,w)]
    normal=(x,wn)
    assert abs(sum(wn)-1)<2e-13
    quadratures=0
    for q in (0.1,0.7,2):
        for r in (-0.85,-0.3,0,0.65,0.92):
            for phase in (0,0.37,math.pi/2):
                m,v=direct_integral(q,r,phase,normal)
                assert abs(m-math.exp(-q/2)*math.cos(phase))<1e-11
                assert abs(v-formula(q,r,phase))<1e-11,(q,r,phase,v,formula(q,r,phase))
                quadratures+=1
    print('PASS:',count,'grid dominance checks;',quadratures,
          'independent bivariate Gaussian quadratures; all limits and endpoint inequalities checked')


if __name__=='__main__':main()
