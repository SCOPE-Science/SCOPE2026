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

# Reproducibility and verification

The supplied `verify.py` is a standalone Python 3 program using SymPy and mpmath; SciPy is optional. It was executed from the actual file path and passed. Its exact symbolic checks cover the baseline factorization, the shock fold radical and fold equality, the explicit quadratic denominator, and the resulting exact logarithm–arctangent travel-time formula. High-precision quadrature gives the illustrative threshold \(13.421142615246071\ldots\) between the two chosen pulse lengths and reproduces the fold-divergence prefactor \(7.512449697187874\ldots\). Successively smaller fold offsets exhibit the expected inverse-square-root trend. Optional numerical integration at \(\varepsilon=10^{-4}\) gives recovery for scaled duration \(12\) and extinction for scaled duration \(15\).

The general theorem is established by the proof in `RESULT.md`, including the compact-interval singular-limit basin argument. Neither symbolic finite specialization nor numerical ODE trajectories prove the all-parameter and small-\(\varepsilon\) statements. The equality \(s=s_c\), exact finite-\(\varepsilon\) crossing duration, and simultaneous limits of duration/amplitude and \(\varepsilon\) remain unproved. Independent audit has not been performed.
