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

# Reproduction
Run `python3 verify.py` with Python 3 and its standard library. The script constructs all \((2n-1)!!\) Stirling permutations at each order \(1\le n\le7\) by unique insertion of each largest adjacent pair. It independently parses every word into a rooted ordered labelled tree and checks its plateau, nesting, leaf, and depth identities. For trees through order \(5\), it enumerates each possible next insertion and checks the exact conditional recurrences, including the mixed product. It recomputes exact rational covariances through order \(7\), checks the closed expression and negativity through order \(1000\), and exits nonzero on any discrepancy.

Actual replay: `VERIFY_OK words=146599 decoded_shape_checks=146599 conditional_insertion_checks=1069 exact_mean_checks=14 covariance_checks=7 finite_sign_checks=7 n_range=1..7 analytic_formula_checks=1000`.

# Logical scope
The code is finite evidence. The assertion for every \(n\ge1\) follows from the complete conditional-moment derivation and solved recurrence in `RESULT.md`; strict negativity follows from the sign-preserving linear recurrence, and the asymptotic from the classical central-binomial estimate. The checker does not establish originality, a full mixed law, any results about generalized multi-copy Stirling permutations, or independent audit.
