---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

At the unique cuspidal normalization preimage, every projective stabilizer lifts to t -> at+b. The pulled-back linear system is span{1,t^q,t^(q+2)+t}. Frobenius expansion contains the otherwise-forbidden a^2 b^q t^2 term for q>=4, enforcing b=0 and a^(q+1)=1; in q=2 the t^2 terms cancel and a^3=1 while b is arbitrary. These conditions give the stated explicit projective matrices, not just necessary relations. Infinitesimally, F_X=Z^(q+1), F_Y=0, F_Z=X Z^q, so coefficient comparison imposes B=C=J=K=0 and A=L, with D_X,Y,Z parameters four-dimensional before quotienting by scalar matrices: Lie dimension 3 for all q. Reduced dimensions 0 (q>=4), 1 (q=2), hence non-smooth/nonreduced over perfect k. Independent GF(2) coefficient linear algebra for q=2,4,8,16,32 reproduces rank 6 in the ten-variable linearization. The direct symbolic proof handles all q=2^n; finite checks are not infinite proof.

## originality

PASS

The original Kollár construction establishes this family and its cusp but the checked material does not calculate full projective stabilizer or scheme tangent. A different positive-characteristic embedding or automorphism-scheme classification could cover the result, so priority remains best of knowledge.

## value

PASS

Computing the actual linear stabilizer of a specific newly studied family of cuspidal rational plane curves reveals a non-smooth symmetry scheme in every power-of-two degree. The one-dimensional-versus-zero-dimensional exceptional q=2 jump and persistent three-dimensional tangent distinguish genuine geometric and infinitesimal automorphisms. This structural classification is not a renaming or routine single numeric check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
