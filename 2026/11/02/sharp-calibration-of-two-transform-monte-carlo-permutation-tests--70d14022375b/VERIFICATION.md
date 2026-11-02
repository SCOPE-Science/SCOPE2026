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

The accompanying standalone script `verify_two_transform.py` computes exact rational rejection probabilities by enumerating permutations of finite cycle score ranks and all binary transformation-resampling strings. It checks cycle lengths 2–6, resampling counts 1–4, and identity masses 0, 1/4, 1/2, 3/4, 1. It compares direct enumeration against the exact binomial formula for each support threshold and checks extremal constructions and the validity reversal at identity mass 27/100. It also tests the key finite identity-mass inequality over a larger grid of cycle lengths and budgets. The actual execution completed with 78,579 passing deterministic checks.

The proof in RESULT.md verifies the arbitrary-cycle and all-budget quantifiers analytically. Numerical/enumerative tests do not certify unseen infinite cases. Literature comparisons are not independent priority certification. The theorem does not include arbitrary many-transform or dependent resampling distributions. Independent mathematical audit has not been performed.
