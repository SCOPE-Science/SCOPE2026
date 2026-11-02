"""Direct finite checks for ideal lattices of independent-fibre graph blowups.

Python 3 standard library only. The verifier tests ideals from their multiplication
closure definition, not from a priori lattice classification.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb


def graph_matrix(kind):
    if kind == 'K2':
        return [[0, 1], [1, 0]]
    if kind == 'K3':
        return [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    if kind == 'C4':
        return [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    raise ValueError(kind)


def blowup(A,b):
    return [[A[i//b][j//b] for j in range(len(A)*b)] for i in range(len(A)*b)]


def rank_mod(A,q):
    a=[list(map(lambda z:z%q,row)) for row in A]; n=len(a); m=len(a[0]); r=0
    for j in range(m):
        piv=next((i for i in range(r,n) if a[i][j]%q),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        v=pow(a[r][j],-1,q);a[r]=[(z*v)%q for z in a[r]]
        for i in range(n):
            if i!=r:
                f=a[i][j];a[i]=[(u-f*w)%q for u,w in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r


def gaussian(n,k,q):
    if k<0 or k>n: return 0
    z=1
    for i in range(k):
        num=q**(n-i)-1;den=q**(k-i)-1
        # compute exact product at the end to avoid intermediate fractions
    from math import prod
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))


def rref_subspaces(n,q):
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
            for vals in product(range(q),repeat=len(free)):
                rows=[[0]*n for _ in range(k)]
                for i,p in enumerate(pivots):rows[i][p]=1
                for (i,j),val in zip(free,vals):rows[i][j]=val
                yield rows


def in_span(vector,basis,q):
    return rank_mod(basis+[vector],q)==len(basis)


def ideal_from_definition(basis,squares,q):
    n=len(squares)
    # For each basis vector x and each basis generator e_i, x*e_i=x_i e_i^2.
    for v in basis:
        for i,c in enumerate(v):
            if c%q and not in_span(squares[i],basis,q):return False
    return True


def finite_ideal_check(kind,b,q):
    A=graph_matrix(kind); M=blowup(A,b); n=len(M)
    squares=M[:]
    count=0; total=0
    for basis in rref_subspaces(n,q):
        total+=1
        if ideal_from_definition(basis,squares,q):count+=1
    r=rank_mod(M,q)
    predicted=1+sum(gaussian(n-r,j,q) for j in range(n-r+1))
    assert count==predicted,(kind,b,q,count,predicted)
    print('IDEALS',kind,b,q,'rank',r,'all_subspaces',total,'ideals',count)


def edge_isoperimetric(A):
    n=len(A);best=None
    for mask in range(1,1<<n):
        size=mask.bit_count()
        if 2*size>n:continue
        boundary=sum(A[i][j] for i in range(n) for j in range(n) if (mask>>i)&1 and not ((mask>>j)&1))
        h=Fraction(boundary,size)
        if best is None or h<best:best=h
    return best


def integer_basis_check(A,b):
    # y_i and w_(i,j)=sum(first j coordinates)-j*coordinate_(j+1)
    n=len(A);M=blowup(A,b); N=b*n
    B=[]
    for i in range(n):
        y=[0]*N
        for a in range(b):y[i*b+a]=1
        B.append(y)
        for j in range(1,b):
            w=[0]*N
            for a in range(j):w[i*b+a]=1
            w[i*b+j]=-j
            B.append(w)
    # pairwise products must be zero; the columns e_i^2 are adjacency rows.
    for a in range(N):
        for c in range(a+1,N):
            v=[sum(B[a][t]*B[c][t]*M[t][h] for t in range(N)) for h in range(N)]
            assert not any(v),(a,c,v)
    # det nonzero if Gram diagonal has nonzero diagonal entries over Q
    assert all(sum(B[a][t]**2 for t in range(N))>0 for a in range(N))
    # y_i span a proper ideal: (y_i)*e_(j,a) is either zero or a square of e_(j,a).
    for i in range(n):
        for j in range(n):
            for a in range(b):
                vec=[B[i*b][j*b+a]*M[j*b+a][h] for h in range(N)]
                assert all(vec[jj*b+aa]==vec[jj*b] for jj in range(n) for aa in range(b))
    print('NATURAL_IDEAL_BASIS',n,b,'dimension',N,'ideal_dim',n)


def direct_extension_ideal_check():
    # Exhaust all projective candidate natural bases over F_3 in four dimensions.
    q=3; A=graph_matrix('K2'); M=blowup(A,2); n=4
    vectors=[]
    for v in product(range(q),repeat=n):
        if not any(v):continue
        first=next(x for x in v if x)
        w=tuple((x*pow(first,-1,q))%q for x in v)
        if w not in vectors:vectors.append(w)
    assert len(vectors)==40
    ideals=[U for U in rref_subspaces(n,q) if ideal_from_definition(U,M,q)]
    assert len(ideals)==7
    extension=[False]*len(ideals); nbases=0
    for inds in combinations(range(len(vectors)),n):
        B=[vectors[i] for i in inds]
        if rank_mod(B,q)!=n:continue
        if any(any(sum(B[i][t]*B[j][t]*M[t][h] for t in range(n))%q for h in range(n))
               for i in range(n) for j in range(i+1,n)):continue
        nbases+=1
        for idx,U in enumerate(ideals):
            if not extension[idx]:
                inside=[v for v in B if in_span(v,U,q)]
                if len(inside)==len(U):extension[idx]=True
    assert nbases>0
    assert sum(extension)==5,(nbases,extension)
    print('EXTENDIBLE_EVOLUTION_IDEALS K2 2 F3',sum(extension),
          'ordinary_ideals',len(ideals),'projective_natural_bases',nbases)


def main():
    for kind,b,q in [('K2',2,2),('K2',2,3),('K3',2,2)]:
        finite_ideal_check(kind,b,q)
    for kind,b in [('K2',2),('K3',2),('K3',3),('C4',2)]:
        A=graph_matrix(kind);G=blowup(A,b)
        h=edge_isoperimetric(G)
        integer_basis_check(A,b)
        print('CHEEGER',kind,b,str(h))
    direct_extension_ideal_check()
    assert edge_isoperimetric(blowup(graph_matrix('K3'),2))==2
    assert rank_mod(blowup(graph_matrix('K3'),2),101)==3
    print('VERIFY_OK')

if __name__=='__main__':main()
