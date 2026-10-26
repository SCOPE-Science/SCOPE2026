#!/usr/bin/env python3
"""Exact dimensions and finite certificates for maximal independent sets of cycles.
No third-party packages are required.  Run: python3 verify.py [certificate.json]."""
import itertools, json, sys
from functools import lru_cache

def enumerate_direct(n):
    ans=[]
    for b in range(1<<n):
        if any((b>>i&1) and (b>>((i+1)%n)&1) for i in range(n)):continue
        if any(not(b>>i&1) and not((b>>((i-1)%n)&1) or (b>>((i+1)%n)&1)) for i in range(n)):continue
        ans.append(b)
    return ans

def enumerate_extend(n):
    # Construct binary words by local prefix constraints, not by bitset tests.
    out=[]
    def go(a):
        i=len(a)
        if i==n:
            if a[-1] and a[0]:return
            if all(a[j] or a[(j-1)%n] or a[(j+1)%n] for j in range(n)):
                out.append(sum(a[j]<<j for j in range(n)))
            return
        for z in (0,1):
            if z and i and a[-1]:continue
            if i>=2 and not (a[i-2] or a[i-1] or z):continue
            go(a+[z])
    go([])
    return sorted(out)

def dimensions(H,n):
    E=[sum(1<<j for j,h in enumerate(H) if h>>i&1) for i in range(n)]
    U=(1<<len(H))-1
    @lru_cache(None)
    def ld(m):
        if m.bit_count()<=1:return 0
        d=0; hi=m.bit_count().bit_length()-1
        for e in E:
            y=m&e
            if y in (0,m):continue
            z=m^y
            if min(y.bit_count(),z.bit_count())<(1<<d):continue
            d=max(d,1+min(ld(y),ld(z)))
            if d==hi:break
        return d
    D=ld(U)
    @lru_cache(None)
    def rank_independent(concepts):
        if len(concepts)<=1:return 0
        best=0
        for i in range(n):
            zero=frozenset(h for h in concepts if not (h>>i&1))
            one=concepts-zero
            if zero and one:
                best=max(best,1+min(rank_independent(zero),rank_independent(one)))
        return best
    assert rank_independent(frozenset(H))==D
    vc=0; best=[]
    for k in range(n+1):
        found=None
        for S in itertools.combinations(range(n),k):
            traces={sum(((h>>i)&1)<<j for j,i in enumerate(S)) for h in H}
            if len(traces)==1<<k:
                found=list(S);break
        if found is None:break
        vc=k;best=found
    def tree(m,d):
        if d==0:
            assert m
            return {'witness':H[(m&-m).bit_length()-1]}
        for i,e in enumerate(E):
            p=m&e; z=m^p
            if p and z and ld(p)>=d-1 and ld(z)>=d-1:
                return {'query':i,'zero':tree(z,d-1),'one':tree(p,d-1)}
        raise AssertionError('No depth-d witness')
    return D,vc,best,tree(U,D),ld.cache_info().currsize

def verify_tree(node,H,depth=0,assign=None):
    if assign is None:assign={}
    if 'witness' in node:
        w=node['witness']
        assert w in H
        assert all((w>>i&1)==b for i,b in assign.items())
        return 1
    x=node['query'];assert x not in assign
    return verify_tree(node['zero'],H,depth+1,{**assign,x:0})+verify_tree(node['one'],H,depth+1,{**assign,x:1})

def main():
    profile=[]; certs={}
    for n in range(3,17):
        H=enumerate_direct(n)
        assert H==enumerate_extend(n),(n,'independent enumerators disagree')
        d,v,S,T,states=dimensions(H,n)
        count=verify_tree(T,H)
        assert count==1<<d
        profile.append({'n':n,'maximal_independent_sets':len(H),'vc':v,'littlestone':d,'states':states,'shattered_set':S})
        print('C%02d concepts=%02d VC=%d Ldim=%d states=%d leaves=%d'%(n,len(H),v,d,states,count))
        if n in (13,16):certs[str(n)]={'n':n,'dimension':d,'shattered_set':S,'tree':T}
    assert [(x['n'],x['vc'],x['littlestone']) for x in profile if x['vc'] != x['littlestone']] == [(13,4,5),(16,5,6)]
    assert profile[10]['maximal_independent_sets']==39 and profile[-1]['maximal_independent_sets']==90
    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf8') as f: incoming=json.load(f)
        assert incoming==certs
    else:
        with open('certificate.json','w',encoding='utf8') as f:json.dump(certs,f,sort_keys=True,indent=2);f.write('\n')
    for nn in (13,16):
        cc=certs[str(nn)]
        print('CERTIFICATE',nn,'ROOT',cc['tree']['query'],'LEAVES',verify_tree(cc['tree'],enumerate_direct(nn)))
    print('ALL_CYCLE_CHECKS_PASS')
if __name__=='__main__': main()
