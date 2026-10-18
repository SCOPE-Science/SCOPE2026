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

# Mathematical reproducibility

The accompanying `verify.py` uses only Python's standard library. It evaluates a two-support example by exact rational arithmetic and checks the signs at five stated arguments. By the intermediate value theorem, those signs establish four distinct interior roots; the theorem's analytic sparse-polynomial upper bound establishes there are no others. It also performs finite checks of the inequalities used in the explicit family, but those checks are not a substitute for the universal estimates proved in `RESULT.md`.

Run `python3 verify.py`. The expected final line is `PASS: four distinct interior roots in the two-size example; elementary margins checked`. Program exit status zero indicates that all included assertions succeeded. Neither the existence of infinitely many examples nor uniqueness for arbitrary support is claimed to follow from the finite checks alone.

Limits: no numerical stability solver, empirical validation, statistical data, spatial network, or stochastic finite-population test is included. No independent audit has been performed.
