#!/usr/bin/env python3
"""Independent finite checks for the weak Heyting--Brouwer chain theorem.

Uses only Python standard library. Operations checked against the four
weak-Heyting axioms, four weak-difference axioms and both WHB axioms.
"""
from itertools import combinations_with_replacement, product
from math import comb


def ops_from_thresholds(t):
    n = len(t)  # dual chain has n points; algebra has n+1 elements
    A = range(n + 1)
    imp, diff = [], []
    for a in A:
        i = n-a
        ia, da = [], []
        for b in A:
            j = n-b
            if a <= b:
                ia.append(n)
                da.append(0)
            else:
                k = next((x for x,v in enumerate(t) if v >= j),n)
                ia.append(n-k)
                da.append(n-t[i])
        imp.append(tuple(ia)); diff.append(tuple(da))
    return tuple(imp), tuple(diff)


def is_WH(imp):
    N=len(imp); top=N-1
    for a,b,c in product(range(N),repeat=3):
        if imp[a][a]!=top: return False
        if imp[a][min(b,c)]!=min(imp[a][b],imp[a][c]):return False
        if imp[max(a,b)][c]!=min(imp[a][c],imp[b][c]):return False
        if min(imp[a][b],imp[b][c])>imp[a][c]:return False
    return True


def is_WD(diff):
    N=len(diff)
    for a,b,c in product(range(N),repeat=3):
        if diff[a][a]!=0:return False
        if diff[max(a,b)][c]!=max(diff[a][c],diff[b][c]):return False
        if diff[a][min(b,c)]!=max(diff[a][b],diff[a][c]):return False
        if diff[a][c]>max(diff[a][b],diff[b][c]):return False
    return True


def is_WHB(imp,diff):
    N=len(imp); top=N-1
    if not (is_WH(imp) and is_WD(diff)):return False
    for a,b in product(range(N),repeat=2):
        if min(a,diff[imp[a][b]][0])>b:return False
        if a>max(b,imp[top][diff[a][b]]):return False
    return True


def cong_from_ops(imp,diff):
    N=len(imp)
    counts=0
    for edges in product((False,True),repeat=N-1):
        # edges[i] means i is identified with i+1
        labels=[0]
        for e in edges:labels.append(labels[-1]+(0 if e else 1))
        pairs=[(x,y) for x in range(N) for y in range(N) if labels[x]==labels[y]]
        ok=True
        for a,aa in pairs:
            for b,bb in pairs:
                if labels[imp[a][b]]!=labels[imp[aa][bb]] or labels[diff[a][b]]!=labels[diff[aa][bb]]:
                    ok=False;break
            if not ok:break
        if ok:counts+=1
    return counts


def graph_components(t):
    n=len(t); adj=[set() for _ in range(n)]
    for i,j in product(range(n),repeat=2):
        if j>=t[i]:adj[i].add(j);adj[j].add(i)
    components=[]; unseen=set(range(n))
    while unseen:
        v=next(iter(unseen));todo=[v];seen={v}
        while todo:
            x=todo.pop()
            for y in adj[x]-seen:
                seen.add(y);todo.append(y)
        components.append(seen);unseen-=seen
    return components


def predicted_rank(t):
    n=len(t); a=sum(x<n for x in t)
    if a==0:return n
    b=t[0]
    return 1+max(0,b-a)


def run():
    for n in range(1,8):
        rank_counts={}
        full_congruence_tests=0
        for t in combinations_with_replacement(range(n+1),n):
            I,D=ops_from_thresholds(t)
            assert is_WHB(I,D), (n,t,'axioms')
            k=predicted_rank(t)
            assert len(graph_components(t))==k,(n,t,'components')
            if n<=4:
                assert cong_from_ops(I,D)==2**k,(n,t,'congruences')
                full_congruence_tests+=1
            rank_counts[k]=rank_counts.get(k,0)+1
        assert sum(rank_counts.values())==comb(2*n,n)
        if n>=2:
            expected={1:comb(2*n,n)-2**(n-2),n:1}
            for g in range(1,n-1):
                expected[g+1]=2**(n-g-2)
            assert rank_counts==expected,(n,rank_counts,expected)
        print('n',n,'total',comb(2*n,n),'boolean_ranks',dict(sorted(rank_counts.items())),
              'direct_congruence_tables',full_congruence_tests)
    # Exhaust all possible binary tables on 3-element chain independently.
    N=3
    all_wh=[];all_wd=[]
    for cells in product(range(N),repeat=N*N):
        table=tuple(tuple(cells[i*N:(i+1)*N]) for i in range(N))
        if is_WH(table):all_wh.append(table)
        if is_WD(table):all_wd.append(table)
    actual={(I,D) for I in all_wh for D in all_wd if is_WHB(I,D)}
    predicted={ops_from_thresholds(t) for t in combinations_with_replacement(range(3),2)}
    assert actual==predicted, ('full_axiom_enumeration',len(actual),len(predicted))
    print('raw_binary_tables',N**(N*N),'WH',len(all_wh),'WD',len(all_wd),
          'WHB',len(actual),'all_WHxWD',len(all_wh)*len(all_wd))
    print('VERIFY_OK')

if __name__=='__main__':run()
