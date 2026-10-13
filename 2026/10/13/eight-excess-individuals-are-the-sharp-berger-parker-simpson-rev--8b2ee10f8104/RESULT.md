# Eight excess individuals are the sharp Berger–Parker–Simpson reversal boundary
## Finding
Fix
\[
k\ge3
\]
species with positive integer abundances
\[
n_1,\ldots,n_k\ge1
\]
and common total
\[
\sum_{i=1}^k n_i=N.
\]

Write
\[
r=N-k
\]
for the number of individuals remaining after assigning one mandatory individual to each species.

Berger–Parker dominance is
\[
B
=
\frac{\max_i n_i}{N}.
\]

Use Simpson concentration in the population-proportion form
\[
S
=
\sum_{i=1}^k
\left(\frac{n_i}{N}\right)^2.
\]

Both indices increase with concentration.

For every fixed
\[
k\ge3,
\]
no two such communities receive opposite strict rankings from \(B\) and \(S\) while
\[
r\le7.
\]

At
\[
r=8,
\]
strict reversal appears for the first time.

A witness valid for every
\[
k\ge3
\]
is
\[
A
=
(\underbrace{1,\ldots,1}_{k-3},2,3,6)
\]
versus
\[
C
=
(\underbrace{1,\ldots,1}_{k-2},5,5).
\]

Both have total
\[
N=k+8.
\]

Berger–Parker gives
\[
B(A)=\frac6{k+8}
>
\frac5{k+8}
=
B(C),
\]
so \(A\) is more dominated by its single largest species.

Simpson gives
\[
S(A)
=
\frac{k+46}{(k+8)^2}
<
\frac{k+48}{(k+8)^2}
=
S(C),
\]
so \(C\) is more concentrated in squared abundance.

For three species, this becomes the sharp eleven-individual pair
\[
A=(2,3,6),
\qquad
C=(1,5,5).
\]
It is the unique first-layer reversal up to species permutation.

At the same sharp excess level \(r=8\), the number of unlabeled reversing excess-partition pairs is
\[
1,\ 2,\ 3,\ 4
\]
for
\[
k=3,\ 4,\ 5,\ k\ge6,
\]
respectively.

The result is unchanged if Simpson concentration is computed in the finite-sample without-replacement form
\[
S_{\mathrm{fin}}
=
\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]
For fixed \(N\),
\[
\sum_i n_i(n_i-1)
=
\sum_i n_i^2-N,
\]
so the two Simpson formulas induce exactly the same ranking.

For two species, Berger–Parker and Simpson never reverse at any resolution.

## Assumptions and scope
The communities being compared have the same number of species and the same total number of individuals.

Every species is present with positive integer abundance. The integer unit is an individual count.

Berger–Parker is used as a dominance index, so larger values mean greater dominance. Simpson is likewise used in its concentration form, not as \(1-S\) or \(1/S\). Those monotone transformations reverse the diversity interpretation but do not change the underlying ordering information.

The theorem concerns ordinal comparison of diversity summaries. It does not state that one index is generally preferable for ecological monitoring.

## Proof
Write
\[
n_i=1+y_i,
\qquad
y_i\ge0,
\qquad
\sum_i y_i=r.
\]

At fixed \(k\) and \(r\), Berger–Parker ranking is exactly ranking by
\[
M(y)=\max_i y_i.
\]

For Simpson,
\[
\sum_i n_i^2
=
\sum_i(1+y_i)^2
=
k+2r+\sum_i y_i^2.
\]
Thus Simpson ranking is exactly ranking by
\[
Q(y)=\sum_i y_i^2.
\]

Zero excess coordinates change neither \(M\) nor \(Q\). The finite problem therefore reduces to integer partitions of the excess total \(r\).

A direct extremal bound explains the lower threshold. Fix \(r\) and suppose the largest excess part is \(m\).

The largest possible quadratic sum among partitions with all parts at most \(m\) is obtained by using as many parts equal to \(m\) as possible. If
\[
r=qm+s,
\qquad
0\le s<m,
\]
then
\[
Q_{\max}(r,m)=qm^2+s^2.
\]

The smallest possible quadratic sum among partitions whose largest part is exactly \(m\) is bounded below by splitting all remaining mass into ones:
\[
Q_{\min}(r,m)=m^2+(r-m).
\]

For every
\[
1\le r\le7
\]
and every
\[
m_1<m_2,
\]
one checks
\[
Q_{\max}(r,m_1)
\le
Q_{\min}(r,m_2).
\]
Therefore a community with the larger maximum abundance cannot have the smaller Simpson quadratic score. Strict reversal is impossible.

At
\[
r=8,
\]
the bound can fail. The excess partitions
\[
(1,2,5)
\]
and
\[
(4,4)
\]
satisfy
\[
M(1,2,5)=5>4=M(4,4),
\]
but
\[
Q(1,2,5)=30<32=Q(4,4).
\]
Restoring the mandatory one individual per species gives the universal witness
\[
(2,3,6)
\]
versus
\[
(5,5)
\]
with unit-abundance padding as needed.

The complete partition census at \(r=8\) has exactly four reversing excess-pair types:
\[
(1,1,1,1,1,3)
\quad\text{versus}\quad
(2,2,2,2),
\]
\[
(1,1,1,1,4)
\quad\text{versus}\quad
(2,3,3),
\]
\[
(1,1,1,5)
\quad\text{versus}\quad
(4,4),
\]
and
\[
(1,2,5)
\quad\text{versus}\quad
(4,4).
\]

A fixed \(k\) permits only partitions with at most \(k\) nonzero excess parts. Hence the first-layer counts are
\[
1,\ 2,\ 3,\ 4
\]
for \(k=3,4,5,\ge6\).

For two species, write the larger relative abundance as
\[
p\in\left[\frac12,1\right].
\]
Then Berger–Parker is \(p\), while Simpson concentration is
\[
p^2+(1-p)^2.
\]
Both are strictly increasing in \(p\), so no reversal is possible.

## Verification
The embedded `verify_berger_parker_simpson_boundary.py` uses only the Python standard library and exact integer arithmetic.

It enumerates every integer partition of
\[
0\le r\le8,
\]
compares every unordered pair by maximum excess part and excess quadratic sum, and verifies strict-reversal counts
\[
0,0,0,0,0,0,0,0,4.
\]

It verifies the complete first-layer list, reconstructs the fixed-\(k\) counts, and checks the universal witness for every
\[
3\le k\le100.
\]

It independently confirms that the population-proportion and finite-sample Simpson formulas induce identical rankings at fixed total abundance.

It also checks two-species nonreversal for every total
\[
2\le N\le500
\]
as a replay of the symbolic monotonicity proof.

Run:

`python3 verify_berger_parker_simpson_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Simpson introduced a concentration measure based on the probability structure of category membership.

Berger and Parker introduced a dominance measure based on the relative abundance of the most abundant species.

Modern ecological work treats the two indices as distinct dominance summaries. Morris and coauthors give Berger–Parker dominance as the maximum species proportion and place it alongside Simpson-based measures in a common diversity framework; they emphasize that Berger–Parker responds only to the most abundant species, whereas Simpson responds more broadly to abundant species.

Bonilla-Rosso and coauthors likewise define Simpson dominance and Berger–Parker dominance side by side and show empirically that different diversity metrics can give different rankings of simulated communities. Thus generic metric disagreement is prior work and is not claimed here.

The accepted claim is the discrete sharp boundary: with fixed richness and positive integer abundances, seven excess individuals are insufficient for strict Berger–Parker–Simpson reversal, eight are sufficient for every richness at least three, the three-species first layer is unique, and the complete first-layer count stabilizes at four types.

Targeted searches using both metric names, ranking reversal, exact abundance profiles, integer abundance, fixed richness, smallest community size, and majorization language did not locate this boundary.

## Limitations
The sharp threshold assumes fixed species richness, equal total abundance across the two communities being compared, and strictly positive integer species counts.

If zero-abundance categories are retained as nominal species, they should first be removed from richness because Berger–Parker and Simpson are community measures over present categories.

With arbitrary real-valued proportions rather than integer counts, three species already suffice for reversal without an eleven-individual resolution constraint.

Generic disagreement between Berger–Parker and Simpson is already documented in ecological applications. The new claim is only the exact positive-integer boundary, complete first layer, and universal excess-unit formulation.

An unindexed teaching example, software regression test, or specialist note could contain the same eleven-individual witness even though the sharp universal boundary was not located.

## References
1. E. H. Simpson, “Measurement of Diversity,” *Nature* 163, 688, published 30 April 1949. DOI: 10.1038/163688a0.
2. W. H. Berger and F. L. Parker, “Diversity of planktonic foraminifera in deep-sea sediments,” *Science* 168(3937), 1345–1347, published 12 June 1970. DOI: 10.1126/science.168.3937.1345.
3. G. Bonilla-Rosso, L. E. Eguiarte, D. Romero, M. Travisano, and V. Souza, “Understanding microbial community diversity metrics derived from metagenomes: performance evaluation using simulated data sets,” *FEMS Microbiology Ecology* 82(1), 37–49, 2012. DOI: 10.1111/j.1574-6941.2012.01405.x.
4. E. K. Morris et al., “Choosing and using diversity indices: insights for ecological applications from the German Biodiversity Exploratories,” *Ecology and Evolution* 4(18), 3514–3524, first published 28 August 2014. DOI: 10.1002/ece3.1155.
