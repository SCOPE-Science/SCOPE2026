"""Exact checks for the full-coefficient Artin--Schreier extremality criterion.

No third-party dependencies. Tests every ordered pair (a0,a1) of nonzero
coefficients over F_{3^4} and F_{5^4}, including the quadratic-rank criterion.
The general theorem rests on the separate algebraic proof, not this finite test.
"""
from itertools import product

class Field:
    def __init__(self, p, modulus):
        self.p, self.n, self.mod = p, 4, modulus
        self.q = p**4
        self.powers = [p**i for i in range(4)]
        self.vectors = [tuple((z // d) % p for d in self.powers) for z in range(self.q)]
        self._multiplication = [[0]*self.q for _ in range(self.q)]
        for x in range(self.q):
            for y in range(x, self.q):
                c=[0]*7
                for i,a in enumerate(self.vectors[x]):
                    for j,b in enumerate(self.vectors[y]):
                        c[i+j] += a*b
                for k in range(6,3,-1):
                    d=c[k]%p
                    for j in range(4):
                        c[k-4+j] -= d*modulus[j]
                z=sum((c[i]%p)*self.powers[i] for i in range(4))
                self._multiplication[x][y]=z
                self._multiplication[y][x]=z
        self._powers_p=[self.power(x,p) for x in range(self.q)]
        self._trace=[]
        for x in range(self.q):
            t=0;y=x
            for _ in range(4):
                t=self.add(t,y)
                y=self._powers_p[y]
            assert all(v==0 for v in self.vectors[t][1:]), ('trace',x,t)
            self._trace.append(t)

    def add(self,x,y):
        return sum(((a+b)%self.p)*d for a,b,d in zip(self.vectors[x],self.vectors[y],self.powers))
    def mul(self,x,y):
        return self._multiplication[x][y]
    def power(self,x,n):
        out=1
        while n:
            if n&1:out=self.mul(out,x)
            x=self.mul(x,x);n//=2
        return out
    def trace(self,x):return self._trace[x]
    def frob(self,x):return self._powers_p[x]
    def inverse(self,x):assert x;return self.power(x,self.q-2)


def rank_mod_p(M,p):
    A=[row[:] for row in M]
    r=0
    for j in range(4):
        pivot=next((i for i in range(r,4) if A[i][j]%p),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        k=pow(A[r][j]%p,-1,p)
        for jj in range(j,4):A[r][jj]=A[r][jj]*k%p
        for i in range(r+1,4):
            k=A[i][j]%p
            for jj in range(j,4):A[i][jj]=(A[i][jj]-k*A[r][jj])%p
        r+=1
    return r


def check(p,modulus):
    F=Field(p,modulus);q=F.q
    v=F.powers;fro=F.frob;mul=F.mul;tr=F.trace;add=F.add;power=F.power
    # Both matrices are independently obtained from the trace polar form.
    G0=[[[0]*4 for _ in range(4)] for _ in range(q)]
    G1=[[[0]*4 for _ in range(4)] for _ in range(q)]
    for a in range(q):
        for i in range(4):
            for j in range(4):
                G0[a][i][j]=tr(mul(a,mul(2,mul(v[i],v[j]))))
                G1[a][i][j]=tr(mul(a,add(mul(v[i],fro(v[j])),mul(v[j],fro(v[i])))))
    counts=[0]*5
    witness=None
    accepted=0
    for a0 in range(1,q):
        for a1 in range(1,q):
            G=[[(G0[a0][i][j]+G1[a1][i][j])%p for j in range(4)] for i in range(4)]
            r=rank_mod_p(G,p)
            counts[r]+=1
            N=power(a1,p*p+1)
            t=mul(mul(2,fro(a0)),F.inverse(power(a1,p+1)))
            rhs=add(F.inverse(N), F.mul(p-1,F.inverse(fro(N))))
            formula=(power(t,p+1)==rhs)
            assert (r==2)==formula, ('formula mismatch',p,a0,a1,r)
            if formula:
                accepted+=1
                if witness is None:witness=(a0,a1)
    assert accepted==p*(q-1),(p,accepted)
    assert counts[0]==counts[1]==0
    # Point-count check for one extremal curve (bypasses quadratic rank).
    a0,a1=witness
    zero=0
    for x in range(q):
        xx=mul(x,x)
        qval=add(mul(a0,xx),mul(a1,mul(x,fro(x))))
        if tr(qval)==0:zero+=1
    points=1+p*zero
    g=p*(p-1)//2
    assert points in {q+1-2*g*p*p,q+1+2*g*p*p},points
    print(f"p={p} q={q} ranks={counts} coefficient_pairs={accepted} witness={(a0,a1)} points={points} OK")

if __name__ == '__main__':
    check(3,(2,1,0,0,1))
    check(5,(2,0,0,0,1))
    print('VERIFY_OK')
