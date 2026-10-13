# Six individuals split Shannon and Simpson; seven reverse them
## Finding
Consider a finite ecological community sample with positive species abundances
\[
n_1,\ldots,n_s,
\qquad
N=\sum_{i=1}^s n_i.
\]
Species labels are irrelevant, so an abundance profile is an integer partition of \(N\).

Write
\[
p_i=\frac{n_i}{N}.
\]
The Shannon diversity is
\[
H=-\sum_{i=1}^s p_i\ln p_i.
\]
Use the finite-sample Simpson diversity convention
\[
D
=
1-
\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]

For every abundance profile with
\[
N\le5,
\]
the two indices induce exactly the same weak ordering.

At
\[
N=6,
\]
the first ordering differences occur. There are exactly two unordered profile pairs on which Shannon is strict while Simpson ties:
\[
(4,1,1)\quad\text{versus}\quad(3,3),
\]
and
\[
(3,1,1,1)\quad\text{versus}\quad(2,2,2).
\]
In both cases Shannon ranks the first profile higher. There is no strict Shannon-Simpson rank reversal through six individuals.

At
\[
N=7,
\]
strict rank reversal occurs for the first time. There are exactly two unordered reversing pairs:
\[
(5,1,1)\quad\text{versus}\quad(4,3),
\]
and
\[
(4,1,1,1)\quad\text{versus}\quad(3,2,2).
\]

For the first pair,
\[
H(5,1,1)>H(4,3),
\]
but
\[
D(5,1,1)=\frac{11}{21}
<
\frac47
=
D(4,3).
\]

For the second pair,
\[
H(4,1,1,1)>H(3,2,2),
\]
but
\[
D(4,1,1,1)=\frac57
<
\frac{16}{21}
=
D(3,2,2).
\]

Hence six individuals are the exact first boundary where the two orderings cease to coincide, and seven individuals are the exact first boundary where they make opposite strict diversity judgments.

## Assumptions and scope
All listed species have positive integer abundance. A zero-abundance species is not part of the observed community profile.

Profiles are compared only at the same total census size \(N\).

Shannon diversity uses the natural logarithm. Changing the logarithm base multiplies every Shannon score by a positive constant and therefore does not affect rankings.

The Simpson convention is the finite-sample form
\[
1-\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]
For fixed \(N\), it has exactly the same ordering as the population Gini-Simpson quantity
\[
1-\sum_i p_i^2.
\]

The theorem is an exact small-census classification. It does not assert that seven individuals are a practically adequate ecological sample size.

## Proof
For a profile
\[
\lambda=(n_1,\ldots,n_s)
\]
with fixed total \(N\), define
\[
P(\lambda)=\prod_i n_i^{\,n_i}
\]
and
\[
Q(\lambda)=\sum_i n_i(n_i-1).
\]

Since
\[
H(\lambda)
=
\ln N
-
\frac1N\sum_i n_i\ln n_i
=
\ln N-\frac1N\ln P(\lambda),
\]
Shannon diversity is strictly decreasing in the positive integer \(P(\lambda)\).

Likewise,
\[
D(\lambda)
=
1-\frac{Q(\lambda)}{N(N-1)},
\]
so Simpson diversity is strictly decreasing in the integer \(Q(\lambda)\).

Therefore every Shannon-Simpson comparison at fixed \(N\) reduces exactly to comparing the integer pair
\[
(P(\lambda),Q(\lambda)).
\]

The integer partitions of \(N=2,\ldots,7\) number
\[
2,\ 3,\ 5,\ 7,\ 11,\ 15.
\]
Exact enumeration gives the following complete comparison census:
\[
\begin{array}{c|c|c|c}
N & \text{profiles} & \text{ordering mismatches} & \text{strict reversals}\\ \hline
2&2&0&0\\
3&3&0&0\\
4&5&0&0\\
5&7&0&0\\
6&11&2&0\\
7&15&4&2
\end{array}
\]

At \(N=6\), the two mismatches are precisely the tie-splitting pairs stated above. For example,
\[
P(4,1,1)=4^4=256<3^6=729=P(3,3),
\]
so Shannon ranks \((4,1,1)\) higher, while
\[
Q(4,1,1)=12=Q(3,3),
\]
so Simpson ties them. Similarly,
\[
P(3,1,1,1)=3^3=27<2^6=64=P(2,2,2),
\]
while both profiles have
\[
Q=6.
\]

At \(N=7\), the two strict reversals are exact integer inequalities. For
\[
(5,1,1)\quad\text{and}\quad(4,3),
\]
\[
P(5,1,1)=5^5=3125
<
4^4\,3^3=6912
=
P(4,3),
\]
so Shannon prefers \((5,1,1)\). But
\[
Q(5,1,1)=20>18=Q(4,3),
\]
so Simpson prefers \((4,3)\).

For
\[
(4,1,1,1)\quad\text{and}\quad(3,2,2),
\]
\[
P(4,1,1,1)=4^4=256
<
3^3\,2^4=432
=
P(3,2,2),
\]
so Shannon prefers \((4,1,1,1)\). Yet
\[
Q(4,1,1,1)=12>10=Q(3,2,2),
\]
so Simpson prefers \((3,2,2)\).

The exhaustive classification shows that no other pair reverses at \(N=7\).

## Verification
The embedded `verify_shannon_simpson_minimal_reversal.py` uses only the Python standard library and exact integer or rational arithmetic.

It constructs every abundance partition through \(N=7\) in two independent ways:
- recursive integer-partition generation;
- all compositions of \(N\), subsequently sorted and deduplicated.

The two constructions agree exactly and reproduce the partition counts
\[
2,\ 3,\ 5,\ 7,\ 11,\ 15.
\]

Every Shannon comparison is reduced to the exact integer product \(P(\lambda)\), so no floating logarithms are used. Every Simpson score is computed as an exact `Fraction`.

The replay verifies:
- identical weak orderings through \(N=5\);
- exactly two tie-splitting mismatches at \(N=6\);
- no strict reversal through \(N=6\);
- exactly four ordering mismatches at \(N=7\);
- exactly two strict reversals at \(N=7\), namely the two displayed pairs;
- equivalence of the finite-sample Simpson ordering and population Gini-Simpson ordering at every checked fixed census size.

Run:

`python3 verify_shannon_simpson_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Simpson's classical 1949 paper introduced a concentration-based diversity measure in terms of population composition.

Ecological diversity-ordering work later emphasized that scalar diversity indices can rank the same communities differently. Tóthmérész gives the formulas
\[
H=-\sum_i p_i\ln p_i
\]
and
\[
D
=
1-
\frac{\sum_i n_i(n_i-1)}{N(N-1)},
\]
then exhibits two communities of total size \(100\) for which Shannon and Simpson make opposite diversity judgments. The same paper treats such disagreements as manifestations of non-comparability under broader diversity profiles.

That literature establishes both the scientific importance and the existence of Shannon-Simpson rank disagreement. The result here asks the finite onset question that the inspected sources do not answer: how small can a positive-integer abundance census be before the two orderings first separate, and when does the first strict reversal occur?

Targeted searches using Shannon/Simpson aliases, minimum-census language, exact seven-individual language, and the four boundary abundance patterns did not locate the six-individual tie boundary, the seven-individual strict-reversal boundary, or the exact first-layer classification.

## Limitations
The result compares only Shannon diversity with the stated Simpson diversity convention.

The census size is fixed within every pairwise comparison.

Only abundance profiles are classified; sampling uncertainty, detectability, spatial structure, and taxonomic relatedness are outside scope.

The theorem is a smallest-census structural statement, not advice that diversity estimation from six or seven observations is statistically reliable.

An unindexed exercise, software test set, or historical table could contain the same small-census classification.

## References
1. E. H. Simpson, “Measurement of Diversity,” *Nature* 163, 688, 1949. DOI: 10.1038/163688a0.
2. B. Tóthmérész, “Comparison of different methods for diversity ordering,” *Journal of Vegetation Science* 6(2), 283–290, 1995. DOI: 10.2307/3236223.
