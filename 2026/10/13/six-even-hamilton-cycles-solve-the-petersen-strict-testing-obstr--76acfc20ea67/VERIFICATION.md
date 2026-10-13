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

# Reproducibility and boundaries

Run `python3 verify.py` (Python 3 standard library). The run checks the six even five-cycles, all fifteen matching pairs and eight outsider edges per pair, and validates Sperner's obstruction to five pools. It then checks every defective subset among sixteen items for the five-first-pool construction, and every subset of at most four defectives among twenty-six items for the six-first-pool construction.

Expected summary is `VERIFY_OK petersen_min=6 two_stage_m5=65536 two_stage_m6_weight_le4`.

The all-size conclusion is established in the written proof by the orbit-based local lemma and the complete case analysis for the number of positive first-stage tests. The finite checker does not attempt a complete search for all alternative optimal designs, and exhaustive tests on small instances alone are not a proof for arbitrary pool count. Independent audit has not been performed.
