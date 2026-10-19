#!/usr/bin/env python3
"""Exact enumerative checks for covariance spectra of overlapping categorical pair counts."""
from fractions import Fraction
from itertools import product


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def calc(q,n,probs,cyclic):
    assert len(probs)==q and sum(probs)==1 and all(v>0 for v in probs)
    assert n>= (3 if cyclic else 2)
    m=n if cyclic else n-1
    d=q*q
    E=[Fraction(0)]*d
    E2=[[Fraction(0)]*d for _ in range(d)]
    for seq in product(range(q),repeat=n):
        prob=Fraction(1)
        for x in seq: prob*=probs[x]
        counts=[0]*d
        for i in range(m):
            j=(i+1)%n
            counts[q*seq[i]+seq[j]]+=1
        for a in range(d):
            E[a]+=prob*counts[a]
            for b in range(d): E2[a][b]+=prob*counts[a]*counts[b]
    Sigma=[[E2[i][j]-E[i]*E[j] for j in range(d)] for i in range(d)]
    expected=[[Fraction(m)*probs[a]*probs[b] for b in range(q)] for a in range(q)]
    assert E==[v for row in expected for v in row]
    for i in range(d):
        a,b=divmod(i,q)
        for j in range(d):
            c,e=divmod(j,q)
            want=m*(probs[a]*probs[b]*int(i==j)-probs[a]*probs[b]*probs[c]*probs[e])
            adjacent=(m if cyclic else m-1)
            want+=adjacent*(probs[a]*probs[b]*probs[e]*int(b==c)
                             +probs[c]*probs[e]*probs[b]*int(e==a)
                             -2*probs[a]*probs[b]*probs[c]*probs[e])
            assert Sigma[i][j]==want,(q,n,cyclic,i,j,Sigma[i][j],want)
    assert sum(Sigma[i][i]/(probs[i//q]*probs[i%q]) for i in range(d))==m*(q*q-1)
    # Convenient expression for covariance quadratic form, with test functions u,v on alphabet.
    for u0 in product(range(-1,2),repeat=q):
        u=[Fraction(x) for x in u0]
        bar=sum(probs[i]*u[i] for i in range(q))
        u=[x-bar for x in u]
        for which in ('sym','anti'):
            f=[u[a]+u[b] if which=='sym' else u[a]-u[b]
               for a in range(q) for b in range(q)]
            for i in range(d):
                # Σ acting on f: lambda * D*f, where D_{ab}=p_a p_b
                actual=sum(Sigma[i][j]*f[j] for j in range(d))
                a,b=divmod(i,q)
                lam = (2*m if cyclic else 2*m-1) if which=='sym' else (0 if cyclic else 1)
                want=Fraction(lam)*probs[a]*probs[b]*f[i]
                assert actual==want,(q,n,cyclic,which,u0,i,actual,want)
    # All row/column centered interaction basis = (delta_{a=i}/p_i-delta_{a=q-1}/p_last)*same for b.
    for a in range(q-1):
      for b in range(q-1):
        ua=[Fraction(1,1)/probs[a] if c==a else -Fraction(1,1)/probs[-1] if c==q-1 else Fraction(0) for c in range(q)]
        vb=[Fraction(1,1)/probs[b] if c==b else -Fraction(1,1)/probs[-1] if c==q-1 else Fraction(0) for c in range(q)]
        f=[ua[i]*vb[j] for i in range(q) for j in range(q)]
        for i in range(d):
            z=sum(Sigma[i][j]*f[j] for j in range(d))
            x,y=divmod(i,q)
            want=Fraction(m)*probs[x]*probs[y]*f[i]
            assert z==want,(q,n,cyclic,a,b,i,z,want)
    # Constant-eigenvector null: every sample has m transitions.
    assert all(sum(row)==0 for row in Sigma)
    return m,d


def main():
    cases=[]
    for q, probs in [(2,[Fraction(1,3),Fraction(2,3)]),(3,[Fraction(1,2),Fraction(1,3),Fraction(1,6)]),(4,[Fraction(1,10),Fraction(2,10),Fraction(3,10),Fraction(4,10)])]:
        for n in range(2,7 if q==2 else 7 if q==3 else 6):
            for cyclic in (False,True):
                if cyclic and n<3: continue
                cases.append(calc(q,n,probs,cyclic))
    print(f'PASS {len(cases)} exhaustively enumerated laws with q in {{2,3,4}}, n in {{2,...,6}}, exact rational nonuniform probabilities, path/cycle configurations.')

if __name__ == '__main__': main()
