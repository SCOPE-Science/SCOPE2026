# Ten individuals are the sharp equal-census Bray–Curtis–chi-square reversal boundary
## Finding
For two ecological communities with the same labeled species set, let the strictly positive integer abundance vectors be
\[
x=(x_1,\ldots,x_k),\qquad y=(y_1,\ldots,y_k),
\]
with
\[
\sum_i x_i=\sum_i y_i=N.
\]
Their Bray–Curtis dissimilarity is
\[
B(x,y)=\frac{1}{2N}\sum_i|x_i-y_i|.
\]
For ordinary correspondence analysis of this two-row table, the species-\(i\) column mass is
\[
c_i=\frac{x_i+y_i}{2N},
\]
so the squared chi-square distance between row profiles is
\[
X(x,y)^2
=\sum_i\frac{(x_i/N-y_i/N)^2}{c_i}
=\frac{2}{N}\sum_i\frac{(x_i-y_i)^2}{x_i+y_i}.
\]

For every
\[
N\le9
\]
and every admissible richness
\[
2\le k<N,
\]
no two positive-integer tables with the same \((N,k)\) receive opposite strict orderings from \(B\) and \(X\).

The sharp first reversal occurs at
\[
N=10.
\]
At
\[
k=3,
\]
compare
\[
(1,3,6)\quad\text{with}\quad(3,1,6)
\]
against
\[
(1,2,7)\quad\text{with}\quad(2,4,4).
\]
Their Bray–Curtis values satisfy
\[
\frac15<\frac3{10},
\]
while their squared chi-square distances satisfy
\[
\frac25>\frac4{11}.
\]
Thus the two distances prefer opposite community pairs. At census ten, reversals occur exactly for richness \(3,4,5,6\).

## Assumptions and scope
Every species is present in both communities, so all abundance counts are positive.

The two rows forming each distance have the same total abundance \(N\), and dissimilarities are compared only within a common pair \((N,k)\).

The chi-square distance is the ordinary correspondence-analysis row-profile distance for the two-row table itself. Column masses are computed from those two rows. In a larger table, global column masses differ, so this theorem need not apply.

The statement concerns exact dissimilarity ordering, not sampling uncertainty or biological importance.

## Proof
At fixed \(N\), Bray–Curtis ordering is exactly the ordering of
\[
L(x,y)=\sum_i|x_i-y_i|.
\]
For the two-row correspondence-analysis table, chi-square ordering is exactly the ordering of
\[
C(x,y)=\sum_i\frac{(x_i-y_i)^2}{x_i+y_i},
\]
because the common factor \(2/N\) is positive.

The criteria weight turnover differently. \(L\) counts absolute changes uniformly, whereas \(C\) squares each change and divides by pooled abundance.

For the first pair,
\[
(1,3,6)\quad\text{and}\quad(3,1,6),
\]
the absolute differences are \((2,2,0)\), giving
\[
B=\frac4{20}=\frac15.
\]
The chi-square core is
\[
C=\frac4{4}+\frac4{4}=2,
\]
so
\[
X^2=\frac2{10}\cdot2=\frac25.
\]

For the second pair,
\[
(1,2,7)\quad\text{and}\quad(2,4,4),
\]
the absolute differences are \((1,2,3)\), giving
\[
B=\frac6{20}=\frac3{10}.
\]
The chi-square core is
\[
C=\frac13+\frac46+\frac9{11}=\frac{20}{11},
\]
so
\[
X^2=\frac2{10}\cdot\frac{20}{11}=\frac4{11}.
\]
Since
\[
\frac15<\frac3{10}
\quad\text{but}\quad
\frac25>\frac4{11},
\]
the ordering reverses.

For minimality, a positive \(k\)-species profile of census \(N\) is a composition of \(N\) into \(k\) positive parts, so there are
\[
\binom{N-1}{k-1}
\]
profiles. The verifier generates every composition, every unordered pair of distinct profiles, and its exact pair \((L,C)\). Exact comparison gives no strict inversion for any \(N\le9\). At \(N=10\), inversions occur only for richness \(3,4,5,6\).

## Verification
The embedded `verify_bray_chi_square_boundary.py` uses only exact integer and rational arithmetic.

For every
\[
3\le N\le10
\]
and every admissible richness, it generates all positive compositions and checks their number against
\[
\binom{N-1}{k-1}.
\]
It then forms every unordered pair of distinct profiles and checks that pair count combinatorially.

Within each common \((N,k)\) layer, it counts strict inversions between the Bray–Curtis numerator and the chi-square core. Equal values under either criterion are excluded from strict reversals.

It verifies no reversal through census nine. At census ten the exact labeled reversal counts are
\[
288,\ 8256,\ 30100,\ 17100
\]
for richness
\[
3,\ 4,\ 5,\ 6,
\]
respectively, and zero otherwise.

Run:

`python3 verify_bray_chi_square_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Greenacre describes ecological correspondence analysis in terms of row profiles and chi-square distances and discusses correspondence-analysis distances as alternatives to Bray–Curtis dissimilarities for abundance data.

Warton, Wright, and Wang distinguish the pairwise standardization in Bray–Curtis from the column standardization in chi-square distance and show that choices of ecological distance encode different abundance-weighting assumptions.

Those sources establish that the two distances have different geometry and ecological behavior. The present claim is narrower: the smallest strictly positive equal-census integer table at which their pairwise rankings can strictly reverse, together with the richness support of that first census layer.

Targeted searches using the two metric names, correspondence-analysis aliases, equal census, ranking reversal, smallest abundance table, and the exact ten-individual witness did not locate this boundary.

## Limitations
The chi-square formula uses column masses computed from the two-row table itself. A larger background table changes those masses.

Zero counts are excluded; allowing absent species changes the finite domain.

The finite boundary is not a statement about ecological sample adequacy or frequency of reversals in field data.

The first-layer reversal counts treat species labels as fixed and are verification details rather than an isomorphism classification.

## References
1. M. Greenacre, “Correspondence analysis of raw data,” *Ecology* 91(4), 2010, DOI: 10.1890/09-0239.1. First published 1 April 2010.
2. D. I. Warton, S. T. Wright, and Y. Wang, “Distance-based multivariate analyses confound location and dispersion effects,” *Methods in Ecology and Evolution* 3(1), 2012, DOI: 10.1111/j.2041-210X.2011.00127.x. First published 6 June 2011.
