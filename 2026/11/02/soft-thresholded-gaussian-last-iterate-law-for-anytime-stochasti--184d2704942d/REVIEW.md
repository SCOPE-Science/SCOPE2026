# Scientific review

## Correctness
PASS. The proof supplies an explicit deterministic discrete sign-drift tracking bound, a Lindeberg central limit theorem for the early weighted Rademacher sum, a maximal-martingale inequality showing late stochastic fluctuations vanish, and a uniform-integrability bound for expectations. Gaussian integration and monotonicity of an exact integral prove the coefficient and unique tuning. The standalone finite checks corroborate, without substituting for, these infinite-parameter arguments. Assumptions and quantifiers are specified in RESULT.md.

## Originality
PASS under accessible-source comparison, subject to specialist historical priority. The full motivating July 2026 paper was inspected, including the complete proof of its expected-rate lower bound; it does not state the proposed weak soft-threshold distribution, limiting zero atom, coefficient, or unique within-family optimum. Other publicly described analyses consider fixed-horizon constant steps, not this anytime schedule. Comparisons against accessible mathematical research records about absolute-value objectives, scalar stochastic approximation, and last-iterate bounds did not expose a covering distribution theorem. One plausible related full text was inaccessible; its distinct abstract setting and the residual priority risk are documented in AUDIT.json. Nonidentification in a database is not a proof of global novelty.

## Value
PASS. The existing sharp logarithmic expected-error rate leaves open whether the lower-bound phenomenon arises in rare catastrophes or is present at ordinary fluctuation scales. The exact weak law, its positive limiting zero mass and full exceedance curve answer that reliability question. The sharp leading expectation coefficient and optimal tuning also provide a natural benchmark for lower-bound constructions, without claiming an unrestricted minimax optimum.

## Boundaries
Only one-dimensional, horizon-dependent absolute-value objectives, independently sampled bounded symmetric noise, the anytime \(\gamma/\sqrt t\) schedule, and exact arithmetic are covered. The weak-limit atom does not imply an atom at zero for any finite horizon. Independent audit and exhaustive historical-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
