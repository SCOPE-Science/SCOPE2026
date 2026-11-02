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

# Mathematical and computational verification

The proof is analytic and is reproduced in `RESULT.md`. The finite computation is an independent consistency test, not a certificate for an infinite theorem.

Run `python3 verify.py` with Python 3 and its standard library. All arithmetic uses exact `fractions.Fraction` objects and all absorbing-chain solves use rational Gauss–Jordan elimination. The tests verify (1) 5760 state/parameter combinations on four biregular connected bipartite graphs, (2) 366 transient states across independently solved homogeneous absorbing Markov matrices, and (3) all 30 transient states of a five-vertex irregular path at product balance, also by exact-rational solving. These results do not test graphs of unbounded order and are not needed for the martingale proof.

Independent external audit and mathematical validation have not been performed. Previously established special cases are disclosed in the literature-comparison section.
