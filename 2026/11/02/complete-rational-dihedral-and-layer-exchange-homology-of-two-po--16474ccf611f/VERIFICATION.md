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

# Reproducible checks

All checker scripts run with the Python 3 standard library and use only the included `code` directory. Commands from the root directory of this package:

```
python3 code/prism_chain.py
python3 code/prism_h1_character.py
python3 code/prism_character.py
python3 code/prism_core.py
```

The chain checker constructs integer boundary columns of the unordered discrete two-particle CW model. It checks both boundary ranks modulo characteristics 2, 3, and 5 at each size from five to twelve and their consistency with the stated homology ranks. The homology-action checker independently computes the quotient of one-chains by the image of the second boundary modulo 1009, reconstructs the representation trace, and checks the formula for every dihedral and layer-switch symmetry for sizes five through ten. The group-character checker tests every group element, the exterior-square decomposition and three quotient character averages for widths five through eighteen. The signed-fixed-cell script independently computes the cellular traces of the displayed group actions. These finite calculations do not by themselves prove the general theorem, integral torsion-freeness, or bibliographic originality. Universal assertions use the proof in RESULT.md.

Independent audit: not performed.
