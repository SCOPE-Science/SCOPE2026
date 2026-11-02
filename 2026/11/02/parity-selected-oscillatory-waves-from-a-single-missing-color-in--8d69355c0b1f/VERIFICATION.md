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

# Reproducibility

Run `python3 cyclic_defect_verify.py` with Python 3 and the standard library. Compare its output byte-for-byte with `cyclic_defect_verification_output.txt`. The program independently implements vertex-level successor-contact updating and detects least first-entry/period by trajectory recurrence; no external software is required.

The recorded checks are 2,046 support-time equalities at all predicted preperiodic times for \(3\le q\le64\), 4,692 distinct microscopic single-defect tests with color rotations and shore swaps for \(3\le q\le48\), and 145,231 exhaustive labelled configurations in five small graph/color cases. At alternating supports it checks primitive least period and the formula's exact labelled periodic-state count.

The proof of the result for unbounded \(q\) is the symbolic support induction and color-class permutation argument in RESULT.md; testing finitely many \(q\) cannot certify all \(q\). The conditional probabilistic limit is an exact occupancy inclusion-exclusion deduction, not a Monte Carlo claim. Historical source uniqueness and independent external audit have not been established.
