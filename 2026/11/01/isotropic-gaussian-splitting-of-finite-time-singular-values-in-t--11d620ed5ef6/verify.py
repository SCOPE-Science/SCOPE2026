"""Exact finite-case regression checks for the twisted baker derivative theorem.
Standard library only.  Infinite assertions follow from the paper's proof.
"""
from fractions import Fraction
from itertools import product


def matmul(A,B):
    m=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(m)] for i in range(m)]


def matrices(m):
    left=[[2 if i==j==0 else int(i==j) for j in range(m)] for i in range(m)]
    right=[[0]*m for _ in range(m)]
    right[0][m-1]=-2
    for j in range(1,m): right[j][j-1]=1
    return left,right


def check_derivatives():
    cases=0
    for m in range(2,7):
        L,R=matrices(m)
        for n in range(1,9):
            for word in product((0,1),repeat=n):
                P=[[int(i==j) for j in range(m)] for i in range(m)]
                r=0
                c=[0]*m
                for branch in word:
                    P=matmul(R if branch else L,P)
                    r=(r+branch)%m
                    c[-r % m]+=1
                diag=[sum(P[i][j]**2 for i in range(m)) for j in range(m)]
                assert diag==[4**k for k in c]
                assert sum(c)==n
                assert all(sum(int(P[i][j]!=0) for i in range(m))==1 for j in range(m))
                cases+=1
    return cases


def check_poisson():
    cases=0
    for m in range(2,18):
        # Basis and all pair-difference observables, plus general test vectors.
        inputs=[]
        for i in range(m):
            a=[Fraction(int(j==i)) for j in range(m)]
            inputs.append(a)
        for i in range(m):
            for j in range(i+1,m):
                a=[Fraction(int(k==i)-int(k==j)) for k in range(m)]
                inputs.append(a)
        inputs.append([Fraction((j*j+3*j+1)%7) for j in range(m)])
        for a in inputs:
            mean=sum(a)/m
            f=[v-mean for v in a]
            g=[Fraction(0) for _ in range(m)]
            for j in range(m-1):
                g[j+1]=g[j]-2*f[j]
            for j in range(m):
                assert g[j]-(g[j]+g[(j+1)%m])/2 == f[j]
            predicted=sum(v*v for v in f)/m
            # Green-Kubo formula: 2 <f,g> - <f,f>.
            from_poisson=sum(2*f[j]*g[j]-f[j]*f[j] for j in range(m))/m
            # Martingale increment is +f_j (stay) or -f_j (move).
            from_martingale=sum((f[j]**2+(-f[j])**2)/2 for j in range(m))/m
            assert from_poisson==predicted==from_martingale
            cases+=1
    return cases


def check_moment_approach():
    comparisons=0
    for m in range(2,7):
        for n in range(1,10):
            # Dynamic-programming distribution for the number of visits to state 0.
            state={(0,0):1}
            for step in range(n):
                new={}
                for (r,k),v in state.items():
                    for branch in (0,1):
                        s=(r+branch)%m
                        t=k+int(s==0)
                        new[(s,t)]=new.get((s,t),0)+v
                state=new
            dp=[0]*(n+1)
            for (_,k),v in state.items(): dp[k]+=v
            direct=[0]*(n+1)
            for word in product((0,1),repeat=n):
                r=0;k=0
                for branch in word:
                    r=(r+branch)%m
                    k+=int(r==0)
                direct[k]+=1
            assert direct==dp and sum(dp)==2**n
            comparisons+=1
    return comparisons

if __name__=='__main__':
    a=check_derivatives()
    b=check_poisson()
    c=check_moment_approach()
    print(f'CHECK_OK derivative_words={a} poisson_vectors={b} exact_moment_distributions={c}')
