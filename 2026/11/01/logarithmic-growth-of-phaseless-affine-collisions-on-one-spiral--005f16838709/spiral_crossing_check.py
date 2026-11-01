"""Reproducible supplementary checks for logarithmic-spiral phaseless collisions.

No symbolic or numerical test is used as proof of the all-parameter theorem.
Python 3 standard library only.
"""
import math
import cmath


def difference(s, alpha, t):
    z = cmath.exp((1+1j*alpha)*t)
    a, b = math.cosh(s), math.sinh(s)
    P = a*z+b
    Q = b*z-a
    return abs(P)**2-abs(Q)**2


def normalized_crossing(alpha, kappa, t):
    return math.sinh(t)/kappa + math.cos(alpha*t)


def count_roots(alpha, kappa):
    # Every root with t >= 0 lies in [0, asinh(kappa)].
    L=math.asinh(kappa)
    n=max(5000,int(150*abs(alpha)*L/math.pi))
    last=normalized_crossing(alpha,kappa,0.)
    assert last>0
    roots=[]
    for i in range(1,n+1):
        t=L*i/n
        now=normalized_crossing(alpha,kappa,t)
        if last*now<0:
            lo,hi=L*(i-1)/n,t
            flo=last
            for _ in range(65):
                mid=(lo+hi)/2
                fm=normalized_crossing(alpha,kappa,mid)
                if flo*fm<=0:
                    hi=mid
                else:
                    lo=mid
                    flo=fm
            roots.append((lo+hi)/2)
        last=now
    for t in roots:
        assert abs(normalized_crossing(alpha,kappa,t))<1e-10
    return roots


checks=0
for alpha in [0.5,1.0,2.3]:
    for s in [0.2,0.8,2.0]:
        kap=math.sinh(2*s)
        for t in [-0.7,0.,0.34,1.8]:
            left=difference(s,alpha,t)
            right=2*math.exp(t)*(math.sinh(t)+kap*math.cos(alpha*t))
            assert abs(left-right)<1e-10*max(1.,abs(right),abs(left))
            checks+=1

for alpha in [0.7,1.0,2.3]:
    for M in [3,5,11,20]:
        kappa=math.sinh((M+1)*math.pi/alpha)+1
        for j in range(M+1):
            v=normalized_crossing(alpha,kappa,j*math.pi/alpha)
            assert (1 if v>0 else -1)==(-1)**j
            checks+=1

# Check representative nonresonant and resonant four-point phaseless samples.
# For nonresonant q=2i, the coefficient intensity lifting columns
# (1, |q^k|^2, 2 Re(q^k), -2 Im(q^k)) have a nonzero 4x4 determinant.
from itertools import permutations
q=2j
A=[]
for k in range(4):
    z=q**k
    A.append([1,int(abs(z)**2),int(2*z.real),int(-2*z.imag)])
sgn=lambda perm: (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
det=sum(sgn(p)*math.prod(A[i][p[i]] for i in range(4)) for p in permutations(range(4)))
assert det!=0
checks+=1
for k in range(12):
    z=q**k
    assert abs(abs(z*z+1j)**2-abs(z*z-1j)**2)<1e-8*max(1,abs(z)**4)
    checks+=1

for alpha in [0.7,1.0,2.3]:
    for logk in [4.,6.,8.,10.]:
        kap=math.exp(logk)
        roots=count_roots(alpha,kap)
        L=math.asinh(kap)
        expected=abs(alpha)*L/math.pi
        assert abs(len(roots)-expected)<4+2*abs(alpha), (alpha,logk,len(roots),expected)
        print('alpha',alpha,'log(kappa)',logk,'N',len(roots),'linear_prediction',round(expected,4))
        checks+=1

print('CHECKS_PASS',checks,'determinant_4nodes',det)
