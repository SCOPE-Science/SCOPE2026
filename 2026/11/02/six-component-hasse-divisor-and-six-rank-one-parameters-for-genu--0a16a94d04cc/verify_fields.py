"""Independent exact GF(25) census and Cartier semilinear iteration.
Represent GF(25)=GF(5)[t]/(t*t-3); no external dependencies.
"""
from collections import Counter
p=5
N=25
add=lambda u,v: ((u//5+v//5)%5)*5+(u%5+v%5)%5
neg=lambda u: (-u//5%5)*5+(-u%5) if False else ((-u//5)%5)*5+((-u%5)%5)
# Be careful: represent u=5*x+y.
sub=lambda u,v: ((u//5-v//5)%5)*5+((u%5-v%5)%5)
def mul(u,v):
    a,b=divmod(u,5); c,d=divmod(v,5)
    return 5*((a*c+3*b*d)%5)+(a*d+b*c)%5
zero=0
one=5
const=lambda n: (n%5)*5
def pow_f(u,n):
    v=one
    while n:
        if n&1: v=mul(v,u)
        u=mul(u,u);n//=2
    return v
assert all(pow_f(u,25)==u for u in range(N))
assert all(mul(u,pow_f(u,23))==one for u in range(1,N))
def det_or_rank(m):
    mat=[row[:] for row in m]
    rr=0
    for c in range(len(mat[0])):
        j=next((i for i in range(rr,len(mat)) if mat[i][c]),None)
        if j is None: continue
        mat[rr],mat[j]=mat[j],mat[rr]
        inv=pow_f(mat[rr][c],23)
        mat[rr]=[mul(t,inv) for t in mat[rr]]
        for i in range(len(mat)):
            if i!=rr and mat[i][c]:
                t=mat[i][c]
                mat[i]=[sub(x,mul(t,y)) for x,y in zip(mat[i],mat[rr])]
        rr+=1
        if rr==len(mat):break
    return rr
def mm(A,B):
    return [[sum_f(mul(A[i][k],B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
def sum_f(xs):
    acc=zero
    for x in xs: acc=add(acc,x)
    return acc

def poly_mul(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): v[i+j]=add(v[i+j],mul(x,y))
    return v

def eval_polys(a,b):
    aa=mul(a,a);bb=mul(b,b);ab=mul(a,b)
    q=sub(add(sub(aa,ab),bb),one)
    p=add(q,mul(const(2),add(a,b)))
    n=sub(q,mul(const(2),add(a,b)))
    r=add(add(add(mul(aa,bb),mul(const(2),aa)),mul(const(3),ab)),add(mul(const(2),bb),one))
    return (p,n,r)

counter=Counter(); special=[]
for a in range(N):
    for b in range(N):
        if a==b or a in (const(2),const(-2)) or b in (const(2),const(-2)):
            counter['singular']+=1;continue
        a4=[one,0,sub(0,a),0,one]
        b4=[one,0,sub(0,b),0,one]
        f=poly_mul(a4,b4)
        f2=poly_mul(f,f)
        H=[[f2[5*(i+1)-(j+1)] for j in range(3)] for i in range(3)]
        H5=[[pow_f(x,5) for x in row] for row in H]
        Hstable=mm(mm(H,H5),H)
        stable_rank=det_or_rank(Hstable)
        cartier_rank=det_or_rank(H)
        pred=eval_polys(a,b)
        expected=sum(bool(x) for x in pred)
        assert stable_rank==expected, (a,b,stable_rank,pred)
        assert cartier_rank==expected, (a,b,cartier_rank,pred)
        counter[(stable_rank,3-cartier_rank)]+=1
        if stable_rank==1:
            special.append((a,b))
# Three explicit degree-two geometric pairs, all inside GF(25).
expected_special=set()
for a in range(N):
    aa=mul(a,a)
    for b in range(N):
        if (aa==const(2) and b==sub(0,a)) or (
            add(add(aa,mul(const(2),a)),const(-2))==0 and b==sub(sub(0,a),const(2))) or (
            add(sub(aa,mul(const(2),a)),const(-2))==0 and b==add(sub(0,a),const(2))):
            expected_special.add((a,b))
assert set(special)==expected_special and len(expected_special)==6
print('GF25_EXHAUSTIVE_HOWE_506_SMOOTH_6_RANK_ONE_OK',dict(counter))
