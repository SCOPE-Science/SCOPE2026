"""Finite exact transition checks for a tree majority process.

Only standard-library Python is required. The proof for all k is analytic;
these finite checks test the graph architecture and local transition laws.
"""
from fractions import Fraction
from collections import deque


def edges(k,s):
    edges=[]; h='h'
    for j in range(s): edges.append((h,'b'+str(j)))
    for i in range(k):
        y='y'+str(i); w='w'+str(i)
        edges += [(h,y),(y,w),(w,'z'+str(i)+'a'),(w,'z'+str(i)+'b')]
    return edges


def diameter_and_tree(k,s):
    E=edges(k,s); vs=set(v for edge in E for v in edge)
    g={v:set() for v in vs}
    for a,b in E: g[a].add(b); g[b].add(a)
    assert len(E)==len(vs)-1
    diam=0
    for root in vs:
        d={root:0}; q=deque([root])
        while q:
            u=q.popleft()
            for v in g[u]:
                if v not in d:d[v]=d[u]+1;q.append(v)
        assert len(d)==len(vs)
        diam=max(diam,max(d.values()))
    assert diam==6
    assert len(vs)==s+4*k+1


def step(k,s,h,leaf,m):
    """Markov transition law restricted to rigid white anchors.
    h: hub color; leaf: uniform color of hub leaves; m: k-bit vector of ties.
    """
    x=m.bit_count(); total=k+s; blue=s*leaf+x
    if blue*2>total: hc={1:Fraction(1)}
    elif blue*2<total: hc={0:Fraction(1)}
    else: hc={0:Fraction(1,2),1:Fraction(1,2)}
    if h: options={j:Fraction(1,2**k) for j in range(1<<k)}
    else: options={0:Fraction(1)}
    out={}
    for hv,ph in hc.items():
        for j,pj in options.items():out[(hv,h,j)]=ph*pj
    assert sum(out.values())==1
    return out


def scc_count(k,s):
    states=[(h,l,m) for h in (0,1) for l in (0,1) for m in range(1<<k)]
    graph={q:set(step(k,s,*q)) for q in states}
    seen=set(); order=[]
    def dfs(u):
        seen.add(u)
        for v in graph[u]:
            if v not in seen:dfs(v)
        order.append(u)
    for u in states:
        if u not in seen:dfs(u)
    reverse={v:set() for v in states}
    for u,outs in graph.items():
        for v in outs:reverse[v].add(u)
    seen.clear(); components=[]
    def revdfs(u,c):
        seen.add(u);c.add(u)
        for v in reverse[u]:
            if v not in seen:revdfs(v,c)
    for u in reversed(order):
        if u not in seen:
            c=set();revdfs(u,c);components.append(c)
    absorbing=[c for c in components if all(graph[u]<=c for u in c)]
    return sorted([len(c) for c in absorbing])


def forced_whiten(k,s,state):
    # Conditional transition path where all floating-node outcomes are white.
    h,leaf,m=state
    for _ in range(3):
        outcomes=step(k,s,h,leaf,m)
        picks=[(new,p) for new,p in outcomes.items() if new[2]==0]
        assert picks
        # For s=k-1 the hub update is deterministic and has no tied case.
        assert len(picks)==1
        (h,leaf,m),_ = picks[0]
    return (h,leaf,m)


def run():
    for k in range(2,8):
        for s in (k-1,k+1):
            diameter_and_tree(k,s)
            assert step(k,s,1,1,(1<<k)-1)
            for mask in range(1,1<<k):
                target=step(k,k-1,1,1,mask)
                assert set(target)=={(1,1,m) for m in range(1<<k)}
                assert all(p==Fraction(1,2**k) for p in target.values())
            recurrent=scc_count(k,s)
            if s==k-1:
                assert recurrent==[1],(k,s,recurrent)
                for h in (0,1):
                    for leaf in (0,1):
                        for mask in range(1<<k):
                            assert forced_whiten(k,s,(h,leaf,mask))==(0,0,0)
                assert step(k,s,1,1,0)=={(0,1,j):Fraction(1,2**k) for j in range(1<<k)}
            else:
                assert 2**k in recurrent,(k,s,recurrent)
                for mask in range(1<<k):
                    out=step(k,s,1,1,mask)
                    assert set(out)=={(1,1,j) for j in range(1<<k)}
                    assert all(p==Fraction(1,2**k) for p in out.values())
            print('k=',k,'buffer=',s,'vertices=',s+4*k+1,'absorbing-SCC-sizes=',recurrent)
    print('VERIFICATION_OK')
if __name__=='__main__':run()
