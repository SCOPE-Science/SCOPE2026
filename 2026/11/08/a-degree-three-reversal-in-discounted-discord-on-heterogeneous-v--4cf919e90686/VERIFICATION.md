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

# Reproducible analytical and finite-state checks

Run `python3 checker.py` using only the Python 3 standard library. Observed output from the checked package:

```
PASS 1196 exact assertions; full-state cases 54
```

The program independently builds full binary voter-chain generators with \(2^{k+1}\) states for \(k=2,3,4\), solves exact rational discounted occupation-time resolvents, and checks the derived closed-form result for 54 combinations of parameters. It also conducts exact rational sign/threshold/invariance checks for \(k\) up to \(50\) and initial slope checks. An independent symbolic quotient differentiation confirms the analytic factorization. No numerical tolerance or stochastic simulation is used.

The universal theorem rests on the explicitly documented generator closure, stable two-dimensional system, Laplace inversion, and algebraic derivative factorization in `RESULT.md`. A finite test sweep, however extensive, cannot certify these for untested reals or network sizes. No independent audit or external certification has occurred.
