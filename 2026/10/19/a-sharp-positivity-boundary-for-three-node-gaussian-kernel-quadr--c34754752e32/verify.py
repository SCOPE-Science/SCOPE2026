"""Standalone numerical cross-checks for the stated three-node Gaussian kernel quadrature result.
The universal assertions are established by the analytical proof in RESULT.md.
Run: python3 verify.py (standard library only).
"""
from decimal import Decimal, localcontext
from itertools import product
from math import prod

with localcontext() as context:
    context.prec = 85
    D = Decimal
    ZERO, ONE, TWO, THREE, FOUR = D(0),D(1),D(2),D(3),D(4)
    checks = 0
    def check(test, label):
        global checks
        checks += 1
        if not test:
            raise AssertionError(label)
    def raw(ell,a):
        ell,a=D(str(ell)),D(str(a))
        t = (-a*a/(TWO*ell*ell)).exp()
        u = (-a*a/(TWO*(ell*ell+ONE))).exp()
        c = ell/(ell*ell+ONE).sqrt()
        w=c*(u-t)/(ONE-t*t)**2
        v=c-TWO*t*w
        return t,u,c,w,v
    def h(y):
        y=D(str(y))
        co = (y.exp()+(-y).exp())/TWO
        return TWO*co.ln()/y
    def y_critical(ell):
        ell=D(str(ell)); c=ONE/(ONE+ell*ell)
        lo=D('1e-40'); hi=TWO
        for j in range(230):
            mid=(lo+hi)/TWO
            if h(mid)>c:hi=mid
            else:lo=mid
        return (lo+hi)/TWO
    # Check the exact kernel linear system in a broad grid of node gaps/bandwidths.
    for es in ('0.1','0.3','0.7','1','2','5','15'):
        for aa in ('0.08','0.1','0.3','0.7','1','1.2','2','3'):
            t,u,c,w,v=raw(es,aa)
            check(abs((ONE+t**4)*w+t*v-c*u)<D('1e-55'), 'outer exactness')
            check(abs(TWO*t*w+v-c)<D('1e-55'), 'center exactness')
            check(w>ZERO and TWO*w+v>ZERO,'side and total sum')
            x=D(aa)**2/D(es)**2
            diff=h(x)-ONE/(ONE+D(es)**2)
            check((v>ZERO)==(diff>ZERO),'sharp positivity sign')
            check((v>=ZERO)==((ONE+t**4)>=TWO*t*u),'exponential sign equivalence')
    # Every bandwidth has a unique threshold; sample bracketing and signs.
    for es in ('0.1','0.3','0.5','0.7','1','2','10','100'):
        ell=D(es); yy=y_critical(ell); ac=ell*yy.sqrt()
        check(ZERO<yy<TWO,'threshold interval')
        check(abs(h(yy)-ONE/(ONE+ell*ell))<D('1e-60'),'threshold root')
        check(ac<ONE,'sub-unit threshold')
        check(raw(ell,ac*D('0.95'))[4]<ZERO,'negative below threshold')
        check(raw(ell,ac*D('1.05'))[4]>ZERO,'positive above threshold')
        # The naturally scaled 3-point Gauss--Hermite physical nodes, alpha=1/sqrt(2).
        aa=(THREE/(ONE+FOUR/(ell*ell)).sqrt()).sqrt()
        check(raw(ell,aa)[4]>ZERO,'natural 3-point exact weights are positive')
        # Exact free Mercer-node scaling parameter frontier.
        bc=-ONE/(ell*ell)+(ONE/ell**4+ D(9)/(FOUR*ac**4)).sqrt()
        alpha_critical=bc.sqrt()
        def scaled_gap(alpha):
            alpha=D(str(alpha))
            return (THREE/(TWO*alpha*(alpha*alpha+TWO/(ell*ell)).sqrt())).sqrt()
        check(abs(scaled_gap(alpha_critical)-ac)<D('1e-57'), 'alpha critical correspondence')
        check(raw(ell,scaled_gap(alpha_critical*D('.9')))[4]>ZERO,'alpha below frontier')
        check(raw(ell,scaled_gap(alpha_critical*D('1.1')))[4]<ZERO,'alpha above frontier')
        check(alpha_critical> ONE/TWO.sqrt(),'natural alpha safely below frontier')
    # Complete tensor-product weight norm, with and without a sign change.
    for es,aa in [('1','0.1'),('1','2'),('0.3','0.1'),('0.3','0.6')]:
        t,u,c,w,v=raw(es,aa)
        ss=TWO*w+v; norm=(TWO*abs(w)+abs(v))/ss
        for dd in (1,2,3,4):
            ww=[p for factors in product((w,v,w),repeat=dd) for p in [prod(factors)]]
            S=sum(ww,ZERO)
            W=sum(map(abs,ww),ZERO)
            check(abs(S-ss**dd)<D('1e-58'),'tensor sum')
            check(abs(W/S-norm**dd)<D('1e-57'),'tensor exact norm')
            check(abs(sum((v0/S for v0 in ww),ZERO)-ONE)<D('1e-57'),'normalized constants')
    # Coalescence normalised norm prefactor: exact limit 4 ell^2/(2 ell^2 +3).
    for es in ('0.3','1','5'):
        ell=D(es)
        c0=FOUR*ell*ell/(TWO*ell*ell+THREE)
        previous=None
        for aa in ('0.04','0.02','0.01','0.005','0.001'):
            a=D(aa); t,u,c,w,v=raw(ell,a)
            norm=(TWO*abs(w)+abs(v))/(TWO*w+v)
            estimate=a*a*norm
            if previous is not None:
                check(abs(estimate-c0)<abs(previous-c0), 'coalescence convergence')
            previous=estimate
        check(abs(previous/c0-ONE)<D('0.0002'),'coalescence sharp constant')
    # Two symmetric nodes always have positive weights.
    for es in ('0.1','1','3'):
        for aa in ('0.01','0.5','5'):
            t,u,c,w,v=raw(es,aa)
            ww=c*u/(ONE+t**4)
            check(ww>ZERO,'two-node positivity')
            check(abs((ONE+t**4)*ww-c*u)<D('1e-50'), 'two-node exactness')
    print('PASS: %d deterministic high-precision checks; universal statements require RESULT.md proof.'%checks)
