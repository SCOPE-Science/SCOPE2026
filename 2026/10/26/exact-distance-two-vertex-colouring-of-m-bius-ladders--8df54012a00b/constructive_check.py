"""Exact finite checks supporting a classification of square colorings of Möbius ladders.

Run: python3 constructive_check.py
No external packages are required.
"""

# A column (a,b) gives colors at i and i+n in a twisted n-rung ladder.
BASE = {
    5: [(0,4),(1,3),(2,0),(3,4),(1,2)],
    7: [(0,2),(1,3),(2,0),(3,4),(0,1),(4,2),(1,3)],
    8: [(0,2),(1,3),(2,0),(3,1),(0,5),(4,2),(5,3),(1,4)],
    9: [(0,2),(1,3),(2,0),(3,1),(0,2),(1,3),(4,0),(3,2),(1,4)],
    12:[(0,2),(1,3),(2,0),(3,1),(0,2),(4,3),(1,0),(2,4),(0,3),(4,1),(3,2),(1,4)],
}

def adjacency(n):
    count=2*n
    neighbors=[set() for _ in range(count)]
    for i in range(count):
        for j in ((i+1)%count,(i-1)%count,(i+n)%count):
            neighbors[i].add(j)
    return neighbors

def color_from_columns(columns):
    return [a for a,b in columns]+[b for a,b in columns]

def verify(columns, limit=None):
    n=len(columns)
    color=color_from_columns(columns)
    if limit is not None: assert all(0<=x<limit for x in color)
    adj=adjacency(n)
    for v in range(2*n):
        forbidden={v}|adj[v]
        for u in adj[v]: forbidden.update(adj[u])
        assert all(color[u]!=color[v] for u in forbidden-{v}), (n,v)
    return True

def duplicate_four(columns):
    # Copy the original first four columns after their first occurrence.
    return columns[:4]+columns[:4]+columns[4:]

def residue_four(n):
    assert n>=6 and n%4==2
    return [(i%4,(i+n)%4) for i in range(n)]

if __name__=='__main__':
    for n,c in BASE.items():
        assert len(c)==n
        verify(c,6 if n==8 else 5)
        print('BASE',n,'PASS')
    for n in (7,9,12):
        word=BASE[n]
        for k in range(12):
            verify(word,5)
            word=duplicate_four(word)
        # At each insertion, the new seam is between the same four columns.
        print('FOUR_COLUMN_EXTENSION',n,'12 iterations PASS')
    for n in range(6,103,4):
        verify(residue_four(n),4)
    print('FOUR_RESIDUE_FAMILY',len(range(6,103,4)),'instances PASS')
    print('All constructive checks passed.')
