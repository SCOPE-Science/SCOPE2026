# Exact size-only NODF ceiling and Ferrers maximizers for rectangular ecological networks
## Finding
Consider a bipartite ecological incidence matrix with
\[
m\ge2
\]
rows, with
\[
n\ge2
\]
columns, and with no entirely zero row or column. Entries are either zero or one. No constraint is imposed on the total number of ones (the number of interactions).

Use the classical NODF metric—nestedness based on overlap and decreasing fill—normalized to the interval
\[
[0,1].
\]

Write
\[
a=\min\{m,n\},\qquad
b=\max\{m,n\}=qa+r,\qquad
q\ge1,\quad 0\le r<a,
\]
and put
\[
K=\binom{m}{2}+\binom{n}{2},\qquad
T=(a-r)\binom{q}{2}+r\binom{q+1}{2}.
\]

**The exact maximum over all such binary incidence matrices is**
\[
\boxed{\max\mathrm{NODF}=1-\frac{T}{K}.}
\]

All maximizing networks are Ferrers (perfectly nested in the sense of neighborhood containment), up to independent permutations of rows and columns and swapping the two guilds. On the larger guild, the degree values
\[
1,2,\ldots,a
\]
all occur, and each degree occurs either
\[
q\quad\text{or}\quad q+1
\]
times, with exactly
\[
r
\]
of the degree values having multiplicity
\[
q+1.
\]

Conversely every such balanced Ferrers network attains the maximum. For fixed dimensions there are exactly
\[
\boxed{\binom{a}{r}}
\]
isomorphism classes of maximizers under independent row and column permutations.

For example, a network with two species on one side and three on the other has maximum
\[
\frac34,
\]
while a network with three species on one side and four on the other has maximum
\[
\frac89.
\]

In a square network the maximum equals one, recovering the previously known staircase case. For every strictly rectangular network with both guilds of size at least two, the maximum is strictly below one, even when its interaction count is unrestricted.

For fixed
\[
a\ge2
\]
and ever larger opposite guild,
\[
\lim_{b\to\infty}\max\mathrm{NODF}=1-\frac1a.
\]
Thus shape alone imposes a nonvanishing ceiling on the index.

## Assumptions and scope
The incidence matrix has only zero-one entries and no isolated vertices. Its two guild sizes are fixed, but its total number of links is **free to vary**.

For any two rows of unequal positive degree, the pair's NODF contribution is the number of shared presences divided by the *smaller* row degree. The contribution is zero when the degrees are equal. The same definition applies to column pairs. Classical normalized NODF is the sum of those pair contributions divided by the sum of the number of unordered pairs within each guild,
\[
\binom{m}{2}+\binom{n}{2}.
\]

This convention is invariant under separate permutations of rows and columns and agrees with the order-independent formulation of Britton, Almeida Neto, and Corso. It is equivalent to dividing the original 0-to-100 scale by 100.

The theorem does not cover weighted NODF, alternative tie rules, zero-degree vertices, a guild of size one, or maximization at a prescribed number of links. Those are distinct domains.

## Proof
**Step 1: the unavoidable tie deficit.**
Interchange rows and columns if necessary so that there are
\[
a\]
rows and
\[
b\]
columns. Every column has a positive degree in
\[
\{1,\ldots,a\}.
\]
Let
\[
c_d
\]
be the number of columns of degree
\[
d.
\]
Then
\[
\sum_{d=1}^{a}c_d=b.
\]
Each unordered pair of columns with equal degree contributes zero to NODF, so the number of such pairs is
\[
E=\sum_{d=1}^{a}\binom{c_d}{2}.
\]

The function
\[
t\longmapsto\binom{t}{2}
\]
is discretely convex. If two nonnegative multiplicities differ by at least two, transferring one column from the larger to the smaller multiplicity strictly reduces their contribution to
\[
E.
\]
Consequently the minimum of
\[
E
\]
subject to the displayed sum is attained *exactly* when all multiplicities differ by at most one. Since
\[
b=qa+r,\quad q\ge1,\quad 0\le r<a,
\]
this minimum is
\[
T=(a-r)\binom{q}{2}+r\binom{q+1}{2}.
\]

Every non-tied pair has a NODF contribution at most one. There are
\[
K=\binom{a}{2}+\binom{b}{2}
\]
row and column pairs in all. Hence every admissible matrix satisfies
\[
\mathrm{NODF}\le\frac{K-E}{K}\le1-\frac{T}{K}.
\]

**Step 2: simultaneous sharpness.**
For each degree
\[
d\in\{1,\ldots,a\},
\]
choose a positive multiplicity
\[
c_d\in\{q,q+1\},
\]
with exactly
\[
r
\]
values equal to
\[
q+1.
\]
Make exactly
\[
c_d
\]
columns whose ones occupy the first
\[
d
\]
rows, all remaining entries zero.

These columns have the prescribed degrees, and their neighborhoods are totally ordered by inclusion. The row at position
\[
i
\]
has degree
\[
\sum_{d=i}^{a}c_d.
\]
Because every
\[
c_d\ge1,
\]
the row degrees are strictly decreasing. Their neighborhoods are also totally ordered by inclusion.

It follows that every row pair contributes one, every unequal-degree column pair contributes one, and precisely the
\[
T
\]
equal-degree column pairs contribute zero. Thus
\[
\mathrm{NODF}=1-\frac{T}{K},
\]
proving the maximum.

**Step 3: necessity and classification.**
Suppose a matrix attains that maximum. Each column tie already loses one unit relative to the largest possible pair sum, so equality in both inequalities from Step 1 forces exactly
\[
T
\]
column ties and no loss from any other pair. Therefore the column degree multiplicities are balanced as in Step 1, every row pair has distinct degrees and contributes one, and every unequal-degree column pair contributes one.

A row pair contributes one precisely when the row neighborhood of smaller degree is a subset of the other row neighborhood. Since this holds for *every* row pair, all row neighborhoods form a strict inclusion chain. After sorting the rows by degree, the columns are initial segments of that chain; the incidence matrix is Ferrers. The longer-guild degree multiset is already required to have multiplicities
\[
q\quad\text{or}\quad q+1
\]
for every value from one to
\[
a.
\]

A Ferrers matrix is determined up to row and column permutation by that longer-guild degree multiset. Choosing which
\[
r
\]
of its
\[
a
\]
possible degrees receive one additional column therefore yields exactly
\[
\binom{a}{r}
\]
inequivalent maximizing matrices.

**Step 4: strict rectangular deficit and limiting ceiling.**
When
\[
a=b,
\]
we have
\[
q=1,\quad r=0,\quad T=0,
\]
and recover the unique square staircase maximizer previously characterized by Britton and coauthors.

If
\[
b>a\ge2,
\]
some degree occurs at least twice, so
\[
T>0.
\]
Thus the maximum is strictly below one.

For fixed
\[
a\ge2,
\]
as
\[
b\to\infty,
\]
the balanced tie count satisfies
\[
T=\frac{b^2}{2a}+O(b),
\]
whereas
\[
K=\frac{b^2}{2}+O(b).
\]
This gives the asserted limiting ceiling.

## Verification
The accompanying `verify_shape_only_nodf.py` uses only the Python standard library. It independently evaluates NODF from incidence bitsets using integer arithmetic scaled by a common denominator, explicitly rejecting matrices with an empty row or column.

For each of the sizes
\[
(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),
\]
it enumerates *every* labeled binary matrix with no zero row or column: a total of
\[
176554
\]
matrices. It verifies the claimed exact maximum, checks that every maximizing matrix has nested row neighborhoods, and counts the longer-guild degree-multiplicity types, checking that the count is exactly
\[
\binom{a}{r}.
\]

It also constructs the claimed Ferrers extremizers and checks the equality formula across a larger rectangular parameter grid. The exhaustive computations concern only the listed finite shapes; the universal result follows from the proof above, not from extrapolation of those computations.

Run:

`python3 verify_shape_only_nodf.py`

The verifier prints `VERIFY_OK` on its first output line after all assertions have passed.

## Relationship to prior work
Almeida-Neto and collaborators introduced NODF to capture two requirements of nestedness: unequal degrees between comparable nodes, and complete paired overlap for the less-connected node. The present paper adopts exactly that index, in its row/column permutation-independent normalization.

Britton, Almeida Neto, and Corso formally characterize matrices with NODF exactly zero and exactly one. In particular, they prove that NODF one requires the square staircase matrix. **That earlier square-case theorem is not claimed as new.** Their endpoint theorems leave open the exact maximum for a prescribed *rectangular shape* and the complete set of maximizers below one. The result here gives that intermediate sharp ceiling for all shapes.

Song, Rohr, and Saavedra motivate normalization of ecological nestedness by the largest achievable value, explicitly considering network size and link count. Hoeppke and Simmons subsequently present fast numerical optimization procedures for maxima *with the number of links fixed*. The present formula is a closed-form, exact **dimension-only** ceiling with link count unrestricted, rather than a replacement for their fixed-fill optimization. It can provide a basic numerical upper bound and a shape-specific consistency check for those procedures.

Searches for exact maximal NODF, rectangular incidence matrices, balanced degrees, Ferrers matrices, and shape-only NODF ceilings, including database searches for equivalent terms, did not locate a published statement of the exact formula or a classification of all rectangular maximizers.

## Limitations
This theorem does not solve maximum NODF at a fixed connectance or fixed link count. In general the size-only ceiling cannot be attained at the observed link count; it must not be substituted for a fixed-fill normalization in ecological inference.

It assumes both guilds contain at least two species, with no isolated species, and uses the usual convention that equal-degree node pairs contribute zero. Other NODF implementations that change tie handling or pair denominators require separate analysis.

The maximizer classification is up to permutations of species labels. Nothing here implies that all balanced Ferrers incidence matrices are equally plausible under ecological formation mechanisms.

Exact-matrix search can miss unindexed or differently phrased formulas. The closest prior mathematical treatment of NODF extremes has been compared at the statement and proof level; an unlocated stronger rectangular bound remains an originality risk.

## References
1. M. Almeida-Neto, P. Guimarães, P. R. Guimarães Jr., R. D. Loyola, and W. Ulrich, “A consistent metric for nestedness analysis in ecological systems: reconciling concept and measurement,” *Oikos* 117 (2008), 1227–1239. First publicly published 7 August 2008. DOI: 10.1111/j.0030-1299.2008.16644.x.
2. N. F. Britton, M. Almeida Neto, and G. Corso, “Which Matrices Show Perfect Nestedness or the Absence of Nestedness? An Analytical Study on the Performance of NODF and WNODF,” *Biomath* 4 (2015), article 1512171; publicly published 16 January 2016. DOI: 10.11145/j.biomath.2015.12.171.
3. C. Song, R. P. Rohr, and S. Saavedra, “Why are some plant–pollinator networks more nested than others?”, *Journal of Animal Ecology* 86 (2017), 1417–1424. DOI: 10.1111/1365-2656.12749.
4. C. Hoeppke and B. I. Simmons, “maxnodf: An R package for fair and fast comparisons of nestedness between networks,” *Methods in Ecology and Evolution* 12 (2021), 580–585. DOI: 10.1111/2041-210X.13545.
