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

# Reproducibility and mathematical limits

Run `python verify.py` with Python 3.9 or newer; only the standard library is used. The script enumerates all projective points over the four-element field for \(4\le n\le7\), evaluates each of the \(n\) polynomial derivatives directly, and compares the exact singular-point sets to the proposed classification. It prints counts \(4,6,25,28\) and `VERIFY_OK` on success. No randomization is involved. This is independent small-rank finite-field confirmation, not an exhaustive check over algebraically closed fields or all ranks. The proof in RESULT.md establishes the infinite statements symbolically through two-coordinate reduction and parity.

For isolated nodes, check the projectivized quadratic tangent cone and its characteristic-two polar form; an odd-dimensional nondegenerate quadratic form can have a one-dimensional polar radical, provided the quadratic form is nonzero on that radical. No external or independent audit is claimed.
