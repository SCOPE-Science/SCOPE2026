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

# Reproduction and limits

Run `python verify.py` with Python 3 and SymPy. The self-contained verification script checks exact rational identities for the projector spectrum, off-diagonal terms, diagonal cubic and its dimension-28 decomposition, and the dimension-29 strict counterexample at scaled step \(x=12\). It then calculates 21 entire extrapolated resolvent matrices over seven complete-graph orders and three rational step parameters and compares them with their exact projector form and sign condition.

Observed output: `VERIFY_OK symbolic identities=4 exact full-matrix cases=21 orders=7`.

The finite matrix tests **cannot** prove universal statements over all orders or timesteps. Those statements are proved in RESULT.md by spectral reduction, elementary inequalities and Descartes' sign rule. No independent audit has been performed.
