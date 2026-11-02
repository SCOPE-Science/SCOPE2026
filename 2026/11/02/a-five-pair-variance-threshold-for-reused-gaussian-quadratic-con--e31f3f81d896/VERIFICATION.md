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

Run `python3 verify.py` in the directory containing this file and the standalone script. The program uses only the Python standard library and verifies exact rational algebraic identities, pathwise sample decompositions, and Monte Carlo consistency checks for two finite-variance configurations. The recorded successful result is `VERIFY_OK 2748`.

The proof in `RESULT.md` separately establishes the general quantifiers, integrability and nonintegrability boundaries by conditional Gaussian calculations and Gamma–Dirichlet negative-moment criteria. Finite simulations cannot establish infinite moments, global originality, or finite-sample statements for every \(n\); they are supplementary diagnostics. The scientific review is not an independent audit.
