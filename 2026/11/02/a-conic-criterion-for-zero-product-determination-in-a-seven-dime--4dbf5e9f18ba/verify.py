#!/usr/bin/env python3
"""Exact finite-field checks for the specified seven-dimensional two-step Lie algebra.
Uses only the standard library; GF(4) is given by t*t=t+1.
"""
from itertools import product, combinations

class F:
    def __init__(self,q):
        assert q in (2,3,4,5,7)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        z=0
        for i in (0,1):
            for j in (0,1):
                if ((a>>i)&1) and ((b>>j)&1):z ^= 1<<(i+j)
        if z&8:z^=0b1100
        if z&4:z^=0b111
        return z
    def inv(self,a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise AssertionError
    def rank(self,rows):
        m=[list(r) for r in rows]
        if not m:return 0
        piv=0
        for j in range(len(m[0])):
            i=next((i for i in range(piv,len(m)) if m[i][j]),None)
            if i is None:continue
            m[piv],m[i]=m[i],m[piv]
            t=self.inv(m[piv][j]);m[piv]=[self.mul(t,x) for x in m[piv]]
            for h in range(len(m)):
                if h==piv:continue
                t=m[h][j]
                if t:m[h]=[self.sub(m[h][k],self.mul(t,m[piv][k])) for k in range(len(m[0]))]
            piv+=1
            if piv==len(m):break
        return piv

def bracket(f,u,v):
    p=[f.sub(f.mul(u[i],v[j]),f.mul(u[j],v[i])) for i,j in combinations(range(4),2)]
    return (f.sub(p[0],p[5]), f.add(p[1],p[4]),f.sub(p[2],p[3]))

def Q(f,a,b,c):return f.add(f.add(f.mul(a,a),f.mul(b,b)),f.mul(c,c))

def grassmann_planes(f):
    for i in range(4):
        for j in range(i+1,4):
            r=[0]*4;s=[0]*4
            r[i]=s[j]=1
            free_r=[k for k in range(i+1,4) if k!=j]
            free_s=list(range(j+1,4))
            for vals in product(range(f.q),repeat=len(free_r)+len(free_s)):
                a=r.copy();b=s.copy()
                for k,x in zip(free_r,vals):a[k]=x
                for k,x in zip(free_s,vals[len(free_r):]):b[k]=x
                yield a,b

def check(q):
    f=F(q)
    roots=[(a,b,c) for a,b,c in product(range(q),repeat=3) if Q(f,a,b,c)==0]
    root_rank=f.rank(roots)
    expect_rank=2 if q in (2,4) else 3
    assert root_rank==expect_rank,(q,root_rank)
    # Direct alternate recovery of bracket kernel from all six coefficient columns.
    b_columns=[]
    basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    for u,v in combinations(basis,2):b_columns.append(bracket(f,u,v))
    assert b_columns==[(1,0,0),(0,1,0),(0,0,1),(0,0,f.neg(1)),(0,1,0),(f.neg(1),0,0)]
    # Pluecker-kernel vectors are exactly the diagonalized triple conic.
    for a,b,c in product(range(q),repeat=3):
        p=(a,b,c,c,f.neg(b),a)
        assert (f.sub(p[0],p[5]),f.add(p[1],p[4]),f.sub(p[2],p[3]))==(0,0,0)
        pf=f.add(f.sub(f.mul(p[0],p[5]),f.mul(p[1],p[4])),f.mul(p[2],p[3]))
        assert pf==Q(f,a,b,c)
    all_planes=list(grassmann_planes(f))
    expected_grass=((q**4-1)*(q**3-1))//((q**2-1)*(q-1)) # [4 choose 2]_q? incorrect formula check below
    expected_grass=(q*q+1)*(q*q+q+1)
    assert len(all_planes)==expected_grass,(q,len(all_planes),expected_grass)
    commuting_planes=sum(not any(bracket(f,u,v)) for u,v in all_planes)
    assert commuting_planes==q+1,(q,commuting_planes)
    expected_pairs=2*q**5+q**4-2*q**3
    # Direct brute-force field operations on all vectors for modest fields.
    if q<=5:
        vectors=list(product(range(q),repeat=4));paircount=0
        for u in vectors:
            for v in vectors:
                if bracket(f,u,v)==(0,0,0):paircount+=1
        assert paircount==expected_pairs,(q,paircount,expected_pairs)
    else:paircount=None
    assert f.rank([(1,0,0),(0,1,0),(0,0,1)])==3
    print(f'q={q} isotropic_cone_nonzero={len(roots)-1} kernel_root_span={root_rank} zpd_defect={3-root_rank} commuting_planes={commuting_planes} planes_tested={len(all_planes)} commuting_V_pairs={expected_pairs} exhaustive_pairs={paircount is not None} commuting_L_pairs={q**6*expected_pairs}')

if __name__=='__main__':
    for q in [2,3,4,5,7]:check(q)
    print('QUATERNIONIC7_ZPD_CONIC_AND_COMMUTING_CENSUS_OK 5_FIELDS')
