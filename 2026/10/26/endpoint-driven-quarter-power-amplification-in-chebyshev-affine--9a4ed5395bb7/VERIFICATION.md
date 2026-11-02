---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Changing variables identifies the operator norm squared with the largest ratio of arcsine L2 measures, original Chebyshev measure versus rescaled subinterval arcsine. At least one endpoint is strictly interior. The Christoffel bound |p(x)|² <= (2N+1)/pi ||p||² and a 1/N endpoint split bound the ratio O(sqrt(N)); a normalized reproducing kernel at an interior endpoint has height squared of order N on a one-sided c/N interval, forcing ratio Omega(sqrt(N)). Thus ||R_N||=Theta(N^(1/4)). Triangular leading coefficients give diagonal 1,alpha,...,alpha^N, and iterates converge at fixed N to evaluation at beta/(1-alpha), yielding exact sqrt(1+2 sum_{j=1}^N T_j(t*)²) power-limit norm. Independently reconstructed finite Chebyshev matrices, computed SVD norms and checked the spectral diagonal; those finite tests do not prove the N-uniform estimates.

## originality

PASS

Best-of-knowledge originality: the exact stated constrained theorem is not mathematically implied by the inspected antecedents, with identified stronger-framework and inaccessible-source risks; negative searches alone are not novelty proof.

## value

PASS

A sharp, motivated growth exponent for a concrete spectral restriction block identifies severe nonnormal norm growth despite radius one. The exact iterated power norm also distinguishes short-time from long-time operator behavior, without claiming instability of the full Volterra solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
