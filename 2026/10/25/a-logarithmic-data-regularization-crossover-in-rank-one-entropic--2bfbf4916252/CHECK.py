"""Check boundary-layer laws for one-measurement entropic least squares.
Requires mpmath. Runs fixed high precision with independently evaluated KKT residuals.
"""
from mpmath import mp
mp.dps = 90


def root_and_x(lam, b, a, q):
    a = tuple(map(mp.mpf, a))
    q = tuple(map(mp.mpf, q))
    c = tuple(z/mp.e for z in q)
    def F(t):
        return sum(ai*ci*mp.exp(-ai*t) for ai,ci in zip(a,c))
    lo = mp.mpf('0')
    hi = mp.mpf('1')
    while F(hi) - lam*hi - b > 0:
        hi *= 2
    for _ in range(440):
        md = (lo+hi)/2
        if F(md) > lam*md+b:
            lo=md
        else:
            hi=md
    t=(lo+hi)/2
    x=[ci*mp.exp(-ai*t) for ai,ci in zip(a,c)]
    residual = abs(sum(ai*xi for ai,xi in zip(a,x))-b-lam*t)
    return t,x,residual

def experiment(a,q,epsilons,betas):
    alpha = min(map(mp.mpf,a))
    c = [mp.mpf(y)/mp.e for y in q]
    C = alpha*sum(ci for ai,ci in zip(a,c) if mp.mpf(ai)==alpha)
    B=alpha*C
    print('a',a,'q',q,'alpha',mp.nstr(alpha,5),'C',mp.nstr(C,12))
    for exponent in epsilons:
        lam=mp.power(10,-exponent)
        L=mp.log(1/lam)
        for mode,beta in betas:
            if mode=='finite':
                b=mp.mpf(beta)*lam*L
                base=lam*L*(mp.mpf(beta)+1/alpha)/C
            elif mode=='dominant':
                b=mp.power(lam,mp.mpf(beta))
                base=b/C
            else:
                b=mp.mpf(0)
                base=lam*mp.lambertw(B/lam)/B
            t,x,res = root_and_x(lam,b,a,q)
            rel=[xi/(ci*base**(ai/alpha)) -1 for xi,ci,ai in zip(x,c,map(mp.mpf,a))]
            worst=max(map(abs,rel))
            assert res<mp.mpf('1e-70')
            print('exp',exponent, mode,beta,'t',mp.nstr(t,12),'worst_relative',mp.nstr(worst,12),'KKT_residual',mp.nstr(res,7))

experiment([1,2,4],[2,3,5],[10,30,60],[('finite',0),('finite','0.5'),('finite',3),('dominant','0.4'),('zero',0)])
experiment([3,3,5,9],['0.4',4,2,6],[10,30,60],[('finite',0),('finite',2),('dominant','0.25'),('zero',0)])
experiment([1,1,1],[2,3,5],[10,30,60],[('finite',0),('finite',2),('dominant','0.25'),('zero',0)])
print('ALL CHECKS PASSED')
