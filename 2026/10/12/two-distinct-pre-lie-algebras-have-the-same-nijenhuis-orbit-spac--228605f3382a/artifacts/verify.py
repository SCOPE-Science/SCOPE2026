from itertools import product
from collections import Counter

def mul_A2(x,y,p):
    a,b=x; c,d=y
    return ((a*c)%p,(a*d+b*c)%p)

def mul_A3(x,y,p):
    a,b=x; c,d=y
    return ((a*c)%p,0)

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

def nijenhuis(M,mul,p):
    e=((1,0),(0,1))
    for x in e:
        for y in e:
            Nx=mat_vec(M,x,p); Ny=mat_vec(M,y,p)
            lhs=mul(Nx,Ny,p)
            xy=mul(x,y,p)
            inside=tuple((u+v-w)%p for u,v,w in
                         zip(mul(Nx,y,p),mul(x,Ny,p),mat_vec(M,xy,p)))
            if lhs!=mat_vec(M,inside,p):
                return False
    return True

def automorphism(P,mul,p):
    if det(P,p)==0:
        return False
    e=((1,0),(0,1))
    for x in e:
        for y in e:
            if mat_vec(P,mul(x,y,p),p)!=mul(mat_vec(P,x,p),mat_vec(P,y,p),p):
                return False
    return True

def conjugate(P,M,p):
    return mat_mul(mat_mul(P,M,p),inv(P,p),p)

for p in (2,3,5,7):
    mats=[((a,c),(b,d)) for a,b,c,d in product(range(p),repeat=4)]
    for name,mul in (("A2",mul_A2),("A3",mul_A3)):
        nij=[M for M in mats if nijenhuis(M,mul,p)]
        predicted=[M for M in mats
                   if M[0][1]==0
                   and M[1][0]*(M[0][0]-M[1][1])%p==0]
        assert set(nij)==set(predicted)

        aut=[P for P in mats if automorphism(P,mul,p)]
        expected_aut=[((1,0),(0,s)) for s in range(1,p)]
        assert set(aut)==set(expected_aut)

        rem=set(nij); orbits=[]
        while rem:
            M=next(iter(rem))
            orb={conjugate(P,M,p) for P in aut}
            orbits.append(orb)
            rem-=orb

        reps={((a,0),(0,d)) for a,d in product(range(p),repeat=2)}
        reps|={((a,0),(1,a)) for a in range(p)}
        assert len(nij)==2*p*p-p
        assert len(orbits)==p*p+p
        assert len(reps)==p*p+p
        assert all(len(orb & reps)==1 for orb in orbits)

        zero=((0,0),(0,0))
        square_zero=[M for M in nij if mat_mul(M,M,p)==zero]
        idempotent=[M for M in nij if mat_mul(M,M,p)==M]
        assert len(square_zero)==p
        assert len(idempotent)==4

        print({
            "q":p,
            "algebra":name,
            "operators":len(nij),
            "orbits":len(orbits),
            "orbit_sizes":dict(sorted(Counter(map(len,orbits)).items())),
            "square_zero":len(square_zero),
            "idempotents":len(idempotent),
        })

print("VERIFY_OK")
