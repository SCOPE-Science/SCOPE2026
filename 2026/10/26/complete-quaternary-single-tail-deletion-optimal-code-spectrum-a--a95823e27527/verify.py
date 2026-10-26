#!/usr/bin/env python3
"""Independent finite verification of partial-permutation one-tail-deletion code census.
Public scientific definitions and methods only.
"""
from itertools import permutations
from collections import Counter
from math import factorial


def all_words(q,ending):
    a=list(range(q))
    return [(ending,)]+[p+(ending,) for k in range(1,q) for p in permutations([u for u in a if u!=ending],k)]


def brute_one_root(q):
    words=all_words(q,0)
    assert len(words)==sum(factorial(q-1)//factorial(q-i) for i in range(1,q+1))
    n=len(words)
    balls=[{w,w[1:]} if len(w)>1 else {w} for w in words]
    # Every pair is tested directly from overlap of actual channel outputs.
    conflicts=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if balls[i]&balls[j]:
                conflicts[i]|=1<<j
                conflicts[j]|=1<<i
    counts=Counter();maxword=0;maxcount=0
    composition=Counter()
    total=0
    for mask in range(1<<n):
        selection=[i for i in range(n) if (mask>>i)&1]
        if any(conflicts[i]&mask for i in selection):continue
        k=len(selection);counts[k]+=1;total+=1
        if k>maxword:maxword=k
        composition[tuple(sum(len(words[i])==l for i in selection) for l in range(1,q+1))]+=1
    maxcount=counts[maxword]
    return counts,maxword,maxcount,composition


def mul(a,b):
    out=Counter()
    for i,u in a.items():
        for j,v in b.items():out[i+j]+=u*v
    return out

def powpoly(a,n):
    b=Counter({0:1})
    for _ in range(n):b=mul(b,a)
    return b

def rec(q):
    # U_b excludes root; V_b includes root. The rooted suffix tree
    # has b interchangeable children, each with b-1 available new symbols.
    U=Counter({0:1});V=Counter({1:1})
    for b in range(1,q):
        t=powpoly(U,b)
        v=Counter({j+1:coef for j,coef in t.items()})
        u=Counter(t)
        extra=mul(V,powpoly(U,b-1))
        for j,c in extra.items():u[j]+=b*c
        U,V=u,v
    return U+V


def main():
    for q in (2,3,4):
        actual,best,num,composition=brute_one_root(q)
        pred=rec(q)
        assert pred==actual,(q,pred,actual)
        assert best==max(pred) and num==pred[best]
        print('q=',q,'words/root=',sum(factorial(q-1)//factorial(q-i) for i in range(1,q+1)),'optimum/root=',best,'maxima/root=',num,'labeled global maxima=',num**q)
        if q==4:
            predicted=Counter()
            for low in (1,2):
                lowcount=1 if low==1 else 3
                active_groups=3 if low==1 else 2
                from math import comb
                for j in range(active_groups+1):
                    profile=[0,0,0,0]
                    profile[low-1]=1
                    profile[2]=j
                    profile[3]=6-j
                    predicted[tuple(profile)]+=lowcount*comb(active_groups,j)*2**j
            checked=Counter({vec:ct for vec,ct in composition.items() if sum(vec)==7})
            assert checked==predicted,(checked,predicted)
            assert sum(predicted.values())==54
            assert min(sum((i+1)*v for i,v in enumerate(vec)) for vec in predicted)==22
            assert max(sum((i+1)*v for i,v in enumerate(vec)) for vec in predicted)==26
            print('q=4 optimum one-root length profiles:',sorted(checked.items()))
            print('q=4 minimum-total-length labeled maxima:',(8**4),'maximum-total-length labeled maxima:',(3**4))
    for q in (5,6):
        poly=rec(q)
        print('q=',q,'root-opt=',max(poly),'root-count=',poly[max(poly)])
    print('VERIFY_OK')

if __name__=='__main__':main()
