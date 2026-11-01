"""Integral chain certificate for the diagonal-deletion chessboard inclusion.

Run with Python 3.10+; standard library and sympy are required.
All matrices are generated from the graph definition with integral coefficients.
"""
from itertools import combinations, permutations
from collections import defaultdict, Counter
from hashlib import sha256
import json

N=6
P=3

def faces(forbid_diagonal):
    F=[]
    for k in range(1,N+1):
        level=[]
        for rows in combinations(range(N),k):
            for cols in permutations(range(N),k):
                if forbid_diagonal and any(i==j for i,j in zip(rows,cols)):
                    continue
                level.append(tuple(i*N+j for i,j in zip(rows,cols)))
        F.append(sorted(level))
    return F

def boundaries(F,degree):
    low={s:i for i,s in enumerate(F[degree-1])}
    return [{low[s[:j]+s[j+1:]]: (-1 if j%2 else 1)
             for j in range(len(s))} for s in F[degree]]

def reduce_units_with_witness(columns):
    # A unimodular integral column elimination, followed by deletion of an
    # isolated unit pivot. The surviving columns carry full original-basis
    # witness vectors, allowing independent reconstruction of boundaries.
    cols={j:col.copy() for j,col in enumerate(columns)}
    reprs={j:{j:1} for j in cols}
    rows=defaultdict(dict)
    for j,col in cols.items():
        for i,a in col.items():rows[i][j]=a
    unit_count=0
    while True:
        pick=None
        for i,rd in rows.items():
            if len(rd)==1:
                (j,v),=rd.items()
                if abs(v)==1:
                    pick=(0,i,j,v)
                    break
            lowcost=len(rd)-1
            if pick is not None and lowcost>pick[0]:
                continue
            for j,v in rd.items():
                if abs(v)!=1:continue
                cost=lowcost*(len(cols[j])-1)
                if pick is None or cost<pick[0]:
                    pick=(cost,i,j,v)
                    if cost==0:break
            if pick is not None and pick[0]==0:break
        if pick is None:break
        _,r,c,pivot=pick
        pc=cols[c].copy()
        pr=reprs[c]
        row=rows[r].copy()
        for k,x in row.items():
            if k==c:continue
            mult=x*pivot
            ck=cols[k]
            for i,a in pc.items():
                if i==r:continue
                z=ck.get(i,0)-mult*a
                if z:
                    ck[i]=z;rows[i][k]=z
                else:
                    ck.pop(i,None);rows[i].pop(k,None)
                    if not rows[i]:rows.pop(i,None)
            ck.pop(r,None)
            # Track the exact integral new column as a combination of the
            # ORIGINAL columns; no rational scaling occurs.
            v=reprs[k]
            for original,a in pr.items():
                z=v.get(original,0)-mult*a
                if z:v[original]=z
                else:v.pop(original,None)
        cols.pop(c)
        reprs.pop(c)
        for i in pc:
            if i==r:continue
            rows[i].pop(c,None)
            if not rows[i]:rows.pop(i,None)
        rows.pop(r,None)
        unit_count+=1
    return unit_count,cols,reprs

def linear_combination(boundary,vector):
    out=defaultdict(int)
    for j,x in vector.items():
        for i,y in boundary[j].items():out[i]+=x*y
    return {i:x for i,x in out.items() if x}

def mod_p_basis(columns,p=3):
    basis={}
    for column in columns:
        z={i:v%p for i,v in column.items() if v%p}
        while z:
            i=max(z)
            if i not in basis:
                q=pow(z[i],-1,p)
                basis[i]={r:v*q%p for r,v in z.items()}
                break
            q=z[i]
            for r,v in basis[i].items():
                t=(z.get(r,0)-q*v)%p
                if t:z[r]=t
                else:z.pop(r,None)
    return basis

def reduce_mod_p(column,basis,p=3):
    z={i:v%p for i,v in column.items() if v%p}
    while z and max(z) in basis:
        q=z[max(z)]
        for r,v in basis[max(z)].items():
            t=(z.get(r,0)-q*v)%p
            if t:z[r]=t
            else:z.pop(r,None)
    return z

def main():
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    a=faces(True); b=faces(False)
    assert list(map(len,a))==[30,315,1420,2715,1854,265]
    assert list(map(len,b))==[36,450,2400,5400,4320,720]
    assert all(set(level_a)<=set(level_b) for level_a,level_b in zip(a,b))
    dA=boundaries(a,4)
    dB=boundaries(b,4)
    count,residual,reps=reduce_units_with_witness(dA)
    assert count==1552
    assert len(residual)==302
    # Check EVERY surviving column, including the zero columns, in the original signed matrix.
    assert all(linear_combination(dA,reps[j])==residual[j] for j in residual)
    nz=[j for j,v in residual.items() if v]
    assert len(nz)==16
    assert all(v%3==0 for j in nz for v in residual[j].values())
    # Each witness is a 4-chain whose boundary is exactly 3 times a cycle.
    # Recompute with the UNREDUCED original signed simplicial boundary.
    zA=[]
    d3A=boundaries(a,3)
    for j in nz:
        zz={i:v//3 for i,v in residual[j].items()}
        assert linear_combination(dA,reps[j])=={i:3*v for i,v in zz.items()}
        assert not linear_combination(d3A,zz)
        zA.append(zz)
    ri=sorted({i for j in nz for i in residual[j]})
    T=Matrix([[residual[j].get(i,0)//3 for j in nz] for i in ri])
    S=smith_normal_form(T, domain=ZZ)
    assert [abs(int(S[k,k])) for k in range(5)]==[1]*5
    assert all(S[k,k]==0 for k in range(5,16))
    pbA=mod_p_basis(dA)
    az=[reduce_mod_p(z,pbA) for z in zA]
    assert len(pbA)==1552
    assert len(mod_p_basis(az))==5
    # Independently form complete-board boundaries and project embedded cycles.
    pbB=mod_p_basis(dB)
    ixB={s:i for i,s in enumerate(b[3])}
    zB=[{ixB[a[3][i]]:v for i,v in z.items()} for z in zA]
    bz=[reduce_mod_p(z,pbB) for z in zB]
    assert len(pbB)==3380
    assert len(mod_p_basis(bz))==5
    print('A face vector: '+str([1]+list(map(len,a))))
    print('B face vector: '+str([1]+list(map(len,b))))
    print('Integral pivot units: '+str(count))
    print('Residual nonzero columns: '+str(len(nz)))
    print('Residual Smith factors after division by 3: 1,1,1,1,1')
    print('mod-3 boundary ranks A,B: '+str((len(pbA),len(pbB))))
    print('Bockstein-span dimension A: '+str(len(mod_p_basis(az))))
    print('Bockstein-span image dimension B: '+str(len(mod_p_basis(bz))))
    print('Integral 3-torsion inclusion: INJECTIVE')
    print('VERIFY_OK')

if __name__=='__main__':main()
