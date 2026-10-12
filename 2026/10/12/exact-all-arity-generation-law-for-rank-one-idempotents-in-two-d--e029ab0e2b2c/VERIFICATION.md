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

Execute `python verify.py` using Python 3 (standard library only). The program constructs every rank-one idempotent from an ordered image/kernel pair and directly closes the matrix-span of each selected tuple under multiplication; this is separate from the line-intersection formula it also computes. The \(\mathbb F_4\) implementation uses the polynomial \(z^2+z+1\).

The exact independent enumeration (\(q,r;\) total, generating) is:

| \(q\) | \(r\) | Total tuples | Generating tuples |
|---:|---:|---:|---:|
| 2 | 1 | 6 | 0 |
| 2 | 2 | 36 | 0 |
| 2 | 3 | 216 | 48 |
| 2 | 4 | 1296 | 576 |
| 3 | 2 | 144 | 24 |
| 3 | 3 | 1728 | 912 |
| 4 | 2 | 400 | 120 |
| 4 | 3 | 8000 | 5520 |
| 5 | 2 | 900 | 360 |
| 7 | 2 | 3136 | 1680 |

The executable returns `VERIFY_OK`; for every listed instance the independent algebra-closure result equals both the invariant-line test and the claimed formula. This exhaustive verification does not quantify over all finite fields or all tuple lengths, and no claim of external validation is made. The written proof supplies the general quantifiers.
