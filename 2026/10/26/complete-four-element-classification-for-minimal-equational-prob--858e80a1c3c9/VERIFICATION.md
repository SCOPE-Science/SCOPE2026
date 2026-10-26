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

# Reproduction and limits

Execute `python3 verify.py` from this directory. The standalone program uses Python's standard library only. It enumerates every four-row Latin table from the 24 row permutations, rejects repeated entries within any column, and calculates all simultaneous-relabelling orbits. It then applies the four necessary equations, identifies the surviving canonical sets with the explicit finite-field affine models, and verifies the labeled-table count.

Actual run output:

```
VERIFY_OK latin=576 latin_isotypes=35 qualifying_latin=30 qualifying_quasigroup_isotypes=5 non_latin_isotypes=5 all_isotypes=10 labeled_minimal_groupoids=52
affine_coefficients= ((1, 1), (2, 1), (1, 2), (2, 2), (2, 3))
quasigroup_isomorphism_orbits= [2, 4, 8, 8, 8]
```

The code does **not** enumerate all term equations; the general affine-term argument in `RESULT.md` proves the spectrum restriction at arbitrary term depth. The exhaustive program establishes all finite cardinality assertions, contingent on its inspectable loops and relabelling implementation. No independent audit or formal verification was performed.
