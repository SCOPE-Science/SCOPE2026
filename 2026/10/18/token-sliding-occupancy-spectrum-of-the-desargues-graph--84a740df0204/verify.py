#!/usr/bin/env python3
"""Reproduce the token-sliding component census of the Desargues graph.
Python 3 standard library only; exact finite enumerations with independent paths.
"""
from itertools import combinations
from collections import Counter,deque
from math import comb

PAIRS=list(combinations(range(5),2))
assert len(PAIRS)==10
# Vertices 0..9 have label (0,pair), 10..19 label (1,pair).
E={(a,10+b) for a,x in enumerate(PAIRS) for b,y in enumerate(PAIRS) if set(x).isdisjoint(y)}
assert len(E)==30
nb=[0]*20
for u,v in E:
    nb[u]|=1<<v;nb[v]|=1<<u
assert all(n.bit_count()==3 for n in nb)
# A fixed label-preserving certificate identifies this incidence graph with
# the classical generalized Petersen graph GP(10,3). GP labels 0..9 (rim),
# 10..19 (inner), rim edges i--i+1, spokes i--(10+i), inner i--i+3.
TO_GP=[0,19,13,2,8,17,11,6,15,4,5,14,18,7,3,12,16,1,10,9]
assert sorted(TO_GP)==list(range(20))
gp_edges=set()
for i in range(10):
    gp_edges.add(tuple(sorted((i,(i+1)%10))))
    gp_edges.add(tuple(sorted((i,10+i))))
    gp_edges.add(tuple(sorted((10+i,10+(i+3)%10))))
assert len(gp_edges)==30
assert {tuple(sorted((TO_GP[u],TO_GP[v]))) for u,v in E}==gp_edges

def enum_rec():
    result=[]
    def visit(avail,mask):
        if not avail:result.append(mask);return
        bit=avail & -avail
        v=bit.bit_length()-1
        visit(avail^bit,mask)
        visit((avail^bit)&~nb[v],mask|bit)
    visit((1<<20)-1,0)
    return sorted(result)

def enum_bipartite():
    result=[]
    for u in range(1<<10):
        prohibited=0
        for i in range(10):
            if (u>>i)&1:
                prohibited|=(nb[i]>>10)
        av=(~prohibited)&1023
        v=av
        while True:
            result.append(u|(v<<10))
            if v==0:break
            v=(v-1)&av
    return sorted(result)

def edges_by_slides(states):
    index={m:i for i,m in enumerate(states)}; edges=set()
    for i,s in enumerate(states):
        for b in range(20):
            if not (s>>b)&1:continue
            remainder=s^(1<<b)
            allowed=nb[b]
            while allowed:
                bit=allowed&-allowed; allowed-=bit
                v=bit.bit_length()-1
                if remainder&nb[v]:continue
                j=index.get(remainder|bit)
                if j is not None:
                    assert i!=j
                    edges.add((min(i,j),max(i,j)))
    return edges

def edges_by_pairs(states):
    ed=set()
    for i,s in enumerate(states):
        for j in range(i+1,len(states)):
            t=states[j];d=s^t
            if d.bit_count()!=2:continue
            u=(s&d).bit_length()-1
            v=(t&d).bit_length()-1
            if (nb[u]>>v)&1:ed.add((i,j))
    return ed

def comp_profile(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    vis=set();comps=[]
    for i in range(n):
        if i in vis:continue
        vis.add(i); q=[i]
        for u in q:
            for v in adj[u]:
                if v not in vis:vis.add(v);q.append(v)
        comps.append(q)
    return adj,comps

def check_union_find(n,edges,comps):
    pa=list(range(n))
    def root(i):
        while pa[i]!=i:
            pa[i]=pa[pa[i]];i=pa[i]
        return i
    for a,b in edges:
        a=root(a);b=root(b);pa[a]=b
    cc=Counter(root(i) for i in range(n))
    assert sorted(cc.values())==sorted(map(len,comps))

def main():
    A=enum_rec();B=enum_bipartite()
    assert A==B and len(A)==6212
    assert sum((1 for s in A if s.bit_count()==10))==2
    print('IS:',len(A),'including empty; graph |V|=20, |E|=30')
    expected={
      1:(20,30,{20:1}),
      2:(160,420,{160:1}),
      3:(660,2220,{660:1}),
      4:(1510,5580,{1500:1,1:10}),
      5:(1924,6870,{1824:1,10:10}),
      6:(1320,3840,{970:1,33:10,1:20}),
      7:(480,780,{38:10,4:20,1:20}),
      8:(115,60,{4:20,1:35}),
      9:(20,0,{1:20}),
      10:(2,0,{1:2})
    }
    allcomp={}
    for k in range(1,11):
        states=[s for s in A if s.bit_count()==k]
        slide=edges_by_slides(states)
        pair=edges_by_pairs(states)
        assert slide==pair,(k,len(slide),len(pair))
        adj,components=comp_profile(len(states),slide)
        check_union_find(len(states),slide,components)
        sizes=dict(Counter(map(len,components)))
        assert (len(states),len(slide),sizes)==expected[k],(k,len(states),len(slide),sizes)
        assert sum(map(len,components))==len(states)
        assert sum(map(len,adj))==2*len(slide)
        assert all(len(c)==len(set(c)) for c in components)
        # Check the unlabelled shape of each natural small component.
        if k==5:
            for c in components:
                if len(c)!=10:continue
                by_degree=Counter(len(adj[v]) for v in c)
                assert by_degree=={3:4,2:6}
                hubs={v for v in c if len(adj[v])==3}
                assert len(hubs)==4
                assert all(not (set(adj[v])&hubs) for v in hubs)
                pairs=[frozenset(set(adj[v])&hubs) for v in c if v not in hubs]
                assert len(set(pairs))==6 and all(len(p)==2 for p in pairs)
                assert set(pairs)==set(map(frozenset,combinations(hubs,2)))
        if k in (7,8):
            for c in components:
                if len(c)==4:
                    assert Counter(len(adj[v]) for v in c)=={1:3,3:1}
        if k==4:
            frozen={states[c[0]] for c in components if len(c)==1}
            stars={(sum(1<<i for i,p in enumerate(PAIRS) if x in p)<<shift) for shift in (0,10) for x in range(5)}
            assert len(stars)==10 and frozen==stars
        print('k=%2d  sets=%4d  TS_edges=%4d  components=%3d  sizes=%s'%(k,len(states),len(slide),len(components),sorted(sizes.items(),reverse=True)))
        allcomp[k]=(states,adj,components)
    for k in (4,5,6,7,8):
        _,adj,comps=allcomp[k]
        rds={}
        for c in comps:
            if len(c)==1:continue
            ecc=[]
            for src in c:
                distances={src:0};q=deque([src])
                while q:
                    a=q.popleft()
                    for b in adj[a]:
                        if b not in distances:distances[b]=distances[a]+1;q.append(b)
                assert len(distances)==len(c)
                ecc.append(max(distances.values()))
            key=len(c);rds.setdefault(key,set()).add((min(ecc),max(ecc)))
        print(' k',k,'component size -> (radius,diameter)',rds)
    print('ALL_CHECKS_OK')
if __name__=='__main__':main()
