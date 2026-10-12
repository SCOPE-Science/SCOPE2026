# Jaccard–Simpson species similarity first reverses at four species
## Finding
For a pair of sites, write
\[
a=|X\cap Y|,
\]
\[
b=|X\setminus Y|,
\qquad
c=|Y\setminus X|,
\]
and swap the site labels if necessary so that
\[
b\le c.
\]

The Jaccard similarity is
\[
J(a,b,c)=\frac{a}{a+b+c},
\]
and the Simpson similarity complementary to Simpson turnover dissimilarity is
\[
S(a,b,c)=\frac{a}{a+b}.
\]

Consider two site-pair comparisons with signatures
\[
(a,b,c)
\quad\text{and}\quad
(A,B,C),
\]
where
\[
a,A>0,
\qquad
b\le c,
\qquad
B\le C.
\]

Then Jaccard and Simpson rank the two comparisons in opposite strict orders if and only if the ratios
\[
\frac{b}{a}
\quad\text{and}\quad
\frac{B}{A}
\]
are ordered oppositely to
\[
\frac{b+c}{a}
\quad\text{and}\quad
\frac{B+C}{A}.
\]

Equivalently, one comparison must have the smaller minimum unique-to-shared ratio but the larger total unique-to-shared ratio.

This criterion gives a sharp finite boundary. If each site pair has regional or gamma richness
\[
a+b+c\le3,
\]
no strict reversal is possible.

At gamma richness \(4\), strict reversal occurs for the first time. Up to swapping the two sites inside each comparison, exactly three unordered Venn-signature pairs reverse:
\[
(1,0,2)\quad\text{versus}\quad(2,1,1),
\]
\[
(1,0,3)\quad\text{versus}\quad(1,1,1),
\]
and
\[
(1,0,3)\quad\text{versus}\quad(2,1,1).
\]

Their exact similarity values are
\[
(J,S)(1,0,2)=\left(\frac13,1\right),
\]
\[
(J,S)(1,0,3)=\left(\frac14,1\right),
\]
\[
(J,S)(1,1,1)=\left(\frac13,\frac12\right),
\]
and
\[
(J,S)(2,1,1)=\left(\frac12,\frac23\right).
\]

Thus every first-layer reversal compares a nested pair of communities, which Simpson similarity treats as perfectly similar because the poorer site is a subset of the richer site, with a non-nested pair that Jaccard ranks as more similar because it has a larger shared fraction of the total species pool.

The mechanism persists indefinitely. For every integer
\[
r\ge2,
\]
the signatures
\[
P_r=(1,0,r)
\]
and
\[
Q_r=(r,1,1)
\]
satisfy
\[
S(P_r)=1>S(Q_r)=\frac{r}{r+1},
\]
while
\[
J(P_r)=\frac1{r+1}
<
\frac{r}{r+2}
=
J(Q_r).
\]

## Assumptions and scope
The data are binary species-presence data for pairs of sites.

Both communities in each comparison are nonempty.

The Simpson quantity is the similarity
\[
1-\beta_{\mathrm{sim}},
\]
where
\[
\beta_{\mathrm{sim}}
=
\frac{\min(b,c)}{a+\min(b,c)}
\]
is Simpson turnover dissimilarity. After ordering the sites so \(b\le c\), this gives
\[
S=\frac{a}{a+b}.
\]

Gamma richness means
\[
|X\cup Y|=a+b+c
\]
for a single site pair. The sharp boundary compares arbitrary site pairs whose individual gamma richness is bounded by the same integer; the four sites used in two comparisons need not be distinct.

Pairs with
\[
a=0
\]
have
\[
J=S=0
\]
and cannot participate in a strict reversal against a positive-overlap pair.

## Proof
With
\[
b\le c,
\]
the two similarities can be rewritten as
\[
S(a,b,c)
=
\frac{1}{1+b/a}
\]
and
\[
J(a,b,c)
=
\frac{1}{1+(b+c)/a}.
\]

Because
\[
x\mapsto\frac1{1+x}
\]
is strictly decreasing on the nonnegative reals, Simpson similarity compares two site pairs solely through
\[
\frac{b}{a},
\]
whereas Jaccard similarity compares them solely through
\[
\frac{b+c}{a}.
\]

Hence the two indices reverse a strict ranking exactly when those two ratio comparisons have opposite signs:
\[
\left(
\frac{b}{a}-\frac{B}{A}
\right)
\left(
\frac{b+c}{a}-\frac{B+C}{A}
\right)
<0.
\]

This proves the general criterion.

For the sharp finite boundary, enumerate Venn signatures with
\[
b\le c,
\]
nonempty sites, and
\[
a+b+c\le N.
\]
The numbers of signatures for
\[
N=1,2,3,4
\]
are respectively
\[
1,\ 4,\ 9,\ 17.
\]

For
\[
N\le3,
\]
no pair satisfies the strict reversal criterion.

For
\[
N=4,
\]
exactly three unordered signature pairs satisfy it, namely the three displayed in the finding. Their exact \(J\) and \(S\) values verify the opposite rankings directly.

A concrete four-species witness for the first pair is
\[
X=\{1\},
\qquad
Y=\{1,2,3\},
\]
versus
\[
U=\{1,2,3\},
\qquad
V=\{1,2,4\}.
\]
The first comparison has
\[
(J,S)=\left(\frac13,1\right),
\]
while the second has
\[
(J,S)=\left(\frac12,\frac23\right).
\]

Finally, for the infinite family,
\[
S(P_r)=1,
\qquad
S(Q_r)=\frac{r}{r+1}<1.
\]
For Jaccard,
\[
J(Q_r)-J(P_r)
=
\frac{r}{r+2}-\frac1{r+1}
=
\frac{r^2-2}{(r+1)(r+2)}>0
\]
for every integer
\[
r\ge2.
\]
So every pair in the family is a strict reversal.

## Verification
The embedded `verify_jaccard_simpson_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

It generates every ordered Venn signature with site-swap normalization
\[
b\le c
\]
through gamma richness \(8\).

For every pair of signatures it independently checks that direct comparison of exact Jaccard and Simpson fractions is equivalent to the ratio criterion in the proof.

At the sharp boundary it verifies:
\[
1,\ 4,\ 9,\ 17
\]
normalized signatures through gamma richness \(1,2,3,4\);
zero strict reversals through gamma richness \(3\);
exactly three strict reversals at gamma richness \(4\);
and exactly the three displayed signature pairs.

It also checks the infinite family
\[
(1,0,r)
\quad\text{versus}\quad
(r,1,1)
\]
for every integer
\[
2\le r\le500
\]
as a finite consistency test. The infinite statement itself is proved algebraically above.

Run:

`python3 verify_jaccard_simpson_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Koleff, Gaston and Lennon review twenty-four presence–absence beta-diversity measures in a common \(a,b,c\) notation and emphasize that different measures capture different aspects of compositional change. Their table includes Jaccard similarity
\[
\frac{a}{a+b+c}
\]
and the Simpson turnover quantity based on
\[
\frac{\min(b,c)}{a+\min(b,c)}.
\]
They distinguish broad-sense measures affected by richness gradients from narrow-sense turnover measures that focus more directly on compositional replacement.

Baselga later makes the ecological mechanism especially explicit: a replacement measure should be independent of richness differences, so adding species only to the richer site should not change Simpson turnover, whereas total Jaccard dissimilarity does respond to those additional unique species. This is exactly the structural tension captured by the reversal criterion above.

The prior literature therefore supplies the two indices, their \(a,b,c\) formulas, and the ecological reason their responses differ. The inspected sources do not state the exact pairwise rank-reversal criterion, the sharp gamma-richness-four boundary, the complete three-pair first layer, or the infinite family above.

Targeted searches using Jaccard/Simpson aliases, rank-reversal language, nested-community language, exact \(a,b,c\) patterns, and four-species language did not locate those statements.

## Limitations
The theorem concerns pairwise presence–absence similarity, not abundance-weighted beta diversity.

The Simpson quantity is the turnover-oriented Simpson similarity complementary to \(\beta_{\mathrm{sim}}\), not Simpson's alpha-diversity concentration index.

The finite classification is by Venn-count signature. It does not classify all joint isomorphism types of four labeled communities appearing simultaneously in two comparisons.

The result isolates ranking disagreement between two scalar indices; it does not claim that either ranking is ecologically preferable in every application.

An unindexed exercise, software test suite, or figure annotation could contain one of the four-species witnesses even if the exact boundary theorem is absent.

## References
1. P. Koleff, K. J. Gaston and J. J. Lennon, “Measuring beta diversity for presence–absence data,” *Journal of Animal Ecology* 72, 367–382, first published 17 April 2003. DOI: 10.1046/j.1365-2656.2003.00710.x.
2. A. Baselga, “The relationship between species replacement, dissimilarity derived from nestedness, and nestedness,” *Global Ecology and Biogeography* 21, 1223–1232, first published 13 February 2012. DOI: 10.1111/j.1466-8238.2011.00756.x.
