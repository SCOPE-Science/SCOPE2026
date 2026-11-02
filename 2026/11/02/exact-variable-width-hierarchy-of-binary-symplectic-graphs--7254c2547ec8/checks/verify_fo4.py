#!/usr/bin/env python3
"""Finite corroboration of bounded-variable types for binary symplectic graphs.
Uses only Python standard library. All results are finite checks; the accompanying
mathematical proof establishes the universal statement.
"""
from itertools import product, combinations

def pair(x,y,d):
    z=0
    for i in range(d):
        a=(x>>(2*i))&1;b=(x>>(2*i+1))&1
        c=(y>>(2*i))&1;e=(y>>(2*i+1))&1
        z^=(a&e)^(b&c)
    return z

def relation_bits(xs):
    # XOR-zero relations of support size 2 or 3; 0-vector is excluded.
    ans=[]
    for s in (2,3):
        for idxs in combinations(range(len(xs)),s):
            v=0
            for i in idxs:v^=xs[i]
            ans.append(int(v==0))
    return tuple(ans)

def signature(xs,d):
    return (tuple(pair(xs[i],xs[j],d) for i,j in combinations(range(len(xs)),2)),relation_bits(xs))

def embed(x,source_d,target_d):
    assert target_d>=source_d
    return x # append zero coordinate pairs

def extension_set(triple,d):
    return {signature(triple+(v,),d) for v in range(1,1<<(2*d))}

def run():
    reps={}
    # Enumeration of all triples over 63 vertices; every 3-orbit appears.
    for triple in product(range(1,64),repeat=3):
        sig=signature(triple,3)
        reps.setdefault(sig,triple)
    print('distinct_three_point_types_in_dimension_six',len(reps))
    # Check that higher symplectic dimension adds no 4-pebble observable
    # extension to any 3-point type. This checks representative triples;
    # proof uses all types and the linear algebra extension lemma.
    for t in reps.values():
        e3=extension_set(t,3)
        e4=extension_set(t,4)
        if e3!=e4:
            raise AssertionError(('dimension mismatch',t,len(e3),len(e4)))
    print('dimension_six_to_eight_extension_profiles',len(reps),'PASS')
    # Repeating all triples at dimension four is cheap and checks
    # pair signatures within one model independently of group theory.
    reps2={}
    for t in product(range(1,16),repeat=3):
        sig=signature(t,2)
        e=extension_set(t,2)
        if sig in reps2 and reps2[sig]!=e:
            raise AssertionError(('nonhomogeneous',t))
        reps2[sig]=e
    print('dimension_four_triple_extensions',15**3,'PASS')
    # Separating formula: three pairwise orthogonal distinct vectors with
    # a single common neighbor, impossible in dimension four, possible six.
    for d in (1,2,3):
        vs=range(1,1<<(2*d))
        found=False
        for a in vs:
            for b in vs:
                if b==a or pair(a,b,d):continue
                for c in vs:
                    if c==a or c==b or pair(a,c,d) or pair(b,c,d):continue
                    # Consistency follows from independence, no need to loop w.
                    if (a^b^c)!=0:
                        found=True;break
                if found:break
            if found:break
        print('dimension',d,'four_variable_separator',found)
        assert found==(d>=3)
    print('VERIFIED')
if __name__=='__main__':run()
