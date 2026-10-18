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

# Verification and reproducibility

The standalone program `check_cyclic4_sections.py` requires Python 3 and only its standard library. Running it against the embedded source file gives:

```text
CYCLIC4_SECTION_FACETS_OK exact_Gale_vs_cycle_n=5..14 exhaustive_admissible_words=6894 moment_curve_determinants=2310 larger_direct_counts=478
```

The checker tests combinatorial tetrahedral facets against Gale parity, supporting-determinant geometry, exhaustive admissible sign patterns in a bounded range, explicit polynomial realizations, and further reproducible larger-size checks. This is reproducibility evidence, not an independent audit or a proof for every size. The all-size result rests on the edge-pair count and optimization proved in `RESULT.md`.

The theorem covers all distinct increasing real moment-curve vertex parameters. The complete generic equality classification is for \(n\ge7\); the finite base cases \(n=5,6\) are handled separately. Independent audit has not been performed.
