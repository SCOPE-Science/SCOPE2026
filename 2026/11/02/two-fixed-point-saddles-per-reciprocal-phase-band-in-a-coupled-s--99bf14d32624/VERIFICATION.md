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

The analytical argument in `RESULT.md` covers every fixed positive parameter pair and all sufficiently high reciprocal-phase bands, with a parameter-dependent onset. Existence and uniqueness rely on the implicit-function theorem and derivative domination, not sampling.

Run `python checks/verify_singular_fixed_points.py` using Python, SymPy and mpmath. In the recorded run, the checker passed 186 assertions: exact symbolic differential and determinant identities, the implicit Taylor jet, and high-precision solutions in three phase bands at each of three positive parameter pairs. Tested parameter pairs are \((0.8,0.6)\), \((1.2,1.1)\) and \((2.1,1.5)\); indices are 100, 200, 400 for the first two pairs and 400, 800, 1600 for the last. All root residuals were less than \(10^{-65}\), with explicit checks of real-eigenvalue type, orientation and the asymptotic coefficients.

The checker is not a machine proof of infinitely many fixed points. No independent review has been performed. The source's complete 2023 full text was unavailable for a definitive priority check, so priority remains provisional.
