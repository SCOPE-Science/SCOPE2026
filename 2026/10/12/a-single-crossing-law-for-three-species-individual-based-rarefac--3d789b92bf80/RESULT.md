# A single-crossing law for three-species individual-based rarefaction

## Finding
For any two communities, each consisting of exactly three observed species and exactly \(N\) individuals, individual-based expected-richness rarefaction changes the *strict relative ranking* of the communities at most once as sample depth increases.

Precisely, let the strictly positive integer abundance triples be
\[
x=(x_1,x_2,x_3),\qquad y=(y_1,y_2,y_3),\qquad \sum_i x_i=\sum_i y_i=N.
\]
For each integer \(1\le m\le N\), sample uniformly without replacement and define
\[
R_m(x)=3-\frac{1}{\binom Nm}\sum_{i=1}^3\binom{N-x_i}{m},
\]
where a binomial coefficient with its lower argument larger than its nonnegative upper argument is zero. Delete zero entries from the finite sequence
\[
\operatorname{sgn}(R_2(x)-R_2(y)),\ldots,\operatorname{sgn}(R_{N-1}(x)-R_{N-1}(y)).
\]
**The remaining signs switch at most once.** Thus the preference cannot return to the original community after switching to the other.

There is a useful two-depth certificate. The two endpoint values are
\[
R_2(x)=2-\frac{\sum_i x_i(x_i-1)}{N(N-1)},\qquad
R_{N-1}(x)=3-\frac{f_1(x)}N,
\]
where \(f_1(x)\) is the number of singleton species in the census. If the two profiles are strictly ordered in the *same* direction at depths \(2\) and \(N-1\), they cannot strictly reverse anywhere between. If the signs at those two depths are opposite, exactly one switch must occur (after ignoring ties).

The one-switch bound is sharp. For
\[
x=(6,2,2),\qquad y=(5,4,1),\qquad N=10,
\]
we have
\[
R_3(x)=\frac{61}{30}<\frac{41}{20}=R_3(y),\qquad
R_4(x)=\frac{163}{70}>\frac{242}{105}=R_4(y).
\]

## Assumptions and scope
The census is finite. Every listed species has a strictly positive integer abundance. Both communities have exactly three species and the same total number of individuals. Species identities play no role, so profiles can be sorted before comparison.

Rarefaction is *individual-based* and *without replacement*, with the expected species count computed under the exact finite hypergeometric sampling law. Only integer depths are asserted; no conclusion is made about artificially interpolated curves or extrapolation beyond the full census.

A strict reversal is a change between signs \(+1\) and \(-1\). A tie can occur at some depths and is discarded in the sign sequence. In particular, agreement at an endpoint alone does not trigger the two-depth certificate if that agreement is merely a tie.

## Proof
Write both triples in decreasing order. If either sorted triple majorizes the other, the result follows at once: for every \(m\), the map
\[
f_m(j)=\binom{N-j}{m}
\]
is discrete convex, since
\[
f_m(j)-2f_m(j+1)+f_m(j+2)=\binom{N-j-2}{m-2}\ge0.
\]
A more unequal abundance triple therefore has a no-smaller sum of species-absence numerators, and hence no-greater rarefied richness at any depth. There can be no reversal.

Otherwise the sorted triples are incomparable under majorization. Relabel the two profiles as
\[
x=(a,b,c),\quad y=(A,B,C),\quad a\ge b\ge c>0,\quad A\ge B\ge C>0.
\]
After possibly interchanging the profiles, incomparability is exactly
\[
a>A,\qquad c>C.
\]
Equal totals then imply \(b<B\), and consequently
\[
C<c\le b<B\le A<a.
\]

For each abundance \(j\), define the signed frequency difference
\[
d_j=\#\{i:x_i=j\}-\#\{i:y_i=j\}.
\]
Because the triples have three entries and equal sum,
\[
\sum_j d_j=0,\qquad \sum_j j d_j=0.
\]
Let \(F_j=\sum_{k\le j}d_k\) and \(G_j=\sum_{t\le j}F_t\). Reading the ordered abundance sizes just displayed, \(F_j\) is \(-1\) on the integer interval \(C\le j<c\), \(+1\) on \(b\le j<B\), and \(-1\) on \(A\le j<a\), and zero elsewhere. Intervals with equal adjacent endpoints are simply empty.

Accordingly, the twice-cumulative sequence \(G_j\) first decreases from zero, then increases past zero, and finally decreases to zero. The equality of total abundances gives
\[
B-b=(c-C)+(a-A),
\]
so at the start of the final decreasing interval \(G_j=a-A>0\). Therefore **the nonzero signs of \(G_j\) occur in a negative block followed by a positive block**, with at most one sign transition.

Summation by parts twice, using the two moment cancellations above, yields the exact identity for each \(2\le m\le N-1\):
\[
H_m:=\sum_{i=1}^3\left[\binom{N-x_i}{m}-\binom{N-y_i}{m}\right]
=\sum_{j=1}^{N-2}G_j\underbrace{\binom{N-j-2}{m-2}}_{K(j,m)}.
\]
The kernel \(K(j,m)\) is nonnegative. It also satisfies, for \(j_1<j_2\) and \(m_1<m_2\),
\[
K(j_1,m_2)K(j_2,m_1)\ge K(j_1,m_1)K(j_2,m_2).
\]
Indeed, with \(u=N-j-2\), the ratio \(\binom{u}{m_2-2}/\binom{u}{m_1-2}\), wherever defined, is an increasing function of \(u\), because it is a product of factors \((u-r)/(r+1)\). Increasing the depth thus favors **smaller** abundance indices \(j\); boundary zeros preserve the displayed inequality.

To extract the sign consequence, split the sum for \(H_m\) into the absolute contribution \(A_m\) from the negative block of \(G_j\) and the contribution \(B_m\) from the positive block: \(H_m=B_m-A_m\). Every index in the negative block precedes every index in the positive block, so the kernel inequality implies
\[
A_{m_2}B_{m_1}\ge A_{m_1}B_{m_2}
\qquad(m_1<m_2).
\]
Thus, if \(H_{m_1}\le0\), then \(H_{m_2}\le0\), with the zero-weight cases following from the nested supports of the binomial coefficients. In particular, after the signs of \(H_m\) change from positive to negative, they cannot change back. Since
\[
R_m(x)-R_m(y)=-\frac{H_m}{\binom Nm},
\]
the nonzero rarefaction ordering signs change at most once. This establishes the theorem for every finite \(N\).

Finally, the exact endpoint formulas follow by counting ordered conspecific pairs for samples of size two and by observing that a sample omitting one individual misses a species if and only if that species is a singleton. The example in the Finding section proves the one-change upper bound is attained.

## Verification
The embedded standalone `verify_three_species_rarefaction_one_crossing.py` runs with the Python standard library and uses integer binomial coefficients and exact rational arithmetic.

It independently generates all positive three-part abundance multisets by ordered-partition enumeration and by compositions followed by sorting for every total through \(N=35\). It compares every unordered pair at all interior sample sizes and finds no pair with more than one sign change. It also independently checks the twice-cumulative identity for \(176194\) profile/depth cases through \(N=26\) and checks \(486980\) valid-order binomial-kernel minors through \(N=27\). The witness fractions and earliest ten-individual crossing are checked exactly.

Run:

`python3 verify_three_species_rarefaction_one_crossing.py`

Successful output begins with `VERIFY_OK`. These finite checks stress-test the formulas; the unbounded theorem follows from the argument in Proof, not from enumeration.

## Relationship to prior work
Heck, van Belle, and Simberloff established exact finite-census rarefied expected richness as a fundamental ecological statistic. Lande, DeVries, and Walla analyze why species-accumulation curves can cross and relate the early slope to Simpson diversity, but compare broader-community scenarios without an all-depth bound restricted to three species. Thompson and Withers explicitly exhibit crossings even at equal true richness by simulations involving many species; their simulations neither imply nor contradict the present three-species constraint.

Chao and Jost study size-based and coverage-based rarefaction, show that ranking reversals can matter for ecological interpretation, and relate counts of crossings between those two standardizations. They do not give a bound of one for the exact fixed-census hypergeometric curve with three observed species.

The new contribution is not the existence of a crossing, which is established. It is the **universal one-reversal ceiling for the smallest nontrivial fixed-richness case**, with an exact monotone-likelihood-ratio proof and a two-endpoint comparison certificate. An earlier exact ten-individual example independently demonstrates sharpness, but an example at one finite census alone cannot establish the all-census theorem.

## Limitations
The result describes expected richness under finite without-replacement sampling, not realized ranks in noisy samples, their confidence intervals, or inferred richness of unobserved species. It does not automatically extend to four or more observed species, unequal total census sizes, unequal observed richness, with-replacement sampling, or coverage-standardized curves.

A strict endpoint certificate requires both endpoint differences to be nonzero. If the singleton counts tie, the near-census endpoint is tied and the stated sufficient certificate is silent. The theorem itself remains valid.

This is a self-contained mathematical result under standard rarefaction assumptions. An equivalent single-crossing statement might exist under an unfamiliar formulation involving majorization, total positivity, or finite sampling transforms; search cannot prove nonexistence of such prior work.

## References
1. K. L. Heck Jr., G. van Belle, and D. Simberloff, “Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size,” *Ecology* 56 (1975), 1459–1461. DOI: 10.2307/1934716. Publisher first-publication date: 1975-10-01.
2. R. Lande, P. J. DeVries, and T. R. Walla, “When Species Accumulation Curves Intersect: Implications for Ranking Diversity Using Small Samples,” *Oikos* 89 (2000), 601–605. DOI: 10.1034/j.1600-0706.2000.890320.x.
3. G. G. Thompson and P. C. Withers, “Effect of Species Richness and Relative Abundance on the Shape of the Species Accumulation Curve,” *Austral Ecology* 28 (2003), 355–360. DOI: 10.1046/j.1442-9993.2003.01294.x.
4. A. Chao and L. Jost, “Coverage-Based Rarefaction and Extrapolation: Standardizing Samples by Completeness Rather than Size,” *Ecology* 93 (2012), 2533–2547. DOI: 10.1890/11-1952.1.
5. T. D. Olszewski, “A Unified Mathematical Framework for the Measurement of Richness and Evenness Within and Among Multiple Communities,” *Oikos* 104 (2004), 377–387. DOI: 10.1111/j.0030-1299.2004.12519.x.
