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

The proof is symbolic and valid for every \(N\ge2\).

`checker.py` performs an independent exact-rational replay. For each tested data set it centers the observations, expands the Dirichlet-weighted linear and quadratic forms by explicit index sums, evaluates every weight monomial with the uniform-Dirichlet factorial moment formula, and reconstructs
\[
\operatorname{Var}(M),
\quad
\mathbb E V,
\quad
\operatorname{Cov}(M,V),
\quad
\operatorname{Var}(V).
\]
These are compared with the closed formulas.

The checker uses no floating-point arithmetic and no Monte Carlo simulation. Its bounded data sets are consistency checks only; the universal result follows from the analytic moment identities in the proof.
