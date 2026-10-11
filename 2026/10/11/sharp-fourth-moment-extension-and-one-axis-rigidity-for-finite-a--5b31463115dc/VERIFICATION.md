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

The accompanying `artifacts/verify.py` was executed using Python 3 and NumPy. It independently constructs the character matrix for each test group and evaluates fourth moments from the full complex Fourier array. Results: \(4,400\) random complex Fourier inputs across eleven finite abelian groups of orders \(5\) through \(11\), \(178\) character-supported coordinate-axis equality examples, \(3,900\) random centered-moment inputs, thirteen exact two-level centered-moment extremizers, and the order-three strict witness \(77/25\). All checks passed. The sum-of-squares polynomial identity was separately confirmed symbolically to have zero residual. Run with `OPENBLAS_NUM_THREADS=1 python artifacts/verify.py` from the package root with NumPy installed.

The complete all-order theorem follows from the analytic proof in RESULT.md, not from these finite checks. The numerical tests do not establish uniqueness of optimizers, rule out undiscovered equivalent published results, or certify independent correctness.
