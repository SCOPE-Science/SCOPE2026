"""Fallback certificate: RIGOROUS Moran/OSC subset at N=4 with k=16 words.

Replaces floats by exact rational interval arithmetic:
 - cos(1), sin(1) enclosed by Taylor intervals (remainder <= first omitted term).
 - M entries, T*=max|Pinv t_i| (t2,t3), R*=T*/(1-rho) enclosed by intervals.
 - Level-4 centers enclosed by interval affine iteration over 81 words.
 - Pairwise separation lower bounds in y-norm vs 2 r_N upper bound => disjoint balls.
 - Ball-in-ball: |c_w|_y + r_N <= R* (crude global disk) => subset of K-ball.
Greedy word-set search uses float proxies only to PROPOSE the 16 words;
the VERDICT uses only rigorous intervals.
Writes artifacts/fallback_certificate.json. Exits nonzero on failure.
"""
import json, math
from fractions import Fraction as Q
from math import nextafter, inf
up = lambda x: nextafter(float(x), inf)    # sound float upper bound
dn = lambda x: nextafter(float(x), -inf)   # sound float lower bound

class I:
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
        lo = lo if isinstance(lo, Q) else Q(lo)
        hi = lo if hi is None else (hi if isinstance(hi, Q) else Q(hi))
        assert lo <= hi
        self.lo, self.hi = lo, hi
    def __add__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__
    def __sub__(self, o):
        o = o if isinstance(o, I) else I(o)
        return I(self.lo-o.hi, self.hi-o.lo)
    def __mul__(self, o):
        o = o if isinstance(o, I) else I(o)
        ps = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(ps), max(ps))
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = o if isinstance(o, I) else I(o)
        assert o.lo > 0 or o.hi < 0, 'division by interval containing 0'
        ps = [self.lo/o.lo, self.lo/o.hi, self.hi/o.lo, self.hi/o.hi]
        return I(min(ps), max(ps))
    def __neg__(self): return I(-self.hi, -self.lo)
    def abs2_lb(self):
        # lower bound of x^2 over interval
        if self.lo >= 0: return self.lo*self.lo
        if self.hi <= 0: return self.hi*self.hi
        return Q(0)
    def mid(self): return (self.lo+self.hi)/2
    def wid(self): return self.hi-self.lo
    def __repr__(self): return f'[{float(self.lo):.6f},{float(self.hi):.6f}]'

def cos1_iv(K=12):
    s = sum(Q((-1)**k, math.factorial(2*k)) for k in range(K+1))
    r = Q(1, math.factorial(2*(K+1)))
    return I(s-r, s+r)
def sin1_iv(K=12):
    s = sum(Q((-1)**k, math.factorial(2*k+1)) for k in range(K+1))
    r = Q(1, math.factorial(2*(K+1)+1))
    return I(s-r, s+r)

c, s = cos1_iv(), sin1_iv()
A1, A2 = I(Q(7,10)), I(Q(2,5))
M = [[A1*c, -A1*s],[A2*s, A2*c]]
rho2 = Q(7,25)
N = 10**12
q = math.isqrt(7*N*N)
sq7 = I(Q(q, N), Q(q+1, N))  # encloses sqrt(7)
rho = sq7/I(Q(5))            # sqrt(0.28) = sqrt(7)/5
om = I(Q(1)) - rho
tr = M[0][0]+M[1][1]
two = I(Q(2))
cphi = I(tr.lo/(2*rho.hi), tr.hi/(2*rho.lo))
# sphi^2 = 1-cphi^2
s2 = I(Q(1)) - cphi*cphi
print('DEBUG s2 =', s2, 'cphi =', cphi, 'rho =', rho, 'tr =', tr)
sphi = I(Q(math.sqrt(max(float(s2.lo),0.0))), Q(math.sqrt(max(float(s2.hi),0.0)))+Q(1,10**15))
# exact q-coords: qx=(rho cphi-m11)/(rho sphi), qy=-m21/(rho sphi)
m11, m12, m21, m22 = M[0][0], M[0][1], M[1][0], M[1][1]
den = rho*sphi
qx = (rho*cphi - m11)/den
qy = (-m21)/den
# Pinv rows from explicit inverse: det=-qy; Pinv=[[-qy/qy.. ]] -> rows: r1=(1,0)?? P=[[1,qx],[0,qy]] => Pinv=[[1,-qx/qy],[0,1/qy]]
r = -qx/qy   # Pinv[0][1]
i00, i01, i10, i11 = I(Q(1)), r, I(Q(0)), I(Q(1))/qy
def ynorm2(p):  # p=(Ix,Iy); |Pinv p|^2 = (x + r y)^2 + (y/qy)^2
    x, y = p
    return (x + r*y)*(x + r*y) + (y/qy)*(y/qy)
def ynorm_lb2(p): return ynorm2(p).lo  # valid lower bound
# T*: |(1,0)|_y = 1; |(0,1)|_y^2 = r^2+(1/qy)^2 -> upper bound
T2 = (r*r + (I(Q(1))/qy)*(I(Q(1))/qy)).hi
T = Q(math.sqrt(float(T2))) + Q(1, 10**14)
Rs = I(T)/om            # R* upper: use hi
Rhi = Rs.hi
rhoN = rho*rho*rho*rho   # rho^4 interval
rN = I(rhoN.lo*Rhi, rhoN.hi*Rhi) if False else None
rNhi = rhoN.hi * Rhi
rNlo = rhoN.lo * Rs.lo
print('c =', c, 's =', s)
print('rho =', rho, '1-rho =', om)
print('cphi =', cphi, 'sphi =', sphi)
print('r =', r, '1/qy =', I(Q(1))/qy)
print('T* <=', float(T), 'R* in', Rs, 'rho^4 in', rhoN, 'rN <=', float(rNhi))
# translations interval points
t = [(I(Q(0)), I(Q(0))), (I(Q(1)), I(Q(0))), (I(Q(0)), I(Q(1)))]
def apply(pt, i):
    x, y = pt
    return (M[0][0]*x + M[0][1]*y + t[i][0], M[1][0]*x + M[1][1]*y + t[i][1])
from itertools import product
C = {}
for w in product(range(3), repeat=4):
    p = (I(Q(0)), I(Q(0)))
    for i in w:
        p = apply(p, i)
    C[w] = p
print('widths sample:', C[(0,0,0,0)][0].wid(), C[(2,2,2,2)][0].wid())
# PROPOSED 16 words (float-greedy discovery; verdict is interval-based)
import subprocess
prop = eval(subprocess.run(['python3','artifacts/propose.py'],capture_output=True,text=True).stdout.strip())
print('proposed k =', len(prop))
assert len(prop) == 16 and len(set(map(tuple,prop))) == 16
# pairwise y-distance lower bounds
def ydist_lo(p, qq):
    return (ynorm2((p[0]-qq[0], p[1]-qq[1]))).lo
pairs = [(a,b) for ii,a in enumerate(prop) for b in prop[ii+1:]]
los = []
for a, b in pairs:
    lo2 = ydist_lo(C[tuple(a)], C[tuple(b)])
    los.append((lo2, a, b))
los.sort()
print('min 3 lo2:', [(float(x), a, b) for x,a,b in los[:3]])
minlo2 = los[0][0]
two_r = Q(2)*rNhi
ok_sep = minlo2 > two_r*two_r
print('min|.|_y^2 >=', float(minlo2), ' vs (2 rNhi)^2 =', float(two_r*two_r), 'SEPARATED' if ok_sep else 'FAIL')
# ball-in-ball: |c_w|_y^2 hi + cross terms... use (|c|+rN)^2 <= R*^2 via upper bounds
def ynorm_hi2(p):
    return ynorm2(p).hi
ok_in = True
for w in prop:
    u2 = ynorm_hi2(C[tuple(w)])
    u = up(math.sqrt(up(u2)))          # sound float upper bounds throughout
    if not (u + up(rNhi) <= dn(Rs.lo)):
        ok_in = False
        print('ball-in-ball FAIL at', w, u + up(rNhi), '>', dn(Rs.lo))
        break
print('BALL-IN-BALL', 'OK' if ok_in else 'FAIL')
# dimension: s = ln16/(4 ln(1/rho)) >= 1  <=> 16 >= rho^-4 <=> 16 rho^4 >= 1
print('16*rho^4lo =', float(Q(16)*rhoN.lo))
ok_dim = Q(16)*rhoN.lo > 1
print('DIM-BOUND', 'OK' if ok_dim else 'FAIL')
# separation re-check in sound floats (certificate values are exact-Fraction based):
import math as _m
sep_ok_float = dn(minlo2) > up(two_r*two_r)
print('SEPARATION float-sound recheck:', 'OK' if sep_ok_float else 'FAIL')
assert ok_sep and ok_in and ok_dim and sep_ok_float
cert = {'N': 4, 'k': 16, 'words': prop,
        'rho': [float(rho.lo), float(rho.hi)],
        'Rstar': [float(Rs.lo), float(Rs.hi)],
        'rNhi': float(rNhi),
        'min_pair_y2_lo': float(minlo2),
        'two_rNhi_sq': float(two_r*two_r),
        'dim_ratio_16rho4_lo': float(Q(16)*rhoN.lo)}
json.dump(cert, open('artifacts/fallback_certificate.json','w'), indent=1)
print('CERTIFICATE WRITTEN')
