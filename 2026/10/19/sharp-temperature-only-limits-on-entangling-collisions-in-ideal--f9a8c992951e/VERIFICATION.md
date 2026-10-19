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

Running `python3 CHECK.py` in the directory containing the embedded files produces `PASS: 1302 independent exact-rational and matrix assertions`. The checker requires only Python 3's standard library. It explicitly constructs each collision unitary and four-by-four joint state independently of the scalar recurrence, checks partial-transpose determinants, and compares signs against exact rational expressions for a range of bath populations, interaction angles, and collision indices. It also verifies sample near-identity sharpness and zero-temperature endpoints.

The universal theorem is analytical: diagonal preservation by the ideal gates, the partial-transpose determinant, a single positive quadratic root, and logarithmic bounds prove the results for the continuum of parameters and all positive integer collision indices. Matrix and numerical spot checks are corroboration, not an exhaustive proof. The result concerns only pre-reset target–ancilla entanglement of freshly reset qubits. The uninspected supplemental parts of the motivating paper leave a residual priority-comparison risk.
