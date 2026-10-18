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

The standalone artifact `verify.py` uses only the Python standard library. From a directory containing this file and the checker, run `python3 verify.py`; the expected final line begins `VERIFY_OK`.

Actual checks replayed before delivery: complete residues and multiplicities for \(k=3,4,\ldots,12\), totaling 8,184 checked indices over ten complete periods; 64 values of the truncated, provably convergent formal derivative modulo eight; and 1,160 pairs testing exact two-adic distance laws on the odd index branch and the two even branches.

The proof's infinite scope rests on uniform divisibility of falling factorials and their derivatives, the integral Taylor remainder, exact derivative valuations, and finite-quotient isometry/bijection. No finite test can establish the all-exponents assertion or exclude an undiscovered equivalent result. No independent audit has been performed.
