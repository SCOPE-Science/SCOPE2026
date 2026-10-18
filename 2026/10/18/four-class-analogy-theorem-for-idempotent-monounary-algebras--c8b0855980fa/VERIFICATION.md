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

# Verification and reproducibility

The Python 3 file `verify.py` computes term-rule justifications directly from the unary operation, using each of the four exponent regimes made exhaustive by \(f\circ f=f\). For each ordered quadruple it implements all four directed maximality conditions at fixed first coordinate and compares the computed proportion with the claimed four-class partition. It then checks the analytic count for the same unary map.

Run `python verify.py`. The completed run printed:

```
labelled 1 1
labelled 2 3
labelled 3 10
labelled 4 41
labelled 5 196
labelled 6 1057
VERIFY_OK labelled_maps=1308 canonical_large=67 ordered_quadruples=1826684
```

The program exhausts labelled unary idempotent maps up to six elements and checks canonical representatives arising from integer partitions for seven to nine elements. These computations are finite; the proof of the unrestricted theorem is contained in `RESULT.md`. No external independent review or proof-assistant certification is claimed.
