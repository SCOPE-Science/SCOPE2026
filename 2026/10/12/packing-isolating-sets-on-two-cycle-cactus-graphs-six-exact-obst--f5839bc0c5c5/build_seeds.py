#!/usr/bin/env python3
"""Construct exact finite seed witnesses for the two-cycle cactus theorem."""
import csv,functools,pathlib

ROOT=pathlib.Path(__file__).resolve().parent

def barbell(a,b,d):
    assert 3<=a<=b and d>=0
    edges=set()
    def add(u,v):
        if u>v:u,v=v,u
        assert u!=v
        edges.add((u,v))
    def cycle(verts):
        for u,v in zip(verts,verts[1:]+verts[:1]):add(u,v)
    cycle(list(range(a)))
    if d==0:
        cycle([0]+list(range(a,a+b-1)))
        n=a+b-1
    else:
        path=[0]+list(range(a,a+d))
        for u,v in zip(path,path[1:]):add(u,v)
        cycle([a+d-1]+list(range(a+d,a+d+b-1)))
        n=a+b+d-1
    assert len(edges)==n+1
    return n,sorted(edges)

def solve(a,b,d):
    n,edges=barbell(a,b,d)
    adj=[0]*n
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    forb=[0]*n;cov=[0]*n;poss=[0]*len(edges)
    for x in range(n):
        closed=(1<<x)|adj[x]
        forbid=closed
        for y in range(n):
            if (closed>>y)&1:forbid|=adj[y]
        forb[x]=forbid
        for j,(u,v) in enumerate(edges):
            if closed&(1<<u|1<<v):cov[x]|=1<<j;poss[j]|=1<<x
    @functools.lru_cache(maxsize=None)
    def go(avail,uncovered):
        if uncovered==0:return ()
        smallest=None
        ebit=uncovered
        while ebit:
            k=(ebit&-ebit).bit_length()-1;ebit&=ebit-1
            c=poss[k]&avail
            if not c:return None
            if smallest is None or c.bit_count()<smallest.bit_count():smallest=c
            if smallest.bit_count()==1:break
        while smallest:
            v=(smallest&-smallest).bit_length()-1;smallest&=smallest-1
            got=go(avail&~forb[v],uncovered&~cov[v])
            if got is not None:return (v,)+got
        return None
    return go((1<<n)-1,(1<<len(edges))-1)

if __name__=='__main__':
    out=ROOT/'seed_table.csv';bad=[];ok=0
    with out.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(['a','b','d','result','vertices'])
        for d in range(11):
            for a in range(3,9):
                for b in range(a,9):
                    sol=solve(a,b,d)
                    if sol is None:
                        bad.append((a,b,d));w.writerow((a,b,d,'NO',''))
                    else:
                        ok+=1;w.writerow((a,b,d,'YES',';'.join(map(str,sorted(sol)))))
    print('base_cases',ok+len(bad),'witnessed',ok,'negative',len(bad),'exceptions',bad)
