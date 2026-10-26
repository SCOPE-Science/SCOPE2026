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

# Reproducible verification

Run `python3 verify_convex.py` using standard-library Python 3. The checker performs Gaussian elimination in exact fractions; for each active pattern in dimensions two through eight it recomputes the orthogonal projector, matrix symmetry, idempotence, and absolute row norms. It verifies the precise five-by-five rational matrix, the active-set and center-row uniqueness, and a finite perturbation attaining the sharp 11/7 amplification. It also checks that the five-observation face embeds with unchanged row norm in lengths five through eight.

Expected result: `PASS 13069 exact-rational assertions`. These tests are finite evidence only; the proof in RESULT.md establishes the universal lower bound and the global five-point result. The source priority assessment is not independently audited.
