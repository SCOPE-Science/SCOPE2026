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

Run `python3 verify_root_packet.py` alongside this file, using the standard Python 3 library. The recorded fresh run reported:

```
PASS 5067 exact collision/deficit/phase assertions; 32 projective q=4 optimizers
```

The checker enumerates ordered-pair frequency sums, compares fourth-moment identities with direct convolution for 120 deterministic complex-integer coefficient arrays across unaliased, order-four, order-five and order-seven settings, checks exact-deficit nonnegativity within numerical tolerance, and exhaustively enumerates all 4096 six-component fourth-root coefficient patterns. Its exact enumerations corroborate the finite aliasing and projective count. The universal inequalities for every integer order at least four are proved symbolically in the accompanying text. Independent audit has not been performed.
