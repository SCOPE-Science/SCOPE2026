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

The theorem is analytic. The accompanying script uses only exact rational
arithmetic.

For thousands of rational Poisson-binomial backgrounds it:

1. constructs the background mass function by exact convolution;
2. balances a selected Bernoulli pair while preserving its sum;
3. checks the exact second-difference probability-mass identity;
4. checks the telescoping first-difference CDF identity;
5. verifies total variation, Kolmogorov distance, and integer-line
   Wasserstein distance from both their definitions and the closed formulas;
6. verifies the stop-loss identity for every threshold intersecting the
   support;
7. removes zero second-difference coefficients and checks exactly two sign
   changes with the pattern \(+,-,+\);
8. checks background unimodality and
   \[
   \sum_k|\Delta a_k|=2\max_k a_k.
   \]

The real-rooted coefficient-sign lemma and the Poisson-binomial
real-rootedness argument in `RESULT.md` prove the crossing statement for all
parameters. Finite replay is not used as a proof of the universal theorem.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK pmf_checks=125741 cdf_checks=161741 metric_checks=54000 stoploss_checks=197741 crossing_checks=18781 variation_checks=18781`.
