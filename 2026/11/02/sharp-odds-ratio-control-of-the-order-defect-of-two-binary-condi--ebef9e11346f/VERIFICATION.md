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

# Reproducibility and limits

Run `python3 verify.py` alongside this document. The standard-library rational checker constructs \(P\) and \(Q\) directly as weighted group-average matrices on all four cells and computes \(PQ-QP\) by matrix multiplication. It verifies 4096 exact table instances, their full matrices and row sums, strict fixed-odds bounds via squared rational inequalities, and 15 exact-rational approaches to the sharp bound.

The checker intentionally does **not** claim an exhaustive search over arbitrary positive reals. The complete proof uses algebraic matrix multiplication and an inequality for two Bernoulli conditional probabilities, as given in RESULT.md. The independent scientific audit channel has not been performed.
