"""Independent exact finite checks of joint orbit-statistics ranks and relations."""
from itertools import product
from sympy import Matrix

def subspaces(p,r):
    E=list(product(range(p),repeat=r)); number={x:i for i,x in enumerate(E)}; N=len(E)
    add=[[number[tuple((a+b)%p for a,b in zip(E[i],E[j]))] for j in range(N)] for i in range(N)]
    def extend(H,g):
        mul=[0];v=0
        for _ in range(1,p):v=add[v][g];mul.append(v)
        return frozenset(add[u][v] for u in H for v in mul)
    all_sub={frozenset([0])};pending=[frozenset([0])]
    for H in pending:
        for g in range(N):
            if g not in H:
                U=extend(H,g)
                if U not in all_sub:all_sub.add(U);pending.append(U)
    S=sorted(all_sub,key=lambda h:(len(h),tuple(sorted(h)))); dims={H:next(j for j in range(r+1) if p**j==len(H)) for H in S}
    M=Matrix([[N*len(H&K)//(len(H)*len(K)) for K in S] for H in S]);
    D=Matrix([[int(dims[K]==j) for K in S] for j in range(r+1)])
    rank=M.col_join(D).rank(); target=sum(1 for H in S if len(H)==p)+r
    assert rank==target,(p,r,rank,target)
    if r>=3:
        U,W=[H for H in S if dims[H]==2][:2]
        linesU=[L for L in S if dims[L]==1 and L<=U]
        linesW=[L for L in S if dims[L]==1 and L<=W]
        z=Matrix([p if K==U else -p if K==W else -int(K in linesU)+int(K in linesW) for K in S])
        assert M*z==Matrix.zeros(len(S),1)
        assert D*z==Matrix.zeros(r+1,1)
    print('OK',p,r,'subgroups',len(S),'rank',rank,'nullity',len(S)-rank)
for p,r in [(2,2),(2,3),(2,4),(3,2),(3,3)]:subspaces(p,r)
print('VERIFY_OK')
