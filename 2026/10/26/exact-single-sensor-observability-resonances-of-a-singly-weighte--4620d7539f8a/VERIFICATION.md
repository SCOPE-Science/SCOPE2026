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

The analytical proof in `RESULT.md` covers every \(n\ge5\) and every \(w>0\). It uses the simple-spectrum symmetric PBH test, reflection parity, the strict-increasing eigenvalues of an irreducible Jacobi rank-one perturbation, and the trigonometric eigenvalues of the remaining tail after setting the measured coordinate to zero.

The standalone `check_observability.py` depends on NumPy and can be executed as `python check_observability.py`. Its fixed-seed trial uses cycles with \(5\le n\le36\), a range of ordinary and randomly sampled positive weights, the uniform weight, and every predicted positive exceptional weight in that range. The executed output is `CASES 816 MISMATCHES 0`. The mathematical theorem is not inferred from these finite tests. During proof development, observability determinants were separately symbolically factored for \(5\le n\le10\); for \(n=6\) the determinant vanished identically, and in other sizes the positive roots matched the stated exceptional set.

The calculations do not assess robustness to sensor noise or numerical conditioning near a resonance. Independent audit and independent validation are unperformed.
