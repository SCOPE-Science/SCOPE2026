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

# Reproducibility and scope

The structural theorem is proved for arbitrary finite positive arity by the two implications in `RESULT.md`; no numerical computation is needed for the all-arity statements. The fixed-arity cardinality claim for three variables is supported by a separate exhaustive interval-poset test.

Run `python3 verify.py`. The expected output includes `arity=1 term_functions=4 disagreement_sets=4`, `arity=2 term_functions=82 disagreement_sets=256`, and `KLEENE_DISAGREEMENT_VERIFY_OK`. This exhausts the term-function closure at arities one and two, tests all possible two-variable disagreement subsets, exercises an explicit converse constructor and tests the definable infectious conditional's complete truth table.

Compile and run `g++ -O3 -std=c++17 verify_convex3.cpp -o verify_convex3 && ./verify_convex3`. The expected output is `three_variable_convex_disagreement_sets=3886222` followed by `TERNARY_CONVEX_CENSUS_OK`. The checker visits all \(2^{26}\) subsets of the ternary three-cube that avoid the all-unknown tuple, and tests each candidate against every nontrivial order interval, so the count is exhaustive. By the proved classification, this is also the number of realizable disagreement sets in that arity; the C++ checker itself does not enumerate syntactic formulas.

These programs check finite consequences and the construction but do not constitute a general proof or an independent formal verification. Independent audit has not been performed.
