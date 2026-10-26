"""Reproduce the two-frequency inverse spectral identities using only Python stdlib.

This finite test is a computational sanity check, not a substitute for the analytic proof.
"""
import math
import random


def forward(h_upper, h_lower, beta, k):
    a = 1.0 / math.tanh(k * h_upper)
    b = 1.0 / math.tanh(k * h_lower)
    leading = a * b + beta
    discr = math.sqrt((a-b)**2 + 4 * beta * (a*b-1+beta))
    total = a + b
    lower = 2 * (1-beta) / (total+discr)
    upper = (total+discr) / (2*leading)
    return lower, upper


def product_invariant(roots):
    p = roots[0]*roots[1]
    return p/(1+p)


def inferred_total_depth(roots, k):
    return (math.atanh(roots[0])+math.atanh(roots[1]))/k


def F(k, H, z):
    return 1-math.cosh(k*z)/math.cosh(k*H)


def reconstruction(k1, roots1, k2, roots2):
    H1=inferred_total_depth(roots1,k1)
    H2=inferred_total_depth(roots2,k2)
    assert abs(H1-H2)<1e-8, ('incompatible total depths',H1,H2)
    H=(H1+H2)*.5
    q1=product_invariant(roots1)
    q2=product_invariant(roots2)
    ratio=q2/q1
    def R(z): return F(k2,H,z)/F(k1,H,z)
    R0=R(0)
    Rend=k2*math.tanh(k2*H)/(k1*math.tanh(k1*H))
    assert R0-1e-12<=ratio<Rend+1e-12
    if abs(ratio-R0)<1e-11:
        z=0.0
    else:
        lo=0.0;hi=H
        for _ in range(90):
            mid=(lo+hi)*.5
            if R(mid)<ratio:lo=mid
            else:hi=mid
        z=(lo+hi)*.5
    beta=1-2*q1/F(k1,H,z)
    assert 0<beta<1
    return H,z,beta


def G(k,H,z):
    return k*math.sinh(k*z)/(math.cosh(k*H)-math.cosh(k*z))


def run():
    rnd=random.Random(412013)
    for i in range(600):
        H=rnd.uniform(.5,2.5)
        z=H*rnd.uniform(.05,.85)
        beta=rnd.uniform(.08,.92)
        k1=rnd.uniform(.2,.6)
        k2=rnd.uniform(.85,1.8)
        hu=(H+z)*.5;hl=(H-z)*.5
        r1=forward(hu,hl,beta,k1)
        r2=forward(hu,hl,beta,k2)
        assert 0<r1[0]<r1[1]<1 and 0<r2[0]<r2[1]<1
        hr,zr,br=reconstruction(k1,r1,k2,r2)
        assert abs(H-hr)<2e-9,(i,H,hr)
        assert abs(z-zr)<3e-6,(i,z,zr)
        assert abs(beta-br)<3e-6,(i,beta,br)
        for k,rs in [(k1,r1),(k2,r2)]:
            assert abs(product_invariant(rs)-(1-beta)*F(k,H,z)*.5)<1e-12
        assert G(k1,H,z)>G(k2,H,z)
    # Symmetric equal-depth case can be distinguished via the left endpoint.
    for beta in [.12,.5,.88]:
        r1=forward(1,1,beta,.33)
        r2=forward(1,1,beta,1.4)
        hr,zr,br=reconstruction(.33,r1,1.4,r2)
        assert abs(hr-2)<1e-11 and zr==0 and abs(br-beta)<1e-10
    # Exact spectral reflection holds pointwise at arbitrary positive k.
    for k in [.1,.4,1.2,3.]:
        a=forward(.4,1.2,.4,k)
        b=forward(1.2,.4,.4,k)
        assert all(abs(x-y)<1e-12 for x,y in zip(a,b))
    print('CHECK_OK: 600 independent forward/inverse cases, strict-ratio samples, symmetric cases, reflection')

if __name__=='__main__':run()
