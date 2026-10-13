"""Finite exhaustive checks of coprime ideals for small commutative Artin rings.

No external packages required. Execute: python verify.py
"""
from itertools import combinations


def all_subspaces(dim):
    # Subspaces of F_2^dim as explicit sets of bit vectors.
    zero = frozenset((0,))
    frontier = {zero}
    seen = {zero}
    while frontier:
        following = set()
        for w in frontier:
            for v in range(1 << dim):
                if v in w:
                    continue
                new = frozenset(w | {x ^ v for x in w})
                if new not in seen:
                    seen.add(new)
                    following.add(new)
        frontier = following
    return sorted(seen, key=lambda w: (len(w), tuple(sorted(w))))


def make_mult(dim, entries):
    # entries[(i,j)] is a sum of basis vectors represented by a bitmask.
    table = [[0]*(1 << dim) for _ in range(1 << dim)]
    for a in range(1 << dim):
        for b in range(1 << dim):
            s = 0
            for i in range(dim):
                if a & (1 << i):
                    for j in range(dim):
                        if b & (1 << j):
                            s ^= entries.get((i,j), 0)
            table[a][b] = s
    return table


def truncated_poly(n):
    return make_mult(n,{(i,j): (1 << (i+j)) for i in range(n) for j in range(n) if i+j<n})


def square_zero(radical_dim):
    n=radical_dim+1
    entries={(0,0):1}
    for i in range(1,n):
        entries[(0,i)]=1<<i
        entries[(i,0)]=1<<i
    return make_mult(n,entries)


def non_gorenstein_cubic():
    # F_2[x,y]/(x^3,xy,y^2), basis 1,x,x^2,y.
    entries={(0,0):1,(1,1):1<<2}
    for i in range(1,4):
        entries[(0,i)]=1<<i
        entries[(i,0)]=1<<i
    return make_mult(4,entries)


def field_times(mat):
    m=(len(mat)).bit_length()-1
    n=m+1
    entries={(0,0):1}
    for i in range(m):
        for j in range(m):
            entries[(i+1,j+1)] = mat[1<<i][1<<j] << 1
    return make_mult(n,entries)


def coprime_ideals(mat):
    dim=(len(mat)).bit_length()-1
    universe=range(1<<dim)
    spaces=all_subspaces(dim)
    ideals=[w for w in spaces if all(mat[1<<i][x] in w for i in range(dim) for x in w)]
    annex={I:frozenset(a for a in universe if all(mat[a][x]==0 for x in I)) for I in ideals}
    product_copr={}
    for I in ideals:
        for J in ideals:
            product_copr[I,J]=frozenset(a for a in universe if all(mat[a][x] in J for x in annex[I]))
    cosp=[]
    for C in ideals:
        if len(C)==1: # zero ideal excluded
            continue
        if all((not C.issubset(product_copr[I,J])) or C.issubset(I) or C.issubset(J)
               for I in ideals for J in ideals):
            cosp.append(C)
    return len(ideals),cosp


def main():
    examples=[
        ('F2',truncated_poly(1),1),
        ('F2[t]/t2',truncated_poly(2),1),
        ('F2[t]/t3',truncated_poly(3),1),
        ('F2 + radical dimension 2 square-zero',square_zero(2),0),
        ('F2 + radical dimension 3 square-zero',square_zero(3),0),
        ('F2[x,y]/(x3,xy,y2), non-square-zero radical',non_gorenstein_cubic(),0),
        ('F2 x F2[t]/t2',field_times(truncated_poly(2)),2),
        ('F2 x (F2 + radical dimension 2 square-zero)',field_times(square_zero(2)),1),
        ('F2 x F2[x,y]/(x3,xy,y2)',field_times(non_gorenstein_cubic()),1),
    ]
    for name,mat,expected in examples:
        ideals,cosp=coprime_ideals(mat)
        print(f'{name}: {ideals} ideals, {len(cosp)} coprime, expected {expected}')
        assert len(cosp)==expected, (name,len(cosp),expected)
    print('VERIFY_OK')

if __name__=='__main__': main()
