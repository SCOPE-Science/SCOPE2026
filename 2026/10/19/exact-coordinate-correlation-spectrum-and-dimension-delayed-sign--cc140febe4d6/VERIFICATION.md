---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof boundaries

Run `python verify_twisted_baker_affine.py` with Python 3 and its standard library. The program checks finite exact identities for the two-branch affine transfer matrix, characteristic polynomial and first-coordinate rational resolvent in dimensions 2 through 8, with a separate planar numerical check. It also checks finite coefficients and the dimension of the first sign reversal, a consequence of the resolvent. Its expected summary is `PASS: 3483 exact-rational identities / finite floating diagnostics`.

The sharp dimensional asymptotic is not a numerical fit or a checker output. Its proof combines no pole cancellation, analytic implicit continuation for a pair of near-unit roots, and an upper bound on any root of maximal modulus derived from the characteristic equation.
