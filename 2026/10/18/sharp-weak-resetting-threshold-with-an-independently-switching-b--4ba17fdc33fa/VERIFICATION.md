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

The exact derivative follows from two coupled backward boundary-value problems and their derivatives at zero resetting. The full computation and the strict endpoint-series comparison appear in RESULT.md.

Run `python verify.py` using NumPy and SciPy. It independently builds the finite-state generator of a reflecting nearest-neighbor walk with a Markov-switched absorbing/reflecting left endpoint. Crucially, the jump-to-reset-location operator preserves the gate state. Two sparse resolvent solves yield the derivative at zero, extrapolated from two lattice meshes.

Executed result: `PASS 193 numerical checks; root thresholds in (0.422649730810,0.552786404500).`

These checks are finite-dimensional approximations and do not independently certify the all-parameter analytic theorem. The strict endpoint inequalities and unique-crossing argument are proved in RESULT.md. Independent external review has not been performed.
