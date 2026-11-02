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
# Analytical and computational verification

The finite checks in `verify.py` reproduce the transition polynomial, the two endpoint factorizations, the exact root equations, and eigenvalue counts for 50 rational pairs. The script exits with success only when these tests pass. To reproduce: `python verify.py` with SymPy available. Its computational checks are finite and make no claim to exhaustive verification of an infinite parameter domain.

The universal result instead follows from the proof in `RESULT.md`: two-cycle coordinates are forced by the shift structure, the quadratic discriminant enumerates all real cycles, and any multiplier crossing the unit circle must pass through one of the three algebraically classified cases. Nonreal unit-pair crossings occur only below the birth boundary, while the \(-1\) crossing is simple and transverse. No local existence result for a four-cycle is asserted. Independent validation remains unperformed.
