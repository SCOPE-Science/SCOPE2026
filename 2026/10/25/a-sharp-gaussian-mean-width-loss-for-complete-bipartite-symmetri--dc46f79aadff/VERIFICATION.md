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

# Verification evidence and limits

The reproducibility artifact `verify.py` is a standalone Python 3 script requiring NumPy. Run `python verify.py` from this directory.

The completed verification reported `VERIFY_OK vertex_support=750 exhaustive_rank=5 gaussian_limit_cases=4 logistic_quadrature=100000`. It used direct signed-root vertex support comparisons, exhaustive distinct-rank configurations in five small bipartitions, midpoint quadrature of the logistic positive-part integral, and independent four-Gumbel simulations for four limiting proportions. The random generator has a fixed seed to make these checks reproducible.

The analytic argument in `RESULT.md`, not finite computation, establishes the limit for all sequences with proportions converging inside the open unit interval. The simulation tolerance is intentionally statistical, and its success does not imply exhaustive verification or independent certification. The claimed bibliographic originality remains qualified by the stated search and equivalence risks.
