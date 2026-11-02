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

The included `verify_exhaustive.py` enumerates all \(126126\) unlabeled equal three-part partitions without quotienting by an unproved group action. It checks all \(35\) projective lines and \(15\) hyperplanes, exact rational expectation values, every attaining partition, all five-caps and the complete \(\operatorname{GL}(4,2)\) orbit. The program uses only exact Python integer and rational operations.

The independent `verify_markov.py` builds the complete lattice of \(67\) binary four-dimensional subspaces and solves for the expected first full-span round by rational dynamic programming, considering all \(125\) equally likely three-container draws per round. It verifies the displayed optimal witness without using the analytic hyperplane formula or optimizer enumeration.

Running `python3 verify_exhaustive.py` and `python3 verify_markov.py` in the artifact directory reproduces `CHECKS.txt`. These are a complete finite proof for the particular fifteen-point balanced optimization, not evidence for an unexamined infinite family. Publication priority and independent mathematical audit remain unperformed.
