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

The script `verify.py` was run from the delivered package contents. It builds path concatenations directly and checks modular adjoint ranks against the explicit symbolic distribution for \((q,m)=(2,1),(2,2),(2,3),(3,1)\), with a separate all-pairs commutation census in the first case. The actual output was:

```text
CENTRALIZERS_OK q=2 m=1 dim=8 classes=46 pairs=11776 ranks=[(0, 4), (1, 20), (2, 56), (3, 112), (4, 64)]
CENTRALIZERS_OK q=2 m=2 dim=10 classes=148 pairs=151552 ranks=[(0, 8), (1, 72), (2, 208), (3, 224), (4, 256), (5, 256)]
CENTRALIZERS_OK q=2 m=3 dim=12 classes=520 pairs=2129920 ranks=[(0, 16), (1, 272), (2, 800), (3, 960), (5, 1024), (6, 1024)]
CENTRALIZERS_OK q=3 m=1 dim=8 classes=273 pairs=1791153 ranks=[(0, 9), (1, 126), (2, 756), (3, 2754), (4, 2916)]
BRUTE_COMMUTATION_OK q=2 m=1 pairs=11776
VERIFY_OK
```

This finite experiment is corroboration, not a proof for every prime power or parameter. The general claim is established by a complete symbolic rank classification. Independent mathematical validation was not performed.
