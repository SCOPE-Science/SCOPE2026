"""Independent two-row graph constructor and finite exact search checks.

Run: python3 independent_check.py
The code constructs twisted boundary edges directly, not using circular indices.
"""
from itertools import combinations

WORDS={
 5: ('01231','43042'),
 7: ('0123041','2304123'),
 8: ('01230451','23015234'),
 9: ('012301431','230123024'),
 12:('012304120431','230123043124'),
}

def graph(n):
    g=[set() for _ in range(2*n)]
    def edge(x,y):
        assert x!=y
        g[x].add(y);g[y].add(x)
    for i in range(n):edge(i,n+i)
    for i in range(n-1):
        edge(i,i+1);edge(n+i,n+i+1)
    edge(n-1,n);edge(2*n-1,0)
    return g

def square(g):
    return [({v}|g[v]|set().union(*(g[w] for w in g[v])))-{v} for v in range(len(g))]

def verify_word(n,word,k):
    assert len(word[0])==len(word[1])==n
    c=list(map(int,word[0]+word[1]))
    assert max(c)<k
    h=square(graph(n))
    assert all(c[u]!=c[v] for u in range(2*n) for v in h[u])

def no_independent_four(n):
    h=square(graph(n)); count=0
    for S in combinations(range(2*n),4):
        if all(v not in h[u] for u,v in combinations(S,2)):
            count+=1
    return count

def exact_chromatic(h,k):
    n=len(h);colors=[-1]*n;visits=0
    def go(t):
        nonlocal visits
        visits+=1
        if t==n:return True
        available=[]
        for i in range(n):
            if colors[i]<0:
                forbidden={colors[j] for j in h[i] if colors[j]>=0}
                allowed=[c for c in range(k) if c not in forbidden]
                if not allowed:return False
                available.append((len(allowed),-len(h[i]),i,allowed))
        _,_,v,allowed=min(available)
        for c in allowed:
            colors[v]=c
            if go(t+1):return True
            colors[v]=-1
        return False
    return go(0),visits

if __name__=='__main__':
    for n,word in WORDS.items():
        verify_word(n,word,6 if n==8 else 5)
        print('TWISTED_GRAPH_BASE',n,'PASS')
    assert no_independent_four(8)==0
    print('M16_SQUARE_INDEPENDENT_4_SETS',0)
    for n,k in ((3,5),(4,7),(5,4),(7,4),(8,5),(9,4),(12,4)):
        valid,count=exact_chromatic(square(graph(n)),k)
        assert not valid
        print('NOT_COLORABLE',n,k,'search_nodes',count)
    print('All independent checks passed.')
