"""Exact finite-population nonlinear public-goods payoff checker.

Run: python verify.py
Uses only the Python standard library and rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def payoff_benefit(ell, delta, num_cooperators):
    return sum((delta**t for t in range(num_cooperators)), F(0))/ell


def direct_gap(N, j, ell, delta):
    """Average benefit difference, excluding common contribution cost."""
    peers_c=[1]*(j-1)+[0]*(N-j)
    peers_d=[1]*j+[0]*(N-1-j)
    s=ell-1
    total=comb(N-1,s)
    pc=sum((payoff_benefit(ell,delta,1+sum(peers_c[t] for t in S)) for S in combinations(range(N-1),s)),F(0))/total
    pd=sum((payoff_benefit(ell,delta,sum(peers_d[t] for t in S)) for S in combinations(range(N-1),s)),F(0))/total
    return pc-pd


def hypergeom_factor(M,K,s,delta):
    return sum((F(comb(K,k)*comb(M-K,s-k),comb(M,s))*delta**k
                for k in range(max(0,s-(M-K)), min(K,s)+1)),F(0))


def predicted_gap(N,j,ell,delta):
    if ell==N:return F(0)
    return F(N-ell,(N-1)*ell)*hypergeom_factor(N-2,j-1,ell-1,delta)


def predicted_second(N,j,ell,delta):
    if ell==N or ell==2:return F(0)
    M=N-2;s=ell-1;K=j-1
    return F(N-ell,(N-1)*ell)*F(s*(s-1),M*(M-1))*(delta-1)**2*hypergeom_factor(M-2,K,s-2,delta)


def main():
    count=0
    second_count=0
    for N in range(4,10):
        for ell in range(2,N+1):
            for delta in (F(1,4),F(1),F(3,2),F(3)):
                values=[]
                for j in range(1,N):
                    d=direct_gap(N,j,ell,delta)
                    p=predicted_gap(N,j,ell,delta)
                    assert d==p,(N,j,ell,delta,d,p)
                    count+=1
                    values.append(p)
                for j in range(1,N-2):
                    d2=values[j+1]-2*values[j]+values[j-1]
                    rhs=predicted_second(N,j,ell,delta)
                    assert d2==rhs,(N,j,ell,delta,d2,rhs)
                    assert d2>=0
                    second_count+=1
    N=4
    groups=[(2,F(3,4),F(1,10)),(3,F(1,4),F(3))]
    benefit=[sum((w*predicted_gap(N,j,ell,delta) for ell,w,delta in groups),F(0)) for j in range(1,N)]
    assert benefit==[F(5,18),F(53,240),F(11,40)],benefit
    r=F(4)
    gains=[r*v-1 for v in benefit]
    assert gains==[F(1,9),-F(7,60),F(1,10)]
    assert [1 if g>0 else -1 if g<0 else 0 for g in gains]==[1,-1,1]
    print('PASS: direct hypergeometric comparisons:',count)
    print('PASS: exact discrete convexity identities:',second_count)
    print('PASS: four-player sharpness, unscaled advantage:',[str(v) for v in benefit])
    print('PASS: four-player net advantages divided by c:',[str(v) for v in gains])

if __name__=='__main__':main()
