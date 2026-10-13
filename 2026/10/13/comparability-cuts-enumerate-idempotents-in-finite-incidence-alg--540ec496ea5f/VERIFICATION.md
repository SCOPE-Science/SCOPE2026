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

The general proof was checked through four exact steps.

1. The radical \(J\) has one basis vector for every strict comparable pair.
2. The published conjugacy construction for an idempotent with diagonal \(\varepsilon_S\) uses a conjugating unit in \(1+J\), so that group is transitive on the complete diagonal fiber.
3. A radical basis vector \(e_{xy}\) commutes with \(\varepsilon_S\) exactly when \(x\) and \(y\) are on the same side of the cut. Hence the stabilizer codimension is exactly \(c_P(S)\).
4. Orbit-stabilizer gives \(q^{c_P(S)}\) elements in that fiber, and the diagonal fibers partition the full idempotent set.

The supplied `verify.py` independently enumerates incidence-algebra elements and tests convolution idempotence. It covers every transitive relation contained in the natural order for \(1\le n\le4\) over \(\mathbb F_2\) and for \(1\le n\le3\) over \(\mathbb F_3\), totaling \(60\) relation-field cases. It also checks the complete-chain specialization for \(1\le n\le8\) at field orders \(2,3,5\). The expected terminal line is:

```text
VERIFY_OK cases=60
```

These finite computations are not used to infer the all-poset theorem. No claim is made for coefficient rings other than finite fields.
