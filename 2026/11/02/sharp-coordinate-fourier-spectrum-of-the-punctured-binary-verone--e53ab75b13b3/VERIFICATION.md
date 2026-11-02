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

# Reproducible verification
Run `python3 check.py` with only the Python standard library. It enumerates all \(2^d-1\) nonzero binary vectors for each \(d\in\{3,4,5,6,7,8\}\), creates every signed diagonal and offdiagonal coordinate character, forms the exact rational probability Gram from the character values, and checks the claimed all-cube moment matrix after deletion of zero. It then performs exact rational Gaussian elimination to verify full column rank and exact determinant
\[
\det G_d=\frac{2^{d(k-1)}(2^d-k)}{4^m(2^d-1)^k}.
\]
It tests the complete three-dimensional trivial-sector bilinear form and the exact invariant action on representative vertex, incidence and edge-kernel contrast vectors. Successful completion prints `VERIFY_OK` after displaying one passed line for each of the six dimensions. The code was executed from its actual embedded-file source before packaging and all six dimensions passed.

The program does **not** enumerate infinitely many dimensions and does not serve as a substitute for the incidence-matrix proof of the full spectrum, the strict Rayleigh bounds on all competing eigenmodes, or the asymptotic perturbation argument. Those proofs are written out in `RESULT.md`. No external independent audit or validation was conducted.
