from itertools import product
from collections import Counter

def det3_cols(x,y,z,q):
    return (
        x[0]*(y[1]*z[2]-y[2]*z[1])
        -x[1]*(y[0]*z[2]-y[2]*z[0])
        +x[2]*(y[0]*z[1]-y[1]*z[0])
    ) % q

def bracket(x,y,z,q):
    return (det3_cols(x,y,z,q),0,0)

def mv(M,x,q):
    return tuple(sum(M[3*i+j]*x[j] for j in range(3)) % q for i in range(3))

def add(*vs,q):
    return tuple(sum(v[i] for v in vs)%q for i in range(3))

def fundamental_identity(q):
    bas=((1,0,0),(0,1,0),(0,0,1))
    for x1,x2,x3,x4,x5 in product(bas,repeat=5):
        lhs=bracket(x1,x2,bracket(x3,x4,x5,q),q)
        r1=bracket(bracket(x1,x2,x3,q),x4,x5,q)
        r2=bracket(x3,bracket(x1,x2,x4,q),x5,q)
        r3=bracket(x3,x4,bracket(x1,x2,x5,q),q)
        if lhs!=add(r1,r2,r3,q=q):
            return False
    return True

def is_embedding(M,q):
    bas=((1,0,0),(0,1,0),(0,0,1))
    for x,y,z in product(bas,repeat=3):
        Tx,Ty,Tz=mv(M,x,q),mv(M,y,q),mv(M,z,q)
        lhs=bracket(Tx,Ty,Tz,q)
        rhs=mv(M,bracket(Tx,Ty,z,q),q)
        if lhs!=rhs:
            return False
    return True

def rank3(M,q):
    A=[list(M[3*i:3*i+3]) for i in range(3)]
    r=0
    for c in range(3):
        p=next((i for i in range(r,3) if A[i][c]%q),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        inv=pow(A[r][c],-1,q)
        A[r]=[(inv*v)%q for v in A[r]]
        for i in range(3):
            if i!=r and A[i][c]%q:
                k=A[i][c]%q
                A[i]=[(A[i][j]-k*A[r][j])%q for j in range(3)]
        r+=1
    return r

def scalar_nonzero(M,q):
    if M[1]%q or M[2]%q or M[3]%q or M[5]%q or M[6]%q or M[7]%q:
        return False
    return M[0]%q!=0 and M[0]%q==M[4]%q==M[8]%q

def criterion(M,q):
    r=rank3(M,q)
    if r<=1:
        return True
    if r==2:
        return M[0]%q==0 and M[3]%q==0 and M[6]%q==0
    return scalar_nonzero(M,q)

def formulas(q):
    profile=(
        1,
        (q-1)*(q*q+q+1)**2,
        (q**3-1)*(q**3-q),
        q-1,
    )
    total=q**6+q**5-q**2+q-1
    assert sum(profile)==total
    return profile,total

for q in (2,3):
    assert fundamental_identity(q)
    cnt=Counter()
    total=0
    for M in product(range(q),repeat=9):
        direct=is_embedding(M,q)
        classified=criterion(M,q)
        assert direct==classified,(q,M,direct,classified)
        if direct:
            cnt[rank3(M,q)]+=1
            total+=1
    expected_profile,expected_total=formulas(q)
    got=tuple(cnt[i] for i in range(4))
    assert got==expected_profile,(q,got,expected_profile)
    assert total==expected_total
    print({"q":q,"total":total,"rank_profile":got})

for q in (2,3,5,7):
    profile,total=formulas(q)
    print({"q":q,"formula_total":total,"formula_rank_profile":profile})

print("VERIFY_OK")
