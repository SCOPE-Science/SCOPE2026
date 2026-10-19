"""Exact finite-electorate checks and numerical asymptotics for three-candidate Thiele ties."""
from fractions import Fraction
from itertools import product
from math import comb, sqrt, pi, lgamma, exp
from collections import defaultdict

B=list(product(range(2),repeat=3))

def score_pairs(v,a,b):
    def w(s): return 0 if s==0 else (b if s==1 else b+a)
    x,y,z=v
    return tuple(w(s) for s in (x+y,x+z,y+z))

def exact_prob_n(n,a,b):
    # Integer-valued score differences (S_AB-S_AC,S_AB-S_BC), with all 8 votes equiprobable.
    inc=defaultdict(int)
    for vote in B:
        ab,ac,bc=score_pairs(vote,a,b)
        inc[(ab-ac,ab-bc)]+=1
    states={(0,0):1}
    for _ in range(n):
        next_states=defaultdict(int)
        for (d,e),count in states.items():
            for (u,v),mult in inc.items():
                next_states[(d+u,e+v)]+=count*mult
        states=next_states
    tie=sum(count for (d,e),count in states.items() if d==0 and e>=0)
    # Three equal maximal committee scores counted thrice above; any tie has 3 choices by symmetry.
    all3=states.get((0,0),0)
    return Fraction(3*tie-2*all3,8**n),Fraction(all3,8**n)

def irr_exact(n):
    # Score S=number of voters with 1 approved + alpha * number with 2 approved,
    # so differences are integer pairs. Small n via exact four-coordinate states.
    inc=defaultdict(int)
    for vote in B:
        x,y,z=vote
        def s(u,v):return (int(u+v>=1),int(u+v==2))
        ab,ac,bc=s(x,y),s(x,z),s(y,z)
        inc[(*[i-j for i,j in zip(ab,ac)],*[i-j for i,j in zip(ab,bc)])]+=1
    states={(0,0,0,0):1}
    for i in range(n):
        next_states=defaultdict(int)
        for k,num in states.items():
            for u,v in inc.items():
                next_states[tuple(c+d for c,d in zip(k,u))]+=num*v
        states=next_states
    tie=0;triple=0
    t=sqrt(2)-1
    for (d0,d1,e0,e1),count in states.items():
        if d0==0 and d1==0 and e0+t*e1>=-1e-13:
            tie+=count
        if d0==d1==e0==e1==0:triple+=count
    return Fraction(3*tie-2*triple,8**n),Fraction(triple,8**n),len(states)

def exact_pair_rational(n,a,b):
    # 1d random walk D, per ballot probs: 0:1/2, plus/minus a,b:1/8 each
    ker=defaultdict(float);ker[0]+=.5
    for step in (a,b):
        ker[step]+=.125;ker[-step]+=.125
    states={0:1.0}
    for _ in range(n):
        nxt=defaultdict(float)
        for pos,p in states.items():
            for jump,v in ker.items():nxt[pos+jump]+=p*v
        states=nxt
    return states.get(0,0)

def exact_pair_irr(n):
    # P(U0=U1=0)=E[q_K*q_(n-K)], K~Bin(n,1/2), q_k=C(2k,k)/4^k.
    sm=0.0
    for k in range(n+1):
        lp=(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)-n*__import__('math').log(2))
        q0=exp(lgamma(2*k+1)-2*lgamma(k+1)-k*__import__('math').log(4))
        l=n-k
        q1=exp(lgamma(2*l+1)-2*lgamma(l+1)-l*__import__('math').log(4))
        sm+=exp(lp)*q0*q1
    return sm

def exhaustive_direct(n,a,b,irrational=False):
    # Independent ballot-tuple enumeration; compare complete committee scores directly.
    t=sqrt(2)-1 if irrational else a/b
    wins=0
    for profile in product(B, repeat=n):
        scores=[0.0,0.0,0.0]
        for x,y,z in profile:
            for j,k in enumerate((x+y,x+z,y+z)):
                scores[j]+=(0.0 if k==0 else 1.0 if k==1 else 1.0+t)
        hi=max(scores)
        wins += sum(abs(x-hi)<1e-10 for x in scores)>1
    return Fraction(wins,8**n)

if __name__=='__main__':
    for n in range(1,9):
        x,y=exact_prob_n(n,1,2)
        assert 0<=x<=1
        assert x>=y
        if n<=4:assert x==exhaustive_direct(n,1,2)
        print('rational n',n,'tie',x,'triple',y)
    for n in range(1,8):
        x,y,num=irr_exact(n)
        assert 0<=x<=1
        assert x>=y
        if n<=4:assert x==exhaustive_direct(n,0,1,irrational=True)
        print('irrational n',n,'tie',x,'triple',y,'states',num)
    for a,b in ((0,1),(1,2),(1,1),(2,3)):
        const=3/sqrt(2*pi*(a*a+b*b))
        print('rational',a,b,'predicted tie sqrt(n) limit',const)
        for n in (100,400,1000):
            approx=1.5*exact_pair_rational(n,a,b)
            print(' n',n,'pair-approx sqrt(n)',approx*sqrt(n))
    print('irrational predicted n*tie',3/pi)
    for n in (100,400,1000):
        approx=1.5*exact_pair_irr(n)
        print(' n',n,'pair-approx*n',approx*n)
    print('ALL CHECKS PASSED')
