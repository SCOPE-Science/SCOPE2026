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

The file `verify.py` performs exact-rational tests of the Dirichlet moment Gram inverse and of the beta-expression for the sharp endpoint norm. Execute `python3 verify.py` with a standard Python 3 interpreter. In this package it completed with `PASS: 360 nonuniform profiles, 7650 rational Gram-inverse coefficient tests, 1638 independent beta-integral comparisons, 7650 strict row-order tests, 406 fixed-total monotonicity comparisons, 99 uniform-simplex specializations`.

The exact computations check integer parameter profiles. They do not establish the real-parameter monotonicity, which is proved by gamma-process conditioning, or the high-dimensional limit statements, which are proved using moment bounds and uniform integrability. No independent audit has been performed.
