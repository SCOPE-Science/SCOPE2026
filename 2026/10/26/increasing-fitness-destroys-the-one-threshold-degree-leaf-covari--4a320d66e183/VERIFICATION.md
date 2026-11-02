---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Writing B_{ki}=1{parent(k)=i} and X_j=1{j has no children}, each pair of different arrivals is independent. The only nonzero terms in Cov(B_{ki},X_j) are j=i (negative −w_i p_i/W_{k−1}) and 2≤j<k,j≠i (positive w_i w_j p_j/[W_{k−1}(W_{k−1}−w_j)]). Summation proves formula (1) for every n and positive real weight vector. For i=n−1, conditioning on the last parent choice proves a strict negative covariance with leaves since the root is not a leaf. The last vertex has D_n=0. Independent exhaustive enumeration of 24 possible increasing-parent maps at n=5 with exact rational product probabilities reproduces covariances (−2087/31104,25/10368,−1225/6912), and independently reproduces formula (1). For n<5 there are fewer than three nontrivial nonroot degree indices, so the alternating triple cannot occur; continuity preserves the sign pattern in an open increasing-weight neighbourhood.

## originality

PASS

Hiesmayr 2017 proves weighted-tree leaf-count expectations and asymptotic laws with specified weight profiles; Eslava–Lodewijks–Ortgiese 2021 address random-weight maximum-degree fluctuations. These works do not state the exact deterministic-weight tagged Cov(D_i,L) or smallest strict-increase -,+,- counterexample in the material read. General Bernoulli indicator algebra is elementary and remains a priority/novelty-strength caveat, but the exact motivated sign boundary is not a direct parameter substitution in the cited aggregate results. Qualified best-of-knowledge PASS.

## value

PASS

The equal-weight chronological one-threshold sign rule naturally invites a robustness question under increasing fitness. The exact counterexample at the smallest possible order disproves that tempting extrapolation, and the universal formula allows diagnosis for arbitrary positive attachment profiles. A sharp motivated boundary is useful even without all-sign-pattern classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
