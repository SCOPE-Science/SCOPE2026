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

The checker constructs \(H_n\) for \(2\le n\le9\), computes all-pairs distances, and exhaustively tests every subset up to the claimed minimum size. It compares the complete minimum-set family with the parity classification.

Recorded output:

```text
VERIFY_OK
n=2: md=1, bases=2
n=3: md=3, bases=6
n=4: md=3, bases=2
n=5: md=5, bases=12
n=6: md=5, bases=2
n=7: md=7, bases=20
n=8: md=7, bases=2
n=9: md=9, bases=30
subsets_checked = 193979
all minimum bases matched the parity classification
```

The checker examines \(193{,}979\) candidate subsets. The finite enumeration is corroborative only; the arbitrary-\(n\) result follows from the exact representation formulas and block proof.
