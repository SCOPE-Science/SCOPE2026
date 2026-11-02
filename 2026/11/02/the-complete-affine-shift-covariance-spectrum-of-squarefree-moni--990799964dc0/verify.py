"""Exact finite-field checks of the shifted squarefree-cubic correlation theorem.

Requires Python 3 standard library only.  Arrays encode field elements by their
base-p digits and polynomials by ascending coefficient order.
"""
from itertools import product

FIELDS = [
    (2, [0, 1]), (3, [0, 1]), (2, [1, 1, 1]),
    (5, [0, 1]), (7, [0, 1]), (2, [1, 1, 0, 1]),
    (3, [1, 0, 1]), (11, [0, 1]), (13, [0, 1]),
    (2, [1, 1, 0, 0, 1]), (5, [2, 0, 1]),
]

class FiniteField:
    def __init__(self, p, modulus):
        self.p = p
        self.modulus = modulus
        self.degree = len(modulus) - 1
        self.q = p ** self.degree
        assert modulus[-1] == 1
        self.digits = [self.expand(x) for x in range(self.q)]
        self.add = [[self.pack([(a+b)%p for a,b in zip(self.digits[x],self.digits[y])])
                     for y in range(self.q)] for x in range(self.q)]
        self.neg = [self.pack([(-a)%p for a in self.digits[x]]) for x in range(self.q)]
        self.mul = [[self.product(x,y) for y in range(self.q)] for x in range(self.q)]
        self.inv = [0]*self.q
        for x in range(1,self.q):
            inverse = [y for y in range(1,self.q) if self.mul[x][y]==1]
            assert len(inverse)==1,(p,modulus,x,inverse)
            self.inv[x]=inverse[0]
        self.two = 2%p
        self.three = 3%p

    def expand(self,n):
        out=[]
        for _ in range(self.degree):
            out.append(n%self.p); n//=self.p
        return out

    def pack(self,ds):
        return sum(d*(self.p**i) for i,d in enumerate(ds))

    def product(self,x,y):
        p=self.p
        h=self.degree
        a=self.digits[x]; b=self.digits[y]
        result=[0]*(2*h-1)
        for i in range(h):
            for j in range(h): result[i+j]=(result[i+j]+a[i]*b[j])%p
        for k in range(2*h-2,h-1,-1):
            c=result[k]
            for j in range(h): result[k-h+j]=(result[k-h+j]-c*self.modulus[j])%p
        return self.pack(result[:h])

    def trim(self,f):
        while f and f[-1]==0: f.pop()
        return f

    def rem(self,a,b):
        a=self.trim(a[:]); b=self.trim(b[:])
        assert b
        while len(a)>=len(b):
            t=self.mul[a[-1]][self.inv[b[-1]]]
            off=len(a)-len(b)
            for i,v in enumerate(b):
                a[off+i]=self.add[a[off+i]][self.neg[self.mul[t][v]]]
            self.trim(a)
        return a

    def squarefree_cubic(self,a,b,c):
        derivative=self.trim([b,self.mul[self.two][a],self.three])
        if not derivative:
            return False
        f=[c,b,a,1]
        while derivative:
            f,derivative=derivative,self.rem(f,derivative)
        return len(f)==1

    def predicted(self,u,v):
        q=self.q; base=q*(q-1)**2
        if self.p==2:
            return base if u else base-q
        if u:
            return base-1
        twice_v=self.mul[self.two][v]
        nroots=sum(self.mul[self.mul[d][d]][d]==twice_v for d in range(1,q))
        return base+q*(nroots-1)

def main():
    cases=0; inputs=0
    for p,mod in FIELDS:
        K=FiniteField(p,mod); q=K.q
        sf={(a,b,c):K.squarefree_cubic(a,b,c) for a,b,c in product(range(q),repeat=3)}
        assert sum(sf.values())==q**3-q**2
        if q<=9:
            shifts=[(u,v) for u in range(q) for v in range(q) if u or v]
        else:
            shifts=sorted(set([(0,v) for v in range(1,min(q,8))]+
                              [(u,v) for u,v in [(1,0),(1,1),(2,0),(2,2),
                                                (q-1,q-1),(0,q-1)]]))
        for u,v in shifts:
            n=0
            for a,b,c in product(range(q),repeat=3):
                if sf[a,b,c] and sf[a,K.add[b][u],K.add[c][v]]:
                    n+=1
            expected=K.predicted(u,v)
            assert n==expected,(q,p,mod,u,v,n,expected)
            cases+=1; inputs+=q**3
    print(f"VERIFY_OK finite_fields={len(FIELDS)} cases={cases} tested_cubics={inputs}")

if __name__=='__main__':
    main()
