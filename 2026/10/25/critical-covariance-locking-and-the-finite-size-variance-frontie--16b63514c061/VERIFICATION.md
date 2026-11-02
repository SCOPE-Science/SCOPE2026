---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Under r>m>0, phi>=0, finite N>=2, identical independent local-reset clocks, first-Wasserstein contraction of synchronized copies proves unique finite-first-moment invariant. Generator yields the correct two-dimensional Metzler raw moment matrix K; Perron eigenvalue gives finite second moments iff m < (3r+2phi -sqrt((r-2phi)^2+8r phi/N))/4, including equality divergence. Independent symbolic rational algebra confirms det K=2D, centered V=Q(delta+phi/N)/D and C=Q phi/(ND), derivatives, critical m=r/2 locking C=x0^2/(N-1), and square-root finite-size window. No stronger tail law claimed.

## originality

PASS

Statement-level search and implication audit, not a novelty proof from a failed search. Homogeneous independent local resets are a special case of affine-reset polynomial processes. Jolakoski Brownian reallocation is close, but differs in stochastic noise; check exact generator forcing before importing results. General affine moment formulas imply a recipe but not the explicitly solved threshold/critical locking result absent model-specific substitution; earlier work is explicitly credited. Best-of-knowledge originality survives with the stated residual risk.

## value

PASS

For a natural interacting finite-reset growth process, exact second-moment boundary and the critical redistribution-invariant covariance identify a nontrivial finite-N phase frontier useful for stationary fluctuation analysis. Generic generator closure alone would not determine its explicit threshold and sign transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
