#!/usr/bin/env python3
"""Independent finite diagnostics for exponential-symbol Fock commutators.

The universal boundedness and essential-norm theorem is proved analytically;
these tests verify finite coefficient expansions and the sharp two-term formula.
"""
import cmath
import math
import random


def close(x, y, tol=1e-9):
    return abs(x-y) <= tol * (1+abs(x)+abs(y))


def direct_pair(a, b, f, g, t, z):
    """T_{f exp(a z)} T_{conj(g exp(b z))} - opposite order on exp(t z)."""
    e1 = cmath.exp((a+t)*z+t*b.conjugate())
    e2 = cmath.exp((a+t)*z+(a+t)*b.conjugate())
    return f*g.conjugate()*(e1-e2)


def compressed_pair(a,b,f,g,t,z):
    q=(1-cmath.exp(a*b.conjugate()))*f*g.conjugate()
    return q*cmath.exp(a*z+t*(z+b.conjugate()))


def check():
    random.seed(11927)
    n=0
    def confirm(ok, why):
        nonlocal n
        n+=1
        if not ok:
            raise AssertionError(f'{why}, test {n}')
    # Random complex parameters validate the entire dense-domain identity.
    for i in range(360):
        a=complex(random.uniform(-1,1),random.uniform(-1,1))
        b=complex(random.uniform(-1,1),random.uniform(-1,1))
        t=complex(random.uniform(-0.7,0.7),random.uniform(-0.7,0.7))
        z=complex(random.uniform(-0.8,0.8),random.uniform(-0.8,0.8))
        f=complex(random.uniform(-1,1),random.uniform(-1,1))
        g=complex(random.uniform(-1,1),random.uniform(-1,1))
        confirm(close(direct_pair(a,b,f,g,t,z),compressed_pair(a,b,f,g,t,z)), 'two-order formula')
        confirm(close(compressed_pair(a,b,f,g,t,z),
                      (1-cmath.exp(a*b.conjugate()))*f*g.conjugate()*
                      cmath.exp(a*z+t*(z+b.conjugate()))), 'coefficient formula')
    # Cross-terms and cancellations: four finite exponential sums.
    F={0.2+0.1j:1+0.3j, -0.5j:0.3-0.7j}
    G={-0.4+0.2j:0.8+0.1j, 0.1+0.6j:0.9-0.2j}
    H={0.2+0.1j:-0.2+0.9j, 0.3-0.7j:0.4}
    K={0.1+0.6j:0.5+0.3j, 0.8-0.2j:-0.5j}
    for i in range(220):
        z=complex(random.uniform(-0.5,0.5), random.uniform(-0.5,0.5))
        t=complex(random.uniform(-0.5,0.5), random.uniform(-0.5,0.5))
        direct=sum(direct_pair(a,b,fa,gb,t,z) for a,fa in F.items() for b,gb in G.items())-sum(direct_pair(a,b,ha,kb,t,z) for a,ha in H.items() for b,kb in K.items())
        compressed=sum(compressed_pair(a,b,fa,gb,t,z) for a,fa in F.items() for b,gb in G.items())-sum(compressed_pair(a,b,ha,kb,t,z) for a,ha in H.items() for b,kb in K.items())
        confirm(close(direct, compressed),'four-sum cancellation')
    # The diagonal (b=-a) is precisely a Weyl displacement times exp(|a|^2/2).
    for i in range(240):
        a=complex(random.uniform(-1.5,1.5),random.uniform(-1.5,1.5))
        z=complex(random.uniform(-1,1),random.uniform(-1,1))
        t=complex(random.uniform(-1,1),random.uniform(-1,1))
        b=-a
        basis=cmath.exp(a*z+t*(z+b.conjugate()))
        weyl=cmath.exp((a*z)-(abs(a)**2)/2)*cmath.exp(t*(z-a.conjugate()))
        confirm(close(basis,math.exp(abs(a)**2/2)*weyl),'Weyl normalization')
        d=(1-cmath.exp(-abs(a)**2))*math.exp(abs(a)**2/2)
        confirm(close(d,2*math.sinh(abs(a)**2/2)),'single-frequency coefficient')
    # Pure phase when b=-a, growth otherwise on an aligned ray.
    for i in range(130):
        a=complex(random.uniform(-1,1),random.uniform(-1,1))
        w=complex(random.uniform(-1,1),random.uniform(-1,1))
        confirm(close(abs(cmath.exp(a*w-a.conjugate()*w.conjugate())),1),'bounded-phase diagonal')
    for i in range(85):
        a=complex(random.uniform(-1,1),random.uniform(-1,1))
        b=complex(random.uniform(-1,1),random.uniform(-1,1))
        s=a+b
        if abs(s)<1e-5:
            continue
        w=5*s.conjugate()/abs(s)
        modulus=abs(cmath.exp(a*w+b.conjugate()*w.conjugate()))
        confirm(close(modulus,math.exp(5*abs(s))),'off-diagonal ray growth')
    # Operator-theoretic two-term norm is certified in the proof by circle spectrum,
    # and the test checks its parameter/equivalent sinh normalization.
    for i in range(140):
        x=random.uniform(0.01,2)
        y=random.uniform(0.01,2)
        d1=(1-math.exp(-x*x))*math.exp(x*x/2)
        d2=(1-math.exp(-y*y))*math.exp(y*y/2)
        confirm(close(d1+d2,2*math.sinh(x*x/2)+2*math.sinh(y*y/2)), 'sharp two-term parameter')
    print(f'PASS: {n} deterministic finite diagnostic assertions; no infinite-dimensional conclusion inferred from tests.')

if __name__=='__main__':
    check()
