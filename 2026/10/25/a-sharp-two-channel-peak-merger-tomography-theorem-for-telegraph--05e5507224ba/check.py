"""Numerical verification for symmetric-telegraph two-channel peak coalescence."""
import math
import cmath
import random

RHO = math.sqrt((1.0 + math.sqrt(2.0)) / 2.0)


def amplitude_cut(g, q):
    h = g + q
    t = (2.0 * g + q) / h
    return h * h / (math.sqrt(1.0 + t*t) + t)


def absorption_cut(g, q):
    return (g + q)**3 / (3.0*g + 2.0*q)


def response(g, a, q, w):
    s = complex(g, -w)
    return (s+q)/(s*(s+q)+a*a)


def response_matrix(g, a, q, w):
    # conditional phase evolutions have switching q/2 in both directions
    s = complex(g, -w)
    d = complex(s.real+q/2, s.imag)
    # solve (s+q/2 - i a) f+ - (q/2) f- = 1
    #       -(q/2) f+ + (s+q/2 + i a) f- = 1
    det = (d-1j*a)*(d+1j*a) - (q/2)**2
    plus = ((d+1j*a)+q/2)/det
    minus = ((d-1j*a)+q/2)/det
    return (plus+minus)/2


def bisect_switch(g,a,cut):
    assert a*a > cut(g,0)
    lo,hi = 0.,max(1.,a)
    while cut(g,hi) < a*a:
        hi *= 2
        assert hi < 1e9
    for _ in range(100):
        mid = (lo+hi)/2
        if cut(g,mid) < a*a:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def recover(P,Q):
    assert P>0 and Q/P>RHO
    lo,hi = 0.,max(P,Q)
    while amplitude_cut(hi,Q) > absorption_cut(hi,P):
        hi*=2
        assert hi<1e13
    for _ in range(110):
        mid=(lo+hi)/2
        if amplitude_cut(mid,Q)>absorption_cut(mid,P):
            lo=mid
        else:
            hi=mid
    g=(lo+hi)/2
    a=math.sqrt(absorption_cut(g,P))
    return g,a


def main():
    random.seed(20261023)
    direct_n=0
    reconstruction_n=0
    peak_n=0
    for _ in range(500):
        g=math.exp(random.uniform(-1.5,1.5))
        a=g*math.exp(random.uniform(math.log(0.59),math.log(15)))
        P=bisect_switch(g,a,absorption_cut)
        Q=bisect_switch(g,a,amplitude_cut)
        assert P>0 and Q>P
        assert Q/P>RHO * (1-1e-11)
        gp,ap=recover(P,Q)
        assert math.isclose(g,gp,rel_tol=2e-8,abs_tol=2e-8), (g,a,P,Q,gp,ap)
        assert math.isclose(a,ap,rel_tol=2e-8,abs_tol=2e-8)
        reconstruction_n+=1
        for _j in range(3):
            w=random.uniform(-5*a,5*a)
            q=random.uniform(0,5*a)
            z=response(g,a,q,w)
            z2=response_matrix(g,a,q,w)
            assert abs(z-z2) < 2e-10*(1+abs(z))
            direct_n+=1
        # At P absorption turns from two to one maxima, M remains split;
        # at Q both have a central maximum. Test via the exact derivatives at z=0.
        for q in [P*(1-1e-6), (P+Q)/2, Q*(1+1e-6)]:
            h=g+q; c=g*h+a*a; b=(2*g+q)**2 - 2*c
            dm=c*c-h*h*b
            di=g*c*c-h*c*b
            assert (dm>0)==(q<Q), (g,a,P,Q,q,dm)
            assert (di>0)==(q<P), (g,a,P,Q,q,di)
            peak_n+=1
    # The sharp ratio boundary is approached as g tends to zero.
    P=2.0
    for ratio in [1.01,RHO,1.098,1.1,1.3,2.0,100.0]:
        val=amplitude_cut(1e-10,P*ratio)/absorption_cut(1e-10,P)
        assert (val >1)==(ratio >RHO) or abs(ratio-RHO)<1e-12
    print('PASS: 500 full forward/inverse parameter reconstructions')
    print(f'PASS: {direct_n} independent conditional matrix response comparisons')
    print(f'PASS: {peak_n} peak-topology sign checks')
    print('PASS: sharp ratio boundary numerical tests')
    print('rho* = %.15f' % RHO)


if __name__ == '__main__':
    main()
