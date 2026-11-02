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

# Verification and limits

The independent audit channel has not been performed. The correctness check uses a direct proof of the defining \(F\)-stochastic hypotheses, explicit matrix powers, stochastic convex-hull bounds, Dobrushin multiplication, and monotone extrema of each column of the reverse product.

Execute `python check.py` with Python 3 to reproduce 152 exact-rational two-state product checks. No external libraries, downloaded datasets, or floating-point calculations are needed. This finite replay is a consistency check, not an infinite-time proof. The proof of the limit uses analytical inequalities valid for all \(n>k\).

The primary 2024 article was read in open-access full text, including its definition of reverse products, hypotheses, Theorems 3.4–3.6, and use of Theorem 3.5 in the quantum section. The earlier perturbation theorem was inspected in its lawful open preprint, particularly its commutation requirement. Residual publication-priority and independent-validation limitations remain.
