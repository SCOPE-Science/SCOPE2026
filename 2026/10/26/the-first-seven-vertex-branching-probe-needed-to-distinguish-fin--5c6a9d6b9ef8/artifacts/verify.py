#!/usr/bin/env python3
"""Exact certificate: restricted tree-homomorphism profiles, finite trees up to order 14.
Pure Python 3 standard library; no external graph library required.
"""
from collections import defaultdict

def canon(g):
    n=len(g)
    if n==1:return '()'
    deg=[len(a) for a in g]
    leaves=[i for i,d in enumerate(deg) if d<=1]
    left=n
    while left>2:
        left-=len(leaves)
        nxt=[]
        for v in leaves:
            deg[v]=0
            for w in g[v]:
                if deg[w]>0:
                    deg[w]-=1
                    if deg[w]==1:nxt.append(w)
        leaves=nxt
    centers=leaves
    def code(v,p):
        return '('+''.join(sorted(code(w,v) for w in g[v] if w!=p))+')'
    if len(centers)==1:return code(centers[0],-1)
    a,b=centers
    return '*'+''.join(sorted([code(a,b),code(b,a)]))

def extend(g,v):
    h=[set(a) for a in g]
    h.append({v});h[v].add(len(g))
    return tuple(tuple(sorted(x)) for x in h)

def trees_through(nmax):
    ans={1:{'()':((),)}}
    for n in range(2,nmax+1):
        group={}
        for g in ans[n-1].values():
            for v in range(n-1):
                h=extend(g,v)
                group[canon(h)]=h
        ans[n]=group
    return ans

def walks(g,terms):
    v=[1]*len(g)
    out=[]
    for k in range(terms):
        out.append(sum(v))
        v=[sum(v[w] for w in g[u]) for u in range(len(g))]
    return tuple(out)

def hom(f,g):
    # Dynamic programming over a rooted source tree, exact positive-integer counts.
    parent={0:-1};order=[0]
    for v in order:
        for u in f[v]:
            if u not in parent:
                parent[u]=v;order.append(u)
    n=len(g); dp={}
    for v in reversed(order):
        children=[u for u in f[v] if parent.get(u)==v]
        d=[1]*n
        for u in children:
            d=[d[x]*sum(dp[u][y] for y in g[x]) for x in range(n)]
        dp[v]=d
    return sum(dp[0])

def arm_lengths(g):
    deg=[len(x) for x in g]
    branch=[v for v,d in enumerate(deg) if d==3]
    if len(branch)!=1:return None
    c=branch[0];res=[]
    for v in g[c]:
        length=1;prev=c;curr=v
        while len(g[curr])==2:
            nxt=next(z for z in g[curr] if z!=prev)
            prev,curr=curr,nxt;length+=1
        res.append(length)
    return tuple(sorted(res))

def main():
    tt=trees_through(14)
    source=trees_through(7)
    expected=[1,1,1,2,3,6,11,23,47,106,235,551,1301,3159]
    counts=[len(tt[n]) for n in range(1,15)]
    assert counts==expected,counts
    print('TARGET_TREE_COUNTS',counts,'TOTAL',sum(counts))
    collisions={}
    for n in range(1,15):
        classes=defaultdict(list)
        for key,g in tt[n].items():
            classes[walks(g,2*n)].append((key,g))
        pairs=[v for v in classes.values() if len(v)>1]
        assert all(len(v)==2 for v in pairs)
        expected_pairs={12:1,13:2,14:6}.get(n,0)
        assert len(pairs)==expected_pairs,(n,len(pairs))
        assert len(classes)==len(tt[n])-expected_pairs
        collisions[n]=pairs
        print('PATH_PROFILE_GROUPS',n,'CLASSES',len(classes),'PAIRS',len(pairs))
    failures6=[]
    min_source_counts={}
    for n in range(1,15):
        counts_by_min=defaultdict(int)
        for pair in collisions[n]:
            (_,a),(_,b)=pair
            assert walks(a,2*n)==walks(b,2*n)
            first=None
            for size in range(1,8):
                diffs=[(key,arm_lengths(f),hom(f,a),hom(f,b)) for key,f in source[size].items() if hom(f,a)!=hom(f,b)]
                if diffs:
                    first=size
                    if size in (6,7):
                        print('FIRST_SEPARATING_SOURCES',n,size,diffs)
                    break
            assert first is not None
            counts_by_min[first]+=1
            if n==14 and first==7:
                failures6.append(pair)
        min_source_counts[n]=dict(counts_by_min)
        print('MINIMUM_SOURCE_ORDER_PROFILE',n,dict(counts_by_min))
    assert min_source_counts[12]=={6:1}
    assert min_source_counts[13]=={6:2}
    assert min_source_counts[14]=={6:5,7:1}
    assert len(failures6)==1
    exceptional=sorted(failures6[0],key=lambda z:z[0])
    for idx,(key,g) in enumerate(exceptional):
        print('FOURTEEN_EXCEPTION_'+str(idx+1)+'_CODE',key)
        print('FOURTEEN_EXCEPTION_'+str(idx+1)+'_EDGES',sorted((v,u) for v in range(len(g)) for u in g[v] if v<u))
    S6={arms:(key,f) for key,f in source[6].items() if (arms:=arm_lengths(f)) in [(1,1,3),(1,2,2)]}
    S7={arms:(key,f) for key,f in source[7].items() if (arms:=arm_lengths(f)) in [(1,1,4),(1,2,3)]}
    assert len(S6)==2 and len(S7)==2
    for arms,(key,f) in S6.items():
        for n in range(1,14):
            seen=set()
            for g in tt[n].values():
                sig=walks(g,2*n),hom(f,g)
                assert sig not in seen
                seen.add(sig)
        print('SINGLE_SIX_VERTEX_PROBE_COMPLETE_THROUGH_13',arms)
    all_good7=[]
    for key,f in source[7].items():
        good=True
        for n in range(1,15):
            seen=set()
            for g in tt[n].values():
                sig=walks(g,2*n),hom(f,g)
                if sig in seen:good=False;break
                seen.add(sig)
            if not good:break
        if good: all_good7.append(arm_lengths(f))
    assert sorted(all_good7)==[(1,1,4),(1,2,3)],all_good7
    print('ONLY_SEVEN_VERTEX_SINGLE_PROBES_COMPLETE_THROUGH_14',all_good7)
    (a_key,a),(b_key,b)=exceptional
    print('FOURTEEN_EXCEPTION_MINIMUM_SEVEN_COUNTS',[(arms,hom(f,a),hom(f,b)) for arms,(key,f) in sorted(S7.items())])
    # All six-vertex connected tree sources fail on exceptional 14-vertex pair.
    assert all(hom(f,a)==hom(f,b) for k in range(1,7) for f in source[k].values())
    print('SIX_VERTEX_PROBE_LIMIT_SHARP_AT_HOST_ORDER_14')
    print('ALL_BOUNDED_TREE_HOMOMORPHISM_CHECKS_PASS')
if __name__=='__main__':main()
