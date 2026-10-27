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

The analytic proof in `RESULT.md` is self-contained modulo the classical Takagi factorization, elementary properties of finite orthogonal projections, and the connectedness of unitary groups. It covers all integer dimensions \(n\geq2\) and all ranks \(1\leq k\leq n\), including the zero matrix and repeated singular values.

The accompanying `verify_trace_disks.py` uses NumPy, a fixed random seed, and no external data. Run `python verify_trace_disks.py` in an environment with NumPy installed. Its recorded outcome was `PASS 1056 dimension-rank instances and 10560 checked frames`. The implementation checks explicit maximal frames, explicit zero-trace frames, arbitrary skew-symmetric perturbations, random frame upper bounds, and orthonormality at floating-point tolerances. These are finite sanity checks only; they are not a computer proof of the universally quantified statement.

The paper arXiv:2610.16823v1 is freely readable online. Bibliographic and implication comparisons appear in `REVIEW.md` and `AUDIT.json`. No third-party manuscript is redistributed. An independent audit has not been performed.
