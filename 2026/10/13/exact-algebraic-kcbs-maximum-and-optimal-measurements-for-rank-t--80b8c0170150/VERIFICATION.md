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

# Mathematical verification

The standalone `verify.py` uses symbolic simplification (SymPy) to check the discriminant and its first two derivatives, the eigenvalue characteristic polynomial, the monotone symmetric-pentagon parameter and exact projector orthogonality/normalization at five distinct algebraic sample values. It additionally uses SciPy for numerical scalar-root comparison and NumPy for independent diagonalization at seven rank-two qutrit spectra. The actual bundled checker prints `VERIFY_OK symbolic_spectral=passed exact_projectors=5 optimizer_cases=7`.

The proof of the maximum for **every** rank-two qutrit state is symbolic: global trace alignment, the complete pentagram spectral range, strict concavity, the sign-controlled sextic equation, exact boundary cases and a realizability construction. Finite tests corroborate only those implementation identities. No claim is made to independently audit the scientific originality or to verify all conceivable later literature.
