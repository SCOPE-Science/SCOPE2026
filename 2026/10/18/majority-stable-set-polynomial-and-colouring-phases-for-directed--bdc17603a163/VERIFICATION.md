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

# Reproduction and proof boundary

Use `python3 verify.py` with standard Python 3 and no third-party dependencies. The script computes the polynomial recurrence, direct weighted occupancy sums, exhaustive labelled vertex-subset counts in small cases, leading coefficients, and all two-colourings via red-count occupancies. It printed:

`VERIFY_OK: 72 recurrence/top/colour checks across 24 parameter pairs; 14 exhaustive labeled-subset checks; no proof inferred from finite tests`

The exact ranges were \(3\le d\le8\), \(1\le m\le4\), with labelled-set enumeration only if \(dm\le14\). All assertions passed. These are finite checks and do not establish the infinite claims. The general proof instead follows from the two-state layer transfer identity, disjoint-pair cardinality inequality, complete extremizer classification, and automorphism averaging. This check does not constitute independent validation.
