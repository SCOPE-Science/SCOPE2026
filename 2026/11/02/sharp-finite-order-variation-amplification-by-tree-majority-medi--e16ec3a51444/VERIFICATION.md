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
# Reproduction and limits

Execute `python check.py` with Python 3.10 or newer. No external dependencies are required. The test enumerates all labeled trees of orders 2 through 6 by Prüfer codes, all nonconstant binary vertex assignments on each, and independently checks the component deficit \(J_T(Mx)\le 2J_T(x)-c(F)\). Additional seeded tree samples with integer real-valued data cover orders 7 through 30; explicit constructions test attainment for orders 2 through 150.

Observed run: `PASS {'binary': 84346, 'trees': 1441, 'real': 4320, 'sharp': 149}`. The equality constructions were checked by exact rational ratios, not floating-point tolerance. The checker does not certify all trees or all real inputs; generality follows from the written proof, specifically the forest edge count and coarea identity. Inertia at degree-even vertices is essential to the strict flip condition; replacing it by another tie convention requires a new proof.

Independent scientific audit has not been performed.
