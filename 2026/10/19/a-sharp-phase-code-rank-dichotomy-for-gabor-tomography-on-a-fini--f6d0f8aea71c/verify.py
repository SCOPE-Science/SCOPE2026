#!/usr/bin/env python3
"""Independent finite-field ambiguity and matrix-rank verification for cross windows."""
import cmath
import itertools
from collections import Counter
import numpy as np

# Monic irreducible polynomial coefficients ascending, when m>1.
FIELD_SPECS = [(2,(0,1)),(3,(0,1)),(2,(1,1,1)),(5,(0,1)),(7,(0,1)),(2,(1,1,0,1)),(3,(1,0,1)),(11,(0,1))]

class Field:
    def __init__(self,p,modulus):
        self.p=p
        self.m=len(modulus)-1
        self.q=p**self.m
        self.modulus=tuple(modulus)
        self.digits=[tuple((n//p**i)%p for i in range(self.m)) for n in range(self.q)]
        self.lookup={x:i for i,x in enumerate(self.digits)}
        self.plus=[[self.lookup[tuple((a+b)%p for a,b in zip(self.digits[i],self.digits[j]))] for j in range(self.q)] for i in range(self.q)]
        self.neg=[self.lookup[tuple(-a%p for a in self.digits[i])] for i in range(self.q)]
        self.mul=[[self._multiply(i,j) for j in range(self.q)] for i in range(self.q)]
        self.trace=[self._trace(i) for i in range(self.q)]
        self.char=[cmath.exp(2j*cmath.pi*t/p) for t in self.trace]
    def _multiply(self,i,j):
        p,m=self.p,self.m
        a,b=self.digits[i],self.digits[j]
        poly=[0]*(2*m-1)
        for k in range(m):
            for h in range(m):poly[k+h]=(poly[k+h]+a[k]*b[h])%p
        for k in range(2*m-2,m-1,-1):
            t=poly[k]
            for j in range(m):poly[k-m+j]=(poly[k-m+j]-t*self.modulus[j])%p
        return self.lookup[tuple(poly[:m])]
    def power(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul[r][a]
            a=self.mul[a][a];n>>=1
        return r
    def _trace(self,a):
        vals=[a]
        for _ in range(1,self.m):vals.append(self.power(vals[-1],self.p))
        t=0
        for u in vals:t=self.plus[t][u]
        if t not in range(self.p):raise AssertionError(('bad trace',t))
        return t

def verify(qspec,check_gram=False):
    F=Field(*qspec);q,p=F.q,F.p
    S={(x,0) for x in range(q)} | {(0,y) for y in range(q)}
    N=q*q
    assert len(S)==2*q-1
    plus,neg,mul=F.plus,F.neg,F.mul
    def plus2(x,y):return (plus[x[0]][y[0]], plus[x[1]][y[1]])
    def sub2(x,y):return (plus[x[0]][neg[y[0]]],plus[x[1]][neg[y[1]]])
    def ps(xi,x):
        t=plus[mul[xi[0]][x[0]]][mul[xi[1]][x[1]]]
        return F.char[t]
    codes={'flat':1+0j,'sign':-1+0j,'ternary':cmath.exp(2j*cmath.pi/3)}
    out={}
    for name,z in codes.items():
        M=2*q-2+abs(z)**2
        G={s:(z if s==(0,0) else 1+0j)/M**0.5 for s in S}
        amp={}
        for h in itertools.product(range(q),repeat=2):
            overlaps=[(x,sub2(x,h)) for x in S if sub2(x,h) in S]
            for xi in itertools.product(range(q),repeat=2):
                val=sum(G[x]*G[y].conjugate()*ps(xi,x).conjugate() for x,y in overlaps)
                amp[(h,xi)]=val
        nz={k:val for k,val in amp.items() if abs(val)>1.e-8}
        rank=len(nz)
        if name=='flat':
            want=N+2*q*(q-1)+(q-1)**2*N*(1 if p%2 else 0.5)
        elif name=='sign' and p%2:
            want=N*N
        elif name=='ternary' and p==2:
            want=N*N-(q-1)**2*N//2
        else:want=None
        if want is not None: assert rank==want,(q,name,rank,want)
        if name=='ternary' and p==2:
            for (h,xi),val in amp.items():
                predicted=(h[0]!=0 and h[1]!=0 and F.trace[plus[mul[h[0]][xi[0]]][mul[h[1]][xi[1]]]]==1)
                assert (abs(val)<1e-8)==predicted,(q,name,h,xi,val,predicted)
        out[name]=rank
        if check_gram and name in ['sign','ternary']:
            # Recover the projector Gram spectrum independently using actual dense matrices.
            shifts=list(itertools.product(range(q),repeat=2))
            mods=shifts
            xx=list(itertools.product(range(q),repeat=2))
            vecs=[]
            for h in shifts:
                translated=np.array([G.get(sub2(x,h),0j) for x in xx])
                for xi in mods:
                    v=translated*np.array([ps(xi,x) for x in xx])
                    vecs.append(np.outer(v,v.conjugate()).reshape(-1))
            mat=np.stack(vecs,axis=0)
            gram=mat@mat.conjugate().T
            ev=np.linalg.eigvalsh(gram)
            numerical_rank=int(sum(ev>1e-7))
            assert numerical_rank==rank,(q,name,numerical_rank,rank)
            assert abs(float(ev.max())-N)<1.e-7,(q,name,ev.max())
    print(f'q={q:>2} p={p}  flat_rank={out["flat"]:>6}  sign_rank={out["sign"]:>6}  ternary_rank={out["ternary"]:>6}  ambient={N*N:>6}'+('  direct_Gram=PASS' if check_gram else ''))

if __name__=='__main__':
    for spec in FIELD_SPECS:
        q=spec[0]**(len(spec[1])-1)
        verify(spec, check_gram=q in (2,3,4))
    print('ALL CHECKS PASSED')
