from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5,7)
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
        # F4 = F2[t]/(t^2+t+1), bits encode a0+a1*t.
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

def inv2(F,M):
    a,b=M[0]
    c,d=M[1]
    det=F.sub(F.mul(a,d),F.mul(b,c))
    if det==0:
        return None
    e=F.inv(det)
    return [
        [F.mul(d,e),F.mul(F.neg(b),e)],
        [F.mul(F.neg(c),e),F.mul(a,e)]
    ]

def transpose(A):
    return [list(x) for x in zip(*A)]

def kron(F,A,B):
    br=len(B)
    bc=len(B[0])
    return [
        [
            F.mul(A[i//br][j//bc],B[i%br][j%bc])
            for j in range(len(A[0])*bc)
        ]
        for i in range(len(A)*br)
    ]

def rank(F,A):
    A=[row[:] for row in A]
    m=len(A)
    n=len(A[0])
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]!=0),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        z=F.inv(A[r][c])
        A[r]=[F.mul(z,x) for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                z=A[i][c]
                A[i]=[
                    F.sub(A[i][j],F.mul(z,A[r][j]))
                    for j in range(n)
                ]
        r+=1
        if r==m:
            break
    return r

def actual(q):
    F=Field(q)
    C=Counter()
    for a,b,c,d in product(range(q),repeat=4):
        M=[[a,b],[c,d]]
        Mi=inv2(F,M)
        if Mi is None:
            continue
        MT=transpose(M)
        T=kron(F,kron(F,MT,MT),Mi)
        A=[
            [
                F.sub(T[i][j],1 if i==j else 0)
                for j in range(8)
            ]
            for i in range(8)
        ]
        C[8-rank(F,A)]+=1
    return dict(C)

def predicted(q,char):
    e2=1 if char!=2 else 0
    ep=1 if q%3==1 else 0
    em=1 if q%3==2 else 0
    return {
        0:
            (q-2)*q*q
            +q*(q+1)*(((q-2)*(q-5))//2+e2+ep)
            +q*(q-1)*(q*(q-1)//2-em),
        1:(q-2-e2-2*ep)*q*(q+1),
        2:ep*q*(q+1)+em*q*(q-1),
        3:e2*(q*q-1)+(q-2-e2)*q*(q+1),
        4:(1-e2)*(q*q-1)+e2*q*(q+1),
        8:1,
    }

def known_algebras(q,char):
    if char==2:
        return q**4+q**3+4*q**2+3*q+6
    if char==3:
        return q**4+q**3+4*q**2+4*q+6
    return q**4+q**3+4*q**2+4*q+7

for q,char in ((2,2),(3,3),(4,2),(5,5),(7,7)):
    A=actual(q)
    P={k:v for k,v in predicted(q,char).items() if v}
    assert A==P,(q,A,P)
    order=q*(q-1)**2*(q+1)
    assert sum(A.values())==order
    burnside=sum(v*(q**k) for k,v in A.items())
    assert burnside%order==0
    assert burnside//order==known_algebras(q,char)
    print({"q":q,"distribution":dict(sorted(A.items())),
           "algebras":burnside//order})

print("VERIFY_OK")
