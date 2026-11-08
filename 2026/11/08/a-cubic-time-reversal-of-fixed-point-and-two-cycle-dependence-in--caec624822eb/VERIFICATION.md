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

# Reproducible checks

Run `python3 verify.py` with a standard Python 3 interpreter. The checker enumerates the complete exact rational Markov distribution at the specified sizes and times, rather than sampling, and compares its covariance with the four-mode formula. It also checks algebraic identities, mode ordering, one-step signs, and integer transition examples. Direct distribution enumeration covers \(n=6\), steps \(0\) through \(5\), and \(n=7\), steps \(0\) through \(3\). Exact rational sign checks cover \(n=6,\ldots,10\) to \(t=1000\).

The infinite-size covariance and unique sign transition are established analytically in `RESULT.md`; finite computation does not independently certify them. The external independent audit is not performed.
