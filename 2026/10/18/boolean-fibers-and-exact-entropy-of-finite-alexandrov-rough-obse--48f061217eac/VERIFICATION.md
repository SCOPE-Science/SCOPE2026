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

# Reproduction and boundaries

Run `python verify_fibers.py` with Python 3.9 or later and no external dependencies. It independently derives Alexandrov lower/upper approximations from each transitive relation and computes every subset's observation. It then compares every resulting fiber to its predicted Boolean interval (checking the complete set of representatives, not just the fiber size).

The enumerated posets include all transitive relations respecting the natural linear extension on up to six points. This covers every finite poset of those sizes up to relabeling, although it does not enumerate every labelled order in every labelling. The script tests 6,231 posets in total, including 1,000 seeded cases with seven through ten points; it tests 324,180 realized fibers. Separately it checks all 389 finite preorders on one through four points for the Boolean-interval/\(T_0\) equivalence. It calculates exact uniform and Bernoulli-\(1/3\) expected free dimensions with rational arithmetic and compares them to the stated degree formulas.

Observed completion marker:

```text
VERIFY_OK preorders 389 sorted_posets_and_samples 6231 realized_fibers 324180 all_boolean_cubes=PASS uniform_and_biased_entropy=PASS non_T0_boundary=PASS
```

The mathematical proof in `RESULT.md` establishes the theorem for arbitrary finite posets; no finite experiment establishes this universal quantifier. The preorders test and the three-point equivalence-class example show that the \(T_0\) requirement is substantive. The entropy identity holds for independent Bernoulli draws, not arbitrary correlated subset distributions. An independent external scientific audit has not been performed.
