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

# Reproducibility and scope

Run `python verify.py` with `requirements.txt` installed. The exact algebraic checker was executed on the packaged source and passed 84 exact symbolic and rational checks, including direct matrix multiplication, all factorization and boundary values, and enumeration of pair sequences at four horizons, four rational step sizes, and four rational coupling probabilities. The proof of the for-all-horizon identity is algebraic; the almost-sure limit uses the classical strong law. Neither is inferred from finite enumeration.

The result assumes two oracle components, uniform marginals on each of the two calls, iid *pairs* across steps, fixed \(\eta>0\), and a nonzero initial vector. At a mean-square stability boundary, equality of a factor to one does **not** imply geometric contraction. Publication priority has not been independently certified; the relevant 2026 abstract had no inspectable full text in this review.
