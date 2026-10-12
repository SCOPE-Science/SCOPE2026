from itertools import product

def mat_vec(A,v,p):
    return tuple(sum(A[i][j]*v[j] for j in range(len(v)))%p for i in range(len(A)))

def rank_mod(A,p):
    M=[list(r) for r in A]; r=0
    if not M: return 0
    for c in range(len(M[0])):
        k=next((i for i in range(r,len(M)) if M[i][c]%p),None)
        if k is None: continue
        M[r],M[k]=M[k],M[r]
        z=pow(M[r][c]%p,-1,p)
        M[r]=[(z*x)%p for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%p:
                z=M[i][c]%p
                M[i]=[(M[i][j]-z*M[r][j])%p for j in range(len(M[0]))]
        r+=1
    return r

def invertible(A,p):
    return rank_mod(A,p)==len(A)

def bracket(A,x,y,p):
    a,u=x[0],x[1:]; b,v=y[0],y[1:]
    return mat_vec(A,tuple((a*v[i]-b*u[i])%p for i in range(len(u))),p)

def part_key(x,p):
    a=x[0]; u=x[1:]
    if a==0: return ("V",)
    z=pow(a,-1,p)
    return ("O",)+tuple((z*w)%p for w in u)

def verify_case(p,n,A):
    assert invertible(A,p)
    zero=(0,)*(n+1)
    V=[x for x in product(range(p),repeat=n+1) if x!=zero]
    keys={x:part_key(x,p) for x in V}
    Q=p**n
    counts={}
    for x in V: counts[keys[x]]=counts.get(keys[x],0)+1
    assert sorted(counts.values())==sorted([Q-1]+[p-1]*Q)

    for x in V:
        d=0
        for y in V:
            if x==y: continue
            actual=any(bracket(A,x,y,p))
            predicted=keys[x]!=keys[y]
            assert actual==predicted
            d+=actual
        assert d==(Q*(p-1) if x[0]==0 else p*(Q-1))

def all_GL(p,n):
    for vals in product(range(p),repeat=n*n):
        A=[list(vals[i*n:(i+1)*n]) for i in range(n)]
        if invertible(A,p): yield A

def mm(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def sm(c,A,p):
    return [[c*x%p for x in r] for r in A]

def prop_sim(A,B,p):
    for c in range(1,p):
        cB=sm(c,B,p)
        for P in all_GL(p,len(A)):
            if mm(P,A,p)==mm(cB,P,p): return True
    return False

for p,n in [(2,1),(2,2),(2,3),(3,2),(5,2)]:
    I=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    verify_case(p,n,I)
    if n>=2:
        J=[r[:] for r in I]; J[0][1]=1
        verify_case(p,n,J)
        if p>2:
            D=[r[:] for r in I]; D[1][1]=2
            verify_case(p,n,D)

for p in (2,3):
    I=[[1,0],[0,1]]
    J=[[1,1],[0,1]]
    assert not prop_sim(I,J,p)

print("VERIFY_OK")
