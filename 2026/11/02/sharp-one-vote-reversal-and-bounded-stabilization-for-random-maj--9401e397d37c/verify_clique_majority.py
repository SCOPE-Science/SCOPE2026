"""Exact independent state-count Markov verification for synchronous fair-tie majority on cliques.
Each complete graph state with k blue nodes is aggregated by exchangeability.
The Markov linear system is solved with exact rational arithmetic (SymPy).
"""
from math import comb
from fractions import Fraction
import sympy as s

def distribution(n,k):
    d={}
    if 2*k>=n+2: return {n:Fraction(1)}
    if 2*k<=n-2: return {0:Fraction(1)}
    if n%2==0: return {n-k:Fraction(1)}  # k=n/2, complement on all vertices
    r=(n-1)//2
    if k==r+1: # old whites become blue; old blues independently flip fair coin
        return {r+j:Fraction(comb(r+1,j),2**(r+1)) for j in range(r+2)}
    if k==r:   # old blues become white; old whites independently flip fair coin
        return {j:Fraction(comb(r+1,j),2**(r+1)) for j in range(r+2)}
    raise ValueError((n,k))

def formulas(n,k):
    if n%2==0:
        r=n//2
        if k==r: return Fraction(0),Fraction(0),Fraction(1)
        if k==0: return Fraction(0),Fraction(0),Fraction(0)
        if k==n: return Fraction(0),Fraction(1),Fraction(0)
        return Fraction(1),Fraction(int(k>r)),Fraction(0)
    r=(n-1)//2
    if k==0:return Fraction(0),Fraction(0),Fraction(0)
    if k==n:return Fraction(0),Fraction(1),Fraction(0)
    a=Fraction(1,2**(r+1));b=Fraction(r+1,2**(r+1))
    e=(2-b-2*a)/(1-a-b)
    reversal=Fraction(1,2**(r+1)-r)
    if k==r:return e,reversal,Fraction(0)
    if k==r+1:return e,1-reversal,Fraction(0)
    return Fraction(1),Fraction(int(k>r)),Fraction(0)

def verify(n):
    absorbing={0,n} | ({n//2} if n%2==0 else set())
    trans=[distribution(n,k) if k not in absorbing else {k:Fraction(1)} for k in range(n+1)]
    for k in absorbing:
        assert distribution(n,k)=={k:Fraction(1)}, (n,k,distribution(n,k))
    unknown=[k for k in range(n+1) if k not in absorbing]
    idx={k:i for i,k in enumerate(unknown)}
    m=len(unknown);M=s.eye(m);rhs=s.zeros(m,2)
    for k in unknown:
        i=idx[k];rhs[i,0]=1
        for j,p in trans[k].items():
            rat=s.Rational(p.numerator,p.denominator)
            if j in idx:M[i,idx[j]]-=rat
            else:rhs[i,1]+=rat*int(j==n)
    ans=M.inv()*rhs if m else s.zeros(0,2)
    for k in range(n+1):
        E,PB,Pblink=formulas(n,k)
        if k in absorbing:
            ex=(s.Integer(0),s.Integer(int(k==n)))
        else:ex=tuple(ans[idx[k],j] for j in range(2))
        assert ex==(s.Rational(E.numerator,E.denominator),s.Rational(PB.numerator,PB.denominator)),(n,k,ex,(E,PB))
        assert 0<=PB<=1 and 0<=Pblink<=1
        assert sum(trans[k].values())==1
    return len(unknown)

if __name__=='__main__':
    tests=0;tr=0
    for n in range(2,41):
        tr+=verify(n);tests+=n+1
    print(f'PASS: {tests} exact n,k-state outcome/time comparisons on K_n for 2<=n<=40; {tr} transient-state equations.')
    for n in [3,5,7,9,11,13,21,41]:
        r=(n-1)//2
        E,P,_=formulas(n,r+1)
        print(f'K_{n}: one-vote lead reversal={1-P}; expected absorption rounds={E}')
