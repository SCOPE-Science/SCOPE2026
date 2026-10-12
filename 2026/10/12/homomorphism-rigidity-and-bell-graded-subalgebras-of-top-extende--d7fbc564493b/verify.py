#!/usr/bin/env python3
"""Finite exact checks for the homomorphism/subalgebra census of the top-extended Boolean Heyting algebras.
Python standard library only; no external files.
"""
from itertools import product
from math import factorial
from collections import Counter

ASSERTIONS = 0

def check(c, why=''):
    global ASSERTIONS
    ASSERTIONS += 1
    if not c:
        raise AssertionError(why)

def stirling(n, k):
    if n == 0: return int(k == 0)
    if k == 0: return 0
    return k*stirling(n-1,k)+stirling(n-1,k-1)

def bell(n):
    return sum(stirling(n,k) for k in range(n+1))

class A:
    def __init__(self,m):
        self.m=m
        self.N=1<<m
        self.U=tuple(range(self.N+1))
        self.TOP=self.N
        self.subset=lambda a,b: (b == self.TOP or (a != self.TOP and a&b==a))
        self.meet=lambda a,b: (a&b if a!=self.TOP and b!=self.TOP else (a if b==self.TOP else b))
        self.join=lambda a,b: (a|b if a!=self.TOP and b!=self.TOP else self.TOP)
        # Direct independent residuation from the order, not the Esakia dual map formula.
        self.impl={}
        for a,b in product(self.U,repeat=2):
            eligible=[c for c in self.U if self.subset(self.meet(a,c),b)]
            maxes=[c for c in eligible if all(self.subset(x,c) for x in eligible)]
            check(len(maxes)==1,('implication_not_unique',m,a,b))
            self.impl[a,b]=maxes[0]

def is_hom(src,dst,arr):
    # 0 and 1 are fixed by algebra homomorphisms.
    if arr[0]!=0 or arr[-1]!=dst.TOP:return False
    for x in src.U:
      for y in src.U:
        if arr[src.meet(x,y)]!=dst.meet(arr[x],arr[y]):return False
        if arr[src.join(x,y)]!=dst.join(arr[x],arr[y]):return False
        if arr[src.impl[x,y]]!=dst.impl[arr[x],arr[y]]:return False
    return True

def is_pmorphism(n,m,arr):
    # Dual rooted-star P_n -> P_m; point 0 is root; leaves 1..n.
    for a,b in product(range(n+1),repeat=2):
        if (a==0 or a==b) and not (arr[a]==0 or arr[a]==arr[b]):return False
    for a in range(n+1):
        upY=set(range(m+1)) if arr[a]==0 else {arr[a]}
        upX=[b for b in range(n+1) if a==0 or b==a]
        if {arr[b] for b in upX} != upY:return False
    return True

def inverse_image_on_A(n,m,arr):
    # Source algebra A_m = upsets(P_m); target algebra A_n = upsets(P_n).
    out=[]
    for elem in range((1<<m)+1):
        occupied=(set(range(m+1)) if elem==(1<<m) else {j+1 for j in range(m) if (elem>>j)&1})
        pre={i for i in range(n+1) if arr[i] in occupied}
        if 0 in pre:
            check(len(pre)==n+1)
            out.append(1<<n)
        else:
            out.append(sum(1<<(i-1) for i in pre))
    return tuple(out)

def partition_normal_forms(m):
    # Restricted growth strings; one representative per set partition.
    forms=[]
    def rec(s,k):
        if len(s)==m:
            blocks=[0]*(k+1)
            for i,j in enumerate(s):blocks[j]|=1<<i
            els={0}
            for membership in range(1<<(k+1)):
                mask=0
                for j,block in enumerate(blocks):
                    if (membership>>j)&1: mask|=block
                els.add(mask)
            els.add(1<<m)
            forms.append((k+1,frozenset(els)))
            return
        for v in range(k+2):rec(s+(v,),max(k,v))
    rec((0,),0)
    return forms

def brute_subalgebras(m):
    alg=A(m)
    # Exhaustively inspect all subsets containing 0 and the new greatest element.
    normal=Counter()
    instances=set()
    for choice in range(1<<(alg.N-1)):
        present={0,alg.TOP}
        for x in range(1,alg.N):
            if choice&(1<<(x-1)):present.add(x)
        ok=True
        for x in present:
            if not ok:break
            for y in present:
                if alg.meet(x,y) not in present or alg.join(x,y) not in present or alg.impl[x,y] not in present:
                    ok=False;break
        if ok:
            normal[len(present)]+=1
            instances.add(frozenset(present))
    return normal,instances

def main():
    subalgebras_screened=0
    for m in range(1,5):
        cnt,inst=brute_subalgebras(m)
        forms=partition_normal_forms(m)
        check(len(forms)==bell(m))
        check(len(set(s for k,s in forms))==len(forms))
        predicted=Counter({2:1})
        for k in range(1,m+1):predicted[(1<<k)+1]=stirling(m,k)
        check(cnt==predicted,(m,cnt,predicted))
        check(inst=={frozenset((0,1<<m))} | {s for k,s in forms})
        subalgebras_screened+=1<<((1<<m)-1)
    full_dual=0
    hom_from_dual=0
    for m in range(1,6):
        for n in range(1,6):
            dual=[]
            for ar in product(range(m+1),repeat=n+1):
                full_dual+=1
                if is_pmorphism(n,m,ar): dual.append(ar)
            exp=m+(factorial(m)*stirling(n,m) if n>=m else 0)
            check(len(dual)==exp,('duals',m,n,len(dual),exp))
            counts=Counter()
            for ar in dual:
                if ar[0]==0:
                    counts[(1<<m)+1]+=1
                else: counts[2]+=1
            check(counts==Counter({2:m, (1<<m)+1:exp-m}))
            if m<=3 and n<=3:
                x=A(m);y=A(n)
                homs={inverse_image_on_A(n,m,ar) for ar in dual}
                check(len(homs)==len(dual))
                for h in homs:check(is_hom(x,y,h))
                hom_from_dual+=len(homs)
            if m==n:
                idem=[ar for ar in dual if all(ar[ar[i]]==ar[i] for i in range(m+1))]
                check(len(idem)==m+1)
                check(len([ar for ar in dual if ar[0]==0])==factorial(m))
    brute_maps=0
    for m,n in ((1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2)):
        src=A(m);dst=A(n)
        count=0
        for middle in product(dst.U,repeat=src.N-1):
            brute_maps+=1
            tup=(0,)+middle+(dst.TOP,)
            if is_hom(src,dst,tup):count+=1
        expected=m+(factorial(m)*stirling(n,m) if n>=m else 0)
        check(count==expected,('algebraic',m,n,count,expected))
    print('VERIFY_OK',ASSERTIONS,'exact assertions;',full_dual,'dual function tables;',subalgebras_screened,
          'candidate subalgebras;',brute_maps,'direct algebra function tables;',hom_from_dual,
          'dual-induced homomorphisms; m,n<=5 dual and m<=4 subalgebras')

if __name__=='__main__':main()
