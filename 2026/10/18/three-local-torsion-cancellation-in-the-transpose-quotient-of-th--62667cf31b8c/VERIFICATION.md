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

The included `verify.py` reconstructs the ordinary five-by-five chessboard complex from its nonattacking-rook definition. With `certificate.json` it verifies a 60-term mod-three boundary proving that a chosen torsion generator plus its transposed image is a boundary, and a nonzero mod-three cocycle pairing. It also computes the two relevant modular boundary ranks 176 and 423, and checks the row, column, and transpose signs. The signed fixed-simplex recurrence yields trace zero for transposition on rational third homology.

The external published inputs that the verifier does not independently re-prove are the integral torsion generator and simple connectivity of the five-by-five chessboard complex; the orbit-space and localization arguments are mathematical deductions, not finite-computation assertions. The result is a self-review, not an independent audit.
