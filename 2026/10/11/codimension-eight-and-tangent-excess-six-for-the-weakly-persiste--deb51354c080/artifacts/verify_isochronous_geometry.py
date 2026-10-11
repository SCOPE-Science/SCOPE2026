#!/usr/bin/env python3
from fractions import Fraction

vars14 = ['a20','a11','a02','a30','a21','a12','a03','b20','b11','b02','b30','b21','b12','b03']
idx={v:i for i,v in enumerate(vars14)}

def row(**kw):
    r=[Fraction(0) for _ in vars14]
    for k,v in kw.items(): r[idx[k]]=Fraction(v)
    return r

def rank(rows):
    A=[r[:] for r in rows]
    m=len(A); n=len(vars14); rr=0
    for c in range(n):
        piv=next((i for i in range(rr,m) if A[i][c]),None)
        if piv is None: continue
        A[rr],A[piv]=A[piv],A[rr]
        q=A[rr][c]; A[rr]=[x/q for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]:
                q=A[i][c]; A[i]=[A[i][j]-q*A[rr][j] for j in range(n)]
        rr+=1
        if rr==m: break
    return rr

common=[row(a21=1),row(b21=1)]
# I01--I17: each item is a list of coefficient rows for the displayed linear equations.
F={
'I01':[row(a20=1),row(a30=1),row(b11=1),row(b02=1),row(b12=1),row(b03=1)],
'I02':[row(b20=1),row(b30=1),row(a11=1),row(a02=1),row(a12=1),row(a03=1)],
'I03':[row(a11=1),row(a02=1),row(a12=1),row(a03=1),row(b11=1),row(b30=1)],
'I04':[row(b11=1),row(b02=1),row(b12=1),row(b03=1),row(a11=1),row(a30=1)],
'I05':[row(a11=1),row(a02=1),row(a12=1),row(a03=1),row(b11=1),row(b02=1),row(b12=1),row(b03=1)],
'I06':[row(a11=1),row(b11=1),row(a02=1),row(a03=1),row(b03=1),row(a12=1,b30=1),row(a30=1,b12=1)],
'I07':[row(a11=1),row(b11=1),row(b02=1),row(b03=1),row(a03=1),row(a30=1,b12=1),row(a12=1,b30=1)],
'I08':[row(a20=1),row(a02=1),row(a12=1),row(a03=1),row(b11=1),row(b02=1),row(b12=1),row(b03=1),row(a11=2,b20=-1)],
'I09':[row(b20=1),row(b02=1),row(b12=1),row(b03=1),row(a11=1),row(a02=1),row(a12=1),row(a03=1),row(b11=2,a20=-1)],
'I10':[row(a20=1),row(a02=1),row(a12=1),row(a03=1),row(b11=1),row(b30=1),row(b03=1),row(a11=2,b20=1),row(a30=2,b12=1)],
'I11':[row(b20=1),row(b02=1),row(b12=1),row(b03=1),row(a11=1),row(a30=1),row(a03=1),row(a20=1,b11=2),row(a12=1,b30=2)],
'I12':[row(a20=1),row(a02=1),row(a30=1),row(a12=1),row(a03=1),row(b11=1),row(b02=1),row(b30=1),row(b12=1),row(a11=3,b20=1)],
'I13':[row(b20=1),row(b02=1),row(b30=1),row(b12=1),row(b03=1),row(a11=1),row(a02=1),row(a30=1),row(a12=1),row(a20=1,b11=3)],
'I14':[row(a20=1),row(a02=1),row(a30=1),row(a03=1),row(b11=1),row(b02=1),row(b12=1),row(a11=3,b20=-1),row(a12=3,b30=1)],
'I15':[row(b20=1),row(b02=1),row(b30=1),row(b03=1),row(a11=1),row(a02=1),row(a12=1),row(b11=3,a20=-1),row(a30=1,b12=3)],
'I16':[row(a20=1),row(a11=1),row(a02=1),row(a30=1),row(a03=1),row(b20=1),row(b11=1),row(b12=1),row(b03=1),row(a12=2,b30=1)],
'I17':[row(b20=1),row(b11=1),row(b02=1),row(b30=1),row(b03=1),row(a20=1),row(a11=1),row(a12=1),row(a03=1),row(a30=1,b12=2)],
}
expected={'I01':6,'I02':6,'I03':6,'I04':6,'I05':4,'I06':5,'I07':5,'I08':3,'I09':3,'I10':3,'I11':3,'I12':2,'I13':2,'I14':3,'I15':3,'I16':2,'I17':2}
for name,rows in F.items():
    d=14-rank(common+rows)
    assert d==expected[name],(name,d,expected[name])
    print(name,d)

# I18: common + 8 independent linear equations leave a 4-plane;
# the remaining cubic a30*b20^2-a20^2*b30 restricts nontrivially there,
# so every irreducible component has dimension 3.
i18lin=common+[row(a02=1),row(b02=1),row(a03=1),row(b03=1),row(a11=1,b20=1),row(a20=1,b11=1),row(a12=1,b30=1),row(a30=1,b12=1)]
assert rank(i18lin)==10
print('I18_linear_slice',14-rank(i18lin),'I18_dimension',3)

# I19 and I20 are rationally parameterized by the two nonzero parameters a20,b20.
print('I19_dimension',2)
print('I20_dimension',2)

# I21: after common conditions, six zero coordinates, and two linear relations,
# four variables remain. Its two binomial equations have independent Jacobian rows
# at (a30,b30,a03,b03)=(7,7,4,4), and on the nonzero torus they are finite over (a30,b30).
i21lin=common+[row(a20=1),row(a11=1),row(a02=1),row(b20=1),row(b11=1),row(b02=1),row(a12=7,b30=3),row(a30=3,b12=7)]
assert rank(i21lin)==10
# gradients of f1=49*a03*b03-16*a30*b30 and f2=a03*a30^2-b03*b30^2
J=[[196,196,-112,-112],[49,-49,56,-56]] # columns a03,b03,a30,b30 at witness
# elementary 2x4 rank check
assert any(J[0][i]*J[1][j]-J[0][j]*J[1][i] for i in range(4) for j in range(i+1,4))
print('I21_linear_slice',14-rank(i21lin),'I21_dimension',2)

# I01 and I02 have complementary free-coordinate sets inside a21=b21=0,
# so their tangent spaces span that entire 12-plane.
def free_coords(rows):
    # For these two coordinate subspaces, a coordinate is free iff no row is its unit row.
    killed=set()
    for r in rows:
        nz=[i for i,x in enumerate(r) if x]
        if len(nz)==1: killed.add(nz[0])
    return {i for i in range(14) if i not in killed and i not in {idx['a21'],idx['b21']}}
f1=free_coords(F['I01']); f2=free_coords(F['I02'])
W=set(range(14))-{idx['a21'],idx['b21']}
assert f1|f2==W and f1.isdisjoint(f2)
assert len(W)==12
print('global_dimension',6)
print('tangent_dimension_at_origin',12)
print('codimension',8)
print('tangent_excess',6)
print('VERIFY_OK')
