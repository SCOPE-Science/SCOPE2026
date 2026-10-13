# Nine individuals are the sharp Simpson–rarefaction identifiability boundary
## Finding
Fix a species richness
\[
S\ge1
\]
and a total abundance
\[
N\ge S.
\]
A community is a multiset of positive integer species abundances
\[
n_1,\ldots,n_S\ge1,
\qquad
\sum_{i=1}^S n_i=N,
\]
with species labels ignored.

Use the finite-sample Simpson collision probability
\[
D_2
=
\frac{\sum_i n_i(n_i-1)}{N(N-1)}
\]
for
\[
N\ge2.
\]

For a without-replacement subsample of size \(m\), let Hurlbert's rarefied expected richness be
\[
R_m
=
\sum_{i=1}^S
\left[
1-
\frac{\binom{N-n_i}{m}}{\binom{N}{m}}
\right].
\]

For every
\[
N\le8,
\]
the data
\[
(N,S,D_2)
\]
determine the full abundance multiset uniquely.

At
\[
N=9,
\]
this fails for the first time. The failure is unique up to species permutation:
\[
(1,4,4)
\qquad\text{and}\qquad
(2,2,5).
\]

Both profiles have
\[
S=3
\]
and
\[
\sum_i n_i(n_i-1)=24,
\]
so
\[
D_2=\frac{24}{9\cdot8}=\frac13.
\]

The two-draw rarefaction value carries exactly the same pair-collision information:
\[
R_2=2-D_2.
\]
Hence both first-collision profiles have
\[
R_2=\frac53.
\]

The three-draw value contains one additional factorial moment. Define
\[
T_3
=
\frac{\sum_i n_i(n_i-1)(n_i-2)}
{N(N-1)(N-2)}.
\]
Then
\[
R_3=3-3D_2+T_3.
\]

For
\[
(1,4,4),
\]
the third-factorial numerator is
\[
48,
\]
whereas for
\[
(2,2,5)
\]
it is
\[
60.
\]
Therefore
\[
R_3(1,4,4)=\frac{44}{21},
\qquad
R_3(2,2,5)=\frac{89}{42},
\]
and
\[
R_3(2,2,5)-R_3(1,4,4)=\frac1{42}.
\]

Thus nine individuals are the sharp fixed-richness point at which Simpson's pairwise concentration summary first loses enough abundance information to leave the next rarefaction point undetermined.

## Assumptions and scope
Species abundances are strictly positive integers. Richness \(S\) and total abundance \(N\) are fixed before profiles are compared.

The Simpson quantity is the without-replacement collision probability
\[
D_2
=
\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]
Its complement is Hurlbert's probability of interspecific encounter.

Rarefaction is also without replacement from the same finite collection.

The result is an identifiability statement about abundance multisets. It does not claim that Simpson concentration or rarefied richness alone is an adequate ecological description, and it does not compare communities with different richness or different total abundance.

## Proof
For a two-individual sample, the number of observed species is either one or two. The probability that both individuals belong to the same species is
\[
D_2.
\]
Therefore
\[
R_2
=
1\cdot D_2
+
2\cdot(1-D_2)
=
2-D_2.
\]

For three sampled individuals, let \(C\) be the number of equal unordered pairs among the three draws and let \(I\) indicate that all three draws belong to the same species.

If all three species labels are distinct, then
\[
C=0,\qquad I=0,
\]
and the observed richness is \(3\).

If exactly two labels agree, then
\[
C=1,\qquad I=0,
\]
and the observed richness is \(2\).

If all three labels agree, then
\[
C=3,\qquad I=1,
\]
and the observed richness is \(1\).

Hence, pointwise,
\[
S_3=3-C+I.
\]

Each of the three unordered draw-pairs agrees with probability \(D_2\), so
\[
\mathbb E[C]=3D_2.
\]
The probability that all three draws come from one species is
\[
T_3
=
\frac{\sum_i n_i(n_i-1)(n_i-2)}
{N(N-1)(N-2)}.
\]
Taking expectations gives
\[
R_3
=
3-3D_2+T_3.
\]

It remains to establish the sharp finite boundary. For every
\[
1\le N\le9
\]
and every
\[
1\le S\le N,
\]
the verifier enumerates every nondecreasing positive integer \(S\)-tuple summing to \(N\). This is exactly the set of abundance multisets.

It independently reconstructs the same finite set from all positive compositions followed by sorting. For each fixed pair \((N,S)\), profiles are grouped by the exact integer numerator
\[
Q_2=\sum_i n_i(n_i-1).
\]

For
\[
N\le8,
\]
every group is a singleton.

For
\[
N=9,
\]
there is exactly one nonsingleton group:
\[
S=3,\qquad Q_2=24,
\]
containing exactly
\[
(1,4,4)
\quad\text{and}\quad
(2,2,5).
\]

This exhaustive finite classification proves both the lower bound and uniqueness of the first collision. The displayed \(R_3\) values then follow from the exact third-factorial numerators.

## Verification
The embedded `verify_simpson_rarefaction_boundary.py` uses only the Python standard library and exact rational arithmetic.

It constructs every positive abundance multiset through
\[
N=9
\]
by two independent finite generators.

For every profile it directly evaluates Hurlbert's hypergeometric formula and verifies
\[
R_2=2-D_2
\]
and
\[
R_3=3-3D_2+T_3.
\]

It then checks all within-\((N,S)\) profile pairs and confirms that the complete collision list through nine individuals is exactly
\[
(9,3,24,\{(1,4,4),(2,2,5)\}).
\]

The verifier checks
\[
109
\]
within-slice unordered profile pairs in total.

For the first collision it verifies
\[
D_2=\frac13,
\qquad
R_2=\frac53,
\qquad
R_3(1,4,4)=\frac{44}{21},
\qquad
R_3(2,2,5)=\frac{89}{42}.
\]

Run:

`python3 verify_simpson_rarefaction_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Simpson introduced a concentration measure for classified populations.

Hurlbert recast finite-sample concentration in directly ecological terms. His probability of interspecific encounter is the complement of the without-replacement Simpson collision probability used here, and he gave the hypergeometric formula for the expected number of species in a random subsample.

Hurlbert also emphasized a broader limitation that is already prior work: collections can agree under a conventional diversity index while having different species-richness curves. The present result therefore does not claim that Simpson concentration fails to determine rarefaction in general.

Olszewski later made the connection between rarefaction and Hurlbert's probability of interspecific encounter explicit, showing that the latter is tied to the initial rise of the rarefaction curve.

The new point here is the exact discrete boundary under two natural controls, fixed total abundance and fixed observed richness: Simpson concentration actually identifies the entire abundance multiset through eight individuals; nine are necessary and sufficient for ambiguity; the first collision is unique; and the very next rarefaction depth separates it by exactly \(1/42\).

Targeted searches using Simpson concentration, probability of interspecific encounter, rarefaction, fixed richness, integer abundance profiles, factorial moments, the exact first profiles, and smallest-sample language did not locate this finite classification.

## Limitations
The threshold depends on fixing both total abundance and observed richness. If richness is allowed to vary, Simpson collisions can occur earlier.

The theorem concerns positive integer abundance profiles. Continuous relative-abundance vectors have no analogous minimum total abundance.

The exact boundary is small and elementary once formulated. An unindexed teaching note, software test, or worked rarefaction example could contain the same pair even though the fixed-richness minimality and uniqueness statement was not located.

The full Hurlbert article was inspected for the relevant formulas and discussion. The Olszewski comparison used the published abstract, so no whole-document noncoverage claim is made for that paper.

## References
1. E. H. Simpson, “Measurement of Diversity,” *Nature* 163, 688, published 30 April 1949. DOI: 10.1038/163688a0.
2. S. H. Hurlbert, “The Nonconcept of Species Diversity: A Critique and Alternative Parameters,” *Ecology* 52(4), 577–586, first published 1 July 1971. DOI: 10.2307/1934145.
3. T. D. Olszewski, “A unified mathematical framework for the measurement of richness and evenness within and among multiple communities,” *Oikos* 104(2), 377–387, first published 16 January 2004. DOI: 10.1111/j.0030-1299.2004.12519.x.
