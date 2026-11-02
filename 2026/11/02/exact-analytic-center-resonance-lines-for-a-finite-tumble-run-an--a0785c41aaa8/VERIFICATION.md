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

Execute `python verify.py` with SymPy installed. The program independently reconstructs the stationary generator identities for the total density and zero-velocity component. It compares exact moments of the operator-constructed distribution against the published hypergeometric moment formula for 15 integer-valued parameter combinations through moment order ten. It also tests two explicit examples and three off-resonance amplitudes. The actual packaged verifier passed 140 checks.

The all-real-rate and all-nonnegative-integer conclusions depend on the analytic moment-determinacy and gamma-residue proof in RESULT.md. A finite program cannot establish those universal assertions. The package does not claim external validation or numerically verified publication priority.
