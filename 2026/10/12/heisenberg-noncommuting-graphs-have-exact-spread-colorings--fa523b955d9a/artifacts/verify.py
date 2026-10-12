from itertools import product, combinations

def invmod(a,p):
    return pow(a,-1,p)

class QuadField:
    def __init__(self,p):
        self.p=p
        if p not in (2,3):
            raise ValueError
        self.elts=[(a,b) for a in range(p) for b in range(p)]
        self.zero=(0,0)
        self.one=(1,0)

    def add(self,x,y):
        return ((x[0]+y[0])%self.p,(x[1]+y[1])%self.p)

    def neg(self,x):
        return ((-x[0])%self.p,(-x[1])%self.p)

    def sub(self,x,y):
        return self.add(x,self.neg(y))

    def mul(self,x,y):
        a,b=x; c,d=y
        if self.p==2:
            return ((a*c+b*d)%2,(a*d+b*c+b*d)%2)
        return ((a*c+2*b*d)%3,(a*d+b*c)%3)

    def pow(self,x,n):
        r=self.one
        while n:
            if n&1:
                r=self.mul(r,x)
            x=self.mul(x,x)
            n//=2
        return r

    def trace(self,x):
        return self.add(x,self.pow(x,self.p))[0] % self.p

def scalar_vec(c,v,p):
    return tuple((c*x)%p for x in v)

def normalize(v,p):
    j=next(i for i,x in enumerate(v) if x%p)
    c=invmod(v[j],p)
    return scalar_vec(c,v,p)

def rank_mod(rows,p):
    M=[list(r) for r in rows if any(x%p for x in r)]
    r=0
    if not M:
        return 0
    m=len(M[0])
    for c in range(m):
        pivot=next((i for i in range(r,len(M)) if M[i][c]%p),None)
        if pivot is None:
            continue
        M[r],M[pivot]=M[pivot],M[r]
        z=invmod(M[r][c]%p,p)
        M[r]=[(z*x)%p for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%p:
                z=M[i][c]%p
                M[i]=[(M[i][j]-z*M[r][j])%p for j in range(m)]
        r+=1
    return r

def standard_symp(v,w,p):
    n=len(v)//2
    return sum(v[i]*w[n+i]-w[i]*v[n+i] for i in range(n))%p

def projective_standard(p,n):
    pts={}
    for v in product(range(p),repeat=2*n):
        if any(v):
            pts[normalize(v,p)]=None
    P=list(pts)
    A=[[False]*len(P) for _ in P]
    for i,j in combinations(range(len(P)),2):
        if standard_symp(P[i],P[j],p):
            A[i][j]=A[j][i]=True
    return P,A

def no_independent_of_size(A,k):
    N=len(A)
    for S in combinations(range(N),k):
        if all(not A[i][j] for i,j in combinations(S,2)):
            return False
    return True

def gf_pair_to_fq4(x,y):
    return (x[0],x[1],y[0],y[1])

def trace_symp(F,X,Y):
    x,y=X; X2,Y2=Y
    det=F.sub(F.mul(x,Y2),F.mul(X2,y))
    return F.trace(det)

def projective_trace(F):
    p=F.p
    vectors=[(x,y) for x in F.elts for y in F.elts if (x,y)!=(F.zero,F.zero)]
    reps={}
    for X in vectors:
        reps[normalize(gf_pair_to_fq4(*X),p)]=X
    P=list(reps.values())
    A=[[False]*len(P) for _ in P]
    for i,j in combinations(range(len(P)),2):
        if trace_symp(F,P[i],P[j])%p:
            A[i][j]=A[j][i]=True
    return P,A

def spread_trace(F,P):
    p=F.p
    idx={}
    for i,X in enumerate(P):
        idx[normalize(gf_pair_to_fq4(*X),p)]=i
    parts=[]
    for a in F.elts:
        S=set()
        for x in F.elts:
            if x==F.zero:
                continue
            X=(x,F.mul(a,x))
            S.add(idx[normalize(gf_pair_to_fq4(*X),p)])
        parts.append(S)
    S=set()
    for y in F.elts:
        if y==F.zero:
            continue
        X=(F.zero,y)
        S.add(idx[normalize(gf_pair_to_fq4(*X),p)])
    parts.append(S)
    return parts

# q=2, n=2.
P2,A2=projective_standard(2,2)
assert len(P2)==15
assert no_independent_of_size(A2,4)
ind3=[S for S in combinations(range(15),3)
      if all(not A2[i][j] for i,j in combinations(S,2))]
assert ind3
for S in ind3:
    assert rank_mod([P2[i] for i in S],2)==2

F4=QuadField(2)
T2,AT2=projective_trace(F4)
parts2=spread_trace(F4,T2)
assert len(parts2)==5
assert all(len(S)==3 for S in parts2)
assert len(set().union(*parts2))==15
for S in parts2:
    assert all(not AT2[i][j] for i,j in combinations(S,2))

# q=3, n=2.
F9=QuadField(3)
P3,A3=projective_trace(F9)
assert len(P3)==40
assert no_independent_of_size(A3,5)
parts3=spread_trace(F9,P3)
assert len(parts3)==10
assert all(len(S)==4 for S in parts3)
assert len(set().union(*parts3))==40
for S in parts3:
    assert all(not A3[i][j] for i,j in combinations(S,2))

assert 2*(2**2-1)==6 and 2**2+1==5
assert 3*(3**2-1)==24 and 3**2+1==10
print("VERIFY_OK")
