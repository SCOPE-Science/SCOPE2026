# Dissimilarity and isolation first strictly reverse with eight members per group
## Finding
Consider exactly two population groups, \(A\) and \(B\), distributed across exactly two nonempty tracts. Suppose the citywide totals are equal:
\[
|A|=|B|=N.
\]

Let the first tract contain \(x\) members of group \(A\) and \(y\) members of group \(B\). The second tract then contains \(N-x\) and \(N-y\).

The Duncan–Duncan dissimilarity index is
\[
D
=
\frac12
\sum_{i=1}^{2}
\left|
\frac{x_i}{N}
-
\frac{y_i}{N}
\right|.
\]

The same-group isolation index is
\[
I
=
\sum_{i=1}^{2}
\frac{x_i}{N}
\frac{x_i}{x_i+y_i}.
\]

Because the group totals are equal, the isolation index is the same whichever group is designated as the focal group.

After swapping tract labels and group labels if necessary, define
\[
t=x+y\le N
\]
for the population of the smaller tract and
\[
d=|x-y|
\]
for its within-tract group imbalance. Feasibility is exactly
\[
1\le t\le N,\qquad
0\le d\le t,\qquad
t\equiv d\pmod 2.
\]

Then the two indices simplify to
\[
D=\frac dN
\]
and
\[
I
=
\frac12+
\frac{d^2}{2t(2N-t)}.
\]

This exposes the difference between the measures. Dissimilarity depends only on the absolute group imbalance \(d\), whereas isolation also depends on how concentrated that imbalance is in a small or large tract.

The two weak orderings first differ at
\[
N=3,
\]
but only through tie splitting: two configurations can have the same \(D\) while isolation distinguishes them.

A strict rank reversal requires more population. No strict reversal exists for
\[
N\le7.
\]

At
\[
N=8,
\]
strict reversal appears for the first time, and there is exactly one unordered pair up to tract and group swaps.

City \(A\):
\[
(1,0)
\quad\text{and}\quad
(7,8).
\]
Its indices are
\[
D(A)=\frac18,
\qquad
I(A)=\frac8{15}.
\]

City \(B\):
\[
(5,3)
\quad\text{and}\quad
(3,5).
\]
Its indices are
\[
D(B)=\frac14,
\qquad
I(B)=\frac{17}{32}.
\]

Therefore
\[
D(A)<D(B)
\]
but
\[
I(A)>I(B).
\]

Dissimilarity judges city \(B\) more segregated because its two group distributions are farther apart in proportional terms. Isolation judges city \(A\) more segregated because one member of group \(A\) occupies a one-person tract and therefore experiences perfect local same-group exposure, enough to outweigh the smaller global distributional imbalance.

The effect is structural rather than isolated. For every
\[
N\ge8,
\]
take city \(P_N\) with tracts
\[
(1,0)
\quad\text{and}\quad
(N-1,N).
\]
If \(N\) is even, compare it with city \(Q_N\) whose tracts are
\[
\left(\frac{N+2}{2},\frac{N-2}{2}\right)
\quad\text{and}\quad
\left(\frac{N-2}{2},\frac{N+2}{2}\right).
\]
If \(N\) is odd, use
\[
\left(\frac{N+1}{2},\frac{N-3}{2}\right)
\quad\text{and}\quad
\left(\frac{N-1}{2},\frac{N+3}{2}\right).
\]
In every case,
\[
D(P_N)<D(Q_N)
\]
while
\[
I(P_N)>I(Q_N).
\]

## Assumptions and scope
There are exactly two groups and exactly two nonempty tracts.

The two groups have equal citywide totals \(N\). This removes the most obvious composition effect on isolation and makes the isolation index symmetric between the two groups.

The result concerns integer population counts. The cutoff \(N=8\) is therefore a smallest-census statement, not a claim about a special real-world population size.

Dissimilarity measures evenness of the two group distributions across tracts. Isolation is an exposure measure: it is the same-group share in the tract occupied by the average group member.

The theorem compares strict ordinal rankings. Equality under one measure is not called a strict reversal.

## Proof
Let the first tract contain \((x,y)\), and write
\[
t=x+y,
\qquad
d=x-y.
\]
After swapping the group labels, assume
\[
d\ge0.
\]
After swapping the tracts, assume
\[
t\le N.
\]
The second tract has population
\[
2N-t
\]
and group difference
\[
-d.
\]

For dissimilarity,
\[
D
=
\frac12
\left(
\frac{|x-y|}{N}
+
\frac{|(N-x)-(N-y)|}{N}
\right)
=
\frac dN.
\]

For isolation,
\[
I
=
\frac{x}{N}\frac{x}{t}
+
\frac{N-x}{N}
\frac{N-x}{2N-t}.
\]
Using
\[
x=\frac{t+d}{2},
\]
the first term is
\[
\frac1N
\frac{(t+d)^2}{4t},
\]
and the second term is
\[
\frac1N
\frac{(2N-t-d)^2}{4(2N-t)}.
\]
Expanding and cancelling the linear terms in \(d\) gives
\[
I
=
\frac12+
\frac{d^2}{2t(2N-t)}.
\]

Thus equal values of \(d\) always tie under dissimilarity, but isolation is larger when the same imbalance is concentrated in a more unequal tract-size split.

The finite cutoff is now an exact lattice problem. A canonical configuration is completely determined by the feasible integer pair
\[
(t,d)
\]
satisfying
\[
1\le t\le N,\qquad
0\le d\le t,\qquad
t\equiv d\pmod2.
\]
The numbers of canonical configurations for
\[
N=1,2,\ldots,8
\]
are
\[
1,\ 3,\ 5,\ 8,\ 11,\ 15,\ 19,\ 24.
\]

Exact comparison of every unordered canonical pair gives strict-reversal counts
\[
0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1.
\]

At \(N=8\), the unique reversing pair is
\[
(t,d)=(1,1)
\quad\text{versus}\quad
(t,d)=(8,2).
\]
These are precisely the two cities in the finding.

The first city has
\[
D=\frac18
\]
and
\[
I
=
\frac12+\frac{1}{2\cdot1\cdot15}
=
\frac8{15}.
\]
The second has
\[
D=\frac28=\frac14
\]
and
\[
I
=
\frac12+\frac{4}{2\cdot8\cdot8}
=
\frac{17}{32}.
\]
Since
\[
\frac8{15}>\frac{17}{32},
\]
the rankings reverse.

For the infinite family, \(P_N\) always has
\[
D(P_N)=\frac1N
\]
and isolation excess over \(1/2\)
\[
I(P_N)-\frac12
=
\frac{1}{2(2N-1)}.
\]

For even \(N\), \(Q_N\) has
\[
D(Q_N)=\frac2N
\]
and
\[
I(Q_N)-\frac12
=
\frac{2}{N^2}.
\]
The desired isolation reversal is equivalent to
\[
N^2-8N+4>0,
\]
which holds for every even
\[
N\ge8.
\]

For odd \(N\), \(Q_N\) has
\[
I(Q_N)-\frac12
=
\frac{2}{N^2-1},
\]
and the reversal is equivalent to
\[
N^2-8N+3>0,
\]
which holds for every odd
\[
N\ge9.
\]
Thus strict reversal persists for every integer \(N\ge8\).

## Verification
The embedded `verify_dissimilarity_isolation_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

It performs two independent descriptions of the finite domain.

First, it enumerates every raw two-tract configuration
\[
(x,y),
\qquad
0\le x,y\le N,
\]
excluding an empty tract, and quotients by the four symmetries generated by tract swap and group swap.

Second, it maps every orbit to the canonical pair
\[
(t,d)
\]
used in the proof and checks that this representation is bijective.

For every raw configuration it independently computes the segregation indices from their original definitions and from the closed forms
\[
D=\frac dN,
\qquad
I=\frac12+\frac{d^2}{2t(2N-t)}.
\]
The two computations agree exactly.

The replay verifies:
- canonical-orbit counts \(1,3,5,8,11,15,19,24\) for \(N=1,\ldots,8\);
- no strict reversal through \(N=7\);
- exactly one strict reversal at \(N=8\);
- the exact witness values \(1/8,8/15,1/4,17/32\);
- the earlier \(N=3\) weak-order split is only a dissimilarity tie resolved by isolation;
- the explicit reversal family for every \(8\le N\le500\) as a finite consistency check.

The all-\(N\) family is proved algebraically above; the finite replay is not a substitute for that proof.

Run:

`python3 verify_dissimilarity_isolation_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Duncan and Duncan's 1955 methodological analysis established the dissimilarity index as a central evenness measure of residential segregation. In their notation it is one half the sum of the absolute differences between the two groups' tractwise population shares, and it has the familiar interpretation as the fraction of one group that would need to relocate to reproduce the other group's distribution.

Bell's 1954 probability model developed the probabilistic logic behind ecological isolation and interaction measures. Later work made the contrast with dissimilarity explicit.

Lieberson and Carter's 1982 reconsideration states that dissimilarity and isolation tap the same segregation process only partly, that isolation incorporates composition, and that using the two approaches can yield substantially different conclusions about segregation trends and intercity differences.

Massey and Denton subsequently organized segregation measurement into distinct dimensions. Dissimilarity represents evenness, whereas isolation represents exposure. Their review emphasizes that measures from different dimensions answer different substantive questions rather than being interchangeable scalar summaries.

The present result removes citywide group-composition differences entirely by fixing both groups at exactly one half of the population and then asks for the first exact finite ranking conflict in the simplest two-tract geometry. The inspected literature establishes the substantive distinction between the measures but does not state the closed two-tract formula
\[
I=\frac12+\frac{d^2}{2t(2N-t)},
\]
the sharp \(N=8\) strict-reversal threshold, the unique first pair, or the all-\(N\) continuation family.

Targeted searches using dissimilarity/isolation aliases, two-tract and two-neighborhood language, equal group totals, rank-reversal language, and the exact witness values did not locate these statements.

## Limitations
The result fixes exactly two tracts and equal citywide group sizes.

Isolation is composition-sensitive in general. The equal-total assumption deliberately removes citywide composition as an explanation for the disagreement; the remaining reversal is driven by how local imbalance interacts with tract size.

The cutoff is an exact integer-census boundary, not a claim that segregation measurement is substantively reliable at very small populations.

The theorem does not compare spatially weighted extensions of either index.

An unindexed exercise, software test case, or specialized small-sample segregation paper could contain the same witness even though the sharp boundary theorem was not located.

## References
1. W. Bell, “A Probability Model for the Measurement of Ecological Segregation,” *Social Forces* 32(4), 357–364, published 1 May 1954. DOI: 10.2307/2574118.
2. O. D. Duncan and B. Duncan, “A Methodological Analysis of Segregation Indexes,” *American Sociological Review* 20(2), 210–217, April 1955.
3. S. Lieberson and D. K. Carter, “Temporal Changes and Urban Differences in Residential Segregation: A Reconsideration,” *American Journal of Sociology* 88(2), 296–310, published 1 September 1982. DOI: 10.1086/227672.
4. D. S. Massey and N. A. Denton, “The Dimensions of Residential Segregation,” *Social Forces* 67(2), 281–315, published 1 December 1988. DOI: 10.1093/sf/67.2.281.
