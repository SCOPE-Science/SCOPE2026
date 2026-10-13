#!/usr/bin/env python3
"""Finite matrix/domain enumerations for partial inner maps."""
from itertools import product
from collections import Counter


def binary_matrix(a, b, n):
    out = []
    for i in range(n):
        row, v = 0, a[i]
        for j in range(n):
            if (v >> j) & 1:
                row ^= b[j]
        out.append(row)
    return tuple(out)


def enumerate_binary(n):
    matrices = list(product(range(1 << n), repeat=n))
    size = len(matrices)
    index = {a:i for i,a in enumerate(matrices)}
    allmask = (1 << size) - 1
    first = []
    for E in matrices:
        domain = 0
        for i, A in enumerate(matrices):
            if binary_matrix(E,A,n)==A and binary_matrix(A,E,n)==A:
                domain |= 1 << i
        first.append(domain)
    gens=set(first)
    seen={allmask}
    frontier=[allmask]
    while frontier:
        old=frontier.pop()
        for d in gens:
            v=old&d
            if v not in seen:
                seen.add(v);frontier.append(v)
    # Separate coordinate-subspace enumerator via span closure.
    vectors=list(range(1<<n))
    subspaces=[]
    for mask in range(1 << len(vectors)):
        if not (mask&1): continue
        members=[v for v in vectors if (mask>>v)&1]
        if all((mask>>(a^b))&1 for a in members for b in members):
            subspaces.append(mask)
    proper=[s for s in subspaces if s not in (1, (1 << (1<<n))-1)]
    rect=set()
    for U in proper:
        for W in proper:
            d=0
            for i,A in enumerate(matrices):
                # output each column lies in U; each w in W mapped to zero
                if not all((U >> sum(((A[r]>>col)&1)<<r for r in range(n)))&1 for col in range(n)):
                    continue
                ok=True
                for w in vectors:
                    if (W>>w)&1:
                        z=0
                        for r in range(n):
                            if ((A[r]&w).bit_count()&1): z |= (1 << r)
                        if z: ok=False; break
                if ok:d |= 1<<i
            rect.add(d)
    rect|={1,allmask} # zero matrix is zero-index
    assert len(rect)==2+len(proper)**2, (n,len(rect),len(proper))
    assert seen==rect, (n,len(seen),len(rect),len(seen^rect))
    sqzero=0
    for domain in seen:
        members=[matrices[i] for i in range(size) if (domain>>i)&1]
        if all(binary_matrix(A,B,n)==(0,)*n for A in members for B in members):
            sqzero+=1
    expected_sq=1+sum(sum(1 for U in proper if (U & W)==U) for W in proper)
    assert sqzero==expected_sq
    sizes=Counter(x.bit_count() for x in seen)
    print(f'n={n},q=2, matrix_elements={size}, nontrivial_subspaces={len(proper)}, domains={len(seen)}, square_zero_domains={sqzero}, sizes={dict(sorted(sizes.items()))}')


def enumerate_ternary_n2():
    q,n=3,2
    matrices=list(product(range(q),repeat=n*n))
    def mul(A,B):return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))
    names={A:i for i,A in enumerate(matrices)}
    gen=[]
    for e in matrices:
        mask=0
        for idx,a in enumerate(matrices):
            if mul(e,a)==a==mul(a,e):mask |=1<<idx
        gen.append(mask)
    seen={(1<<len(matrices))-1};new=list(seen)
    while new:
        x=new.pop()
        for d in gen:
            v=x&d
            if v not in seen:seen.add(v);new.append(v)
    assert len(seen)==2+(q+1)**2
    print(f'n=2,q=3, matrix_elements={len(matrices)}, domains={len(seen)}, sizes={dict(sorted(Counter(x.bit_count() for x in seen).items()))}')



def verify_full_partial_monoid_binary_two():
    n=2
    mats=list(product(range(1<<n),repeat=n)); idx={a:i for i,a in enumerate(mats)}
    idm=tuple(1<<i for i in range(n))
    gens=set()
    for g in mats:
        for h in mats:
            e=binary_matrix(g,h,n)
            dom=[a for a in mats if binary_matrix(e,a,n)==a==binary_matrix(a,e,n)]
            out=[-1]*len(mats)
            for a in dom:
                out[idx[a]]=idx[binary_matrix(binary_matrix(h,a,n),g,n)]
            gens.add(tuple(out))
    seen=set(gens)
    seen.add(tuple(range(len(mats))))
    todo=list(seen)
    def compose(f,g):return tuple(-1 if a<0 else g[a] for a in f)
    while todo:
        f=todo.pop()
        for g in tuple(seen):
            for c in (compose(f,g),compose(g,f)):
                if c not in seen:
                    seen.add(c);todo.append(c)
    ids=[p for p in seen if all(y<0 or x==y for x,y in enumerate(p))]
    assert len(ids)==11
    print('Full partial inner monoid n=2 q=2:',len(seen),'elements,',len(ids),'idempotents')

if __name__=='__main__':
    enumerate_binary(2)
    enumerate_binary(3)
    enumerate_ternary_n2()
    verify_full_partial_monoid_binary_two()
    print('VERIFY_OK')
