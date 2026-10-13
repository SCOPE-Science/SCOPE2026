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

Run `python3 verify.py` in the directory containing this document and the standalone script, with Python 3.8 or newer. No third-party dependencies are required.

The checker directly builds prefixes of the binary words with ones at positive integral powers, enumerates distinct length-n factors modulo reversal (by the lexicographically smaller orientation), and compares the counts against the mathematically derived all-length summation and closed formula. It tests every length from 1 through 140 for bases 2 through 7, including the exceptional boundary at base 2 and length 4, as well as length zero.

The prefix length for each base is chosen large enough that every factor containing two or more ones of the tested lengths has already occurred; it also includes a zero run long enough to witness all zero-only and one-one words. This guarantees that the direct finite-prefix computation is complete for the tested lengths. It cannot establish the statement for untested lengths or arbitrarily large bases; those follow from the proof in `RESULT.md`.

The output ends with `VERIFY_OK` when all assertions succeed.
