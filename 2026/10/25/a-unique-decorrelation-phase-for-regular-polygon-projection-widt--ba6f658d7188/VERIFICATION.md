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

# Reproducibility and limitations

## Analytic checks
1. Difference-body support reduces both parity cases to a regular even \(N\)-gon of radius \(\rho\), with centered cosine chambers of half-width \(a=\pi/N\).
2. The mixed moment is the sum of two explicit cosine-product integrals separated at \(a-d\). Subtracting the square of the exact mean yields (1).
3. Differentiation gives the exact derivative (7); strict sinc monotonicity and the zero average of centered autocovariance yield exactly one simple zero on \((0,a)\).
4. Uniform Taylor expansion of the centered folded cosine, followed by two polynomial integrations, yields the quartic limit. A nonzero derivative at its root yields the \(O(a^2)\) root error.

## Computational checks
Running `python verify.py` with Python 3 standard library returned `VERIFY_OK: 223 finite numerical regression checks`. It constructs vertices and takes projection maxima and minima instead of generating test widths from the claimed cosine chamber. It numerically integrates angular covariance at five lags for each \(3\le n\le12\), tests periodic symmetry and numerical root signs, and compares larger regular polygons against the limiting root. The deterministic finite quadrature and floating-point tolerances are auxiliary regression tests; they are not exhaustive and do not prove any statement with universal quantifiers.

## Scientific limits
Unshifted width variance and generic edge-projection pair moments appear in prior published work. The exact joint-lag monotonicity, unique threshold and universal normalized limiting phase are asserted as the evaluated extension. No result for arbitrary polygons or empirical-noise reconstruction is claimed. Bibliographic priority remains subject to further independent checks. Independent audit has not been performed.
