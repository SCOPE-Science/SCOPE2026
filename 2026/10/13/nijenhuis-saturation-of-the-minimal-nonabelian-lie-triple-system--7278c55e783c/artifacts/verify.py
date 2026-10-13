import sympy as sp
from itertools import product
from collections import Counter

a,b,c,d=sp.symbols("a b c d")
N=sp.Matrix([[a,b],[c,d]])
x1,x2,y1,y2,z1,z2=sp.symbols("x1 x2 y1 y2 z1 z2")
x=sp.Matrix([x1,x2]); y=sp.Matrix([y1,y2]); z=sp.Matrix([z1,z2])

def br(x,y,z):
    return sp.Matrix([sp.expand((x[0]*y[1]-x[1]*y[0])*z[1]),0])

def defect(x,y,z):
    Nx,Ny,Nz=N*x,N*y,N*z
    return sp.simplify(
        br(Nx,Ny,Nz)
        -N*(br(x,Ny,Nz)+br(Nx,y,Nz)+br(Nx,Ny,z))
        +(N**2)*(br(Nx,y,z)+br(x,Ny,z)+br(x,y,Nz))
        -(N**3)*br(x,y,z)
    )

D=defect(x,y,z)
assert all(sp.simplify(w)==0 for w in D)

def nibr(x,y,z):
    Nx,Ny,Nz=N*x,N*y,N*z
    return sp.simplify(
        br(x,Ny,Nz)+br(Nx,y,Nz)+br(Nx,Ny,z)
        -N*(br(Nx,y,z)+br(x,Ny,z)+br(x,y,Nz))
        +(N**2)*br(x,y,z)
    )

B=nibr(x,y,z)
target=sp.Matrix([
    (x1*y2-x2*y1)*(c*z1+d*z2)*d,
    -(x1*y2-x2*y1)*(c*z1+d*z2)*c
])
assert sp.simplify(B-target)==sp.zeros(2,1)

def mv(M,v,q):
    return ((M[0]*v[0]+M[1]*v[1])%q,(M[2]*v[0]+M[3]*v[1])%q)

def bq(x,y,z,q):
    return (((x[0]*y[1]-x[1]*y[0])*z[1])%q,0)

def is_nij(M,q):
    bas=((1,0),(0,1))
    def matmul(A,B):
        return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%q for i in range(2) for j in range(2))
    M2=matmul(M,M); M3=matmul(M2,M)
    for x,y,z in product(bas,repeat=3):
        Nx,Ny,Nz=mv(M,x,q),mv(M,y,q),mv(M,z,q)
        lhs=bq(Nx,Ny,Nz,q)
        S2=[bq(x,Ny,Nz,q),bq(Nx,y,Nz,q),bq(Nx,Ny,z,q)]
        S1=[bq(Nx,y,z,q),bq(x,Ny,z,q),bq(x,y,Nz,q)]
        s2=tuple(sum(v[i] for v in S2)%q for i in range(2))
        s1=tuple(sum(v[i] for v in S1)%q for i in range(2))
        rhs=tuple((mv(M,s2,q)[i]-mv(M2,s1,q)[i]+mv(M3,bq(x,y,z,q),q)[i])%q for i in range(2))
        if lhs!=rhs: return False
    return True

def rank2(M,q):
    if all(v%q==0 for v in M): return 0
    return 2 if (M[0]*M[3]-M[1]*M[2])%q else 1

for q in (3,5,7,11):
    mats=list(product(range(q),repeat=4))
    assert all(is_nij(M,q) for M in mats)
    zero=[M for M in mats if M[2]%q==0 and M[3]%q==0]
    assert len(zero)==q**2
    ranks=Counter(rank2(M,q) for M in mats)
    expected=(1,(q-1)*(q+1)**2,q*(q-1)**2*(q+1))
    assert tuple(ranks[i] for i in range(3))==expected

    # Every nonzero second row admits v with c*v1+d*v2=1.
    for M in mats:
        cc,dd=M[2],M[3]
        if cc==0 and dd==0: continue
        found=False
        for v1,v2 in product(range(q),repeat=2):
            if (cc*v1+dd*v2)%q==1:
                w=(dd%q,(-cc)%q)
                det=(w[0]*v2-w[1]*v1)%q
                assert det==1
                # induced [w,v,v] equals w
                ell=(cc*v1+dd*v2)%q
                out=(det*ell*dd%q, det*ell*(-cc)%q)
                assert out==w
                found=True
                break
        assert found
    print({"q":q,"nijenhuis":len(mats),"zero_induced":len(zero),"rank_profile":expected})

print("VERIFY_OK")
