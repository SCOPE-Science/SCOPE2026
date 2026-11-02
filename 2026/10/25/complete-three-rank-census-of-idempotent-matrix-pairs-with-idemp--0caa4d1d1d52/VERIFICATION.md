---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Fix E and conjugate to diag(I_r,0); writing F=[A B;C D], (EF)^2=EF forces A^2=A, AB=B. With T=im A, L=ker A, expand F^2=F to BC_T=BC_L=BD=DC_T=0, DC_L=C_L and D^2+C_TB=D. Then D^3=D^2 and D^2 is a projection giving a unique splitting W=H⊕K; maps C_T:T→K, B:K→T satisfy BC_T=0, C_L:L→H arbitrary. Conversely D=I_H⊕C_TB reconstructs all equations. The map F has rank t+dim H. Count splittings by Gaussian coefficient q^{hk}, C_L by q^{h(r-t)}, (C_T,B) via rank-j sum Z. This proves exact count with no overcounting and commuting specialization B=C=0. Independent complete GF(2) brute-force ranks of ordered idempotent pairs for n=2,3 agree all strata (58 and 2608 qualifying), and integer formula sums n=4 to 375244. The algebra proves all prime-power fields, not finite enumeration.

## originality

PASS

Closest primary work treats existence of unspecified idempotent factorizations and rank-one nonnegative real two-factor decompositions, not the full three-rank GF(q) count with EF idempotent. Known commuting-pair formulas are a special lower-dimensional subcount; Z correction is substantive. Full Laffey text remains inaccessible but abstract explicitly targets Euclidean-ring existence.

## value

PASS

Joint ranks of two idempotents and their idempotent product give natural statistics on a noncommutative algebraic locus over all finite fields. The formula separates the commuting locus by an exact multiplicative correction from arbitrary noncommuting pairs. The reversible block decomposition and whole-parameter Gaussian-binomial census supply a useful complete classification beyond textbook counting of single projections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
