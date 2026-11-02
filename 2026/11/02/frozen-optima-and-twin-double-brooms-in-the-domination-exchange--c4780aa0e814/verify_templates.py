"""Independent symbolic classification and adjacency verification on ladders.

Tests exact symbolic families for arbitrary even half-length k; not an
infinite proof. All masks and adjacency tests use Python's standard library.
"""


def ones(k):
    n = 2*k
    masks = {}
    for r in (0, 1):
        for j in range(1,k+1):
            for s in (0,1):
                mask = 0
                for l in range(1,k+2):
                    col = 2*l-1 if l <= j else 2*l-2
                    row = (r^((l-1)%2)) if l <= j else (s^((l-j-1)%2))
                    mask |= 1 << (2*(col-1)+row)
                masks[('A',r,j,s)] = mask
    for s in (0,1):
        left = 3 << 2
        for t, c in enumerate(range(4,n+1,2)):
            left |= 1 << (2*(c-1)+(s^(t%2)))
        masks[('L',s)] = left
        right = 3 << (2*(n-2))
        for t,c in enumerate(range(n-3,0,-2)):
            right |= 1 << (2*(c-1)+(s^(t%2)))
        masks[('R',s)] = right
    assert len(set(masks.values())) == len(masks) == 4*k+4
    return masks


def dominates(bits, n):
    for c in range(n):
        for row in (0,1):
            x = 2*c+row
            neighboring = {x,2*c+1-row}
            if c:
                neighboring.add(2*(c-1)+row)
            if c+1 < n:
                neighboring.add(2*(c+1)+row)
            if not any(bits & (1<<v) for v in neighboring):
                return False
    return True


def slide(a,b):
    delta = a^b
    if delta.bit_count() != 2:
        return False
    x = (delta & -delta).bit_length()-1
    y = (delta ^ (1<<x)).bit_length()-1
    return abs(x//2-y//2)+abs(x%2-y%2) == 1


def expected_edges(k):
    out=set()
    def edge(a,b):
        out.add(frozenset((a,b)))
    for r in (0,1):
        q=lambda j:r^(j%2)
        for j in range(1,k):
            edge(('A',r,j,q(j)), ('A',r,j+1,q(j+1)))
        edge(('A',r,1,q(1)), ('L',r))
        edge(('A',r,1,q(1)), ('A',1-r,1,q(1)))
        edge(('A',r,k,q(k)), ('R',q(k)))
        edge(('A',r,k,q(k)), ('A',r,k,1-q(k)))
    return out


for k in range(4,27):
    masks = ones(k)
    assert all(mask.bit_count()==k+1 and dominates(mask,2*k)
               for mask in masks.values())
    labels=list(masks)
    actual=set()
    for i,a in enumerate(labels):
        for b in labels[i+1:]:
            if slide(masks[a],masks[b]):
                actual.add(frozenset((a,b)))
    pred=expected_edges(k)
    assert actual == pred, (k,actual^pred)
    assert len(actual)==2*k+6
    # Every non-listed template must be isolated by the equality above.
    active=set().union(*actual)
    assert len(active)==2*k+8
    assert len(masks)-len(active)==2*k-4
    if k in (4,8,16,26):
        print('half-length',k,'templates',len(masks),'edges',len(actual))
print('SYMBOLIC_TEMPLATE_AND_EXCHANGE_PASS')
