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

# Reproducible analytical and numerical checks

Install the packages specified in `requirements.txt`, then run `python verify.py`. The program constructs genuine motion-invariant Crofton affine lines conditional on intersection with a unit cube, using the projected-area directional acceptance weight and flux-proportional entry facet; all exit facets are checked from uniform facet-start points. Exact one-dimensional numerical integration is compared in dimensions 2, 3, 5 and 10. A separate stable quadrature computes high-dimensional saddle ratios and the centered first two amplitude moments in dimensions 100, 300, 1000, 5000 and 20000. The final local test returned `ALL_CROFTON_HYPERCUBE_CHECKS_PASSED`.

The exact formula and asymptotic expansion rely on the independent mathematical derivation in `RESULT.md`: invariant offset measure, homogeneous Gaussian flux ratio, explicit truncated-half-normal integration, a unique global saddle with controlled tails, and a radial chi distribution. The finite experiments do not prove convergence, exhaustively enumerate real-valued directions, or independently certify historical priority. Numerical results are seed-controlled and accuracy is limited by floating-point quadrature and Monte Carlo error.
