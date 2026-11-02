#!/usr/bin/env python3
"""Exact characteristic-three checks for a genus-nine Artin--Schreier family.

Requires only the Python standard library. Symbolic reasoning establishing
geometric automorphism uniqueness and the global rank jump is supplied in
RESULT.md; these finite-field checks are reproducible supporting evidence.
"""
from math import comb

P = 3
MONOMIALS = [(i,j) for j in (0,1) for i in range(6 if j == 0 else 3)]
assert len(MONOMIALS) == 9
assert all(3*i + 10*j <= 16 for i,j in MONOMIALS)
assert len({3*i + 10*j for i,j in MONOMIALS}) == 9


def exp_polynomial(f, u, v):
    """Coefficients of f(ux+v), over F3."""
    ans = {}
    for degree, coeff in f.items():
        for i in range(degree+1):
            term = coeff * comb(degree,i) * pow(u,i,P) * pow(v,degree-i,P)
            ans[i] = (ans.get(i,0)+term)%P
    return ans


def f_of_a(a):
    return {10:1,8:a,7:1}


def cartier_image(monomial,a):
    i,j=monomial
    out={}
    if j==0:
        if i%3==2:
            out[(i-2)//3,0]=1
    else:
        if i%3==2:
            out[(i-2)//3,1]=1
        for power,coef in f_of_a(a).items():
            if (i+power)%3==2 and coef%3:
                key=((i+power-2)//3,0)
                out[key]=(out.get(key,0)-coef)%3
    return {k:v%3 for k,v in out.items() if v%3}


def rank_mod3(columns):
    mat=[[columns[c].get(MONOMIALS[r],0)%3 for c in range(len(columns))]
         for r in range(len(MONOMIALS))]
    rank=0
    for c in range(len(columns)):
        piv=next((r for r in range(rank,len(mat)) if mat[r][c]),None)
        if piv is None:continue
        mat[piv],mat[rank]=mat[rank],mat[piv]
        inv=pow(mat[rank][c],-1,3)
        mat[rank]=[(z*inv)%3 for z in mat[rank]]
        for r in range(len(mat)):
            if r!=rank and mat[r][c]:
                t=mat[r][c]
                mat[r]=[(z-t*w)%3 for z,w in zip(mat[r],mat[rank])]
        rank+=1
    return rank

# The general-degree comparisons used in the automorphism argument.
assert comb(8,3)%3 == 2
assert comb(7,3)%3 == 2
assert comb(10,3)%3 == 0
assert comb(10,5)%3 == 0
assert comb(10,6)%3 == 0
assert comb(7,2)%3 == 0

for a in range(P):
    f=f_of_a(a)
    cols=[cartier_image(m,a) for m in MONOMIALS]
    assert rank_mod3(cols) == (4 if a==0 else 5)
    assert cartier_image((2,0),a) == {(0,0):1}
    assert cartier_image((5,0),a) == {(1,0):1}
    assert cartier_image((0,1),a) == ({(2,0):(-a)%3} if a else {})
    assert cartier_image((1,1),a) == {(3,0):2,(2,0):2}
    assert cartier_image((2,1),a) == {(0,1):1}
    # Check the only affine x-transformations over F3 that preserve the AS cover.
    matches=[]
    for u in (1,2):
        for v in range(3):
            for eps in (1,2):
                g=exp_polynomial(f,u,v)
                d={k:(g.get(k,0)-eps*f.get(k,0))%3 for k in set(g)|set(f)}
                d={k:val for k,val in d.items() if val}
                # h^3-h has no degrees 4,5,7,8,10 when deg h <=3.
                if any(k not in {0,1,2,3,6,9} for k in d):continue
                # Solve h^3-h = d for h in F3[x] of degree <=3.
                for h0 in range(3):
                    for h1 in range(3):
                        for h2 in range(3):
                            for h3 in range(3):
                                h={0:h0,1:h1,2:h2,3:h3}
                                delta={e:(h.get(e//3,0) if e%3==0 else 0)-h.get(e,0) for e in range(10)}
                                if all((delta.get(e,0)-d.get(e,0))%3==0 for e in range(11)):
                                    matches.append((u,v,eps,h0,h1,h2,h3))
    assert sorted(matches)==[(1,0,1,c,0,0,0) for c in range(3)]
print('VERIFY_OK: genus basis, universal coefficients, Cartier rank, F3 automorphisms')
