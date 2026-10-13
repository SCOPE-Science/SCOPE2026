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

# Finite verification

From a directory containing all three standalone attachments, run `python3 verify.py` and `c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`. Python checks all 65,536 masks by both direct signature comparison and separation-set transversals; it also checks the 88-constraint reduction, the 96-automorphism enumeration, and all orbit representatives against the CSV. C++ reconstructs the same graph independently and performs a complete direct-signature census.

Observed outputs:

```text
VERIFY_PY_OK GP(8,3) vertices=16 edges=24 bipartition=8+8 constraints=136 minimal_constraints=88
VERIFY_PY_OK every_mask=65536 signatures_and_hitting_agree minimum=8 minimum_codes=584
VERIFY_PY_OK polynomial=8:584,9:3840,10:5440,11:3888,12:1780,13:560,14:120,15:16,16:1
VERIFY_PY_OK min_bipartition_profiles=(0, 8):2,(1, 7):48,(2, 6):72,(3, 5):192,(4, 4):270
VERIFY_PY_OK automorphisms=96 optimum_orbits=13 orbit_sizes=2,6,24,24,48,48,48,48,48,48,48,96,96
VERIFY_CPP_OK vertices=16 all_masks=65536 minimum=8 minimum_identifying_codes=584 polynomial=8:584,9:3840,10:5440,11:3888,12:1780,13:560,14:120,15:16,16:1
```

The domain is finite and the loops cover it exhaustively. This verifies the given finite graph only; the checks do not establish external historical priority, publication acceptance, or an independent audit.
