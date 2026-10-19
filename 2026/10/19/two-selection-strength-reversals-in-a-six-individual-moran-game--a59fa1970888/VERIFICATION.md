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

The finite-population claim is verified algebraically for every positive selection strength. With a fixed no-self-interaction convention, the five payoff differences for each mutant are reconstructed from the full matrix; the absorbing birth-death fixation formula gives exact Laurent polynomials in \(z=e^w\). Clearing positive denominators yields \(P(z)\), and Descartes' rule plus the three disjoint positive-root brackets proves both completeness and simplicity of the roots. The independent Markov-chain recurrence gives the same fixation probabilities using only exact rational arithmetic at five rational \(z>1\) values.

Run `python verify.py` with Python 3's standard library. The checker is finite verification of the algebra and recurrence, not a substitute for the universal Descartes argument in the proof. It verifies no biological data, no real-world predictiveness and no uniqueness of this example across all possible games. Independent scientific audit has not been conducted.
