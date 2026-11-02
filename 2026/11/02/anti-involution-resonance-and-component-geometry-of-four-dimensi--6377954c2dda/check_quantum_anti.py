#!/usr/bin/env python3
"""Direct anti-involution census on four-dimensional quantum complete intersections.
Uses the original product table, not the equations in the classification.
"""
from itertools import product

class Field:
    def __init__(self,p,mod=None):
        self.p=p;self.mod=mod;self.deg=1 if mod is None else len(mod)-1;self.q=p**self.deg
    def digits(self,x):
        o=[]
        for _ in range(self.deg):o.append(x%self.p);x//=self.p
        return o
    def encode(self,a):return sum((v%self.p)*(self.p**i) for i,v in enumerate(a))
    def add(self,a,b):return self.encode([x+y for x,y in zip(self.digits(a),self.digits(b))])
    def neg(self,a):return self.encode([-x for x in self.digits(a)])
    def mul(self,a,b):
        if self.mod is None:return a*b%self.p
        p=self.p;u=self.digits(a);v=self.digits(b);w=[0]*(2*self.deg-1)
        for i in range(self.deg):
            for j in range(self.deg):w[i+j]=(w[i+j]+u[i]*v[j])%p
        for d in range(len(w)-1,self.deg-1,-1):
            z=w[d]
            for j in range(self.deg):w[d-self.deg+j]=(w[d-self.deg+j]-z*self.mod[j])%p
        return self.encode(w[:self.deg])
    def inv(self,a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise ValueError(a)


def direct(qfield,lam):
    F=qfield;q=F.q; inv=F.inv(lam);minus_inv=F.neg(inv)
    def prod(a,b):
        t=F.add(F.mul(a[0],b[0]),0)
        a0,a1,a2,a3=a;b0,b1,b2,b3=b
        return (F.mul(a0,b0),
                F.add(F.mul(a0,b1),F.mul(a1,b0)),
                F.add(F.mul(a0,b2),F.mul(a2,b0)),
                F.add(F.add(F.mul(a0,b3),F.mul(a3,b0)),F.add(F.mul(a1,b2),F.mul(minus_inv,F.mul(a2,b1)))))
    e=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    def scale(a,u):return tuple(F.mul(a,t) for t in u)
    def add(a,b):return tuple(F.add(x,y) for x,y in zip(a,b))
    def rank(mat):
        M=[list(row) for row in mat];nr=len(M);nc=len(M[0]);row=0
        for col in range(nc):
            k=next((k for k in range(row,nr) if M[k][col]),None)
            if k is None: continue
            M[row],M[k]=M[k],M[row]
            scale=F.inv(M[row][col]);M[row]=[F.mul(scale,x) for x in M[row]]
            for z in range(nr):
                if z!=row and M[z][col]:
                    a=M[z][col]
                    M[z]=[F.add(M[z][i],F.neg(F.mul(a,M[row][i]))) for i in range(nc)]
            row+=1
            if row==nr:break
        return row
    counts=0;by_lin={};nrel=0;fixed_hist={}
    for aa,bb,cc,dd in product(range(q),repeat=4):
        det=F.add(F.mul(aa,dd),F.neg(F.mul(bb,cc)))
        if det==0:continue
        for h1,h2 in product(range(q),repeat=2):
            sx=(0,aa,cc,h1);sy=(0,bb,dd,h2)
            # Verify every presentation relation directly before considering involution.
            if prod(sx,sx)!=(0,0,0,0) or prod(sy,sy)!=(0,0,0,0):continue
            szy=prod(sy,sx);sz=prod(sx,sy)
            if add(szy,scale(lam,sz))!=(0,0,0,0):continue
            nrel+=1
            S=(e[0],sx,sy,prod(sy,sx))  # WARNING: z = xy, so sigma(z)=sigma(y)sigma(x).
            def apply(v):
                y=(0,0,0,0)
                for i in range(4): y=add(y,scale(v[i],S[i]))
                return y
            if all(apply(S[i])==e[i] for i in range(4)):
                counts+=1
                mat=[[F.add(S[j][i],F.neg(1) if i==j else 0) for j in range(4)] for i in range(4)]
                fixdim=4-rank(mat)
                fixed_hist[fixdim]=fixed_hist.get(fixdim,0)+1
                by_lin[(aa,bb,cc,dd)]=by_lin.get((aa,bb,cc,dd),0)+1
    # The appropriate finite-field formula is checked independently.
    if lam!=1 and lam!=F.neg(1): expect=q*(q-1)
    elif lam==1 and F.p==2:expect=q**3+q**2-q
    elif lam==1: expect=q**3+2*q**2+1
    else: expect=2*q**2+q+1
    assert counts==expect,(q,lam,counts,expect)
    if lam!=1 and lam!=F.neg(1): expected_hist={3:q*(q-1)}
    elif lam==1 and F.p==2: expected_hist={4:1,3:q**3+q**2-q-1}
    elif lam==1:expected_hist={1:1,3:q**3+2*q**2}
    else:expected_hist={4:1,3:q*(q-1),2:q*q+2*q}
    assert fixed_hist==expected_hist,(q,lam,fixed_hist,expected_hist)
    assert by_lin
    return counts,nrel,len(by_lin),fixed_hist

def main():
    configs=[(Field(2),[1]),(Field(3),[1,2]),(Field(5),[1,2,4]),
             (Field(2,[1,1,1]),[1,2,3])] # GF4: u^2+u+1
    for F,lams in configs:
        for lam in lams:
            c,na,nl,hist=direct(F,lam)
            print(f'GF({F.q}), lambda={lam}: anti_involutions={c}, candidate_anti_automorphisms={na}, linear_involutions={nl}, fixed_space_histogram={hist}')
    print('QUANTUM_EXTERIOR_ANTI_INVOLUTIONS_ORIGINAL_PRODUCTS_OK')
if __name__=='__main__':main()
