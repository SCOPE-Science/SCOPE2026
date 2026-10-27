"""Finite independent exhaustive checks for minority dynamics on clique windmills.
No external Python packages required. Run: python verify.py
"""
from itertools import product
from math import comb


def neighbors(s,r):
    n=1+s*r
    out=[[] for _ in range(n)]
    for j in range(r):
        vs=list(range(1+j*s,1+(j+1)*s))
        for v in vs:
            out[0].append(v)
            out[v]=[0]+[u for u in vs if u!=v]
    return out


def flipped_states(mask, adj):
    for v,ns in enumerate(adj):
        bit=(mask>>v)&1
        same=sum(((mask>>u)&1)==bit for u in ns)
        if 2*(same+1)>len(ns)+1:
            yield mask ^ (1<<v),v,(len(ns)-2*same)


def recurrent_formula(mask,s,r):
    h=mask&1
    target={s//2,s//2+1} if s%2==0 else {(s+1)//2}
    for j in range(r):
        k=sum(((mask>>(1+j*s+t))&1)!=h for t in range(s))
        if k not in target: return False
    return True


def scc_tarjan(adj):
    N=len(adj);number=[-1]*N;low=[0]*N;on=set();stack=[];components=[];counter=0
    def dfs(v):
        nonlocal counter
        number[v]=low[v]=counter;counter+=1;stack.append(v);on.add(v)
        for w in adj[v]:
            if number[w]==-1:
                dfs(w);low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],number[w])
        if low[v]==number[v]:
            comp=[]
            while True:
                w=stack.pop();on.remove(w);comp.append(w)
                if w==v:break
            components.append(comp)
    for v in range(N):
        if number[v]==-1:dfs(v)
    return components


def check(s,r):
    n=1+s*r
    E=len([(v,w) for v,N in enumerate(neighbors(s,r)) for w in N if v<w])
    ad=neighbors(s,r)
    m=1<<n
    nexts=[[] for _ in range(m)]
    energies=[0]*m
    for x in range(m):
        ex=sum(((x>>u)&1)==((x>>v)&1) for v in range(n) for u in ad[v] if v<u)
        energies[x]=ex
        for y,v,de in flipped_states(x,ad):
            ey=sum(((y>>u)&1)==((y>>w)&1) for w in range(n) for u in ad[w] if w<u)
            assert ey-ex==de, (s,r,x,v,ey-ex,de)
            assert de<=0,(s,r,x,v,de)
            nexts[x].append(y)
    comps=scc_tarjan(nexts)
    belongs=[0]*m
    for j,c in enumerate(comps):
        for x in c:belongs[x]=j
    terminal=[c for j,c in enumerate(comps) if all(belongs[y]==j for x in c for y in nexts[x])]
    actual=set(x for c in terminal for x in c)
    predicted=set(x for x in range(m) if recurrent_formula(x,s,r))
    assert actual==predicted, (s,r,actual^predicted)
    for x in range(m):
        if x not in predicted:
            assert any(v!=0 and de<0 for _,v,de in flipped_states(x,ad)),(s,r,x)
    if s%2:
        l=(s-1)//2
        ground=r*l*(l+1)
    else:
        l=s//2
        ground=r*l*l
    assert all(energies[x]==ground for x in actual),(s,r,'nonground recurrent')
    assert all(energies[x]>ground for x in range(m) if x not in actual),(s,r,'missed ground')
    if s%2:
        expected=2*comb(s,(s+1)//2)**r
        assert len(terminal)==expected
        assert all(len(c)==1 for c in terminal)
    else:
        l=s//2
        expected=2*(comb(s,l)+comb(s,l+1))**r
        assert len(terminal)==1 and len(terminal[0])==expected
        # All moves within limit set reversible, and uniform measure stationary.
        hub_edges=sum(any(y==(x^1) and v==0 for y,v,_ in flipped_states(x,ad)) for x in actual)
        assert hub_edges==2*comb(s,l)**r,(s,r,hub_edges)
        assert any(len(nexts[x])<n for x in actual),(s,r,'no aperiodic self-loop')
        for x in actual:
            for y in nexts[x]:
                assert x in nexts[y],(s,r,x,y)
    assert len(actual)==expected,(s,r,len(actual),expected)
    return f's={s} r={r} vertices={n} configurations={m} limit={len(actual)} terminal_classes={len(terminal)} energy_edges={E}'

if __name__=='__main__':
    cases=[(s,r) for s in range(1,7) for r in range(1,9) if 1+s*r<=11]
    for s,r in cases:
        print(check(s,r))
    print('CHECK_OK cases',len(cases))
