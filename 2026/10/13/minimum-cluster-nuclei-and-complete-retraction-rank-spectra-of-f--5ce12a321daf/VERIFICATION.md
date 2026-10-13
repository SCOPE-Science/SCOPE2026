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

# Finite, independently coded structural checks

Run the accompanying standalone source file with `python3 verify.py`. It uses only the Python standard library, has no external dependencies, and never reads an external corpus or ledger.

For sixteen explicit equivalence-cluster profiles, with total frame sizes at most six, the program enumerates **all point functions** and tests each one by direct successor-set equality. It independently computes the proposed endomorphism spectrum using Stirling-surjection counts and inclusion–exclusion, and the proposed idempotent spectrum using the anchor-cluster product; it then compares full rank distributions and all retraction-support sets. For profiles with at most five points, each accepted bounded map is also checked algebraically against every truth subset for preservation of modal saturation under inverse image. The script does not assume the formulas are correct when screening point functions.

Its completed replay produced:

```text
VERIFY_OK {'shapes': 16, 'candidate_tables': 197086, 'bounded_maps': 1059, 'direct_algebra_subset_checks': 10874, 'rank_checks': 48}
```

The test list includes unequal class sizes, equal class sizes, singleton classes, a single cluster, all-singleton frames, and the mixed profile \((1,2,3)\). The direct tests confirm \(39\) bounded endomorphisms and \(10\) idempotents for that mixed profile. All computations use exact integers. The test does not claim exhaustive verification beyond these finite profiles, does not independently establish mathematical novelty, and does not replace the universal proof in `RESULT.md`.
