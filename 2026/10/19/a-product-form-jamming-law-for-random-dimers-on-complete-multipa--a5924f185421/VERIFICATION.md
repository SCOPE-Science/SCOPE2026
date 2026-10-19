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

# Verification instructions and outcomes

Execute `python verify.py` from the same directory as this document, using Python 3.10 or newer and only its standard library. The included program implements: (a) recursive exact-rational absorption probabilities computed from class-level transition rates, (b) separately enumerated uniform physical priority permutations for four small input graphs, (c) polynomial ODE identities and boundary limits for three-, four- and five-class rational inputs, and (d) a reproducible finite-size stochastic consistency test.

The program completed successfully: **37 finite exact checks**, predicted density **3/160** at proportions **2/5, 7/20, 1/4**, and sample mean 0.01979167 on 48 fixed-seed simulations with 2,000 vertices. The independent exhaustive comparisons use at most nine edges per graph; no higher-size exhaustive enumeration is asserted.

The rigorous asymptotic claim is established in `RESULT.md` by the exact Markov-chain rates, fixed-time martingale quadratic-variation bound, explicit solution to the deterministic fluid ODE, and a deterministic terminal-vacancy bound. The executable is a reproducibility check rather than a machine-checked general proof. No statement about a convergence rate, central limit law, or behavior with growing numbers of vertex classes is established.
