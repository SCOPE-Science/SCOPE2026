#!/usr/bin/env python3
"""Independent finite checks of the two-agent grid generator classification.
Uses ordinary modal set-refinement; does not call the structural theorem to decide acceptance.
"""
from itertools import product
from collections import defaultdict
from math import factorial
import random


def is_ferrers(m,n,bits):
    rows = [{j for j in range(n) if (bits>>(i*n+j))&1} for i in range(m)]
    return all(x <= y or y <= x for x in rows for y in rows)


def distinct_profiles(m,n,bits):
    rows = [tuple((bits>>(i*n+j))&1 for j in range(n)) for i in range(m)]
    cols = [tuple((bits>>(i*n+j))&1 for i in range(m)) for j in range(n)]
    return len(set(rows))==m and len(set(cols))==n


def oracle(m,n,bits):
    # Iterative refinement by independently computed sets of successor classes.
    labels = [((bits>>z)&1) for z in range(m*n)]
    counts = [len(set(labels))]
    while True:
        rsets = [frozenset(labels[i*n+j] for j in range(n)) for i in range(m)]
        csets = [frozenset(labels[i*n+j] for i in range(m)) for j in range(n)]
        sigs = [(labels[i*n+j],rsets[i],csets[j]) for i in range(m) for j in range(n)]
        # Canonical IDs from first occurrence, not using any Ferrers property.
        ids = {}
        for sig in sigs:
            if sig not in ids: ids[sig] = len(ids)
        nxt = [ids[sig] for sig in sigs]
        counts.append(len(ids))
        if len(ids)==len(set(labels)):
            return counts
        labels=nxt


def mixed_core(m,n,bits):
    # Find induced 2K2; enlarge until all outside rows and columns are constant
    # on the current opposite-side core.
    B = [[(bits>>(i*n+j))&1 for j in range(n)] for i in range(m)]
    for i in range(m):
        for ii in range(i+1,m):
            for j in range(n):
                for jj in range(j+1,n):
                    if B[i][j]==B[ii][jj]!=B[i][jj]==B[ii][j]:
                        r,c={i,ii},{j,jj}
                        changed=True
                        while changed:
                            changed=False
                            for x in range(m):
                                if x not in r and len({B[x][y] for y in c})==2:
                                    r.add(x); changed=True
                            for y in range(n):
                                if y not in c and len({B[x][y] for x in r})==2:
                                    c.add(y); changed=True
                        return r,c
    return None


def verify_core_certificate(m,n,bits,core):
    if core is None:return True
    r,c=core
    B = [[(bits>>(i*n+j))&1 for j in range(n)] for i in range(m)]
    assert all({B[i][j] for j in c}=={0,1} for i in r)
    assert all({B[i][j] for i in r}=={0,1} for j in c)
    assert all(len({B[i][j] for j in c})==1 for i in range(m) if i not in r)
    assert all(len({B[i][j] for i in r})==1 for j in range(n) if j not in c)
    # Explicit equivalence E: collapse both core coordinates, keep all other
    # coordinates individually named, and retain the vertex's P color.
    labels=[(('*' if i in r else i),('*' if j in c else j),B[i][j])
            for i in range(m) for j in range(n)]
    classes=defaultdict(list)
    for z,label in enumerate(labels): classes[label].append(z)
    # Every E class must have identical sets of E classes in each modality.
    for members in classes.values():
        def succ(z, axis):
            i,j=divmod(z,n)
            return {labels[i*n+y] for y in range(n)} if axis==0 else {labels[x*n+j] for x in range(m)}
        for axis in (0,1):
            target=succ(members[0],axis)
            assert all(succ(z,axis)==target for z in members)
    assert any(len(x)>=2 for x in classes.values())
    return True


def direct_closure(m,n,bits):
    # Enumerate actual Boolean modal subalgebra (small universes only).
    assert m*n<=9
    univ=(1<<(m*n))-1
    rowm=[sum(1<<(i*n+j) for j in range(n)) for i in range(m)]
    colm=[sum(1<<(i*n+j) for i in range(m)) for j in range(n)]
    def dia(S,masks):
        ans=0
        for mask in masks:
            if S&mask: ans|=mask
        return ans
    closure={0,univ,bits,univ^bits}
    while True:
        before=len(closure)
        b=list(closure)
        for x in b:
            closure.add(univ^x)
            closure.add(dia(x,rowm));closure.add(dia(x,colm))
        b=list(closure)
        for i,x in enumerate(b):
            for y in b[i:]:closure.add(x|y);closure.add(x&y)
        if len(closure)==before:return len(closure)


def main():
    checked=0; evidence=0; core_checks=0; algebra_cases=0; size_count={}
    for m,n in product(range(1,5), repeat=2):
        if m*n>16:continue
        good=0
        for bits in range(1<<(m*n)):
            spec=oracle(m,n,bits)
            full=spec[-1]==m*n
            expect=is_ferrers(m,n,bits) and distinct_profiles(m,n,bits)
            assert full==expect,(m,n,bits,spec)
            if full:good+=1
            checked+=1
            if not is_ferrers(m,n,bits) and ((bits*197+m*13+n)%103==0):
                core=mixed_core(m,n,bits)
                assert core is not None
                verify_core_certificate(m,n,bits,core)
                core_checks+=1
            if m*n<=9 and ((bits*37+m*11+n)%149==0):
                observed=direct_closure(m,n,bits)
                assert observed==(1<<spec[-1]),(m,n,bits,observed,spec)
                algebra_cases+=1
        target=0
        if m==n:target=2*factorial(m)*factorial(n)
        if abs(m-n)==1:target=factorial(m)*factorial(n)
        assert good==target,(m,n,good,target)
        size_count[f'{m}x{n}']=good
        evidence+=1
    # Larger random matrices and planted strict staircase witnesses.
    rng=random.Random(71392026)
    random_cases=0
    for m,n in ((5,5),(5,6),(6,5),(6,6),(7,7),(8,8),(9,10)):
        for z in range(240):
            bits=rng.getrandbits(m*n)
            good=oracle(m,n,bits)[-1]==m*n
            assert good==(is_ferrers(m,n,bits) and distinct_profiles(m,n,bits))
            random_cases+=1
        if abs(m-n)<=1:
            for orientation in ((0,1) if m==n else (0,)):
                if m==n:
                    lens=[(n-1-i if orientation==0 else n-i) for i in range(m)]
                elif m==n+1:lens=[n-i for i in range(m)]
                else:lens=[m-i for i in range(m)]
                bits=sum(1<<(i*n+j) for i in range(m) for j in range(lens[i]))
                assert oracle(m,n,bits)[-1]==m*n
    print('VERIFY_OK', 'exhaustive_matrices',checked,'rectangular_parameter_cases',evidence,
          'explicit_bisimulation_core_checks',core_checks,
          'direct_boolean_algebra_closures',algebra_cases,'random_large_matrices',random_cases,
          'generator_counts',size_count)
if __name__=='__main__':main()
