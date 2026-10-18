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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 and SymPy available. This test checks nine rational-function identities exactly in the quotient field defined by \(s^2=3\), including all junction equations and both exact excess factorizations; checks 12 signs at rational choices of the perturbed cell length; and compares six finite-interval Gram-integral evaluations with the infinite-mesh formulas. It does not require access to any other file.

The relevant closed-form coefficient entries and series are derived in `RESULT.md`. Analytical verification applies to every real \(\tau>0\) because every factor needed in the positive numerator and denominator has a fixed sign. Tests at finitely many parameter values are diagnostic, not a substitute for the proof. The limiting finite-mesh comparisons are numerical and are not claimed as a finite-interval theorem. No independently authored audit has been performed.
