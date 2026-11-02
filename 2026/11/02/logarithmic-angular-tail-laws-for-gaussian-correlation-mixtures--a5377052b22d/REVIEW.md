# Scientific assessment: logarithmic Gaussian-correlation-mixture tails

## Correctness — PASS

The statement specifies independent standard normal innovations and an almost-surely subunit nonnegative random correlation whose endpoint survival probability is asymptotic to a positive constant times a positive power. Its proof establishes an exact Plackett/Tonelli integral for arbitrary mixing laws, a precise normal-quantile scaling, a global integrable bound at both endpoints, and the Gamma/elementary formulas. The assumptions and quantifiers are kept fixed throughout. The actual packaged numerical program checks the special-function and finite-scale formulas, but no inference from finitely many numerical tests to the asymptotic theorem is needed.

## Originality — PASS, with residual historical risk

The closest same-object work is Manner and Segers (arXiv:0912.3516v1), whose Section 3.2 and Proposition 4 establish zero tail dependence and the residual index one, without the sharp logarithmic coefficient and off-diagonal angular law. Koike, Hofert and Tsunekawa (arXiv:2604.05985v1) explicitly require a non-degenerate first-order tail copula for their tail-path framework; their theorem does not imply this limit for the class with identically zero first-order tail copula. Fixed-correlation Gaussian-tail estimates and Hüsler–Reiss near-perfect-correlation limits are related but are not themselves the evaluated mixture with a general regularly varying endpoint and its explicit uniform-correlation angular profile. Searches of mathematical research records, exact-copula formulations, and accessible primary papers did not reveal the full asserted result. A stronger, unindexed integration theorem remains a priority risk; this is not an assertion of exhaustive global novelty.

## Mathematical value — PASS

The result determines a natural quantitative invariant of a known near-asymptotically dependent probability model: the entire small-tail angular intensity. Neither a zero first-order tail coefficient nor the residual dependence exponent identifies the multiplicative logarithmic rate or the dependence on unequal thresholds. A universal endpoint-power classification, exact Gamma coefficients, and an elementary non-product two-threshold law can inform extreme-risk calibration. The extension from one special law to all endpoint regularly varying correlation laws is structural, not an arbitrary finite computation.

## Sources and limitations

Evidence consists of the directly inspected HTML text of arXiv:2604.05985v1 (especially Theorem 1 and its non-degeneracy assumption), the directly inspected arXiv:0912.3516v1 (Section 3.2, Proposition 4 and its proof), and accessible bibliographic material on fixed-correlation normal copulas. Uncertainty remains about broad, unpublished or unindexed Hüsler–Reiss mixture reductions; this is a historical-priority risk, not a gap in the presented mathematical argument. The proof is only pointwise in fixed positive threshold multipliers and only for the specified endpoint-power law. No external independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
