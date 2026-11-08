---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

An unbiased bridge of 2n steps can be decomposed uniquely into k signed excursions. The unsigned excursion generating series F(z)=(1-sqrt(1-4z))/2 and Lagrange inversion give a_{m,j}=j/(2m-j)*binom(2m-j,m-j). Counting the first r and final k-r excursion lengths yields P(T_r=t|K=k)=a_{t,r}a_{n-t,k-r}/a_{n,k}; the fixed step probability p cancels on conditioning. Factorial ratios for k+1 versus k are proportional to (u-q)/(2u-q-1), u=n-t,q=k-r; its derivative in u equals (q-1)/(2u-q-1)^2, and the larger-k distribution additionally excludes the rightmost t. This proves nonincreasing likelihood ratio and strict first-order stochastic dominance at every admissible comparison. At q=1 the common-support ratio is constant and the new law is precisely a truncation; the removed atom and TV distance equal n(k-1)/(k(2n-k-1)). Independent exhaustive balanced-walk enumeration verified all laws, likelihood ratios and boundary for 2<=n<=7. Boundary r=k is deterministic T_r=n and is treated separately.

## originality

PASS

The chronological return-time family conditional on total zero visits forms a strict finite MLR/stochastic hierarchy. Existing main reference enumerates longest ranked excursion durations, which is a different statistic from chronological r-th return given K. Catalan excursion counting is classical. The precise finite MLR ratio plus exact exceptional truncation/TV appear not covered by the inspected primary sources, but an unindexed earlier composition-comparison lemma could imply it.

## value

PASS

Conditional chronological return times are basic path observables. The theorem provides an exact all-size, all-rank stochastic monotonicity hierarchy, stronger than expectation monotonicity, and identifies a sharp boundary where the comparison becomes literal truncation with exact TV distance. It answers a motivated relation between contact number and excursion chronology, not a numerical edge case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
