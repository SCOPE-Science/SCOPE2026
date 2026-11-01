#!/usr/bin/env python3
"""Reproduce rank/Jordan and finite-state orbit checks for leaf-corona XOR systems."""
from collections import Counter
from itertools import product

def adj_path(n):
    a=[0]*n
    for i in range(n-1):
        a[i]|=1<<(i+1); a[i+1]|=1<<i
    return a

def adj_cycle(n):
    a=adj_path(n)
    a[0]|=1<<(n-1); a[n-1]|=1
    return a

def corona(core):
    n=len(core)
    return [core[i] | (1<<(n+i)) for i in range(n)]+[1<<i for i in range(n)]

def action(a,x):
    return sum((int((r&x).bit_count()&1)<<i) for i,r in enumerate(a))

def mul(a,b):
    # each row of A B = xor rows B indexed by entries of row of A
    z=[]
    for r in a:
        v=0
        while r:
            bit=r&-r; v^=b[bit.bit_length()-1];r^=bit
        z.append(v)
    return z

def rank(a):
    basis={}
    for v in a:
        while v:
            k=v.bit_length()-1
            if k not in basis:
                basis[k]=v;break
            v^=basis[k]
    return len(basis)

def jordan_dims_bplus1(core):
    b=corona(core); z=len(b)
    c=[b[i]^(1<<i) for i in range(z)]
    p=[1<<i for i in range(z)]
    out=[]
    for k in range(z+1):
        out.append(z-rank(p))
        p=mul(p,c)
    return out

def partition_from_kernel(dims):
    dd=dims+[dims[-1]]
    second=[(dd[k]-dd[k-1])-(dd[k+1]-dd[k]) for k in range(1,len(dd)-1)]
    return sorted((k for k,m in enumerate(second,1) for j in range(m)),reverse=True)

def predicted(coren):
    return [min(k,2*coren) for k in range(2*coren+1)]

def brute_orbits(b):
    d=len(b); seen=set(); counts=Counter()
    for x in range(1<<d):
        if x in seen:continue
        trajectory=[]; lookup={};y=x
        while y not in lookup:
            lookup[y]=len(trajectory);trajectory.append(y);y=action(b,y)
        if lookup[y]!=0: raise AssertionError('nonperiodic vertex')
        for v in trajectory:seen.add(v)
        counts[len(trajectory)]+=1
    return counts

def test_partitions():
    total=0
    # every partition of dimensions 1..8 (nilpotent Jordan block direct sum)
    def parts(n,m=None):
        if m is None: m=n
        if n==0:
            yield ();return
        for k in range(min(m,n),0,-1):
            for rem in parts(n-k,k):yield (k,)+rem
    for n in range(1,9):
        for lens in parts(n):
            a=[]; off=0
            for L in lens:
                for i in range(L):a.append((1<<(off+i+1)) if i<L-1 else 0)
                off+=L
            dims=jordan_dims_bplus1(a)
            assert dims==[sum(min(k,2*L) for L in lens) for k in range(2*n+1)],(lens,dims)
            assert partition_from_kernel(dims)==sorted([2*L for L in lens],reverse=True)
            total+=1
    return total

def test_families():
    nchecks=0
    for r in range(2,7):
        n=2**r
        a=adj_cycle(n)
        # core nilpotent blocks (n/2,n/2); corona (n,n)
        dims=jordan_dims_bplus1(a)
        assert dims==[2*min(k,n) for k in range(2*n+1)],('cycle',n)
        nchecks+=1
    for r in range(2,7):
        n=2**r-1
        a=adj_path(n)
        dims=jordan_dims_bplus1(a)
        assert dims==[min(k,2*n) for k in range(2*n+1)],('path',n)
        nchecks+=1
    return nchecks

def test_states():
    records=[]
    for name,n,a,blocks in [('cycle',4,adj_cycle(4),[4,4]),('cycle',8,adj_cycle(8),[8,8]),('path',3,adj_path(3),[6]),('path',7,adj_path(7),[14])]:
        b=corona(a); obs=brute_orbits(b)
        m=max(x.bit_length() for x in blocks)
        exp=Counter()
        prev=0
        for j in range(m+1):
            t=1<<j
            fixed=1<<sum(min(t,L) for L in blocks)
            count=(fixed-prev)//t
            assert count>=0 and count*t+prev==fixed
            exp[t]=count;prev=fixed
        assert obs==exp,(name,n,obs,exp)
        records.append(f'{name} n={n} configurations={1<<len(b)} primitive_orbits={dict(sorted(obs.items()))}')
    return records

if __name__=='__main__':
    print('NILPOTENT_BLOCK_PARTITION_CASES',test_partitions())
    print('DYADIC_FAMILY_CASES',test_families())
    for r in test_states():print('EXHAUSTIVE',r)
    print('CORONA_JORDAN_DOUBLING_VERIFIED')
