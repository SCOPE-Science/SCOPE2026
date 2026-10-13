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

# Verification of the ternary valuation spectrum

Run `python3 verify.py` in the directory containing this file and compare stdout with `verification_output.txt`. The program uses only the Python standard library; the computations rely on integer arithmetic and polynomial-list arithmetic, not floating point.

The script cross-checks three-adic valuations from Legendre's factorial formula against an independently coded ternary digit-sum formula for all 6,561 indices below \(3^8\). Direct enormous-integer computation of \(\binom{3n+1}{n}/(n+1)\) supplies a third check for the first 220 indices. All valuation polynomials through scale \(m=8\) are checked against recurrence output, their coefficients sum to \(3^m\), and the known nondivisible counts and maximal-valuation counts are checked. It separately tests the rational generating identity through degree 12 and the exact valuation-one frequency formula through scale 12.

All recorded runs passed. The general generating function, every larger index and all fixed-valuation asymptotics require the proof in `RESULT.md`; a finite test does not certify them. No independent audit has been performed.
