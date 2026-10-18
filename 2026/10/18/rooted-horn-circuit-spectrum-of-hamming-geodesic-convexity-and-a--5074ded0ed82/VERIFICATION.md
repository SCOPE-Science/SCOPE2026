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

# Computational verification and proof boundaries

Run the standalone Python 3 standard-library program from the same directory:

`python3 verify.py`

A successful execution yielded:

```
CASE 2 2 per_root {2: 1} direct_unit 4 PASS
CASE 3 2 per_root {2: 6, 3: 1} direct_unit 56 PASS
CASE 4 2 per_root {2: 25, 3: 22, 4: 1} direct_unit 768 PASS
CASE 2 3 per_root {2: 4} direct_unit 36 PASS
CASE 3 3 per_root {2: 36, 3: 64} direct_unit 2700 PASS
CASE 2 4 per_root {2: 9} direct_unit 144 PASS
CASE 3 4 per_root {2: 108, 3: 729} direct_unit 53568 PASS
VERIFY_OK cases=7 independent_subset_hulls= 984 direct_stem_counts=PASS extremal_counts=PASS
```

The program enumerates candidate row sets, tests matching of every coordinate, independently checks deletion minimality, and compares the counts with the proposed inclusion–exclusion expression. In small configurations it recomputes hulls by iterating graph intervals, rather than assuming their rectangular shape. Those bounded checks do not imply correctness for all parameter values. The general proof relies instead on the private-coordinate characterization, inclusion–exclusion, and a direct necessity argument for unit Horn rules. Classical binary minimal-cover enumerations are prior known results and are not new numerical certificates.
