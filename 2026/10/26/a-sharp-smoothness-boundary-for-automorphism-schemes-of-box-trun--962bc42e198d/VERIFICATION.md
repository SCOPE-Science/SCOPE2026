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

# Verification and scope

The first-order tangent calculation is explicit: the linearized relation for an image perturbation of \(x_i\) is \(m x_i^{m-1}h_i\). Monomial multiplication gives rank \(m^{n-1}\) for each coordinate when \(m\) is invertible, and rank zero otherwise. This identifies all infinitesimal directions including constant translations in the modular case.

The family \(x_i\mapsto x_i u_i\) with \(u_i\) units has the tangent dimension predicted in the invertible-exponent case; automorphisms are guaranteed by the invertible cotangent map. The modular case fails smoothness by a strict tangent/geometric dimension comparison.

Run `python verify.py` with Python 3. Its finite-field exhaustive tests return the counts 24, 72, 2048 for \((n,m,q)=(2,2,2),(2,2,3),(2,3,2)\), and its monomial Jacobian linearization tests cover 60 combinations. The expected output is `VERIFY_OK aut_counts=3 tangent_cases=60`. Finite checks are not used as substitutes for the arbitrary-exponent proof.

The full nonreduced group scheme is not determined in composite modular cases. The prime-exponent non-smoothness is earlier literature; the precise global if-and-only-if criterion may need further specialist priority assessment. No independent audit was performed.
