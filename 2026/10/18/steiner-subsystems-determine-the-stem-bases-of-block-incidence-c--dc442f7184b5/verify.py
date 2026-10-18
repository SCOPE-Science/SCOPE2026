#!/usr/bin/env python3
"""Standalone finite verification of Steiner-design incidence stem bases."""
from itertools import combinations
from math import comb

def pg_blocks(d):
    vs=range(1,1<<d)
    return sorted({frozenset((a,b,a^b)) for a,b in combinations(vs,2)},key=lambda z:tuple(sorted(z)))

def affine_blocks():
    pts=[(x,y) for x in range(3) for y in range(3)]
    idx={p:i for i,p in enumerate(pts)}
    return sorted({frozenset(idx[((x+j*u)%3,(y+j*w)%3)] for j in range(3))
                  for x,y in pts for u,w in ((1,0),(0,1),(1,1),(1,2))}, key=lambda z:tuple(sorted(z)))

def graph_context(blocks,pts):
    indices={p:i for i,p in enumerate(pts)}
    rows=[sum(1<<indices[p] for p in block) for block in blocks]
    n=len(pts); full=(1<<n)-1
    def closure(mask):
        containing=[b for b in rows if (b & mask)==mask]
        if not containing:return full
        result=full
        for b in containing:result &= b
        return result
    return n,rows,closure

def exhaustive_pseudo(n,closure):
    ps=[]
    clos=[]
    for k in range(n+1):
        for ix in combinations(range(n),k):
            mask=sum(1<<i for i in ix)
            c=closure(mask)
            if c==mask:continue
            if all((p & mask)!=p or (pc & mask)==pc for p,pc in zip(ps,clos)):
                ps.append(mask); clos.append(c)
    return ps,clos

def test_case(label,pts,blocks,expected,counting=True):
    n,rows,cl=graph_context(blocks,pts)
    assert len(rows)==n*(n-1)//6, (label,n,len(rows))
    for a,b in combinations(range(n),2):
        assert sum((1<<a|1<<b)&row==(1<<a|1<<b) for row in rows)==1
    ps,cs=exhaustive_pseudo(n,cl)
    assert len(ps)==expected,(label,len(ps),expected)
    pairs=[p for p in ps if p.bit_count()==2]
    assert len(pairs)==comb(n,2)
    higher=[p for p in ps if p.bit_count()>2]
    for m in higher:
        assert m.bit_count()>=7 and cl(m)==(1<<n)-1
    if counting:
        full=(1<<n)-1
        subsets_tested=0
        for mask in range(1<<n):
            target=cl(mask)
            cur=mask
            while True:
                new=cur
                for premise,consequence in zip(ps,cs):
                    if premise&cur==premise:new |= consequence
                if new==cur:break
                cur=new
            assert cur==target,(label,mask,target,cur)
            subsets_tested+=1
    else:subsets_tested=0
    print('CASE_OK', label, 'points',n,'blocks',len(rows),'pseudo_intents',len(ps),
          'pairs',len(pairs),'larger',len(higher),'sizes',sorted({p.bit_count() for p in higher}),
          'subset_replays',subsets_tested)
    return ps,higher

def gaussian(n,k):
    num=den=1
    for j in range(k):num*=2**n-2**j; den*=2**k-2**j
    assert num%den==0
    return num//den

if __name__=='__main__':
    for d in (3,4):
        pts=list(range(1,1<<d))
        ps,extra=test_case('PG_F2_dimension_'+str(d),pts,pg_blocks(d),comb(len(pts),2)+(gaussian(d,3) if d>=4 else 0))
        if d==4:
            assert len(extra)==15
            assert all(p.bit_count()==7 for p in extra)
    test_case('Affine_plane_F3_dim2',list(range(9)),affine_blocks(),comb(9,2))
    assert gaussian(4,3)==15 and gaussian(5,3)==155 and gaussian(6,3)==1395
    print('VERIFY_OK exhaustive_STS7_STS9_STS15 Gaussian=[15,155,1395]')
