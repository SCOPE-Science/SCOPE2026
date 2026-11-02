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

For each fixed even n the multinomial triangular CLT yields the centered normal vector (G_j-Gbar)/sqrt(n) plus kappa n^(-3/4) epsilon_j. The Pearson limit is the corresponding sum of squares, and D/sqrt(N) is a sum of absolute adjacent Gaussian differences. The null Gaussian edge array is one-dependent, with Var(|G_2-G_1|)=2-4/pi and adjacent covariance=1/3+(2sqrt(3)-4)/pi; its long-run variance is sigma^2. The cross moment Cov(|G_2-G_1|,G_1^2-1)=1/sqrt(pi) follows exactly by conditional Gaussian regression and absolute third moments. Even folded-normal mean expansion yields D shift 2kappa^2/sqrt(pi); the random perturbed-edge fluctuation vanishes and Pearson has deterministic shift kappa^2/sqrt(2). The bivariate CLT and inversion of its covariance establish the stated negative optimal Pearson coefficient; normalization and boundary kappa=0 checked. Independent numerical Gaussian cross-moment, folded-normal Taylor, covariance inversion and ratio checks passed.

## originality

PASS

Best-of-knowledge new joint Gaussian alternative-power law, cross-statistic covariance and optimal two-statistic combination. The original Comb Test establishes empirical advantages, and the 2026 null-moment papers establish distinct null mean/variance contributions that are credited, but none inspected statement specifies this iterated shrinking period-two alternative law. Full Part 2 text was not accessible and remains a concrete originality risk.

## value

PASS

The recent comb test is expressly motivated by alternating ordered-bin departures. This gives a rigorous Gaussian power comparison in precisely that natural regime, including how dependence with Pearson changes optimal combined screening. The negative Pearson coefficient is a non-obvious dependence effect. No unrestricted Pitman-efficiency or simultaneous sample/bin limit is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
