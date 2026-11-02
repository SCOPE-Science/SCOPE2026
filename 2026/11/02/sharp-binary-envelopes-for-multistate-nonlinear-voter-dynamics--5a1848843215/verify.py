"""Finite-state reproducibility checks for the multistate nonlinear voter comparison."""
from fractions import Fraction
from itertools import product
from math import comb, sqrt
from functools import lru_cache
import numpy as np
from scipy.linalg import expm


def states(n, m):
    if m == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for rem in states(n-a, m-1):
                yield (a,) + rem


def generator(n, m, q):
    ss = list(states(n, m))
    ix = {s:i for i,s in enumerate(ss)}
    Q = np.zeros((len(ss), len(ss)))
    for k, s in enumerate(ss):
        for b in range(m):
            for a in range(m):
                if a == b or not s[b] or not s[a]:
                    continue
                z = list(s); z[b]-=1; z[a]+=1
                rate=s[b]*(s[a]/(n-1))**q
                Q[k,ix[tuple(z)]]+=rate
                Q[k,k]-=rate
    return ss, Q


def exact_binary_h(n,a,q):
    vals=np.array([comb(n-1,r)**(q-1) for r in range(n)],dtype=float)
    return sum(vals[:a])/sum(vals)


def absorbing_prob(ss,Q,focus=0):
    good=np.array([s[focus]==sum(s) for s in ss]); bad=np.array([sum(x>0 for x in s)==1 for s in ss]) & ~good
    transient=~(good|bad)
    h=np.zeros(len(ss)); h[good]=1
    h[transient]=np.linalg.solve(Q[np.ix_(transient,transient)],-Q[np.ix_(transient,good)].sum(axis=1))
    return h


def run():
    fixation=0; finite_time=0; strict=0
    for q in (0.5,1.0,2.0,3.0):
        for n in range(3,9):
            for m in (3,4):
                ss,Q=generator(n,m,q)
                h=absorbing_prob(ss,Q)
                for k,s in enumerate(ss):
                    a=s[0]
                    b=exact_binary_h(n,a,q)
                    tol=1.5e-9
                    assert -tol<=h[k]<=1+tol,(q,n,m,s,h[k])
                    if q>1: assert h[k]>=b-tol,(q,n,m,s,h[k],b)
                    if q<1: assert h[k]<=b+tol,(q,n,m,s,h[k],b)
                    if q==1: assert abs(h[k]-a/n)<tol,(q,n,m,s,h[k])
                    if q!=1 and a>0 and sum(x>0 for x in s[1:])>=2:
                        assert abs(h[k]-b)>1e-9,('strict',q,n,m,s,h[k],b)
                        strict+=1
                    fixation+=1
                # Compare binary distribution upper-tail at finite horizons.
                if n<=6:
                    sb,Qb=generator(n,2,q)
                    for t in (0.1,0.6,1.5):
                        P=expm(Q*t); Pb=expm(Qb*t)
                        for k,s in enumerate(ss):
                            a=s[0]
                            ib=sb.index((a,n-a))
                            for cutoff in range(n+1):
                                p=sum(P[k,j] for j,z in enumerate(ss) if z[0]>=cutoff)
                                b=sum(Pb[ib,j] for j,z in enumerate(sb) if z[0]>=cutoff)
                                if q>1: assert p>=b-4e-10,(q,n,m,s,cutoff,p,b)
                                if q<1: assert p<=b+4e-10,(q,n,m,s,cutoff,p,b)
                                if q==1: assert abs(p-b)<4e-10,(q,n,m,s,cutoff,p,b)
                                finite_time+=1
    print('fixation_states_checked=',fixation)
    print('strict_fixation_cases_checked=',strict)
    print('finite_time_tail_compared=',finite_time)
    n=4
    for q in (0.5,2.0):
        ss,Q=generator(n,4,q); h=absorbing_prob(ss,Q)
        actual=h[ss.index((1,1,1,1))]
        binary=exact_binary_h(n,1,q)
        assert abs(actual-0.25)<1e-11
        print(f'four_singleton_opinions_q={q} multistate={actual:.12f} binary={binary:.12f}')

if __name__=='__main__':run()

# This separate exact calculation deliberately runs only for small finite systems.
def exact_rational_checks():
    import sympy as sp
    total=0
    for n in (3,4,5):
        for m in (3,4):
            ss=list(states(n,m)); ix={s:i for i,s in enumerate(ss)}
            mat=sp.zeros(len(ss))
            for k,s in enumerate(ss):
                for old in range(m):
                    for new in range(m):
                        if old==new or s[old]==0 or s[new]==0:continue
                        z=list(s);z[old]-=1;z[new]+=1
                        rate=sp.Rational(s[old]*s[new]**2,(n-1)**2)
                        mat[k,ix[tuple(z)]]+=rate
                        mat[k,k]-=rate
            transient=[k for k,s in enumerate(ss) if sum(x>0 for x in s)>1]
            good=[k for k,s in enumerate(ss) if s[0]==n]
            sol=mat.extract(transient,transient).inv()*(-mat.extract(transient,good)*sp.ones(len(good),1))
            for k,s in enumerate(ss):
                if k in transient: v=sol[transient.index(k)]
                else: v=sp.Integer(int(s[0]==n))
                a=s[0]
                h=sp.Rational(sum(comb(n-1,r) for r in range(a)),2**(n-1))
                assert v>=h,(n,m,s,v,h)
                if 0<a<n and sum(x>0 for x in s[1:])>=2: assert v>h
                total+=1
    print('exact_rational_q2_states_checked=',total)

if __name__=='__main__':exact_rational_checks()
