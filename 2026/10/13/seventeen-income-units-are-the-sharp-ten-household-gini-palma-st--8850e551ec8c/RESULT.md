# Seventeen income units are the sharp ten-household Gini–Palma strict-reversal boundary
## Finding
Fix exactly \(10\) households with strictly positive integer incomes
\[
x_1\le x_2\le\cdots\le x_{10},\qquad \sum_{i=1}^{10}x_i=S.
\]
The ordinary Gini coefficient is
\[
G(x)=\frac{\sum_{i<j}(x_j-x_i)}{10S}.
\]
For ten equally weighted households, the Palma ratio is exactly
\[
P(x)=\frac{x_{10}}{x_1+x_2+x_3+x_4}.
\]
No two profiles with \(S\le16\) receive opposite strict inequality rankings from \(G\) and \(P\). At \(S=17\), strict reversal appears for the first time, in exactly two unordered pairs up to household permutation:
\[
(1,1,1,1,1,1,1,2,4,4)\quad\text{versus}\quad(1,1,1,1,1,1,2,2,2,5),
\]
and
\[
(1,1,1,1,1,1,2,3,3,3)\quad\text{versus}\quad(1,1,1,1,1,2,2,2,2,4).
\]
For the first pair,
\[
G=\frac{53}{170}>\frac3{10},\qquad P=1<\frac54.
\]
For the second pair,
\[
G=\frac9{34}>\frac{43}{170},\qquad P=\frac34<1.
\]
Thus Gini ranks the first profile in each pair as more unequal, while Palma ranks the second as more unequal.

## Assumptions and scope
The population has ten equally weighted households, so the richest ten per cent is one household and the poorest forty per cent is four households without interpolation. All incomes are positive integers, both profiles in a comparison have the same total, and household labels are irrelevant.

The theorem concerns opposite strict rankings. Weak-order disagreement begins at \(S=14\), when a tie under one measure can be split by the other. The integer total is a resolution parameter, not a monetary threshold; common scaling preserves both indices.

## Proof
At fixed \(S\), Gini ordering is exactly the ordering of
\[
D(x)=\sum_{i<j}(x_j-x_i),
\]
because the denominator \(10S\) is common. Palma ordering is the exact rational ordering of
\[
P(x)=\frac{x_{10}}{x_1+x_2+x_3+x_4}.
\]
Every admissible profile is a partition of \(S\) into exactly ten positive parts. For \(S=10,\ldots,17\), the numbers of profiles are
\[
1,1,2,3,5,7,11,15.
\]
Exhaustive comparison of every unordered pair gives zero strict reversals for \(S=10,\ldots,16\) and exactly two at \(S=17\).

For
\[
a=(1,1,1,1,1,1,1,2,4,4),\quad b=(1,1,1,1,1,1,2,2,2,5),
\]
one has
\[
D(a)=53>D(b)=51,\qquad P(a)=1<P(b)=\frac54.
\]
For
\[
c=(1,1,1,1,1,1,2,3,3,3),\quad d=(1,1,1,1,1,2,2,2,2,4),
\]
one has
\[
D(c)=45>D(d)=43,\qquad P(c)=\frac34<P(d)=1.
\]
These are the complete strict-reversal layer at total seventeen.

## Verification
The embedded `verify_gini_palma_boundary.py` uses only exact integer and rational arithmetic. It generates every positive ten-part partition for \(10\le S\le17\), checks every unordered pair, separately counts weak-order disagreements, and verifies the displayed values.

Run `python3 verify_gini_palma_boundary.py`. The first output line must be `VERIFY_OK`.

## Relationship to prior work
Palma's distributional argument emphasizes relative stability in middle income shares and greater variation in the top ten per cent and bottom forty per cent. Cobham and Sumner formalize the Palma ratio as the richest-ten-per-cent income share divided by that of the poorest forty per cent and compare it directly with Gini. Their analysis stresses different distributional sensitivities despite very strong empirical association.

Those facts make disagreement possible but do not determine the smallest positive-integer ten-household profile at which the measures give opposite strict judgments. Searches using both metric names, fixed-total profiles, smallest-reversal language, and the exact sharp profiles did not locate this boundary. Generic Gini–Palma rank differences are not claimed as new; the contribution is the sharp constrained boundary and complete first strict layer.

## Limitations
The theorem uses exactly ten equally weighted households and positive integer incomes. The cutoff is grid-dependent and does not classify arbitrary real-valued profiles or all larger reversal layers. An unindexed exercise or software test could contain one of the small witnesses even though the sharp boundary was not located.

## References
1. J. G. Palma, “Homogeneous Middles vs. Heterogeneous Tails, and the End of the ‘Inverted-U’: It's All About the Share of the Rich,” *Development and Change* 42(1), 87–153, 2011. DOI: 10.1111/j.1467-7660.2011.01694.x. Version of record online 14 April 2011.
2. A. Cobham and A. Sumner, “Is Inequality all about the Tails?: The Palma Measure of Income Inequality,” *Significance* 11(1), 10–13, 2014. DOI: 10.1111/j.1740-9713.2014.00718.x. Published 19 February 2014.
