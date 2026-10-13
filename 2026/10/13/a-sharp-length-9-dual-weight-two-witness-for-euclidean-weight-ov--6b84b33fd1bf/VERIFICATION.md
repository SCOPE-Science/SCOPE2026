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

The standalone verifier `artifacts/verify.py` uses only the Python standard library and exact arithmetic modulo \(5\).

It first reconstructs the two displayed \(2\)-by-\(9\) matrices, checks row rank \(2\), normalizes all nonzero columns modulo \(\{\pm1\}\), and recovers the stated twelve-entry multiplicity vectors. It enumerates all \(25\) messages of each code and verifies the common primal Euclidean-weight enumerator exactly.

For an independent dual check, it propagates a dynamic-programming table indexed by the syndrome in \(\mathbb F_5^2\) and total Euclidean weight. Restricting to zero syndrome gives each complete dual enumerator; both totals equal \(5^7=78125\), while the Euclidean weight-\(2\) counts are respectively \(14\) and \(10\).

For the lower bound, the verifier enumerates every nonnegative twelve-part multiplicity vector of total length \(n\) for each \(2\le n\le8\). It keeps precisely the vectors whose occupied column representatives span dimension \(2\), groups them by the exact sorted Euclidean weights of all \(24\) nonzero messages, and verifies that \(2\sum_j\binom{\eta_j}{2}\) is constant inside each group. The retained state counts are \(60,340,1335,4332,12334,31776,75528\), agreeing with the stored certificate.

The verifier then confirms that the two explicit length-\(9\) multiplicity vectors have the same primal signature and different dual Euclidean weight-\(2\) counts. A successful replay prints `VERIFY_OK`.

The computation proves only the stated effective dimension-\(2\), dual-weight-\(2\) cutoff. It does not enumerate higher-dimensional codes or prove that no shorter pair can first differ at a larger dual Euclidean weight.
