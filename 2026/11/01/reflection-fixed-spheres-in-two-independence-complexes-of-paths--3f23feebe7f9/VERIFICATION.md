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

# Reproducibility and limits

Run Python 3 without external packages from the directory containing the extracted `verification` folder:

```
python verification/check_reflect_ind2.py
python verification/check_reflect_ind2_morse.py
```

Observed after executing both bundled programs: the direct orbit-complex and local forbidden-rule face families agreed at each path length from 1 through 25; the reduced mod-two Betti numbers agreed for path lengths 1 through 21; the explicitly defined augmented Morse matching had precisely the predicted critical faces and no directed Hasse cycles for all boundary-complex sizes 1 through 14. The orbit-face program reports 8,900 admissible orbit subsets across the tested sizes. No random assumptions or library dependencies are used.

The scripts do not establish correctness for arbitrarily many vertices and do not check integer torsion in unbounded dimensions. Those conclusions follow from the explicit infinite discrete-Morse proof and elementary orbit-barycenter identification. Only the self-review documented in REVIEW.md has been performed. Independent auditing has not occurred.
