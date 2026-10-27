"""Independent finite check: bounded maps of ancestor trees to reflexive chains."""
from itertools import product
from math import comb, prod


def shapes_upto(N):
    by_size={1:[()]}
    catalog=[(1,())]
    for n in range(2,N+1):
        result=set()
        def extend(left,start,selected):
            if left==0:
                result.add(tuple(selected));return
            for j in range(start,len(catalog)):
                weight,s=catalog[j]
                if weight>left:break
                selected.append(s)
                extend(left-weight,j,selected)
                selected.pop()
        extend(n-1,0,[])
        by_size[n]=sorted(result,key=repr)
        catalog.extend((n,s) for s in by_size[n])
    return by_size

def counts(shape):
    cs=[counts(s) for s in shape]
    if not cs:return (1,1)
    b=1+prod(x[0] for x in cs)
    a=prod(x[1] for x in cs)+prod(x[0] for x in cs)
    return b,a

def descendant_arrays(shape):
    ancestors=[]
    def build(s,parent_anc):
        v=len(ancestors)
        ancestors.append(parent_anc+(v,))
        for child in s:build(child,ancestors[v])
    build(shape,())
    n=len(ancestors)
    return [tuple(j for j,a in enumerate(ancestors) if i in a) for i in range(n)]

def direct(shape,k):
    desc=descendant_arrays(shape)
    n=len(desc)
    total=0
    for vals in product(range(k),repeat=n):
        if any(vals[v]>vals[w] for v in range(n) for w in desc[v]):continue
        if any(not any(vals[w]==target for w in desc[v])
               for v in range(n) for target in range(vals[v],k)):continue
        total+=1
    return total

by_size=shapes_upto(8)
print('SIZE SHAPES MAX_2CHAIN MAX_3CHAIN PATH_2 PATH_3')
for n,ss in by_size.items():
    pair=[counts(s) for s in ss]
    print(n,len(ss),max(x[0] for x in pair),max(x[1] for x in pair),n,1+comb(n,2))
    if n<=7:
        for s,(b,a) in zip(ss,pair):
            assert direct(s,2)==b,(n,s,'2',b,direct(s,2))
            assert direct(s,3)==a,(n,s,'3',a,direct(s,3))
# Sharpness includes every smaller rooted isomorphism class and unique first maximizers.
for n in range(1,6):
    assert max(counts(t)[0] for t in by_size[n])==n
for n in range(1,7):
    assert max(counts(t)[1] for t in by_size[n])==1+comb(n,2)
for n,coordinate,winner in ((6,0,7),(7,1,25)):
    maximizing=[t for t in by_size[n] if counts(t)[coordinate]==winner]
    assert len(maximizing)==1, (n,maximizing)
    assert winner>(n if coordinate==0 else 1+comb(n,2))
print('SHARP_THRESHOLDS_AND_UNIQUENESS_PASS')
assert [len(by_size[n]) for n in range(1,9)]==[1,1,2,4,9,20,48,115]
for k in range(2,10):
    limbs3=(((),),)
    limbs4=((((),),),)
    # limbs with 3 and 4 vertices including limb root
    c3=(((),),)
    c4=((((),),),)
    for r in range(3):
        children=[c3]*k
        for j in range(r):children[j]=c4
        tree=tuple(children)
        n=3*k+1+r
        expected=(4**(k-r)*7**r)+(3**(k-r)*4**r)
        assert counts(tree)[1]==expected
        assert expected>1+comb(n,2)
for k in range(2,10):
    c2=((),)
    c3=(((),),)
    for r in range(2):
        children=[c2]*k
        for j in range(r):children[j]=c3
        n=2*k+1+r
        expected=1+(2**(k-r)*3**r)
        assert counts(tuple(children))[0]==expected
        if n>=6:assert expected>n
print('ALL_CHECKS_PASS')
