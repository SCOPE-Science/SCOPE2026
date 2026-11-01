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
# Computational verification

Run `python3 verify.py` in the extracted package. The standard-library program independently evaluates the projection formula, Jacobian absolute row sums, and finite differences. It reports 8,020 successful assertions in spatial dimensions one through twenty, and prints the first sharp constants. All-dimensional sharpness and the dimension-five threshold are justified analytically in RESULT.md; randomized or finite tests are not a proof. The checker makes no claim of independent or external certification.
