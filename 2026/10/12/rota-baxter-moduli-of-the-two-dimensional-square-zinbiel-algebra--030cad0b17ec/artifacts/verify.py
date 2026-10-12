from itertools import product
from collections import Counter

def mul(x,y,p):
    return (0, x[0]*y[0] % p)

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

def rb(M,p):
    basis=((1,0),(0,1))
    for x in basis:
        for y in basis:
            Rx=mat_vec(M,x,p); Ry=mat_vec(M,y,p)
            lhs=mul(Rx,Ry,p)
            inside=tuple((u+v)%p for u,v in zip(mul(Rx,y,p),mul(x,Ry,p)))
            if lhs!=mat_vec(M,inside,p):
                return False
    return True

def automorphism(P,p):
    if det(P,p)==0:
        return False
    basis=((1,0),(0,1))
    return all(mat_vec(P,mul(x,y,p),p)==mul(mat_vec(P,x,p),mat_vec(P,y,p),p)
               for x in basis for y in basis)

def conjugate(P,M,p):
    return mat_mul(mat_mul(P,M,p),inv(P,p),p)

for p in (2,3,5,7):
    mats=[((a,c),(b,d)) for a,b,c,d in product(range(p),repeat=4)]
    operators=[M for M in mats if rb(M,p)]
    predicted=[M for M in mats
               if M[0][1]==0 and M[0][0]*(M[0][0]-2*M[1][1])%p==0]
    assert set(operators)==set(predicted)

    aut=[P for P in mats if automorphism(P,p)]
    expected_aut=[((s,0),(t,s*s%p)) for s in range(1,p) for t in range(p)]
    assert set(aut)==set(expected_aut)

    rem=set(operators); orbits=[]
    while rem:
        M=next(iter(rem))
        orb={conjugate(P,M,p) for P in aut}
        orbits.append(orb)
        rem-=orb

    zero=((0,0),(0,0)); nil=((0,0),(1,0))
    reps={zero,nil}
    reps|={((0,0),(0,d)) for d in range(1,p)}
    if p!=2:
        reps|={((2*d%p,0),(0,d)) for d in range(1,p)}

    assert all(len(orb & reps)==1 for orb in orbits)

    got=Counter(map(len,orbits))
    expected=Counter()
    expected[1]+=1
    expected[p-1]+=1
    expected[p]+=(p-1 if p==2 else 2*(p-1))
    assert got==expected, (p,got,expected)

    if p==2:
        assert len(operators)==p*p and len(orbits)==p+1
    else:
        assert len(operators)==2*p*p-p and len(orbits)==2*p

    print({"q":p,"operators":len(operators),"orbits":len(orbits),
           "orbit_sizes":dict(sorted(got.items()))})

print("VERIFY_OK")
