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

# Reproducible checks

The accompanying `verify.py` uses the standard library only, with exact `fractions.Fraction` arithmetic. It carries out 2,201 exact comparisons for every abstract state with \(4\le k\le65\) extant lineages and \(0\le b\le k\) surviving singletons, comparing the state-specific first moments and the claimed covariance formula to an independently generated recursive mixed moment.

It separately enumerates all possible labeled merger histories of standard Kingman trees with \(2\le n\le7\) leaves. Each merger history has the same probability because the choice count at each lineage level depends only on that level. Conditional on a history, exponential holding times contribute expected total external length \(\sum_k b_k/\binom{k}{2}\). Exact covariance from these histories is zero at two and three leaves and \(-2/9\) at every tested larger size.

The critical scientific proof is the rational three-transition induction in `RESULT.md`, including the terminal-state exception and the independence of coalescent times from pair choices. Enumeration and dynamic-program outputs are supportive checks and do not prove infinitely many cases. The tests do not investigate nonhomogeneous coalescents or historical originality. No independent audit or independent validation is claimed.

Command: `python verify.py`.
