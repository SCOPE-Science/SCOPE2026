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
# Verification and scope

The analytic proof in `RESULT.md` consists of (i) an exhaustive partition of the two BH rejection regimes, (ii) an exact Gaussian antithetic threshold identity and bounded-convergence passage to strictly negative nonsingular correlations, and (iii) a finite rational probability comparison for an explicit positive-definite covariance. This is a general proof over every \(0<\alpha<1/2\), not an extrapolation from a numerical grid.

Run `python3 verify.py` using the Python standard library. The script checks the exact fraction \(\rho=-99999999/100000000\), \(2(1+\rho)=2\cdot10^{-8}\), the Chebyshev term \(1/1250\), the disagreement upper bound \(29/5000\), the FDR lower bound \(317/10000\), the rational conjecture upper bound \(30307/1088000\), and their strict difference. It also checks an illustrative normal threshold identity and a quadrature diagnostic for a different nonsingular correlation. These diagnostics are *not* used as proof of probability bounds; the normal-density and Chebyshev inequalities justify the universal numerical certificate.

Limitations: The Gaussian result concerns one-sided tests, exactly one true null and one false null, and exactly two hypotheses. The explicit correlation is near singular but positive definite. No claim of uniqueness of the maximizing nonnull mean, an interior maximizer, or a general many-test bound is made. Literature comparison is based on inspected sources and does not constitute independent priority validation.
