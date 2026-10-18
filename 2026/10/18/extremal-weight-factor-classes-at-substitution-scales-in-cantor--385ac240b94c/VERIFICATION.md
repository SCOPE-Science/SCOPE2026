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

# Reproducibility and verification

Run `python verify.py` with Python 3. No additional packages are required. The program constructs the word by repeated uniform substitution and independently by a digit predicate, then directly enumerates distinct factors at lengths \(q^k\) and \(2q^k\).

For every \(3\le q\le8\) and \(0\le k\le3\), the program checks the full predicted factor set, its published-style total cardinality, both maximum one-counts, the unique length-\(q^k\) maximizer, and the complete length-\(2q^k\) maximizing set and its cardinality. Actual execution yielded `VERIFY_OK cases=24; substitutions and digit formula agree; exact factors, maxima, and all extremizers agree`.

These finite tests do not certify the theorem for unbounded parameters. The infinite claim rests on the full block decomposition and disjointness proof in `RESULT.md`. Every symbol of the comparison prefixes is generated anew; no hidden data or external dependencies are used. Independent scientific review has not been conducted.
