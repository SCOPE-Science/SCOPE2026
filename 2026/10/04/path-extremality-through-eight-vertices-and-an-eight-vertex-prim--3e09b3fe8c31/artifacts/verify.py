#!/usr/bin/env python3
from pathlib import Path
from collections import Counter

EXPECTED_COUNTS = {1:1,2:2,3:4,4:11,5:34,6:156,7:1044,8:12346}
EXPECTED_PATH = {
    1:[0,1],
    2:[0,2,1],
    3:[0,2,3,1],
    4:[0,2,6,4,1],
    5:[0,2,9,10,5,1],
    6:[0,2,12,20,15,6,1],
    7:[0,2,15,34,35,21,7,1],
    8:[0,2,18,52,70,56,28,8,1],
}

def decode_graph6(s):
    s=s.strip()
    if not s or s.startswith('>>graph6<<'):
        raise ValueError('unexpected graph6 header/empty line')
    n=ord(s[0])-63
    if not (0 <= n <= 62):
        raise ValueError('only small graph6 order is supported')
    bits=[]
    for ch in s[1:]:
        x=ord(ch)-63
        if not (0 <= x < 64):
            raise ValueError('bad graph6 byte')
        bits.extend((x >> j) & 1 for j in range(5,-1,-1))
    need=n*(n-1)//2
    if len(bits) < need:
        raise ValueError('truncated graph6 line')
    adj=[0]*n
    t=0
    for j in range(1,n):
        for i in range(j):
            if bits[t]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            t += 1
    return adj

def is_zero_forcing(adj, start):
    n=len(adj)
    allmask=(1<<n)-1
    blue=start
    while True:
        if blue == allmask:
            return True
        changed=0
        b=blue
        while b:
            vbit=b & -b
            v=vbit.bit_length()-1
            white_neighbors=adj[v] & ~blue & allmask
            if white_neighbors and (white_neighbors & (white_neighbors-1)) == 0:
                changed |= white_neighbors
            b -= vbit
        if not changed:
            return False
        blue |= changed

def z_vector(adj):
    n=len(adj)
    z=[0]*(n+1)
    for S in range(1<<n):
        if is_zero_forcing(adj,S):
            z[S.bit_count()] += 1
    return z

def main():
    p=Path(__file__).with_name('graphs_upto8.g6')
    counts=Counter()
    equality=Counter()
    subset_tests=0
    graphs=0
    for line_no,line in enumerate(p.read_text(encoding='ascii').splitlines(),1):
        adj=decode_graph6(line)
        n=len(adj)
        if n not in EXPECTED_COUNTS:
            raise AssertionError((line_no,n))
        counts[n]+=1; graphs+=1; subset_tests += 1<<n
        z=z_vector(adj)
        target=EXPECTED_PATH[n]
        if len(z)!=len(target):
            raise AssertionError((line_no,'length'))
        bad=[k for k,(a,b) in enumerate(zip(z,target)) if a>b]
        if bad:
            raise AssertionError((line_no,n,bad,z,target,line))
        if z==target:
            equality[n]+=1
    if dict(sorted(counts.items())) != EXPECTED_COUNTS:
        raise AssertionError(('counts',dict(counts)))
    if dict(sorted(equality.items())) != {n:1 for n in EXPECTED_COUNTS}:
        raise AssertionError(('path-equality-counts',dict(equality)))
    print('orders:', ' '.join(f'{n}:{counts[n]}' for n in sorted(counts)))
    print('graphs_checked:', graphs)
    print('subsets_checked:', subset_tests)
    print('path_vector_n8:', EXPECTED_PATH[8])
    print('full_vector_equality_counts:', ' '.join(f'{n}:{equality[n]}' for n in sorted(equality)))
    print('ALL CHECKS PASSED')

if __name__=='__main__':
    main()
