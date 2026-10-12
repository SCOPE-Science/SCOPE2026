"""Reproducible finite-field tests for endomorphism counts of radical-square-zero cyclic quiver algebras."""
from itertools import product
from collections import Counter


def mul(u,v,n,p):
    return tuple((u[i]*v[i])%p for i in range(n))+tuple((u[j]*v[n+j]+u[n+j]*v[(j+1)%n])%p for j in range(n))


def add(u,v,p):
    return tuple((a+b)%p for a,b in zip(u,v))


def neg(u,p):
    return tuple((-a)%p for a in u)


def all_vectors(n,p):
    return list(product(range(p),repeat=2*n))


def matrix_rank(columns,p):
    if not columns: return 0
    A=[list(row) for row in zip(*columns)]
    rows,cols=len(A),len(A[0]); rank=0
    for c in range(cols):
        k=next((r for r in range(rank,rows) if A[r][c]%p),None)
        if k is None: continue
        A[rank],A[k]=A[k],A[rank]
        inv=pow(A[rank][c],-1,p)
        A[rank]=[(x*inv)%p for x in A[rank]]
        for r in range(rows):
            if r!=rank and A[r][c]:
                t=A[r][c]; A[r]=[(a-t*b)%p for a,b in zip(A[r],A[rank])]
        rank+=1
        if rank==rows: break
    return rank


def direct_rank_poly(n,p):
    # Enumerate all orthogonal idempotent lifts, then all possible arrow images.
    zero=(0,)*(2*n)
    one=(1,)*n+(0,)*n
    basis=[tuple(int(j==i) for j in range(2*n)) for i in range(2*n)]
    idem=[v for v in all_vectors(n,p) if mul(v,v,n,p)==v]
    radical=[(0,)*n+w for w in product(range(p),repeat=n)]
    result=Counter()
    for initial in product(idem,repeat=n-1):
        last=add(one,neg(tuple(sum(a[i] for a in initial)%p for i in range(2*n)),p),p)
        es=initial+(last,)
        if any(mul(x,x,n,p)!=x for x in es): continue
        if any(mul(es[i],es[j],n,p)!=zero for i in range(n) for j in range(n) if i!=j): continue
        allowed=[]
        for i in range(n):
            allowed.append([v for v in radical if mul(es[i],v,n,p)==v and mul(v,es[(i+1)%n],n,p)==v])
        for arrows in product(*allowed):
            images=es+arrows
            if any(mul(images[i],images[j],n,p)!=add(zero,tuple(0 for _ in range(2*n)),p) for i in range(n,2*n) for j in range(n,2*n)):
                raise AssertionError('radical square failure')
            # independently verify all multiplicative relations on the 2n basis
            for a in range(2*n):
                for b in range(2*n):
                    prod=mul(basis[a],basis[b],n,p)
                    actual=mul(images[a],images[b],n,p)
                    expected=zero
                    for k,c in enumerate(prod):
                        for _ in range(c): expected=add(expected,images[k],p)
                    assert actual==expected,(n,p,a,b,images)
            result[matrix_rank(images,p)]+=1
    return dict(sorted(result.items()))


def parametrized_rank_poly(n,p):
    result=Counter()
    for phi in product(range(n),repeat=n):
        k=len(set(phi))
        changes=sum(phi[j]!=phi[(j+1)%n] for j in range(n))
        counts=[sum(phi[j]==i and phi[(j+1)%n]==(i+1)%n for j in range(n)) for i in range(n)]
        cur={0:1}
        for cnt in counts:
            nxt=Counter()
            for rank,ways in cur.items():
                nxt[rank]+=ways
                nxt[rank+1]+=ways*(p**cnt-1)
            cur=nxt
        for r,ways in cur.items():result[k+r]+=ways*p**changes
    return dict(sorted(result.items()))


def transfer_count(n,q):
    B=[[1 if i==j else q*q if j==(i+1)%n else q for j in range(n)] for i in range(n)]
    X=[[int(i==j) for j in range(n)] for i in range(n)]
    for _ in range(n):
        X=[[sum(X[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return sum(X[i][i] for i in range(n))


def closed_count(n,q):
    return (q*q+(n-2)*q+1)**n + (q-1)**n*(n*(q**n+(-1)**n)-(q-1)**n)


def main():
    for n,p in [(2,2),(2,3),(3,2),(3,3),(4,2),(5,2)]:
        predicted=parametrized_rank_poly(n,p)
        assert sum(predicted.values())==closed_count(n,p)==transfer_count(n,p)
        if (n,p) in [(2,2),(2,3),(3,2)]:
            exact=direct_rank_poly(n,p)
            assert exact==predicted,(n,p,exact,predicted)
        print(f'n={n} q={p}:',predicted,'total=',sum(predicted.values()))
    print('VERIFY_OK')

if __name__=='__main__':main()
