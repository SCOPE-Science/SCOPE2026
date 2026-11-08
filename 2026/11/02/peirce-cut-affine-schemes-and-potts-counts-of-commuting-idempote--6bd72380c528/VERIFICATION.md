---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For any commutative base k-algebra R, commuting idempotents project to Boolean label coordinates in (A/J)⊗R. Polynomial joint spectral projectors p_alpha produce an orthogonal idempotent system reducing to d_alpha. The conjugator w=Σ p_alpha d_alpha is a unit (1 modulo nilpotent J); decomposition J=H_alpha+N_alpha by equal/cross labels gives unique normalization w=(1+x)(1+h) with x=n(1+h)^{-1}. Both inverses are polynomial, so each labeled functor fiber is truly affine scheme A^{dim N}, not just a bijection of k-points, and reducedness/smoothness hold in all characteristics. Cut dimension κ and Fortuin–Kasteleyn expansion then yield exact point counts, weighted max-cut/chromatic cutoff, and truncated-quiver polynomial recovery. Independently computed ordered commuting idempotents in upper triangular 2x2 over F2,F3 and genuine F4 (counts for m=1,2: (6,28),(8,40),(10,52)); these and inspected 31-case source checker are corroborative only.

## originality

PASS

Classical conjugacy of orthogonal idempotents and Potts random-cluster identities are explicitly credited; those ingredients alone do not state the complete scheme decomposition for any radical nilpotency and all arities. Existing radical-square-zero orbit-count work counts conjugacy classes instead of actual points. An unknown older idempotent-variety theorem could subsume this, so originality is qualified.

## value

PASS

Full smooth affine scheme and arithmetic count for unbounded split-basic algebras, governed only by off-diagonal Peirce dimensions, is a structural classification. Nilpotency independence, cut/chromatic maximum-dimensional strata, and finite reconstruction of a graph polynomial are natural useful invariants not a renaming of the Potts polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
