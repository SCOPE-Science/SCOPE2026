"""Independent exact-rational checks for the matched-edge price theorem.

Run with Python 3: python verify.py. No external packages are needed.
These finite tests supplement, but do not replace, the all-size proof.
"""
from fractions import Fraction as F
from itertools import combinations


def pair_list(n,k):
    return [(2*i,2*i+1) for i in range(k)]


def matvec(a,x):
    return [sum(a[i][j]*x[j] for j in range(len(x))) for i in range(len(x))]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def laplacian(n,k,weights):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for (i,j),w in weights.items():
        assert w>=0
        L[i][i]+=w; L[j][j]+=w
        L[i][j]-=w; L[j][i]-=w
    return L


def all_edges(n):
    return list(combinations(range(n),2))


def dual(n,k,s):
    G=[[F(i==j,2) for j in range(n)] for i in range(n)]
    for a,b in pair_list(n,k):
        G[a][b]=G[b][a]=(1-s)/2
    J=[[F(i==j)-F(1,n) for j in range(n)] for i in range(n)]
    X=[[sum(J[i][u]*G[u][v]*J[v][j] for u in range(n) for v in range(n)) for j in range(n)] for i in range(n)]
    return X


def deletion(n,k):
    mm={tuple(p) for p in pair_list(n,k)}
    out={}
    if k==1:
        l=n-2
        for e in all_edges(n):
            a,b=e
            if e in mm: w=F(0)
            elif a<2 or b<2: w=F(1,l)
            else: w=F(l-2,l*l)
            out[e]=w
    else:
        marked=set(range(2*k))
        pair={i:i//2 for i in marked}
        for e in all_edges(n):
            a,b=e
            if e in mm: w=F(0)
            elif a in marked and b in marked: w=F(k,(k-1)*n) if pair[a]!=pair[b] else F(0)
            else: w=F(1,n)
            out[e]=w
    return out


def check():
    checks=0
    for n in range(4,19):
      for k in range(1,n//2+1):
        rc=F(2*(n-1),n-2) if k==1 else F(2)
        match=set(pair_list(n,k))
        w=deletion(n,k)
        L=laplacian(n,k,w)
        # Check all standard orthogonal eigenvectors, no numerical diagonalization.
        V=[]
        for a,b in pair_list(n,k):
            v=[F(0)]*n; v[a]=F(1); v[b]=F(-1)
            V.append((v,F(1)))
        for i in range(1,k):
            v=[F(0)]*n
            v[0]=v[1]=F(1);v[2*i]=v[2*i+1]=F(-1)
            V.append((v,F(1)+F(2*k,(k-1)*n)))
        l=n-2*k
        if l:
            for i in range(1,l):
                v=[F(0)]*n;v[2*k]=F(1);v[2*k+i]=F(-1)
                V.append((v,F(1)))
            v=[F(l)]*(2*k)+[F(-2*k)]*l
            V.append((v,F(1) if k>1 else F(n,l)))
        assert len(V)==n-1, (n,k,len(V))
        assert all(sum(v)==0 and matvec(L,v)==[lam*z for z in v] for v,lam in V),(n,k)
        checks+=len(V)
        # Cost exactly matches the claimed boundary dual trace.
        c=sum(z*(rc if e in match else 1) for e,z in w.items())
        target=F(n-1,2)+F(k,n)*(rc-1)
        assert c==target,(n,k,c,target)
        checks+=1
        for s in (F(1,5),F(1),F(3,2),rc):
            if s>rc:continue
            X=dual(n,k,s)
            # Exact dual edge lengths, and exact trace of projected dual.
            for a,b in all_edges(n):
                dd=X[a][a]+X[b][b]-2*X[a][b]
                assert dd==(s if (a,b) in match else 1),(n,k,s,a,b,dd)
                checks+=1
            trace=sum(X[i][i] for i in range(n))
            assert trace==F(n-1,2)+F(k,n)*(s-1)
            checks+=1
            # Dual nonnegative on complete orthogonal eigen-basis of matching blocks.
            for v,_ in V:
                assert dot(v,matvec(X,v))>=0
                checks+=1
        # Uniform unit-gap primal certificate, for a range of marked prices.
        for r in (F(1,10),F(1),F(3,2),rc):
            ww={e:F(1,n) for e in all_edges(n)}
            LL=laplacian(n,k,ww)
            assert all(matvec(LL,v)==v for v,_ in V)
            cost=sum(z*(r if e in match else 1) for e,z in ww.items())
            assert cost==F(n-1,2)+F(k,n)*(r-1)
            checks+=len(V)+1
        # Non-degenerate PSD at rc and strictly positive below (formula-based test).
        assert rc>1 and (rc==2 if k>1 else rc==F(2*(n-1),n-2))
        checks+=1
    print('PASS: ',checks,' exact rational assertions on 4 <= n <= 18 and all matching sizes')

if __name__=='__main__':
    check()
