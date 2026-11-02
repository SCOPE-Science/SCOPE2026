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

# Reproducibility

Execute `python3 verify.py` using Python 3 standard library only. The verification performed on the packaged script reports `VERIFICATION_OK 258852 assertions`.

The script explicitly enumerates elimination orders for paths of lengths two through eight, checks the analytic probability-generating function, iterates over all labelled trees through six vertices for the expectation and extremal inequalities, independently reconstructs fill graphs, and performs rational positive-definite Schur-complement calculations on selected concrete matrices. All equality and normalization tests are exact except for none of these finite checks requiring random simulation for proof.

These computations are finite tests, not a replacement for the general combinatorial proof given in `RESULT.md`. No independent scientific assessment has been performed.
