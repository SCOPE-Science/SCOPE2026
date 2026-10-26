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

# Verification

The ordinary Python script `verify_rounding.py` enumerates every possible rounded matrix from four independent Bernoulli bits, computes each exact Gram eigenvalue, and sums the corresponding symbolic probabilities. Symbolic checks establish the exact expectation, the rank-loss polynomial, the three-occupied-entry golden-ratio spectrum, the orientation derivative, and its critical value. Additional checks are 121 exact rational parameter comparisons, 1,000 independently evaluated dense-SVD comparisons of all sixteen matrices per parameter sample, and six grid checks of the orientation transition. The script finished without assertion failures.

These checks are **not** a proof of the universal claims; the complete algebraic enumeration and analytic optimization are given in `RESULT.md`. No interval enclosure, hardware rounding validation, high-dimensional experiment, or external independent audit is asserted. The script needs `sympy` and `numpy` in addition to the standard Python library.
