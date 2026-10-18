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

# Verification of sharp real-window Gabor tomography rank

The general proof is analytical. It uses the finite Weyl orthogonal basis, a forced cancellation at nonzero order-two translations, an explicit base-dominance construction to exclude all other ambiguity zeros, and polynomial genericity. The proof requires neither an exhaustive subgroup enumeration nor numerical approximations.

The standalone program `verify_real_gabor.py` checks the corresponding roots-of-unity equalities using exact cyclotomic polynomial reduction. It exhausts every nonempty support subset for ten groups: cyclic orders 2, 3, 4, 5, 6, 8, plus \(\mathbb Z_2^2\), \(\mathbb Z_2\times\mathbb Z_4\), \(\mathbb Z_2^3\), and \(\mathbb Z_3^2\). It checks all shifts and characters for each support, including every putatively forced vanishing and the absence of any accidental vanishing for the explicit integer witness. It concluded `EXACT_CHECK_OK support_patterns=1410` when run on the packaged script.

Run `python3 verify_real_gabor.py` in the directory containing the script. The results of this finite suite corroborate rather than establish the unbounded finite-group claim. There is no assertion of independent audit, external formal proof verification, or a uniform stability estimate.
