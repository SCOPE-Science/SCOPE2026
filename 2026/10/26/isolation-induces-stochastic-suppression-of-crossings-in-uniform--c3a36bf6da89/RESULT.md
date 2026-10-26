# Isolation induces stochastic suppression of crossings in uniform chord diagrams

## Finding

Let \(C_n\) be the number of pairs of crossing chords and \(I_n\) the number of chords that cross no other chord in a uniformly random matching of \(2n\) cyclically ordered labeled endpoints. For every integer \(n\ge2\) and every nondecreasing function \(g:\{0,\ldots,\binom n2\}\to\mathbb R\),

\[
\operatorname{Cov}(I_n,g(C_n))\le0.
\]

The inequality is strict whenever \(g\) is strictly increasing. Equivalently, the \(I_n\)-size-biased law of \(C_n\), defined by \(\Pr_*(C_n\in B)=\mathbb E[I_n\mathbf1_{\{C_n\in B\}}]/\mathbb E[I_n]\), is smaller than the ordinary crossing-count law in usual first-order stochastic order.

For a designated chord \(c\), let \(A_c\) denote that it occurs and is isolated. If its two open circular arcs contain exactly \(2k\) and \(2(n-1-k)\) endpoints, then, conditional on \(A_c\),

\[
C_n\ \stackrel{d}{=}\ C_k^{(1)}+C_{n-1-k}^{(2)}\ \le_{\mathrm{st}}\ C_{n-1}\ \le_{\mathrm{st}}\ C_n,
\]

where the two summands are independent uniform-matching crossing counts, and \(C_0=0\). Its exact crossing-mean deficit relative to the unconditioned diagram is

\[
\mathbb E[C_n\mid A_c]-\mathbb E[C_n]
=-\frac{n-1+k(n-1-k)}3.
\]

Put \(M_j=(2j-1)!!\) for \(j\ge0\), with \(M_0=1\). The exact mixed covariance is

\[
\operatorname{Cov}(I_n,C_n)
=-\frac{n}{3M_n}\sum_{k=0}^{n-1}M_kM_{n-1-k}\bigl(n-1+k(n-1-k)\bigr)<0.
\]

In particular, the full finite-size expansion begins

\[
\operatorname{Cov}(I_n,C_n)
=-\frac n3-\frac16-\frac{5}{6n}+O(n^{-2})
\qquad(n\to\infty).
\]

## Assumptions and scope

Endpoints \(1,\dots,2n\) are placed around a circle in that order. All \((2n-1)!!\) perfect matchings of them are equally likely. Two chords cross exactly when their endpoints alternate around the circle. A chord is isolated if its vertex has degree zero in the corresponding intersection (circle) graph. The random variable \(C_n\) counts graph edges and \(I_n\) counts isolated graph vertices. The stochastic order means \(\mathbb E[g(X)]\le\mathbb E[g(Y)]\) for every nondecreasing real function on the finite support.

The size-biased distribution is **not** the distribution conditional on \(I_n>0\). The theorem concerns the expectation weighting by \(I_n\), not conditional negative association given any prescribed number of isolates.

## Proof

**1. A coloring-and-deletion coupling.** Generate a uniformly random matching with \(m=a+b\) chords, then independently select exactly \(a\) of its chords uniformly and color them red, the remaining \(b\) blue. Delete blue endpoints, retaining the cyclic order of the red endpoints, and likewise form the blue induced diagram. Both resulting matchings are independent and uniform on \(2a\) and \(2b\) endpoints: for each prescribed endpoint-color set of size \(2a\), each pair of within-color matchings has the same probability \(1/(M_m\binom ma)\). The identity \(\binom{2m}{2a}M_aM_b=\binom ma M_m\) confirms normalization and the uniformity of endpoint-color sets. Every crossing of two chords of one color is still a crossing of the original matching. Therefore under this coupling the sum of the two induced crossing counts is pointwise no greater than the full crossing count. Thus \(C_a^{(1)}+C_b^{(2)}\le_{\mathrm{st}}C_{a+b}\). Separately, deleting one uniformly chosen chord from a uniform matching of \(m+1\) chords produces a uniform matching of \(m\) chords in induced order, while never creating crossings. Hence \(C_m\le_{\mathrm{st}}C_{m+1}\). The latter comparison is strict for every \(m\ge1\) under strictly increasing test functions, because the deleted chord crosses another with positive probability.

**2. Conditional isolation.** Fix an unordered endpoint pair \(c\) for which each of the two arcs contains an even number of remaining endpoints, say \(2k\) and \(2\ell\), with \(k+\ell=n-1\). The event \(A_c\) occurs precisely when the pair \(c\) is matched together and every other pair lies entirely within one of its two arcs. There are \(M_kM_\ell\) matching completions, and so

\[
\Pr(A_c)=\frac{M_kM_\ell}{M_n}.
\]

Conditional on this event, both within-arc matchings are independent and uniform. They cannot cross one another or the designated chord, proving \(C_n\mid A_c\stackrel d=C_k^{(1)}+C_\ell^{(2)}\). Step 1 then gives the stochastic inequality for each \(c\). Pairs having an odd number of endpoints in either arc cannot be isolated and contribute probability zero.

**3. Isolation-weighted stochastic dominance.** Write \(I_n=\sum_c\mathbf1_{A_c}\), over all unordered endpoint pairs. For any nondecreasing \(g\), Step 2 gives

\[
\mathbb E[I_ng(C_n)]
=\sum_c\Pr(A_c)\mathbb E[g(C_n)\mid A_c]
\le\mathbb E[I_n]\mathbb E[g(C_n)].
\]

Each event with positive probability gives a strict inequality if \(g\) is strictly increasing, by the strict deletion coupling in Step 1; there are such events for every \(n\ge2\). This proves the claimed strict negative covariance and the equivalent size-biased stochastic ordering.

**4. Exact means.** In a uniform matching with \(j\) chords, each unordered pair of chords crosses with probability \(1/3\) (the three matchings of its four induced endpoints are equiprobable), giving \(\mathbb E[C_j]=j(j-1)/6\). Consequently

\[
\mathbb E[C_n\mid A_c]-\mathbb E[C_n]
=\frac{k(k-1)+\ell(\ell-1)-n(n-1)}6
=-\frac{n-1+k\ell}3.
\]

For each \(k=0,\ldots,n-1\), there are exactly \(n\) unordered candidate endpoint pairs when counted according to a chosen circular arc containing \(2k\) endpoints: a directed choice of starting endpoint gives \(2n\) possibilities, and identifying the two orientations of each chord contributes the factor \(1/2\), including the equal-arc case. Summing the probability in Step 2 and the mean deficit therefore yields

\[
\operatorname{Cov}(I_n,C_n)
=\sum_c\Pr(A_c)\bigl(\mathbb E[C_n\mid A_c]-\mathbb E[C_n]\bigr)
=-\frac n{3M_n}\sum_{k=0}^{n-1}M_kM_{n-1-k}\bigl(n-1+k(n-1-k)\bigr).
\]

Every summand is positive when \(n\ge2\).

**5. Asymptotics.** Set \(m=n-1\) and \(W_k=M_kM_{m-k}\). Terms \(k=0,m\) contribute \(-2n(n-1)/(3(2n-1))\). Terms \(k=1,m-1\) contribute \(-2n/(3(2n-1))\). Terms \(k=2,m-2\) contribute \(-2n(3n-7)/((2n-1)(2n-3)(2n-5))\). Their total expands to \(-n/3-1/6-5/(6n)+O(n^{-2})\).

To bound the remainder, note

\[
\frac{W_k}{M_m}=\frac{\binom mk}{\binom{2m}{2k}}\le\frac1{\binom mk},
\]

by Vandermonde's convolution. For fixed \(k=3,4\) and their symmetric counterparts the ratio is respectively \(O(m^{-3})\) and \(O(m^{-4})\), and the multiplier \(m+k(m-k)\) is \(O(m)\). The central range \(5\le k\le m-5\) has \(W_k/M_m\le1/\binom m5=O(m^{-5})\), has at most \(m\) terms, and has multiplier \(O(m^2)\). Since \(nM_m/M_n=n/(2n-1)=O(1)\), the whole omitted contribution is \(O(m^{-2})\). This proves the expansion.

## Verification

The accompanying `verify.py` is an independent standard-library checker. It enumerates all \(135135\) matchings on fourteen endpoints, in addition to all smaller matching sizes, tests the isolation event law against independent products of crossing distributions, checks all thresholds of the asserted stochastic orders and the isolation-size-biased tail order, and verifies the exact covariance formulas. It reports 1037 exact-rational assertions passed. The arbitrary-size proof is combinatorial; finite enumeration and numerical asymptotic checks are supplemental rather than a substitute.

Run: `python verify.py`.

## Relationship to prior work

Flajolet and Noy (2000) gave marginal component-count and crossing-count distributions and asymptotic laws for random chord diagrams. Acan (2015) studied intersection-graph degrees and monolithic structure. Acan and Pittel (2014) studied crossing-conditioned, sparsely crossing component formation. Paguyo (2023) gave separate quantitative crossing-Gaussian and simple-chord-Poisson approximations. The present result concerns a different **joint** question: stochastic ordering of crossings under isolation-size-biasing, including all increasing test functions, together with a geometrically resolved exact mean deficit. The independence of colored induced submatchings is used here as a direct coupling proof.

## Limitations

This does not establish full negative association between arbitrary functions of \(C_n\) and arbitrary increasing functions of \(I_n\). It does not assert stochastic dominance after simply conditioning on \(I_n>0\), nor a joint limit theorem. Historical-priority searches can miss implicit corollaries of earlier bivariate generating functions, particularly broader component/crossing joint enumerations; independent literature validation has not occurred. The finding is proved for uniformly weighted matchings and may fail under nonuniform diagram weights.

## References

- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report 3914, March 4, 2000. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, January 7, 2015. https://arxiv.org/abs/1501.01489
- H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867, June 11, 2014. https://arxiv.org/abs/1406.2867
- J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, initial preprint 2021, revised January 11, 2023. https://arxiv.org/abs/2104.01134
