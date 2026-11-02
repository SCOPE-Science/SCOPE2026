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

Run `python3 CHECK.py` with Python 3.10 or later from the directory containing the files. No third-party libraries are used. The exact stdout is `CHECK_output.txt`.

The program performs two independent conditions on every set partition of the \(2m\) cells for \(1\le m\le4\): direct closure of every pair of class sums by calculating all product coefficients, and equality of each class's complete row/column profiles. For \(m=5\), it enumerates all \(115975\) labeled set partitions of ten cells and applies the profile condition. In every accepted case it generates a subgroup of the actual rectangular-band automorphism group and checks its orbit partition against the Schur classes, and it separates counts by row-profile type. A separate weighted-Bell recurrence computes the expected exact counts through \(m=9\). The program ends with `VERIFY_OK` only if all assertions succeed.

These checks establish the listed finite counts and verify the implementing arithmetic, but they cannot by themselves prove the classification for all \(m\). The proof of the infinite assertion is the row/column profile argument in `RESULT.md`; the code is an independent finite consistency check. External independent auditing is not performed.
