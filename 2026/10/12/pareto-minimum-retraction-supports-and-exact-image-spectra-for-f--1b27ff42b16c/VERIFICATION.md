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

# Reproducibility and checks

Run `python3 verify.py` using the Python 3 standard library. No network access, external packages, or research infrastructure are required.

Actual replay output:

```
VERIFY_OK 19 direct_shape_cases 23249 direct_function_tables 3658 bounded_maps 23249 direct_algebra_candidate_checks 5 larger_symbolic_support_checks example_320_endomorphisms_27_idempotents
ND_VERIFY_OK 6 three_modal_shapes 7022 direct_tables 28 bounded_maps
LARGE_EXAMPLE_OK 320 distinct_structural_maps_rechecked
```

For the 19 two-modal test shapes, the checker enumerates all 23,249 raw function tables and directly tests the two named bounded-morphism conditions by comparing successor sets, yielding 3,658 bounded maps. For these small shapes, it independently checks algebraic preservation of the two modal diamonds under inverse images, for all subsets and every raw function table. It compares the unrestricted and idempotent image polynomials and the per-component support multiplicities with the closed formulas. For six three-modal shapes, it enumerates 7,022 raw functions and detects 28 bounded maps by successor-set equality.

The ten-world example is too large for brute enumeration over all raw functions. Instead, the checker enumerates all possible componentwise coordinate surjections from the proven structural normal form, producing 320 distinct functions. Every one is then independently rechecked against the original relational successor-set conditions and idempotence, giving the stated polynomials. The proof, not this normal-form enumeration by itself, establishes that no additional bounded morphisms exist.

Checks are deterministic and exact (integer arithmetic and finite sets). These computational confirmations do not constitute independent mathematical review, nor do they establish a general theorem without its argument.
