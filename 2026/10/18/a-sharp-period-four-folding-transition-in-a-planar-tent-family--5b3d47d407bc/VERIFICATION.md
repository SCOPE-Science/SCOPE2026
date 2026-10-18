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

# Verification record

The supplied `verify.py` program uses the Python 3 standard library `fractions` module and exhaustively constructs exact affine returns for every binary itinerary of lengths one, two and four at five rational parameter values. It confirms the predicted primitive counts, point coordinates, triangle membership, branch choices, return-period divisibility, and the polynomial identities forcing the simultaneous boundary collision. The program reports 129 passing rational checks.

The analytic proof in `RESULT.md`—not finite tests—establishes completeness for all parameters, uniqueness of the threshold, the equality case, and universal absence of further period-four orbits. The supporting full 2022 preprint and the 2024/2025 primary source were read in relevant sections. The 2015 originating Nonlinearity article was not available in full; therefore the originality assessment retains priority risk.

This record does not constitute independent verification.
