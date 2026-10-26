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

# Reproducibility

Run `python CHECK.py` under Python 3.10+ with its built-in standard library only. A recorded execution returned `PASS: 3955 exact assertion checks, including exhaustive enumeration of all graphs on up to six labeled vertices.`

The checker separately calculates empirical moments by iterating over all edge subsets and comparing them to the exact binomial-coefficient formulas. It also checks the rational conditional-moment factor and the predicted finite sign phase across selected parameters through \(n=54\).

The analytic proof, rather than the finite checks, establishes all integer parameter values and the sparse limit. This verification does not establish independent validation, originality in the entire historical literature, or any stronger dependence ordering.
