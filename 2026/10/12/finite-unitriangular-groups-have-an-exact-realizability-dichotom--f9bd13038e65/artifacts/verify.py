from itertools import product

class F:
    def __init__(self,q):
        assert q in (2,4)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%2
    def neg(self,a):
        return a if self.q in (2,4) else None
    def mul(self,a,b):
        if self.q==2:
            return (a*b)%2
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        # t^2=t+1 in F4.
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0 | (c1<<1)

def mat_add(Fd,A,B):
    n=len(A)
    return tuple(tuple(Fd.add(A[i][j],B[i][j]) for j in range(n)) for i in range(n))

def mat_mul(Fd,A,B):
    n=len(A)
    return tuple(tuple(sum_field(Fd,[Fd.mul(A[i][k],B[k][j]) for k in range(n)]) for j in range(n)) for i in range(n))

def sum_field(Fd,xs):
    s=0
    for x in xs:
        s=Fd.add(s,x)
    return s

def eye(n):
    return tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))

def zero(n):
    return tuple(tuple(0 for j in range(n)) for i in range(n))

def strictly_upper_mats(q,n):
    pos=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    for vals in product(range(q),repeat=len(pos)):
        M=[[0]*n for _ in range(n)]
        for (i,j),v in zip(pos,vals):
            M[i][j]=v
        out.append(tuple(tuple(r) for r in M))
    return out

def ring(q,n):
    Fd=F(q); I=eye(n); N=strictly_upper_mats(q,n)
    R=[]
    for a in (0,1):
        for X in N:
            A=tuple(tuple(Fd.add(a if i==j else 0,X[i][j]) for j in range(n)) for i in range(n))
            R.append(A)
    return Fd,I,N,R

def check(q,n):
    Fd,I,N,R=ring(q,n)
    S=set(R)
    assert len(S)==2*(q**(n*(n-1)//2))
    # exhaustive closure for tested sizes
    for A in R:
        for B in R:
            assert mat_add(Fd,A,B) in S
            assert mat_mul(Fd,A,B) in S
    # direct inverse search
    units=set()
    for A in R:
        if any(mat_mul(Fd,A,B)==I and mat_mul(Fd,B,A)==I for B in R):
            units.add(A)
    target=set()
    for X in N:
        target.add(tuple(tuple(Fd.add(1 if i==j else 0,X[i][j]) for j in range(n)) for i in range(n)))
    assert units==target
    print({'q':q,'n':n,'ring_order':len(R),'unit_order':len(units)})

for q,n in [(2,2),(2,3),(2,4),(4,2),(4,3)]:
    check(q,n)

# Direct noncommutativity check in odd prime fields.
def mm_p(A,B,p):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)) for i in range(n))
for p in (3,5):
    n=3
    A=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    B=[r[:] for r in A]
    A[0][1]=1
    B[1][2]=1
    A=tuple(tuple(r) for r in A); B=tuple(tuple(r) for r in B)
    assert mm_p(A,B,p)!=mm_p(B,A,p)
    print({'odd_p':p,'UT3_nonabelian':True})

print('VERIFY_OK')
