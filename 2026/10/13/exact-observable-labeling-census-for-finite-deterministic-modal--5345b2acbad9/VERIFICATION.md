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

# Verification scope

The accompanying standalone `verify.py` uses only Python standard-library modules and directly tests the theorem against separate algorithms: finite deterministic trace-partition refinement, direct Boolean modal term closure under complements, unions and predecessor operators, and the graph-theoretic cycle/fiber constraints. It also independently enumerates all alphabet-valued labelings and compares their census with the closed product. Reproduce with `python verify.py`.

Observed successful output:

```
VERIFY_OK exhaustive_colorings 196579 full_census_graphs 7402 direct_boolean_modal_closures 26122 random_colorings 12000 rank_boundaries 9000 examples (24, 18)
```

Exhaustive coverage comprises all functions on sets of up to five elements for one and two colors, and functions on sets up to four elements for three and four colors. The direct modal-term closures are independently constructed for 26,122 colorings (small state sets, alphabets with at most three colors). Randomized checks use a fixed seed, 12,000 pairwise tests over graphs with up to 25 states. Boundary checks verify all 9,000 tested rank/feasibility comparisons. Examples recover 24 and 18 generating tuples respectively.

# Limits

Finite computation does not establish the universal theorem for all finite state sets and all generator counts. Correctness of the unrestricted formula, rank, and modal-depth claims is established by the proof in `RESULT.md`. No independent audit has been performed, and none is implied by the test method or the status data.
