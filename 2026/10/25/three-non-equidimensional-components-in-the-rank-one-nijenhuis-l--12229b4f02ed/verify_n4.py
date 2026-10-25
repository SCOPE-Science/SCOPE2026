#!/usr/bin/env python3
"""Independent basis-level test of the rank-one Lie Nijenhuis classification.

Every equation is reconstructed from commutators of 4-by-4 matrix units.
The field of order 4 is represented with X^2+X+1.
"""
from itertools import product

PAIRS = [(0, 1), (1, 2), (2, 3), (0, 2), (1, 3), (0, 3)]
DIM = len(PAIRS)

class Field:
    def __init__(self, q):
        self.q = q
        self.char = 2 if q == 4 else q
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q
    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q
    def mul(self, a, b):
        if self.q != 4: return a * b % self.q
        ans = 0
        for i in range(2):
            for j in range(2):
                if (a >> i) & 1 and (b >> j) & 1:
                    ans ^= 1 << (i+j)
        if ans & 8: raise AssertionError('unexpected degree')
        if ans & 4: ans ^= 7  # x^2 = x+1
        return ans
    def inv(self, a):
        assert a != 0
        return next(b for b in range(1,self.q) if self.mul(a,b) == 1)
    def sub(self, a,b):
        return self.add(a,self.neg(b))

def bracket(x,y,F):
    z = [0]*DIM
    for i,(r,s) in enumerate(PAIRS):
        if not x[i]: continue
        for j,(t,u) in enumerate(PAIRS):
            if not y[j]: continue
            xij = F.mul(x[i],y[j])
            if s == t and (r,u) in PAIRS:
                k = PAIRS.index((r,u)); z[k]=F.add(z[k],xij)
            if u == r and (t,s) in PAIRS:
                k = PAIRS.index((t,s)); z[k]=F.sub(z[k],xij)
    return z

def dot(f,x,F):
    ret=0
    for u,v in zip(f,x): ret=F.add(ret,F.mul(u,v))
    return ret

def torsion_coeff(f,a,i,j,F):
    ei=[int(k==i) for k in range(DIM)]
    ej=[int(k==j) for k in range(DIM)]
    # The scalar equation from the full Nijenhuis torsion of N(x)=f(x)a.
    gij=bracket(ei,ej,F)
    gaj=bracket(a,ej,F)
    gia=bracket(ei,a,F)
    return F.sub(F.add(F.mul(f[i],dot(f,gaj,F)), F.mul(f[j],dot(f,gia,F))), F.mul(dot(f,a,F),dot(f,gij,F)))

def rank(M,F):
    M=[row[:] for row in M]
    rr=0
    for j in range(DIM):
        piv=next((r for r in range(rr,len(M)) if M[r][j]!=0),None)
        if piv is None:continue
        M[rr],M[piv]=M[piv],M[rr]
        inv=F.inv(M[rr][j]);M[rr]=[F.mul(inv,x) for x in M[rr]]
        for r in range(len(M)):
            if r==rr:continue
            fac=M[r][j]
            if fac:
                M[r]=[F.sub(x,F.mul(fac,y)) for x,y in zip(M[r],M[rr])]
        rr+=1
        if rr==DIM:break
    return rr

def main():
    for q in (2,3,4,5):
        F=Field(q)
        stat={'I':0,'II':0,'III':0}
        classes={'I':1,'II':3,'III':6}
        for fv in product(range(q),repeat=DIM):
            if not any(fv):continue
            # Natural matrix-unit order: a,b,c,d,e,z maps to [0,1,3,2,4,5].
            # Coordinate access below always uses actual matrix-unit indexing.
            f=[fv[0],fv[1],fv[2],fv[3],fv[4],fv[5]]
            # d = E13 index3; e = E24 index4; z = E14 index5.
            cat='I' if f[5] else 'II' if (f[3] or f[4]) else 'III'
            M=[]
            for i in range(DIM):
                for j in range(i+1,DIM):
                    row=[]
                    for k in range(DIM):
                        a=[int(t==k) for t in range(DIM)]
                        row.append(torsion_coeff(f,a,i,j,F))
                    M.append(row)
            dim=DIM-rank(M,F)
            assert dim==classes[cat],(q,f,cat,dim)
            stat[cat]+=1
        expected={'I':(q-1)*q**5,'II':q**3*(q**2-1),'III':q**3-1}
        assert stat==expected,(q,stat,expected)
        count=sum(stat[c]*(q**classes[c]-1)//(q-1) for c in stat)
        formula=((q**3-1)*(q**6-1)+q**3*(q**2-1)*(q**3-1))//(q-1)+(q-1)*q**5
        assert count==formula
        # Independently check full torsion, not just the formula, for all 63 x 63 pairs when q=2.
        if q==2:
            good=0
            vectors=[v for v in product(range(q),repeat=DIM) if any(v)]
            for fv in vectors:
                for a in vectors:
                    valid=all(torsion_coeff(fv,a,i,j,F)==0 for i in range(DIM) for j in range(i+1,DIM))
                    if valid:good+=1
            assert good==formula==(641)
        print('Q',q,'f-strata',stat,'rank-one Nijenhuis operators',count)
    print('N4_RANK_ONE_NIJENHUIS_OK')

if __name__=='__main__': main()
