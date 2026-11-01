"""Standalone exact checker for simultaneous linear complete mappings.

This reproduces selected finite-field cases by direct matrix enumeration. It does
not replace the symbolic proof for arbitrary finite fields.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, p, polynomial=None):
        self.p = p
        self.poly = polynomial
        self.q = p if polynomial is None else p * p

    def add(self, x, y):
        if self.poly is None:
            return (x+y) % self.p
        a,b = x % self.p,x // self.p
        c,d = y % self.p,y // self.p
        return (a+c) % self.p + self.p * ((b+d) % self.p)

    def neg(self, x):
        if self.poly is None:
            return -x % self.p
        return (-x % self.p) + self.p * (-(x // self.p) % self.p)

    def mul(self, x, y):
        if self.poly is None:
            return x*y % self.p
        a,b = x % self.p,x // self.p
        c,d = y % self.p,y // self.p
        r0,r1 = self.poly  # z*z + r1*z + r0 = 0
        return (a*c-b*d*r0) % self.p + self.p * ((a*d+b*c-b*d*r1) % self.p)

    def sub(self,x,y):return self.add(x,self.neg(y))


def run(F):
    q=F.q
    mats=list(product(range(q),repeat=4))
    ident=(1,0,0,1)
    def add(A,B):return tuple(F.add(a,b) for a,b in zip(A,B))
    def det(A):return F.sub(F.mul(A[0],A[3]),F.mul(A[1],A[2]))
    gl=[A for A in mats if det(A)!=0]
    labels=Counter()
    values=Counter()
    for C in gl:
        compatible=sum(det(add(B,ident))!=0 and det(add(B,C))!=0 for B in gl)
        eig=0; fix=0
        for t in range(q):
            u=(1,t)
            Cu=(F.add(F.mul(C[0],u[0]),F.mul(C[1],u[1])),F.add(F.mul(C[2],u[0]),F.mul(C[3],u[1])))
            if F.sub(F.mul(u[0],Cu[1]),F.mul(u[1],Cu[0]))==0:eig+=1
            if Cu==u:fix+=1
        u=(0,1); Cu=(C[1],C[3])
        if Cu[0]==0:eig+=1
        if Cu==u:fix+=1
        # rank(I-C) by checking its determinant and entries
        D=tuple(F.sub(x,y) for x,y in zip(ident,C))
        r=0 if D==(0,0,0,0) else 2 if det(D) else 1
        T=q**3+q**2-q
        P={0:T,1:q*(2*q-1),2:q*(q+1)}[r]
        expected=q**4-3*T+2*q*(q+1)+P-(q+1+q*fix-eig)
        assert compatible==expected,('wrong',q,C,compatible,expected,r,eig,fix)
        if r==0: label='identity'
        elif eig==q+1: label='other scalar'
        elif eig==0: label='irreducible'
        elif eig==1 and fix: label='Jordan at one'
        elif eig==1: label='Jordan off one'
        elif eig==2 and fix: label='split one-and-other'
        elif eig==2: label='split other-and-other'
        else: raise AssertionError((q,C,r,eig,fix))
        labels[label,compatible]+=1
        values[compatible]+=1
    expected_mult={
        'identity':1,
        'other scalar':q-2,
        'irreducible':q*q*(q-1)*(q-1)//2,
        'Jordan at one':q*q-1,
        'Jordan off one':(q-2)*(q*q-1),
        'split one-and-other':(q-2)*q*(q+1),
        'split other-and-other':(q-2)*(q-3)//2*q*(q+1)
    }
    for name, mult in expected_mult.items():
        observed=sum(c for (name0,n),c in labels.items() if name0==name)
        assert observed==mult,(q,name,observed,mult)
    assert sum(values.values())==(q*q-1)*(q*q-q)
    print('GF(%d): %d relative maps; frequency-by-mate-count %s; seven-family multiplicities OK' %
          (q,len(gl),sorted(values.items())))

if __name__=='__main__':
    for F in [Field(2),Field(3),Field(2,(1,1)),Field(5)]:
        run(F)
    print('VERIFY_OK')
