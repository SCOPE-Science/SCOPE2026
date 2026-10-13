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

# Reproducibility and limits

The result is established by the analytic population recursion, the normalized two-qubit Choi partial transpose, the exact neighboring-swap identity, and monotone polynomial inequalities. This file reports only supporting finite checks; it does not assert independent validation.

Execute `python artifacts/verify.py` with `numpy>=1.24` from the package root. The script represents the channels both via exact rational parameters and via explicit Kraus matrices, acts on a normalized Bell state, transposes the output factor, and computes numerically its eigenvalues. It compares all 5,320 tested permutation matrices with the analytically predicted negativity, checks rational offsets and sorted order bounds, verifies the adjacent-swap identity, and tests the explicit two-contact order reversal. It also locates the unique roots of the two threshold cubics by bisection and confirms their reported approximations. The actual execution returned:

`VERIFY_OK 5320 permutation matrices; exact rational composition/EB checks; example verified`

Matrix numerics are floating-point and the finite rational instances sample finitely many damping strengths and equilibrium populations; neither extends the proof beyond the analytic argument. Independent audit: not performed.
