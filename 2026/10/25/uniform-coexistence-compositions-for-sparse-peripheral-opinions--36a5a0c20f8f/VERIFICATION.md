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

# Reproduction of finite checks

With Python and SymPy available, run `python verify.py` from this directory. The script independently enumerates positive transient peripheral support vectors, constructs the original finite absorbing Markov chain with exact rational transition probabilities, and solves for the probabilities of reaching every fully coexisting terminal vector. It checks equality individually against the analytic factorial formula and verifies their sum.

The reported result is 114 verified terminal probabilities over 13 small cases, with examples \((d,n)=(3,7)\) yielding \(1/126\) for each of 15 compositions and \((4,7)\) yielding \(1/120\) for each of 20. The program uses matrix inversion on a finite state space. The universal theorem is mathematical, proved in `RESULT.md`, and not inferred from testing. No independent human audit or formal verification has taken place.
