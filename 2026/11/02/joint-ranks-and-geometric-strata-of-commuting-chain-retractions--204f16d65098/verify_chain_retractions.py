"""Direct finite-field verification of commuting idempotent cochain endomorphisms.

Usage: python verify_chain_retractions.py
No third-party packages. The direct enumerator constructs every linear map on each
cochain group and filters the ORIGINAL chain, idempotence and commutativity identities.
The independent formula enumerator uses splitting multiplicities and automorphism orders.
All fields in these tests are prime fields; the proof covers arbitrary fields.
"""
import math
import itertools
import collections


def gl_order(n,q):
    return math.prod(q**n-q**j for j in range(n))


def radical_dim(h,b):
    return sum(b[i]*(h[i]+h[i+1]+(b[i+1] if i+1<len(b) else 0))
               for i in range(len(b)))


def aut_order(h,b,q):
    return q**radical_dim(h,b)*math.prod(gl_order(x,q) for x in (*h,*b))


def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for a in range(n+1):
            for remaining in compositions(n-a,k-1):
                yield (a,)+remaining


def predicted_histogram(h,b,q,m):
    k=1<<m
    numerator=aut_order(h,b,q)
    result=collections.Counter()
    for pieces in itertools.product(*[list(compositions(t,k)) for t in (*h,*b)]):
        hs=pieces[:len(h)]
        bs=pieces[len(h):]
        denominator=math.prod(
            aut_order([v[c] for v in hs],[v[c] for v in bs],q)
            for c in range(k))
        assert numerator%denominator==0
        multiplicity=numerator//denominator
        profile=[]
        for j in range(m):
            selected=[c for c in range(k) if (c>>j)&1]
            chains=tuple(sum(hs[i][c]+(bs[i][c] if i<len(b) else 0)
                             +(bs[i-1][c] if i else 0) for c in selected)
                         for i in range(len(h)))
            homology=tuple(sum(hs[i][c] for c in selected)
                           for i in range(len(h)))
            boundaries=tuple(sum(bs[i][c] for c in selected)
                             for i in range(len(b)))
            profile.append((chains,homology,boundaries))
        result[tuple(profile)]+=multiplicity
    return result


def matmul(A,B,p):
    return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(len(B)))%p
                       for j in range(len(B[0]))) for i in range(len(A)))


def matrices(rows,cols,p):
    for seq in itertools.product(range(p),repeat=rows*cols):
        yield tuple(tuple(seq[i*cols+j] for j in range(cols)) for i in range(rows))


def rank(M,p):
    a=[list(row) for row in M]
    rows=len(a); cols=len(a[0]) if rows else 0
    pivot=0
    for j in range(cols):
        z=next((i for i in range(pivot,rows) if a[i][j]),None)
        if z is None:
            continue
        a[pivot],a[z]=a[z],a[pivot]
        inv=pow(a[pivot][j],-1,p)
        a[pivot]=[(inv*v)%p for v in a[pivot]]
        for i in range(rows):
            if i==pivot: continue
            factor=a[i][j]
            a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==rows: break
    return pivot


def direct_histogram(h,b,p,m):
    degrees=len(h)
    dims=[h[i]+(b[i] if i<len(b) else 0)+(b[i-1] if i else 0)
          for i in range(degrees)]
    # Fixed basis in degree i: homology, outgoing disk bottoms, incoming disk tops.
    differentials=[]
    for i in range(degrees-1):
        D=[[0]*dims[i] for _ in range(dims[i+1])]
        for j in range(b[i]):
            D[h[i+1]+(b[i+1] if i+1<len(b) else 0)+j][h[i]+j]=1
        differentials.append(tuple(map(tuple,D)))
    all_degree_matrices=[list(matrices(d,d,p)) for d in dims]
    idempotents=[]
    for F in itertools.product(*all_degree_matrices):
        if not all(matmul(differentials[i],F[i],p)==
                   matmul(F[i+1],differentials[i],p)
                   for i in range(degrees-1)):
            continue
        if not all(matmul(A,A,p)==A for A in F):
            continue
        idempotents.append(F)

    def signature(F):
        chain_ranks=tuple(rank(A,p) for A in F)
        homology_ranks=tuple(
            rank(tuple(tuple(F[i][u][v] for v in range(h[i]))
                       for u in range(h[i])),p) if h[i] else 0
            for i in range(degrees))
        boundary_ranks=tuple(
            rank(tuple(tuple(F[i][h[i]+u][h[i]+v] for v in range(b[i]))
                       for u in range(b[i])),p) if b[i] else 0
            for i in range(degrees-1))
        return chain_ranks,homology_ranks,boundary_ranks

    out=collections.Counter()
    for tuple_F in itertools.product(idempotents,repeat=m):
        if all(matmul(tuple_F[i][d],tuple_F[j][d],p)==
               matmul(tuple_F[j][d],tuple_F[i][d],p)
               for i in range(m) for j in range(i) for d in range(degrees)):
            out[tuple(signature(F) for F in tuple_F)]+=1
    return out,len(idempotents)


def main():
    configurations=[
        ([1,1],[1],2,1),
        ([1,1],[1],2,2),
        ([1,1],[1],2,3),
        ([1,1],[1],3,2),
        ([1,1],[1],5,2),
        ([0,0,0],[1,1],2,2),
        ([0,0,0],[1,1],3,2),
        ([1,0],[2],2,2),
        ([0,0],[2],2,2),
        ([0,0],[2],3,2),
        ([1,1],[2],2,2),
    ]
    for h,b,p,m in configurations:
        predicted=predicted_histogram(h,b,p,m)
        direct,individual=direct_histogram(h,b,p,m)
        assert predicted==direct,(h,b,p,m,'full multirank histogram mismatch')
        print('PASS h=%s b=%s field=%s tuple=%s idempotents=%s compatible=%s histogram_cells=%s'%
              (h,b,p,m,individual,sum(direct.values()),len(direct)))
    # Analytic test for the three distinct one-copy summands.
    for m in range(1,5):
        for q in (2,3,5):
            actual=sum(predicted_histogram([1,1],[1],q,m).values())
            expected=2**m*(1+(2**m-1)*q)**2
            assert actual==expected
    rich=predicted_histogram([1,1],[2],2,2)
    homology_invisible=sum(v for stat,v in rich.items()
                           if all(all(x==0 for x in entry[1]) for entry in stat))
    components=math.comb(1+4-1,4-1)**2*math.comb(2+4-1,4-1)
    assert sum(rich.values())==5860 and homology_invisible==409 and components==160
    print('REPEATED_DISK_CASE pairs=5860 homology_zero=409 components=160')
    print('CHAIN_RETRACTIONS_JOINT_RANK_OK 11_DIRECT_HISTOGRAMS 12_CLOSED_FORM_TESTS')

if __name__=='__main__':
    main()
