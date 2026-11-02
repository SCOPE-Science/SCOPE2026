#!/usr/bin/env python3
"""Independent immutable-type recursion for finite interval-inclusion posets."""
import sys

def rank3_type(n):
    # Type A_n positive roots: [i,j] where 0 <= i <= j < n.
    elements = [(i,j) for j in range(n) for i in range(j+1)]
    N = len(elements)
    contained = lambda a,b: a != b and b[0] <= a[0] <= a[1] <= b[1]
    def atomic(a,b,c):
        arr=(a,b,c)
        # a full, *ordered* matrix of equalities and strict inclusions
        return tuple((arr[u] == arr[v],contained(arr[u],arr[v])) for u in range(3) for v in range(3))
    type_1 = {(a,b):frozenset(atomic(a,b,c) for c in elements) for a in elements for b in elements}
    type_2 = {a:frozenset(type_1[a,b] for b in elements) for a in elements}
    return frozenset(type_2.values()), (len(set(type_1.values())),len(set(type_2.values())))

def main():
    groups=[]
    for n in range(1,int(sys.argv[1])+1 if len(sys.argv)>1 else 12):
        t,ns=rank3_type(n)
        try: cl=groups.index(t)
        except ValueError: cl=len(groups);groups.append(t)
        print(f'n={n:02d} rank3={cl} pair-types={ns[0]} singleton-types={ns[1]}',flush=True)
if __name__=='__main__': main()
