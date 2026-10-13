"""Standalone exhaustive check of independent double Roman corona identity.

Uses no external dependencies.  Every labeling is examined independently of
construction and compared with the proposed neighborhood transform.
"""
from itertools import combinations, product
from collections import Counter
from math import comb


def edges_of_graph(n,mask):
    pairs=list(combinations(range(n),2))
    return [e for k,e in enumerate(pairs) if (mask>>k)&1]


def is_independent(G,I):
    S=set(I)
    return all(not (u in S and v in S) for u,v in G)


def neighborhood(G,I):
    S=set(I)
    return {v for u,v in G if u in S and v not in S} | {u for u,v in G if v in S and u not in S}


def idrd_feasible(n,E,labels):
    # Coordinates 0..n-1 = core vertices; n..2n-1 = private leaves.
    if any(a>0 and b>0 for a,b in [(labels[i],labels[n+i]) for i in range(n)]):
        return False
    if any(labels[u]>0 and labels[v]>0 for u,v in E):
        return False
    ne=[[] for _ in range(2*n)]
    for u,v in E:
        ne[u].append(v);ne[v].append(u)
    for i in range(n):
        ne[i].append(n+i)
        ne[n+i].append(i)
    for v,x in enumerate(labels):
        if x==0:
            nb=[labels[u] for u in ne[v]]
            if 3 not in nb and nb.count(2)<2:
                return False
        if x==1 and not any(labels[u]>=2 for u in ne[v]):
            return False
    return True


def predicted(n,E):
    out=Counter()
    for mask in range(1<<n):
        I={i for i in range(n) if (mask>>i)&1}
        if not is_independent(E,I):
            continue
        k=len(neighborhood(E,I))
        for j in range(k+1):
            out[3*n-k+j]+=comb(k,j)
    return out


def indep_domination(n,E):
    ans=n+1
    for mask in range(1<<n):
        I={i for i in range(n) if (mask>>i)&1}
        if is_independent(E,I) and len(I | neighborhood(E,I))==n:
            ans=min(ans,len(I))
    return ans


def test_graph(n,E):
    predicted_poly=predicted(n,E)
    actual=Counter()
    for labels in product(range(4),repeat=2*n):
        if idrd_feasible(n,E,labels):
            actual[sum(labels)]+=1
    assert actual==predicted_poly, (n,E,actual,predicted_poly)
    assert min(actual)==2*n+indep_domination(n,E), (n,E,actual)
    return sum(actual.values()),actual[min(actual)]


def main():
    graph_count=0
    all_labs=0
    for n in range(1,5):
        ecount=n*(n-1)//2
        for mask in range(1<<ecount):
            E=edges_of_graph(n,mask)
            test_graph(n,E)
            graph_count+=1
            all_labs+=4**(2*n)
        print(f'ALL_LABELINGS_OK_n={n}_graph_count={2**ecount}')
    E=[(i,i+1) for i in range(4)]
    total,min_count=test_graph(5,E)
    print(f'P5: all_functions={total}, min_count={min_count}, i(G)={indep_domination(5,E)}')
    graph_count+=1;all_labs+=4**10
    E=[(i,(i+1)%5) for i in range(5)]
    total,min_count=test_graph(5,E)
    print(f'C5: all_functions={total}, min_count={min_count}, i(G)={indep_domination(5,E)}')
    graph_count+=1;all_labs+=4**10
    E=[(0,i) for i in range(1,5)]
    total,min_count=test_graph(5,E)
    print(f'K1,4: all_functions={total}, min_count={min_count}, i(G)={indep_domination(5,E)}')
    graph_count+=1;all_labs+=4**10
    E=[(i,j) for i in range(5) for j in range(i+1,5)]
    total,min_count=test_graph(5,E)
    print(f'K5: all_functions={total}, min_count={min_count}, i(G)={indep_domination(5,E)}')
    graph_count+=1;all_labs+=4**10

    E=[(0,1),(1,2),(2,3)]
    pred=predicted(4,E)
    print(f'P4: gamma={min(pred)}, min_count={pred[min(pred)]}, indep_dom={indep_domination(4,E)}')
    assert min(pred)==10 and pred[10]==5
    print('graphs_checked=',graph_count)
    print('labelings_checked=',all_labs)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
