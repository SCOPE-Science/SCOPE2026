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

# Reproducibility and limits

Run `python3 verifier/verify.py` from the directory containing the extracted package, using Python 3.9 or newer. The checker uses only the standard library. A successful replay prints a `PASS` line with the number of deterministic bounded checks. It uses exact rational arithmetic for sampled two-by-two covariance contractions, rank-one sharpness determinants, and reset-boundary inequalities, and floating-point sampling for the continuous trajectory and thermal midpoint. Every test is finite and therefore cannot establish the all-dimension theorem. The universal proof is supplied in RESULT.md: the two congruences, rank-one determinant witnesses, thermal minimax and explicit two-eigenvalue spectrum.

The matrix rule is not asserted to be a completely positive trace-preserving quantum operation. Its guaranteed property is preservation of the admissible fermionic one-particle correlation-matrix cone. The resonant trajectory theorem applies only to the listed one-mode, zero-detuning continuous equations. The related October 2026 paper identifies a general hard-reset physicality obstruction, but complete full-text priority comparison could not be performed; this does not constitute independent novelty certification.
