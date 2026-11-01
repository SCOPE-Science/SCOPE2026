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

# Verification of the join polynomial

Use Python 3 and run `python verify.py` in the extracted package directory; no external modules are required. The program constructs labeled graphs and complete joins, directly enumerates assignments from \(\{0,1,2\}\), checks that each zero has a neighboring two, and tests whether reducing any single positive coordinate yields another valid Roman function. It does not use the theorem's structural classification when computing the direct polynomial.

The program compares complete coefficient dictionaries indexed by the number of two-labels and total weight, including equal-degree collisions and boundary cases with one-vertex factors. The deterministic test covers all pairs of graphs with each shore size from one to three, together with 160 larger pseudo-random pairs with shore sizes up to four. A successful direct execution gave:

`VERIFY_OK join_pairs=281 direct_join_assignments=331245`

A finite exhaustive check over a specified range cannot prove an all-order identity. The mathematical proof in `RESULT.md` supplies the infinite argument. Independent mathematical audit has not been performed.
