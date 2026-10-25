"""Reproducible exact finite checks of the Hermite-product and two-angle rank statements.
The analytic proof is needed for the all-dimension theorem; these finite checks do not certify it.
"""
from functools import lru_cache
import sympy as sp
x=sp.symbols('x')
@lru_cache(None)
def H(n):
    return sp.Poly(sp.hermite(n,x),x)

def raw_columns(d,r):
    deg=2*r*(d-1)
    return {(i,j):[int((H(r*i)*H(r*j)).nth(k)) for k in range(deg+1)]
            for i in range(d) for j in range(i,d)}

def matrix_rank_mod(A,p=1000000007):
    if not A:return 0
    z=[[int(v)%p for v in row] for row in A]
    m,n=len(z),len(z[0]); rank=0
    for c in range(n):
        k=next((i for i in range(rank,m) if z[i][c]),None)
        if k is None:continue
        z[rank],z[k]=z[k],z[rank]
        inv=pow(z[rank][c],p-2,p)
        z[rank]=[v*inv%p for v in z[rank]]
        for i in range(rank+1,m):
            if z[i][c]:
                factor=z[i][c]
                z[i]=[(a-factor*b)%p for a,b in zip(z[i],z[rank])]
        rank+=1
        if rank==m:break
    return rank

def check(d,r):
    P=raw_columns(d,r)
    deg=2*r*(d-1)
    # Basis columns are diagonal entries, real and imaginary offdiagonals.
    labels=[('diag',i,i) for i in range(d)]
    for i in range(d):
        for j in range(i+1,d):
            labels.extend([('real',i,j),('imag',i,j)])
    def two_phase(b):
        # phase 0 then pi/(b*r).  Use exact cyclotomic values when b=1 or 2.
        assert b in (1,2)
        def factor(typ,i,j,phase):
            if typ=='diag':return 1
            if phase==0:return 2 if typ=='real' else 0
            k=j-i
            if b==1:return 2*((-1)**k) if typ=='real' else 0
            c=[1,0,-1,0][k%4]
            s=[0,1,0,-1][k%4]
            return 2*(c if typ=='real' else s)
        rows=[]
        for phase in (0,1):
            for k in range(deg+1):
                rows.append([factor(t,i,j,phase)*P[i,j][k] for t,i,j in labels])
        return matrix_rank_mod(rows)
    u=[P[i,j] for i in range(d) for j in range(i,d)]
    product_rank=matrix_rank_mod(u)
    assert product_rank==d*(d+1)//2,(d,r,product_rank)
    res={}
    for b in (1,2):
        resonance=sum(d-k for k in range(1,d) if k%b==0)
        found=two_phase(b)
        expected=d*d-resonance
        assert found==expected,(d,r,b,found,expected)
        res[b]=found
    return {'d':d,'r':r,'unordered_product_rank':product_rank,
            'two_angle_ranks':{'pi_over_r':res[1],'pi_over_2r':res[2]}}

if __name__=='__main__':
    out=[]
    for d in range(2,8):
        r=2*((d-1)//2)+1
        out.append(check(d,r))
    # A direct countercheck of a four-spaced, four-level ladder (covered by the theorem).
    out.append(check(4,4))
    for a in out:print(a)
    # In a four-step Fock ladder, the nonresonant pair (0, pi/16)
    # supplies all 16 real matrix coordinates. Use exact sqrt(2) arithmetic.
    d,r=4,4
    polys={(i,j):H(r*i)*H(r*j) for i in range(d) for j in range(i,d)}
    labels=[('D',i,i) for i in range(d)]
    labels += [(kind,i,j) for i in range(d) for j in range(i+1,d)
               for kind in ('R','I')]
    def phase_coefficient(kind,i,j,phase):
        if kind=='D':return 1
        if phase==0:return 2 if kind=='R' else 0
        k=j-i
        return 2*(sp.cos(sp.pi*k/4) if kind=='R' else sp.sin(sp.pi*k/4))
    rows=[[phase_coefficient(kind,i,j,phase)*polys[i,j].nth(k)
           for kind,i,j in labels]
          for phase in (0,1) for k in range(2*r*(d-1)+1)]
    exact_generic=sp.Matrix(rows).rank()
    assert exact_generic==d*d
    print('nonresonant exact algebraic rank for d=4,r=4,Delta=pi/16:',exact_generic)
    print('PASS: exact integer coefficients for 7 parameter pairs, 14 resonant two-angle ranks, 1 nonresonant rank')
