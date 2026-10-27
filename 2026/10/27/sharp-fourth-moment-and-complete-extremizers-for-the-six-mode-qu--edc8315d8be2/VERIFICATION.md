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

# Reproducibility and verification limits

The analytic proof establishes a fourth-power norm bound and every extremizer for **all** complex six-tuples; it is not derived from finite sampling. In the accompanying `CHECK.py`, run `python3 CHECK.py` from the package directory (requires Python 3 and SymPy). The completed execution reported `PASS`, exact zero residuals for both the Fourier-convolution identity and the global sum-of-squares identity, an exact rational factorization of the one-variable derivative, exact algebraic resultant, rational isolation of the unique positive cubic root, 75 two-dimensional finite-grid moment comparisons, 25 arbitrary complex coefficient checks, and 3 extremizing-phase checks.

Critical algebraic identity: with \(U=A^2+D^2+F^2\), \(V=B^2+C^2+E^2\), \(T=ADB^2+AFC^2+DFE^2\) and the corner/edge quartic deviations \(D_U,D_V\), the nonnegative sum of squares in `RESULT.md` equals \(D_U+D_V+4UV/3-4T\) identically. Coupled with Cauchy–Schwarz and AM–GM, this proves fixed-mass symmetrization globally. The cubic stationarity equation has exactly one positive root and the boundary ratios are smaller. Complex extremizers require three explicit phase equations, reducing precisely to affine coordinate phases.

The numerical trials verify specific finite values only. They do not establish the inequality for all coefficients, do not establish bibliographic novelty, and do not provide independent validation. The independent-audit status in front matter remains unperformed.
