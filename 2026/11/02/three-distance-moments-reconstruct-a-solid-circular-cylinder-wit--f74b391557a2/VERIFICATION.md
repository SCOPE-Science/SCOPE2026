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

# Verification and reproducibility

Run `python3 verification.py` with Python 3, SymPy, and NumPy. The file is standalone and uses only standard-library packages plus those two named dependencies. It checks the exact polynomial relations symbolically; the rational witness using integer fractions; and seeded direct point sampling in three right circular cylinders. The actual package-specific execution returned `EXACT_FORWARD_MOMENTS_AND_GLOBAL_INVERSE_PASSED`, `SHARP_TWO_MOMENT_AMBIGUITY_PASSED`, `DIRECT_INDEPENDENT_CYLINDER_SIMULATION_PASSED`, and `ALL_CHECKS_PASSED`.

The symbolic checks verify stated identities for indeterminates but do not substitute for the geometrical derivation of the disk and interval moments, which is provided in RESULT.md. The numerical checks compare empirical moments only in selected finite samples; they are **not proofs** of the global theorem, uniqueness, or sharpness. The proof holds for all real positive radii and heights and does not depend on those samples. These checks do not constitute independent mathematical audit.
