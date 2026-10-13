"""Exact independent verification of near-universal-vertex domination statements.
Requires only Python 3 standard library. Run: python3 verify.py
"""
from math import comb
from fractions import Fraction

def prediction(n,a,b,c):
    T=n-1
    def bc(q,j):
        return comb(q,j) if 0<=j<=q else 0
    # Entries indexed by TOTAL set size (the prescribed vertex is always selected).
    return [0]+[bc(T,j)-bc(T-a,j)-bc(T-b,j)+bc(T-c,j) for j in range(T+1)]

def graph_check(n):
    m=n-3; total=0; tested=0
    for e in range(2):
      for U in range(1<<m):
       for W in range(1<<m):
        k=U.bit_count(); l=W.bit_count(); t=(U&W).bit_count()
        a=k+e+1; b=l+e+1; c=2+k+l-t
        expected=prediction(n,a,b,c)
        for R in range(1<<(m*(m-1)//2)):
            closed=[1<<i for i in range(n)]
            def edge(i,j):
                closed[i]|=1<<j;closed[j]|=1<<i
            for i in range(m):
                edge(0,3+i)
                if (U>>i)&1:edge(1,3+i)
                if (W>>i)&1:edge(2,3+i)
            if e:edge(1,2)
            bit=0
            for i in range(m):
                for j in range(i+1,m):
                    if (R>>bit)&1:edge(3+i,3+j)
                    bit+=1
            actual=[0]*(n+1)
            for sub in range(1<<(n-1)):
                selected=1|(sub<<1)
                if all(selected&closed[i] for i in range(n)):
                    actual[selected.bit_count()]+=1
                tested+=1
            assert actual==expected,(n,e,U,W,R,expected,actual)
            total+=1
    return total,tested

def stochastic_checks():
    checked=0;strict=0
    for n in range(5,10):
      m=n-3
      for e in range(2):
       for k in range(m+1):
        for l in range(m+1):
         if not (k+l>=1 and (e==1 or (k>=1 and l>=1))):continue
         a=k+e+1;b=l+e+1
         lo=max(0,k+l-m);hi=min(k,l)
         hists=[]
         for t in range(lo,hi+1):
            c=2+k+l-t
            vals=prediction(n,a,b,c)
            mean=Fraction(sum(j*v for j,v in enumerate(vals)),sum(vals))
            baseline=Fraction(n+1,2)
            bound=baseline+Fraction(a,2*((1<<a)-1))+Fraction(b,2*((1<<b)-1))
            assert mean<=bound
            assert (mean==bound)==(e==0 and t==0),(n,k,l,e,t,mean,bound)
            hists.append((t,vals,mean))
            checked+=1
         for (t1,x,m1),(t2,y,m2) in zip(hists,hists[1:]):
            assert t1+1==t2
            assert m1>m2,(n,k,l,e,t1,t2,m1,m2)
            sx,sy=sum(x),sum(y)
            # Smaller overlap t1 has stochastically LARGER set-size distribution.
            for threshold in range(n+2):
                assert sum(x[threshold:])*sy>=sum(y[threshold:])*sx,(n,k,l,e,t1,t2,threshold)
            strict+=1
    return checked,strict

if __name__=='__main__':
    total=0;tested=0
    for n in range(4,8):
        graphs,subsets=graph_check(n)
        total+=graphs;tested+=subsets
        print(f'n={n}: graphs={graphs}, containing-vertex subsets={subsets}; exact profiles agree')
    profiles,strict=stochastic_checks()
    print(f'stochastic profiles={profiles}, strict successive overlap comparisons={strict}; all inequalities agree')
    print(f'ALL CHECKS PASSED; graphs={total}; containing-vertex subsets={tested}')
