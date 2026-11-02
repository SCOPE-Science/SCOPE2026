"""Reproducible finite checks for the local critical Bergman-dilation normal form.

All polynomial moment computations below are exact rational arithmetic, including
non-real coefficients represented by pairs of rational numbers. They supplement,
not replace, the analytic proof for all functions and real alpha > 1.
"""
from fractions import Fraction as F
from random import Random

rng = Random(17301)
N = 0

def check(condition, message):
    global N
    N += 1
    if not condition:
        raise AssertionError(message)

def g(x=0, y=0):
    return (F(x), F(y))

def ga(u, v):
    return (u[0] + v[0], u[1] + v[1])

def gm(u, v):
    return (u[0]*v[0]-u[1]*v[1], u[0]*v[1]+u[1]*v[0])

def gs(u, z):
    return (u[0]*z, u[1]*z)

def norm2(u):
    return u[0]**2 + u[1]**2

def moments(alpha, end):
    out=[F(1)]
    for n in range(1,end+1):
        out.append(out[-1] * F(n)/(alpha+n-1))
    return out

def evaluate(f, alpha):
    deg=len(f)-1
    m=moments(alpha,2*deg)
    s=sum(m[j]*norm2(v) for j,v in enumerate(f))
    sq=[g() for _ in range(2*deg+1)]
    for i,x in enumerate(f):
        for j,y in enumerate(f):
            sq[i+j]=ga(sq[i+j],gm(x,y))
    # r^2=1/2: L4^4 = sum mu_n 2^{-n}|(f*f)_n|^2.
    l4=sum(m[n]*F(1,2**n)*norm2(v) for n,v in enumerate(sq))
    return s*s-l4

def form(f, alpha):
    a=f[1] if len(f)>1 else g()
    b=f[2] if len(f)>2 else g()
    m=moments(alpha,len(f)-1)
    a2=gm(a,a)
    correction=ga(b,gs(a2,F(-1,2)))
    total=norm2(a)**2/(alpha*alpha*(alpha+1)) + m[2]*norm2(correction)
    for n in range(3,len(f)):
        total += (F(2)-F(1,2**(n-2)))*m[n]*norm2(f[n])
    return total


def structural_remainder(f, alpha):
    """Exact difference D-Q via the resonant decomposition f²=P+R."""
    degree=len(f)-1
    m=moments(alpha,2*degree)
    a=f[1]
    h=f[2:]
    hn=sum(m[n]*norm2(f[n]) for n in range(2,len(f)))
    p=[g() for _ in range(2*degree+1)]
    p[0]=g(1)
    p[1]=gs(a,F(2))
    for n in range(2,len(f)):
        p[n]=gs(f[n],F(2))
    p[2]=ga(p[2],gm(a,a))
    sq=[g() for _ in range(2*degree+1)]
    for i,x in enumerate(f):
        for j,y in enumerate(f):
            sq[i+j]=ga(sq[i+j],gm(x,y))
    rem=[ga(sq[i],gs(p[i],F(-1))) for i in range(len(p))]
    cross=sum(m[n]*F(1,2**n)*(p[n][0]*rem[n][0]+p[n][1]*rem[n][1]) for n in range(len(p)))
    nr=sum(m[n]*F(1,2**n)*norm2(rem[n]) for n in range(len(rem)))
    return 2*m[1]*norm2(a)*hn+hn*hn-2*cross-nr

def random_coeff(scale):
    return g(F(rng.randint(-4,4),6)*scale,F(rng.randint(-4,4),6)*scale)

for alpha in [F(6,5),F(3,2),F(2),F(3),F(7)]:
    m=moments(alpha,9)
    check(m[1]==F(1)/alpha,"first moment")
    check(m[2]==F(2)/(alpha*(alpha+1)),"second moment")
    check(m[1]**2-m[2]/2==1/(alpha**2*(alpha+1)),"quartic constant")
    for _ in range(25):
        f=[g(1),random_coeff(F(1,8))] + [random_coeff(F(1,32)) for j in range(3)]
        d=evaluate(f,alpha)
        check(d>=0, "finite polynomial contraction violated")
        q=form(f,alpha)
        check(q>=0, "normal form negativity")
        check(d-q==structural_remainder(f,alpha),"exact structural remainder identity")
    for k in [4,6,8,10,12]:
        e=F(1,2**k)
        a=g(e,F(1,2)*e)
        a2=gm(a,a)
        f=[g(1),a,gs(a2,F(1,2))]
        d=evaluate(f,alpha)
        q=form(f,alpha)
        # On the canonical nonlinear correction, D/Q=1+O(e^2).
        check(abs(d/q-1)<F(10)*e*e,"canonical correction convergence")
        check(q==norm2(a)**2/(alpha**2*(alpha+1)),"sharp leading value")
        affine=[g(1),a]
        da=evaluate(affine,alpha)
        check(da==norm2(a)**2 * (alpha+2)/(2*alpha**2*(alpha+1)),"affine exact deficit")
        check(d<da,"quadratic correction must improve affinity")
    # Two genuinely different scales (h = epsilon and h = epsilon^2).
    for k in [5,7,9]:
        e=F(1,2**k)
        for power in [1,2]:
            a=g(e,F(1,3)*e)
            f=[g(1),a,random_coeff(e**power),random_coeff(e**power),random_coeff(e**power)]
            d=evaluate(f,alpha)
            q=form(f,alpha)
            h2=sum(m[j]*norm2(f[j]) for j in range(2,5))
            scale=norm2(a)**2+h2
            # Exact computations verify relative little-o over shrinking perturbations.
            check(abs(d-q) / scale < F(20)*e,"normal form bound")
            check(d>=0,"nonnegative deficit with mixed scales")
print(f"PASS: {N} exact rational checks in five Bergman weights, complex modes, and two perturbation scales")
