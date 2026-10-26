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

# Verification record

The proof differentiates the exact finite-depth inviscid dispersion law and establishes strict global derivative monotonicity. It then proves the inverse map is a strictly increasing bijection on \(x\in(0,\infty)\) with image \((0,2/3)\). These are analytical, not computational, steps.

The standalone `CHECK.py` executes representative independent bounded optimization of the forward dispersion and inverse reconstruction. It verifies 76 parameter sets with non-extreme \(k_*H\) and 63 constructed observation pairs across the realizable interval; extreme-depth inverse ill-conditioning limits double-precision experiments. Passing numerical tests are finite supporting checks, not an exhaustive proof. Results for unequal depths, viscous damping, finite-amplitude dynamics, experimental uncertainty, and originality in uninspected historical text have not been established. Independent audit has not been performed.
