#!/usr/bin/env python3
"""Reproduce nested-equivalence generator tests without external packages."""
import itertools
import math
import random


def leaves(tree):
    if isinstance(tree,int): return (tree,)
    return tuple(x for child in tree for x in leaves(child))


def shape_labeled(tree,colors):
    """Colored rooted unordered-tree type, including multiplicity."""
    if isinstance(tree,int): return ('leaf', colors[tree])
    return ('node',tuple(sorted((shape_labeled(c,colors) for c in tree),key=repr)))


def is_rigid(tree,colors):
    if isinstance(tree,int): return True
    profiles=[shape_labeled(c,colors) for c in tree]
    return all(is_rigid(c,colors) for c in tree) and len(set(profiles))==len(profiles)


def partitions(tree):
    if isinstance(tree,int): return []
    this=(tuple(leaves(tree)),)
    # all equivalence levels, coarsest through finest
    if not tree or all(isinstance(x,int) for x in tree): return [this]
    # each child has its own partition hierarchy; for a valid levelled tree
    # each child must have same level count
    ch=[partitions(c) for c in tree]
    assert len(set(map(len,ch)))==1
    levels=[this]
    for j in range(len(ch[0])):
        levels.append(tuple(block for c in ch for block in c[j]))
    return levels


def number_modal_classes(tree,colors):
    ls=leaves(tree); n=len(ls); assert set(ls)==set(range(n))
    rel=[]
    for partition in partitions(tree):
        look={v:tuple(block) for block in partition for v in block}
        rel.append(look)
    cur=list(colors)
    for t in range(n+1):
        signatures=[(cur[w],)+tuple(frozenset(cur[v] for v in rel_i[w]) for rel_i in rel) for w in range(n)]
        idx={v:k for k,v in enumerate(set(signatures))}
        nxt=[idx[t] for t in signatures]
        if len(set(nxt))==len(set(cur)):return len(set(cur))
        cur=nxt
    raise AssertionError('refinement should have stabilized')


def regular(branches):
    z=0
    def build(i):
        nonlocal z
        if i==0:
            w=z; z+=1; return w
        return tuple(build(i-1) for j in range(branches[i-1]))
    return build(len(branches))


def count_formula(q,branches):
    A=q; factor=1;n=math.prod(branches); nodes=n
    for b in branches:
        nodes//=b
        factor*=math.factorial(b)**nodes
        A=math.comb(A,b) if A>=b else 0
    return A*factor


def standard_algebra_size(tree,colors):
    n=len(colors);V=(1<<n)-1
    rel=[]
    for partition in partitions(tree):
        masks=[sum(1<<i for i in block) for block in partition]
        rel.append(masks)
    initial={0,V}
    for val in set(colors):initial.add(sum(1<<i for i,x in enumerate(colors) if x==val))
    known=set(initial)
    while True:
        before=len(known)
        added={V^x for x in known}
        for a in tuple(known):
            for b in tuple(known):
                added.add(a&b)
            for prt in rel:
                added.add(sum((m for m in prt if m&a),0) & V)
        known|=added
        if len(known)==before:return len(known)


def grouped_examples():
    # Nonuniform, but all leaves have the same hierarchy depth.
    return [
        ((0,1),(2,3,4)),
        ((0,),(1,2)),
        (((0,1),(2,)),((3,),(4,5))),
        (((0,1),(2,3)),((4,5),(6,))),
        (((0,),(1,2)),((3,4),(5,))),
        (((0,1,2),(3,)),((4,),(5,6))),
    ]


def run():
    n_reg=0;n_non=0;total=0;n_direct=0
    for b,q in [((2,),2),((3,),3),((2,2),2),((2,2),3),((2,2),4),((3,2),4),((2,3),4),((2,2,2),3)]:
        tree=regular(b);n=math.prod(b);seen=0
        for col in itertools.product(range(q),repeat=n):
            result=number_modal_classes(tree,col)==n
            assert result==is_rigid(tree,col),('regular',b,q,col)
            seen+=result;total+=1
        assert seen==count_formula(q,b),(b,q,seen,count_formula(q,b))
        n_reg+=1
    for tree in grouped_examples():
        n=len(leaves(tree));q=3
        for col in itertools.product(range(q),repeat=n):
            result=number_modal_classes(tree,col)==n
            assert result==is_rigid(tree,col),(tree,col,result)
            n_non+=1
    rng=random.Random(20261010)
    for tree in grouped_examples():
        n=len(leaves(tree));
        for j in range(55):
            col=tuple(rng.randrange(3) for _ in range(n))
            classes=number_modal_classes(tree,col)
            closure=standard_algebra_size(tree,col)
            assert closure==2**classes,(tree,col,closure,classes)
            n_direct+=1
    print('VERIFY_OK regular_exhaustive_cases',n_reg,'regular_colorings',total,
          'nonregular_colorings',n_non,'direct_modal_closures',n_direct,
          'binary_three_level',count_formula(3,(2,2,2)))
if __name__=='__main__':run()

def refine_depth(tree,colors):
    n=len(colors)
    rel=[]
    for partition in partitions(tree):
        look={v:tuple(block) for block in partition for v in block}
        rel.append(look)
    sig=list(colors)
    for t in range(n+1):
        if len(set(sig))==n:return t
        k=[(sig[w],)+tuple(frozenset(sig[v] for v in R[w]) for R in rel) for w in range(n)]
        c={x:j for j,x in enumerate(set(k))}
        new=[c[x] for x in k]
        if len(set(new))==len(set(sig)):return None
        sig=new
    raise AssertionError('no stabilization')

def sharp_family():
    reps=[(0,),(1,),(2,)]
    for h in range(1,8):
        reps=[reps[(j+1)%3]+reps[(j+2)%3] for j in range(3)]
        colors=reps[0]
        tree=regular((2,)*h)
        d=refine_depth(tree,colors)
        assert d==h-1,(h,d)
        assert is_rigid(tree,colors)
    return 7

if __name__=='__main__':
    print('SHARP_DEPTH_OK levels',sharp_family())
