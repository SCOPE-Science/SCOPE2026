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

# Verification notes

Reproduce the checks with `python3 verify.py`, using only the Python standard library. The script confirms the five exact rational threshold comparisons at group sizes \(5,6,7,17,18\), checks exact strict log-convex inequalities on a finite sample of indices, and independently expands the binomial payoff average for rational cooperation frequencies and several group sizes. The program returned `PASS` for all tests in the prepared package.

The proof, not the finite test, covers *every* admissible distribution and all infinitely many integer group sizes. The critical reasoning is (i) the cooperator-minus-defector increment \(r\omega^k/G-1\), (ii) convexity of the binomially averaged payoff difference, (iii) Cauchy–Schwarz moment log-convexity strengthened by division by group size, and (iv) the positive-synergy tail lower bound. The example's infinite-index tail follows from increasing adjacent moment ratios after its exact threshold crossing. No independent audit or external proof certification is asserted.
