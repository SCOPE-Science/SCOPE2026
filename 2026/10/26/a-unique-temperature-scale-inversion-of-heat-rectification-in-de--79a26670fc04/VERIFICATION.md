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

Run `python3 verify.py` from the unpacked finding files using only the Python standard library. The script independently assembles all four energy states, two transition channels and both local bath contributions. It solves the stationary rate generator by pivoted elimination and evaluates hot-contact heat flux from transition energies. On 175 reproducible generated parameter sets it checks that those currents match the closed analytical formula and that the exact factored current difference matches their subtraction. It independently bisects the example crossing and checks monotonicity at 115 sampled temperatures.

These calculations are finite diagnostics, not certificates of the universal analytic uniqueness theorem. The latter follows from a complete derivative sign argument for \(\phi(z)=z\coth z\) and the strict endpoint limits given in RESULT.md. Inputs must satisfy the global secular model's assumptions. Independent scientific audit has not been performed.
