#!/usr/bin/env python3
"""Independent finite Heyting truth-table checks of the stated materializer theorem."""
from itertools import product
from math import comb

def trial(n,k):
    b=1<<n
    # Boolean elements 0..b-1; appended new upper chain b,...,b+k-1.
    N=b+k
    def le(x,y):
        if x<b and y<b: return (x & y)==x
        if x<b: return True
        if y<b: return False
        return x<=y
    def meet(x,y):
        if x<b and y<b: return x&y
        if x<b: return x
        if y<b: return y
        return min(x,y)
    def join(x,y):
        if x<b and y<b: return x|y
        if x<b: return y
        if y<b: return x
        return max(x,y)
    def impl(x,y):
        z=[z for z in range(N) if le(meet(x,z),y)]
        mx=[t for t in z if all(le(w,t) for w in z)]
        assert len(mx)==1,(n,k,x,y,z,mx)
        return mx[0]
    top=N-1
    M=[]; errors=0
    for x in range(N):
        neg=impl(x,0)
        good={y for y in range(N) if impl(x,y)==join(neg,y)}
        M.append(good)
        if x==0 or x==top: predicted=set(range(N))
        elif x<b: predicted={y for y in range(b) if (x&y)!=x}|{top}
        else: predicted=set(range(b)) | set(range(b,x)) | {top}
        assert good==predicted,(n,k,x,good,predicted)
        errors+=N-len(good)
    F=3**n-b+(b-1)*(k-1)+k*(k-1)//2
    assert errors==F,(n,k,errors,F)
    distinct=list(dict.fromkeys(map(frozenset,M)))
    assert len(distinct)==b-1+k,(n,k,len(distinct))
    # Check the asserted materializer-inclusion order exhaustively.
    for x,y in product(range(1,b),repeat=2):
        assert (M[x]<=M[y])==le(x,y)
    for x in range(1,b):
        for i in range(k):
            assert M[x]<M[b+i]
    for i in range(k):
        for j in range(k):
            assert (M[b+i]<=M[b+j])==(i<=j)
    return N*N,errors

def main():
    cases=pairs=0
    for n in range(1,6):
        for k in range(1,7):
            N2,e=trial(n,k)
            cases+=1; pairs+=N2
    print('VERIFY_OK', 'cases',cases,'material_implication_pairs',pairs,
          'materializer_orders_checked',cases)
if __name__=='__main__':main()
