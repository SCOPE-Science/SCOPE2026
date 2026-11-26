---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verify.py` from this directory with Python 3.9 or newer. It finds the Fibonacci periods by first return of the residue pairs; applies the stated divisibility implications to one complete period of index classes; and verifies the counts and overlaps in the table, the prime-3 classes modulo 24, and the odd parity of all survivors. The program uses only integer arithmetic and the Python standard library. The Zeckendorf weight identities, even-index exclusion for the second shape, and reduction to a periodic predicate are proved separately in `RESULT.md`. The script does not check full divisibility of the terms or existence of runs.
