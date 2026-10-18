"""Exact finite tests of Alexandrov rough-approximation fibers.
Independent enumeration of subsets and transitive posets; standard library only.
"""
from collections import defaultdict
from fractions import Fraction
import itertools
import random

def closure_of_upper_triangle(n, edges):
    up=[1<<i for i in range(n)]
    k=0
    for i in range(n):
        for j in range(i+1,n):
            if edges>>k&1: up[i]|=1<<j
            k+=1
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if up[i]>>j&1: up[i]|=up[j]
    return tuple(up)

def rough(up, X):
    I=sum((1<<i) for i,U in enumerate(up) if U&X == U)
    C=sum((1<<i) for i,U in enumerate(up) if U&X)
    return I,C

def free_mask(up, I,C):
    F=0
    for i,U in enumerate(up):
        S=U & ~(1<<i)
        # There is a selected strict successor iff some successor is in C.
        # There is an absent strict successor iff some successor is outside I.
        if S&C and S&~I: F|=1<<i
    return F

def check(up):
    n=len(up)
    fibers=defaultdict(list)
    for X in range(1<<n):fibers[rough(up,X)].append(X)
    dims=[]
    for (I,C),xs in fibers.items():
        F=free_mask(up,I,C)
        fixed=((1<<n)-1)^F
        ref=xs[0]&fixed
        predicted={ref|Y for Y in range(1<<n) if Y&~F==0}
        assert set(xs)==predicted,(up,(I,C),xs,predicted)
        dims.extend([F.bit_count()]*len(xs))
    # Independent evaluation of the entropy formula for a uniform source.
    theoretical=Fraction(0)
    for i,U in enumerate(up):
        d=(U&~(1<<i)).bit_count()
        if d>0: theoretical+=1-Fraction(2,2**d)
    observed=Fraction(sum(dims),1<<n)
    assert observed==theoretical, (up, observed,theoretical)
    # Independent rational-weight check at Bernoulli(1/3).
    weighted=Fraction(sum((1<< (n-X.bit_count()))*free_mask(up,*rough(up,X)).bit_count()
                         for X in range(1<<n)),3**n)
    predicted=Fraction(0)
    for i,U in enumerate(up):
        d=(U&~(1<<i)).bit_count()
        if d>0: predicted+=1-Fraction(1,3**d)-Fraction(2**d,3**d)
    assert weighted==predicted, (up,weighted,predicted)
    return len(fibers)

def preorder_boundary_test():
    total=0
    for n in range(1,5):
        ordered_pairs=[(i,j) for i in range(n) for j in range(n) if i!=j]
        count=0
        for mask in range(1<<len(ordered_pairs)):
            U=[1<<i for i in range(n)]
            for k,(i,j) in enumerate(ordered_pairs):
                if mask>>k&1:U[i]|=1<<j
            if any((U[i]>>j&1) and (U[j]&~U[i]) for i in range(n) for j in range(n)):continue
            antisymmetric=all(not (U[i]>>j&1 and U[j]>>i&1) for i in range(n) for j in range(i+1,n))
            fib=defaultdict(list)
            for X in range(1<<n): fib[rough(U,X)].append(X)
            # An interval is determined by the intersection and union of its members.
            intervals=True
            for xs in fib.values():
                lo=(1<<n)-1
                hi=0
                for X in xs:lo&=X;hi|=X
                if len(xs)!=(1<<(hi^lo).bit_count()):
                    intervals=False
                    break
            assert antisymmetric==intervals,(n,U,antisymmetric,intervals)
            count+=1
        total+=count
        print('PREORDER_N',n,'relations',count,'interval_iff_T0=PASS')
    return total

def main():
    graph_cases=0
    fibers=0
    seen=set()
    for n in range(1,7):
        count=0
        for e in range(1<<(n*(n-1)//2)):
            up=closure_of_upper_triangle(n,e)
            if up in seen:continue
            seen.add(up)
            fibers+=check(up)
            count+=1
        graph_cases+=count
        print('POSITIVE_N',n,'distinct_topologically_sorted_orders',count)
    rng=random.Random(20261017)
    for n in range(7,11):
        for _ in range(250):
            e=sum((1<<k) for k in range(n*(n-1)//2) if rng.random()<0.23)
            fibers+=check(closure_of_upper_triangle(n,e))
            graph_cases+=1
    # Non-T0 preorder: indistinguishable 3-point equivalence class.
    up=(7,7,7)
    f=defaultdict(list)
    for X in range(8):f[rough(up,X)].append(X)
    assert sorted(map(len,f.values()))==[1,1,6]
    # Non-T0 two-point preorder has a non-interval fiber {01,10}.
    up=(3,3)
    f=defaultdict(list)
    for X in range(4):f[rough(up,X)].append(X)
    assert sorted(map(len,f.values()))==[1,1,2]
    assert set(max(f.values(),key=len))=={1,2}
    preorders=preorder_boundary_test()
    print('VERIFY_OK preorders',preorders,'sorted_posets_and_samples',graph_cases,'realized_fibers',fibers,'all_boolean_cubes=PASS','uniform_and_biased_entropy=PASS','non_T0_boundary=PASS')

if __name__=='__main__':main()
