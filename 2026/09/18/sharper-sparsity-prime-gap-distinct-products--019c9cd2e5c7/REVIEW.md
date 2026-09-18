# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The key improvement is a degree-ratio stratification inside the
split-product curve estimate already proved in the source literature. If the
reduced numerator \(u=r/\gcd(r,s)\) equals \(2\), then the reduced denominator
must equal \(1\), so \((r,s)=(2h,h)\); this leaves only one parameter \(h\),
not the two-parameter family used in the published crude summation. Summing
the uniform curve estimate over this subfamily gives
\(X^{1/2+5\theta+o(1)}\). The complementary family \(u\ge3\) contributes only
\(X^{1/3+6\theta+o(1)}\), so at \(\theta=1/20\) the raw exponent is \(3/4\).

Substitution of \(3/4\) into the independently published length-sensitive
forest summation gives exponent \(13/16\) for the all-equal descendant term.
The competing contributions are \(4/5\), \(103/156\), and \(115/156\), all
strictly smaller. The monotonicity coefficients are \(37/95\) and \(205/741\),
both positive. These exact rational identities are reproduced by the included
verification script.

The parameterized formula
\[
F(\theta)=\frac12+\frac{13}{2}\theta-5\theta^2
\]
follows by the same substitution. At the Li threshold \(2/43\) it equals
\(2927/3698\). The branch inequalities are strict at that endpoint, so the
argument remains valid in a sufficiently small right neighborhood. Li's
Theorem 1.1 explicitly permits an exceptional set
\(O(X(\log X)^{-B})\) for arbitrarily large sufficiently fixed \(B\), which
also supports the stated all-log-powers complement bound after dyadic
summation.

No empirical computation is used as a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** The current arXiv version of
Chojecki's paper was inspected through the theorem statements and Sections
2--4 relevant to the construction, curve count, raw-gap summation, and forest
bound. It states raw exponent \(4/5\) and short-gap mass exponent \(9/10\).
The pinned public audit by Rob Sneiderman was inspected in the corresponding
sections; it improves the short-gap mass to \(43/50\) by length-sensitive
equal-chain summation but retains the same \(4/5\) raw-gap exponent.

Repository searches found no existing SCOPE record on this object, claim
family, source paper, or synonymous rejected-gap formulation. External
searches for the exact exponents \(3/4\), \(13/16\), and \(2927/3698\)
together with the distinct-consecutive-products setting found no matching
theorem. The exact source code of Sneiderman's refinement was also searched
for these formulations without a match.

The main residual risk is Ryan Kielhorn's September 2026 Zenodo preprint,
DOI 10.5281/zenodo.21287064. Its abstract and the public description of its
formalization were accessible and were inspected. They establish a
density-one distinct-consecutive-products construction using prime-gap
deletions and connector intervals, but the full mathematical preprint was not
inspected here. Because its construction is closely related, it could contain
an unindexed quantitative estimate comparable to the present one.

## Value

**PASS.** The result improves a recent quantitative boundary twice over:
\(9/10\) in the current primary preprint and \(43/50\) in the public expanded
audit become \(13/16\) for the same short-gap mass at the paper's fixed
parameter. The mechanism is structural rather than numerical: the reduced
degree ratio in the curve bound reveals that the worst \(B^{1/2}\) case is a
one-parameter family. The parameterized form also identifies the limiting
short-gap exponent \(2927/3698\) allowed by the present almost-all
short-interval input and extracts an all-logarithmic-powers rate of density
convergence for the canonical set.

## Review status

Same-model review: passed. Cross-model review: not yet performed.
