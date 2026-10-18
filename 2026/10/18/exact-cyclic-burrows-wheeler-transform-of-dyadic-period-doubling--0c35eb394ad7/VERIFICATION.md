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

A complete proof of the infinite-family transform recurrence appears in `RESULT.md`. To repeat the finite cross-checks, run `python3 check_bwt.py` (Python 3 standard library only) in the directory containing the files. The script compares the complete predicted cyclic transform with an independently computed cyclic rank-doubling transform through \(m=13\); through \(m=9\), it also compares with an explicit lexicographic list of all cyclic rotations. All assertions were executed successfully.

The code verifies finite instances, not the induction for every \(m\). The cited primary literature provides context for general logarithmic bounds and related morphism properties; it is not used as an unproved lemma in the proof. This work has not received an independent external audit.
