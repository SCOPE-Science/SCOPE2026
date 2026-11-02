#!/usr/bin/env python3
"""Exact four-round first-order type computation for binary orthogonal polar graphs.
The tuples are represented by their first-independent basis, quadratic Gram
matrix and coordinates. All extension counts are exact Gaussian character sums."""
from functools import lru_cache

TYPE_IDS={}
def keyid(signature):
    if signature not in TYPE_IDS: TYPE_IDS[signature]=len(TYPE_IDS)
    return TYPE_IDS[signature]

def oddpop(x): return x.bit_count()&1

def bilinear(x,y,rows):
    out=0
    while x:
        i=(x&-x).bit_length()-1
        out ^= oddpop(rows[i]&y)
        x &= x-1
    return out

def quadratic(x,rows):
    out=0
    while x:
        i=(x&-x).bit_length()-1
        x&=x-1
        out ^= oddpop(rows[i]&x)
    return out

class Model:
    def __init__(self,r,eps):
        self.r,self.eps=r,eps
        self.color_calls=0
        self.states={}

    @lru_cache(None)
    def ext(self,state):
        vecs,rows=state
        m=len(rows)
        ch=set()
        W=range(1<<m)
        in_span=[z for z in W if z!=0 and quadratic(z,rows)==0]
        for z in in_span:
            ch.add((vecs+(z,),rows))
        for t in W:
            zsum=sum(1 if oddpop(t&a)^quadratic(a,rows)==0 else -1 for a in W)
            numerator=(1<<(2*self.r))+self.eps*(1<<self.r)*zsum
            assert numerator%(1<<(m+1))==0,(state,t,numerator)
            total=numerator>>(m+1)
            inside=0
            for z in [0]+in_span:
                if all(bilinear(z,1<<i,rows)==((t>>i)&1) for i in range(m)):
                    inside+=1
            if total > inside:
                new_rows=tuple(rows[i] | (((t>>i)&1)<<m) for i in range(m))+(t,)
                assert all(not (new_rows[i]>>i)&1 for i in range(m+1))
                assert all(((new_rows[i]>>j)&1)==((new_rows[j]>>i)&1) for i in range(m+1) for j in range(m+1))
                ch.add((vecs+(1<<m,),new_rows))
            else:
                assert total==inside,(self.r,self.eps,state,t,total,inside)
        return tuple(sorted(ch))

    @lru_cache(None)
    def col(self,state,remain):
        self.color_calls+=1
        vecs,rows=state
        atom=tuple(0 if vecs[i]==vecs[j] else (1 if bilinear(vecs[i],vecs[j],rows)==0 else 2) for i in range(len(vecs)) for j in range(i+1,len(vecs)))
        if remain==0: return keyid((0,atom))
        ch={self.col(child,remain-1) for child in self.ext(state)}
        return keyid((remain,atom,tuple(sorted(ch))))

    def root(self,q):
        return self.col(((),()),q)

if __name__=='__main__':
    for depth in (3,4):
        roots={}
        for r in range(2,9):
            for eps in (+1,-1):
                mo=Model(r,eps)
                roots[(r,eps)]=mo.root(depth)
        classes={u:frozenset(x for x,v in roots.items() if v==u) for u in set(roots.values())}
        expected=[]
        if depth==3:
            expected=[frozenset({(2,-1)}), frozenset(set(roots)-{(2,-1)})]
        else:
            expected=[frozenset({(2,-1)}),frozenset({(2,+1)}),frozenset({(3,-1)}),frozenset(set(roots)-{(2,-1),(2,+1),(3,-1)})]
        assert set(classes.values())==set(expected),(depth,classes)
        print('RANK_CLASSES_OK',depth,'class_count',len(classes))
        for k,group in enumerate(sorted(classes.values(),key=lambda z:(len(z),min(z))),1):
            print(' CLASS',k,'members',sorted(group))
    # Once r >= 5, every independent fourth-vector extension exists.
    for r in range(5,17):
        for m in range(0,4):
            bound=2**(2*r-m-1)-2**(r-1)
            assert bound>2**m
    print('UNIFORM_EXTENSION_BOUND_OK r>=5 and m<=3')
    print('FOUR_ROUND_CLASSIFICATION_OK')
    print('VERIFY_OK')
