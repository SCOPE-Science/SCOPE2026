"""Standalone arithmetic checks of the binary transition/entropy identities.

Uses Python's standard-library decimal arithmetic only. Finite checks support
but do not replace the asymptotic argument.
Run: python3 verify.py
"""
from decimal import Decimal, localcontext

D = Decimal

def h(p):
    if p == 0 or p == 1:
        return D(0)
    return -p * p.ln() - (1-p) * (1-p).ln()

def channel(a, b, t):
    k = -( (-(a+b)*t).exp() - 1) / (a+b)
    return a*k, b*k

def H(e, a, b, t):
    u,v = channel(a,b,t)
    w = u+(1-u-v)*e
    return h(e)+(1-e)*h(u)+e*h(v)-h(w)

def derivative(e,a,b,t):
    u,v=channel(a,b,t)
    k=1-u-v
    w=u+k*e
    return ((1-e)/e).ln()-k*((1-w)/w).ln()+h(v)-h(u)

def optimum(a,b,t):
    lo=D('1e-120')
    hi=1-lo
    assert derivative(lo,a,b,t)>0 and derivative(hi,a,b,t)<0
    for _ in range(470):
        m=(lo+hi)/2
        if derivative(m,a,b,t)>0:lo=m
        else:hi=m
    return (lo+hi)/2

def joint_conditional(e,u,v):
    # X=0,1 has distribution 1-e,e; Y=0,1 follows the channel.
    entries = ((1-e)*(1-u), (1-e)*u, e*v, e*(1-v))
    y0=entries[0]+entries[2]; y1=entries[1]+entries[3]
    ans=D(0)
    for c,y in zip(entries,(y0,y1,y0,y1)):
        if c>0: ans -= c*(c/y).ln()
    return ans

def main():
    with localcontext() as ctx:
        ctx.prec=145
        checks=0
        for a,b in ((D(3),D(1)),(D(5),D(2)),(D(11),D(10))):
            values=[]
            for power in (3,6,12,24,40):
                t=D(10)**(-power)
                e=optimum(a,b,t)
                L=(D(1)/((a-b)*t)).ln()
                score=H(e,a,b,t)
                scaled=e*(a-b)*L/a
                residual=(score-a*t*(L-L.ln()))/t
                assert D(0)<e<D(1)
                assert abs(derivative(e,a,b,t))<D('1e-75')
                assert score>0
                values.append((power,scaled,residual))
                checks+=4
            # Longer-time asymptotic approach is visible without extrapolation.
            assert abs(values[-1][1]-1)<abs(values[0][1]-1)
            # A second-order remainder need not be monotone at accessible times.
            # Near-balanced rates exhibit a very long preasymptotic crossover.
            checks+=1
            for t in (D('0.02'),D('0.005')):
                u,v=channel(a,b,t)
                for e in (D('0.1'),D('0.29'),D('0.65'),D('0.93')):
                    assert abs(joint_conditional(e,u,v)-H(e,a,b,t)) < D('1e-120')
                    k=1-u-v; w=u+k*e
                    variance = w*(1-w)-k*k*e*(1-e)
                    rhs=(1-e)*u*(1-u)+e*v*(1-v)
                    assert abs(variance-rhs)<D('1e-120') and variance>0
                    checks+=2
        # Symmetric case: unique minimizer is the fair prior and cost is h(u).
        for a in (D('0.25'),D(1),D(7)):
            for power in (2,4,8,12):
                t=D(10)**(-power)
                e=optimum(a,a,t)
                u,v=channel(a,a,t)
                assert abs(e-D('0.5'))<D('1e-110')
                assert abs(H(e,a,a,t)-h(u))<D('1e-110')
                checks+=2
        print(f'PASS {checks} deterministic exact-formula and high-precision checks')
        for a,b in ((D(3),D(1)),):
            print('a,b',a,b)
            for power in (4,12,24,40):
                t=D(10)**(-power)
                e=optimum(a,b,t)
                L=(D(1)/((a-b)*t)).ln()
                f=H(e,a,b,t)
                print('t=1e-',power,'q_rare=',str(e)[:15], 'optimizer_scale=',str(e*(a-b)*L/a)[:12], 'cost_remainder_over_t=',str((f-a*t*(L-L.ln()))/t)[:12])

if __name__ == '__main__': main()
