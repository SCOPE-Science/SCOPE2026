from itertools import product
from fractions import Fraction

# basis vectors in dimension four
B=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]

def det3(x,y,z,mod=None):
    v=(x[0]*(y[1]*z[2]-y[2]*z[1])
       -x[1]*(y[0]*z[2]-y[2]*z[0])
       +x[2]*(y[0]*z[1]-y[1]*z[0]))
    return v if mod is None else v%mod

def br(x,y,z,mod=None):
    v=det3(x,y,z,mod)
    return (0,0,0,v)

def mv(M,x,mod=None):
    y=tuple(sum(M[4*i+j]*x[j] for j in range(4)) for i in range(4))
    return y if mod is None else tuple(v%mod for v in y)

def add(x,y,mod=None):
    z=tuple(x[i]+y[i] for i in range(4))
    return z if mod is None else tuple(v%mod for v in z)

def is_net(M,mod=None):
    for x,y,z in product(B,repeat=3):
        Tx,Ty,Tz=mv(M,x,mod),mv(M,y,mod),mv(M,z,mod)
        lhs=br(Tx,Ty,Tz,mod)
        rhs=mv(M,add(br(Tx,Ty,z,mod),br(x,y,z,mod),mod),mod)
        if lhs!=rhs:
            return False
    return True

def det3_matrix(A,q):
    return (A[0]*(A[4]*A[8]-A[5]*A[7])
            -A[1]*(A[3]*A[8]-A[5]*A[6])
            +A[2]*(A[3]*A[7]-A[4]*A[6]))%q

def rank(M,q,n=4):
    A=[list(M[n*i:n*i+n]) for i in range(n)]
    r=0
    for c in range(n):
        p=next((i for i in range(r,n) if A[i][c]%q),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        inv=pow(A[r][c],-1,q)
        A[r]=[(inv*v)%q for v in A[r]]
        for i in range(n):
            if i!=r and A[i][c]%q:
                k=A[i][c]%q
                A[i]=[(A[i][j]-k*A[r][j])%q for j in range(n)]
        r+=1
    return r

def criterion(M,q):
    # u = first three entries of final column
    if any(M[4*i+3]%q for i in range(3)):
        return False
    A=(M[0],M[1],M[2], M[4],M[5],M[6], M[8],M[9],M[10])
    t=M[15]%q
    if t==0:
        return det3_matrix(A,q)==0
    # nonzero branch: A=lambda I and t(lambda^2+1)=lambda^3
    lam=A[0]%q
    if lam==0: return False
    if A!=(lam,0,0,0,lam,0,0,0,lam):
        return False
    return (t*(lam*lam+1)-lam**3)%q==0

# Exhaustive direct test over F2.
q=2
profile=[0]*5
count=0
for M in product(range(q),repeat=16):
    d=is_net(M,q)
    c=criterion(M,q)
    assert d==c,(M,d,c)
    if d:
        count+=1
        profile[rank(M,q)]+=1
assert count==2752
assert tuple(profile)==(1,105,1470,1176,0)
print({'q':2,'count':count,'rank_profile':tuple(profile)})

# Closed counts for F3.
q=3
N1=(q-1)*(q*q+q+1)**2
N2=q*(q+1)*(q**3-1)**2
S=q**9-(q**3-1)*(q**3-q)*(q**3-q**2)
r=sum(1 for x in range(1,q) if (x*x+1)%q==0)
m=q-1-r
profile3=(1,q**3-1+q*N1,(q**3-q)*N1+q*q*N2,(q**3-q*q)*N2,q**3*m)
count3=q**3*(S+m)
assert count3==228231
assert profile3==(1,1040,81120,146016,54)
assert sum(profile3)==count3
print({'q':3,'count':count3,'rank_profile':profile3})

# Direct characteristic-zero checks of the arXiv-v1 diagonal family.
def Tk(k):
    return (1,0,0,0, 0,1,0,0, 0,0,2*k,0, 0,0,0,k)
assert is_net(Tk(Fraction(0)))
assert is_net(Tk(Fraction(1,2)))
assert not is_net(Tk(Fraction(1)))
print('V1_FAMILY_CHECK_OK')
print('VERIFY_OK')
