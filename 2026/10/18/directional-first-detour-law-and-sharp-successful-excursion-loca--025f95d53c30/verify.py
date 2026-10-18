"""Independent finite combinatorial checks for the first-arrival excursion theorem.

Run: python3 verify.py. Only Python standard library is needed.
The infinite-r and infinite-d claims are proved in RESULT.md, not by these tests.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, exp, sqrt

checks = 0

def check(condition, explanation):
    global checks
    assert condition, explanation
    checks += 1

def first_hit_counts(start, steps):
    """Count exactly all trajectories that first hit 0 on each step."""
    d = len(start)
    alive = {tuple(start): 1}
    hit = {}
    for n in range(1, steps+1):
        new = defaultdict(int)
        for site, mass in alive.items():
            for j in range(d):
                for s in (-1, 1):
                    v = list(site)
                    v[j] += s
                    new[tuple(v)] += mass
        hit[n] = new.pop((0,)*d, 0)
        alive = new
    return hit

def marked_first_hit_counts(start, steps):
    """Independently track per-coordinate hop counts (not using any path formula)."""
    d=len(start)
    alive={(tuple(start),(0,)*d):1}
    marked=defaultdict(int)
    for n in range(1,steps+1):
        nxt=defaultdict(int)
        for (site,used),mass in alive.items():
            for j in range(d):
                for direction in (-1,1):
                    dest=list(site)
                    dest[j]+=direction
                    use=list(used)
                    use[j]+=1
                    if all(v==0 for v in dest):
                        if n==steps:
                            excess=[k for k in range(d) if use[k]==abs(start[k])+2]
                            assert len(excess)==1
                            marked[excess[0]]+=mass
                    else:
                        nxt[(tuple(dest),tuple(use))]+=mass
        alive=nxt
    return [marked[j] for j in range(d)]

def predicted_counts(start):
    L = sum(abs(x) for x in start)
    K = factorial(L)
    den = 1
    for x in start:
        den *= factorial(abs(x))
    K //= den
    C = [Fraction((L+2)*(L+1), abs(x)+1)-2 for x in start]
    return L,K,[K*e for e in C]

# All nonzero sites in moderate finite boxes: independently enumerated finite first hits.
for d in (1,2,3):
    bound = 3 if d==1 else 2 if d==2 else 1
    for site in product(range(-bound,bound+1),repeat=d):
        if not any(site):
            continue
        L,K,per_coordinate = predicted_counts(site)
        got = first_hit_counts(site,L+2)
        check(got[L] == K, (site,'shortest paths',got[L],K))
        check(got[L+2] == sum(per_coordinate), (site,'one detour',got[L+2],sum(per_coordinate)))
        check(all(v>=0 and v.denominator==1 for v in per_coordinate), (site,'integrality'))
        marks=marked_first_hit_counts(site,L+2)
        check(all(a==b for a,b in zip(marks,per_coordinate)),(site,'directional marks',marks,per_coordinate))
        check(all((n-L)%2 or not got[n] for n in got if n<L), (site,'parity'))

# An independent generating-function computation.  Coefficient of t^n of
# I_0(2t)^d or I_2(2t) I_0(2t)^(d-1), times n!, counts unrestricted walks.
def convolve(a,b,kmax):
    out=[Fraction(0) for _ in range(kmax+1)]
    for i,u in enumerate(a):
        if not u:continue
        for j,v in enumerate(b[:kmax+1-i]):
            out[i+j]+=u*v
    return out

def ordinary_green_coefficients(d,max_degree):
    z=Fraction(0)
    b0=[z]*(max_degree+1)
    b2=[z]*(max_degree+1)
    for k in range(max_degree//2+1):
        b0[2*k]=Fraction(1,factorial(k)**2)
        if 2+2*k<=max_degree:
            b2[2+2*k]=Fraction(1,factorial(k)*factorial(k+2))
    g0=[Fraction(1)]+[z]*max_degree
    for _ in range(d-1):g0=convolve(g0,b0,max_degree)
    g2=convolve(g0,b2,max_degree)
    g0=convolve(g0,b0,max_degree)
    return [v*factorial(i) for i,v in enumerate(g0)],[v*factorial(i) for i,v in enumerate(g2)]

for d in (1,2,3,4,8,15,40,100):
    A0,A2=ordinary_green_coefficients(d,12)
    check(A0[0]==1,(d,'Green constant'))
    check(A2[2]==1,(d,'Green n2'))
    check(A2[4]==12*d-8,(d,'unrestricted n4'))
    # Renewal division: all walks from 2e_1 to 0 = first-hit * all-return-to-0.
    F=[0]*len(A0)
    for n in range(2,len(A0)):
        F[n]=A2[n]-sum(F[j]*A0[n-j] for j in range(2,n))
    check(F[2]==1,(d,'first hit n2'))
    check(F[4]==10*d-8,(d,'first hit n4'))
    check(all(F[n]>=0 and F[n].denominator==1 for n in range(2,len(F))),(d,'first-hit coefficients'))
    # q=1/(4d): route-probability expansion, including high-d coefficient.
    q=Fraction(1,4*d)
    pf=sum(F[n]*q**n for n in range(len(F)))
    rare=1-q*q/pf
    leading=Fraction(10*d-8,1)*q*q
    check(rare>=leading/(1+leading),(d,'non-geodesic lower bound'))
    if d>=40:
        check(abs(float(d*rare)-0.625)<0.1,(d,'large-d coefficient'))

# Exact gamma-TV shape difference, independent CDF identity.
for L in range(1,12):
    t=sqrt(L*(L+1))
    delta=exp(-t)*(t**L/factorial(L)+t**(L+1)/factorial(L+1))
    check(0<delta<1,(L,'TV coefficient'))
    # Gamma(L+2) - Gamma(L) densities cross once at t, so CDF diff is delta.
    left=exp(-t)*sum(t**j/factorial(j) for j in range(L,L+2))
    check(abs(left-delta)<1e-12,(L,'gamma crossing identity'))

print(f'PASS: {checks} independent finite exact/comparison checks')
