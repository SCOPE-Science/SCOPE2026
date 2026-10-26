"""Exact finite checks of the noncaterpillar leaf-rarefaction bounds.
Run: python3 verify.py; no third-party dependencies required.
The all-size theorem follows from the separate analytic proof, not enumeration.
"""
from itertools import combinations
from math import comb


def seed():
    return {0:{3}, 1:{3}, 2:{3}, 3:{0,1,2}}


def edges(g):
    return [(u,v) for u in g for v in g[u] if u < v]


def graft(g, u, v):
    h={a:set(b) for a,b in g.items()}
    w=max(h)+1; x=w+1
    h[u].remove(v); h[v].remove(u)
    h[u].add(w); h[v].add(w)
    h[w]={u,v,x}; h[x]={w}
    return h


def canonical(g):
    remain={v:set(ns) for v,ns in g.items()}
    while len(remain)>2:
        leaves=[v for v in remain if len(remain[v])<=1]
        for v in leaves:
            for w in remain[v]:
                remain[w].remove(v)
            del remain[v]
    centers=sorted(remain)
    def enc(v,parent):
        sub=sorted(enc(w,v) for w in g[v] if w!=parent)
        return '('+''.join(sub)+')' if sub else 'L'
    return min(enc(c,None) for c in centers)


def tree_shapes(n_max=11):
    fs={3:[seed()]}
    for n in range(4,n_max+1):
        uniq={}
        for g in fs[n-1]:
            for u,v in edges(g):
                h=graft(g,u,v)
                uniq.setdefault(canonical(h),h)
        fs[n]=list(uniq.values())
    return fs


def components(g, v):
    ans=[]
    for w in g[v]:
        todo=[w]; seen={v}; leaves=set()
        while todo:
            x=todo.pop()
            if x in seen: continue
            seen.add(x)
            if len(g[x])==1: leaves.add(x)
            todo.extend(g[x])
        ans.append(leaves)
    return ans


def noncat_by_branch(g, S):
    S=set(S)
    return any(len(g[v])==3 and all(len(S & q)>=2 for q in components(g,v))
               for v in g)


def induced_tree(g,S):
    S=set(S)
    h={v:set() for v in S}
    for a,b in combinations(S,2):
        parent={a:None};todo=[a]
        for u in todo:
            if u==b:break
            for v in g[u]:
                if v not in parent:
                    parent[v]=u;todo.append(v)
        v=b
        while parent[v] is not None:
            u=parent[v]
            h.setdefault(u,set()).add(v)
            h.setdefault(v,set()).add(u)
            v=u
    while True:
        deg2=next((v for v in h if v not in S and len(h[v])==2),None)
        if deg2 is None:break
        a,b=tuple(h[deg2]);h[a].remove(deg2);h[b].remove(deg2)
        h[a].add(b);h[b].add(a);del h[deg2]
    return h


def noncat_by_induced_tree(g,S):
    h=induced_tree(g,S)
    return any(len(h[v])==3 and all(
        sum(1 for w in q if len(h[w])==1)>=2
        for q in components(h,v)) for v in h)


def six_sextets(g):
    return sum(comb(len(a),2)*comb(len(b),2)*comb(len(c),2)
               for v in g if len(g[v])==3
               for a,b,c in [components(g,v)])


def count_noncat(g,k):
    leaves=[v for v in g if len(g[v])==1]
    return sum(noncat_by_branch(g,S) for S in combinations(leaves,k))


def destructive(g):
    leaves=[v for v in g if len(g[v])==1]
    if not noncat_by_branch(g,leaves):return 0
    return sum(not noncat_by_branch(g,set(leaves)-{v}) for v in leaves)


def main():
    shape_counts={3:1,4:1,5:1,6:2,7:2,8:4,9:6,10:11,11:18}
    checked_probabilities=0
    checked_full=0
    for n,shapes in tree_shapes().items():
        assert len(shapes)==shape_counts[n],(n,len(shapes))
        if n<6: continue
        for g in shapes:
            if six_sextets(g)==0: continue
            assert destructive(g)<=4 if n>=7 else True
            direct6=sum(noncat_by_branch(g,S) for S in
                         combinations([v for v in g if len(g[v])==1],6))
            assert direct6==six_sextets(g)
            for k in range(6,n+1):
                c=count_noncat(g,k)
                assert c>=comb(n-4,k-4)
                if k<n and c==comb(n-4,k-4):
                    assert six_sextets(g)==comb(n-4,2)
                checked_probabilities+=1
            if n<=9:
                leaves=[v for v in g if len(g[v])==1]
                for k in range(6,n+1):
                    for S in combinations(leaves,k):
                        assert noncat_by_branch(g,S)==noncat_by_induced_tree(g,S)
                        checked_full+=1
        if n>=7:
            for k in range(6,n):
                equal=sum(count_noncat(g,k)==comb(n-4,k-4) for g in shapes if six_sextets(g)>0)
                assert equal==1,(n,k,equal)
        print(f'leaves={n}; shapes={len(shapes)}; minimum sextets={min((six_sextets(g) for g in shapes if six_sextets(g)>0),default="none")}; exact bound={comb(n-4,2)}')
    print(f'PASS: {checked_probabilities} shape/sample-size tests; {checked_full} independent induced-tree comparisons; equality unique for n>=7 and k<n.')

if __name__=='__main__':main()
