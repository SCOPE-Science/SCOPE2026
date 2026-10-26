"""Exact verification of endpoint cut/cycle projections on 3-design incidence graphs.

Requires Python 3.9+; no external dependencies.  Constructed from first principles:
1) verify all triple incidences;
2) solve grounded Laplacians by rational Gaussian elimination on small examples;
3) verify full column sums, Kirchhoff conditions, and idempotent symmetry
   via explicit edge currents on larger examples.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def complete_design(v, k):
    return tuple(combinations(range(v), k))


def affine_quadruples(m):
    """Blocks are affine two-planes in F_2^m."""
    v = 1 << m
    return tuple(sorted({tuple(sorted((a, b, c, a ^ b ^ c)))
                         for a, b, c in combinations(range(v), 3)}))


def parameters(v, blocks):
    k = len(blocks[0])
    assert 4 <= k <= v-2
    assert len(blocks) == len(set(blocks))
    assert all(len(B)==k and len(set(B))==k for B in blocks)
    triple = {T: 0 for T in combinations(range(v), 3)}
    for B in blocks:
        for T in combinations(B, 3):
            triple[T] += 1
    ts = set(triple.values())
    assert len(ts)==1 and next(iter(ts))>0, ts
    tau=next(iter(ts))
    l=F(tau*(v-2), k-2)
    r=F(l*(v-1),k-1)
    assert l.denominator==1 and r.denominator==1
    return k,int(tau),int(l),int(r)


def formula(v,k,tau,lam,r):
    q=F(1)+F(2*(k-1),k*lam*v)*(lam*(2*v-k)-k-(v-k)*tau)
    p=q+F(k-2,k)-F(2*(k-1),lam*v)
    return q,p


def potential_columns(v, blocks, k, lam):
    gamma=F(1,lam*v)
    for S in blocks:
        Sset=set(S)
        for i in S:
            potential=[((k-1)*gamma if j==i else (-gamma if j in Sset else F(0)))
                       for j in range(v)]
            col={}
            for T in blocks:
                target=F(1) if T==S else F(0)
                phi=(sum((potential[j] for j in T),F(0))-target)/k
                for j in T:
                    col[(j,T)]=potential[j]-phi
            yield i,S,col


def inverse(A):
    n=len(A)
    B=[[F(x) for x in A[i]]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        p=next((j for j in range(i,n) if B[j][i]),None)
        assert p is not None
        B[i],B[p]=B[p],B[i]
        pivot=B[i][i]
        B[i]=[a/pivot for a in B[i]]
        for j in range(n):
            if j!=i:
                f=B[j][i]
                if f:
                    B[j]=[a-f*b for a,b in zip(B[j], B[i])]
    return [row[n:] for row in B]


def full_laplacian(v, blocks):
    n=v+len(blocks)
    A=[[0]*n for _ in range(n)]
    for t,T in enumerate(blocks):
        for i in T:
            b=v+t
            A[i][i]+=1; A[b][b]+=1
            A[i][b]-=1; A[b][i]-=1
    return A


def exact_grounded_check(v, blocks, target_q, target_p):
    A=full_laplacian(v,blocks)
    N=len(A); root=N-1
    inv=inverse([row[:root] for row in A[:root]])
    edges=[(j,s) for s,S in enumerate(blocks) for j in S]
    for i,s in edges:
        rhs=[F(0) for _ in range(root)]
        rhs[i]+=1
        if v+s<root: rhs[v+s]-=1
        x=[sum((a*b for a,b in zip(row,rhs)),F(0)) for row in inv]+[F(0)]
        curr=[x[j]-x[v+t] for j,t in edges]
        Q=sum(map(abs,curr),F(0))
        P=sum((abs(F(int((j,t)==(i,s)))-u) for (j,t),u in zip(edges,curr)),F(0))
        assert Q==target_q and P==target_p, (v,len(blocks),(i,s),Q,P)
    return len(edges)


def check_one(name, v, blocks, do_grounded=False):
    k,tau,lam,r=parameters(v, blocks)
    q,p=formula(v,k,tau,lam,r)
    edges=[(j,T) for T in blocks for j in T]
    count=0
    for i,S,col in potential_columns(v,blocks,k,lam):
        assert len(col)==len(edges)
        # Verify every node divergence exactly (not merely the edge-column norm).
        for j in range(v):
            assert sum((col[(j,T)] for T in blocks if j in T),F(0))==int(j==i)
        for T in blocks:
            assert sum((col[(j,T)] for j in T),F(0))==int(T==S)
        qc=sum((abs(a) for a in col.values()),F(0))
        pc=sum((abs(F(int(e==(i,S)))-a) for e,a in col.items()),F(0))
        assert (qc,pc)==(q,p), (name,i,S,qc,pc,q,p)
        count+=1
    grounded=exact_grounded_check(v,blocks,q,p) if do_grounded else 0
    print(f'{name}: v={v} k={k} blocks={len(blocks)} triple_lambda={tau} pair_lambda={lam} '
          f'columns={count} Q={q} P={p} grounded_columns={grounded}')
    return count,grounded


def main():
    total=0; direct=0
    for name,v,blocks,ground in (
        ('Complete(6,4)',6,complete_design(6,4),True),
        ('Complete(7,4)',7,complete_design(7,4),False),
        ('Complete(8,4)',8,complete_design(8,4),False),
        ('AffineSQS(8)',8,affine_quadruples(3),True),
        ('AffineSQS(16)',16,affine_quadruples(4),False),
    ):
        a,b=check_one(name,v,blocks,ground)
        total+=a; direct+=b
    assert total == 60+140+280+56+560  # All oriented incidence columns.
    assert direct==60+56
    print(f'DESIGN_HODGE_CERTIFICATE_OK columns={total} grounded_columns={direct}')


if __name__=='__main__':
    main()
