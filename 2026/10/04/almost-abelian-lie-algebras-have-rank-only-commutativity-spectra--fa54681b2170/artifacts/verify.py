from itertools import product
from collections import Counter
from fractions import Fraction

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q in (2,4) else (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:
            return (a*b)%self.q
        # F4 = F2[t]/(t^2+t+1); bits encode a0+a1*t.
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0 | (c1<<1)
    def inv(self,a):
        assert a!=0
        for b in range(1,self.q):
            if self.mul(a,b)==1:
                return b
        raise AssertionError

def mat_vec(F,A,v):
    return tuple(
        sum_field(F,[F.mul(A[i][j],v[j]) for j in range(len(v))])
        for i in range(len(A))
    )

def sum_field(F,vals):
    s=0
    for x in vals:
        s=F.add(s,x)
    return s

def vec_add(F,u,v):
    return tuple(F.add(a,b) for a,b in zip(u,v))

def vec_scale(F,a,v):
    return tuple(F.mul(a,x) for x in v)

def vec_neg(F,v):
    return tuple(F.neg(x) for x in v)

def rank(F,A):
    if not A:
        return 0
    M=[list(row) for row in A]
    m=len(M); n=len(M[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if M[i][c]!=0),None)
        if p is None:
            continue
        M[r],M[p]=M[p],M[r]
        z=F.inv(M[r][c])
        M[r]=[F.mul(z,x) for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]!=0:
                z=M[i][c]
                M[i]=[
                    F.sub(M[i][j],F.mul(z,M[r][j]))
                    for j in range(n)
                ]
        r+=1
        if r==m:
            break
    return r

def bracket(F,A,x,y):
    alpha=x[0]; beta=y[0]
    u=x[1:]; v=y[1:]
    av=mat_vec(F,A,v)
    au=mat_vec(F,A,u)
    w=vec_add(F,vec_scale(F,alpha,av),vec_neg(F,vec_scale(F,beta,au)))
    return (0,)+w

def adjoint_matrix(F,A,x):
    n=len(A)
    basis=[(1,)+(0,)*n]
    for j in range(n):
        v=[0]*n
        v[j]=1
        basis.append((0,)+tuple(v))
    cols=[bracket(F,A,x,b) for b in basis]
    return [[cols[j][i] for j in range(n+1)] for i in range(n+1)]

def predicted_hist(q,n,r):
    H=Counter()
    H[0]+=q**(n-r)
    H[1]+=q**n-q**(n-r)
    H[r]+=(q-1)*q**n
    return dict(H)

def check(q,A,label):
    F=Field(q)
    n=len(A)
    r=rank(F,A)
    assert 1<=r<=n
    elems=list(product(range(q),repeat=n+1))

    H=Counter()
    for x in elems:
        H[rank(F,adjoint_matrix(F,A,x))]+=1
    P=predicted_hist(q,n,r)
    assert dict(H)==P,(label,dict(H),P)

    commuting=0
    zero=(0,)*(n+1)
    for x in elems:
        for y in elems:
            if bracket(F,A,x,y)==zero:
                commuting+=1

    observed=Fraction(commuting,len(elems)**2)
    expected=Fraction(q**r+q**2-1,q**(r+2))
    assert observed==expected,(label,observed,expected)

    print({
        "label":label,
        "q":q,
        "n":n,
        "rank_A":r,
        "rank_hist":dict(sorted(H.items())),
        "commutativity":f"{observed.numerator}/{observed.denominator}",
    })

cases=[
    (2, [[0,1],[0,0]], "F2_nilpotent_rank1"),
    (3, [[1,0],[0,2]], "F3_semisimple_rank2"),
    (3, [[0,1,0],[0,0,1],[0,0,0]], "F3_nilpotent_rank2_dim3"),
    (4, [[1,1],[0,1]], "F4_Jordan_rank2"),
    (5, [[1,0,0],[0,0,0],[0,0,0]], "F5_rank1_dim3"),
    (5, [[1,0,0],[0,1,0],[0,0,1]], "F5_rank3_dim3"),
]
for q,A,label in cases:
    check(q,A,label)

print("VERIFY_OK")
