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

The proof was replayed symbolically from the stated definitions. For the induction step, the polar isometry of the \(k\)-th iterate is \(U^{2^k}\), its modulus is diagonal with entries \(w_{n+2^k-1}^{R_k}\), and applying the next transform gives the shift length \(2^{k+1}\), offset \(2^{k+1}-1\), and exponent product \(R_{k+1}\).

For a positive \(d\)-step weighted shift, \(W^*W\) and \(WW^*\) were computed on every basis vector. Their diagonal comparison proves that \(p\)-hyponormality is equivalent to monotonicity of the weights at spacing \(d\), with no restriction arising from a finite test range.

The tail implication was checked for every index in its quantified range. The finite-threshold constructions and the never-hyponormal construction were substituted directly into the same necessary-and-sufficient criterion.

No computation, experiment, or external certificate is needed for correctness. The result does not establish claims for noncentral quaternionic weights, zero weights, bilateral shifts, or general operators.
