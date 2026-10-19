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

# Verification and reproducibility

Execute `python3 verify_exact.py` using Python 3 and its standard library. The code uses exact `fractions.Fraction` arithmetic throughout (including the complete finite Markov-chain solve) and reports `PASS 1416 exact assertions` on successful execution.

The verification independently calculates full-state fixation probabilities by exact Gaussian elimination of the absorbing neutral-voter Markov chain on the five-vertex graph, compares them against degree-weighted fixation values for each of its 32 configurations, and then computes the full probability distributions through both pre-final stages for durations 0 through 10. It also checks the spectral formula, each four-vertex attachment case, and one hundred members of the tree family.

Analytical scope is stronger than those finite tests: the proof gives explicit formulas for any finite connected admissible final graph, shows four-vertex minimality by complete elementary attachment logic, and proves the optimizer for every integer parameter of the tree family. Computation verifies arithmetic and finite examples but does not certify publication priority or replace the proof for unbounded graph order. Independent scientific audit is not performed.
