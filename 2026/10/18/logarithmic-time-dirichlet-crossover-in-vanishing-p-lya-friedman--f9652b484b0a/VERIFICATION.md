---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For fixed k>=2, integer r,a,b and p_N→0, exact conditional proportions give drift −gamma_N(Z−u)/(theta+j), gamma_N=kb p_N/c. Dividing by the product A_t of drift factors gives a square-integrable vector martingale with maximal tail O(K^{−1/2}) uniformly for gamma_N<=1/4; a common uniform-input coupling makes every fixed initial K draws equal to a classical Pólya process eventually. Its bounded Dirichlet limit B is therefore the *single shared random vector* for all logarithmic times. The harmonic expansion of log A_floor(N^s) is uniform for s∈[delta,1] and yields e^{−kb lambda s/c}; if p_N log N diverges, the maximal multiplier tends to zero. The finite exact rational drift test independently checks several k,r,a,b, but path convergence follows from martingale bounds and the coupling.

## originality

PASS

No inspected primary or indexed result was shown to imply the exact final claim (not merely its tools, endpoints, or analogous construction). Structured same-object, broader-implication, equivalence, and table comparisons below document precise boundaries; best-of-knowledge and residual risks explicitly retained.

## value

PASS

An explicit critical scale p_N~lambda/log N interpolates classical random Dirichlet proportions and deterministic balanced proportions, *uniformly as a stochastic logarithmic-time path* with one common Dirichlet variable. This is a nontrivial singular triangular-array limit, not simply a restatement of either endpoint theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
