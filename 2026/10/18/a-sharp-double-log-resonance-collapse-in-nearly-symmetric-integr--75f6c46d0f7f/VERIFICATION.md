---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the physical-time quadrature from xdot squared = 1-(E-B cos x)^2 and sin(x/2)=sqrt(u) sin(phi), counting four quarters. The centre limit is 2 pi/sqrt(B). With s=E-delta and alpha=1-u, beta=w, the error after replacing the integrand on the lower half by (phi^2+beta)^(-1/2) is bounded in integral by O(1+alpha log(1/beta)); this is bounded on delta^3<=s<=s0. On the reflected upper half the analogous bound is O(1+(alpha+beta)log(1/alpha)); both logarithms have coefficient 1/2. For s<delta^3 the lower-half integrand is at least (phi^2+beta)^(-1/2), excluding this range by comparison with the trial s=delta/(2 log(1/delta)). In the small window the comparison reduces to minimizing 2Lt-log(t), t=s/delta, L=log(1/delta). Outside that window the explicit lower bound with subtractive term -CE (fixed C) increases up to a sufficiently small fixed E0, and for E>=E0 the period is bounded below directly by the quadrature (both factors under the square root are at most one). This proves the global two-scale asymptotic, near-edge localization of all minimizers, and attainment. The two-torus statement follows from continuity on either side of a minimizer and the endpoint values; it does not imply uniqueness. The supporting quadrature code was inspected, not executed; the singular limit is analytic.

## originality

PASS

Best-of-knowledge pass for the optimized two-term singular asymptotic and minimizing-energy localization. The elliptic winding formula and rational-periodic-torus criterion are prior work, not independent novelty claims. The checked nearby statements do not establish the global minimum through the log-log term.

## value

PASS

This is an all-energy extremal claim in a natural degenerating vortex family. It resolves the rate at which the minimum available resonant winding collapses, with a secondary term not supplied by the winding quadrature alone. The exact scale and localization distinguish it from an example of a rational periodic orbit or a leading-order numerical fit; no nonintegrable or perturbative consequence is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
