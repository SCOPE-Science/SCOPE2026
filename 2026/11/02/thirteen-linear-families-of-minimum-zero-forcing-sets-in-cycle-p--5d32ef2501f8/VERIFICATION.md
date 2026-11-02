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

# Reproduction and limits

Run the Python 3 files `prism_infinite_certificate.py`, `prism_direct_check.py`, and `prism_symbolic.py` with no additional dependencies. The first checks all 25,013 reduced cyclic cases (weights one through four), fort-matrix stabilization after five empty columns, all-orbit matches, and finite cyclic exchange data. The second independently uses the ordinary color-change rule and exhaustive four-subset enumeration on cyclic lengths six through fifteen. The third checks all possible single-exchange neighbors on integer-lifted local templates, yielding degrees 12, 8, 8, 8, 5. The mathematical proof supplies the implication from the local certificate to every length, and explicitly accounts for short-wraparound cases. The scripts provide reproducible exhaustive finite computations; they do not independently constitute a formalized proof of that implication. The result has not undergone independent scholarly audit.
