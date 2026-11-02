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

The analytic correctness check reconstructs the graph automorphism reduction; the exact skew-matrix Pfaffian and singular-speed identity; the two sharp attained pair calculations; the coercive two-parameter hub–leaf optimization; induced-subgraph monotonicity; and matching lower/upper inequalities giving the asymptotic coefficient. The proof treats every integer \(m\ge2\) and the limit \(m\to\infty\).

To replay supplemental diagnostics, run `python check_book.py` with Python, NumPy and SciPy. It tests 850 full-matrix/reduced-matrix/radical identities and finite optimization/asymptotic checkpoints. Neither random checks nor finite numerical minimizations prove the infinite statement.

Exact operator conditions use *real* diagonal potentials acting on the *complex* finite-dimensional Hilbert space. No statement is made for arbitrary complex potentials. The hub–outer formula is a genuine attained two-variable extremum, not a closed elementary number. No independent audit or external validation is claimed.
