---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Uniform weak compositions yield exact one- and two-part marked stars-and-bars probabilities and a positive normalized cross-moment R for 1<=r<s, r+s<=n, k>=2. For k>2, the logarithmic derivative has sign 2-(s+1)T(k), with T a strictly increasing sum of x/(x+A_j)*(x-2)/(x+B_j), A_j>0 and B_j>=-2. At n=r+s it decreases throughout (the limit at 2 gives equality at the derivative endpoint), otherwise R rises once and falls once; its large-k limit (n-r)_s/(n)_s<1 yields one finite consecutive positive covariance band. Direct separate weak-composition enumeration and exact fractions reproduced n=10,r=1,s=6: k=2..7 ratios 0,22/25,26/25,26/25,1,20/21. This is an all-n,r,s proof; finite checks corroborate only bounded examples.

## originality

PASS

Best-of-knowledge PASS for the varying-category unimodality/covariance-positive interval, not for the known occupancy factorial moments. Huillet–Martínez gives general mixed factorial moments; specializing these moments does not without a further nontrivial inequality state the sign-band theorem. Huillet–Paroissin gives Dirichlet(1) sampling, not the shape theorem. Related published SCOPE findings concern iid occupancy richness-versus-count and a uniform-composition maximum, not this two-frequency covariance under growing k.

## value

PASS

Pairwise covariance of two abundance frequency classes is a natural statistic for species occupancy under Dirichlet-multinomial sampling. An exact one-band sign law prevents multiple correlations changing sign as category count increases and the explicit two-reversal witness demonstrates content beyond routine moment computation. It is an all-parameter structural shape theorem with a potentially useful parameter threshold, not merely one small experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
