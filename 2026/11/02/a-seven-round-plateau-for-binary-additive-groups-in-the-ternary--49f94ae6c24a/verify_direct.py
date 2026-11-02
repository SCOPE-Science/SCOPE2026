#!/usr/bin/env python3
"""Independent explicit-element FO type recursion for small binary additive groups."""
from itertools import product

def atomic_tuple(tup):
    n = len(tup)
    return (tuple(int(tup[i] == tup[j]) for i in range(n) for j in range(n)),
            tuple(int((tup[i] ^ tup[j]) == tup[k]) for i in range(n) for j in range(n) for k in range(n)))

def direct(q, ds=(1,2,3)):
    intern = [dict() for _ in range(q+1)]
    ids = []
    for d in ds:
        N=1<<d
        cache={}
        def typ(tup):
            if tup in cache:return cache[tup]
            t=len(tup)
            a=atomic_tuple(tup)
            if t==q:k=(a,())
            else:k=(a,tuple(sorted({typ(tup+(x,)) for x in range(N)})))
            idx=intern[t].setdefault(k,len(intern[t])+1)
            cache[tup]=idx
            return idx
        ids.append(typ(()))
    return ids

def main():
    for q in range(1,5):
        ids=direct(q)
        print(f'DIRECT q={q}: {ids} classes={len(set(ids))}')
        assert ids == {1:[1,1,1],2:[1,2,2],3:[1,2,3],4:[1,2,3]}[q]
    print('DIRECT_VERIFY_OK')
if __name__=='__main__':main()
