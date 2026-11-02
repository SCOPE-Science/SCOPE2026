#!/usr/bin/env python3
"""Self-contained exact lower-bound and construction checker for ternary length-five palindromes.
Run: python3 verify.py [optional-path-to-certificates.json]
Uses the standard library only. The proof is the degree/cut dual argument in RESULT.md.
"""
import itertools,json,sys
from collections import Counter
from pathlib import Path


def patterns():
    return [''.join(trip)+trip[1]+trip[0] for trip in itertools.product('012',repeat=3)]


def overlap_cost(a,b):
    return 5-max((k for k in range(1,5) if a[-k:]==b[:k]),default=0)


def verify_section(mode,obj,ss):
    n=len(ss)+(mode=='linear')
    a=obj['alpha2'];b=obj['beta2'];cuts=obj['cuts'];order=obj['order'];best=obj['optimum']
    assert len(a)==len(b)==n and len(order)==len(ss)
    assert sorted(order)==list(range(len(ss)))
    assert all(isinstance(x,int) for x in a+b)
    assert all(v['weight2']>0 and 0<len(v['subset'])<n
               and v['subset']==sorted(set(v['subset']))
               and 0<=v['subset'][0]<n and v['subset'][-1]<n for v in cuts)
    assert sum(a)+sum(b)+sum(v['weight2'] for v in cuts)==2*best
    def c(i,j):
        if mode=='linear':
            if i==len(ss):return 5
            if j==len(ss):return 0
        return overlap_cost(ss[i],ss[j])
    checks=0
    for i in range(n):
        for j in range(n):
            if i==j:continue
            lhs=a[i]+b[j]+sum(v['weight2'] for v in cuts
                                   if i in v['subset'] and j not in v['subset'])
            assert lhs<=2*c(i,j),(mode,i,j,lhs,2*c(i,j))
            checks+=1
    # For a directed Hamilton circuit each vertex has one entry and exit;
    # every proper nonempty vertex subset has at least one outward edge.
    # Summing the inequalities on its edges proves total cost >= best.
    if mode=='linear':
        starts=[0]
        for i,j in zip(order,order[1:]):starts.append(starts[-1]+c(i,j))
        L=starts[-1]+5
        assert L==best
        s=[None]*L
        for i,p in zip(order,starts):
            for k,ch in enumerate(ss[i]):
                if s[p+k] is not None: assert s[p+k]==ch
                s[p+k]=ch
        assert all(x is not None for x in s)
        word=''.join(s)
        counts=Counter(word[i:i+5] for i in range(L-4))
        seen=set(counts)
    else:
        starts=[0]
        for i,j in zip(order,order[1:]):starts.append(starts[-1]+c(i,j))
        L=starts[-1]+c(order[-1],order[0])
        assert L==best
        s=[None]*L
        for i,p in zip(order,starts):
            for k,ch in enumerate(ss[i]):
                t=(p+k)%L
                if s[t] is not None: assert s[t]==ch
                s[t]=ch
        assert all(x is not None for x in s)
        word=''.join(s)
        counts=Counter((word+word)[i:i+5] for i in range(L))
        seen=set(counts)
    assert set(ss).issubset(seen)
    assert all(counts[p]==1 for p in ss)
    assert len(word)==best
    print('VERIFIED',mode,'optimum',best,'dual_edges',checks,
          'positive_cuts',len(cuts),'witness',word)
    return word


def main(path):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    assert data['alphabet']=='012' and data['palindrome_length']==5
    ss=patterns()
    assert len(ss)==27 and all(x==x[::-1] for x in ss)
    for mode in ('cyclic','linear'):
        verify_section(mode,data[mode],ss)
    print('VERIFICATION_OK')

if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('certificates.json'))
