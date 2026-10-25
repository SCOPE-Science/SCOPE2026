---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Each square-zero rank-a operator is determined by a flag U=im X subset K=ker X of dimensions a,n-a and an isomorphism V/K→U, giving Z_a=[n a]_q[n-a a]_q |GL_a(q)|. For Y use flag S⊂W and an isomorphism V/W→S. Because X,Y inject on quotients, r=rank(XY)=b−dim(S∩K) and s=rank(YX)=a−dim(U∩W). With c=dim(S∩U), d=b−r−c, e=n−2b−a+s+c, subspace intersection counts and graph-of-map lifts yield the formula in RESULT.md; no overlap of flag choices. Nonempty integer index set reduces exactly to |r−s|≤n−a−b, and for n=2h,a=b=h enforces r=s. Independently evaluated Gaussian coefficients giving F_(3,2)(1,1;r,s)=[105,84,84,168] in lexicographic (r,s), F_(4,2)(2,2;r,r)=[1260,22680,20160], and exact all-fiber normalization for 1≤n≤7 at q=2. Arbitrary-field statement follows from flag counting, not these finite cases.

## originality

PASS

Schröer, Oblak and Huang address the proper mutually-annihilating XY=YX=0 sublocus, while Bernau–Abian/Flanders address constraints on Jordan invariants of AB and BA without counting ordered square-zero factors by two product ranks over finite fields. The submitted finite q, full joint (a,b,r,s) distribution and exact support are not a corollary of the inspected stated theorems; general finite-field incidence calculus is shared, and an unindexed equivalent old count remains possible.

## value

PASS

A complete bivariate product-rank profile is a natural invariant of ordered finite-field representations of F_q<x,y>/(x²,y²); the product-rank asymmetry boundary and forced diagonal collapse for maximal square-zero ranks have intrinsic representation-theoretic meaning. It distinguishes noncommuting pairs beyond mutual annihilation and is not a manufactured finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
