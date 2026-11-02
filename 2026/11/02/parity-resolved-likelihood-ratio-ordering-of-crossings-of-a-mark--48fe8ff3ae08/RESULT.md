# Parity-resolved likelihood-ratio ordering of crossings of a marked random chord

## Finding

Fix a chord in a uniform random diagram with \(n\ge3\) chords, and let \(X_a\) be its crossing degree when the shorter arc between its endpoints contains \(a\) other endpoints. For all \(0\le a<c\le n-1\) with \(a\equiv c\pmod2\),

\[
X_a<_{\mathrm{lr}}X_c.
\]

The strict likelihood-ratio ordering entails strict increasing crossing-degree upper tails at every nontrivial threshold. For the elementary step \(a\mapsto a+2\), the likelihood ratio is strictly increasing and crosses unity at the explicit cutoff

\[
x_*=\frac{(2n-2-a)(a+2)}{2n-1}.
\]

This supplies an exact monotone likelihood-ratio decision rule between equal-prior, same-parity candidate arc lengths given a measured crossing degree. The parity qualification is necessary: for every \(n\ge3\), \(X_1\) is constantly one, whereas \(X_2\) takes both zero and two with positive probability.

## Assumptions and scope

A chord diagram is a perfect matching of \(2n\) distinguished points arranged cyclically. All \((2n-1)!!\) matchings are equiprobable. Condition on the presence of a specified chord, so that its \(2n-2\) remaining endpoints form complementary arcs of lengths \(a\) and \(b=2n-2-a\), with \(0\le a\le n-1\). A chord crosses the specified chord precisely when its two endpoints lie in opposite arcs. Let \(X_a\) be the number of crossing chords under this conditional law; symmetry makes the choice of which chord with the same arc lengths immaterial. All stated claims are for integer \(n\ge3\), with valid integer arc lengths and the described conditional uniform matching; no independent-chord assumption is used.

For two laws on a common ordered lattice, the monotone likelihood-ratio relation means their probability-mass quotient increases on the smaller support, and extra mass in the larger law occurs only above the smaller support. Strictness is asserted by a nonconstant likelihood ratio or new upper-support mass, not by a strict difference at trivial thresholds.

## Proof

Put \(N=2n-2\) and \(b=N-a\). If exactly \(x\) pairs cross between the two arcs, there are \(\binom ax\binom bx x!\) ways to choose and match cross-arc endpoints. The remaining endpoints must match internally, giving \((a-x-1)!!(b-x-1)!!\) further matchings. Interpreting \((-1)!!=1\) and dividing by the \((2n-3)!!\) equiprobable residual matchings yields the exact law

\[
\Pr(X_a=x)=\frac{a!b!}{(2n-3)!!\,x!\,2^{n-1-x}\,((a-x)/2)!\,((b-x)/2)!},
\]

for \(x\in\{a\bmod2,a\bmod2+2,\ldots,a\}\), and zero otherwise. Because \(a\le b\), every listed value is feasible.

For \(0\le a\le n-3\), fix any \(x\) on the support of \(X_a\). Canceling factorials between the mass functions for \(a+2\) and \(a\), with the new complementary length \(b-2\), gives

\[
R_a(x):=\frac{\Pr(X_{a+2}=x)}{\Pr(X_a=x)}=
\frac{(a+2)(a+1)}{b(b-1)}\frac{b-x}{a+2-x}.
\]

The fraction \((b-x)/(a+2-x)\) strictly increases with \(x\) because \(b-(a+2)=2(n-a-2)>0\). Both masses are positive on the smaller support, and \(X_{a+2}\) has exactly one additional upper-support value \(x=a+2\), with positive probability. Hence \(X_a<_{\mathrm{lr}}X_{a+2}\) strictly. Finite transitivity over steps of two gives the result for every same-parity pair \(a<c\).

The sign of \(R_a(x)-1\) equals that of

\[
(2n-1)x-b(a+2),
\]

which proves the exact likelihood-ratio threshold. Standard finite-sum rearrangement (or the single-crossing property together with unit total mass) gives the strict upper-tail inequalities for all integer thresholds \(t\) satisfying \(a\bmod2<t\le a+2\); other thresholds may have coinciding trivial tails. For more widely separated same-parity lengths, strict stochastic ordering follows by chaining the adjacent steps.

For the sharp boundary, \(X_1=1\) deterministically because the sole endpoint on its small arc must match across. For \(a=2\), the two small-arc endpoints either match each other or match outside. The first event has probability \(1/(2n-3)\), so

\[
\Pr(X_2=0)=\frac1{2n-3},\qquad
\Pr(X_2=2)=\frac{2n-4}{2n-3}.
\]

Consequently \(\Pr(X_1\ge1)>\Pr(X_2\ge1)\), while \(\Pr(X_1\ge2)<\Pr(X_2\ge2)\), so even first-order stochastic ordering fails between adjacent opposite-parity lengths. This holds for the smallest eligible size \(n=3\).

## Verification

The embedded standalone `verify_chord_order.py` uses only Python standard-library exact integers and rational numbers. Run `python3 verify_chord_order.py` from the extracted artifact directory. It independently enumerates all residual perfect matchings for \(3\le n\le8\), verifies each exact conditional histogram, checks normalization and first two moments through \(n=64\), tests every common-support likelihood ratio and sign cutoff through \(n=64\), verifies strict upper-tail comparisons, and checks the parity obstruction through \(n=24\). In the reviewed execution it reported **119,211 exact assertions passed**. The finite enumeration corroborates the algebraic proof but does not substitute for the proof for arbitrary \(n\).

## Relationship to prior work

Hüseyin Acan, *On a uniformly random chord diagram and its intersection graph* (public arXiv version dated 2015-01-07, arXiv:1501.01489v1), Section 2, studies chord length and degree, gives exact first and second moments of the number of internal chords, and proves an asymptotic distribution for a uniformly chosen chord's degree. Since crossing degree equals arc length minus twice the number of internal chords, the basic marginal and moment framework is already known. An earlier 2013 dissertation by Acan develops related enumeration and asymptotics; its year-only dating is not used to invent a day-specific source date.

Chen, Deng, Du, Stanley, and Yan, *Crossings and Nestings of Matchings and Partitions* (arXiv:math/0501230, 2005), study crossing/nesting tableaux symmetries and maximal crossing statistics, not this conditional local-degree comparison. The contribution asserted here is the strict **cross-length likelihood-ratio order**, its exact threshold, and the sharp opposite-parity obstruction; neither counting matchings nor one-point degree moments is asserted as new. Bounded searches did not establish absolute historical priority.

## Limitations

The theorem concerns one specified chord conditioned present in a uniformly random perfect matching. It does not claim a monotone likelihood-ratio order across opposite parities, under nonuniform matching weights, or for the joint crossing degrees of several chords. The ordering is finite-sample and does not assert independence. An older general total-positivity theorem for two-color random pairings might imply the same statement; this historical-priority possibility remains unresolved. All exact arithmetic checks cover finite \(n\) only.

## References

- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (first public 2015-01-07), https://arxiv.org/abs/1501.01489.
- H. Acan, *An Enumerative-Probabilistic Study of Chord Diagrams*, PhD dissertation, The Ohio State University (2013); consulted as earlier related work with year-only date evidence.
- W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley, and C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, arXiv:math/0501230 (first public 2005-01-14), https://arxiv.org/abs/math/0501230.
