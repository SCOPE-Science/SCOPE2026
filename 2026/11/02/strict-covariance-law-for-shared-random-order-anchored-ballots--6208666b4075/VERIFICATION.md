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

# Finite checks and proof boundaries

Execute `python3 verify.py` using the standard Python 3 library. The verifier checks the exact rational two-record indicator probability for pairs of labels, compares it against direct enumeration of the shared uniform presentation for \(m=2,3,4,5\), and checks covariance and the adjacent-swap theorem through \(m=6\), together with randomized independent ranking relabelings for \(m=7\). Results were 152 complete brute-force comparisons, 872 pair-formula evaluations, and 2,283 adjacent-swap identity checks, all passing. The sharp extremal values and unique equality profiles were checked in the enumerated sizes.

The universal mathematical proof is in `RESULT.md`: it is an exact clock-coupling identity, elementary integrals, a telescoping sum, and the independence of uniform insertion ranks. No finite experiment is represented as an infinite certificate. The exact covariance law does not cover smaller acceptability thresholds, nonuniform or separate presentation orders, or strategic voting. No independent scientific audit has been performed.
