#!/usr/bin/env python3
"""Exact finite-field collision and sharp fourth-moment checks for odd-characteristic Frobenius graphs.
Uses only the Python standard library. Finite tests corroborate, but do not establish, universal claims.
"""
from collections import defaultdict
from math import gcd, pi
from cmath import exp

class Field:
    def __init__(self,p,poly):
        self.p=p; self.m=len(poly); self.poly=poly; self.q=p**self.m
        self.digits=[self.dec(i) for i in range(self.q)]
        self.add=[[self.enc([(x+y)%p for x,y in zip(self.digits[a],self.digits[b])])
                   for b in range(self.q)] for a in range(self.q)]
        self.neg=[self.enc([(-x)%p for x in self.digits[a]]) for a in range(self.q)]
        self.mul=[[self._mult(a,b) for b in range(self.q)] for a in range(self.q)]
    def dec(self,a):
        out=[]
        for _ in range(self.m):out.append(a%self.p);a//=self.p
        return out
    def enc(self,ds):return sum(x*self.p**i for i,x in enumerate(ds))
    def _mult(self,a,b):
        p=self.p;m=self.m;x=self.digits[a];y=self.digits[b];w=[0]*(2*m-1)
        for i in range(m):
            for j in range(m):w[i+j]=(w[i+j]+x[i]*y[j])%p
        for j in range(2*m-2,m-1,-1):
            t=w[j]
            if t:
                for i in range(m):w[j-m+i]=(w[j-m+i]-t*self.poly[i])%p
        return self.enc(w[:m])
    def sub(self,a,b):return self.add[a][self.neg[b]]
    def power(self,a,n):
        ans=1
        while n:
            if n&1:ans=self.mul[ans][a]
            a=self.mul[a][a];n>>=1
        return ans
    def trace(self,a):
        t=0;x=a
        for _ in range(self.m):t=self.add[t][x];x=self.power(x,self.p)
        assert t<self.p, ('trace',self.p,self.m,t)
        return t

CASES=[(3,[0],1),(5,[0],1),(7,[0],2),
       (3,[1,0],1),(3,[1,2,0],1),(3,[2,1,0,0],1),
       (3,[2,1,0,0],2),(5,[2,0],1),(7,[1,0],1)]
# [0] means degree-one polynomial X over F_p.

def modular_rank(rows, n, prime=101):
    pivots={}
    for row in rows:
        v=[x%prime for x in row]
        while True:
            j=next((i for i,x in enumerate(v) if x),None)
            if j is None:break
            if j in pivots:
                z=pivots[j];a=v[j]
                v=[(u-a*w)%prime for u,w in zip(v,z)]
            else:
                inv=pow(v[j],-1,prime)
                pivots[j]=[(x*inv)%prime for x in v]
                break
    return len(pivots)

def check_case(p,poly,k):
    F=Field(p,poly);q=F.q;m=F.m;d=gcd(m,k);e=p**k+1
    g=gcd(e,q-1)
    expected=2 if m//d%2 else p**d+1
    assert g==expected,(p,m,k,g,expected)
    A=F.add;M=F.mul; root={u for u in range(1,q) if F.power(u,e)==1}
    assert len(root)==g
    fibers=defaultdict(list)
    for a in range(q):
        for b in range(q):
            fibers[(A[a][b],A[F.power(a,e)][F.power(b,e)])].append((a,b))
    counts=defaultdict(int)
    for vals in fibers.values():counts[len(vals)]+=1;assert len(vals) in (1,g)
    assert counts[1]==q and counts[g]==q*(q-1)//g if g!=1 else True
    energy=sum(len(v)**2 for v in fibers.values())
    assert energy==q*(1+(q-1)*g)
    values=[(3*t*t+5*t+1)%7-3 for t in range(q)]
    S=sum(v*v for v in values);four=sum(v**4 for v in values)
    W=sum(sum(values[a]*values[b] for a,b in v)**2 for v in fibers.values())
    half=F.enc([(p+1)//2]+[0]*(m-1))
    orbits={}
    for h in range(1,q):
        o=tuple(sorted({M[h][z] for z in root}));orbits[o]=1
    gap=0
    for s in range(q):
        for orb in orbits:
            u=[]
            for h in orb:
                a=M[half][A[s][h]];b=M[half][F.sub(s,h)]
                u.append(values[a]*values[b])
            gap+=sum((u[i]-u[j])**2 for i in range(g) for j in range(i+1,g))
    assert g*S*S-(g-1)*four-W==gap, (p,m,k,g,S,W,gap)
    # Flat phases: zero-phase always extremal; for g=2 arbitrary phases do.
    if g==2:
        phase=[(t*t+2*t*t*t+7*t)%p for t in range(q)]
        for s in range(q):
            for orb in orbits:
                u=[]
                for h in orb:
                    a=M[half][A[s][h]];b=M[half][F.sub(s,h)]
                    u.append((phase[a]+phase[b])%p)
                assert len(set(u))==1
    else:
        assert F.power(next(z for z in root if z not in (1,F.neg[1])),p**d+1)==1
        nonlinear_found=False
        for alpha in range(1,q):
            phase=[F.trace(M[alpha][F.power(t,p**d+1)]) for t in range(q)]
            for s in range(q):
                for orb in orbits:
                    u=[]
                    for h in orb:
                        a=M[half][A[s][h]];b=M[half][F.sub(s,h)]
                        u.append((phase[a]+phase[b])%p)
                    assert len(set(u))==1
            if any((phase[A[a][b]]-phase[a]-phase[b]+phase[0])%p for a in range(q) for b in range(q)):
                nonlinear_found=True;break
        assert nonlinear_found,(p,m,k)
    if g>2 and q<=25:
        zeta=next(z for z in root if z not in (1,F.neg[1]))
        rows=[]
        for x in range(q):
            for h in range(1,q):
                v=[0]*q
                for t,sgn in ((A[x][h],1),(F.sub(x,h),1),
                              (A[x][M[zeta][h]],-1),(F.sub(x,M[zeta][h]),-1)):
                    v[t]+=sgn
                rows.append(v)
        assert modular_rank(rows,q)==q-1, ('phase-lattice-rank',p,m,k)
    if q<=25:
        roots=[exp(2j*pi*v/p) for v in range(p)]
        calc=0.0
        for xi in range(q):
            for eta in range(q):
                z=0j
                for t in range(q):
                    phase=F.trace(A[M[xi][t]][M[eta][F.power(t,e)]])
                    z+=values[t]*roots[phase]
                calc+=abs(z)**4
        calc/=q*q
        assert abs(calc-W)<1e-7*max(1,W),(p,m,k,calc,W)
    return q,g,energy

def main():
    for p,poly,k in CASES:
        q,g,energy=check_case(p,poly,k)
        print('CASE_OK',f'p={p}',f'm={len(poly)}',f'k={k}',f'q={q}',f'root_size={g}',f'additive_energy={energy}')
    print('VERIFY_OK',f'field_parameter_cases={len(CASES)}','exact_collision_and_deficit=all','nonlinear_phase=all_nonplanar','direct_Fourier=small_cases')
if __name__=='__main__':main()
