#!/usr/bin/env python3
"""Separate cycle-permutation generator, fiber shatter test, and game-tree replay."""
import itertools
import json
from functools import lru_cache
from pathlib import Path

TARGET = {3:(1,[1],0),4:(3,[1,6],1),5:(12,[1,10,45,60],3),
          6:(70,[1,15,105,395,360],5),7:(465,[1,21,210,1190,3780,2520],6)}

def all_factors(n):
    edges=list(itertools.combinations(range(n),2))
    positions={e:i for i,e in enumerate(edges)}
    factors=set()
    for p in itertools.permutations(range(n)):
        start=[]
        cycles=[]
        seen=set()
        for i in range(n):
            if i in seen:continue
            cyc=[];j=i
            while j not in seen:
                seen.add(j);cyc.append(j);j=p[j]
            if len(cyc)<3:break
            cycles.append(cyc)
        else:
            eidx=set()
            for cyc in cycles:
                for a,b in zip(cyc,cyc[1:]+cyc[:1]):
                    eidx.add(positions[tuple(sorted((a,b)))])
            factors.add(sum(1<<q for q in eidx))
    return edges,sorted(factors)

def fiber_census(H,qcount):
    B=[sum(1<<i for i,g in enumerate(H) if (g>>j)&1) for j in range(qcount)]
    front=[(-1,((1<<len(H))-1,))]
    counts=[1]
    while front:
        nxt=[]
        for last,parts in front:
            for j in range(last+1,qcount):
                one=B[j]
                new=[]
                for part in parts:
                    a=part&one; z=part&~one
                    if not a or not z:break
                    new.extend((z,a))
                else:nxt.append((j,tuple(new)))
        if not nxt:break
        counts.append(len(nxt));front=nxt
    return counts,B

def replay(cert_entry,H,edges):
    assert cert_entry['edge_order']==[list(e) for e in edges]
    assert set(int(x,16) for x in cert_entry['factors'])==set(H)
    internal=[];seen=set()
    def walk(t,constraints,d):
        if not d:
            wi=t['witness']
            W=int(cert_entry['factors'][wi],16)
            assert all(bool(W & (1<<e))==bool(v) for e,v in constraints)
            assert W not in seen
            seen.add(W)
            return
        e=t['query'];internal.append(e)
        walk(t['zero'],constraints+[(e,0)],d-1)
        walk(t['one'],constraints+[(e,1)],d-1)
    depth=cert_entry['depth']
    walk(cert_entry['tree'],[],depth)
    assert len(internal)==2**depth-1 and len(seen)==2**depth
    return len(internal),len(seen)

def upper_positive(H,edge_index,depth,qcount):
    S=frozenset(g for g in H if g>>edge_index&1)
    @lru_cache(None)
    def test(V,k):
        if k==0:return True
        if len(V)<2**k:return False
        for j in range(qcount):
            a=frozenset(g for g in V if g>>j&1)
            if len(a)<2**(k-1) or len(V)-len(a)<2**(k-1):continue
            if test(a,k-1) and test(V-a,k-1):return True
        return False
    ans=test(S,depth)
    return ans,len(S),test.cache_info().currsize

def main():
    cert=json.loads((Path(__file__).with_name('certificate.json')).read_text())
    for n,(nh,counts,d) in TARGET.items():
        edges,H=all_factors(n)
        assert len(H)==nh
        got,B=fiber_census(H,len(edges))
        assert got==counts,(n,got)
        c=cert['trees'][str(n)]
        assert c['depth']==d
        inn,leaf=replay(c,H,edges)
        print(f'INDEPENDENT_N{n}_PASS factor_count={nh} VC={len(got)-1} LD_lower={d} tree_nodes={inn} tree_leaves={leaf}',flush=True)
        if n==7:
            assert upper_positive(H,0,6,len(edges))[0] is False
            print('INDEPENDENT_N7_LD_UPPER_PASS positive branch cannot shatter depth six',flush=True)
    print('INDEPENDENT_TWO_FACTOR_ALL_CHECKS_PASS')
    hcert=json.loads((Path(__file__).with_name('hamilton_certificate.json')).read_text())
    expected={3:(1,[1],0),4:(3,[1,6],1),5:(12,[1,10,45,60],3),6:(60,[1,15,105,375,360],5),7:(360,[1,21,210,1155,3465,2520],6)}
    for n,(nh,count,ld) in expected.items():
        edges,FF=all_factors(n)
        def connected(g):
            visited={0};queue=[0]
            while queue:
                v=queue.pop()
                for i,(a,b) in enumerate(edges):
                    if (g>>i)&1 and (a==v or b==v):
                        w=b if a==v else a
                        if w not in visited:visited.add(w);queue.append(w)
            return len(visited)==n
        H=[g for g in FF if connected(g)]
        assert len(H)==nh
        got,B=fiber_census(H,len(edges)); assert got==count,(n,got)
        ent=dict(hcert['trees'][str(n)])
        ent['factors']=ent['cycles']
        assert ent['depth']==ld
        a,b=replay(ent,H,edges)
        if n==7:assert upper_positive(H,0,6,len(edges))[0] is False
        print(f'INDEPENDENT_HAMILTON_N{n}_PASS count={nh} support_counts={got} depth={ld} leaves={b}',flush=True)
    print('INDEPENDENT_BOTH_FAMILIES_ALL_CHECKS_PASS')

if __name__=='__main__':main()
