"""Exact-rational cross-check for graph heat transports on clique bouquets.

Run: python verify.py. All assertions use fractions, and Wasserstein dual
maximization is independent of the claimed closed-form transports.
"""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache


def add(A, B):
    return [[x + y for x, y in zip(row, other)]
            for row, other in zip(A, B)]


def scalar(a, A):
    return [[a * x for x in row] for row in A]


def matmul(A, B):
    Bt = list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) for col in Bt]
            for row in A]


def data(profile, base):
    k = sum(profile)
    N = k+1
    groups = []
    j = 1
    for d in profile:
        groups.append(tuple(range(j,j+d)))
        j += d
    zero = [[F(0) for _ in range(N)] for _ in range(N)]
    P0 = [[F(1,N) for _ in range(N)] for _ in range(N)]
    v = [k]+[-1]*k
    PN = [[F(v[i]*v[j],k*N) for j in range(N)] for i in range(N)]
    P1 = [row[:] for row in zero]
    for block in groups:
        d = len(block)
        for i in block:
            for j in block:
                P1[i][j] += F(1,d)
    for i in range(1,N):
        for j in range(1,N):
            P1[i][j] -= F(1,k)
    Ps = []
    for block in groups:
        d = len(block)
        P = [row[:] for row in zero]
        for i in block:
            for j in block:
                P[i][j] += (F(1) if i == j else F(0)) - F(1,d)
        Ps.append(P)
    identity = [[F(i==j) for j in range(N)] for i in range(N)]
    assert add(add(P0,PN),add(P1, sum_matrices(Ps,N))) == identity
    # Directly verify that the exhibited projections are L-eigenspaces.
    edges = [(0,i) for i in range(1,N)]
    for block in groups:
        edges += [(i,j) for i in block for j in block if i<j]
    L = [row[:] for row in zero]
    for i,j in edges:
        L[i][i] += 1; L[j][j] += 1
        L[i][j] -= 1; L[j][i] -= 1
    for P,lam in [(P0,0),(P1,1),(PN,N)]+[(Ps[i],len(groups[i])+1) for i in range(len(groups))]:
        assert matmul(L,P) == scalar(F(lam),P)
        assert matmul(P,P) == P
    a = F(1,base)
    c = a**N
    H = add(P0,add(scalar(c,PN),scalar(a,P1)))
    for block,P in zip(groups,Ps):
        H = add(H,scalar(a**(len(block)+1),P))
    assert all(sum(row)==1 and all(v>=0 for v in row) for row in H)
    assert all(H[i][j]==H[j][i] for i in range(N) for j in range(N))
    return H,groups,a,c


def sum_matrices(Ps,N):
    A = [[F(0) for _ in range(N)] for _ in range(N)]
    for P in Ps:
        A=add(A,P)
    return A


@lru_cache(None)
def integral_group_potentials(d):
    # Anchor the hub at zero. Integer 1-Lipschitz potentials have leaf
    # values in {-1,0,1}; within a clique, spread at most one.
    return [t for t in product((-1,0,1),repeat=d) if max(t)-min(t)<=1]


def exact_dual_w1(diff,groups):
    # The bounded network-difference polytope is integral (incidence
    # constraints), so all its extreme potentials are integral.
    ans=F(0)
    for group in groups:
        q=[diff[j] for j in group]
        ans+=max(sum(x*y for x,y in zip(q,t))
                 for t in integral_group_potentials(len(group)))
    return ans


def closed_w1(x,y,groups,a,c):
    k=sum(map(len,groups))
    if x==0 or y==0:
        u=y if x==0 else x
        d=next(len(group) for group in groups if u in group)
        return c+2*F(k-d,k)*(a-c)
    gx=next(i for i,group in enumerate(groups) if x in group)
    gy=next(i for i,group in enumerate(groups) if y in group)
    if gx==gy:
        return a**(len(groups[gx])+1)
    return 2*a


def compositions(k):
    for cuts in product((0,1),repeat=k-1):
        profile=[];d=1
        for bit in cuts:
            if bit:
                profile.append(d);d=1
            else:d+=1
        profile.append(d)
        yield tuple(profile)


def main():
    cases=0; comparisons=0; compositions_seen=0
    for k in range(1,9):
        for profile in compositions(k):
            compositions_seen+=1
            for base in (2,3):
                H,groups,a,c=data(profile,base)
                N=len(H)
                for x in range(N):
                    for y in range(x+1,N):
                        diff=[u-v for u,v in zip(H[x],H[y])]
                        independent=exact_dual_w1(diff,groups)
                        formula=closed_w1(x,y,groups,a,c)
                        assert independent == formula, (profile,base,x,y,independent,formula)
                        comparisons += 1
                # Lipschitz norm is max W1 across actual edges.
                predicted=max(c+2*F(k-d,k)*(a-c) for d in profile)
                if len(profile)==1:
                    assert predicted==c
                edges=[(0,j) for j in range(1,N)]
                edges += [(i,j) for group in groups for i in group for j in group if i<j]
                independent=max(exact_dual_w1([u-v for u,v in zip(H[x],H[y])],groups)
                                for x,y in edges)
                assert independent==predicted,(profile,base,independent,predicted)
                cases += 1
    print('CERTIFICATE_OK compositions=',compositions_seen,
          'exact_rational_heat_instances=',cases,
          'W1_pairwise_dual_comparisons=',comparisons)

if __name__=='__main__':
    main()
