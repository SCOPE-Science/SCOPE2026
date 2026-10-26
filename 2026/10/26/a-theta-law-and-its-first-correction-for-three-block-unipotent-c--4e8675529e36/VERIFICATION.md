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

The executable `verify_threeblock.py` is self-contained and uses only Python's standard library. Execute `python3 verify_threeblock.py` from the directory containing this file and compare its output with `verification_output.txt`.

The checker exhaustively tests the matrix-product condition and rank counts for matrices of order \(2\) over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); for the latter it implements \(\mathbb F_2[u]/(u^2+u+1)\). It independently enumerates central-block conjugacy orbits for the three corresponding five-dimensional unipotent groups, recovering 58, 417, and 1636 classes. It separately verifies the full rank histogram over \(\mathbb F_2\) in order \(4\). Its finite-precision comparisons at larger dimensions test the two-term asymptotic and use a tolerance appropriate to floating-point roundoff.

The proof of the rank-stratum identity uses the independent count of surjections, rather than the output log. The convergence and first-order bias rely on a uniform error estimate for infinite Euler-product tails and summability against \(q^{-t^2}\); these cannot be proved by exhaustive finite computations. There is no claim of independent audit or exhaustive comparison with unpublished literature.
