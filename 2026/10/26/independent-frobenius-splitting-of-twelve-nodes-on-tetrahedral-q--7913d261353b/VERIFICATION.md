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

# Verification

Run the included standalone program with `python3 verify.py`. The program uses Python's standard library and prints `VERIFY_OK` on success.

Checks actually performed: arithmetic of the trace classes and square maps for fields of sizes 2, 4, 8; exhaustive enumeration of every one of 59,049 allowed presentations over the four-element field; agreement of all 64 labeled splitting-mask frequencies with the closed formula; direct projective-singular-point counts for one representative of each mask over the four- and eight-element fields; and the sole allowed presentation over the two-element field.

The observed count distribution over the four-element field, grouped by 0, 2, 4, 6, 8, 10, 12 rational nodes respectively, is `5184, 15552, 19440, 12960, 4860, 972, 81`. These finite checks do not establish the universal geometric/node statements, which are proved separately by explicit gradients, edge quadratics, and local tangent cones. The zeta quotient uses the standard rationality of smooth conics over finite fields, and no independent audit or outside certification has been performed.
