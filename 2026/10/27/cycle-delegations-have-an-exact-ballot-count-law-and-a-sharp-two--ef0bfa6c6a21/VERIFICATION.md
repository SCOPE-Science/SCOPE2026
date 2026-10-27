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

# Reproducible verification

The companion standalone program `verify_cycle_delegations.py` depends solely on Python 3 standard library; run `python verify_cycle_delegations.py` from the package directory.

It (1) independently enumerates all directed neighbor-choice functions and rejects any actual directed cycle by following each voter to its eventual root; (2) enumerates independent arc cutpoints; (3) verifies equality of full joint guru-weight distributions, feasible counts and exact means; (4) verifies every nontrivial guru coalition's cut-variance law with exact rational arithmetic; (5) independently constructs candidate-A ballot-count polynomials and checks every coefficient; and (6) checks the two-guru tie count and probability. Tested all 1418 cycle/guru placements with 3–10 vertices, 2–5 fixed gurus as applicable; a total of 19966 feasible delegations. All checks passed.

The finite checker provides regression evidence, not an exhaustive proof over arbitrary cycle sizes. The main proof in RESULT.md handles all admissible cases without reliance on this finite verification. It makes no claim about general networks or independent external validation.
