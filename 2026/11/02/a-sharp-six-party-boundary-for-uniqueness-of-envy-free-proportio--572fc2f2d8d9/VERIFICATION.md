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

The full-column-rank assertion is supported by the thirteen explicitly tabulated unit-determinant minors in RESULT.md. The enumerated positive-part patterns are exhaustive for three strata and at most five parties. The exact rational code in `verify_rank.py` independently constructs every zero-one marginal matrix, checks all thirteen rank/minor certificates and the boundary surplus cases, and verifies both distinct six-party lottery distributions. An additional computer-algebra rank calculation independently reproduced the same matrices and unit minors. These computations were executed on the embedded source prior to packaging.

Run `python verify_rank.py` using Python 3. The program uses only the Python standard library. The scope is strictly the finite stratum-size cutoff; it does not prove any generalization beyond that cutoff. An independent audit has not been performed.
