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

`python verify.py` (Python 3.10 or newer, standard library only) completed with `PASS: 2838 deterministic arithmetic and structural checks` on the embedded standalone script. It compares formula and procedural ETD2 stage construction on basis vectors for multiple dimensions, positive step scales and coupling fractions, checks exact exponential polynomials and row/column contractions, reproduces the stiff limiting shift powers and post-threshold algebraic residue coefficients, and checks the fixed-stiffness small-step consistency ratios.

The proof in `RESULT.md` establishes the infinite-domain assertions symbolically using nilpotency and finite matrix multiplication. The numerical verifier provides no exhaustive test of all dimensions, step sizes or stiffness values and does not assess independent mathematical or bibliographic priority.
