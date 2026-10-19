"""Finite symbolic and quadrature diagnostics for the two-jump averaging bound.

The proof of the universal root count is in RESULT.md, not in these tests.
Run with: python verify.py  (requires sympy and mpmath)
"""
import math
import random
import sympy as S
import mpmath as mp

r, a, k, c = S.symbols('r a k c', positive=True, finite=True)
z = a / r
G = k * (S.acos(z) + z * S.sqrt(1 - z*z)) + (2*c/r) * S.sqrt(1-z*z)
P = c*(r*r - 2*a*a) - k*a**3
assert S.simplify(S.diff(G, r) + 2*P/(r**3*S.sqrt(r*r-a*a))) == 0

s, a1, a2, c1, c2, k1, k2 = S.symbols('s a1 a2 c1 c2 k1 k2')
p1 = c1*(s-2*a1*a1) - k1*a1**3
p2 = c2*(s-2*a2*a2) - k2*a2**3
cubic = S.expand(p1*p1*(s-a2*a2) - p2*p2*(s-a1*a1))
assert S.Poly(cubic, s).degree() <= 3
assert cubic.subs({a1:1, a2:3, c1:2, c2:4, k1:5, k2:7}) != 0
# Check negative and positive switching locations reduce to the same
# positive-radius affine-step representation.
def direct_F(x, alpha, beta, jumps):
    return alpha*x + beta + sum((k*x+c) for t,k,c in jumps if x>t)

def radial_step_h(x, alpha, jumps):
    slope = 2*alpha + sum(2*k for t,k,c in jumps if t < 0)
    out = slope*x
    for t,k,c in jumps:
        A, B = (k,c) if t > 0 else (-k,c)
        if x>abs(t):out += A*x+B
    return out

rng=random.Random(1729)
for case in range(20):
    alpha=rng.uniform(-2,2); beta=rng.uniform(-4,4)
    locations=[rng.uniform(-4,-0.5), rng.uniform(0.5,4)]
    jumps=[(t,rng.uniform(-2,2),rng.uniform(-2,2)) for t in locations]
    for x in [0.1,0.3,0.6,1.1,2.0,5.0]:
        H=direct_F(x,alpha,beta,jumps)-direct_F(-x,alpha,beta,jumps)
        assert abs(H-radial_step_h(x,alpha,jumps))<1e-10

mp.mp.dps = 40
for alpha,ka,ca,kb,cb,A,B in [
    (1,2,-3,-1,2,1,3),(-2,3,1,2,-4,2,5),(0,1,2,-3,4,1,4)
]:
    # Explicit D for radial h(x)=2 alpha*x + (ka*x+ca) 1_{x>A}
    #                                       + (kb*x+cb) 1_{x>B}
    def h(x):
        return 2*alpha*x + (ka*x+ca if x>A else 0) + (kb*x+cb if x>B else 0)
    def D_integral(rr):
        seg=[0]+[t for t in (A,B) if t<rr]+[rr]
        return 2/rr**2 * sum(mp.quad(lambda xx: xx*h(xx)/mp.sqrt(rr**2-xx**2),[lo,hi])
                             for lo,hi in zip(seg[:-1],seg[1:]))
    def D_explicit(rr):
        out=mp.pi*alpha
        for t,kk,cc in ((A,ka,ca),(B,kb,cb)):
            if rr>t:
                z=t/rr
                out += kk*(mp.acos(z)+z*mp.sqrt(1-z*z))+(2*cc/rr)*mp.sqrt(1-z*z)
        return out
    for rr in (mp.mpf(A)/2, mp.mpf(A+B)/2, 2*B):
        assert abs(D_integral(rr)-D_explicit(rr)) < mp.mpf('1e-15'), (D_integral(rr),D_explicit(rr))
print('PASS: exact derivative identity, cubic-degree certificate, 120 radial reductions, 9 independent quadratures.')

# An explicit rational-and-pi two-jump witness with six sign changes.
# Uses enclosing interval arithmetic for pi, roots, and atan2, rather
# than rounded point evaluation.  These six brackets, together with
# the proved six-zero upper bound, force six distinct simple zeros.
iv=mp.iv
iv.dps=85
alpha=iv.mpf(8)/(109*iv.pi*50**5)
beta=-iv.mpf(239)/(3270*50**4)
delta=iv.mpf(115)/19620000+125*alpha/36+25*beta/24
k_a=iv.mpf(10)/109-2
c_a=-iv.mpf(81)/218+delta
k_b=alpha-iv.mpf(10)/109
c_b=beta-c_a

def enclosed_D(label):
    rr=iv.mpf(label)
    value=iv.pi
    for t,kk,cc in ((1,k_a,c_a),(5,k_b,c_b)):
        if float(label)>t:
            z=t/rr
            q=iv.sqrt(1-z*z)
            # acos(z)=atan2(sqrt(1-z*z),z) for 0<z<1
            value += kk*(iv.atan2(q,z)+z*q)+2*cc/rr*q
    return value

brackets=[('1.9','2.1'),('4.5','4.8'),('14','16'),
          ('46','48'),('100','102'),('149','151')]
for left,right in brackets:
    vl,vr=enclosed_D(left),enclosed_D(right)
    assert (vl.a>0 and vr.b<0) or (vl.b<0 and vr.a>0), (left,right,vl,vr)
print('PASS: six disjoint sign-changing brackets, with interval enclosures.')
