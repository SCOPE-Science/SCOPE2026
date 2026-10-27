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

# Verification scope

The analytical covariance derivation in `RESULT.md` proves the current and the strict-convexity optimization. The accompanying standard-library-only script `check_heat.py` constructs the stationary \(4\times4\) covariance equations in exact rational arithmetic, compares the heat current in three independent forms with the rational closed expression in eight cases, and tests the unique optimizer against finite numerical comparison grids in six further cases.

Executed check: `python check_heat.py` returned `PASS: 8 exact-rational stationary covariance/current checks, 6 optimality grids`.

This computation corroborates, but does not logically establish, the universal theorem; existence, uniqueness, strictness, and asymptotics follow from the written proof. Statistical estimation, finite-noise robustness, non-Ohmic baths, and quantum corrections have not been verified. Independent scientific audit has not been performed.
