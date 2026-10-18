#!/usr/bin/env python3
"""Finite characteristic-two cross-checks for path-algebra polynomial function spans.
Computations check finite examples only, not the all-quiver asymptotic theorem.
"""
from itertools import product


def path_basis(num_vertices, arrows):
    paths=[(v,()) for v in range(num_vertices)]
    frontier=[(v,()) for v in range(num_vertices)]
    while frontier:
        newer=[]
        for start,seq in frontier:
            end=arrows[seq[-1]][1] if seq else start
            for a,(source,target) in enumerate(arrows):
                if source==end:
                    newer.append((start,seq+(a,)))
        paths.extend(newer)
        frontier=newer
        assert len(paths)<200, 'Cyclic or unexpectedly large example'
    idx={p:i for i,p in enumerate(paths)}
    end=lambda p: arrows[p[1][-1]][1] if p[1] else p[0]
    product_index={}
    for i,p in enumerate(paths):
        for j,r in enumerate(paths):
            if end(p)==r[0]:
                product_index[(i,j)]=idx[(p[0],p[1]+r[1])]
    return paths, product_index


def dimension_of_polynomial_functions(num_vertices, arrows, generators):
    paths, multiplication=path_basis(num_vertices,arrows)
    m=len(paths)
    evaluations=list(product(range(1<<m), repeat=generators))
    def mult(a,b):
        out=0
        for (i,j),k in multiplication.items():
            if (a>>i)&1 and (b>>j)&1:
                out^=1<<k
        return out
    identity=sum(1<<i for i,(v,p) in enumerate(paths) if not p)
    evaluations_identity=[identity]*len(evaluations)
    xs=[[v[k] for v in evaluations] for k in range(generators)]
    def integer_function_vector(values):
        result=0
        for i,value in enumerate(values):
            result |= value << (m*i)
        return result
    pivots={}
    def insert(w):
        candidate=integer_function_vector(w)
        while candidate:
            msb=candidate.bit_length()-1
            if msb not in pivots:
                pivots[msb]=candidate
                return True
            candidate^=pivots[msb]
        return False
    queue=[]
    for f in [evaluations_identity]+xs:
        if insert(f):
            queue.append(f)
    pointer=0
    while pointer<len(queue):
        current=queue[pointer]
        pointer+=1
        for generator in xs:
            new=[mult(u,v) for u,v in zip(current,generator)]
            if insert(new):
                queue.append(new)
    assert pointer==len(queue)
    return len(pivots),len(evaluations),m


def height(num_vertices,arrows):
    heights=[1]*num_vertices
    for iteration in range(num_vertices):
        next_heights=heights[:]
        for x,y in arrows:
            next_heights[y]=max(next_heights[y],heights[x]+1)
        if next_heights==heights:
            return max(heights)
        heights=next_heights
    raise ValueError('Input contains directed cycle')


def run():
    specimens=[
        ('single_vertex',1,[],1,2),
        ('two_isolated_vertices',2,[],2,4),
        ('single_arrow',2,[(0,1)],2,24),
        ('two_parallel_arrows',2,[(0,1),(0,1)],2,24),
        ('directed_three_chain',3,[(0,1),(1,2)],1,6),
        ('two_arrows_to_sink',3,[(0,2),(1,2)],1,4),
    ]
    for title,vertices,arrows,n,expected in specimens:
        d,count,m=dimension_of_polynomial_functions(vertices,arrows,n)
        assert d==expected,(title,d,expected)
        h=height(vertices,arrows)
        lower=(2**(n-1))*((2**(n-1)-1)**(h-1)) if n>=2 else 1
        assert d>=lower,(title,d,lower)
        print(f'{title}: q=2, n={n}, dim={d}, input_count={count}, basis_size={m}, height={h}')
    # Diagonal-point orthogonality of the lower-bound construction for h=3,
    # n=3: at each vertex assign an arbitrary 2-bit vector.
    choices=list(product(range(2),repeat=2))
    target_tuples=[v for v in product(choices,repeat=3)
                   if v[0]!=v[1] and v[1]!=v[2]]
    assert len(target_tuples)==36
    # For every target choose an index separating each neighboring pair.
    for t in target_tuples:
        k=[next(i for i in range(2) if t[j][i]!=t[j+1][i]) for j in (0,1)]
        nonzero=0
        for c in product(choices,repeat=3):
            deltas=all(c[i]==t[i] for i in range(3))
            factor=(c[0][k[0]]^c[1][k[0]])*(c[1][k[1]]^c[2][k[1]])
            coef=int(deltas)*factor
            assert coef==int(c==t)
            nonzero+=coef
        assert nonzero==1
    print('chain3 lower-bound separator supports: 36/36 isolated')
    print('VERIFIED: all finite examples and separators')

if __name__=='__main__':
    run()
