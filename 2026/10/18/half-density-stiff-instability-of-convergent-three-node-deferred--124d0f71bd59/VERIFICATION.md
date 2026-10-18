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

Run `python verify.py` with Python 3 and SymPy to replay exact-rational and symbolic checks of the specified SDC matrices. The replay returns `VERIFIED: 114 exact assertions` and checks the finite-stiffness witness \(R_8(-5000)>1\), along with the exact stiff amplification \(35934757/35831808\). The proof separately establishes the analytic recurrence, irrationality, and equidistribution needed for the infinite-density theorem. Computational assertions do not constitute a proof of irrationality or of an infinite frequency.

No independent scientific audit has been performed. The source-comparison limitations are stated in `REVIEW.md`.
