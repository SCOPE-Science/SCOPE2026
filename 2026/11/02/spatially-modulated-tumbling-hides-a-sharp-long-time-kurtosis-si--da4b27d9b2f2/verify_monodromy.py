"""Numerical monodromy verification for a two-zone persistent-transport model.

Run using Python 3.11 or later: python verify_monodromy.py
Only Python's standard library is required. This is finite numerical evidence,
not a substitute for the analytic Taylor expansion in RESULT.md.
"""
from decimal import Decimal as D, localcontext


def calc(a, b, L, v, k):
    a, b, L, v, k = map(lambda x: D(str(x)), (a,b,L,v,k))
    h=L/2
    def F(z):
        d1=(z*(z+2*(a+b))).sqrt()/v
        d2=(z*(z+2*(a-b))).sqrt()/v
        def ch(x): return (x.exp()+(-x).exp())/2
        def sinhc(x):
            if x == 0: return D(1)
            return (x.exp()-(-x).exp())/(2*x)
        return ch(h*d1)*ch(h*d2)+z*(z+2*a)/v**2*h**2*sinhc(h*d1)*sinhc(h*d2)
    target=((k*L).exp()+(-k*L).exp())/2
    lo=D(0)
    hi=v**2*k*k/a
    for _ in range(260):
        mid=(lo+hi)/2
        if F(mid)<target: lo=mid
        else: hi=mid
    return (lo+hi)/2

with localcontext() as ctx:
    ctx.prec=78
    trials=[('2','1','10','1'),('4','2','1','1'),('3','2','8','1.7'),('1','0','4','2'),('2','1','3','2'),('3','1.2','6','2')]
    checks=0
    for a,b,L,v in trials:
        a,b,L,v=map(D,(a,b,L,v))
        c2=v*v/(2*a)
        c4=-(v**4)/(8*a**3)+(L*L*b*b*v*v)/(96*a**3)
        # Directly solve the analytic 2-layer transfer-matrix dispersion,
        # then independently estimate its fourth-order Taylor coefficient.
        for eta in map(D,('0.04','0.02','0.01')):
            k=eta/L
            psi=calc(a,b,L,v,k)
            estimated=(psi-c2*k*k)/(k**4)
            assert abs(estimated-c4)<D('0.02')*max(D(1),abs(c4)),(a,b,L,v,estimated,c4)
            checks+=1
        c4rate=24*c4
        assert (c4rate>0)==(L*abs(b)>D(12).sqrt()*v)
        checks+=1
    print(f'PASSED {checks} high-precision monodromy and sign checks; no external packages')
