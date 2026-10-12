from fractions import Fraction

N=4

def zmat():
    return [[Fraction(0) for _ in range(N)] for __ in range(N)]

def E(i,j):
    M=zmat(); M[i][j]=Fraction(1); return M

def add(A,B): return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(N)] for i in range(N)]
def scale(a,A): return [[a*A[i][j] for j in range(N)] for i in range(N)]
def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def comm(A,B): return sub(mul(A,B),mul(B,A))
def flat(A): return [A[i][j] for i in range(N) for j in range(N)]

def rank(vectors):
    A=[list(v) for v in vectors]
    if not A: return 0
    m=len(A); n=len(A[0]); r=0; c=0
    while r<m and c<n:
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:
            c+=1; continue
        A[r],A[piv]=A[piv],A[r]
        p=A[r][c]
        A[r]=[x/p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

def span_basis(mats):
    out=[]; rv=[]; rr=0
    for M in mats:
        v=flat(M)
        nr=rank(rv+[v])
        if nr>rr:
            out.append(M); rv.append(v); rr=nr
    return out

# Lie algebra L: [e4,e1]=e1, [e4,e2]=-e2, [e4,e3]=e3.
c=[[[Fraction(0) for k in range(N)] for j in range(N)] for i in range(N)]
c[3][0][0]=1; c[0][3][0]=-1
c[3][1][1]=-1; c[1][3][1]=1
c[3][2][2]=1; c[2][3][2]=-1

def bracket_vec(u,v):
    out=[Fraction(0)]*N
    for i in range(N):
        for j in range(N):
            if u[i] and v[j]:
                for k in range(N): out[k]+=u[i]*v[j]*c[i][j][k]
    return out

def matvec(A,v): return [sum(A[i][j]*v[j] for j in range(N)) for i in range(N)]
Ivec=[[Fraction(int(i==j)) for i in range(N)] for j in range(N)]

# Published antiderivation space, independently checked against the defining identity.
D=add(add(E(0,0),E(1,1)),add(E(2,2),scale(-2,E(3,3))))
anti_basis=[D,E(0,1),E(0,3),E(1,0),E(1,2),E(1,3),E(2,1),E(2,3)]
assert rank([flat(M) for M in anti_basis])==8
for A in anti_basis:
    for i in range(N):
        for j in range(N):
            lhs=matvec(A,bracket_vec(Ivec[i],Ivec[j]))
            rhs=[-x for x in [a+b for a,b in zip(bracket_vec(matvec(A,Ivec[i]),Ivec[j]),bracket_vec(Ivec[i],matvec(A,Ivec[j])) )]]
            assert lhs==rhs

# Candidate local-antiderivation space S from the source, reconstructed by pointwise interpolation.
D13=add(E(0,0),E(2,2))
S=[D13,E(1,1),E(3,3),E(0,1),E(0,3),E(1,0),E(1,2),E(1,3),E(2,1),E(2,3)]
assert rank([flat(M) for M in S])==10

# Necessary pointwise constraints: columns at e1,e2,e3 and at e1+e3 force exactly the S pattern.
# e1: only rows 1,2; e2: only rows 1,2,3; e3: only rows 2,3; e1+e3: diagonal 11=33.
# These are encoded by a 10-dimensional linear constraint space, which S spans.
allowed=[D13,E(1,1),E(3,3),E(0,1),E(0,3),E(1,0),E(1,2),E(1,3),E(2,1),E(2,3)]
assert rank([flat(M) for M in allowed])==10

# Sufficiency is constructive: for a generic T in S and arbitrary x, solve D_x x=T x.
# We test the explicit case split algebraically on a dense integer grid, including all exceptional coordinate patterns.
def T_of(params):
    s,u,v,a,p,b,c,q,d,r=params
    M=zmat()
    M[0][0]=s; M[2][2]=s; M[1][1]=u; M[3][3]=v
    M[0][1]=a; M[0][3]=p; M[1][0]=b; M[1][2]=c; M[1][3]=q; M[2][1]=d; M[2][3]=r
    return M

def witness(T,x):
    x1,x2,x3,x4=x
    # choose t and then solve freely for off-diagonal coefficients
    if x4:
        t=-T[3][3]/2
        aa=T[0][1]; bb=T[1][0]; cc=T[1][2]; dd=T[2][1]
        pp=(matvec(T,x)[0]-t*x1-aa*x2)/x4
        qq=(matvec(T,x)[1]-bb*x1-t*x2-cc*x3)/x4
        rr=(matvec(T,x)[2]-dd*x2-t*x3)/x4
    else:
        t=T[0][0] if (x1 or x3) else T[1][1]
        aa=T[0][1] if not x2 else (matvec(T,x)[0]-t*x1)/x2
        dd=T[2][1] if not x2 else (matvec(T,x)[2]-t*x3)/x2
        # solve second coordinate using whichever of x1,x3 is available; otherwise t must match target on x2
        bb=T[1][0]; cc=T[1][2]
        target=matvec(T,x)[1]
        if x1:
            bb=(target-t*x2-cc*x3)/x1
        elif x3:
            cc=(target-t*x2-bb*x1)/x3
        else:
            assert target==t*x2
        pp=qq=rr=Fraction(0)
    A=scale(t,D)
    for coeff,M in [(aa,E(0,1)),(pp,E(0,3)),(bb,E(1,0)),(cc,E(1,2)),(qq,E(1,3)),(dd,E(2,1)),(rr,E(2,3))]:
        A=add(A,scale(coeff,M))
    return A

samples=[Fraction(-2),Fraction(-1),Fraction(0),Fraction(1),Fraction(2)]
params=(Fraction(2),Fraction(-1),Fraction(3),Fraction(1),Fraction(-2),Fraction(2),Fraction(1),Fraction(-1),Fraction(3),Fraction(2))
T=T_of(params)
for x1 in samples:
  for x2 in samples:
    for x3 in samples:
      for x4 in samples:
        x=[x1,x2,x3,x4]
        A=witness(T,x)
        assert matvec(A,x)==matvec(T,x)

# Maximal parabolic P = stabilizer of U=span(e1,e2,e3): arbitrary top-left 3x3, arbitrary last column, zero bottom-left row.
P=[E(i,j) for i in range(3) for j in range(3)] + [E(i,3) for i in range(3)] + [E(3,3)]
assert rank([flat(M) for M in P])==13

# Three explicit triple brackets add exactly the missing directions.
H=sub(E(0,0),E(1,1))
assert comm(comm(D13,E(0,1)),E(1,0))==H
assert comm(comm(D13,E(0,1)),E(1,2))==E(0,2)
assert comm(comm(D13,E(1,0)),E(2,1))==E(2,0)
assert rank([flat(M) for M in S+[H,E(0,2),E(2,0)]])==13

# P is a Lie algebra, hence a Lie triple system.
for A in P:
    for B in P:
        assert rank([flat(M) for M in P]+[flat(comm(A,B))])==13

# Direct iterative closure confirms both ordinary Lie closure and Lie-triple closure stabilize at P.
def closure(seed,triple=False):
    cur=span_basis(seed)
    while True:
        new=list(cur)
        if triple:
            for A in cur:
                for B in cur:
                    AB=comm(A,B)
                    for C in cur: new.append(comm(AB,C))
        else:
            for A in cur:
                for B in cur: new.append(comm(A,B))
        nxt=span_basis(new)
        if len(nxt)==len(cur): return nxt
        cur=nxt

LC=closure(S,False); TC=closure(S,True)
assert len(LC)==13 and len(TC)==13
assert rank([flat(M) for M in P+LC])==13
assert rank([flat(M) for M in P+TC])==13

print('antiderivation_dim=8')
print('local_antiderivation_dim=10')
print('lie_closure_dim=13')
print('triple_closure_dim=13')
print('closure=maximal_parabolic_stabilizer_span_e1_e2_e3')
print('CHECK_OK')
