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

# Verification

The analytic evidence is the exact three-edge-type transition kernel, a minority-fraction martingale drift calculation and maximal-inequality estimate, rare-event Bernoulli coupling, and the compensator second-moment bound. The accompanying `verification.py` carries out exact rational checks for 112 admissible finite states, checks the terminal vacancy identity during Monte Carlo runs, and reports four simulated critical-scale means and zero-count probabilities.

Execute `python3 verification.py` using Python 3 with the standard library; no external dependencies or specialized proof-assistant claims are made. Exact finite-state calculations do not certify limiting total variation on infinitely many graphs, and the numerical comparisons do not certify historical priority. The proven scope is as specified in `RESULT.md`.
