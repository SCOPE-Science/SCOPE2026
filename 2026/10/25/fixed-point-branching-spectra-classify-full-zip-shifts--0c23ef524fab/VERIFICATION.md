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

# Verification

Run the adjacent standalone file `verification.py` with standard Python 3; no external dependencies or network calls are needed. The recorded run reported:

```
N=2: 3 surjections, 2 conjugacy classes
N=3: 13 surjections, 3 conjugacy classes
N=4: 75 surjections, 5 conjugacy classes
N=5: 541 surjections, 7 conjugacy classes
N=6: 4683 surjections, 11 conjugacy classes
PASS: 5315 onto transition maps, 28 partition classes, 23 exact finite-window conjugacies.
```

This exhausts only the stated finite alphabets up to six symbols. The code checks the identity for the fixed-point inverse-degree spectrum, the partition-class census, and the explicit \(\alpha,\beta\) commuting relation on finite windows. It cannot certify uniqueness under arbitrary homeomorphisms on an infinite product; that is proved by conjugacy invariance of inverse-degree at fixed points in RESULT.md. It likewise does not independently certify bibliographic originality.
