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
# Verification performed

The standalone standard-library Python program `verify_bipartite.py` was executed on the same content supplied with this finding. It printed `ALL CHECKS PASSED: 41930 assertions`. It verifies rational spectral-projector identities, exact reconstruction of the graph Laplacian, independently constructed truncated matrix exponentials, stochasticity, cross-part positivity, signed within-part entries, exact row-sum norms, the dominant row part, recovery order and signs, and the derived finite maximum.

The parameter sweep covers all ordered and reversed pairs with two through six vertices in each part (25 pairs), evaluated at five time parameters each. It also examines large-contrast pairs with sizes \(300\), \(1000\), and \(5000\) for fixed small parts. Floating numerical comparisons use explicit tolerances; the projector identities use exact rational arithmetic.

These checks confirm finite computations and support reproduction; they do not replace proof of the universal inequalities, uniqueness, or asymptotic limits. Those claims are proved analytically in `RESULT.md`. No independent audit was conducted.
