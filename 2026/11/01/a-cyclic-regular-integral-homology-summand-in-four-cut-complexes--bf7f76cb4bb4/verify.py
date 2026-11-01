#!/usr/bin/env python3
"""Finite exact checks for four-cut complexes of third powers of cycles.

Only Python's standard library is required. Infinite-parameter assertions
are proved by the separate combinatorial case analysis in RESULT.md.
"""
from itertools import combinations, product

W12 = {
    (0,3,4,7), (1,3,5,10), (1,3,6,10), (1,3,7,10),
    (1,3,8,10), (1,6,9,10), (3,4,7,9), (3,4,7,10),
    (4,5,7,9), (4,6,7,9), (4,6,9,10), (4,7,8,9),
}
W13 = {(0,3,4,7),(3,4,7,10)}
COEF12 = [-1,-1,-1,-1,-1,1,1,1,-1,-1,1,1]
COEF13 = [1,-1]
T = (0,2,4,7)

def connected(U,n):
    U=tuple(U)
    visited={U[0]}
    while True:
        new=visited | {v for u in visited for v in U
                       if min(abs(u-v), n-abs(u-v))<=3}
        if len(new)==len(visited):return len(new)==len(U)
        visited=new

def quads_and_fives(n):
    Q={q for q in combinations(range(n),4) if connected(q,n)}
    F=[f for f in combinations(range(n),5)
       if all(f[:i]+f[i+1:] in Q for i in range(5))]
    return Q,F

def boundary_rank(columns):
    basis={}
    for col in columns:
        while col:
            p=col.bit_length()-1
            if p not in basis:
                basis[p]=col;break
            col ^=basis[p]
    return len(basis)

def sign_boundary(ordered_simplices):
    out={}
    for simplex, coeff in ordered_simplices:
        for i in range(len(simplex)):
            face=simplex[:i]+simplex[i+1:]
            out[face]=out.get(face,0)+coeff*((-1)**i)
    return {key:value for key,value in out.items() if value}

def cross_polytope_chain():
    out=[]
    for bits in product((0,1),repeat=4):
        tet=tuple(2*i+bits[i] for i in range(4))
        out.append((tet,(-1)**sum(bits)))
    assert len(out)==16 and not sign_boundary(out)
    return out

def check_small(n,w,coefficients,expected_beta):
    Q,F=quads_and_fives(n)
    z=cross_polytope_chain()
    assert {q for q,c in z}.issubset(Q)
    assert w.issubset(Q)
    omega = dict(zip(sorted(w),coefficients))
    assert len(omega)==len(w)
    # Exact signed integral cocycle condition, not just mod-two.
    assert all(sum(((-1)**i)*omega.get(f[:i]+f[i+1:],0)
                   for i in range(5))==0 for f in F)
    integral_pairing=sum(c*omega.get(q,0) for q,c in z)
    assert abs(integral_pairing)==1
    # All 5-simplices have zero mod-2 coboundary.
    assert all(sum(tuple(sorted(f[:i]+f[i+1:])) in w
                   for i in range(5))%2==0 for f in F)
    pairing=sum(q in w for q,c in z)%2
    assert pairing==1
    triples=list(combinations(range(n),3)); tind={t:i for i,t in enumerate(triples)}
    sortedQ=sorted(Q); qind={q:i for i,q in enumerate(sortedQ)}
    b3=[sum(1<<tind[q[:i]+q[i+1:]] for i in range(4)) for q in sortedQ]
    b4=[sum(1<<qind[f[:i]+f[i+1:]] for i in range(5)) for f in F]
    r3=boundary_rank(b3);r4=boundary_rank(b4)
    assert all(not (col.bit_count()%2) for col in b3)
    for f in F:
        # Boundary squared vanishes over F2.
        counts={}
        for i in range(5):
            q=f[:i]+f[i+1:]
            for j in range(4):
                t=q[:j]+q[j+1:]
                counts[t]=counts.get(t,0)^1
        assert not any(counts.values())
    beta=len(Q)-r3-r4
    assert beta==expected_beta
    print('VERIFY_OK n={} valid_4faces={} valid_5faces={} ranks=({}, {}) beta3_F2={} integral_cocycle_size={} integral_pairing={}'.format(n,len(Q),len(F),r3,r4,beta,len(w),integral_pairing))

def translated_chain(oriented, shift, n):
    out={}
    for simplex,coef in oriented:
        moved=[(x+shift)%n for x in simplex]
        inversions=sum(moved[i]>moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))
        key=tuple(sorted(moved))
        out[key]=out.get(key,0)+coef*((-1)**inversions)
    return out

def check_regular_pairings(n):
    z=cross_polytope_chain()
    base = dict(zip(sorted(W13),COEF13)) if n==13 else {T:-1}
    Z=[translated_chain(z,i,n) for i in range(n)]
    W=[translated_chain(base.items(),i,n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            actual=sum(c*Z[j].get(q,0) for q,c in W[i].items())
            assert actual == int(i==j),(n,i,j,actual)
    print('VERIFY_OK n={} cyclic_regular_pairing=identity_{}x{}'.format(n,n,n))

def check_unbounded_case_finite_examples():
    z=cross_polytope_chain()
    for n in range(14,29):
        Q,F=quads_and_fives(n)
        assert {q for q,c in z}.issubset(Q)
        assert T in Q
        assert not any(set(T).issubset(f) for f in F)
    print('VERIFY_OK n=14..28 cross-polytope_3cycle_and_unextendable_tetrahedron')

if __name__=='__main__':
    check_small(12,W12,COEF12,2)
    check_small(13,W13,COEF13,14)
    for n in range(13,29):check_regular_pairings(n)
    check_unbounded_case_finite_examples()
    print('ALL_VERIFY_OK; unbounded assertion follows from the proved case analysis')
