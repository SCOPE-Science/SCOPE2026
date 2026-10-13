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

# Verification of the Haar-orbit formulas

The analytic argument in `RESULT.md` establishes the full infinite family. This record provides independent finite-dimensional checks, not a replacement for proof.

The decisive conditional-distribution fact is that, after fixing the first Haar row, the second lies uniformly in its complex orthogonal complement. A unit vector's first-coordinate squared magnitude has the \(\operatorname{Beta}(1,d-2)\) law in complex dimension \(d-1\). Hence the Dirichlet spectral variance factor and the beta factor can be independent. For \(d=2\) the latter is a point mass at one. This verifies the normalization and both edge cases in the proof.

The independently derived covariance check for every real spectrum is
\[
 \mathbb E|(U\Lambda U^\dagger)_{12}|^2
 =\frac{d\operatorname{tr}(\Lambda^2)-(\operatorname{tr}\Lambda)^2}{d(d^2-1)}.
\]
For a rank-\(k\) normalized projector this equals \((d-k)/[kd(d^2-1)]\). Both expressions agree algebraically with the beta-product moment formula at \(s=2\).

To replay from the accompanying standalone script, run `python verify.py` in an environment with NumPy. The script verifies the exact pure and corank-one endpoint coefficients, independently compares second moments for all \(2\le d\le15\) and \(1\le k<d\), and checks three rational multiples of \(\pi\) from the gamma formula. It then samples independently generated complex Haar unitaries by phase-corrected Gaussian QR and compares \(21000\) seeded Monte Carlo coherence values to the analytic means. Successful replay prints `VERIFY_OK endpoints=passed gamma_cases=3 second_moments=passed Haar_samples=21000`.

The Monte Carlo tolerances are probabilistic numerical diagnostics; passing them does not establish any formula for untested dimensions, prove independence in law, or exclude previously published equivalent formulations. No claims about concentration of the sum of entries, general elementary Dirichlet integrations, or uniqueness of this sampling representation are made.
