"""Standalone small-field computations of averaging projections and trace-similarity counts."""
from itertools import product
from math import prod

def mm(A,B,n,q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))

def vmm(X,Y,q):
    return tuple((x+y)%q for x,y in zip(X,Y))

def rank(A,n,q):
    x=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for c in range(n):
        u=next((i for i in range(r,n) if x[i][c]%q),None)
        if u is None:continue
        x[r],x[u]=x[u],x[r]
        a=pow(x[r][c],-1,q)
        x[r]=[v*a%q for v in x[r]]
        for i in range(n):
            if i!=r and x[i][c]:
                k=x[i][c];x[i]=[(x[i][j]-k*x[r][j])%q for j in range(n)]
        r+=1
    return r

def rank_one_projection_direct(n,q):
    N=n*n
    basis=[tuple(1 if k==i else 0 for k in range(N)) for i in range(N)]
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    counts={}
    samples=[]
    for B in product(range(q),repeat=N):
        if not any(B):continue
        b0=next(x for x in B if x)
        if b0!=1:continue # for q=2/3 representative of projective B always first nonzero 1
        BB=mm(B,B,n,q)
        left=[mm(e,B,n,q) for e in basis]
        right=[mm(B,e,n,q) for e in basis]
        for f in product(range(q),repeat=N):
            dot=lambda z:sum(a*b for a,b in zip(f,z))%q
            if dot(B)!=1:continue
            # Identity on basis: f_i*f_j BB = f_j * dot(e_i B) B = f_i * dot(B e_j) B
            ok=True
            for i in range(N):
                for j in range(N):
                    lhs=tuple(f[i]*f[j]*x%q for x in BB)
                    v=tuple((f[j]*dot(left[i])*x)%q for x in B)
                    w=tuple((f[i]*dot(right[j])*x)%q for x in B)
                    if lhs!=v or lhs!=w:ok=False;break
                if not ok:break
            if not ok:continue
            P1=tuple(dot(I)*x%q for x in B)
            r=rank(P1,n,q)
            counts[r]=counts.get(r,0)+1
            samples.append((B,f))
    return counts,samples

def gaussian(n,r,q):
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))

def predicted(n,q):
    return {r:gaussian(n,r,q)*q**(r*(n-r)+r*r-1) for r in range(1,n+1)}

def trace_similarity_classes(n,q):
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    Z=tuple(0 for _ in range(n*n))
    def determinant(A):
        if n==1:return A[0]
        if n==2:return (A[0]*A[3]-A[1]*A[2])%q
        return (A[0]*(A[4]*A[8]-A[5]*A[7])-A[1]*(A[3]*A[8]-A[5]*A[6])+A[2]*(A[3]*A[7]-A[4]*A[6]))%q
    patterns=set()
    for A in product(range(q),repeat=n*n):
        tr=sum(A[i*n+i] for i in range(n))%q
        if n==1:ch=( -tr%q,1)
        elif n==2:ch=(determinant(A),-tr%q,1)
        else:
            sigma=sum(A[i*n+i]*A[j*n+j]-A[i*n+j]*A[j*n+i] for i in range(3) for j in range(i+1,3))%q
            ch=(-determinant(A)%q,sigma,-tr%q,1)
        powers=[I]
        for i in range(1,n+1):powers.append(mm(powers[-1],A,n,q))
        mip=None
        for d in range(1,n+1):
            for coeff in product(range(q),repeat=d):
                val=tuple((powers[d][k]+sum(coeff[j]*powers[j][k] for j in range(d)))%q for k in range(n*n))
                if val==Z:
                    mip=coeff+(1,)
                    break
            if mip is not None:break
        assert mip is not None
        patterns.add((ch,mip,tr))
    counts={t:sum(p[2]==t for p in patterns) for t in range(q)}
    return counts

def kq(n,q):
    dp=[0]*(n+1);dp[0]=1
    for d in range(1,n+1):
        for r in range(d,n+1):dp[r]+=q*dp[r-d]
    return dp[n]

if __name__=='__main__':
    for q in [2,3]:
        counts, samples=rank_one_projection_direct(2,q)
        assert counts==predicted(2,q),(q,counts,predicted(2,q))
        print('DIRECT_IDEMPOTENT_AVERAGING',q,counts,'total',sum(counts.values()))
    for q,n in [(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]:
        got=trace_similarity_classes(n,q)
        total=kq(n,q);sub=kq(n//q,q) if n%q==0 else 0 # q prime in these cases
        want={a:(total + (q-1)*sub if a==0 else total-sub)//q for a in range(q)}
        assert got==want,(q,n,got,want)
        print('TRACE_SIMILARITY_CLASSES',q,n,got,'Kq',total)
    print('RANK_ONE_AVERAGING_AND_TRACE_CLASSES_OK')
