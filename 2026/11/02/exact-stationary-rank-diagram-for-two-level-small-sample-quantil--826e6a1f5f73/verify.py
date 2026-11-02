"""Exact independent checks for a two-valued order-statistic Kaczmarz model.

Run with Python >=3.9; no external packages required.
All tests use exact rational arithmetic and enumerate row subsets directly.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def weights(clean, corrupt, batch, replacement=False):
    total = clean + corrupt
    if replacement:
        return [Fraction(comb(batch, k) * corrupt**k * clean**(batch-k), total**batch)
                for k in range(batch+1)]
    return [Fraction(binom(corrupt,k)*binom(clean,batch-k),comb(total,batch))
            for k in range(batch+1)]


def probabilities(w, rank):
    batch = len(w)-1
    a = sum(w[batch-rank+1:], Fraction())
    b = sum(w[:rank], Fraction())
    assert b > 0
    return a, b


def stationary(w, rank):
    a, b = probabilities(w,rank)
    return a/(a+b)


def direct_without_replacement(clean,corrupt,batch,rank):
    total=clean+corrupt
    x0_corrupt=x1_clean=0
    for rows in combinations(range(total), batch):
        k=sum(i >= clean for i in rows)
        # At x=0, clean residuals precede corrupt residuals.
        ordered_at_zero=sorted(rows,key=lambda i: (i >= clean,i))
        # At x=C, corrupt residuals precede clean residuals.
        ordered_at_c=sorted(rows,key=lambda i: (i < clean,i))
        x0_corrupt += ordered_at_zero[rank-1]>=clean
        x1_clean += ordered_at_c[rank-1]<clean
    denom=comb(total,batch)
    return Fraction(x0_corrupt,denom),Fraction(x1_clean,denom)


def check():
    checks=0
    for total in range(3,11):
        for corrupt in range(1,(total-1)//2+1):
            clean=total-corrupt
            if not clean>corrupt:continue
            for batch in range(1,clean+1):
                w=weights(clean,corrupt,batch)
                assert sum(w)==1
                checks += 1
                pi=[]
                for rank in range(1,batch+1):
                    a,b=probabilities(w,rank)
                    da,db=direct_without_replacement(clean,corrupt,batch,rank)
                    assert (a,b)==(da,db),(total,corrupt,batch,rank,a,b,da,db)
                    checks+=2
                    lam=1-a-b
                    if 2*rank<=batch:
                        assert lam==sum(w[rank:batch-rank+1],Fraction())
                    elif 2*rank==batch+1:
                        assert lam==0 and b==1-a
                    else:
                        assert lam==-sum(w[batch-rank+1:rank],Fraction())
                    checks+=1
                    pi.append(stationary(w,rank))
                    if batch%2 and rank==(batch+1)//2:
                        assert pi[-1]==a
                        checks+=1
                if batch<=corrupt:
                    assert all(pi[i]<pi[i+1] for i in range(batch-1))
                    assert pi[0]==Fraction(comb(corrupt,batch),comb(corrupt,batch)+comb(clean,batch))
                    checks+=2
                else:
                    assert all(pi[i]==0 for i in range(batch-corrupt))
                    assert all(pi[i]>0 for i in range(batch-corrupt,batch))
                    checks+=2
                for rank in range(1,batch+1):
                    aw,bw=probabilities(w,rank)
                    # Verify explicit k-step transition probabilities from state 0.
                    p=Fraction(0)
                    for _ in range(7):
                        p=(1-p)*aw+p*(1-bw)
                    expected=aw/(aw+bw)*(1-(1-aw-bw)**7)
                    assert p==expected
                    checks+=1
                # Compare all positive-probability binomial replacement laws.
                wrep=weights(clean,corrupt,batch,replacement=True)
                prep=[stationary(wrep,j) for j in range(1,batch+1)]
                assert all(prep[i]<prep[i+1] for i in range(batch-1))
                assert prep[0]==Fraction(corrupt**batch,corrupt**batch+clean**batch)
                checks+=2
    # Exact illustrative example: 6 clean, 3 corrupted rows.
    w3=weights(6,3,3)
    assert stationary(w3,1)==Fraction(1,21)
    assert stationary(w3,2)==Fraction(19,84)
    w4=weights(6,3,4)
    assert stationary(w4,1)==0
    assert Fraction(1,probabilities(w4,1)[1])==Fraction(42,5)
    checks+=4
    return checks

if __name__=='__main__':
    n=check()
    print(f'PASS: {n} exact rational identities and enumerated row-selection checks')
