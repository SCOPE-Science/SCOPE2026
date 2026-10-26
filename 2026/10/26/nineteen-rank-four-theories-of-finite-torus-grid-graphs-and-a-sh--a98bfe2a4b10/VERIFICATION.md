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

The finite calculations can be reproduced with `python3 verify.py` next to `classification.json`, using only the Python standard library. The program independently enumerates four-variable atomic diagrams by (A) rooted triple-extension masks and (B) full ordered-quadruple diagrams generated from a separate graph representation. It evaluates all 45 unordered dimension pairs in the closed range 3 through 11, checks agreement of both partitions, and checks the exact 19-class table and 64-vertex minimum bound.

Recorded execution:

```text
FINITE_CENSUS_OK canonical_pairs=45 classes=19 implementations=2
CUTOFF_TABLE_OK 3:8 4:8 5:7 6:8 7:7 8+:8+
SHARP_BOUND_OK largest_least_representative=64 graph=C8_square_C8
SUPPLEMENTAL_OK instances=6
VERIFY_OK
```

The infinite reduction is mathematical: the published four-round cutoff for cycles, combined with a direct coordinatewise Cartesian-product game strategy, reduces every pair of dimensions to the 45 canonical cases. The software does not purport to prove the cited published cutoff; it proves the exact finite facts used with it. The six supplemental larger cases are consistency checks, not a substitute for the infinite proof.
