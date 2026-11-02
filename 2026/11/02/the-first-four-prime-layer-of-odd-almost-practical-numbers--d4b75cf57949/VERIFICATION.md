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

# Reproducibility and limitations

Run `python3 verify.py` from the directory containing the extracted files. The verifier uses only Python's standard library, two independent exact algorithms for subset-sum membership, and integer-divisor enumeration. Recorded output:

`VERIFY_OK bases=4 base_holes315=9 two_block_t=1..104 boundary=103 positives=28 min=3465 max=32445`

The finite checks include independent bitset/Boolean methods, all integer shifts through the cutoff and first excluded shift, all five special-case induction certificates, and every listed positive example. The infinite cutoff and universal exclusions follow from the explicit interval-coverage and missing-sum proof, not from testing a finite numerical range. There has been no independent mathematical audit.
