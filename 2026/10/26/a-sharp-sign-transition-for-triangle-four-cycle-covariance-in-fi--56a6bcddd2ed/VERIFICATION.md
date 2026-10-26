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

# Verification

`verify.py` uses Python 3.9+, Python's exact `fractions.Fraction`, and SymPy to perform independent computational checks of the stated rational covariance formula.

The checks enumerate all \(2^{\binom n2}\) labeled graphs for \(n=4,5,6\): respectively 64, 1024 and 32768 graphs, totaling 33856. Every fixed-edge layer is checked against the moment-overlap expression and factored result, and the one- and two-statistic marginal counts are independently counted. The script checks the unrestricted rational identity symbolically and validates finite sign cases for all \(4\le n\le50\). The observed output is `PASS 138 exact checks; fully enumerated graphs: 33856` followed by `PASS finite sign crosschecks for n<=50 (supplements exact sign proof)`.

These enumerations do not establish an unrestricted graph theorem; the proof for arbitrary size is the combinatorial intersection classification plus symbolic cancellation, both detailed in `RESULT.md`. No external independent audit is claimed. The only scientific priority limitation is potential earlier implicit coverage by a broader unpublished or uninspected mixed-moment formula.
