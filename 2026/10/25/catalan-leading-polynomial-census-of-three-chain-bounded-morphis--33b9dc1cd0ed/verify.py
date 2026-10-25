"""Independent finite checks for the three-chain bounded-morphism census.

Run with Python 3 standard library: python grid_chain3_verify.py
All frames use reflexive componentwise order.
"""
from itertools import product, combinations_with_replacement
from math import comb


def direct(a,b):
    points=list(product(range(a),range(b)))
    succ=[[j for j,(v,w) in enumerate(points) if v>=i and w>=k]
          for i,k in points]
    ans=0
    for labels in product(range(3),repeat=a*b):
        if len(set(labels))!=3:
            continue
        if any(labels[i]>labels[j] for i in range(a*b) for j in succ[i]):
            continue
        if any(any(level not in {labels[j] for j in succ[i]}
                   for level in range(labels[i],3)) for i in range(a*b)):
            continue
        ans+=1
    return ans


def row_pairs(a,b):
    weak=[tuple(reversed(p)) for p in combinations_with_replacement(range(b+1),a)]
    ans=0
    for L in weak:
        if L[0]==0:
            continue
        for U in weak:
            if U[-1]==b or any(x>y for x,y in zip(L,U)):
                continue
            if all((L[i]==0 or (i+1<a and L[i+1]==L[i])
                    or U[i]>L[i] or (i+1<a and U[i+1]>=L[i])) for i in range(a)):
                ans+=1
    return ans


def transfer(a,b):
    states=[(l,u) for u in range(b+1) for l in range(u+1)]
    counts={(l,u):1 for l,u in states if l>0}
    for _ in range(1,a):
        next_counts={}
        for l,u in states:
            s=sum(v for (L,U),v in counts.items() if l<=L and u<=U
                  and (L==l or U>L or u==L))
            if s:
                next_counts[(l,u)]=s
        counts=next_counts
    return sum(v for (l,u),v in counts.items() if u<b and (l==0 or u>l))


def pattern_coefficient(a,m):
    top=m+1
    ans=0
    for seq in product(range(top+1),repeat=2*a):
        L=seq[:a]
        U=seq[a:]
        if set(range(1,top))-set(seq):
            continue
        if not (0<L[0] and U[-1]<top):
            continue
        if not all(L[i]>=L[i+1] and U[i]>=U[i+1] for i in range(a-1)):
            continue
        if any(L[i]>U[i] for i in range(a)):
            continue
        if any(L[i]>0 and (i==a-1 or L[i+1]<L[i])
               and not (U[i]>L[i] or (i<a-1 and U[i+1]>=L[i])) for i in range(a)):
            continue
        ans+=1
    return ans


def run():
    direct_tests=0
    for a in range(1,6):
        for b in range(1,6):
            if a*b<=10:
                assert direct(a,b)==row_pairs(a,b)==transfer(a,b),(a,b)
                direct_tests+=1
            else:
                assert row_pairs(a,b)==transfer(a,b),(a,b)
    patterns=[]
    for a in range(1,4):
        c=[pattern_coefficient(a,m) for m in range(2*a+1)]
        assert c[-1]==comb(2*a,a)//(a+1)
        for b in range(1,9):
            assert transfer(a,b)==sum(x*comb(b-1,m) if b-1>=m else 0
                                      for m,x in enumerate(c)),(a,b)
        patterns.append((a,c))
    assert patterns[1][1]==[0,3,9,7,2]
    checks=0
    for a in range(1,9):
        for b in range(1,9):
            assert transfer(a,b)==transfer(b,a),(a,b)
            checks+=1
    for b in range(1,31):
        assert transfer(2,b)==(b-1)*(b**3+5*b**2+10*b-12)//12
    print('ALL_CHECKS_PASS direct_configs={} transpose_cases={} pattern_coefficients={}'.format(
          direct_tests, checks, patterns))

if __name__=='__main__':
    run()
