---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility checks

Run `python3 verify.py` with a standard Python 3 interpreter. The script independently enumerates all candidate images of the two algebra generators for each field and parameter, multiplies basis vectors according to the original presentation, rejects failed defining relations, counts algebra automorphisms and idempotent maps, composes every pair of retractions, and constructs the commuting graph. It compares enumerations with the closed endomorphism counts, idempotent counts, all graph component sizes, vertex degrees and edge counts.

## Completed finite checks

- Over \(\mathbb F_2\), tested its sole nonzero parameter (exterior).
- Over \(\mathbb F_3\), tested both nonzero parameters, ordinary-commutative and exterior.
- Over \(\mathbb F_4\), used a direct arithmetic implementation with irreducible polynomial \(u^2+u+1\), and tested all three nonzero parameters.
- Over \(\mathbb F_5\), tested all four nonzero parameters, including the exterior, commutative-nonexterior and genuinely quantum regimes.

All ten parameter instances returned `CHECK_OK`; the script completed with `VERIFY_OK`. The most computationally intensive case includes \(5^6=15625\) possible pairs of radical generator images.

## Verification limits

The computation uses finite samples of field orders and is not an exhaustive check across prime powers. It is not an independent mathematical audit. The algebraic proof in the main result establishes all finite-field cases. Publication priority beyond inspected literature is unverified.
