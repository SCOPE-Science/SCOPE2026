---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The supplied `verify.py` is a standalone Python 3 program using SymPy and mpmath; SciPy is optional. The reported package run passed. Its exact symbolic checks concern the baseline factorization, the shock fold radical and fold equality, and the explicit quadratic denominator in the example. It compares the logarithm–arctangent formula to high-precision quadrature, giving the illustrative threshold \(13.421142615246071\ldots\) between the two chosen pulse lengths. It evaluates the fold-divergence prefactor \(7.512449697187874\ldots\); successively smaller fold offsets exhibit the expected inverse-square-root trend. Optional numerical integration at \(\varepsilon=10^{-4}\) illustrates recovery for scaled duration \(12\) and extinction for scaled duration \(15\).

The general theorem is established by the proof in `RESULT.md`. The restored dynamics use a bounded fast transient followed by a relative-entropy sublevel for coexistence or a forward-invariant low-prey region for extinction. Neither symbolic finite specialization nor numerical ODE trajectories prove the all-parameter and small-\(\varepsilon\) statements. The equality \(s=s_c\), exact finite-\(\varepsilon\) crossing duration, and simultaneous limits of duration/amplitude and \(\varepsilon\) are not classified.
