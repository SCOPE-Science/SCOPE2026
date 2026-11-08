---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Two-phase strong Markov splitting at first endpoint, reset-generating function F_x(s), and renewal H_x^r=(1-F_x)/(r F_0) give the exact mean. Chebyshev coefficient recurrence has positive coefficients; discounted survival-tail representation is convex, strictly so L>=2, while L=1 is affine M_1(u)=5+3u. Exact boundary derivative L^2(25-7L^2)/6 is negative L>=2. Uniform arcosh expansion at r=alpha/L^2 gives f(alpha) and h(alpha), and coercivity plus f strict convexity give alpha_* and optimized order-one term. Nine independent exact-rational finite-state mean calculations for L<=3 and rates 0,1/5,1/2 matched; extrapolation not used as proof.

## originality

PASS

Best-of-knowledge qualified originality: the precise complete claim is not shown to be implied by the inspected primary sources, searched published findings, or general results. Pre-existing components are explicitly credited; inaccessible source material remains as named residual risk.

## value

PASS

Completing coverage of two endpoints is a natural renewal-search objective rather than one-target hitting. The exact five-vertex positive-reset threshold, all-rate uniqueness, and O(1) lattice correction to the previously known continuum optimizer are concrete reusable discrete search results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
