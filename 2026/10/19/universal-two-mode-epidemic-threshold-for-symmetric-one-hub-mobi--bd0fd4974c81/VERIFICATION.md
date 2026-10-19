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

# Verification evidence

The claim is proved analytically by decomposing the next-generation matrix into an invariant two-dimensional subspace and an orthogonal complement, then applying an exact rank-one positive-definiteness test. The finite script does **not** establish the all-size result; it checks independently stated algebraic identities and finite cases.

Run `python verify.py` with Python 3 and its standard library. Expected output is two PASS lines: 192 finite exact-rational comparisons and 17 exact neutral-threshold cases. The script constructs two different symmetric stochastic peripheral mobilities at each sampled parameter set and verifies the same two-mode invariants. This is a reproducible numerical-algebraic cross-check without probabilistic tolerances.

Independent audit was not performed. The spectral result does not address nonlinear SIR dynamics at the critical threshold, nonuniform hub exchange, unequal populations, or asymmetric mobility. Complete 2024 journal text and separate supplement were not accessible; the 2023 full author preprint was consulted.
