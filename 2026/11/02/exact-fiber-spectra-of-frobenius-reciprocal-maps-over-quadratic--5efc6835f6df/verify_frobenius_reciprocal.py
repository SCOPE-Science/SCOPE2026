#!/usr/bin/env python3
"""Direct finite-field enumeration of fibers of Frobenius--reciprocal maps.
Pure standard-library arithmetic and irreducible-field-model selection.
The direct image computations do not use the theorem's norm-discriminant test.
"""
from collections import Counter
from itertools import product

def is_irreducible_monic(f,p):
    """Exact trial-division irreducibility for the small test fields."""
    d=len(f)-1
    for e in range(1,d//2+1):
        for coeffs in product(range(p),repeat=e):
            g=list(coeffs)+[1]
            r=list(f)
            for k in range(d-e,-1,-1):
                b=r[k+e]
                if b:
                    for j in range(e+1):
                        r[k+j]=(r[k+j]-b*g[j])%p
            if not any(r):
                return False
    return True

class Field:
    def __init__(self,p,d):
        self.p, self.d, self.order = p,d,p**d
        if d==1:
            self.mod = [0,1]
        else:
            self.mod = None
            for coeffs in product(range(p), repeat=d):
                if is_irreducible_monic(list(coeffs)+[1],p):
                    self.mod = list(coeffs)+[1]
                    break
            assert self.mod is not None
        self.repr = [[(i//(p**j))%p for j in range(d)] for i in range(self.order)]
    def embed(self,coeff):
        return sum((coeff[i]%self.p)*(self.p**i) for i in range(self.d))
    def add(self,a,b):
        return self.embed([(u+v)%self.p for u,v in zip(self.repr[a],self.repr[b])])
    def mul(self,a,b):
        p,d=self.p,self.d
        u=self.repr[a];v=self.repr[b]
        res=[0]*(2*d-1)
        for i,ui in enumerate(u):
            if ui:
                for j,vj in enumerate(v):
                    if vj:res[i+j]=(res[i+j]+ui*vj)%p
        for z in range(2*d-2,d-1,-1):
            c=res[z]
            if c:
                for j in range(d):res[z-d+j]=(res[z-d+j]-c*self.mod[j])%p
        return self.embed(res[:d])
    def pow(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out


def direct_test(p,m):
    q=p**m; F=Field(p,2*m); N=q*q
    base=[i for i in range(N) if F.pow(i,q)==i]
    assert len(base)==q
    cases={}
    for a in range(1,N):
        in_base=F.pow(a,q)==a
        norm=F.pow(a,q+1)
        square_norm=(p==2 or F.pow(norm,(q-1)//2)==1)
        kind='base' if in_base else ('outside_square' if square_norm else 'outside_nonsquare')
        cases.setdefault(kind,[]).append(a)
    checked=0;outputs=0
    for kind,samples in cases.items():
        for a in samples[:min(len(samples),5)]:
            fibers=Counter()
            for x in range(1,N):
                y=F.add(F.pow(x,q),F.mul(a,F.pow(x,N-2)))
                fibers[y]+=1
            hist=Counter(fibers.values());hist[0]=N-len(fibers)
            if p%2:
                if kind=='base':
                    exp={0:(q*q-1)//2,1:q+1,2:(q+1)*(q-3)//2,q+1:1}; image=(q*q+1)//2
                elif kind=='outside_square':
                    exp={0:(q*q-2*q-1)//2,1:2*(q+1),2:(q+1)*(q-3)//2}; image=(q+1)**2//2
                else:
                    exp={0:(q*q+1)//2,2:(q*q-1)//2};image=(q*q-1)//2
            else:
                if kind=='base':
                    exp={0:q*(q+1)//2,2:(q+1)*(q-2)//2,q+1:1}; image=q*(q-1)//2
                else:
                    exp={0:q*(q-1)//2,1:q+1,2:(q+1)*(q-2)//2};image=q*(q+1)//2
            exp={k:v for k,v in exp.items() if v!=0}
            hist={k:v for k,v in hist.items() if v!=0}
            assert hist==exp,(p,m,kind,a,F.mod,hist,exp)
            assert len(fibers)==image,(p,m,a)
            assert fibers[0]==(q+1 if kind=='base' else 0)
            checked+=1;outputs+=N-1
            if kind=='base':
                for x in range(1,N):
                    y=F.mul(a,F.pow(F.pow(x,q),N-2))
                    lhs=F.add(F.pow(x,q),F.mul(a,F.pow(x,N-2)))
                    rhs=F.add(F.pow(y,q),F.mul(a,F.pow(y,N-2)))
                    assert lhs==rhs
    return checked,outputs,sorted((k,len(v)) for k,v in cases.items())

if __name__=='__main__':
    tests=[(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),
            (5,1),(5,2),(7,1),(7,2),(11,1),(13,1),(17,1)]
    total=0; evaluated=0; kinds=set()
    for p,m in tests:
        a,b,c=direct_test(p,m); total+=a; evaluated+=b; kinds.update(k for k,_ in c)
    print(f'VERIFY_OK fields={len(tests)} coefficient_cases={total} direct_nonzero_inputs={evaluated} types={sorted(kinds)} all_fibers=PASS')
