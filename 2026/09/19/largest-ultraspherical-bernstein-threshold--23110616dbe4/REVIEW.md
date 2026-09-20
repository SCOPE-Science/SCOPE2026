# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The result uses three ingredients stated explicitly in Castillo's 2026 paper:

1. the arbitrary-\(d\) Laurent expansion
   \[
   G_{n,1,d}(\lambda)
   =
   h_n+\frac{h_n\{4d-(2h_n^2+2n-1)\}}{8\lambda}+O(\lambda^{-2});
   \]
2. the largest-branch boundary orientation and sublinear local growth used in
   Proposition A.4;
3. the Pick--Bernstein characterization of complete Bernstein functions.

For \(d<d_n^\star\), the Laurent coefficient is negative, so the source's boundary
minimum proof applies unchanged. At \(d=d_n^\star\), local uniform convergence from
subcritical \(d\) preserves the Pick property on the common slit domain. For
\(d>d_n^\star\), the positive Laurent coefficient forces the derivative to be
negative for sufficiently large positive parameter, excluding both monotonicity and
complete Bernstein behavior.

The endpoint closure was checked separately because the source's original
large-circle argument uses a strictly negative \(1/\lambda\) coefficient and hence
does not directly cover the vanishing-coefficient case.

The Airy correction follows algebraically from DLMF 18.16.17--18:
\[
h_n=(2n+1)^{1/2}+2^{-1/3}a_1(2n+1)^{-1/6}+O(n^{-5/6}).
\]

## Originality

**PASS, to the best of our knowledge.**

The nearest source is Castillo, arXiv:2609.19186. Its Theorem A.3 gives the exact
threshold for nonlargest zeros, while Proposition A.4 gives only
\(d\le\lceil n/2\rceil\) for the largest zero and immediately states:
"This proposition asserts sufficiency only. No optimality of its upper endpoint is
claimed." The present theorem supplies that missing largest-zero if-and-only-if
classification and closes the complete square-root-scale phase diagram.

Searches were made for exact and synonymous formulations involving ultraspherical
and Gegenbauer zeros, largest-zero monotonicity, square-root scales
\(\sqrt{\lambda+d}\), complete monotonicity, complete Bernstein/Pick functions,
Hermite limits, and optimal scale constants. No equivalent statement or stronger
general theorem implying the claimed threshold was located.

Relevant older literature includes Ahmed--Muldoon--Spigler (1986),
Elbert--Siafarikas (1999), and Gautschi (2018). Their accessible descriptions concern
first-derivative monotonicity for distinguished scales and conjectured higher
monotonicity, not the all-\(d\) complete Bernstein threshold above.

### Residual literature risk

The full text of Elbert--Siafarikas (1999) was not independently inspected here; its
published abstract/secondary descriptions state the distinguished-scale monotonicity
result. Likewise, the complete text of Ahmed--Muldoon--Spigler (1986) was not
independently inspected beyond the accessible journal abstract and the detailed
historical account in Castillo's paper. These are the older sources most plausibly
capable of containing a related optimal first-derivative scale statement. Such a
statement, even if present, would not by itself establish the complete Bernstein
if-and-only-if classification, but it could reduce the novelty of the real-variable
necessity observation.

The direct 2026 source is very recent, so unindexed contemporaneous follow-up work is
also a residual risk.

## Value

**PASS.**

The source paper explicitly leaves the largest-zero endpoint unoptimized. The result
turns its one-sided sufficient range into an exact phase transition, completes the
classification already available for every other positive zero, and identifies a
different governing mechanism: the largest Hermite edge rather than the zero index.
The asymptotic \(d_n^\star\sim 3n/2\) also shows that the previously certified
largest-zero range, asymptotic to \(n/2\), is far from the true complete-Bernstein
boundary.

## Limitations

The statement is restricted to square-root scales with constant shift \(d\). It does
not classify arbitrary scale functions, finite-order sign patterns outside the
complete-monotone regime, or analogous Jacobi families with unequal parameters.

**Same-model review: passed. Independent audit: not yet performed.**
