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

# Verification details

Run `python3 verify.py` with only the Python 3 standard library.

The checker enumerates every word over alphabets of cardinalities \(q=2\) and \(q=3\) at source lengths \(n=3,4,5,6,7\). At every burst length, it constructs a set of all \(n-b+1\) actual deletion outputs. It independently computes the lag-disagreement expression, exact binomial histogram, and pairwise and triple centered products. Triple products use integer scaling, avoiding floating-point uncertainty. The final line is `VERIFY_OK 10 complete parameter sets`.

The graph proof, rather than the finite census, establishes the result for all permitted integers. The literature comparison remains subject to the explicit residual risk of an unindexed equivalent triangle-moment theorem. No independent audit was performed.
