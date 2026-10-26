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

The standalone `verify.py` has been executed successfully on the actual Rule 110 formula. It constructs all eight local triples, checks the reachable subset collection and quotient transitions, verifies pairwise distinguishability of the six deterministic states including the dead state, and exhaustively enumerates preimages and output words for every length from zero through ten. It checks 21 rational-generating-function coefficients by exact recurrence and 149 minimal forbidden-word witnesses. All checks use standard-library exact integer calculations.

The unrestricted result depends on the explicit mathematical proof: finite-state language equivalence, linear algebra over integers, Perron–Frobenius theorem, and the all-\(m\) forbidden-word argument. The verifier is neither an infinite proof nor an independent scientific audit. No claims concerning later iterates of the cellular automaton have been checked.
