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
# Verification notes

The theorem applies to every \(n\ge4\) and every subgroup of the standard dihedral action. Its complete proof is in `RESULT.md`; the finite checker is additional reproducible evidence, not the all-size argument.

Execute `python verify_reflection.py` with Python 3 and no third-party packages. The actual packaged script was executed successfully before acceptance, producing:

```
ORBIT_GRAPH_OK n=4..120, both reflection classes
FIXED_HOMOLOGY_OK n=4..18, both classes, exact augmented GF(2) boundaries
AMBIENT_HOMOLOGY_OK n=4..9, source homology dimensions corroborated
LOW_BOUNDARY_OK n=3, one S^0 and one empty fixed space
ALL_SUBGROUPS_OK 4711 direct subgroup orbit-graph comparisons
VERIFY_OK
```

The checker directly forms permutation-group vertex orbits, omits internally adjacent orbits, and compares all resulting quotient edges to the claimed exact graph models. It separately constructs augmented simplicial boundary matrices over \(\mathbb F_2\) for independently enumerated fixed-space faces and verifies their reduced homology. Computations for finitely many parameters do not establish the unrestricted theorem. Its all-size proof relies on the orbit-classification argument, the two graph folds, and the previously published nonequivariant result. This is not an independent audit.
