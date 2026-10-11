#!/usr/bin/env python3
import cmath, math
from fractions import Fraction


def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d==0: return False
        d += 2
    return True

def primitive_root(p):
    phi=p-1; q=phi; fac=[]; d=2
    while d*d<=q:
        if q%d==0:
            fac.append(d)
            while q%d==0: q//=d
        d += 1
    if q>1: fac.append(q)
    for g in range(2,p):
        if all(pow(g,phi//r,p)!=1 for r in fac): return g
    raise RuntimeError

def find_LM(p):
    lim=int(math.isqrt(4*p))
    sols=[]
    for L in range(-lim,lim+1):
        if L % 3 != 1: continue
        t=4*p-L*L
        if t<0 or t%27: continue
        q=t//27; M=math.isqrt(q)
        if M*M==q: sols.append((L,M))
    if len(sols)!=1:
        raise AssertionError((p,sols))
    return sols[0]

def theorem_norm(p,L):
    theta=math.acos(L/(2*math.sqrt(p)))/3
    if L >= -2:
        return 4*(p-1)/(9*p)*(1+math.sqrt(p)*math.cos(theta))
    return 2*(p-1)/(9*p)*(1-2*math.sqrt(p)*math.cos(theta+2*math.pi/3))

def direct_data(p):
    k=(p-1)//3
    H=sorted({pow(a,3,p) for a in range(1,p)})
    assert len(H)==k
    g=primitive_root(p)
    zeta=cmath.exp(2j*math.pi/p)
    periods=[]
    for j in range(3):
        C={(pow(g,j,p)*h)%p for h in H}
        periods.append(sum(zeta**x for x in C).real)
    # all periods real because -1 is a cube for p=1 mod 6
    imax=max(abs(sum((zeta**(x*h)) for h in H).imag) for x in range(1,p))
    kernel=[sum(zeta**(x*h) for h in H) for x in range(p)]
    direct=sum(abs(v) for v in kernel)/p
    return periods,direct,imax

count=0; max_norm_err=0.0; max_poly_res=0.0; max_imag=0.0
branches={"one_positive":0,"one_negative":0}
for p in range(7,1001):
    if not is_prime(p) or p%3!=1: continue
    count += 1
    L,M=find_LM(p)
    periods,direct,imax=direct_data(p)
    max_imag=max(max_imag,imax)
    e1=sum(periods)
    e2=sum(periods[i]*periods[j] for i in range(3) for j in range(i+1,3))
    e3=periods[0]*periods[1]*periods[2]
    max_poly_res=max(max_poly_res,abs(e1+1),abs(e2+(p-1)/3),abs(e3-(p*(L+3)-1)/27))
    pred=theorem_norm(p,L)
    max_norm_err=max(max_norm_err,abs(direct-pred))
    signs=sum(x>1e-9 for x in periods)
    if L>=-2:
        assert signs==1, (p,L,periods)
        branches['one_positive'] += 1
    else:
        assert signs==2, (p,L,periods)
        branches['one_negative'] += 1
    assert abs(direct-pred)<2e-11, (p,L,direct,pred)
    # Check root formula as an unordered set.
    th=math.acos(L/(2*math.sqrt(p)))/3
    roots=sorted([-1/3+2*math.sqrt(p)/3*math.cos(th+2*math.pi*j/3) for j in range(3)])
    assert max(abs(a-b) for a,b in zip(sorted(periods),roots)) < 2e-11
print('VERIFY_OK primes=%d one_positive=%d one_negative=%d max_norm_err=%.3e max_poly_res=%.3e max_imag=%.3e' %
      (count,branches['one_positive'],branches['one_negative'],max_norm_err,max_poly_res,max_imag))
