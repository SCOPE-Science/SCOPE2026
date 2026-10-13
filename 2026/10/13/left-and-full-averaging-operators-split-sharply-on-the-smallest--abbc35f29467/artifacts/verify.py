from itertools import product
from collections import Counter

def bracket(x,y,p):
    return (0, x[0]*y[1] % p)

def mat_vec(M,x,p):
    return ((M[0][0]*x[0]+M[0][1]*x[1])%p,
            (M[1][0]*x[0]+M[1][1]*x[1])%p)

def mat_mul(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p
                       for j in range(2)) for i in range(2))

def det(M,p):
    return (M[0][0]*M[1][1]-M[0][1]*M[1][0])%p

def inv(M,p):
    z=pow(det(M,p),-1,p)
    return ((M[1][1]*z%p,-M[0][1]*z%p),
            (-M[1][0]*z%p,M[0][0]*z%p))

def left_avg(M,p):
    E=((1,0),(0,1))
    for x in E:
        for y in E:
            Px=mat_vec(M,x,p); Py=mat_vec(M,y,p)
            lhs=bracket(Px,Py,p)
            rhs=mat_vec(M,bracket(Px,y,p),p)
            if lhs!=rhs: return False
    return True

def full_avg(M,p):
    if not left_avg(M,p): return False
    E=((1,0),(0,1))
    for x in E:
        for y in E:
            Px=mat_vec(M,x,p); Py=mat_vec(M,y,p)
            lhs=bracket(Px,Py,p)
            rhs=mat_vec(M,bracket(x,Py,p),p)
            if lhs!=rhs: return False
    return True

def automorphism(P,p):
    if det(P,p)==0: return False
    E=((1,0),(0,1))
    for x in E:
        for y in E:
            if mat_vec(P,bracket(x,y,p),p)!=bracket(mat_vec(P,x,p),mat_vec(P,y,p),p):
                return False
    return True

def conj(P,M,p):
    return mat_mul(mat_mul(P,M,p),inv(P,p),p)

def rank(M,p):
    if det(M,p): return 2
    if any(M[i][j]%p for i in range(2) for j in range(2)): return 1
    return 0

for p in (2,3,5,7):
    mats=[((a,c),(b,d)) for a,b,c,d in product(range(p),repeat=4)]
    L=[M for M in mats if left_avg(M,p)]
    F=[M for M in mats if full_avg(M,p)]
    predL=[M for M in mats if M[0][1]==0 and M[0][0]*M[1][0]%p==0]
    predF=[M for M in mats if M[0][1]==0 and
           M[0][0]*M[1][0]%p==0 and M[1][0]*M[1][1]%p==0 and
           M[1][1]*(M[1][1]-M[0][0])%p==0]
    assert set(L)==set(predL)
    assert set(F)==set(predF)
    assert len(L)==2*p*p-p
    assert len(F)==3*p-2

    aut=[P for P in mats if automorphism(P,p)]
    exp=[((1,0),(0,s)) for s in range(1,p)]
    assert set(aut)==set(exp)

    def orbits(S):
        rem=set(S); out=[]
        while rem:
            M=next(iter(rem))
            O={conj(P,M,p) for P in aut}
            out.append(O)
            rem-=O
        return out
    OL=orbits(L); OF=orbits(F)
    assert len(OL)==p*p+p
    assert len(OF)==2*p
    assert Counter(map(len,OF))==Counter({1:2*p-1,p-1:1}) if p>2 else Counter(map(len,OF))==Counter({1:4})

    rc=Counter(rank(M,p) for M in F)
    assert rc==Counter({0:1,1:2*p-2,2:p-1})
    zero=((0,0),(0,0))
    idem=[M for M in F if mat_mul(M,M,p)==M]
    sq0=[M for M in F if mat_mul(M,M,p)==zero]
    assert len(idem)==3
    assert len(sq0)==p

    print({"q":p,"left":len(L),"left_orbits":len(OL),
           "full":len(F),"full_orbits":len(OF),
           "full_rank_distribution":dict(sorted(rc.items())),
           "idempotents":len(idem),"square_zero":len(sq0)})

print("VERIFY_OK")
