"""Exact finite checks for edge-conditioned descents of uniform perfect matchings."""
from fractions import Fraction
from collections import defaultdict

def matchings(available):
    if not available:
        yield ()
    else:
        a=available[0]
        for k in range(1,len(available)):
            b=available[k]
            for tail in matchings(available[1:k]+available[k+1:]):
                yield ((a,b),)+tail

def predicted_shift(N,a,b):
    assert N%2==0 and N>=6 and 1<=a<b<=N
    if a==1 and b==N:
        return Fraction(1)
    if a==1:
        return Fraction(0) if b==2 else Fraction(b-N//2-2,N-3)
    if b==N:
        return Fraction(0) if a==N-1 else Fraction(N//2-a-1,N-3)
    if b==a+1:
        return Fraction(N-2,2*(N-3))
    return Fraction(-1,N-3)

def exact_conditioned(N,a,b):
    baseline=Fraction(N-2,2*(N-3))
    out=Fraction(0)
    for j in range(1,N):
        if b==a+1 and j==a: p=1
        elif j==a:p=Fraction(b-3,N-3)
        elif j+1==a:p=Fraction(N-b,N-3)
        elif j==b:p=Fraction(a-1,N-3)
        elif j+1==b:p=Fraction(N-a-2,N-3)
        else:p=baseline
        out+=p
    return out-Fraction(N,2)

def main():
    tests=0
    for N in (6,8,10,12):
        T=0
        edge_sum=defaultdict(int)
        moments_s=moments_d=moment_sd=moments_ss=0
        for pairs in matchings(list(range(1,N+1))):
            T+=1
            pi=[0]*(N+1)
            for a,b in pairs:pi[a]=b;pi[b]=a
            d=sum(pi[j]>pi[j+1] for j in range(1,N))
            s=sum(b==a+1 for a,b in pairs)
            moments_s+=s; moments_d+=d;moment_sd+=s*d; moments_ss+=s*s
            for a,b in pairs:edge_sum[(a,b)]+=d
        assert Fraction(moments_d,T)==Fraction(N,2)
        assert Fraction(moments_s,T)==1
        assert Fraction(moments_ss,T)-1==Fraction(N-2,N-1)
        assert Fraction(moment_sd,T)-Fraction(N,2)==Fraction(N-2,2*(N-1))
        tests+=4
        for a in range(1,N):
            for b in range(a+1,N+1):
                pred=predicted_shift(N,a,b)
                cnd=exact_conditioned(N,a,b)
                obs=Fraction(edge_sum[(a,b)],T//(N-1))-Fraction(N,2)
                assert pred==cnd==obs,(N,a,b,pred,cnd,obs)
                tests+=1
        print(f'N={N}: {T} matchings, all {N*(N-1)//2} marked edges verified')
    for N in range(12,102,2):
        assert sum(predicted_shift(N,a,b) for a in range(1,N) for b in range(a+1,N+1))==0
        tests+=1
    print(f'PASS {tests} exact checks')

if __name__=='__main__':main()
