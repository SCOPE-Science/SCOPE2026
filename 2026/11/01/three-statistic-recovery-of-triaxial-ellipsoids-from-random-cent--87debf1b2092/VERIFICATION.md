---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The stated cone event follows from restricting the diagonal quadratic form diag(a^-2,b^-2,c^-2) to N-perp and applying weighted Cauchy-Schwarz. Haar latitude is uniform; integrating its cone threshold yields the precise interior CDF. Dominated convergence yields the square-root upper-tail coefficient, and strict derivative of the complete elliptic integral on (0,1) proves unique recovery of the third axis after the support endpoints determine the two largest. Independently recomputed for axes (3,2,1): F(2.5)=0.550111203752269 and T=0.53370587242544; numeric checks are corroboration, not an infinite proof.

## originality

PASS

Best-of-knowledge statement/implication comparison. After a,b are recovered as support endpoints, the single upper-tail coefficient is strictly monotone in c through E(m); no explicit prior three-statistic inverse implication found. Residual possibility: implicit corollary of classical joint kernel or older stereology.

## value

PASS

An inverse stereological question is solved with only three intrinsic observables of a one-dimensional radius law, not full joint compression spectral data; strict recoverability and an explicit elliptic coefficient are relevant exact shape diagnostics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
