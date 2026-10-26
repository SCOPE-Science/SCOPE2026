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

# Verification details

The analytic argument uses the exact binomial spin-count measure, the entropy series, a quartic-dominated Riemann-sum limit and two-well Laplace localization with shrinking curvatures. The nonstandard small-coupling coexistence location is checked by the analytic implicit-function equations and their explicit Taylor coefficients. The separate `CHECK.py` script numerically checks three finite-
\(K\) coexistence locations, the reflection-symmetric limiting density and illustrative finite-spin binomial probabilities using only the Python standard library. Execute `python3 CHECK.py` with Python 3. This is a finite computational sanity check, **not** an external or independent audit. The results remain conditional on the exact Gibbs Hamiltonian and its stated scaling assumptions.
