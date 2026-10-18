"""Finite exact checks for the projective toric edge varieties of complete tripartite graphs.

Run: python verify.py.  All computations are over integers/rationals.
These bounded checks support but do not replace the all-size proof.
"""
from itertools import combinations, combinations_with_replacement, product
from math import comb
from fractions import Fraction


def rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    m, n = len(a), len(a[0]); r = 0
    for col in range(n):
        piv = next((i for i in range(r, m) if a[i][col]), None)
        if piv is None:
            continue
        a[r],a[piv]=a[piv],a[r]
        pivot=a[r][col]
        for j in range(col,n): a[r][j] /= pivot
        for i in range(m):
            if i != r and a[i][col]:
                factor=a[i][col]
                for j in range(col,n): a[i][j] -= factor*a[r][j]
        r += 1
        if r == m: break
    return r


def edge_vectors(a,b,c):
    blocks = [list(range(a)),list(range(a,a+b)),list(range(a+b,a+b+c))]
    n=a+b+c; edges=[]
    for q,r in combinations(range(3),2):
        for i in blocks[q]:
            for j in blocks[r]:
                v=[0]*n;v[i]+=1;v[j]+=1
                edges.append((i,j,tuple(v)))
    return blocks,edges


def check_vertex_chart(a,b,c,q,r):
    blocks,edges=edge_vectors(a,b,c); t=3-q-r; n=a+b+c
    i,j=blocks[q][0],blocks[r][0]
    vbase=next(v for x,y,v in edges if {x,y}=={i,j})
    def sub(x,y): return tuple(a-b for a,b in zip(x,y))
    def basis(x,y):
        v=[0]*n;v[x]+=1;v[y]-=1;return tuple(v)
    U={p:basis(p,i) for p in blocks[q] if p != i}
    V={p:basis(p,j) for p in blocks[r] if p != j}
    S={p:basis(p,j) for p in blocks[t]}
    T={p:basis(p,i) for p in blocks[t]}
    generators=list(U.values())+list(V.values())+list(S.values())+list(T.values())
    assert rank(list(zip(*generators)))==n-1
    # Every coordinate ratio is a nonnegative monomial in the listed generators.
    for x,y,vec in edges:
        g=[0]*n
        for p,z in U.items():
            if p in (x,y): g=[z0+z1 for z0,z1 in zip(g,z)]
        for p,z in V.items():
            if p in (x,y): g=[z0+z1 for z0,z1 in zip(g,z)]
        if x in blocks[t] or y in blocks[t]:
            p=x if x in blocks[t] else y
            z=S[p] if (x in blocks[q] or y in blocks[q]) else T[p]
            g=[z0+z1 for z0,z1 in zip(g,z)]
        assert tuple(g)==sub(vec,vbase),(a,b,c,q,r,x,y)
    ct=len(blocks[t]);
    for x,y in combinations(blocks[t],2):
        assert tuple(S[x][z]+T[y][z] for z in range(n)) == tuple(S[y][z]+T[x][z] for z in range(n))
    return ct


def check_segre_cone(c):
    # Degree-d equality classes of monomials of the 2c generators.
    for d in range(0,5):
        words=set()
        for positions in combinations_with_replacement(range(2*c),d):
            e=[0]*(2+c)
            for p in positions:
                e[0 if p<c else 1] += 1
                e[2+(p%c)] += 1
            words.add(tuple(e))
        assert len(words)==(d+1)*comb(d+c-1,c-1),(c,d,len(words))
    if c>=2:
        # On a generic rank-one matrix rows are (1,2,...,c) and twice that.
        s=[i+1 for i in range(c)]; t=[2*(i+1) for i in range(c)]
        J=[]
        for i,j in combinations(range(c),2):
            row=[0]*(2*c)
            # df/d(s_i,s_j,t_i,t_j), f=s_i t_j - s_j t_i
            row[i]+=t[j];row[j]-=t[i];row[c+j]+=s[i];row[c+i]-=s[j]
            J.append(row)
        assert rank(J)==c-1,(c,rank(J))
        assert 2*c>c+1


def main():
    charts=0
    for a,b,c in product(range(1,5),repeat=3):
        for q,r in combinations(range(3),2):
            check_vertex_chart(a,b,c,q,r)
            charts += 1
    for c in range(1,7): check_segre_cone(c)
    examples={(1,1,1):(0,[]),(1,1,2):(1,[0]),(2,2,2):(3,[2,2,2]),(2,3,5):(3,[3,5,6])}
    for (a,b,c),(count,dims) in examples.items():
        raw=[(a+b-2,c),(a+c-2,b),(b+c-2,a)]
        d=sorted(d for d,omitted in raw if omitted>=2)
        assert len(d)==count and d==sorted(dims)
    print(f'VERIFY_OK charts={charts} segre_sizes=1..6 degrees=0..4 examples={len(examples)}')

if __name__=='__main__': main()
