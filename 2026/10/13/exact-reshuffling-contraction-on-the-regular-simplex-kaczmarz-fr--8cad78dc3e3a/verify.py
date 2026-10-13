from fractions import Fraction as F
from itertools import permutations
from math import factorial

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def mt(A):
    return [list(x) for x in zip(*A)]

def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(s,A):
    return [[s*x for x in row] for row in A]

def c_sum(n):
    q=F(n+1,n)
    return -F(1,n)+F(1,n**3)*sum(F(n-l)*q**(2*l) for l in range(n))

def c_closed(n):
    return F(n,(2*n+1)**2)*(F(n+1,n)**(2*n+2)-7-F(7,n)-F(2,n*n))

def projectors(n):
    m=n+1
    # q_i=e_i-(1/m)1 in ambient R^m; v_i v_i^T=((n+1)/n) q_i q_i^T
    I=eye(m)
    out=[]
    for i in range(m):
        q=[F(-1,m) for _ in range(m)]
        q[i]+=1
        P=[]
        for a in range(m):
            P.append([I[a][b]-F(m,n)*q[a]*q[b] for b in range(m)])
        out.append(P)
    return out

def epoch(P,perm):
    T=eye(len(P))
    for i in perm:
        T=mm(P[i],T)
    return T

def target_gram(n,c):
    m=n+1
    J=[[F(1,m) for _ in range(m)] for __ in range(m)]
    H=[[F(int(i==j))-J[i][j] for j in range(m)] for i in range(m)]
    return madd(J,scale(c,H))

known={1:F(0),2:F(1,32),3:F(58,2187),4:F(5673,262144),5:F(879916,48828125)}
for n in range(1,6):
    c=c_sum(n)
    assert c==c_closed(n)==known[n]
    P=projectors(n)
    m=n+1
    G=[[F(0) for _ in range(m)] for __ in range(m)]
    count=0
    for perm in permutations(range(m)):
        T=epoch(P,perm)
        G=madd(G,mm(mt(T),T))
        count+=1
    assert count==factorial(m)
    G=scale(F(1,count),G)
    assert G==target_gram(n,c)
    d=F(n-1,n)**(n+1)
    if n==2: assert d==F(1,8)
    if n==3: assert d==F(16,81)

for n in range(1,20):
    assert c_sum(n)==c_closed(n)
print('VERIFY_OK')
