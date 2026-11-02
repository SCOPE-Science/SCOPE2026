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

# Reproduction of finite and rational checks

Run `python checker.py` under a standard Python 3 interpreter. The script exhaustively compares greedy support counts against direct stabilized modal bisimulation partition refinement for 13,012 independently enumerated finite assignments; cross-checks three exact distributions by two different algorithms; and checks the stationary recurrence over 21 exact rational parameter settings, including the \(159/112\) slope. A successful run prints `ALL_CHECKS_OK`.

The script does not test infinitely many frame sizes and does not constitute a proof of the almost-sure phase transition. That conclusion uses the positive absorbing probability at and above \(r=q\), and irreducible finite-state Markov ergodic theory below \(r=q\). Absolute historical priority and independent validation have not been established.
