#!/usr/bin/env python3
from itertools import product


def coeff_conditions(p, A, F):
    B={k:(1-v)%p for k,v in F.items()}
    for i,j,k in product((0,1), repeat=3):
        if B[i,j]*(A[i,k]-A[j,k]) % p:
            return False
        if (B[i,k]*(1-A[i,j])-B[i,j]*B[j,k]) % p:
            return False
    return True


def op_factory(p,A,F):
    def op(a,b):
        i,x=a; j,y=b
        return (i,(A[i,j]*x+(1-F[i,j])*y)%p)
    return op


def direct_quandle_check(p,A,F):
    X=[(i,x) for i in (0,1) for x in range(p)]
    op=op_factory(p,A,F)
    for x in X:
        assert op(x,x)==x
    for y in X:
        images=[op(x,y) for x in X]
        assert len(set(images))==len(X)
    for x,y,z in product(X, repeat=3):
        assert op(op(x,y),z)==op(op(x,z),op(y,z))


def enumerate_unit_solutions(p):
    lam=2%p
    sols=[]
    for a,b,f,g in product(range(1,p), repeat=4):
        A={(0,0):lam,(1,1):lam,(0,1):a,(1,0):b}
        F={(0,0):lam,(1,1):lam,(0,1):f,(1,0):g}
        if coeff_conditions(p,A,F):
            sols.append((a,b,f,g))
    predicted={(1,1,1,1)}
    for r in range(1,p):
        if r==1: continue
        predicted.add((2%p,2%p,(1-r)%p,(1-pow(r,-1,p))%p))
    assert set(sols)==predicted
    return sols

for p in (5,7,11):
    sols=enumerate_unit_solutions(p)
    assert len(sols)==p-1
    for r in range(1,p):
        if r==1: continue
        A={(0,0):2%p,(1,1):2%p,(0,1):2%p,(1,0):2%p}
        F={(0,0):2%p,(1,1):2%p,(0,1):(1-r)%p,(1,0):(1-pow(r,-1,p))%p}
        assert all(v%p for v in A.values())
        assert all(v%p for v in F.values())
        direct_quandle_check(p,A,F)

p=5
sols=enumerate_unit_solutions(p)
assert set(sols)=={(1,1,1,1),(2,2,2,2),(2,2,3,4),(2,2,4,3)}
print('VERIFY_OK primes=5,7,11 unit_solution_count=p-1 p5_solutions=4 p5_extra=2 family_missing_choices=p-3')
