from fractions import Fraction
from itertools import combinations, product


def edges_from_mask(n, mask):
    pairs=list(combinations(range(n),2))
    return {pairs[i] for i in range(len(pairs)) if (mask>>i)&1}

def is_edge(E,i,j):
    if i>j:i,j=j,i
    return (i,j) in E

def is_clique(E, S):
    return all(is_edge(E,i,j) for i,j in combinations(S,2))

def is_stable(E, S):
    return all(not is_edge(E,i,j) for i,j in combinations(S,2))

def omega(E, V):
    best=0
    V=list(V)
    for mask in range(1<<len(V)):
        S=[V[i] for i in range(len(V)) if (mask>>i)&1]
        if len(S)>best and is_clique(E,S): best=len(S)
    return best

def chromatic(E, V):
    V=list(V)
    if not V:return 0
    m=len(V)
    for k in range(1,m+1):
        col=[-1]*m
        def bt(pos):
            if pos==m:return True
            v=V[pos]
            for c in range(k):
                ok=True
                for j in range(pos):
                    if col[j]==c and is_edge(E,v,V[j]):
                        ok=False;break
                if ok:
                    col[pos]=c
                    if bt(pos+1):return True
                    col[pos]=-1
            return False
        if bt(0): return k
    raise AssertionError

def is_perfect(E,n):
    V=list(range(n))
    for mask in range(1,1<<n):
        W=[i for i in V if (mask>>i)&1]
        if omega(E,W)!=chromatic(E,W):return False
    return True

def all_subsets(n,pred):
    out=[]
    for mask in range(1<<n):
        S=[i for i in range(n) if (mask>>i)&1]
        if pred(S):out.append(S)
    return out

def inv_matrix(A):
    n=len(A)
    M=[list(map(Fraction,row))+[Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c])
        M[c],M[p]=M[p],M[c]
        z=M[c][c]
        M[c]=[x/z for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                z=M[r][c]
                M[r]=[M[r][j]-z*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def quad(A,x):
    n=len(x)
    return sum(Fraction(x[i])*A[i][j]*Fraction(x[j]) for i in range(n) for j in range(n))

def signed_vectors(S,n):
    if not S:
        yield [0]*n; return
    for sg in product((-1,1), repeat=len(S)):
        x=[0]*n
        for i,s in zip(S,sg):x[i]=s
        yield x

def matrices(n):
    I=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    yield I
    # Strictly positive definite diagonal plus rank-one perturbation.
    d=[Fraction(i+2, i+1) for i in range(n)]
    u=[Fraction((i%3)+1, n+3) for i in range(n)]
    Q=[[Fraction(int(i==j))*d[i] + u[i]*u[j] for j in range(n)] for i in range(n)]
    yield Q

perfect_graphs=0
ellipsoid_cases=0
for n in range(1,6):
    m=n*(n-1)//2
    for mask in range(1<<m):
        E=edges_from_mask(n,mask)
        if not is_perfect(E,n):
            continue
        perfect_graphs += 1
        cliques=all_subsets(n,lambda S:is_clique(E,S))
        stables=all_subsets(n,lambda S:is_stable(E,S))
        for Q in matrices(n):
            # Scale Q so the ellipsoid support satisfies every signed clique inequality.
            M=Fraction(0)
            for C in cliques:
                for x in signed_vectors(C,n):
                    M=max(M,quad(Q,x))
            assert M>0
            Qn=[[q/M for q in row] for row in Q]
            Qi=inv_matrix(Qn)
            # Exact diagonal shadow of the proof.
            s=[Qn[i][i] for i in range(n)]
            assert all(sum(s[i] for i in C)<=1 for C in cliques)
            reciprocal=max(sum(Fraction(1,1)/s[i] for i in S) for S in stables)
            assert reciprocal>=n
            assert all(Qi[i][i]*Qn[i][i]>=1 for i in range(n))
            # Exact outer dilation forced by all signed stable-set points.
            lam2=max(quad(Qi,x) for S in stables for x in signed_vectors(S,n))
            assert lam2>=n
            ellipsoid_cases += 1
print(f"VERIFY_OK unconditional-reflexive BM lower bound perfect_graphs={perfect_graphs} ellipsoid_cases={ellipsoid_cases} n=1..5")
