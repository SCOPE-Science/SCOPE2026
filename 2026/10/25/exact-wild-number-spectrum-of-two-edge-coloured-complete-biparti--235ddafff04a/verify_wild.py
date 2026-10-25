"""Exact independent subset enumeration for two-colour wild-number spectra.

Use: python verify_wild.py
The component count is computed directly on both monochromatic spanning
subgraphs using union-find; all labelled surjective 2-colourings are tested.
"""
from itertools import product

def components(n, edges):
    parent=list(range(n))
    def root(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]]
            v=parent[v]
        return v
    for x,y in edges:
        parent[root(x)]=root(y)
    return len({root(i) for i in range(n)})

def expected_range(a,b):
    return set(range(max(0,2*(a+b-1)-a*b),a+b-1))

def verify(a,b):
    n=a+b
    E=[(i,a+j) for i in range(a) for j in range(b)]
    observed=set()
    histogram={}
    for mask in range(1,(1<<len(E))-1):
        r=[e for j,e in enumerate(E) if (mask>>j)&1]
        b_edges=[e for j,e in enumerate(E) if not ((mask>>j)&1)]
        w=components(n,r)+components(n,b_edges)-2
        observed.add(w)
        histogram[w]=histogram.get(w,0)+1
    target=expected_range(a,b)
    assert observed==target, (a,b,observed,target)
    assert sum(histogram.values())==(1<<len(E))-2
    print(f'K_{{{a},{b}}}: {((1<<len(E))-2)} colorings, range {min(observed)}..{max(observed)}; histogram {sorted(histogram.items())}')

if __name__=='__main__':
    for a,b in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4)]:
        verify(a,b)
    print('VERIFY_OK')
