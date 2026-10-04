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
# Verification

The proof uses only finite-dimensional semigroup identities and Perron asymptotics for the two irreducible single-type blocks. The critical coefficient is obtained by integrating the mixed-class forcing against the class Perron mode; strict \(\alpha_3>\alpha_k\) makes the resolvent integral finite.

The bundled `verify.py` checks the explicit three-transient-state witness. It verifies the closed-form prefactor, the gap-only crossing, the amplitude-adjusted crossing, and the exact class-probability ratio by direct bisection. A successful run prints `VERIFY_OK`.

The computation is illustrative only. It does not reconstruct the source's biological generator, so no source-specific replacement Table 5 number is certified here. The theorem-level formula, not the numerical witness, carries the infinite-time asymptotic claim.
