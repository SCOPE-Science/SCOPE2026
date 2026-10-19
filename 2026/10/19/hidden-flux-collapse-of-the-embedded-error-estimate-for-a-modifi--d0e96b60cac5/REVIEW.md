# Review of hidden-flux masking for MPRK22(1)

## Correctness — PASS
The claim concerns every strictly positive four-tuple of starting populations, physical rate and timestep, and every nonnegative cancellation parameter. The independent two-by-two linear systems yield the exact stage transfer (1), output transfer (2), and positive embedded difference (3). The limiting constants follow from the explicit coefficient limits. Both numerical stages remain positive and conservative. The exact ODE displacement is strictly positive and independent of the cancellation parameter. The code checks rational instances but does not prove the universal result; the written algebra does.

## Originality — PASS, qualified by bibliographic uncertainty
The 2022 two-species nonlinear PDS stability paper and the complete accessible 2026 flux-balanced manuscript concern different claims. The accessible 2026 controller article supplies precisely the numerical formulas and acknowledges the nonuniqueness of PDS representations, but does not state the exact artificial-flux limit or the arbitrarily misleading embedded estimate for an unchanged ODE. Semantic research-record searches and title/claim overlap checks found no stronger equivalent statement; this is not a proof that a specialized earlier derivation is absent. The inference compares mathematical implications rather than titles.

## Mathematical value — PASS
This is a specific structural failure mode for error control in conservative positivity-preserving integration: the method's stage discrepancy can become uninformative solely from the choice of positive production/destruction decomposition, without altering the Jacobian or exact dynamics. The exact inverse-strength coefficient and conservative positive witness demonstrate a limitation not addressed by positivity, conservation, or formal fixed-decomposition order conditions. The result motivates diagnosing reaction-flux cancellation or using genuinely decomposition-robust error information, but does not itself validate a replacement estimator.

## Limits and competing coverage
The result is restricted to one embedded MPRK22(1) step, positive two-component input, exact arithmetic and an auxiliary mass-action flux parameter. Prior literature gives the underlying integrator, its positive/conservative character, and error estimator; these are not new. A specialized previous numerical-analysis observation might already express the same cancellation mechanism; the full search is necessarily nonexhaustive. No independent examination has occurred.

Self-review: passed. Independent audit: not yet performed.
