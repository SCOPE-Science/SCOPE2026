---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For N=V⊕(V⊗V) with W=N², Leibniz forces every derivation D(v,w)=(Av,f(v)+(A⊗I+I⊗A)w). D²=D is equivalent to A²=A, B²=B, Bf+fA=f. Splitting V=im A ⊕ ker A gives B scalar sectors 2,1,1,0, so char!=2 forces D=0; in char2 allowed f blocks are exactly UU⊕ZZ from U and UZ⊕ZU from Z. Rank is r+2r(n-r), Gaussian subspace/complement count yields the claimed q-polynomial, and the half-rank bound follows from (n-2r)(n-2r+1)/2. Independent exact GF(2) n=2 full enumeration gives 1+256T²+96T³=353, using rank over GF(2), not real rank.

## originality

PASS

Earlier derivation research addresses untruncated free associative algebras, locally nilpotent derivations in characteristic zero, Leibniz/Lie two-step algebras, or other relatively free quotients; none of those statements entails this characteristic-two composition-idempotent lift classification and labeled finite-field census.

## value

PASS

The characteristic discontinuity, explicit quadratic lifts, exact rank polynomial and sharp half-dimensional bound resolve natural structural questions for the universal nonunital two-step free associative algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
