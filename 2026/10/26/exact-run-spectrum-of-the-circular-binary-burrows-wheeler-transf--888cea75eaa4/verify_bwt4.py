"""Exact standalone verification of binary weight-four circular BWT run spectra.

The finite 365-cell sum is a polynomial identity over Z[z], not a
truncated generating-function experiment. Requires Python 3, stdlib only.
"""
from itertools import product, combinations
from collections import defaultdict, Counter
from math import comb


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c

def shift(a,n): return [0]*n+a

def powpol(a,n):
    b=[1]
    for _ in range(n):b=mul(b,a)
    return b

def factor(k):return [1]+[0]*(k-1)+[-1]

def bwt(g):
    k=len(g); output=[]
    for t in range(max(g),-1,-1):
        idx=sorted((i for i in range(k) if g[i]>=t),
                   key=lambda i:tuple(-g[(i+j)%k] for j in range(1,k+1)))
        output.extend('1' if g[i]==t else '0' for i in idx)
    return ''.join(output)

def direct_bwt(w):
    return ''.join(s[-1] for s in sorted(w[i:]+w[:i] for i in range(len(w))))

def nruns(s):return 1+sum(s[i]!=s[i-1] for i in range(1,len(s)))

def gaps_to_word(g):return ''.join('1'+'0'*v for v in g)

def cell_polys():
    common={r:[0] for r in (1,2,4,6,8)}
    # Common denominator T=(1-z)(1-z^2)(1-z^3)(1-z^4).
    T=[1]
    for k in (1,2,3,4):T=mul(T,factor(k))
    common[1]=add(common[1],T) # exactly (0,0,0,0)
    for p in product(range(4),repeat=4):
        s=max(p)+1
        if set(p)!=set(range(s)):continue
        for e in product((1,2),repeat=s-1):
            if s==1:
                # all-equal positive gap: z^4/(1-z^4)
                numerator=shift(mul(mul(factor(1),factor(2)),factor(3)),4)
                common[2]=add(common[2],numerator)
                continue
            levels=[0]
            for d in e:levels.append(levels[-1]+d)
            g=tuple(levels[j] for j in p)
            r=nruns(bwt(g))
            heights=[sum(j>=h for j in p) for h in range(1,s)]
            exponent=sum(d*c for d,c in zip(e,heights))
            denominator_factors={4}|{c for d,c in zip(e,heights) if d==2}
            numerator=[1]
            for k in (1,2,3,4):
                if k not in denominator_factors:numerator=mul(numerator,factor(k))
            common[r]=add(common[r],shift(numerator,exponent))
    return common,T

def clean(a):
    a=a[:]
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def theorem_numerators(T):
    F={1:T}
    U=mul(mul(factor(1),factor(2)),factor(3))
    F[2]=mul(shift([4,2,4,1],1),U)
    P4=[4,10,13,17,11,6]
    F[4]=shift(mul(powpol(factor(1),2),[2*x for x in P4]),2)
    P6=[1,5,3,7,4,3]
    F[6]=shift(mul(factor(1),[4*x for x in P6]),3)
    P8=[2,0,2,1,1]
    F[8]=shift([4*x for x in P8],5)
    return F

def main():
    C,T=cell_polys()
    F=theorem_numerators(T)
    for r in C:
        assert clean(C[r])==clean(F[r]), ('GF polynomial identity',r,clean(C[r]),clean(F[r]))
    total=[0]
    for a in C.values():total=add(total,a)
    target=mul(mul([1,1],[1,1,1]),[1,1,1,1])
    assert clean(total)==clean(target),('total identity',total,target)
    print('365 exact cell classes: all five rational generating functions and total identity verified')
    n_cases=0
    for g in product(range(7),repeat=4):
        w=gaps_to_word(g)
        assert bwt(g)==direct_bwt(w),(g,bwt(g),direct_bwt(w))
        n_cases+=1
    print('Directly sorted circular BWT agrees with gap construction on',n_cases,'gap tuples')
    for n in range(4,20):
        hist=Counter()
        for positions in combinations(range(n),4):
            w=['0']*n
            for x in positions:w[x]='1'
            hist[nruns(direct_bwt(''.join(w)))]+=1
        print(n,dict(sorted(hist.items())))
        assert sum(hist.values())==comb(n,4)
    print('PASS')
if __name__=='__main__':main()
