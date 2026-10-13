# Two Hill diversities identify every integer abundance profile through 23 individuals, but not 24
## Finding
Let an ecological abundance profile be an unlabeled multiset of strictly positive integer species abundances
\[
n_1,\ldots,n_S,
\qquad
\sum_i n_i=N.
\]

Write
\[
p_i=\frac{n_i}{N}.
\]

Shannon entropy is
\[
H=-\sum_i p_i\log p_i,
\]
and Simpson concentration is
\[
C_2=\sum_i p_i^2.
\]

For every
\[
N\le23,
\]
the pair
\[
(H,C_2)
\]
uniquely determines the entire abundance multiset.

At
\[
N=24,
\]
joint identifiability fails for the first time. Up to species permutation there are exactly two collisions:
\[
(1,1,1,1,1,1,3,3,4,4,4)
\quad\text{and}\quad
(2,2,2,2,2,2,2,2,2,6),
\]
and
\[
(1,1,1,1,4,4,6,6)
\quad\text{and}\quad
(2,2,3,3,3,3,8).
\]

The first pair has species richness \(11\) versus \(10\), while the second has richness \(8\) versus \(7\). Thus species richness resolves both first collisions.

More strongly, the triple
\[
(S,H,C_2)
\]
uniquely determines every positive-integer abundance multiset for
\[
N\le29.
\]

At
\[
N=30,
\]
that triple fails for the first time, in exactly one collision:
\[
(1,4,4,4,4,4,9)
\quad\text{and}\quad
(2,2,3,3,6,6,8).
\]
Both profiles have richness
\[
S=7.
\]

## Assumptions and scope
Species labels are ignored, so abundance profiles are integer partitions of the total census size.

All represented species have positive abundance. Zero-abundance species are not counted in richness.

The Simpson quantity used here is the population-form concentration
\[
C_2=\sum_i p_i^2,
\]
whose inverse is Hill diversity of order \(2\). Shannon diversity of order \(1\) is the exponential of \(H\). Because exponential and reciprocal transformations are injective on their domains, the identifiability statements are unchanged if one works with Hill numbers
\[
{}^1D=\exp(H),
\qquad
{}^2D=\frac1{C_2}.
\]

The result is a finite-resolution statement for integer census counts. It does not claim that finitely many Hill-number orders determine an arbitrary real-valued abundance distribution.

## Proof
At fixed total
\[
N,
\]
Shannon entropy can be rewritten as
\[
H
=
\log N
-
\frac1N\sum_i n_i\log n_i.
\]

Define the positive integer
\[
Q(n)
=
\prod_i n_i^{n_i}.
\]

Then
\[
H
=
\log N
-
\frac1N\log Q(n).
\]

Hence two integer abundance profiles with the same total have equal Shannon entropy if and only if they have equal \(Q\).

Likewise,
\[
C_2
=
\sum_i\left(\frac{n_i}{N}\right)^2
=
\frac{\sum_i n_i^2}{N^2}.
\]

Therefore, at fixed \(N\), equality of both Shannon entropy and Simpson concentration is exactly equality of the integer pair
\[
\left(
Q(n),
\sum_i n_i^2
\right).
\]

Every unlabeled positive-integer abundance profile of total \(N\) is an integer partition of \(N\). Exhaustive exact enumeration of all partitions for
\[
1\le N\le30
\]
shows that the map
\[
n\longmapsto
\left(
Q(n),
\sum_i n_i^2
\right)
\]
is injective through
\[
N=23.
\]

At
\[
N=24,
\]
there are exactly two collision classes.

For the first,
\[
Q=12230590464,
\qquad
\sum_i n_i^2=72.
\]
Thus both profiles have
\[
C_2=\frac{72}{24^2}=\frac18,
\]
but their richnesses are \(11\) and \(10\).

For the second,
\[
Q=142657607172096,
\qquad
\sum_i n_i^2=108.
\]
Thus both profiles have
\[
C_2=\frac{108}{24^2}=\frac3{16},
\]
but their richnesses are \(8\) and \(7\).

Adding richness means comparing the integer triple
\[
\left(
S,
Q(n),
\sum_i n_i^2
\right).
\]

That triple is injective for every partition through
\[
N=29.
\]

At
\[
N=30,
\]
the unique collision is
\[
(1,4,4,4,4,4,9)
\]
and
\[
(2,2,3,3,6,6,8).
\]
For both,
\[
S=7,
\]
\[
Q=425973332494163902464,
\]
and
\[
\sum_i n_i^2=162.
\]
Hence both have the same Shannon entropy and
\[
C_2=\frac{162}{30^2}=\frac9{50}.
\]

## Verification
The embedded `verify_hill_joint_identifiability.py` uses only the Python standard library and exact integer arithmetic.

It independently generates every integer partition through total
\[
30
\]
and checks its partition count against a separate dynamic-programming computation of the partition number.

In total it checks
\[
28628
\]
abundance profiles.

For each profile it computes
\[
Q=\prod_i n_i^{n_i},
\qquad
\sum_i n_i^2,
\qquad
S.
\]

It verifies no \((H,C_2)\) collision through total \(23\), exactly the two stated collisions at \(24\), no \((S,H,C_2)\) collision through total \(29\), and exactly the stated unique collision at \(30\).

Run:

`python3 verify_hill_joint_identifiability.py`

The first output line must be `VERIFY_OK`.

The finite enumeration is exhaustive over the stated integer domain; no floating-point entropy comparison is used.

## Relationship to prior work
Hill unified species richness, Shannon diversity, and Simpson diversity as orders \(0\), \(1\), and \(2\) of one diversity-number family. He emphasized that different orders weight rare and common species differently, and that a complete abundance partition generally cannot be summarized adequately by one statistic.

Modern diversity-profile treatments likewise use a continuum of Hill orders to describe an abundance distribution.

The present result asks a narrower inverse question on integer census profiles: how long do the two classic abundance-sensitive orders \(1\) and \(2\) determine the entire unlabeled abundance multiset exactly, and how long does adding richness \(q=0\) postpone failure?

Targeted searches for equal Shannon and Simpson values, joint Hill-number identifiability, exact abundance-profile collisions, and the displayed vectors did not locate these sharp finite cutoffs.

## Limitations
The theorem is restricted to positive integer census abundances and exact equality of indices.

For arbitrary real abundance vectors, two or three scalar summaries cannot be expected to identify a general distribution.

The full Hill diversity profile contains substantially more information than the orders \(0\), \(1\), and \(2\) alone; this result does not contradict profile-based characterization results.

An unindexed worked example, teaching note, or software test could contain one of the displayed collisions even though the sharp minimal totals were not located in the checked literature.

## References
1. M. O. Hill, “Diversity and Evenness: A Unifying Notation and Its Consequences,” *Ecology* 54(2), 427–432, first published 1 March 1973. DOI: 10.2307/1934352.
2. A. Chao, K. H. Ma, T. C. Hsieh, and C.-H. Chiu, “Quantifying sample completeness and comparing diversities among assemblages,” *Ecological Research* 35, 292–314, 2020. DOI: 10.1111/1440-1703.12102.
