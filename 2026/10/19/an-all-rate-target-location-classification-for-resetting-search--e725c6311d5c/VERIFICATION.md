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

# Verification record

The independent Poisson resetting renewal identity was derived from exponential race probabilities; it is not an empirical assumption. The result's proof explicitly gives all domains, the lumped transient generators, Laplace transforms, exact mean times, and strict sign arguments. The `verify.py` script uses SymPy to check the symbolic matrix inversions, mean-renewal identities and bridge transform and NumPy to solve the unreduced full absorbing generator. Execution passed all symbolic assertions and all 600 finite-graph comparisons.

The finite calculations are consistency tests only. Correctness for arbitrary clique sizes and continuous reset rates follows from the generator identities and derivative inequalities in RESULT.md. Prior-literature comparisons were performed separately; numerical or symbolic computations cannot establish absence of prior publication. This is a self-reviewed result, not an independent audit.
