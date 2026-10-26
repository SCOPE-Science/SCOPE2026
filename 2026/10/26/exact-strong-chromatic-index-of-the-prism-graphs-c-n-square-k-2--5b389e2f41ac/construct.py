"""Explicit strong edge colorings of prism graphs; Python 3, no dependencies."""
import sys

# A column gives the colors on (rung i, upper edge i->i+1,
# lower edge i->i+1). Color labels are nonnegative integers.
PERIOD4 = ((5, 0, 2), (4, 1, 3), (5, 2, 0), (4, 3, 1))
SEEDS = {
 3: ((6,0,3),(7,1,4),(8,2,5)),
 5: ((5,0,7),(6,1,4),(5,2,0),(7,3,1),(6,4,2)),
 6: ((5,0,6),(4,1,3),(5,2,0),(4,3,7),(5,6,2),(4,7,1)),
 7: ((2,0,6),(4,1,3),(5,2,0),(4,3,6),(1,0,5),(2,6,4),(3,5,1)),
 9: ((2,0,6),(4,1,3),(5,2,0),(4,6,1),(3,0,2),(4,5,6),(3,1,0),(2,6,4),(3,5,1)),
 10: ((5,0,6),(4,1,3),(5,2,0),(4,6,1),(5,3,2),(4,0,6),(5,1,3),(4,6,2),(5,3,0),(4,2,1)),
 11: ((5,0,2),(4,1,3),(5,2,0),(4,3,1),(5,0,2),(4,1,3),(6,2,0),(5,3,4),(6,1,2),(5,4,0),(6,3,1)),
 13: ((5,0,2),(4,1,3),(5,2,0),(4,3,1),(5,0,2),(4,1,3),(5,2,0),(4,3,1),(6,0,2),(5,1,4),(6,2,3),(5,4,0),(6,3,1)),
 14: ((5,0,2),(4,1,3),(5,2,0),(4,3,1),(5,0,2),(4,1,3),(5,2,6),(4,0,1),(5,6,2),(4,3,0),(5,1,6),(4,2,3),(5,6,0),(4,3,1))
}

def coloring(n):
    assert isinstance(n, int) and n>=3
    if n in SEEDS: return list(SEEDS[n])
    if n%4==0: return list(PERIOD4)*(n//4)
    base={1:13,2:14,3:11}[n%4]
    assert n>=base and (n-base)%4==0
    seq=list(SEEDS[base]); repeats=(n-base)//4
    assert seq[0:2]==seq[4:6]
    return seq[:6]+list(seq[2:6])*repeats+seq[6:]

def graph(n):
    vertices=range(2*n)
    edge_list=[(i,(i+1)%n) for i in range(n)]
    edge_list += [(n+i,n+(i+1)%n) for i in range(n)]
    edge_list += [(i,n+i) for i in range(n)]
    assert len(edge_list)==3*n
    neighbours=[set() for _ in vertices]
    for u,v in edge_list:
        neighbours[u].add(v);neighbours[v].add(u)
    return edge_list,neighbours

def verify(n,cols):
    assert len(cols)==n
    edges,nb=graph(n)
    cols=[tuple(c) for c in cols]
    assigned=[cols[i][1] for i in range(n)]
    assigned += [cols[i][2] for i in range(n)]
    assigned += [cols[i][0] for i in range(n)]
    for j,(a,b) in enumerate(edges):
        for k,(c,d) in enumerate(edges[:j]):
            if (a in (c,d) or b in (c,d)
                or c in nb[a] or d in nb[a]
                or c in nb[b] or d in nb[b]):
                assert assigned[j]!=assigned[k],(n,j,k,assigned[j])
    return len(set(assigned))

if __name__=='__main__':
    for n in range(3,101):
        cols=coloring(n)
        num=verify(n,cols)
        expected=(9 if n==3 else 8 if n in (5,6)
                  else 6 if n%4==0 else 7)
        assert num==expected,(n,num,expected)
        if n in SEEDS or n in (8,12,15,17,18,19,22,23,25,26,27,30,31,41,99,100):
            print(f'n={n} colors={num} verified')
    print('CONSTRUCTION_OK all n=3..100; template insertions verified for all residue classes')
