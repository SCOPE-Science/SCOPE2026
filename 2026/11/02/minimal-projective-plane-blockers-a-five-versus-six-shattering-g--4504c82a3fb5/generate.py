#!/usr/bin/env python3
"""Exact small projective-plane minimal-blocking-set experiment."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path

def projective(q):
    raw=[(a,b,c) for a in range(q) for b in range(q) for c in range(q) if a or b or c]
    def normal(t):
        f=next(x for x in t if x)
        u=pow(f,-1,q)
        return tuple(x*u%q for x in t)
    points=sorted(set(map(normal,raw)))
    line_sets=sorted(set(frozenset(i for i,(x,y,z) in enumerate(points)
                          if (a*x+b*y+c*z)%q==0) for a,b,c in points),key=lambda a:tuple(sorted(a)))
    line_masks=tuple(sorted(sum(1<<i for i in line) for line in line_sets))
    return points,line_masks

def blockers(n,lines):
    return [a for a in range(1<<n)
            if all(a&l for l in lines)
            and all(any((a&l)==(1<<p) for l in lines) for p in range(n) if a>>p&1)]

def trace_mask(concepts, support):
    queries=[i for i in range(13) if support>>i&1]
    return {sum((bool(C>>i&1))<<j for j,i in enumerate(queries)) for C in concepts}

def spectrum(concepts,n,k):
    out=Counter()
    for S in combinations(range(n),k):
        pat={sum(((C>>i)&1)<<j for j,i in enumerate(S)) for C in concepts}
        out[len(pat)]+=1
    return dict(sorted(out.items()))

def triangles(lines):
    out=set()
    for a,b,c in combinations(lines,3):
        if a&b&c:continue
        T=(a|b|c) & ~((a&b)|(a&c)|(b&c))
        assert T.bit_count()==6
        out.add(T)
    return out

def tree_for(concepts,n,depth):
    masks=[sum((1<<j) for j,C in enumerate(concepts) if C>>i&1) for i in range(n)]
    allmask=(1<<len(concepts))-1
    @lru_cache(None)
    def rank(S):
        best=0
        for q in masks:
            a=S&q;b=S&~q
            if a and b:
                best=max(best,1+min(rank(a),rank(b)))
        return best
    R=rank(allmask)
    print('RANK',R,'STATES',rank.cache_info().currsize,flush=True)
    assert R>=depth
    def build(S,d):
        if d==0:
            j=(S&-S).bit_length()-1
            return {'witness':concepts[j]}
        options=[]
        for i,q in enumerate(masks):
            a=S&q;b=S&~q
            if a and b and rank(a)>=d-1 and rank(b)>=d-1:
                options.append((abs(a.bit_count()-b.bit_count()),i,a,b))
        _,i,a,b=min(options)
        return {'query':i,'zero':build(b,d-1),'one':build(a,d-1)}
    return build(allmask,depth)

def main():
    p3,L3=projective(3)
    p2,L2=projective(2)
    C3=blockers(13,L3)
    C2=blockers(7,L2)
    print('POINTS',len(p3),len(p2),'LINES',len(L3),len(L2))
    print('MINIMAL3',len(C3),dict(Counter(C.bit_count() for C in C3)))
    print('MINIMAL2',len(C2),dict(Counter(C.bit_count() for C in C2)))
    assert len(C3)==247 and Counter(C.bit_count() for C in C3)=={4:13,6:234}
    assert len(C2)==7 and all(C.bit_count()==3 for C in C2)
    T=triangles(L3)
    assert T==set(C for C in C3 if C.bit_count()==6)
    print('TRIANGLES',len(T))
    for k in (3,4,5,6):
        print('SPECTRUM',k,spectrum(C3,13,k),flush=True)
    assert spectrum(C3,13,4)=={15:13,16:702}
    assert spectrum(C3,13,5)=={29:117,31:468,32:702}
    assert spectrum(C3,13,6)=={56:468,57:78,60:936,61:234}
    q5=Counter(C^(1<<i) for C in T for i in range(13) if C>>i&1)
    assert len(q5)==702 and set(q5.values())=={2}
    for ss in combinations(range(13),5):
        sm=sum(1<<i for i in ss)
        assert (len(trace_mask(C3,sm))==32)==(sm in q5)
    for k in (2,3):
        print('FANO_SPECTRUM',k,spectrum(C2,7,k))
    assert spectrum(C2,7,2)=={4:21}
    assert spectrum(C2,7,3)=={4:7,7:28}
    tree=tree_for(C3,13,6)
    obj={'schema_version':1,'q':3,'points':p3,'line_masks':L3,'minimal_blocker_masks':C3,'tree_depth':6,'adaptive_tree':tree,
         'expected_spectrum':{'3':{8:286},'4':{15:13,16:702},'5':{29:117,31:468,32:702},'6':{56:468,57:78,60:936,61:234}}}
    dest=Path(__file__).with_name('certificate.json')
    dest.write_text(json.dumps(obj,separators=(',',':'),ensure_ascii=False)+'\n',encoding='utf8')
    print('CERTIFICATE',dest,len(dest.read_bytes()),flush=True)
if __name__=='__main__':main()
