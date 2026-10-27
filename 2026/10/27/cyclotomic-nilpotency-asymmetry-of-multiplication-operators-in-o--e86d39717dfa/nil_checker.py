#!/usr/bin/env python3
"""Exact independent operator-power checks of nilpotent multiplication maps.
Requires only verify.py in the same directory (standard library otherwise).
"""
from itertools import product
from collections import Counter
from verify import Field, factor, divmodpoly, trim

def mm(A,B,F):
    n=len(A);C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:C[i][j]=F.add[C[i][j]][F.mul[A[i][k]][B[k][j]]]
    return C

def op(a,n,F,left):
    M=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if left:
                M[(2*j-i)%n][j]=F.add[M[(2*j-i)%n][j]][a[i]]
            else:
                M[(2*j-i)%n][i]=F.add[M[(2*j-i)%n][i]][a[j]]
    return M

def is_nilpotent(M,F):
    n=len(M);P=[[int(i==j) for j in range(n)] for i in range(n)]
    for k in range(1,n+1):
        P=mm(P,M,F)
        if not any(any(row) for row in P):return True
    return False

def mod_f_subst_zero(g,u,f,F):
    h=[0]*((len(g)-1)*u+1)
    for j,c in enumerate(g):h[j*u]=c
    return divmodpoly(h,f,F)[1]==[0]

def cycles_for(n,F,u):
    p=F.p;h=n
    while h%p==0:h//=p
    e=n//h
    xn=[F.neg(1)]+[0]*(h-1)+[1]
    factors=factor(xn,F)
    assert all(ex==1 for f,ex in factors)
    fs=[f for f,ex in factors]
    perm=[]
    for f in fs:
        z=[i for i,g in enumerate(fs) if mod_f_subst_zero(g,u,f,F)]
        assert len(z)==1,(n,F.q,u,z)
        perm.append(z[0])
    seen=set();cc=[]
    for i in range(len(fs)):
        if i in seen:continue
        a=[];j=i
        while j not in seen:
            seen.add(j);a.append(j);j=perm[j]
        assert j==i
        assert all(len(fs[t])==len(fs[i]) for t in a)
        cc.append((len(a),len(fs[i])-1))
    return cc,h

def predict(n,F,u):
    cc,h=cycles_for(n,F,u)
    ans=F.q**(n-h)
    for ell,d in cc:
        ans*=F.q**(d*ell)-(F.q**d-1)**ell
    return ans,cc

def check(n,F,exhaustive=True):
    pl,cl=predict(n,F,2);pr,cr=predict(n,F,n-1)
    vals=product(range(F.q),repeat=n)
    if exhaustive:
        counts=[0,0];ne=0
        for a in vals:
            ne+=1
            if is_nilpotent(op(a,n,F,True),F):counts[0]+=1
            if is_nilpotent(op(a,n,F,False),F):counts[1]+=1
        assert counts==[pl,pr],(n,F.q,counts,[pl,pr])
    else:
        ne=0
        for a in vals:
            if ne>=100:break
            # Operator power and cyclotomic orbit residue criterion are checked separately
            for left,u in [(True,2),(False,n-1)]:
                M=op(a,n,F,left)
                # Compare with exact combinatorial condition computed by polynomial reduction
                residue_zero=[]
                h=n
                while h%F.p==0:h//=F.p
                fs=[f for f,e in factor([F.neg(1)]+[0]*(h-1)+[1],F)]
                # Transformation by exponent -1 (left) or 2 (right)
                z=n-1 if left else 2
                poly=[0]*(n*z+1)
                for j,v in enumerate(a):poly[j*z]=v
                for f in fs:residue_zero.append(divmodpoly(poly,f,F)[1]==[0])
                target=all(any(residue_zero[t] for t in cyc) for cyc in orbit_indices(fs,u,F))
                assert is_nilpotent(M,F)==target,(n,F.q,a,left)
            ne+=1
    print('PASS nilpotent operators n=%d q=%d left=%d right=%d left_cycles=%s right_cycles=%s exhaustive=%s elements=%d' %
          (n,F.q,pl,pr,cl,cr,exhaustive,ne))
    return ne

def orbit_indices(fs,u,F):
    perm=[]
    for f in fs:
        z=[i for i,g in enumerate(fs) if mod_f_subst_zero(g,u,f,F)]
        assert len(z)==1
        perm.append(z[0])
    seen=set();ans=[]
    for i in range(len(fs)):
        if i not in seen:
            a=[];j=i
            while j not in seen:
                a.append(j);seen.add(j);j=perm[j]
            ans.append(a)
    return ans

if __name__=='__main__':
    cases=[(3,Field(2)),(3,Field(3)),(3,Field(5)),(3,Field(7)),
           (5,Field(2)),(5,Field(3)),(7,Field(2)),(9,Field(2)),
           (5,Field(2,[1,1,1])),(3,Field(2,[1,1,0,1])),(3,Field(3,[1,0,1]))]
    total=0
    for n,F in cases:total+=check(n,F)
    F=Field(11)
    total+=check(5,F,False)
    print('ALL_DIHEDRAL_NILPOTENT_MULTIPLIER_TESTS_PASSED cases=%d exhaustive_elements=%d'%(len(cases)+1,total-100))
