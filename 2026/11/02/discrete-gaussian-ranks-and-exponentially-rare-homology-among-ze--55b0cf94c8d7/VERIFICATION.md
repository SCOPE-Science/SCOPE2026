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

The standalone finite checker `verify.py` enumerates actual ordered finite-field matrix pairs for five small \((q,n)\) configurations, computes both matrix ranks and the matrix product, and compares every observed rank-pair count with the closed counting expression. It also makes 48 exact integer-arithmetic consistency tests for the two formulas for the total number of zero-product pairs. The replay command is `python3 verify.py`; successful output ends with `VERIFY_OK`. The proof's limiting claims instead depend on discrete-Gaussian dominated convergence and full-rank probability estimates; no finite check is presented as a proof of a limit. Independent scientific audit has not been performed.
