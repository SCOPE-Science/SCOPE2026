"""Exact finite-ring checks of the majority-cellular-automaton stabilization theorem.

No third-party packages. Enumeration is evidence at tested sizes, not a proof
for arbitrary ring length or of the limiting Poisson distribution.
"""

def update(x,n):
    out=0
    for i in range(n):
        q=((x>>((i-1)%n))&1)+((x>>i)&1)+((x>>((i+1)%n))&1)
        if q>=2:out|=1<<i
    return out

def transient(x,n):
    seen={};t=0
    while x not in seen:
        seen[x]=t;t+=1;x=update(x,n)
    return seen[x],t-seen[x]

def predicted(x,n):
    e=[((x>>i)^(x>>((i+1)%n)))&1 for i in range(n)]
    if all(e):return 0
    d=0;best=0
    j=e.index(0)
    for k in range(1,n+1):
        if e[(j+k)%n]:d+=1
        else:best=max(best,d);d=0
    return best//2

def matmul(A,B):
    z=len(A);C=[[0]*z for _ in range(z)]
    for i in range(z):
        for k,v in enumerate(A[i]):
            if v:
                for j,w in enumerate(B[k]):
                    if w:C[i][j]+=v*w
    return C

def trace_matrix(n,t):
    L=2*t+2;dim=2*L;M=[[0]*dim for _ in range(dim)]
    for j in range(L):
        for p in (0,1):
            src=2*j+p
            M[src][p]+=1
            if j<L-1:M[src][2*(j+1)+(1-p)]+=1
    P=[[int(i==j) for j in range(dim)] for i in range(dim)]
    for _ in range(n):P=matmul(P,M)
    return sum(P[i][i] for i in range(dim))+2*(n%2==0)

def main():
    states=0;matrix_tests=0;max_tests=0
    for n in range(3,13):
        tlist=[]
        for x in range(1<<n):
            tau,period=transient(x,n)
            assert tau==predicted(x,n),(n,x,tau,predicted(x,n))
            assert period in (1,2)
            if period==2:assert n%2==0 and all((x>>i&1)!=(x>>((i+1)%n)&1) for i in range(n))
            tlist.append(tau);states+=1
        assert max(tlist)==(n-1)//2
        assert tlist.count(max(tlist))==2*n
        max_tests+=1
        for t in range(0,n//2+2):
            actual=sum(v<=t for v in tlist)
            predicted_count=trace_matrix(n,t)
            assert actual==predicted_count,(n,t,actual,predicted_count)
            matrix_tests+=1
    print('VERIFY_OK independent_configuration_tests',states,
          'matrix_count_tests',matrix_tests,'sharp_maximum_tests',max_tests)

if __name__=='__main__':main()
