---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify.py` with Python 3. The script exhausts the quandle homomorphism equation at moduli 3 and 5 and checks equality with the affine family. For moduli 3, 5, 9, 25 and 27 it builds adjacency from affine composition, checks the determinant criterion for all pairs, verifies clique neighborhoods in the proposed elimination order, and checks the maximum clique size from that order. It tests all six pairs of the four Chinese remainder witnesses at each of moduli 15, 21 and 45.

Observed output:

```
VERIFY_OK affine=3,5 orders=3,5,9,25,27 cycles=15,21,45
```

These finite checks concern the listed moduli only. The general theorem uses the affine representation, the complete neighborhoods of the primitive vertices, the lifting argument for the remaining graph, and the induced cycle proof.
