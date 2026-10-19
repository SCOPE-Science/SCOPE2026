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

# Reproduction and mathematical boundaries

Run `python verify.py` with Python 3, NumPy, and SymPy. The program first computes an exact rational normal Gram and exact eigenvalues for the benchmark with \(u=v=3/5\). It then tests 350 independently generated admissible correlation pairs, 33,250 independently sampled probability distributions, 10,552 grid-distributed laws, and 1,050 direct complement-projector identities. The final program output was:

`PASS exact rational symbolic eigenvalues; 350 Gram families, 33250 random laws,`
`10552 probability-grid laws, 1050 direct projection identities; total numeric checks: 43801`

The randomized test uses the fixed generator seed specified in `verify.py`, but finite checks are **not** a proof for continuous parameters, arbitrary distributions, or unbounded iterations. Those assertions follow from the exact normal-Gram inverse, the balanced-sign Rayleigh witness, and the positive-semidefinite edge decomposition in `RESULT.md`. The proof treats exact arithmetic, normalized column-space geometry, and one-step conditional expectation only. No independently performed external audit is asserted.
