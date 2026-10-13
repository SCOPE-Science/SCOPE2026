#!/usr/bin/env python3
"""Finite-field sanity checks for the sharp condition-(Q) witness theorem.

The proof in RESULT.md is field-uniform.  This script is only a finite replay:
it exhausts all matrices for q=3,5 and checks one canonical representative of
every nonscalar similarity type, plus every scalar, for q=7,11.
"""
from itertools import product


def det(M,q):
    a,b,c,d=M
    return (a*d-b*c)%q

def tr(M,q):
    return (M[0]+M[3])%q

def sub(A,B,q):
    return tuple((x-y)%q for x,y in zip(A,B))

def inv(U,q):
    a,b,c,d=U
    z=det(U,q)
    zi=pow(z,-1,q)
    return (d*zi%q, -b*zi%q, -c*zi%q, a*zi%q)

def disc(A,q):
    t=tr(A,q); d=det(A,q)
    return (t*t-4*d)%q

def nonsquare(x,q):
    return x%q != 0 and pow(x%q,(q-1)//2,q)==q-1

def witness_count(A,q,units=None):
    if units is None:
        mats=list(product(range(q),repeat=4))
        units=[U for U in mats if det(U,q)]
    n=0
    for U in units:
        if det(sub(A,U,q),q) and det(sub(A,inv(U,q),q),q):
            n+=1
    return n

def target(q):
    return q**4-3*q**3+5*q-1

def is_equality_type(A,q):
    d=det(A,q); t=tr(A,q)
    scalar=(A[1]%q==0 and A[2]%q==0 and A[0]%q==A[3]%q)
    return d!=0 and t!=0 and not scalar and nonsquare(disc(A,q),q)

def exhaustive(q):
    mats=list(product(range(q),repeat=4))
    units=[U for U in mats if det(U,q)]
    vals=[]
    for A in mats:
        w=witness_count(A,q,units)
        vals.append(w)
        assert (w==target(q)) == is_equality_type(A,q), (q,A,w,disc(A,q))
    m=min(vals)
    assert m==target(q),(q,m,target(q))
    return len(mats),len(units),sum(v==m for v in vals)

def class_reps(q):
    mats=list(product(range(q),repeat=4))
    units=[U for U in mats if det(U,q)]
    reps=[]
    # Companion matrix [[0,-d],[1,t]] represents every nonscalar similarity type.
    for t in range(q):
        for d in range(q):
            reps.append((0,(-d)%q,1,t))
    # Add every scalar type.
    for lam in range(q):
        reps.append((lam,0,0,lam))
    eq=0
    for A in reps:
        w=witness_count(A,q,units)
        if w==target(q):
            eq+=1
        assert w>=target(q),(q,A,w,target(q))
        assert (w==target(q)) == is_equality_type(A,q),(q,A,w,disc(A,q))
    return len(reps),len(units),eq

def rank_one_formula_checks(q):
    mats=list(product(range(q),repeat=4))
    units=[U for U in mats if det(U,q)]
    # nilpotent rank-one representative
    A=(0,1,0,0)
    w=witness_count(A,q,units)
    expected=q**4-3*q**3+2*q**2+q
    assert w==expected,(q,'nilpotent-rank1',w,expected)
    # semisimple rank-one representatives diag(s,0)
    base=q**4-3*q**3+q**2+q
    for s in range(1,q):
        A=(s,0,0,0)
        I=(q-1)*(2*q-1) if (s*s)%q==1 else (q-1)**2
        expected=base+I
        w=witness_count(A,q,units)
        assert w==expected,(q,s,w,expected)


def expected_invertible_nonscalar(A,q):
    t=tr(A,q); d=det(A,q); D=(t*t-4*d)%q
    assert d!=0
    base=q**4-3*q**3-q**2+5*q
    if t==0:
        I=q**3-2*q if d==q-1 else q**2+q
    elif D==0:
        I=2*q**2-3*q if d==1 else q**2
    else:
        sq=pow(D,(q-1)//2,q)==1
        if not sq:
            I=q**2-1
        else:
            K=(t*t-(d+1)*(d+1))%q
            I=(q-1)*(2*q-1) if K==0 else q**2+1
    return base+I

def case_formula_checks(q):
    mats=list(product(range(q),repeat=4))
    units=[U for U in mats if det(U,q)]
    for t in range(q):
        for d in range(1,q):
            A=(0,(-d)%q,1,t)
            w=witness_count(A,q,units)
            e=expected_invertible_nonscalar(A,q)
            assert w==e,(q,t,d,w,e,disc(A,q))

def main():
    report=[]
    for q in (3,5):
        report.append((q,'all',*exhaustive(q)))
        rank_one_formula_checks(q)
        case_formula_checks(q)
    for q in (7,11):
        report.append((q,'classes',*class_reps(q)))
        rank_one_formula_checks(q)
        case_formula_checks(q)
    print('VERIFY_OK')
    for row in report:
        print(row)

if __name__=='__main__':
    main()
