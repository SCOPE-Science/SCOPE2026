# Four papers and nine citations are the sharp h-index–g-index reversal boundary
## Finding
Let a citation profile be a nonincreasing integer vector
\[
c_1\ge c_2\ge\cdots\ge c_n\ge0.
\]

The Hirsch index is
\[
h
=
\max\{r:c_r\ge r\},
\]
with value zero when no positive \(r\) satisfies the condition.

The standard Egghe index, constrained by the number of published papers, is
\[
g
=
\max\left\{r\le n:
\sum_{i=1}^{r}c_i\ge r^2
\right\}.
\]

Compare two profiles only when they have the same number \(n\) of papers and the same total number
\[
C=\sum_{i=1}^{n}c_i
\]
of citations.

Opposite strict rankings by \(h\) and \(g\) are impossible whenever
\[
C\le8.
\]

The global sharp boundary is
\[
C=9,
\qquad
n=4.
\]

At this first layer there are exactly fifteen unordered reversing pairs. The profiles with
\[
(h,g)=(1,3)
\]
are exactly
\[
(9,0,0,0),
\quad
(8,1,0,0),
\quad
(7,1,1,0).
\]

The profiles with
\[
(h,g)=(2,2)
\]
are exactly
\[
(5,2,1,1),
\quad
(4,3,1,1),
\quad
(4,2,2,1),
\quad
(3,3,2,1),
\quad
(3,2,2,2).
\]

Every pair obtained by choosing one profile from each displayed class is a strict reversal. Hence the first layer contains
\[
3\cdot5=15
\]
unordered reversing pairs.

A particularly simple witness is
\[
A=(3,2,2,2),
\qquad
B=(7,1,1,0).
\]
They have the same four papers and the same nine total citations, but
\[
h(A)=2>1=h(B),
\]
while
\[
g(A)=2<3=g(B).
\]

If every listed paper is additionally required to have at least one citation, no reversal exists at total nine. The positive-citation sharp boundary is
\[
n=4,
\qquad
C=10.
\]
There are exactly two unordered reversing pairs:
\[
(7,1,1,1)
\quad\text{versus}\quad
(4,2,2,2),
\]
and
\[
(7,1,1,1)
\quad\text{versus}\quad
(3,3,2,2).
\]

Finally, appending zero-cited papers to both members of any unrestricted boundary pair preserves both indices, so the nine-citation reversal exists for every
\[
n\ge4.
\]

## Assumptions and scope
Citation counts are nonnegative integers and are sorted in nonincreasing order.

The standard paper-count-constrained definition of the \(g\)-index is used. Thus \(g\le n\); a modified extension that allows fictitious zero papers beyond the publication count is a different index and is not considered here.

Both compared profiles have the same number of papers and the same total number of citations. These controls isolate the effect of how a fixed citation budget is distributed across papers.

The positive-citation variant is stated separately because zero-cited publications are allowed by the usual citation-vector formalism but may be omitted from some empirical datasets.

The result is an ordinal statement about bibliometric indices. It does not claim that either index is a normatively preferable measure of scientific quality.

## Proof
For every citation profile,
\[
h\le g.
\]
Indeed, if the \(h\)-index is \(h\), then the first \(h\) papers each have at least \(h\) citations, so
\[
\sum_{i=1}^{h}c_i\ge h^2,
\]
and the trial value \(h\) is admissible in the definition of \(g\).

Now suppose the common total citation count satisfies
\[
C\le8.
\]
A profile with \(g\ge3\) would require
\[
\sum_{i=1}^{3}c_i\ge9,
\]
which is impossible. Hence
\[
g\le2.
\]
Together with \(h\le g\), the only positive-index pairs are
\[
(1,1),
\quad
(1,2),
\quad
(2,2).
\]
No two such pairs can be ordered oppositely in both coordinates. Therefore strict reversal is impossible below nine total citations, regardless of the number of papers.

At total nine, a reversal requires one profile to have
\[
(h,g)=(1,3)
\]
and the other to have
\[
(h,g)=(2,2).
\]
If \(n\le2\), then \(g\le2\). If \(n=3\), the sum of the first three citation counts is the entire total, namely nine, so every profile has
\[
g=3.
\]
Thus four papers are necessary.

For
\[
n=4,
\qquad
C=9,
\]
a profile has \(h=1\) exactly when
\[
c_2\le1.
\]
To also have \(g=3\), the first three entries must sum to at least nine. Because the total itself is nine, this forces
\[
c_4=0
\]
and
\[
c_1+c_2+c_3=9.
\]
With
\[
1\ge c_2\ge c_3\ge0,
\]
the only solutions are
\[
(9,0,0,0),
\quad
(8,1,0,0),
\quad
(7,1,1,0).
\]

A profile has \((h,g)=(2,2)\) exactly when
\[
c_2\ge2,
\qquad
c_3\le2,
\qquad
c_1+c_2+c_3\le8.
\]
Together with the total-nine constraint and monotonicity, direct integer solving gives exactly
\[
(5,2,1,1),
\quad
(4,3,1,1),
\quad
(4,2,2,1),
\quad
(3,3,2,1),
\quad
(3,2,2,2).
\]
Every cross-pair has larger \(h\) but smaller \(g\) in the second class, proving the exact count of fifteen.

For the positive-citation variant at total nine, a profile with \(h=1\) has every entry after the first at most one. If there are at least four positive entries, at least one citation lies outside the first three, so their sum is at most eight and \(g\le2\). Thus no positive-citation reversal occurs at nine.

At
\[
n=4,
\qquad
C=10,
\]
positive \((h,g)=(1,3)\) forces
\[
(7,1,1,1).
\]
Positive \((h,g)=(2,2)\) profiles capable of reversing against it must have
\[
c_3=c_4=2,
\qquad
c_1+c_2=6,
\]
which gives exactly
\[
(4,2,2,2)
\quad\text{and}\quad
(3,3,2,2).
\]
This proves the positive-citation sharp boundary and its two-pair classification.

## Verification
The embedded `verify_h_g_equal_total_boundary.py` uses only the Python standard library and exact integer arithmetic.

It replays the inequality
\[
h\le g
\]
across a finite test range, exhaustively enumerates sorted citation profiles through the sharp unrestricted and positive-citation layers, verifies the complete profile lists and pair counts, and checks zero-padding invariance through one hundred papers.

It also exhaustively checks that no strict equal-total reversal occurs below nine citations over a larger finite census and that no three-paper reversal occurs through sixty citations.

Run:

`python3 verify_h_g_equal_total_boundary.py`

The first output line must be `VERIFY_OK`.

The universal lower bounds are proved symbolically above; they do not rely on extrapolation from the finite replay.

## Relationship to prior work
Hirsch introduced the \(h\)-index as the largest number of papers having at least that many citations.

Egghe introduced the \(g\)-index to increase the weight assigned to highly cited papers. The standard definition takes the largest number of top-ranked papers whose cumulative citations reach the square of that number.

Empirical comparisons already show that the two indices can rank researchers differently. Schreiber's comparison of twenty-six physicists reports that ordering the datasets by \(h\) or by \(g\) produces significantly different arrangements. Thus generic rank disagreement is prior work and is not the claim here.

Recent mathematical work also formalizes citation vectors with nonnegative integer entries, proves the standard relation
\[
h\le g,
\]
and studies indices interpolating between \(h\) and \(g\).

The present result fixes both the publication count and the total citation count and asks for the smallest citation budget at which opposite strict rankings become possible. Targeted searches using equal-paper, equal-total, citation-vector, rank-reversal, exact-profile, and smallest-boundary language did not locate the nine-citation theorem, the complete fifteen-pair first layer, or the ten-citation positive variant.

## Limitations
The sharp boundary is specific to the standard paper-count-constrained \(g\)-index and integer citation counts.

The unrestricted first layer permits a zero-cited paper. The positive-citation variant addresses datasets in which every listed publication must have at least one citation.

The result controls both paper count and total citations. If either is allowed to vary between the two researchers, smaller or qualitatively different examples can occur.

Generic disagreement between the \(h\)-index and \(g\)-index is already documented. The new claim is only the exact equal-resource finite boundary and its complete first-layer classification.

A recent full-text mathematical treatment contains several small illustrative citation vectors, and an unindexed teaching example or software test could also contain an isolated witness. Exact-profile searches did not locate the displayed pair; moreover, an isolated witness would not by itself cover the minimality or complete first-layer classification.

## References
1. J. E. Hirsch, “An index to quantify an individual's scientific research output,” arXiv:physics/0508025, first submitted 3 August 2005; later *Proceedings of the National Academy of Sciences* 102, 16569–16572 (2005). DOI: 10.1073/pnas.0507655102.
2. L. Egghe, “An improvement of the h-index: the g-index,” *ISSI Newsletter* 2(1), 8–9 (2006).
3. L. Egghe, “Theory and practise of the g-index,” *Scientometrics* 69, 131–152 (2006). DOI: 10.1007/s11192-006-0144-7.
4. M. Schreiber, “An empirical investigation of the g-index for 26 physicists in comparison with the h-index, the A-index, and the R-index,” *Journal of the American Society for Information Science and Technology* 59, 1513–1522, first published 14 May 2008. DOI: 10.1002/asi.20856.
5. R. Nuermaimaiti, L. Bogachev, and J. Voss, “A citation index bridging Hirsch's h and Egghe's g,” *PNAS Nexus* 5, pgaf368, published 13 January 2026. DOI: 10.1093/pnasnexus/pgaf368.
