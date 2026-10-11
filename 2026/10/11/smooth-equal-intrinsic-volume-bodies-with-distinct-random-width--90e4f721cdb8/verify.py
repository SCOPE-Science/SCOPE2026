from fractions import Fraction as F
from math import factorial

# Polynomial dictionary in x,y,z: exponent triple -> rational coefficient.
def add(A,B):
    C=dict(A)
    for m,c in B.items(): C[m]=C.get(m,F(0))+c
    return {m:c for m,c in C.items() if c}

def scale(A,c): return {m:c*v for m,v in A.items() if c*v}
def mul(A,B):
    C={}
    for (a,b,c),u in A.items():
        for (d,e,f),v in B.items():
            m=(a+d,b+e,c+f)
            C[m]=C.get(m,F(0))+u*v
    return {m:c for m,c in C.items() if c}

def powp(A,n):
    R={(0,0,0):F(1)}
    for _ in range(n): R=mul(R,A)
    return R

def d2(A,idx):
    C={}
    for m,v in A.items():
        k=m[idx]
        if k>=2:
            mm=list(m); mm[idx]-=2
            C[tuple(mm)]=C.get(tuple(mm),F(0))+v*k*(k-1)
    return C

def lap(A): return add(add(d2(A,0),d2(A,1)),d2(A,2))

def odd_df(n):
    if n<=0: return 1
    r=1
    for k in range(1,n+1,2): r*=k
    return r

def sphere_moment(A):
    # Uniform probability on S^2.
    s=F(0)
    for (a,b,c),v in A.items():
        if a%2 or b%2 or c%2: continue
        aa,bb,cc=a//2,b//2,c//2
        s += v*F(odd_df(2*aa-1)*odd_df(2*bb-1)*odd_df(2*cc-1), odd_df(2*(aa+bb+cc)+1))
    return s

U={(0,4,0):F(1),(0,2,2):F(-6),(0,0,4):F(1)}
W={(4,0,0):F(1),(2,0,2):F(-6),(0,0,4):F(1)}
H=add(U,scale(W,F(-1)))
assert lap(U)=={}
assert lap(W)=={}
assert sphere_moment(U)==0 and sphere_moment(H)==0
m2f=sphere_moment(powp(U,2))
m3f=sphere_moment(powp(U,3))
m4f=sphere_moment(powp(U,4))
# g=(2*sqrt(7)/7) H, hence g^2=(4/7)H^2 and g^4=(16/49)H^4.
m2g=F(4,7)*sphere_moment(powp(H,2))
m3g=F(0)  # swap x and y sends H to -H, so every odd sphere moment is zero.
m4g=F(16,49)*sphere_moment(powp(H,4))
assert m2f==m2g==F(64,315)
assert m3f==m3g==0
assert m4f==F(4096,36465)
assert m4g==F(241664,2501499)
assert m4f-m4g==F(65536,4169165)>0
# Since integral q^2 d sigma = 4*pi*m2, the exact coefficient 9*integral q^2 is (256*pi/35).
assert 36*m2f == F(256,35)
print('VERIFY_OK')
print('m2=',m2f,'m4f=',m4f,'m4g=',m4g,'difference=',m4f-m4g)
