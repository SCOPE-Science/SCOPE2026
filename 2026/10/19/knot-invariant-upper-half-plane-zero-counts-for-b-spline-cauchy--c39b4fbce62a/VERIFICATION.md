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

# Verification of the knot-invariant zero census

The mathematical proof is in `RESULT.md`. `checker.py` verifies, by exact symbolic polynomial arithmetic, the recurrence for the numerator as needed for each tested derivative, exact polynomial degrees, noncancellation identities at knots, isolation counts of all distinct real roots, and the upper-half-plane census obtained by conjugation. The four strictly increasing real knot sets are `(0, 1)`, `(0, 2, 5)`, `(-3, 0, 2, 7)`, and `(0, 1, 2, 3, 4)`; each was checked for all integer orders from zero through six. Execute `python checker.py` with SymPy installed. `checker_output.txt` records the successful run.

The unrestricted identities, strict even-order positivity, odd-order simple real-root uniqueness, polynomial degree, and conjugate-pair census are justified by the analytic argument, not by extrapolation from these examples. The checker does not prove novelty, infinite-domain correctness, or root simplicity off the real axis. Independent mathematical audit has not been performed.
