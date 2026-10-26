"""Reproducible finite checks for a structural squarefree-arch theorem.
Only stdlib is needed. The infinite proof is mathematical, not enumerative.
"""
from itertools import permutations,product

def squarefree(word):
    n=len(word)
    return all(word[i:i+p]!=word[i+p:i+2*p]
               for p in range(1,n//2+1) for i in range(n-2*p+1))

def extend_squarefree(word,letter):
    v=word+letter
    return all(v[-2*p:-p]!=v[-p:] for p in range(1,len(v)//2+1))

def greedy_arches(word):
    arches=[]; start=0; seen=set()
    for i,c in enumerate(word):
        seen.add(c)
        if len(seen)==3:
            arches.append(word[start:i+1]);start=i+1;seen=set()
    return arches,word[start:]

def subsequence(v,w):
    j=0
    for c in w:
        if j<len(v) and c==v[j]:j+=1
    return j==len(v)

# A four-letter greedy arch has the form abac, with all symbols distinct.
long_arches={a+b+a+c for a,b,c in permutations('012')}
assert len(long_arches)==6
base='0102'
possible=[base]
for k in range(1,5):
    if k>1:
        possible=[s+t for s in possible for t in long_arches if squarefree(s+t)]
    expect={1:[base],2:['01021012'],3:['010210120102'],4:[]}[k]
    assert sorted(possible)==expect,(k,possible)

# Exact finite check through n=19, with an independently computed universality index.
front=['']
size_at_18=0; example=None; total19=0
for n in range(1,20):
    front=[s+c for s in front for c in '012' if extend_squarefree(s,c)]
    for s in front:
        arches,residue=greedy_arches(s)
        assert len(residue)<=3
        assert all(3<=len(a)<=4 for a in arches)
        assert not any(all(len(a)==4 for a in arches[i:i+4]) for i in range(len(arches)-3))
        if n==19: assert len(arches)>=5
        if n==18 and len(arches)==4:
            example=s; size_at_18+=1
    if n==19:total19=len(front)
assert total19==1830 and size_at_18>0
w=example
for k in range(1,6):
    yes=all(subsequence(''.join(v),w) for v in product('012',repeat=k))
    assert yes==(k<=4),(w,k,yes)
for s in front:
    assert all(subsequence(''.join(v),s) for v in product('012',repeat=5))
assert squarefree('010210120102')
print('SQUAREFREE_ARCH_RIGIDITY_PASS',f'n19={total19}',f'n18_index4_witness={w}',
      f'n18_index4_count={size_at_18}')
