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

# Finite reproducibility and limits

Run `python3 checker.py` in the directory containing the embedded verification file. Python 3 standard library is sufficient.

The program enumerates all partial injections for \(1\le n\le6\) and all integer partitions representing permutation cycle types; it compares the complete rank distribution at every permissible nilpotency-index bound against an independently computed integer path recurrence. It further enumerates the equivariant partial injections of four two-cycles directly on eight points, verifying the complete \(361\)-element nilpotent distribution by actual composition and index computation. Several cycle-class sizes and nilpotency bounds are tested for exact rank support and maxima. Expected final stdout line: `VERIFY_OK`.

All checks were executed on the packaged `checker.py` and returned the expected result. These finite tests are not an exhaustive verification of arbitrary \(n\). The general mathematical proof rests on the cyclewise equivariant reduction, the directed-path decomposition, the labeled exponential formula, and the elementary path-length realizability criterion. Bibliographic novelty outside the inspected source portions remains subject to fuller external comparison.
