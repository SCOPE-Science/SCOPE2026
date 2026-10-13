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

The symbolic proof in `RESULT.md` is the primary evidence. The standalone `verify.py` is an independent finite replay of the definitions: it constructs \(\operatorname{Cr}_n\), enumerates all vertex subsets for \(5\le n\le9\), computes the closed-neighborhood traces directly, finds every minimum identifying code, and checks both the structural characterization and the exact count.

Replay command:

`python3 verify.py`

Expected output:

`VERIFY_OK n_range=5..9 subset_checks=349184 basis_checks=3538 max_order=18`

The finite range does not certify the theorem for larger \(n\); the all-\(n\) conclusion rests on the explicit trace proof. The literature comparison does not treat the inaccessible body of the 2020 same-object paper as having been inspected.
