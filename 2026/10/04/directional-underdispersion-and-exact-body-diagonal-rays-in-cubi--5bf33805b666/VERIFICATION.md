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

# Verification

The proof uses the exact principal-band relation
\[
\cos(k\ell)=\frac1\nu\sum_{j=1}^\nu\cos(\ell p_j)
\]
and the strict convexity of \(t\mapsto\cos\sqrt t\) on \([0,\pi^2]\). The sign and equality statement are therefore analytic over the complete first Brillouin zone, including boundary points by continuity.

The standalone checker independently evaluates the exact arccos formula in several dimensions and verifies three consequences numerically: sampled energies do not exceed \(\lvert p\rvert_2^2\), signed body-diagonal points agree with continuum dispersion to floating-point tolerance, and the normalized small-\(\ell\) error approaches \(-\nu\operatorname{Var}(p_j^2)/12\). These computations are consistency checks only and are not used to infer an infinite-domain theorem.

Unproved limits: no higher-band statement, no result for Dirichlet flat bands, no perturbative potential or magnetic extension, and no assertion that the literature search is exhaustive beyond the inspected and indexed sources.
