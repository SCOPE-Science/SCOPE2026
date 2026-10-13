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

The proof has two exact components.

1. The degree-\(30\) witness uses \(\beta=(4,6,8,12,14,20,24,28,30)\) and \(\alpha=(1,1,1,1,1,1,1,5,1)\). Direct rational arithmetic gives \(\sum_i\alpha_i/\beta_i=1\), and the denominator exponents are distinct and even.
2. For any hypothetical degree-\(\le28\) bounded nine-variable example, write \(\beta_i=2d_i\) with nine distinct \(d_i\in\{1,\ldots,14\}\). Then \(1\le\alpha_i\le2d_i-1\). With \(L=360360\), the exact equation is a finite bounded subset-sum problem. `verify_db9.py` enumerates all \(2002\) denominator sets using integer bitsets only. It reports \(1228\) sets impossible already at \(\alpha_i=1\), and checks the remaining \(774\) exactly, with zero feasible sets.

`verification.log` is the replay output. No floating-point calculation is used in acceptance. The computation proves only the finite lower bound for nine variables; it is not a general theorem about all \(D_b(n)\).
