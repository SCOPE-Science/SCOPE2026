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

With Python 3 and the accompanying `verify.py` and `octahedral_spines.json` in one directory, execute:

```
python3 verify.py octahedral_spines.json
```

The program is stand-alone and uses only the standard library. It reconstructs the complete simplicial face set and checks all eighteen 72-pair relative elementary-collapse certificates against the changing current complex, including all strict cofaces of each deleted free face. It also enumerates all minimal induced octahedral spines, their two dihedral orbits, and the signed simplicial Lefschetz traces for all twelve automorphisms. On the checked package inputs it completed with:

```
VERIFY_OK: F_VECTOR_12_48_74_36, CORES_18, COLLAPSES_1296, ORBITS_6_12, DIHEDRAL_CHARACTER
```

# Scope of the checks

The exact certificates establish the stated finite simplicial collapses, not a general theorem for other graphs. Identification with \(S^2\), the resulting integral homology, and the orientation character additionally use standard topological and representation-theoretic facts laid out in `RESULT.md`. The full-graph automorphism assertion follows from the triangle structure and outer hexagon, not from trusting a software automorphism database. No independent external audit has been carried out.
