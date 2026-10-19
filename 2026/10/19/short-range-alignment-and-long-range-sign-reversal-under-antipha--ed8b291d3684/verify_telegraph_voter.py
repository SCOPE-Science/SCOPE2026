"""Independent full-generator test for the finite telegraph-boundary voter model.
Pure Python 3 standard library. The analytical proof is in RESULT.md.
"""

def solve(A,b):
    A=[list(map(float,row))+[float(bb)] for row,bb in zip(A,b)]
    n=len(A)
    for k in range(n):
        piv=max(range(k,n),key=lambda z:abs(A[z][k])); assert abs(A[piv][k])>1e-12
        A[k],A[piv]=A[piv],A[k]
        row=A[k]; z=row[k]
        for t in range(k,n+1):row[t]/=z
        for i in range(k+1,n):
            factor=A[i][k]
            if not factor:continue
            cur=A[i]
            for j in range(k+1,n+1):cur[j]-=factor*row[j]
            cur[k]=0.0
    x=[0.0]*n
    for i in range(n-1,-1,-1):x[i]=A[i][n]-sum(A[i][j]*x[j] for j in range(i+1,n))
    return x

def moments(n,kappa):
    A=[[0.0]*n for _ in range(n)]
    for i in range(n):
        A[i][i]=2+4*kappa
        if i:A[i][i-1]=-1
        if i<n-1:A[i][i+1]=-1
    rhs=[0.0]*n;rhs[0]=1;rhs[-1]=-1
    a=solve(A,rhs)
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    idx={p:k for k,p in enumerate(pairs)}
    B=[[0.0]*len(pairs) for _ in pairs];q=[0.0]*len(pairs)
    for k,(i,j) in enumerate(pairs):
        B[k][k]=4
        for u,v in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if u==v:q[k]+=1
            elif u==-1:q[k]+=a[v]
            elif v==n:q[k]-=a[u]
            else:B[k][idx[tuple(sorted((u,v)))]]-=1
    b=solve(B,q)
    return a,dict(zip(pairs,b))

def direct_generator(n,kappa):
    S=1<<(n+1)
    Q=[[0.0]*S for _ in range(S)]
    def spin(state,j):return 1 if ((state>>j)&1) else -1
    for s in range(S):
        z=spin(s,n)
        Q[s][s^(1<<n)]+=kappa
        for i in range(n):
            for j in (i-1,i+1):
                other=z if j==-1 else (-z if j==n else spin(s,j))
                if spin(s,i)!=other:Q[s][s^(1<<i)]+=0.5
        Q[s][s]=-sum(Q[s])
    T=[[Q[j][i] for j in range(S)] for i in range(S)]
    T[-1]=[1.0]*S
    rr=[0.0]*S;rr[-1]=1.0
    p=solve(T,rr)
    assert min(p)>-1e-10
    a=[sum(v*spin(s,n)*spin(s,i) for s,v in enumerate(p)) for i in range(n)]
    b={(i,j):sum(v*spin(s,i)*spin(s,j) for s,v in enumerate(p)) for i in range(n) for j in range(i+1,n)}
    return a,b

def main():
    checked=0
    for n in range(2,7):
        for rate in (0.01,0.2,0.4070307623281496,1.0,10.0):
            a,b=moments(n,rate)
            da,db=direct_generator(n,rate)
            assert max(abs(x-y) for x,y in zip(a,da))<1e-9
            for pair in b:
                assert abs(b[pair]-db[pair])<1e-9,(n,rate,pair)
                checked+=1
            assert all(b[i,i+1]>0 for i in range(n-1))
    for r in (0.001,0.1,0.4,1.0,10.0,100.0):
        _,b=moments(4,r)
        f=(32*r*r+14*r-11)/(11*(16*r*r+20*r+5))
        assert abs(b[0,3]-f)<1e-10
    print('PASS:',checked,'independent full-generator pair comparisons and 6 exact-formula checks')
if __name__=='__main__':main()
