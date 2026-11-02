from fractions import Fraction
from functools import lru_cache
from math import comb

def analytic(parts,p):
    N=sum(parts);q=1-p
    full=Fraction(0);side=[]
    for a in parts:
        z=N-a
        if z==0: raise ValueError('Need at least 2 parts')
        fa=sum(Fraction(comb(a-1,j))*p**(a-1-j)*q**j*Fraction(z)*p/(z*p+j) for j in range(a))
        fb=sum(Fraction(comb(a-1,j))*q**(a-1-j)*p**j*Fraction(z)*q/(z*q+j) for j in range(a))
        w=Fraction(a,N)*(p*(1-fa)+q*(1-fb))
        side.append(w)
        full+=Fraction(a,N)*(p*fa+q*fb)
    return full,side

def dp(parts,p):
    N=sum(parts);q=1-p;k=len(parts)
    @lru_cache(None)
    def solve(state):
        naccept=sum(state)
        rates=[]
        for i,a in enumerate(parts):
            ai=state[2*i];bi=state[2*i+1]
            vac=a-ai-bi
            if not vac:continue
            outer_a=sum(state[2*j] for j in range(k) if j!=i)
            outer_b=sum(state[2*j+1] for j in range(k) if j!=i)
            if outer_b==0: rates.append((i,0,p*vac))
            if outer_a==0: rates.append((i,1,q*vac))
        total=sum((rate for _,_,rate in rates),Fraction(0))
        if not total:return {naccept:Fraction(1)}
        out={}
        for i,c,rate in rates:
            nxt=list(state);nxt[2*i+c]+=1
            for n,v in solve(tuple(nxt)).items():out[n]=out.get(n,Fraction(0))+rate/total*v
        return out
    return solve((0,)*(2*k))

def partitions(n, maximum=None):
    if n==0:
        yield ()
        return
    top = min(n,maximum if maximum is not None else n)
    for a in range(top,0,-1):
        for rest in partitions(n-a,a):
            yield (a,)+rest

def verify():
    count=0;cases=0
    for n in range(2,9):
        for parts in partitions(n):
            if len(parts)<2: continue
            for p in (Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(3,4)):
                cases+=1
                full,side=analytic(parts,p)
                assert full+sum(side)==1
                count+=1
                target={n:full}
                for a,w in zip(parts,side):
                    if w: target[a]=target.get(a,Fraction(0))+w
                actual=dp(parts,p)
                assert actual==target, (parts,p,actual,target)
                count+=1
                assert all(t in (n,*parts) for t in actual)
                count+=1
    for n in range(1,151):
        f=sum(Fraction(comb(n-1,j),2**(n-1))*Fraction(n,n+2*j) for j in range(n))
        g,_=analytic((n,n),Fraction(1,2))
        assert f==g
        count+=1
        if n>1:
            assert f>Fraction(1,2)
            count+=1
    print(f'PASS: {cases} exact Markov-chain distributions, {count} assertions; n=1..150 binomial identities')

if __name__=='__main__': verify()
