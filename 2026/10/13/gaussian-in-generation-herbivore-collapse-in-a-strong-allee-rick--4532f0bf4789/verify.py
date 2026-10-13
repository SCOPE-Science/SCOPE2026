"""Reproduce finite checks for the quadratic-log extinction law.

No finite calculation substitutes for the convergence proof in RESULT.md.
Uses only the Python standard library. Run: python verify.py
"""
import math


def log_exprel(z):
    """Stable log((exp(z)-1)/z), for z>0; continuous value zero at zero."""
    if z == 0.0:
        return 0.0
    if z < 1e-5:
        return z / 2.0 + z*z / 24.0 - (z**4)/2880.0
    return math.log(math.expm1(z)/z)


def experiment(r, b, a, x0, y0, n=230):
    assert r > 0 and 0 < b < 1 and a > 0 and 0 < x0 < b and y0 > 0
    s = r*b
    q = math.exp(-s)
    logx, logy = math.log(x0), math.log(y0)
    S, weighted, T = 0., 0., 0.
    records = {}
    for k in range(n):
        x = math.exp(logx)
        y = math.exp(logy) if logy > -735 else 0.0
        d = r*(1+b)*x - r*x*x - a*y
        new_logx = logx - s + d
        T += log_exprel(a*y)
        if k >= 1:
            weighted += k*d
        S += d
        new_logy = logy + math.log(a) + new_logx + log_exprel(a*y)
        if k < 12:
            xx = x * math.exp(r*(1-x)*(x-b)) * math.exp(-a*y)
            yy = x * math.exp(r*(1-x)*(x-b)) * (-math.expm1(-a*y))
            assert abs(math.log(xx)-new_logx) < 4e-14
            assert abs(math.log(yy)-new_logy) < 5e-14
        logx, logy = new_logx, new_logy
        if k+1 in [100,160,230]:
            records[k+1]=(logx,logy,S,weighted,T)
    logC=math.log(x0)+S
    logD=math.log(y0)-weighted+T
    for m in [100,160,230]:
        lx,ly,sm,w,tm = records[m]
        mx = math.log(x0)+sm
        md = math.log(y0)-w+tm
        estimated_x = lx + s*m
        estimated_y = ly + s*m*(m+1)/2-m*(math.log(a)+mx)
        assert abs(estimated_x-logC) < (1e-9 if m==100 else 1e-11)
        assert abs(estimated_y-logD) < (1e-6 if m==100 else 1e-8)
        assert abs(ly / (m*m)+s/2) < 0.09
    lx,ly,_,_,_ = records[230]
    assert abs(lx + s*230-logC) < 1e-11
    assert abs(ly + s*230*231/2 - 230*(math.log(a)+logC)-logD) < 1e-8
    return {'r':r,'b':b,'a':a,'logC':logC,'logD':logD,'logy230':ly}


def main():
    for params in [(1.,.25,1.3,.12,.14), (2.,.20,.8,.07,.4), (1.5,.3,2.,.22,.03)]:
        print(experiment(*params))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
