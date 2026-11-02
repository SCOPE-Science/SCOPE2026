#!/usr/bin/env python3
"""Standalone integer verification of a proposed exact zero-field Ising result.
No third-party modules are required. Finite checks do not replace the proof.
"""
from collections import defaultdict
from itertools import combinations
from math import comb

PAIRS = ((-1,-1),(-1,1),(1,-1),(1,1))

def energy(u,v):
    n=len(u)
    return sum(u[i]*u[(i+1)%n]+u[i]*v[i]+v[i]*v[(i+2)%n] for i in range(n))

def lucas(k):
    a,b=2,1
    for i in range(k):a,b=b,a+b
    return a

def independent_sets(m):
    for bits in range(1<<m):
        if bits & ((bits<<1)|(bits>>(m-1))) & ((1<<m)-1):continue
        yield bits

def reconstruct(n,a,b,bits):
    assert n%4==0 and n>=8
    m=n//2
    t=[1 if bits>>j&1 else -1 for j in range(m)]
    u=[None]*n;v=[None]*n
    def sign(x):return 1 if x>0 else -1
    for j in range(m):
        v[2*j]=a*(-1)**j
        v[2*j+1]=b*(-1)**j
        u[2*j]=a*(-1)**j*t[j]
        u[2*j+1]=-(-1)**j*sign(a*(t[j]-t[(j+1)%m])+b)
    return u,v

def transfer(n):
    """Exact cyclic width-two DP: minimum energy and # minimizing configurations."""
    M={}
    for x in range(4):
        for y in range(4):
            state={(x,y):(0,1)}
            for step in range(n):
                out={}
                for (aa,bb),(E,C) in state.items():
                    u0,v0=PAIRS[aa];u1,v1=PAIRS[bb]
                    for z in range(4):
                        u2,v2=PAIRS[z]
                        dest=(bb,z)
                        EE=E+u0*v0+u0*u1+v0*v2
                        old=out.get(dest)
                        if old is None or EE<old[0]:out[dest]=(EE,C)
                        elif EE==old[0]:out[dest]=(EE,old[1]+C)
                state=out
            ans=state.get((x,y))
            if ans is not None:
                E,C=ans
                if E not in M:M[E]=C
                else:M[E]+=C
    E=min(M)
    return E,M[E]

def exhaustive(n):
    E=10**9;count=0
    for bits in range(1<<(2*n)):
        u=[1 if bits>>i&1 else -1 for i in range(n)]
        v=[1 if bits>>(n+i)&1 else -1 for i in range(n)]
        ee=energy(u,v)
        if ee<E:E=ee;count=1
        elif ee==E:count+=1
    return E,count

def main():
    assert lucas(0)==2 and lucas(4)==7 and lucas(6)==18
    verified=0
    for n in range(8,65,4):
        e,c=transfer(n)
        assert (e,c)==(-2*n,4*lucas(n//2)),(n,e,c)
        verified+=1
    print('TRANSFER',verified,'sizes n=8..64 step4: exact minimum and full degeneracy matched')
    for n in (8,12,16,20,24,28,32):
        m=n//2
        hist=defaultdict(int); seen=set()
        for a in (-1,1):
            for b in (-1,1):
                for bits in independent_sets(m):
                    u,v=reconstruct(n,a,b,bits)
                    assert energy(u,v)==-2*n
                    assert sum(u)+sum(v)==0
                    key=tuple(u+v)
                    assert key not in seen
                    seen.add(key)
                    hist[bits.bit_count()]+=1
        assert len(seen)==4*lucas(m)
        for q in range(m//2+1):
            expected=4*m*comb(m-q,q)//(m-q)
            assert hist[q]==expected,(n,q,hist[q],expected)
        print('BIJECTION',n,'states',len(seen),'counts',dict(sorted(hist.items())))
    e,c=exhaustive(8)
    assert (e,c)==(-16,28)
    print('EXHAUSTIVE n=8: 65536 independent labelled spin configurations; min=-16 count=28')
    print('ALL CHECKS PASSED')
if __name__=='__main__': main()
