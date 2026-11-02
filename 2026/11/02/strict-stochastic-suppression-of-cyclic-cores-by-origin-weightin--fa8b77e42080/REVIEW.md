# Review: stochastic order of cyclic cores under origin weighting

## Correctness — PASS

The claim is defined for every finite \(n\ge2\) and real \(1\le s<t\). Conditional on any prescribed set of origins, all remaining arrows form an independent uniform map on the complement, proving the factorial moment identity. The binomial expansion for \(t\ge1\) has nonnegative coefficients and produces the exact mixture over sizes. The cyclic-core tail is exactly \((m)_{\underline k}/m^k\), strictly increasing with \(m\), and the mixing index increases strictly in likelihood-ratio order with \(t\). This establishes the entire strict stochastic-order claim, including the boundary \(s=1\). The covariance and correlation constants follow by exact moment identities and justified Gaussian-scale Riemann limits. A standalone exhaustive verifier checked every map through size seven (486 exact assertions), but the finite checks are not used as infinite proof.

## Originality — PASS, qualified

Arney–Bender (1982) develops origin-fugacity generating functions and cyclic-structure asymptotics, while Hansen–Jaworski (2006, Theorem 1) establishes a broader indegree-based formula for the *marginal law* of cyclic-point counts. Those stronger counting frameworks are acknowledged; neither of the inspected sections establishes the strict **comparison of entire cyclic-vertex distributions between every pair of fugacity values**, and the proof here supplies the missing positive-mixture and likelihood-ratio ordering. The general marginal formula can specialize to this measure, so the novelty claimed is the monotonicity theorem, not the parameterized marginal distribution. The 2010 rooted-forest work addresses conditioning on cyclic count, not comparison under origin weighting. Historical priority risks remain from the full random-mapping and stochastic-order literature, including Flajolet–Odlyzko (1990), whose full text was not retrieved in this review. Independent comparison is still necessary.

## Value — PASS

The natural question is whether favoring indegree-zero labels forces smaller directed cyclic cores or merely lowers their mean. Proving strict first-order stochastic order answers *all* threshold and monotone-loss questions uniformly in system size and degree of weighting. The positive mixture exhibits the mechanism at finite \(n\), while the sharp negative covariance and decaying-correlation constant quantify the unweighted competition between origins and core size. This is structural information not supplied by an isolated moment computation.

## Scientific boundaries

Only \(t\ge1\) is established; the conditional-forest occupancy formula is included for derivation and checking, not as an independent novelty claim. The asymptotic covariance is for the unbiased model. Broad earlier enumeration frameworks may yield further equivalent forms on specialization.

Self-review: passed. Independent audit: not yet performed.
