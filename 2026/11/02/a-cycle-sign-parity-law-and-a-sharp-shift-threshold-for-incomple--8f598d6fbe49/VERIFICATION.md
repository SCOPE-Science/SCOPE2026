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

The proof and the script `verify_cycle_ic.py` are self-contained except for NumPy used by the executable finite checks. Run `python3 verify_cycle_ic.py`. It must report 3,667 passing exact-rational recurrence, matrix-spectral, sign, shift and asymptotic consistency checks.

# Actual scientific checks

- Reconstructed the sign-gauge eigenvalue formula for both edge-sign products and both parities.
- Derived the complete sparse IC(0) pivot recurrence from the retained pattern; identified the extra closing-edge contribution in the final pivot.
- Proved the path determinant identity and located the first two positive zeros to exclude false sign claims beyond the first crossing.
- Compared the phase diagram and shift equality boundaries against explicit finite matrix factorizations, and verified the exact four-vertex rational witness.
- Checked the condition-number boundary and large-size asymptotic expansion against direct spectral calculations.

# Unproved and external limits

The finite checker does not certify the infinite family; the algebraic proof does. The result does not cover variable edge magnitudes, other orderings, roundoff, Krylov iteration performance, or other fill policies. Publication priority is conditional on accessible literature; a plausible older existence note was not available in full text. Independent scientific audit has not been performed.
