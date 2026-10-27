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

The all-size result is proved by decomposition of downset/upset extension profiles; finite computation does not establish its infinite quantifiers.

To reproduce the finite checks, run `python3 verify_series_parallel.py`. This constructs strict order relations for all binary series/parallel expressions on consecutively labelled leaves through six vertices, checks all ternary new-point comparison profiles against transitivity, and counts downsets independently by subsets. It also checks 260 pseudorandom expression trees on 7–10 vertices, with a fixed seed, and the empty and four-element diamond cases.

The attached `verification_output.txt` records the actual run. It reports 1, 2, 6, 22, 90, and 394 distinct strict orders generated at sizes 1–6; 260 sampled larger instances; the diamond pair `(6, 18)` of ideals and types; and `ALL_TESTS_PASS`.

Limitations: the exhaustive coverage is over the specified expression convention rather than all relabellings, and higher sizes are sampled, not exhaustive. The proof, not finite enumeration, validates arbitrary decompositions. Independent audit has not been performed.
