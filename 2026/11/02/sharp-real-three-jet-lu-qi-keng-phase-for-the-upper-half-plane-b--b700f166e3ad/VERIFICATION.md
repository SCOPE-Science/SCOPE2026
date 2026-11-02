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

# Verification and limits

The proof in `RESULT.md` gives exact mixed-derivative coefficients, an explicit inverse for the attainable lower half-plane, and an exhaustive real-polynomial root classification including the vanishing-second-jet and double-root boundary. The proof does not use finite sampling.

`CHECK.py` is self-contained (Python standard library) and in this packaged form completed `CHECK_OK 4313`. It checks factorial coefficient identities over rational parameters, numerical complex roots and realized zero pairs over a finite grid, positive diagonals, Hermitian symmetry, two-point Gram positivity and the sharp double-root threshold. An additional direct symbolic differentiation of the base Bergman kernel was performed and agreed exactly with the polynomial in the theorem. Finite tests do not establish the universal assertion by themselves.

The claim is only for real, normalized value/first/second derivative coefficients of the canonical Riesz Gram kernel on the unweighted upper half-plane. It does not cover complex parameter phases, arbitrary fixed point slices, or higher-support functionals. Independent mathematical assessment has not been performed.
