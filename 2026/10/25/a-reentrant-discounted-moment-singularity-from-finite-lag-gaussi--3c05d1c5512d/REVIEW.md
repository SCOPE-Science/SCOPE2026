# Scientific review

## Correctness — PASS

The exact Gaussian OU one-step law gives the estimated drift and uncentered quadratic coefficient without approximation. Integration of the zero-current stationary equation gives a normalized Student law with \(1+2/(1-e^{-ah})\) degrees of freedom; its variance matches \(\sigma^2/(2a)\) and fourth-moment integrability ends sharply at \(ah=\log3\). Generator action on quadratic and quartic monomials gives an exact two-equation moment system, whose positive forcing proves divergence at the discount boundary as well as strictly below it. The derivative of the lag-profile numerator has a strictly decreasing sign-test function on \((\log3,\infty)\), establishing one and only one interior maximum. Standard-library rational and time-domain checks support the exact algebra but are not relied on for infinitary claims.

## Originality — PASS, with priority risk

Lade (2009) already computes both exact finite-lag OU Kramers–Moyal coefficients. Monthus (2023), and independently the Pearson diffusion literature, already supply Student invariant laws and polynomial-moment recursions. The accepted mathematical distinction is only the **sharp, global, reentrant lag/discount fourth-moment evaluation phase diagram**, proved by optimizing the lag-substituted quartic growth exponent. The inspected source-specific treatments do not supply this conclusion as a theorem, nor was a matching published mathematical record identified. The combination is directly computable from known ingredients and could have been recorded under another terminology: this residual originality risk remains and should be independently checked before a stronger priority assertion.

## Mathematical value — PASS

The quartic cost is the first even polynomial cost able to separate matched invariant variance from explosive surrogate moments, so it is not an arbitrary exponent selection. At fixed discount, reducing an observation gap **or enlarging it past a second exact threshold** can restore a finite surrogate evaluation; such reentrance is invisible to invariant variance and local small-lag estimates. This gives a concrete diagnostic about when the uncentered second-increment continuous-time surrogate is unsuitable for fourth-order risk evaluation, without alleging failure of an algorithm under hypotheses it does not satisfy.

## Scope and limits

Only the exact-data scalar uncontrolled first-order surrogate is covered; no finite-sample guarantee, higher-order reconstruction, optimal-control theorem, or assertion about uninspected literature is supplied. Numerical thresholds are approximations, while existence and uniqueness are analytic. The closest sources are Bayraktar et al. (2026) Section 4.1, Lade (2009) Section 3, Monthus (2023) Sections III and XIII, and the general Pearson classification (Forman–Sørensen 2008).

Self-review: passed. Independent audit: not yet performed.
