#!/usr/bin/env python3
"""Exact finite characteristic-3 Hom-Jacobi certificate, using Python's standard library.

The seven basis classes in psl_3 are E12,E13,E21,E23,E31,E32,H,
where H=E11-E22, and H2=E22-E33 equals H in the quotient.
"""
from itertools import combinations

P=3
PAIRS=((0,1),(0,2),(1,0),(1,2),(2,0),(2,1))
ROWS=(0,1,2,3,4,5,6,8,10,15,16,17,20,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,57,58,59,60,61,62,63,64,68,71,78,106,112,178)

def elementary(a,b):
    m=[[0]*3 for _ in range(3)];m[a][b]=1;return m

def diag(d):return [[d[i] if i==j else 0 for j in range(3)] for i in range(3)]

def bracket(a,b):
    return [[sum(a[i][s]*b[s][j]-b[i][s]*a[s][j] for s in range(3))%P for j in range(3)] for i in range(3)]

def project(a,quotient):
    v=[a[i][j] for (i,j) in PAIRS]
    return v+([(a[0][0]-a[2][2])%P] if quotient else [a[0][0]%P,(-a[2][2])%P])

def coeffs(quotient):
    mats=[elementary(i,j) for i,j in PAIRS]+[diag((1,-1,0))]
    if not quotient:mats.append(diag((0,1,-1)))
    n=len(mats)
    c={}
    for i in range(n):
        for j in range(n):c[i,j]=project(bracket(mats[i],mats[j]),quotient)
    return n,c

def homjacobi(n,c):
    entries=[]
    for a,b,d in combinations(range(n),3):
        for t in range(n):
            row=[0]*(n*n)
            for i,j,k in ((a,b,d),(d,a,b),(b,d,a)):
                for r in range(n):
                    x=sum(c[i,j][s]*c[s,r][t] for s in range(n))%P
                    row[n*k+r]=(row[n*k+r]+x)%P
            entries.append(row)
    return entries

def rank(a):
    data=[x[:] for x in a];ncol=len(data[0]);nrow=len(data);r=0
    for col in range(ncol):
        k=next((i for i in range(r,nrow) if data[i][col]%P),None)
        if k is None:continue
        data[r],data[k]=data[k],data[r]
        inv=pow(data[r][col],-1,P)
        data[r]=[x*inv%P for x in data[r]]
        for i in range(r+1,nrow):
            f=data[i][col]
            if f:
                data[i]=[(u-f*v)%P for u,v in zip(data[i],data[r])]
        r+=1
        if r==nrow:break
    return r

def determinant(a):
    m=[row[:] for row in a];n=len(m);val=1
    for j in range(n):
        i=next((i for i in range(j,n) if m[i][j]%P),None)
        if i is None:return 0
        if i!=j:m[i],m[j]=m[j],m[i];val=(-val)%P
        pivot=m[j][j]%P
        val=val*pivot%P;inverse=pow(pivot,-1,P)
        for i in range(j+1,n):
            f=m[i][j]*inverse%P
            if f:
                for k in range(j,n):m[i][k]=(m[i][k]-f*m[j][k])%P
    return val

def evaluate_map(M,vec):return [sum(a*b for a,b in zip(row,vec))%P for row in M]

def check():
    n,c=coeffs(True)
    assert n==7
    m=homjacobi(n,c)
    assert len(m)==245
    id7=[int(i==j) for i in range(7) for j in range(7)]
    # Flat column index = n*input + output, so identity entries are n*i+i.
    assert all(sum(row[n*i+i] for i in range(n))%P==0 for row in m)
    fixed=[[row[j] for j in range(1,n*n)] for row in m]
    minor=[fixed[i] for i in ROWS]
    det=determinant(minor)
    assert len(ROWS)==48 and len(set(ROWS))==48 and det==1
    assert rank(fixed)==48
    print('PSL3 characteristic 3: 48x48 minor determinant =',det)
    print('PSL3 characteristic 3: rank 48, HomLie dimension 1')
    n8,c8=coeffs(False)
    m8=homjacobi(n8,c8)
    assert n8==8 and len(m8)==448
    # The single central matrix I has coordinates h1-h2=(1,-1).
    z=(0,0,0,0,0,0,1,2)
    for k in range(8):
        v=[0]*64
        for t in range(8):v[8*k+t]=z[t]
        assert not any(evaluate_map(m8,v))
    I=[int(i==j) for i in range(8) for j in range(8)]
    assert not any(evaluate_map(m8,I))
    fullrank=rank(m8)
    assert fullrank==55
    print('SL3 characteristic 3: rank 55, HomLie dimension 9')
    print('SL3: scalar identity plus 8 independent maps into its centre')
    print('VERIFY_OK')
if __name__=='__main__':check()
