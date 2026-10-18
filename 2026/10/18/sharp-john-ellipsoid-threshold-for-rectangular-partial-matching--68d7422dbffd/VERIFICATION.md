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

# Verification details

The proof uses exact facet support, an explicit John contact certificate, matrix eigenvalues, and a strict log-determinant comparison. The file `verify.py` is a standalone Python-standard-library exact-rational check of these identities for \(2\le a\le12\), \(a\le b<a+12\). Running `python3 verify.py` yields:

```
VERIFY_OK cases=132 stable=110 changed=22 boundary=[(4, 5), (9, 11)]
```

The checker reconstructs the row-block inverse, the weights/moment conditions for coordinate and row-cap contacts, the squared support radii, the integer threshold (including non-square and square cases), and the eigenvalues; it separately checks the two boundary cases and selected subcritical/supercritical cases. These finite calculations do not replace the infinite-family analytic proof. The program does not attempt an independent numerical solution of the subcritical ellipsoid or a complete literature-priority certificate.
