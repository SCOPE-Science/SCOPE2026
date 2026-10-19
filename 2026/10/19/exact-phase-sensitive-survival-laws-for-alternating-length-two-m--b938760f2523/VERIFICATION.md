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

The proof uses an exact two-step transition product and a two-dimensional invariant subspace. Its trace, determinant, and two initial counts determine the full finite-horizon sequence for every alphabet and ordered pair of forbidden words. Strict coefficientwise comparisons and the spectral ordering are proved algebraically; the boundary convention changes no Lebesgue probability.

The standalone `verify.py` executable (Python 3 standard library only) was run on the packaged bytes and returned `VERIFY_OK`. Its tests check all ordered hole pairs for bases \(2\) through \(6\), independently enumerate short word sequences, check the universal four-type ordering, compare phase-dependent counts, and confirm the exceptional binary formula. This is finite corroboration, not an infinite proof. The result does not cover arbitrary holes or nonuniform symbol measures. Independent audit has not been performed.
