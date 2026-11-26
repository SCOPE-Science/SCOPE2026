---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Grouping the unspecified colours in the symmetric Dirichlet mixture gives the reported rising-factorial formulas for p_m and q_m. Two colours and three draws force q_2=0, so the covariance is strictly negative there; strict ratio monotonicity is asserted only for m>=3. For those m the covariance sign is that of q_m/p_m^2-1. The k=0 terms cancel in the logarithmic derivative; the remaining three grids give the discrete second difference of F_s. The Laplace representation follows by the finite geometric sum, and (exp(u/s)-1)^(-1) is strictly convex in s>0: the bracket in its second derivative is B(x)=x(exp(x)+1)-2(exp(x)-1) with B(0)=B'(0)=0 and B''(x)=x exp(x)>0. The strictly positive discrete second difference integrates against a positive weight. The small-mass limit is below one by (2m-1)/((m+1)(m-1)^3); the large-mass limits are 243/256 and 32768/32805 for m=3,4. For t=m-1>=4 the truncated alternating binomial series is a lower bound (successive terms decrease), and multiplying out gives the stated polynomial with positive coefficients after t=u+4. Hence each m>=5 crosses once and only once. A separate exact sequential state recursion reproduced both m=5 covariances, and numerical bisection gave 0.3168812738193324758.... Another exact composition enumeration checked the two probability formulas and normalization for m=2 through 6 and alpha=1/4,1,2.

## originality

PASS

The exact event probabilities follow from the classical law, and the alpha=1 slice for these very indicators is already known in a broader sample-size window. The supported distinct claim is the strict concentration monotonicity of the ratio and the existence and uniqueness classification in alpha at N=m+1, not the single slice or either standard occupancy law. No inspected statement implies this varying-alpha result.

## value

PASS

The first overfull sample size is a natural occupancy boundary at which repetitions are forced. A complete all-alphabet classification for two nonlinear indicators, including a separation from negative count covariance and a proof of exactly one concentration crossing, answers a concrete dependence question that neither the fixed-mass occupancy comparison nor an isolated sign example resolves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
