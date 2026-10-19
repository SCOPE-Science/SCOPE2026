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
# Reproducibility and proof limits

The standalone `verify.py` runs with Python 3 and the standard library only. Its integer and `fractions.Fraction` assertions check all branch-cell images and symmetry for \(2\le m\le40\), finite graph reachability/primitivity for these parameters, exact stationary probabilities for \(2\le m\le8\), selected rational-orbit entries, and the \(m=2\) density moments. Execution reproduced `PASS exact finite checks: 13078` with stationary vector \((1/6,1/3,1/3,1/6)\), mean \(1\), variance \(1/9\).

Finite checks do not certify infinitely many parameter values, generic convergence of empirical measures, or originality. Those claims require the independent mathematical reasoning provided in `RESULT.md`, including the all-parameter directed-graph proof and the stationary Markov-chain argument. No external independent mathematical audit is claimed.
