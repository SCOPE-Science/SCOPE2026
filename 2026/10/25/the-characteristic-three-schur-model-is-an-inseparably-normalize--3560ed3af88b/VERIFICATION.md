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

# Reproducible exact checks

Execute `python3 verify.py` using Python 3 and its standard library, without third-party dependencies. The verifier implements polynomial-basis fields of orders \(3\), \(9\), and \(27\), enumerates all normalized projective rational points, and counts the singular-line points using the exact equation \(ua^3-vb^3=0\).

The recorded successful run printed:

```text
points 3 16 singular-line-points 4
lines 3 6 rref-subspaces-examined 130
points 9 100 singular-line-points 10
lines 9 12 rref-subspaces-examined 7462
points 27 784 singular-line-points 28
F3-pointwise-false-line-positives 2
VERIFY_OK
```

All rational two-dimensional vector subspaces over \(\mathbb F_3\) and \(\mathbb F_9\) are enumerated as candidate projective lines; restriction of the defining quartic is tested as an identity of homogeneous binary forms. In contrast, merely checking the points on a line can give false positives when the field is small. These checks are finite corroborations, not infinite proofs. The universal field and line claims are established algebraically in RESULT.md. No independent audit or external validation has been performed.
