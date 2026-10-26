"""Verify coordinate-color wild-set certificates on binary cubes.
Pure Python 3, no external dependencies.
"""
import json,sys,collections
from pathlib import Path

def cube_edges(d):
    return {(u,u^(1<<i)):i for i in range(d) for u in range(1<<d) if not ((u>>i)&1)}

def verify(d, listed):
    E=cube_edges(d)
    W=[]
    for e in listed:
        if not isinstance(e,list) or len(e)!=2: raise ValueError('bad edge')
        a,b=e
        if a>b:a,b=b,a
        if (a,b) not in E:raise ValueError(f'noncube edge {e}')
        if (a,b) in W:raise ValueError('duplicate edge')
        W.append((a,b))
    n=1<<d
    color_counts=collections.Counter(E[e] for e in W)
    tree_certificates={}
    for i in range(d):
        par=list(range(n))
        def find(v):
            while par[v]!=v:
                par[v]=par[par[v]]
                v=par[v]
            return v
        for e,c in E.items():
            if c==i:
                a,b=e;a=find(a);b=find(b)
                if a!=b:par[a]=b
        tree=[]
        for a,b in W:
            u=find(a);v=find(b)
            if u!=v:par[u]=v;tree.append([a,b])
        comps=len({find(v) for v in range(n)})
        assert comps==1,(d,i,comps)
        assert len(tree)==n//2-1,(d,i,len(tree))
        tree_certificates[str(i)]=tree
    return color_counts,tree_certificates

def main():
    data=json.loads(Path(__file__).with_name('certificate.json').read_text())
    expected={2:2,3:5,4:10,5:20}
    for d, w in sorted((int(d),v) for d,v in data['wild_sets'].items()):
        assert d in expected and len(w)==expected[d]
        counts, trees=verify(d,w)
        lower=(d*((1<<(d-1))-1)+(d-2))//(d-1)
        assert lower=={2:2,3:5,4:10,5:19}[d]
        print(f'Q_{d}: edges={d*(1<<(d-1))}, wild={len(w)}, lower={lower}, per_color={[counts[i] for i in range(d)]}')
        for i in range(d):print(f'  color={i}: contracted_spanning_tree_edges={len(trees[str(i)])}')
    print('VERIFY_OK')

if __name__=='__main__':main()
