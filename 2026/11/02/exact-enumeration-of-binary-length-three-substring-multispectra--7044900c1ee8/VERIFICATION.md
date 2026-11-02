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

The supplied `checker.py` uses Python standard libraries only. From the folder containing the files, run `python3 checker.py`.

The checker enumerates all eight-entry three-read occurrence vectors directly for every binary word at lengths 3 through 16, separately enumerates Euler-feasible arc-multiplicity vectors through 40 reads by three free integral coordinates and support connectivity, and compares the resulting integer coefficients against the rational generating-function identity through degree 40. It also checks the initial 21 exact counts.

The mathematical degree bound in RESULT.md is an essential part of the infinite proof: after exact symbolic support inclusion-exclusion, the polynomial multiplied by the explicit denominator has degree at most 28, so complete equality through degree 40 certifies the polynomial identity. Finite word checks alone would not prove an unbounded statement.

The independently audited status is not performed. Priority comparison remains qualified by inaccessible complete text of an expanded related 2012 paper.
