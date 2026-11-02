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
The standalone `verify.py` script uses only Python 3 standard-library exact rational arithmetic. Execute `python verify.py` in this directory. It verifies six permutations at three snapshots, two explicitly printed rational monodromy characteristic polynomials, two strict positive-vector Perron inequalities, and 24 labeled permutations of the four-snapshot multiset. The proof in RESULT.md establishes the universal lower bound and nonlinear global outcomes; finite verification alone does not prove either universal assertion. The model concerns the deterministic mean-field SIS process; independent audit is not performed.
