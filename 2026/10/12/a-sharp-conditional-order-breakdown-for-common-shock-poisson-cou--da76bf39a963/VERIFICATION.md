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

`VERIFY.py` is a standalone Python 3 program requiring only the standard library; execute `python VERIFY.py` from the directory containing the embedded files.

The program calculates each conditional law from the independent-Poisson decomposition \(S_n=T_n+nZ\) with \(T_n\sim\operatorname{Pois}(na)\), omitting a common exponential factor that cancels. It computes the conditional binomial mixture with `fractions.Fraction`, including exact tail probabilities and order tests. The following checks actually ran and all passed:

- 28 rational parameter cases for the three-coordinate \(b=2a^3\) likelihood-ratio and \(b=6a^3\) usual-stochastic thresholds, including exact equality cases.
- 90 rational parameter cases for the general-dimensional single-tail transition, for integers \(3\leq n\leq12\), on each side and at the threshold.
- 676 exact adjacent \(\mathrm{TP}_2\) determinants of the bivariate conditional-sum mass kernel.
- 104,328 exact finite-lattice \(\mathrm{MTP}_2\) inequalities for shared-shock Poisson mass functions on two, three and four coordinates.

All computations use integer and rational operations without floating-point tolerances. The tests are finite and do not imply the theorem for all dimensions and parameter values. The analytic proof in RESULT.md proves the infinite statements using Poisson log-concavity, convolution stability under total positivity, the established \(\mathrm{MTP}_2\) marginalization theorem, and exact finite latent-state decomposition at the two specified totals. No external certification, formal proof assistant, or independent audit is claimed.
