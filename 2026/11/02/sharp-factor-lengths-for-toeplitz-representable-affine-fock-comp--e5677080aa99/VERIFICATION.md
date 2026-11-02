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

The complete analytic proof is in RESULT.md. Its premises are the bounded-symbol Toeplitz recognition theorem in Lin--Lu--Zu, Corollary 3.1, and standard complex-affine composition. The key inequality \(\prod_j r_j\le\prod_j\cos t_j\le\cos^n((\sum_jt_j)/n)\) follows by concavity of \(\log\cos\); equality entails every generator's boundary slope and zero translation. Explicit factors realize all allowed points. The derivative of \(x\log\cos(\theta/x)\) establishes strict threshold growth, and Taylor expansion yields the rotation-boundary asymptotic.

Run `python3 scripts/verify.py` using Python's standard library. On the reviewed script this produced:

```
PASS 79629 deterministic finite assertions
```

The test covers thousands of permitted random products, constructive affine factorizations, exact sharp examples, strict threshold monotonicity, and angular blow-up. These are supplementary numerical checks only; they are not proofs for infinitely many factors or parameters. The manuscript claims no independent audit or externally certified status.
