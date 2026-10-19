"""Exact checks for finite triplet majority/contrarian dynamics.

Usage: python check.py  (requires SymPy). This verifies combinatorial
transition-moment formulas, critical drift, and both variance constants.
"""
from fractions import Fraction as Q
from math import comb
import sympy as s

p,a,b=s.symbols('p a b',real=True)
q=[a,b,1-b,1-a]
w=[s.binomial(3,k)*p**k*(1-p)**(3-k) for k in range(4)]
f=s.factor(sum(w[k]*q[k] for k in range(4)))
expect=s.factor(f)
y=s.symbols('y',real=True)
assert s.factor(f.subs(p,y+s.Rational(1,2))-s.Rational(1,2) - (s.Rational(3,2)*(1-a-b)*y-2*(1+a-3*b)*y**3))==0
assert s.factor(f.subs({a:a,b:s.Rational(1,3)-a,p:y+s.Rational(1,2)})-(y+s.Rational(1,2)-8*a*y**3))==0
mu=s.Rational(1,2)
weights=[s.Rational(comb(3,k),8) for k in range(4)]
qbar=sum(weights[k]*q[k] for k in range(4))
Eflip=s.factor(sum(weights[k]*q[k]*(1-q[k]) for k in range(4)))
Vq=s.factor(sum(weights[k]*(q[k]-qbar)**2 for k in range(4)))
Cov=s.factor(sum(weights[k]*(q[k]-qbar)*(k-s.Rational(3,2)) for k in range(4)))
var=s.factor(Eflip+3*Vq-4*Cov**2)
low=s.factor(var.subs(b,s.Rational(1,3)-a))
upper=s.factor(var.subs(b,s.Rational(5,3)-a))
assert s.simplify(low-(s.Rational(1,6)+2*a*a))==0
assert s.simplify(upper-(s.Rational(1,6)+2*(1-a)**2))==0
print('mean polynomial:',expect)
print('critical lower diffusion variance:',low)
print('critical upper diffusion variance:',upper)


def falling(n,k):
    out=1
    for i in range(k):out*=n-i
    return out

def probK(N,j,k):
    return Q(comb(3,k)*falling(j,k)*falling(N-j,3-k),falling(N,3))

def probKL(N,j,k,l):
    return Q(comb(3,k)*comb(3,l)*falling(j,k+l)*falling(N-j,6-k-l),falling(N,6))

def exact_moments(N,j,aa,bb):
    qq=[aa,bb,1-bb,1-aa]
    pk=[probK(N,j,k) for k in range(4)]
    pq=sum(pk[k]*qq[k] for k in range(4))
    pq2=sum(pk[k]*qq[k]**2 for k in range(4))
    eflip=sum(pk[k]*qq[k]*(1-qq[k]) for k in range(4))
    eq1q2=sum(probKL(N,j,k,l)*qq[k]*qq[l] for k in range(4) for l in range(4))
    m=N//3
    varJ=3*m*eflip+9*m*(pq2-pq*pq)+9*m*(m-1)*(eq1q2-pq*pq)
    return pq, varJ/Q(N)

for aa,bb in [(Q(1,6),Q(1,6)),(Q(1,4),Q(1,12)),(Q(3,4),Q(11,12)),(Q(5,6),Q(5,6))]:
    vlim=Q(1,6)+2*min(aa,1-aa)**2
    for N in [12,24,60,120,240,600]:
        mn,v=exact_moments(N,N//2,aa,bb)
        assert mn==Q(1,2)
        # Sampling-without-replacement correction vanishes as N grows.
        if N==600: assert abs(v-vlim)<Q(1,100)
    print('parameters',aa,bb,'sigma^2 limit',vlim,'N=600 exact',v)

# Separately enumerate every 6-agent grouping (all 10 unordered triplet bipartitions)
# and conditional outputs for one explicit critical parameter.
from itertools import combinations
N=6; j=3;aa=Q(1,6);bb=Q(1,6)
items=tuple(range(6)); triples=[]
for G in combinations(items,3):
    H=tuple(i for i in items if i not in G)
    if G[0]<H[0]:triples.append((G,H))
assert len(triples)==10
mu_enum=Q(0);second_enum=Q(0)
for G,H in triples:
    qs=[]
    for T in (G,H):
        k=sum(i<j for i in T)
        qs.append([aa,bb,1-bb,1-aa][k])
    m=3*(qs[0]+qs[1])
    v=3*(qs[0]*(1-qs[0])+qs[1]*(1-qs[1]))
    mu_enum += m/Q(len(triples))
    second_enum += (v+m*m)/Q(len(triples))
_,vardensity=exact_moments(6,3,aa,bb)
assert mu_enum==3 and second_enum-mu_enum**2==vardensity*6
print('N=6 full partition enumeration: PASS; E, Var:',mu_enum,vardensity)
# Exhaustive six-agent transition kernels certify the exact flip-front parity duality.
def one_step_mass6(j, aa, bb):
    masses=[Q(0) for _ in range(7)]
    for G,H in triples:
        qg=[]
        for T in (G,H):
            k=sum(i<j for i in T)
            qg.append([aa,bb,1-bb,1-aa][k])
        for r in range(4):
            for t in range(4):
                masses[r+t] += Q(comb(3,r)*comb(3,t),10)*qg[0]**r*(1-qg[0])**(3-r)*qg[1]**t*(1-qg[1])**(3-t)
    assert sum(masses)==1
    return masses

for j in range(7):
    low_k=one_step_mass6(j,Q(1,4),Q(1,12))
    high_k=one_step_mass6(j,Q(3,4),Q(11,12))
    low_flipped=one_step_mass6(6-j,Q(1,4),Q(1,12))
    for m in range(7):
        assert high_k[m]==low_k[6-m]==low_flipped[m]
print('N=6 exact flip-line parity conjugacy: PASS')
print('ALL CHECKS PASS')
