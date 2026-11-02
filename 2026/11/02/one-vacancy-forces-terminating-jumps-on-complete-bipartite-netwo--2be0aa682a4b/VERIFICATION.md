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

The complete symbolic argument is in `RESULT.md`. The standalone `verify.py` uses Python's exact `fractions.Fraction` class. It checked the four specified labeled moves on the six-vertex graph and obtained, in order, payoff improvements \(0\to20/33\), \(20/27\to10/11\), \(0\to20/33\), and \(20/27\to10/11\), returning to the original labeled occupancy. It also completed 2,250 parameter instances of the one-vacancy population-state check (including arbitrary, not necessarily single-peaked color-dependent tables), checking graph-edge shape and acyclicity. Neither finite parameter sweeps nor tests on a bounded graph order can substitute for the infinite-family proof. No external human audit or independent validation is claimed.

Reproduce with `python verify.py` in the extracted directory. The checker has no third-party dependencies.
