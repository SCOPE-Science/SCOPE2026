#!/usr/bin/env python3
from itertools import product
from math import comb

MAX_N = 10

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def pscale(a,k): return [k*x for x in a]
def padd(*ps):
    m=max((len(p) for p in ps), default=0); c=[0]*m
    for p in ps:
        for i,x in enumerate(p): c[i]+=x
    return c

def psub(a,b): return padd(a,pscale(b,-1))
def shift(a,k): return [0]*k+a

def ppow(base,n):
    r=[1]
    for _ in range(n): r=conv(r,base)
    return r

def trim(a):
    a=a[:]
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def closed_formula(parts):
    N=sum(parts)
    all_lab=ppow([1,1,1],N)
    no2=ppow([1,1],N)
    exact_one_support=[0]
    for n in parts:
        inside_with_2=psub(ppow([1,1,1],n),ppow([1,1],n))
        exact_one_support=padd(exact_one_support,conv(inside_with_2,ppow([1,1],N-n)))
    multi=psub(psub(all_lab,no2),exact_one_support)

    one=[0]
    for n in parts:
        C=ppow([1,1],N-n)
        V=ppow([0,1,1],n)
        P=ppow([1,1,1],n)
        U=ppow([1,1],n)
        nozero_with_2=psub(V,shift([1],n))
        both_zero_and_2=padd(P,pscale(U,-1),pscale(V,-1),shift([1],n))
        outside_two_ones=C[:]
        if len(outside_two_ones)<2: outside_two_ones += [0]*(2-len(outside_two_ones))
        outside_two_ones[0]-=1
        outside_two_ones[1]-=(N-n)
        one=padd(one,conv(nozero_with_2,C),conv(both_zero_and_2,outside_two_ones))

    zero=[0]*(N+1)
    s=sum(n==1 for n in parts)
    zero[2]=sum(n==2 for n in parts)+comb(s,2)
    for t in range(3,N+1):
        q=comb(N,t)
        for n in parts:
            if t<n: q-=comb(n,t)
            if t-1<n: q-=comb(n,t-1)*(N-n)
        zero[t]=q
    return trim(padd(multi,one,zero))

def partitions(n,hi=None):
    if n==0:
        yield []
        return
    hi=n if hi is None else min(hi,n)
    for x in range(hi,0,-1):
        for rest in partitions(n-x,x):
            yield [x]+rest

def direct_ok(parts,lab):
    N=sum(parts); start=0
    for n in parts:
        a=sum(lab[v]==1 for v in range(start,start+n))
        b=sum(lab[v]==2 for v in range(start,start+n))
        z=n-a-b
        if z:
            A=sum(x==1 for x in lab); B=sum(x==2 for x in lab)
            local=((B-b)>=1 or (A-a)>=2)
            for v in range(start,start+n):
                if lab[v]==0:
                    outside=[u for u in range(N) if not (start<=u<start+n)]
                    vertex=(any(lab[u]==2 for u in outside) or sum(lab[u]==1 for u in outside)>=2)
                    if vertex!=local: raise AssertionError(('local criterion',parts,lab,v))
                    if not vertex: return False
        start+=n
    return True

def brute(parts):
    N=sum(parts); c=[0]*(2*N+1); local=0
    for lab in product(range(3),repeat=N):
        local+=1
        if direct_ok(parts,lab): c[sum(lab)]+=1
    return trim(c),local

def main():
    profiles=labelings=0
    for N in range(2,MAX_N+1):
        for parts in partitions(N):
            if len(parts)<2: continue
            profiles+=1
            got,k=brute(parts); labelings+=k
            want=closed_formula(parts)
            if got!=want:
                raise AssertionError(('coefficients',parts,got,want))
    print(f'VERIFY_OK profiles={profiles} labelings={labelings} local_checks={labelings} max_order={MAX_N}')
if __name__=='__main__': main()
