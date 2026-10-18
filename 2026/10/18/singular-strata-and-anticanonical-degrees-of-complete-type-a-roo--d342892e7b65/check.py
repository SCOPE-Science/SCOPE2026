"""Exact combinatorial checks for type-A complete root-polytope toric varieties.

Standalone finite-size checks supplement the all-n lattice argument.
Requires Python 3 standard library only.
"""
from itertools import combinations, product
from math import comb, factorial


def nonempty_disjoint(n):
    # For each index: 0 unused, 1 A, 2 B.
    for state in product(range(3), repeat=n):
        A=tuple(i for i,s in enumerate(state) if s==1)
        B=tuple(i for i,s in enumerate(state) if s==2)
        if A and B:
            yield (A,B)


def roots(A,B,n):
    # In Z^(n-1), with e_(n-1)=-(e_0+...+e_(n-2)).
    # Instead use ambient Z^n zero-sum vectors, sufficient for ranks.
    ans=[]
    for a in A:
        for b in B:
            v=[0]*n;v[a]=1;v[b]=-1;ans.append(tuple(v))
    return ans


def rank(vs):
    if not vs:return 0
    A=[[__import__('fractions').Fraction(x) for x in row] for row in vs]
    p=0
    for j in range(len(A[0])):
        q=next((i for i in range(p,len(A)) if A[i][j]),None)
        if q is None:continue
        A[p],A[q]=A[q],A[p]
        fac=A[p][j]
        A[p]=[x/fac for x in A[p]]
        for i in range(p+1,len(A)):
            fac=A[i][j]
            if fac:A[i]=[x-fac*y for x,y in zip(A[i],A[p])]
        p+=1
        if p==len(A):break
    return p


def check(n):
    faces=list(nonempty_disjoint(n))
    # Every proper nonempty face is uniquely indexed by (A,B), giving all its vertices.
    square=[]
    for A,B in faces:
        nv=len(A)*len(B)
        dim=rank(roots(A,B,n))-1
        assert dim==len(A)+len(B)-2
        assert (nv > dim+1)==(len(A)>=2 and len(B)>=2)
        if len(A)==len(B)==2:square.append((A,B))
        if len(A)>=2 and len(B)>=2:
            assert any(set(a).issubset(A) and set(b).issubset(B)
                       for a,b in square) or (len(A)>2 or len(B)>2)
    assert len(square)==6*comb(n,4), (n,len(square))
    assert all(sum(len(a)==2 and len(b)==2 and set(a).issubset(A) and set(b).issubset(B)
                   for a,b in square)>0 for A,B in faces if len(A)>=2 and len(B)>=2)
    A,B=square[0]
    remaining=tuple(i for i in range(n) if i not in A and i not in B)
    # Maximal cones containing the square correspond to distributing every other vertex
    # between the two extremal levels; hence product-of-P1 quotient fan.
    extending=[(AA,BB) for AA,BB in faces if set(A).issubset(AA)
              and set(B).issubset(BB) and len(AA)+len(BB)==n]
    assert len(extending)==2**(n-4)
    expected={(tuple(sorted(A+tuple(i for i,b in zip(remaining,bits) if b==0))),
               tuple(sorted(B+tuple(i for i,b in zip(remaining,bits) if b==1))))
              for bits in product(range(2),repeat=len(remaining))}
    assert set(extending)==expected
    # A reference K_2,2 has the unique primitive four-ray parallelogram relation.
    a,c=A;b,d=B
    vec={(i,j):roots((i,),(j,),n)[0] for i in A for j in B}
    assert tuple(x+y for x,y in zip(vec[a,b],vec[c,d])) == \
           tuple(x+y for x,y in zip(vec[a,d],vec[c,b]))
    assert rank(list(vec.values()))==3
    print('n',n,'faces',len(faces),'minimal_singular_squares',len(square),
          'maximal_containing_each',len(extending),'component_dim',n-4,
          'component_anticanonical_degree',factorial(n-4),
          'total_anticanonical_degree',factorial(n)//4)


if __name__=='__main__':
    for n in range(4,8):check(n)
    print('VERIFY_OK')
