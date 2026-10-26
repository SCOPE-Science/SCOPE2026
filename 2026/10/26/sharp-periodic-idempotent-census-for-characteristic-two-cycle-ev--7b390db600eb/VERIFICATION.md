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

# Reproducibility and verification

Run `python3 check_idempotents.py` using the embedded code and Python 3 standard library. The verified output is:

```
CYCLE_EVOLUTION_IDEMPOTENTS_OK 480 matrix_pairs 19 direct_enumerations 642 period_tests
```

The executable independently constructs the binary cycle-adjacency matrix and computes \(\dim\ker(A^m-I)\) by Gaussian elimination for 480 pairs \((n,m)\). A separate finite-field arithmetic implementation checks the original coordinate equations \(v_i=v_{i-1}^2+v_{i+1}^2\) for 19 small instances over \(\mathbb F_2,\mathbb F_4,\mathbb F_8\) and \(\mathbb F_{16}\). Further tests check the period and saturation predictions at 642 parameter pairs, and the low-extension explicit expressions for \(3\le n<80\).

The general proof is independent of those enumerations. Its critical ingredients are the normal-basis bijection, the cyclic-polynomial kernel-gcd lemma (valid for repeated factors), the derivative-squarefreeness test for odd extension exponent, and the finite-unit-order divisibility argument for minimal saturation length. The code checks finitely many instances only; it cannot certify an infinite theorem or publication priority.

Independent mathematical audit: not performed. No external certification is asserted.
