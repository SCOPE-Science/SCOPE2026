"""Finite-field exhaustive verifier for fourth-order substitution jets."""
from itertools import product
from collections import Counter

class GF:
    # Monic irreducible defining polynomials (constant first).
    defs = {2:(2,[0,1]),3:(3,[0,1]),4:(2,[1,1,1]),5:(5,[0,1]),7:(7,[0,1]),8:(2,[1,1,0,1]),9:(3,[1,0,1]),11:(11,[0,1]),13:(13,[0,1]),16:(2,[1,1,0,0,1])}
    def __init__(self,q):
        self.q=q; self.p,self.pol=self.defs[q]
        self.e=len(self.pol)-1
        self.vec=[tuple((i//(self.p**j))%self.p for j in range(self.e)) for i in range(q)]
        self.addtab=[[sum(((x+y)%self.p)*(self.p**k) for k,(x,y) in enumerate(zip(self.vec[a],self.vec[b]))) for b in range(q)] for a in range(q)]
        self.neg=[sum(((-x)%self.p)*(self.p**k) for k,x in enumerate(self.vec[a])) for a in range(q)]
        self.multab=[]
        for a in range(q):
            row=[]
            for b in range(q):
                poly=[0]*(2*self.e-1)
                for i,x in enumerate(self.vec[a]):
                    for j,y in enumerate(self.vec[b]):poly[i+j]=(poly[i+j]+x*y)%self.p
                for j in range(2*self.e-2,self.e-1,-1):
                    t=poly[j]
                    for k in range(self.e):poly[j-self.e+k]=(poly[j-self.e+k]-t*self.pol[k])%self.p
                row.append(sum(poly[k]*(self.p**k) for k in range(self.e)))
            self.multab.append(row)
        self.inv=[None]+[next(b for b in range(1,q) if self.multab[a][b]==1) for a in range(1,q)]
    def plus(self,a,b):return self.addtab[a][b]
    def minus(self,a,b):return self.plus(a,self.neg[b])
    def mult(self,a,b):return self.multab[a][b]
    def sc(self,n,a):
        n%=self.p
        return self.mult(n,a)
    def power(self,a,n):
        r=1
        for _ in range(n):r=self.mult(r,a)
        return r

def matrix(F,a,b,c,d):
    mul=F.mult;add=F.plus;sc=F.sc
    a2=mul(a,a);a3=mul(a2,a);a4=mul(a3,a)
    return [[a,0,0,0],[b,a2,0,0],[c,sc(2,mul(a,b)),a3,0],
            [d,add(mul(b,b),sc(2,mul(a,c))),sc(3,mul(a2,b)),a4]]

def rank(F,rows):
    mat=[list(row) for row in rows];h=len(mat);w=len(mat[0]);r=0
    for col in range(w):
        pivot=next((i for i in range(r,h) if mat[i][col]!=0),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        t=F.inv[mat[r][col]];mat[r]=[F.mult(t,x) for x in mat[r]]
        for i in range(h):
            if i==r:continue
            t=mat[i][col]
            if t:
                mat[i]=[F.minus(x,F.mult(t,y)) for x,y in zip(mat[i],mat[r])]
        r+=1
        if r==h:break
    return r

def prediction(F):
    q=F.q;p=F.p
    r3=sum(1 for a in range(1,q) if a!=1 and F.power(a,3)==1)
    r4=sum(1 for a in range(1,q) if F.power(a,4)==1 and F.power(a,2)!=1)
    if p==2:
        vals={1:(q-2-r3)*q**3,2:r3*q**3,3:(q-1)*q**2,4:q*q-1,5:1}
        orbit=q*(2*q+r3+3)
    elif p==3:
        vals={1:(q-3-r4)*q**3,2:(q**3-q**2)+r4*q**3,3:q**3+q**2-q,4:q-1,5:1}
        orbit=q*(q+r4+6)
    else:
        vals={1:(q-3-r3-r4)*q**3,2:2*q*q*(q-1)+(r3+r4)*q**3,
              3:2*q*q-q,4:q-1,5:1}
        orbit=q*(7+r3+r4)
    assert sum(vals.values())==(q-1)*q**3
    assert sum(n*(q**j) for j,n in vals.items())//((q-1)*q**3)==orbit
    return vals,orbit,r3,r4

def action(F,abc,elem):
    a,b,c,d=abc
    s,t,u,v,w=elem
    M=matrix(F,a,b,c,d)
    rad=(t,u,v,w)
    return (s,)+tuple(sumfield(F,[F.mult(M[i][j],rad[j]) for j in range(4)]) for i in range(4))

def sumfield(F,ls):
    s=0
    for v in ls:s=F.plus(s,v)
    return s

def orbit_census(F):
    q=F.q;els=set(product(range(q),repeat=5));groups=list(product(range(1,q),range(q),range(q),range(q)))
    orbits=[]
    while els:
        seed=next(iter(els))
        images=set(action(F,g,seed) for g in groups)
        assert images<=els
        orbits.append(len(images)); els-=images
    return Counter(orbits)

def verify(q,orbits=False):
    F=GF(q);expect,o,r3,r4=prediction(F)
    actual=Counter()
    for a in range(1,q):
        for b,c,d in product(range(q),repeat=3):
            M=matrix(F,a,b,c,d)
            mat=[[F.minus(M[i][j],int(i==j)) for j in range(4)] for i in range(4)]
            actual[5-rank(F,mat)]+=1
    assert dict(actual)=={i:c for i,c in expect.items() if c},(q,actual,expect)
    weighted=sum(n*q**i for i,n in actual.items())
    assert weighted==o*(q-1)*q**3,(q,weighted,o)
    print(q,'counts',dict(sorted(actual.items())),'orbits',o,'r3',r3,'r4',r4)
    if orbits:
        lengths=orbit_census(F)
        assert sum(lengths.values())==o,(q,lengths,o)
        assert sum(k*v for k,v in lengths.items())==q**5
        print('orbit_sizes',q,dict(sorted(lengths.items())))

if __name__=='__main__':
    for q in [2,3,4,5,7,8,9,11,13,16]:verify(q, q in (2,3,4))
    print('VERIFY_OK')
