from fractions import Fraction as F
from math import sqrt


def dets(k, s):
    D = [F(1)]
    if k == 0:
        return D
    D.append(F(1) + 2*s)
    for j in range(2, k+1):
        D.append((F(1)+2*s)*D[-1] - s*s*D[-2])
    return D


def c2(s):
    # M = I+s*T_2 = [[1+2s,-s],[-s,1+2s]]
    a = F(1) + 2*s
    den = a*a - s*s
    rdiag = a/den
    roff = s/den
    return ((2*rdiag-F(1), 2*roff), (2*roff, 2*rdiag-F(1)))

# Exact threshold equation for k=2: D_2 - 2 D_1 = 3 s^2 - 1.
s = F(3,5)
D = dets(2,s)
assert D[2] - 2*D[1] == 3*s*s - 1
C = c2(s)
assert C == ((F(-1,56),F(15,56)),(F(15,56),F(-1,56)))
assert C[0][0]*C[0][1] == F(-15,3136)

s_safe = F(11,20)
C_safe = c2(s_safe)
assert C_safe == ((F(37,1643),F(440,1643)),(F(440,1643),F(37,1643)))
assert all(x > 0 for row in C_safe for x in row)

# Exact inverse-diagonal formula and endpoint minimality on rational probes.
for k in range(2,9):
    for s in (F(1,10),F(1,3),F(3,5),F(1)):
        D = dets(k,s)
        diag = [D[i]*D[k-i-1]/D[k] for i in range(k)]
        assert diag[0] == D[k-1]/D[k] == diag[-1]
        assert min(diag) == diag[0]
        q = [None] + [D[j]/D[j-1] for j in range(1,k+1)]
        assert all(q[j+1] < q[j] for j in range(1,k))

# Numerical roots are diagnostics only; the proof establishes uniqueness and the limit.
def dfloat(k,s):
    d0=1.0
    if k==0: return d0
    d1=1.0+2.0*s
    if k==1: return d1
    for _ in range(2,k+1):
        d0,d1=d1,(1.0+2.0*s)*d1-s*s*d0
    return d1

def f(k,s):
    return dfloat(k,s)-2.0*dfloat(k-1,s)

def root(k):
    lo,hi=0.0,1.0
    assert f(k,lo)<0 and f(k,hi)>0
    for _ in range(100):
        mid=(lo+hi)/2
        if f(k,mid)<=0: lo=mid
        else: hi=mid
    return (lo+hi)/2

roots=[root(k) for k in range(1,15)]
assert abs(roots[0]-0.5)<1e-14
assert abs(roots[1]-1/sqrt(3))<1e-13
assert all(roots[i] < roots[i+1] for i in range(len(roots)-1))
limit=2-sqrt(2)
assert all(r < limit for r in roots)
assert limit-roots[-1] < 1e-12

print('VERIFY_OK')
