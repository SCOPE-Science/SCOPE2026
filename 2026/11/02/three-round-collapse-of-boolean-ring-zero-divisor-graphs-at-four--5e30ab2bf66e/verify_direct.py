#!/usr/bin/env python3
"""Independent element-level EF rank-3 verification for Boolean zero-divisor graphs.
Scientific object: all nonempty proper supports in {1,...,n}; E(U,V) iff U & V == 0.
No external packages required.
"""
from itertools import product


def root_signature(n):
    V=tuple(range(1,(1<<n)-1))
    def edge(a,b):return int(a!=b and (a&b)==0)
    # Equality + irreflexive adjacency are all relevant atomic facts on 3 vertices.
    triple_type={}
    for a in V:
        for b in V:
            for c in V:
                triple_type[(a,b,c)] = (
                    int(a==b),int(a==c),int(b==c),
                    edge(a,b),edge(a,c),edge(b,c))
    pair_type={(a,b):(
        int(a==b),edge(a,b),
        frozenset(triple_type[(a,b,c)] for c in V))
        for a in V for b in V}
    point_type={a:frozenset(pair_type[(a,b)] for b in V) for a in V}
    return frozenset(point_type.values()),(len(set(pair_type.values())),len(set(point_type.values())))


def main():
    signatures={}
    for n in range(2,8):
        sig,nums=root_signature(n)
        signatures[n]=sig
        print(f'n={n}, vertices={2**n-2}, pair_types={nums[0]}, pointed_types={nums[1]}')
    assert signatures[2]!=signatures[3]
    assert signatures[3]!=signatures[4]
    assert signatures[4]==signatures[5]==signatures[6]==signatures[7]
    print('PASS: complete element-level rank-three types for n=2,...,7.')

if __name__=='__main__':main()
