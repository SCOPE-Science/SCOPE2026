"""High-precision numerical cross-checks for binary continuous-time channels.

Run: python verification/minimax_verifier.py
The asymptotic results are proved analytically; numerical checks are non-exhaustive.
"""
from decimal import Decimal as D, localcontext


def H(x):
    if x == 0 or x == 1:
        return D(0)
    return -x * x.ln() - (1-x) * (1-x).ln()


def dH(x):
    return ((1-x)/x).ln()


def channel(a, b, t):
    w = (-((a+b)*t)).exp()
    u = a/(a+b) * (1-w)
    v = b/(a+b) * (1-w)
    return u, v


def conditional(a, b, t, q):
    u, v = channel(a, b, t)
    out = u+(1-u-v)*q
    return H(q)+(1-q)*H(u)+q*H(v)-H(out)


def derivative(a, b, t, q):
    u, v = channel(a, b, t)
    return dH(q)-H(u)+H(v)-(1-u-v)*dH(u+(1-u-v)*q)


def optimum(a, b, t):
    left, right = D('1e-85'), 1-D('1e-85')
    for _ in range(270):
        middle = (left+right)/2
        if derivative(a,b,t,middle) > 0:
            left = middle
        else:
            right = middle
    q = (left+right)/2
    return q, conditional(a,b,t,q)


def transition_joint(a, b, t, q):
    u, v = channel(a,b,t)
    joints = ((1-q)*(1-u), (1-q)*u, q*v, q*(1-v))
    ys = (joints[0]+joints[2], joints[1]+joints[3])
    return -sum(j* (j/ys[k]).ln() for j,k in zip(joints,(0,1,0,1)) if j)


def crossover_g(q, kappa, eta):
    return eta*(D('0.5')-q)-kappa*(1-2*q)*dH(q)


def crossover_derivative(q,kappa,eta):
    return -eta+kappa*(2*dH(q)+(1-2*q)/(q*(1-q)))


def crossover_optimum(kappa,eta):
    l,r=D('1e-70'),D('0.5')
    for _ in range(270):
        q=(l+r)/2
        if crossover_derivative(q,kappa,eta)>0:
            l=q
        else:
            r=q
    q=(l+r)/2
    return q,crossover_g(q,kappa,eta)


def run():
    count=0
    with localcontext() as ctx:
        ctx.prec=110
        for a,b,t,q in [(D(3),D(1),D('0.125'),D('.2')),
                        (D(3),D(1),D('.00001'),D('.6')),
                        (D('1.5'),D('1.25'),D('.002'),D('.49'))]:
            f=conditional(a,b,t,q)
            assert abs(f-transition_joint(a,b,t,q))<D('1e-70')
            count+=1
            qstar,ff=optimum(a,b,t)
            assert 0<qstar<1 and abs(derivative(a,b,t,qstar))<D('1e-65')
            assert ff>=f-D('1e-70')
            count+=2
        for a in (D('0.7'),D(1),D(3)):
            for t in (D('0.000001'),D('.05'),D('.2')):
                q,f=optimum(a,a,t)
                assert abs(q-D('.5'))<D('1e-60')
                u,_=channel(a,a,t)
                assert abs(f-H(u))<D('1e-65')
                count+=2
        a,b=D(3),D(1)
        gap=a-b
        previous_q=previous_err=None
        for exp in (4,6,9,15,25,45):
            t=D(10)**(-exp)
            q,f=optimum(a,b,t)
            L=(1/(gap*t)).ln()
            err=abs(f/t-a*(L-L.ln()))
            assert abs((gap/a)*q*L-1)<D('.31')
            assert err<D(2)
            if previous_err is not None:
                assert err<previous_err
                assert q<previous_q
                count+=2
            previous_q,previous_err=q,err
            count+=2
        for eta in (D(0),D(2),D(6)):
            kappa=D(1)
            qinf,ginf=crossover_optimum(kappa,eta)
            previous_e=None
            for exp in (4,7,12,24,48):
                t=D(10)**(-exp)
                L=(1/(kappa*t)).ln()
                a=kappa+eta/(2*L);b=kappa-eta/(2*L)
                q,f=optimum(a,b,t)
                e=abs((f/t-kappa*L-kappa)-ginf)
                assert abs(q-qinf)<D('.08')
                if previous_e is not None:
                    assert e<previous_e + D('1e-30')
                    count+=1
                previous_e=e
                count+=1
        print('PASS:',count,'high-precision analytical-formula checks')


if __name__=='__main__':
    run()
