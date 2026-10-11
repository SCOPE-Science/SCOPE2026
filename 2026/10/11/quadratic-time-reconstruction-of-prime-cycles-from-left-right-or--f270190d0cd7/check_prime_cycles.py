#!/usr/bin/env python3
"""Exhaustive finite checks of cyclic-shift reconstruction of prime cycles."""
from itertools import permutations

def match_rotation(hay,pat):
    p=len(hay)
    # KMP prefix function, O(p)
    lps=[0]*p
    j=0
    for i in range(1,p):
        while j and pat[j]!=pat[i]: j=lps[j-1]
        if pat[j]==pat[i]: j+=1
        lps[i]=j
    j=0
    matches=[]
    for k in range(2*p-1):
        ch=hay[k%p]
        while j and pat[j]!=ch: j=lps[j-1]
        if pat[j]==ch: j+=1
        if j==p:
            st=k-p+1
            if st<p: matches.append(st)
            j=lps[j-1]
    return matches

def recover(signs):
    p=len(signs); S={0}; a=[0]*p
    for i in range(1,p):
        A=[int(k in S) for k in range(p)]
        C=signs[i].copy(); C[0]=0
        # C[n] = A[(n+a_i)%p], so rotated A by +a_i matches C
        shifts=match_rotation(A,C)
        assert len(shifts)==1, (p,i,shifts)
        a[i]=shifts[0]
        assert a[i] not in S
        S.add(a[i])
    positions={u:i for i,u in enumerate(a)}
    return tuple(positions[(u+1)%p] for u in a)

def signs_of(perm):
    p=len(perm); answer=[]
    for i in range(p):
        j=i; row=[]
        for t in range(p):
            row.append(int(j<=i));j=perm[j]
        assert j==i
        answer.append(row)
    return answer

def cycle_perms(p):
    for order in permutations(range(1,p)):
        cycle=(0,)+order
        perm=[0]*p
        for j,x in enumerate(cycle): perm[x]=cycle[(j+1)%p]
        yield tuple(perm)

if __name__=='__main__':
    for p in [2,3,5,7]:
        n=0
        for f in cycle_perms(p):
            assert recover(signs_of(f))==f, (p,f)
            n+=1
        print(f'p={p}: {n} complete cycles checked')
    import random
    rng=random.Random(20261008)
    for p in [11,13,17,19,23]:
        for _ in range(200):
            order=list(range(1,p));rng.shuffle(order)
            perm=[0]*p; c=[0]+order
            for j,x in enumerate(c):perm[x]=c[(j+1)%p]
            assert recover(signs_of(tuple(perm)))==tuple(perm)
        print(f'p={p}: 200 random cycles checked')
