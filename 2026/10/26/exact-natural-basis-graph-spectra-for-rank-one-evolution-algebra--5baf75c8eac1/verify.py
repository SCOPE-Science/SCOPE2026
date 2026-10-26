#!/usr/bin/env python3
"""Finite, independent checks for orthogonal-frame graph-support formulas.
Uses only Python's standard library; polynomial bases for F2, F4, F8.
No external data or certifier is invoked.
"""
from itertools import product
from collections import Counter
from math import factorial, comb
from functools import reduce

MOD = {2: 0b11, 4: 0b111, 8: 0b1011}

def mul(a,b,q):
    out=0
    m=MOD[q]
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&q: a^=m
    return out

def dot(a,b,q):
    o=0
    for x,y in zip(a,b): o ^=mul(x,y,q)
    return o

def orthogonal_frames(q,d):
    # For characteristic two, coordinate sum is XOR; unit norm means sum = 1.
    unit=[v for v in product(range(q),repeat=d) if reduce(lambda a,b:a^b,v,0)==1]
    def rec(frame):
        if len(frame)==d:
            yield tuple(frame);return
        for v in unit:
            if all(dot(v,w,q)==0 for w in frame):
                yield from rec(frame+[v])
    yield from rec([])

def sympl_size(m,q):
    ans=q**(m*m)
    for i in range(1,m+1):ans*=q**(2*i)-1
    return ans

def order(d,q):
    if d%2:return sympl_size((d-1)//2,q)
    return q**(d-1)*sympl_size((d-2)//2,q)

def A(k,c,q):
    if c:
        return ((q-1)**k -(-1)**k)//q
    return ((q-1)**k+(q-1)*(-1)**k)//q

def expected(d,q,u):
    c=reduce(lambda a,b:a^b,u,0)
    t=tuple([c]*d) if d%2 else None
    if d%2:
        if u==t: return 1,Counter({d:1}), 'fixed odd'
        size=q**(d-1)-1
        freq=Counter({k:comb(d,k)*A(k,c,q)-(int(k==d and c!=0)) for k in range(1,d+1)})
        return size, +freq, 'moving odd'
    tscalar=len(set(u))==1
    if not c and tscalar:
        return 1,Counter({d:1}), 'fixed even'
    if c:
        return q**(d-1),+Counter({k:comb(d,k)*A(k,c,q) for k in range(1,d+1)}),'anisotropic even'
    size=q**(d-1)-q
    freq=Counter({k:comb(d,k)*A(k,0,q)-(q-1 if k==d else 0) for k in range(1,d+1)})
    return size,+freq,'isotropic even'

def main():
    combos=[(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4),(8,2),(8,3)]
    for q,d in combos:
        frames=list(orthogonal_frames(q,d))
        assert len(frames)==order(d,q),(q,d,len(frames),order(d,q))
        assert len(frames)%factorial(d)==0
        samples=[(1,)+(0,)*(d-1), (1,)*d]
        if d>=3:samples +=[(1,1,0)+(0,)*(d-3)]
        if q>2 and d>=3:samples += [(1,2,0)+(0,)*(d-3), (1,2,3)+(0,)*(d-3)]
        for u in samples:
            if not any(u):continue
            orbit_size,expected_freq,kind=expected(d,q,u)
            counts=Counter()
            points=set()
            for frame in frames:
                w=tuple(dot(u,v,q) for v in frame)
                counts[sum(x!=0 for x in w)]+=1
                points.add(w)
            assert len(points)==orbit_size,(q,d,u,kind,len(points),orbit_size)
            assert sum(expected_freq.values())==orbit_size,(q,d,u,kind,expected_freq,orbit_size)
            for k in range(1,d+1):
                assert counts[k]*orbit_size == len(frames)*expected_freq[k],(q,d,u,kind,k,counts[k],expected_freq[k])
            print('PASS',q,d,kind,'frames',len(frames),'natural_bases',len(frames)//factorial(d),'spectrum',[k for k in range(1,d+1) if expected_freq[k]],'counts',dict(sorted(counts.items())))
    # Full nonzero-vector census for three extension-field parameter sets.
    for q,d in [(4,3),(4,4),(8,3)]:
        frames=list(orthogonal_frames(q,d))
        vectors_checked=0
        for u in product(range(q), repeat=d):
            if not any(u):continue
            size, frequencies, kind=expected(d,q,u)
            orbit=set()
            observed=Counter()
            for frame in frames:
                w=tuple(dot(u,v,q) for v in frame)
                orbit.add(w)
                observed[sum(x!=0 for x in w)]+=1
            assert len(orbit)==size,(q,d,u,kind,'orbit')
            for k in range(1,d+1):
                assert observed[k]*size==len(frames)*frequencies[k],(q,d,u,kind,k)
            vectors_checked+=1
        print('FULL_VECTOR_CENSUS',q,d,'vectors',vectors_checked,'frames',len(frames))
    print('VERIFY_OK')

if __name__=='__main__':main()
