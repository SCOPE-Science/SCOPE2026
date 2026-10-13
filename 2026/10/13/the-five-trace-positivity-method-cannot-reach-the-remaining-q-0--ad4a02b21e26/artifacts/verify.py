from fractions import Fraction as F

# Exact arithmetic in Q(sqrt(3)): a + b*sqrt(3).
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]-3*x[1]*x[1]
    assert d != 0
    return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def q(a,b=1): return (F(a,b),F(0))
def s3(a,b=1): return (F(0),F(a,b))

def det(M):
    A=[[v for v in row] for row in M]
    n=len(A); out=q(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k] != q(0)),None)
        assert pivot is not None
        if pivot != k:
            A[k],A[pivot]=A[pivot],A[k]
            out=neg(out)
        p=A[k][k]; out=mul(out,p)
        for i in range(k+1,n):
            f=div(A[i][k],p)
            for j in range(k,n):
                A[i][j]=sub(A[i][j],mul(f,A[k][j]))
    return out

def positive(x):
    a,b=x
    if b==0: return a>0
    if b>0:
        if a>=0: return True
        return 3*b*b > a*a
    return positive(neg(x)) is False  # not used for certificate minors

U=q(921685,59049)
w={1:s3(9),2:q(1),3:s3(1,27),4:q(1,243),5:s3(1,6561)}
T=[[q(0) for _ in range(6)] for __ in range(6)]
for i in range(6):
    for j in range(6):
        if i!=j:
            T[i][j]=(w[abs(i-j)][0]/2,w[abs(i-j)][1]/2)
A=[[sub(U if i==j else q(0),T[i][j]) for j in range(6)] for i in range(6)]
expected=[
 F(921685,59049),
 F(2550724347457,13947137604),
 F(758392953105899099,411782264189298),
 F(3221110006544454859744597,194522647344910860816),
 F(1534702319835786298666213421719,11486367803069641420323984),
 F(2568340416337200082724303333950965613,2713034129613837024914843724864),
]
mins=[]
for k in range(1,7):
    d=det([row[:k] for row in A[:k]])
    assert d[1]==0
    mins.append(d[0])
assert mins==expected
assert all(x>0 for x in mins)

# Consistency check for the source coefficient vector.
c=[F(x) for x in (2,4,5,5,4,2)]
S=sum(x*x for x in c)
ray=(q(0))
num=q(0)
for i in range(1,6):
    B=sum(c[r+i]*c[r] for r in range(6-i))
    num=add(num,(w[i][0]*B,w[i][1]*B))
R=div(num,q(S))
# Exact check R < U: U-R = a+b*sqrt(3), and direct sign test.
gap=sub(U,R)
a,b=gap
if b>=0:
    assert a>=0 or 3*b*b>a*a
else:
    assert a>0 and a*a>3*b*b
print('VERIFY_OK')
