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

# Reproducibility checks

Using Python 3, run `python3 verify_top_choice.py top_choice_depth10_certificate.json` and `python3 independent_top_choice.py`. Both use only Python's standard library. The complete finite-depth certificate is included and is checked on all internal nodes, terminal witnesses and Boolean branches.

Verified results include `DISTINCT_CONCEPTS_PASS 2520`, `VC_SIX_OBSTRUCTION_PASS nodes 286503`, `VC_FIVE_WITNESS_PASS 32`, `LITTLESTONE_DEPTH_TEN_TREE_PASS internal 1023 leaves 1024`, `LITTLESTONE_DEPTH_ELEVEN_OBSTRUCTION_PASS 840 1024`, and `TERNARY_CHOICE_ALL_CHECKS_PASS`. The independent program confirms the static dimensions on three through seven alternatives and the exact finite adaptive depths through six.

The finite check does not establish a result beyond the stated query class or certify historical uniqueness. The full-text status of the Kalai source is a scholarly priority limitation, not a substitute for mathematical verification. Independent audit has not been performed.
