---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Verified Jφ_j=(j+1)^(-1/2)φ_(j+1), resolvent matrix entries t^(k-j)√(j!/k!), quasinilpotence ∥J^k∥=1/√k!, and normalized exact columns √j! t^-j P_(≥j)u_t. For fixed cutoff m the omitted columns have bound e^(-t²/2)∑_n t^n/√n!=O(t^1/2) by Poisson-weight Cauchy-Schwarz. This yields O_m(t^(-m+1/2)) rank-one remainder, and m=2N+3 gives all fixed-order factorial expansion. Spectrum {0} and logarithmic pseudospectral radius follow, with fixed N and no convergence assertion for full divergent series; no finite matrix is used as an infinite-dimensional proof.

## originality

PASS

Prior Fock Volterra theory contains the quasinilpotent resolvent formula and coherent exponential lower bound, not the factorial all-order operator-norm expansion or explicit rank-one error reported here. Relevant Constantin–Persson paper was read; unresolved equivalent weighted-shift literature remains a risk.

## value

PASS

The full fixed-order factorial singular-norm expansion and explicit coherent-state rank-one operator-norm approximant quantify the extreme pseudospectral growth of a natural quasinilpotent integration operator, not merely rename a known resolvent equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
