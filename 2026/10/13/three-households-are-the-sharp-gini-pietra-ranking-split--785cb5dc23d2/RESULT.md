# Three households are the sharp Gini–Pietra ranking split
## Finding
For a nonnegative income vector
\[
x=(x_1,\ldots,x_n)
\]
with positive total
\[
S=\sum_i x_i,
\]
use the finite-population Gini coefficient
\[
G(x)=\frac{1}{2nS}\sum_{i=1}^n\sum_{j=1}^n|x_i-x_j|
\]
and the Pietra index
\[
P(x)=\frac12\sum_{i=1}^n\left|\frac{x_i}{S}-\frac1n\right|.
\]
The Pietra index is also called the Hoover or Robin Hood index and equals the share of total income that must be transferred from above-mean units to below-mean units to reach equality.

For two households,
\[
G(x)=P(x)
\]
for every nonzero income vector. Consequently the two indices cannot give opposite strict rankings at support size two.

Three households are sharp. Sort the incomes as
\[
x_1\le x_2\le x_3
\]
and define
\[
\ell=\frac13-\frac{x_1}{S},
\qquad
u=\frac{x_3}{S}-\frac13.
\]
Both are nonnegative. Then
\[
G=\frac23(\ell+\nu)
\]
and
\[
P=\max\{\ell,\nu\}.
\]
Thus Gini measures the sum of the two endpoint departures from the mean share, while Pietra keeps only the larger endpoint departure.

Accordingly, for two three-household distributions, strict ranking reversal occurs exactly when their values of
\[
\ell+\nu
\]
and
\[
\max\{\ell,\nu\}
\]
are ordered oppositely.

A smallest-support equal-total witness is
\[
A=(1,6,9)
\]
and
\[
B=(3,3,10).
\]
Both totals equal \(16\). Their exact indices are
\[
G(A)=\frac13,
\qquad
P(A)=\frac{13}{48},
\]
and
\[
G(B)=\frac7{24},
\qquad
P(B)=\frac7{24}.
\]
Hence
\[
G(A)>G(B)
\]
but
\[
P(A)<P(B).
\]
Gini judges \(A\) more unequal because its total extreme spread is larger, while Pietra judges \(B\) more unequal because its single largest departure from the equal-income share is larger.

## Assumptions and scope
Incomes are nonnegative and total income is positive.

The comparison is scale invariant: multiplying all incomes in one distribution by the same positive constant changes neither index.

The finite-population Gini convention used here agrees with the mean-absolute-difference normalization
\[
G=\frac{1}{2\mu}\,E|X-X'|
\]
for the empirical distribution assigning probability \(1/n\) to each household income.

The Pietra convention is the normalized mean absolute deviation from the mean,
\[
P=\frac{1}{2\mu}E|X-\mu|,
\]
which is equivalent to the maximum vertical Lorenz-curve gap.

The theorem concerns ranking disagreement, not Lorenz dominance. If one distribution Lorenz-dominates another, both indices respect that dominance.

## Proof
For two sorted incomes
\[
a\le b,
\]
the Gini numerator is
\[
2(b-a),
\]
so
\[
G=\frac{b-a}{2(a+b)}.
\]
The two normalized income shares are symmetric around \(1/2\), hence
\[
P
=\frac12\left(\left|\frac{a}{a+b}-\frac12\right|+\left|\frac{b}{a+b}-\frac12\right|\right)
=\frac{b-a}{2(a+b)}.
\]
Therefore \(G=P\) identically for support two.

Now let
\[
x_1\le x_2\le x_3
\]
with total \(S\). The pairwise absolute-difference sum is
\[
\sum_{i,j}|x_i-x_j|=4(x_3-x_1),
\]
so
\[
G=\frac{2(x_3-x_1)}{3S}.
\]
Since
\[
x_3-x_1
=S\left(\frac{x_3}{S}-\frac13+\frac13-\frac{x_1}{S}\right),
\]
this is
\[
G=\frac23(\ell+\nu).
\]

For Pietra, total normalized shortfall below \(1/3\) equals total normalized excess above \(1/3\). With only three ordered shares, either the middle share is at most \(1/3\), in which case the only above-mean household is the richest and
\[
P=\nu,
\]
or the middle share is at least \(1/3\), in which case the only below-mean household is the poorest and
\[
P=\ell.
\]
At equality both formulas agree. Hence
\[
P=\max\{\ell,\nu\}.
\]

Because the constants multiplying \(\ell+\nu\) in \(G\) are positive, two three-household profiles are ranked oppositely exactly when the sum and the maximum of their endpoint deviations are ranked oppositely.

For the witness, direct substitution gives the fractions stated above, proving existence at support three and therefore sharpness.

## Verification
The embedded `verify_gini_pietra_minimal_support.py` uses exact rational arithmetic.

It independently checks the support-two identity on a grid of nonnegative integer pairs and the support-three endpoint formulas on all sorted integer triples in a finite test box. It then verifies the exact witness values.

As an additional finite consistency check, it exhausts positive integer three-household profiles with a common total and finds no strict Gini–Pietra reversal below total \(16\); at total \(16\) the displayed pair is the unique reversal up to sorting.

The universal support-two identity and support-three formulas are proved algebraically above; the finite replay is not used as a substitute for those proofs.

Run:

`python3 verify_gini_pietra_minimal_support.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The Gini and Pietra indices are classical Lorenz-based inequality measures with different geometric meanings. Modern treatments describe Gini as twice the area between the Lorenz curve and equality, while Pietra is the maximum vertical gap and has the Robin-Hood redistribution interpretation.

Fellman explicitly notes that Gini and Pietra orderings are not identical in general and that Lorenz dominance implies agreement of both. He also records the general pointwise inequality \(G\ge P\). Thus the existence of some ordering disagreement is prior work and is not claimed as new here.

Dong and coauthors give a full modern derivation of Pietra as normalized absolute deviation from the mean and discuss how Gini and Pietra weight different parts of the income distribution. This supplies the exact formulas underlying the finite-support analysis.

The present claim is narrower: it identifies the minimum empirical support at which opposite strict rankings are possible and gives the exact three-household reduction to the sum versus maximum of two endpoint deviations. Targeted searches using Gini/Pietra/Hoover/Robin-Hood aliases, ranking-disagreement language, three-household language, support-size language, and the exact witness did not locate this boundary or criterion.

A 2026 preprint devoted specifically to unifying Hoover and Gini was identified and its abstract inspected, but the full arXiv text was not retrievable through the available route. Its abstract describes an interpolating family and statistical properties, not the finite-support boundary; uninspected details remain a residual literature risk.

## Limitations
The result concerns equally weighted finite populations. Weighted households require a separate support notion.

The theorem assumes nonnegative incomes because the usual Lorenz and Pietra redistribution interpretations rely on income shares.

Three households are the sharp support size, but the result does not classify every higher-support reversal.

The positive-integer total-\(16\) check is only a supplementary finite benchmark and is not part of the main minimal-support theorem.

An unindexed exercise, software test, or specialist note could contain the same three-household witness even though the sharp support theorem was not located.

## References
1. I. Eliazar and M. H. Cohen, “On social inequality: Analyzing the rich-poor disparity,” *Physica A* 401, 148–158, published 1 May 2014. DOI: 10.1016/j.physa.2014.01.033.
2. J. Fellman, “Income Inequality Measures,” *Theoretical Economics Letters* 8, 557–574, 2018. DOI: 10.4236/tel.2018.83039.
3. Z. Dong, Y. Till, G. M. Giorgi and A. Guandalini, “Generalised Income Inequality Index,” *International Statistical Review* 92, 87–105, 2024. DOI: 10.1111/insr.12551.
4. R. Vila, H. Saulo and F. Quintino, “Unifying the Hoover and Gini indices: Analytical, bias, and computational aspects,” arXiv:2603.26166, submitted 27 March 2026.
