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

# Reproduction and boundaries

Run `python CHECK.py` with Python 3 and no third-party modules. The executable independently inverts rational graph Laplacians with a mean-zero normalization and tests the rank-one Green expression entrywise, reconstructs extremal zero-sum sign loads, checks the exact homogeneous four-class values, and compares several growing cycles with the first-order limit and quarter-cycle site predictions. In the completed test, 4269 finite assertions passed.

The proof of the infinite family and the \(1/16\) coefficient is analytic in `RESULT.md`. Finite calculations do not establish either theorem for all cycle sizes, do not certify unknown equivalences in the literature, and are not independent mathematical audits. The convention \(L=D-A\) must not be replaced by a degree-normalized random-walk Laplacian in these formulas.
