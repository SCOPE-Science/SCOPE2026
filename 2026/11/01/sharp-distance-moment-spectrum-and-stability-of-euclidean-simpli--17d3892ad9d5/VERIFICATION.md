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

# Reproducible verification

The file `verify.py` requires only Python 3 standard library and is run using `python3 verify.py`. It was executed successfully during this review with output:

`VERIFY_OK 591 exact identities and seeded pair-distance tests`

The checker independently enumerates exact Dirichlet fourth moments, checks the centered Gram identities and exact rational spectrum at dimensions 3--9, exercises positive definite Gram interpolations, and compares two seeded independently sampled chord distributions. The actual bundled file was executed, rather than relying on stale logs.

**Analytic limits.** The finite checker does not prove the all-dimensional quartic extremal lemma, unique spike equality class, or absence of hidden prior equivalents. Those depend on the manuscript's algebraic and variational proof and the primary-source comparison respectively. Near-extremal upper configurations are limiting objects, not full-dimensional probability distributions. Independent audit is not performed.
