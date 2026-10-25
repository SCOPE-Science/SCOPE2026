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

The standalone script `verify_wheel.py` was executed in the research environment with NumPy/SciPy and produced `VERIFY_OK support= 1600`, followed by nine finite-size spoke-exposure diagnostics. It directly compares all signed generating roots against the two-maximum formula at dimensions 4, 5, 7 and 10, weights 0.3, 1, \(\sqrt2\), 2.4, for 100 Gaussian directions per setting. Exact support comparisons have absolute numerical discrepancy below \(10^{-12}\). The nine diagnostics use sample sizes 300, 1500, 7000 and are explicitly **not** a certificate of asymptotic probability; critical convergence is demonstrably slow. For the general theorem, check proof steps 1–5 in `RESULT.md`: projection norm identity; Gaussian maxima/minima; disjoint-edge lower bound; adjacent two-Gaussian tail estimate and degree-two Poisson approximation; transfer from Gaussian to intrinsic spherical widths. The complete proof applies to all sufficiently large integers in the critical window, unlike the finite checker.
