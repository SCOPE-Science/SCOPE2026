#!/usr/bin/env python3
"""Standalone finite checks for the binary length-two palindromic-duplication congruence."""
from itertools import product

def duplicate(word, index):
    assert 0 <= index < len(word)-1
    return word[:index+2] + word[index+1] + word[index] + word[index+2:]

def signature(w):
    if not w:
        return ('empty',)
    if len(w) == 1:
        return ('singleton',w[0])
    a=w[0]
    k=next((i for i,letter in enumerate(w) if letter!=a),len(w))
    kind = 'constant' if k==len(w) else ('one' if k==1 else ('even' if k%2==0 else 'odd'))
    return (len(w)%2,a,kind)

# Two explicit directed branches prove 010 and 011 have a common descendant.
branch0=['010','01001','0110001','011010001','01101100001']
branch1=['011','01101','0110101','011011001','01101100001']
for branch in (branch0,branch1):
    for x,y in zip(branch,branch[1:]):
        assert y in {duplicate(x,i) for i in range(len(x)-1)},(x,y)
assert branch0[-1]==branch1[-1]
# Replacing 0 by 1 and 1 by 0 proves the second identity.
for b in (branch0,branch1):
    cb=[w.translate(str.maketrans('01','10')) for w in b]
    for x,y in zip(cb,cb[1:]):
        assert y in {duplicate(x,i) for i in range(len(x)-1)}

# Every legal expansion preserves all claimed classification invariants.
for n in range(2,14):
    for bits in product('01',repeat=n):
        w=''.join(bits)
        for i in range(n-1):
            assert signature(w)==signature(duplicate(w,i)),(w,i)

# Finite graph has edges across lengths of the same parity. The bound 14 is
# used solely to check the local classification, not to prove its infinite form.
length_limit=14
words=[''.join(bits) for n in range(2,length_limit+1) for bits in product('01',repeat=n)]
word_ids={w:i for i,w in enumerate(words)}
parent=list(range(len(words)))

def root(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]]
        i=parent[i]
    return i

def merge(i,j):
    ri,rj=root(i),root(j)
    if ri!=rj:
        parent[ri]=rj

edge_count=0
for w,i in word_ids.items():
    if len(w)+2>length_limit:
        continue
    for j in range(len(w)-1):
        merge(i,word_ids[duplicate(w,j)])
        edge_count+=1
for n in range(2,10):
    groups={}
    for bits in product('01',repeat=n):
        w=''.join(bits)
        groups.setdefault(signature(w),set()).add(root(word_ids[w]))
    assert all(len(v)==1 for v in groups.values()),(n,groups)
    assert len(groups)==(4 if n==2 else 6 if n==3 else 8),n
# Count all finite canonical signatures, including the empty word and singleton states.
all_signatures=set()
for n in range(10):
    for letters in product('01',repeat=n):
        all_signatures.add(signature(''.join(letters)))
assert len(all_signatures)==19, all_signatures
for n in range(10):
    assert len({signature(''.join(v)) for v in product('01',repeat=n)}) == (1 if n==0 else 2 if n==1 else 4 if n==2 else 6 if n==3 else 8)
print(f'VERIFY_OK primitive_join_paths=4 prefix_signatures_preserved_through_length=13 graph_limit={length_limit} graph_vertices={len(words)} graph_edges={edge_count} exact_component_slices=2..9 quotient_size=19')
