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

# Reproducibility

Execute `python verify.py` using Python 3.10+ and the standard library. This independently constructs point sets, every two-point box, all nonclosed-pair implications, and exact Cartesian bounding-box closure.

Exhaustive initial subsets: grids (2), (3), (2,2), (3,2), (2,2,2), (3,3), and (2,2,2,2); respectively 4, 8, 16, 64, 256, 512, and 65,536 candidates. Recursive pseudo-intent identification is independently repeated for the first six. Additional 3,000 seeded samples each test (3,2,2) and (2,2,2,2,2). Unit-vector sharpness configurations are verified in dimensions 2 through 6.

Observed: (2,2,2) has 16 rules and a round histogram (28,212,16); (2,2,2,2) has 88 rules and round histogram (82,61838,3616). The checker ends with `VERIFY_OK grid_closure=PASS pseudo_intent_characterization=PASS exact_minimal_rule_count=PASS exact_parallel_depth=PASS`.

The computation is finite and cannot certify the universal theorem, which rests on the proof in RESULT.md. No external independent audit has been performed.
