---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Unit-rate exchanges connect all size-k subsets; reset preserves that space, so there is a unique stationary law. Summing the exchange increments at i gives k−Nη_i; adding reset gives the mean m_i=(k+r b_i)/(N+r). For distinct sites apply the Markov generator product rule. The only exchange contributing to the product of increments is {i,j}, contributing −(η_i−η_j)^2, while reset contributes r(b_i−η_i)(b_j−η_j). Stationarity therefore gives [2(N−1)+r]Cov = −m_i−m_j+2m_i m_j+r(b_i−m_i)(b_j−m_j). This checks the second-moment closure and isolates the source of positive same-class covariance. Substituting the means gives the stated three numerators over the common positive denominator. The same-class numerators have intercept −2kℓ and slopes k(k−2) or ℓ(ℓ−2); mixed pairs have a strictly negative quadratic numerator. This verifies uniqueness, strict signs, the existence conditions of each pair class, and the N≥5 interior-filling consequence. The uniform r↓0 limiting covariance and the large-r orders agree. Positive covariance contradicts negative association by testing the increasing single-site occupations, but the converse was not used. Exact unreduced generator checks using python /workspace/branches/independent_checks.py give 00 covariances −3/704, 0 and 3/1300 at (N,k)=(5,3), r=3,4,5, plus both homogeneous zeros and mixed covariance −1/16 at (6,3,6). Independently counted 2,766 cases in the reported finite grid; these are corroboration, not the general proof.

## originality

PASS

Global renewal and deterministic-time exclusion dependence are established. The distinct result supported here is the explicit finite-volume, complete-graph, fixed-particle all-pair sign classification and its exact unique cutoffs. The closest graph-general indexed global-reset result partially covers reversal existence but not the exact complete-graph cutoffs.

## value

PASS

An exact controlled instance separates negative dependence under ordinary conservative exchange from stationarity under a common reset age. The result identifies when particle conservation permits positive covariance, when reversal is impossible, and where it occurs, for all system sizes and fillings. These provide useful sign and finite-volume benchmarks without overclaiming higher-order negative dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
