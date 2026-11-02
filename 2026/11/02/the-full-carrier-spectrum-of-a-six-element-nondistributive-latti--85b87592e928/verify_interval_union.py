#!/usr/bin/env python3
"""Two independent finite checks of a six-element unary congruence lattice."""
from itertools import combinations, product

def partitions(n):
    out=[0]*n
    def rec(i,k):
        if i==n:
            yield tuple(out)
            return
        for v in range(k+2):
            out[i]=v
            yield from rec(i+1,max(k,v))
    yield from rec(1,0)

def canon(seq):
    code={}
    result=[]
    for x in seq:
        if x not in code:code[x]=len(code)
        result.append(code[x])
    return tuple(result)

def pair_rel(n):
    a=list(range(n));a[1]=a[0]
    b=list(range(n));b[3]=b[2]
    d=list(range(n));d[1]=d[0];d[3]=d[2]
    g=[i%2 for i in range(n)]
    for i in range(4,n):g[i]=0
    return tuple(map(canon,(a,b,d,g)))

def ops(n):
    U=[0,2]+list(range(4,n)); V=[1,3]
    blocks=[(0,1),(2,3)]+[(i,) for i in range(4,n)]
    for C in (U,V):
        for p,q in combinations(C,2):
            for bits in product((0,1),repeat=len(blocks)):
                if all(z==bits[0] for z in bits):continue
                o=[-1]*n
                for block,bit in zip(blocks,bits):
                    for x in block:o[x]=(p,q)[bit]
                o=tuple(o)
                assert len(set(o))==2
                yield o

def preserves(f,theta):
    return all(theta[i]!=theta[j] or theta[f[i]]==theta[f[j]]
               for i in range(len(theta)) for j in range(i))

def wanted(n):
    a,b,d,g=pair_rel(n)
    return {canon(range(n)),a,b,d,g,(0,)*n}

def direct(n):
    F=list(ops(n))
    good={theta for theta in partitions(n) if all(preserves(f,theta) for f in F)}
    expect=wanted(n)
    assert good==expect, ('direct',n,good^expect)
    expected_count=(len([0,2]+list(range(4,n)))*(len([0,2]+list(range(4,n)))-1)//2+1)*(2**(n-2)-2)
    assert len(F)==expected_count
    print(f'DIRECT n={n} maps={len(F)} congruences={len(good)} verified')

def independent(n):
    # For a fixed output pair (p,q), use only images and the coarsest
    # admissible kernel, computed by joining all target relations separating p,q.
    target=wanted(n)
    nodes=list(partitions(n))
    defects=[]
    for theta in nodes:
        preserved=True
        for p,q in combinations(range(n),2):
            if theta[p]==theta[q]:continue
            parent=list(range(n))
            def root(x):
                while parent[x]!=x:
                    parent[x]=parent[parent[x]]
                    x=parent[x]
                return x
            for relation in target:
                if relation[p]!=relation[q]:
                    for x in range(n):
                        for y in range(x):
                            if relation[x]==relation[y]:
                                parent[root(x)]=root(y)
            classes=[root(x) for x in range(n)]
            if any(theta[x]==theta[y] and classes[x]!=classes[y] for x in range(n) for y in range(x)):
                preserved=False;break
        if preserved and theta not in target:defects.append(theta)
        if not preserved and theta in target:defects.append(theta)
    assert not defects,('independent',n,defects[:3])
    print(f'KERNEL_TEST n={n} partitions={len(nodes)} congruences=6 verified')

if __name__=='__main__':
    for n in range(4,8):direct(n)
    for n in range(4,9):independent(n)
    print('VERIFY_OK')
