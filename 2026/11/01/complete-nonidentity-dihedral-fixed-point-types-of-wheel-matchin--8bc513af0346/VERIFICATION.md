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
# Reproduction and scope

Execute `python3 VERIFIER.py` from the directory containing that file. It requires Python 3.9+ and no third-party packages. The program constructs the wheel's edge set and all edge orbits under each dihedral element, discards orbits with incident edges, derives the conflict graph, and compares its component invariants with the four theoretical graph families. It separately enumerates full matchings and independently reconstructs invariant matching faces for the smallest instances; it also computes reduced mod-two homology ranks from direct simplicial boundary matrices of the path and cycle templates.

Actual completed output:

```
PASS: 4080 nonidentity dihedral orbit graphs match all four families
PASS: 105 independently enumerated fixed-matching face sets
PASS: 28 template mod-2 boundary-rank tests
```

These are finite computational checks. In particular, mod-two homology cannot detect integral torsion in general and cannot prove a statement for all widths. The all-width result instead follows from the orbit-barycenter lemma, the explicit rotation/reflection orbit classification and established path/cycle-independence homotopy results recorded in `RESULT.md`. A separate external mathematical review has not been performed.
