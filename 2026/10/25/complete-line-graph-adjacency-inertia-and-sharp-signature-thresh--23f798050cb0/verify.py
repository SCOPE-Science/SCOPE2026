"""Exact independent adjacency-matrix inertia checks for cycle dumbbells.
Public graph theory verification: Python 3 standard library only.
"""
from fractions import Fraction
from itertools import product


def make_graph(a, b, d):
    if min(a, b) < 3 or d < 1:
        raise ValueError('Cycle lengths at least 3; connecting path positive')
    n = a + b + d - 1
    E = set()
    def edge(u, v):
        E.add(tuple(sorted((u, v))))
    for i in range(a): edge(i, (i+1)%a)
    for j in range(b): edge(a+j, a+(j+1)%b)
    path = [0] + list(range(a+b, n)) + [a]
    assert len(path) == d+1
    for u, v in zip(path, path[1:]): edge(u, v)
    return sorted(E)


def line_adjacency(edges):
    m=len(edges)
    return [[int(i!=j and bool(set(edges[i])&set(edges[j]))) for j in range(m)] for i in range(m)]


def exact_inertia(source):
    """Independent rational symmetric Gaussian elimination, including 2x2 pivots."""
    A=[[Fraction(x) for x in row] for row in source]
    pos=zero=neg=0
    while A:
        n=len(A)
        i=next((i for i in range(n) if A[i][i]),None)
        if i is not None:
            if i: 
                A[0],A[i]=A[i],A[0]
                for row in A: row[0],row[i]=row[i],row[0]
            v=A[0][0]
            pos += v>0
            neg += v<0
            A=[[A[j][k]-A[j][0]*A[0][k]/v for k in range(1,n)] for j in range(1,n)]
            continue
        ij=next(((i,j) for i in range(n) for j in range(i+1,n) if A[i][j]),None)
        if ij is None:
            zero+=n
            break
        i,j=ij
        perm=[i,j]+[k for k in range(n) if k not in (i,j)]
        A=[[A[u][v] for v in perm] for u in perm]
        c=A[0][1]
        pos+=1; neg+=1
        A=[[A[u][v]-(A[u][0]*A[1][v]+A[u][1]*A[0][v])/c for v in range(2,n)] for u in range(2,n)]
    return (pos,zero,neg)


def boundary_weight(length):
    r=length%4
    return {0:1,1:3,3:-1}.get(r)


def local_count(length):
    r=length%4
    return (length-1)//2 + int(r==2),int(r==0)


def inertia_residual(a,b,d):
    wa,wb=boundary_weight(a),boundary_weight(b)
    if wa is not None and wb is not None:
        if d%2==0:
            h=d//2
            s=wa+wb
            return (h+int(s>0),int(s==0),h+int(s<0))
        h=(d-1)//2
        tr=wa+wb
        det=wa*wb-1
        if det<0: signs=(1,0,1)
        elif det==0: signs=(int(tr>0),1,int(tr<0))
        elif tr>0: signs=(2,0,0)
        else: signs=(0,0,2)
        return (h+signs[0],signs[1],h+signs[2])
    if wa is None and wb is None:
        return ((d-1)//2,int(d%2==0),(d-1)//2)
    w=wa if wa is not None else wb
    if d%2==0:
        return (d//2,0,d//2)
    h=(d-1)//2
    return (h+int(w>0),0,h+int(w<0))


def predicted_inertia(a,b,d):
    qa,za=local_count(a)
    qb,zb=local_count(b)
    p,z,n=inertia_residual(a,b,d)
    return (qa+qb+p,za+zb+z,qa+qb+n+1)


def signature_closed(a,b,d):
    r,s=a%4,b%4
    if d%2==1:
        if 2 not in (r,s):
            if r in (0,1) and s in (0,1):
                return 1 if 1 in (r,s) else 0
            return -2 if (r,s)==(3,3) else -1
        if r==s==2:return -1
        other=s if r==2 else r
        return -2 if other==3 else 0
    if 2 in (r,s):return -1
    if r==s==3:return -2
    if set((r,s))=={0,3}:return -1
    return 0


def main():
    n=0
    for a,b,d in product(range(3,11),range(3,11),range(1,9)):
        edges=make_graph(a,b,d)
        observed=exact_inertia(line_adjacency(edges))
        expected=predicted_inertia(a,b,d)
        assert sum(observed)==len(edges)==a+b+d
        assert observed==expected, (a,b,d,observed,expected)
        assert observed[0]-observed[2]==signature_closed(a,b,d)
        n+=1
    # Explicit boundary and singular cases, including the formerly conjectured equality examples.
    reference={(4,5,1):(5,1,4),(5,5,1):(6,0,5),(4,4,1):(3,3,3),
               (3,3,1):(2,1,4),(6,6,2):(6,1,7)}
    for triple,target in reference.items():
        got=exact_inertia(line_adjacency(make_graph(*triple)))
        assert got==target,(triple,got,target)
    print(f'VERIFY_OK exact_line_graphs={n} maximum_edges=28 residue_and_singular_branches=all')

if __name__=='__main__':main()
