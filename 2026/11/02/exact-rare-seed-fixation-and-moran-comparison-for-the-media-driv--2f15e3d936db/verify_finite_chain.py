"""Exact finite-chain verification of a media-driven nonlinear voter process."""
from fractions import Fraction
from itertools import combinations
from math import comb, prod

def fall(a,b):
    return prod(range(a-b+1,a+1)) if a>=b else 0

def rates(N,q,p,k):
    T=fall(N-1,q)
    plus=Fraction(N-k,N)*Fraction(fall(k,q),T)
    mixed=Fraction(N-k,N)*p*Fraction(T-fall(k,q)-fall(N-k-1,q),T)
    minus=Fraction(k,N)*Fraction(fall(N-k,q),T)
    return plus+mixed,minus

def brute(N,q,p,k):
    s=[1]*k+[0]*(N-k)
    up=down=Fraction(0)
    for voter in range(N):
        others=[z for z in range(N) if z!=voter]
        for committee in combinations(others,q):
            v=[s[z] for z in committee]
            if all(v):
                new=1
                chg=Fraction(1)
            elif not any(v):
                new=0
                chg=Fraction(1)
            else:
                new=1
                chg=p
            if new!=s[voter]:
                if new: up+=chg
                else: down+=chg
    return up/(N*comb(N-1,q)),down/(N*comb(N-1,q))

def fixation(N,q,p,m):
    assert p>0
    weights=[Fraction(1)]
    for k in range(1,N):
        u,d=rates(N,q,p,k)
        assert u>0
        weights.append(weights[-1]*d/u)
    return sum(weights[:m],Fraction(0))/sum(weights,Fraction(0))

def test():
    c=0
    for q in range(2,7):
        for N in range(q+1,min(q+6,11)):
            for p in [Fraction(1,7), Fraction(2,5), Fraction(1,1)]:
                for k in range(1,N):
                    u,d=rates(N,q,p,k)
                    assert (u,d)==brute(N,q,p,k),(N,q,p,k,u,d,brute(N,q,p,k))
                    assert u >= p*q*d
                    if k==1: assert u==p*q*d
                    c+=1
    print('EXACT_MICROSTATE_CHECKS',c)
    for q,p in [(2,Fraction(3,4)), (3,Fraction(1,2)),(5,Fraction(2,5)),(5,Fraction(1,5)),(5,Fraction(3,20)),(7,Fraction(3,10))]:
        m=2
        print('q',q,'p',str(p),'target', (1-Fraction(1,p*q)**m if p*q>1 else 0))
        for N in [q+2, 40, 200, 800]:
            if N<=q:continue
            x=fixation(N,q,p,m)
            print(' ',N,'fixation m=2',f'{float(x):.9f}')
            if p*q>1:
                z=Fraction(p*q-1,p*q)
                B=(1-Fraction(1,p*q)**m)/(1-Fraction(1,p*q)**N)
                assert x>=B
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':test()
