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
# Verification evidence

The complete proof appears in `RESULT.md`; `verification/check.py` is an executable, standalone Python 3 standard-library exact-rational consistency checker. It enumerates each of the \(2^{\binom n2}\) tournaments for \(n=3,4,5,6\). For each \(k=0,\ldots,n-1\), it calculates the conditional mean and conditional variance of the circular-triad count given the score of a fixed vertex and the covariance of circular-triad count with the number of players having score \(k\), then checks them against the analytic expressions without floating-point rounding. The 54 exact rational comparisons consist of \(3(3+4+5+6)\) distinct reported comparisons. Enumerated orientation counts are \(8\), \(64\), \(1024\), and \(32768\), respectively.

To replay: run `python3 verification/check.py` from the extracted package directory. The script uses only Python's standard library. This verifies finite instances; it is not an exhaustive proof for arbitrary tournament order and no independent audit has been performed. The proof is an analytic argument based on conditional pairwise independence, a centered regression, and finite orthogonal polynomials.
