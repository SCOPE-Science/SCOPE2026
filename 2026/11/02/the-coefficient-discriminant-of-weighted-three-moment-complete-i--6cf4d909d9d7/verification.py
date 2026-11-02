from itertools import product,combinations

def rank(M,p):
    if not M:return 0
    A=[[x%p for x in row] for row in M]; nr=len(A); nc=len(A[0]); k=0
    for j in range(nc):
        t=next((i for i in range(k,nr) if A[i][j]),None)
        if t is None:continue
        A[k],A[t]=A[t],A[k]; inv=pow(A[k][j],-1,p);A[k]=[(v*inv)%p for v in A[k]]
        for i in range(k+1,nr):
            mul=A[i][j]; A[i]=[(A[i][h]-mul*A[k][h])%p for h in range(nc)]
        k+=1
        if k==nr:break
    return k

def check(p,weights):
    n=len(weights); assert n==6 and p in (5,7,11)
    assert all(a%p for a in weights) and sum(weights)%p
    expected={tuple(1 if (mask>>i)&1 else 0 for i in range(n)) for mask in range(1,(1<<n)-1) if sum(weights[i] for i in range(n) if (mask>>i)&1)%p==0}
    observed=set();hits=0
    for first in range(n):
        for tail in product(range(p),repeat=n-first-1):
            X=(0,)*first+(1,)+tail
            if any(sum(a*pow(x,j,p) for a,x in zip(weights,X))%p for j in (1,2,3)):continue
            hits+=1
            J=[[a*(j*pow(x,j-1,p))%p for a,x in zip(weights,X)] for j in (1,2,3)]
            if rank(J,p)<3:observed.add(X)
    print({'p':p,'weights':weights,'complete_intersection_points_Fp':hits,'expected_singular':len(expected),'observed_singular':len(observed),'matches':observed==expected})
    assert observed==expected

if __name__=='__main__':
    check(5,[1,4,1,1,1,1])
    check(5,[1,1,1,1,1,1])
    check(7,[1,6,2,3,4,6])
    print('VERIFY_OK')
