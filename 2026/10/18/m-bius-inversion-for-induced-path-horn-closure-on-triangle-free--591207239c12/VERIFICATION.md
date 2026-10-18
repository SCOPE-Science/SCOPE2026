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

The standalone Python 3 program `verify.py` reconstructs the induced-path Horn hull, the edge-induced closure, all closed edge sets, and each interval Möbius value via the defining lattice recurrence. It compares every value to the stated independence-polynomial formula. The program needs only the Python standard library and runs with `python3 verify.py`.

Reproduced output:

```text
TRIANGLE_FREE 2 graphs 2
TRIANGLE_FREE 3 graphs 7
TRIANGLE_FREE 4 graphs 41
TRIANGLE_FREE 5 graphs 388
TREES 6 random 60
TREES 7 random 60
TREES 8 random 60
TREES 9 random 60
VERIFY_OK graphs 678 intervals 215512 max_concepts 151 triangle_free_hull=PASS mobius_formula=PASS forest_bound=PASS triangle_boundary=PASS
```

The 678 checked graphs include all 438 labeled triangle-free graphs of orders two through five plus 240 deterministically sampled trees on six through nine vertices, and 210,708 examined lattice intervals. This is finite corroboration, not a substitute for proof or independent external validation. The triangle counterexample is explicitly checked.
