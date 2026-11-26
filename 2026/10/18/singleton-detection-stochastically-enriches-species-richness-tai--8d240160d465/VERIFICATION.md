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

Conditional on tag count y, the untagged sample is uniform of size m-y in the untagged census, or iid of that size with probabilities renormalized on the untagged categories. Couple all feasible untagged sample sizes by prefixes. Richness R_l is nondecreasing and increases by at most one per draw. Thus R_m <= 1+R_(m-1) if count zero is feasible, and 1+R_(m-y) <= 1+R_(m-1) for y>=2; the right-hand side is exactly the singleton-conditioned law. This proves every fixed-count comparison, not just comparison to the mixture. Feasibility ensures the needed prefix lengths exist; for one species only length zero is needed and richness is constant. Averaging and applying each monotone score prove the indicator covariance, summing proves the F_1 covariance, and dividing the tail covariance by E[F_1]>0 proves size-bias dominance. Zero singleton-event probability gives zero indicator covariance, not a conditional law. For sample size r+1 with two equal abundances r+1, exactly two out of B=binom(2r+2,r+1) subsets have richness one, while (r+1)^2 subsets have tag count r and richness two. This gives 2(r+1)^2/B^2. In the profile with tag abundance r and r+1 other singletons, K=2 on count r and K>=3 at every smaller feasible count, with both events possible. These signs concern a tagged indicator, not the general total F_r. Separate integer count-vector dynamic programming reproduced 9,666 selected fixed-count inequalities and both finite-census signs for every 2<=r<=20 (workspace checks/frozen_checks.py, argument 3; output checks/3.txt); the unrestricted result is the coupling proof, not the finite calculation.

## originality

PASS

The supported contribution is tagged count-one stochastic maximality among all feasible tag counts in both sampling schemes, its monotone-score consequences, and the tagged higher-frequency contrast at a common finite-census sample size. Uniform-iid positive covariance with total singleton count is known and not novel here. The strongest inspected related results do not establish the two-scheme fixed-tag order; this is a bounded best-of-knowledge assessment.

## value

PASS

The result gives a sharp, distribution-free conditional tail comparison for a common rarefaction or occupancy statistic. The size-biased richness law and all monotone scores are consequences that a mere covariance sign cannot establish, and the common-depth exact-frequency examples delimit the mechanism. No claim is needed about uncontrolled field sampling, weighted diversity, or estimator quality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
