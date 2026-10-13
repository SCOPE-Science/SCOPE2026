# Jaccard–Ochiai similarity first strictly reverses at five species
## Finding
For a pair of communities, write
\[
a=|X\cap Y|,
\qquad
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
and the Ochiai similarity is
\[
O(a,b,c)
=
\frac{a}{\sqrt{(a+b)(a+c)}}.
\]

Consider two comparisons with signatures
\[
(a,b,c)
\quad\text{and}\quad
(A,B,C),
\]
with
\[
a,A>0,
\qquad
b\le c,
\qquad
B\le C.
\]

Define
\[
u=\frac{b+c}{a},
\qquad
v=\frac{bc}{a^2},
\]
and analogously
\[
U=\frac{B+C}{A},
\qquad
V=\frac{BC}{A^2}.
\]

Then Jaccard and Ochiai give opposite strict rankings exactly when
\[
(u-U)(u+v-U-V)<0.
\]

Their weak orderings first differ when the gamma-richness bound is
\[
3.
\]
The unique first mismatch is
\[
(1,0,2)
\quad\text{versus}\quad
(1,1,1).
\]
Both have
\[
J=\frac13,
\]
but their squared Ochiai similarities are
\[
\frac13
\quad\text{and}\quad
\frac14,
\]
so Ochiai breaks the Jaccard tie in favor of the nested pair.

No strict rank reversal is possible when each comparison has gamma richness at most
\[
4.
\]

At gamma richness
\[
5,
\]
strict reversal occurs for the first time. Up to swapping the two sites inside a comparison, the unique first pair is
\[
P=(1,0,4)
\quad\text{versus}\quad
Q=(1,1,2).
\]

Their Jaccard similarities are
\[
J(P)=\frac15
<
\frac14
=
J(Q).
\]

Their squared Ochiai similarities are
\[
O(P)^2=\frac15
>
\frac16
=
O(Q)^2,
\]
and hence
\[
O(P)>O(Q).
\]

Thus Jaccard regards the more balanced-mismatch comparison \(Q\) as more similar, while Ochiai regards the nested comparison \(P\) as more similar.

The effect persists indefinitely. For every integer
\[
r\ge2,
\]
set
\[
P_r=(1,0,r+2),
\qquad
Q_r=(1,1,r).
\]
Then
\[
J(P_r)<J(Q_r)
\]
but
\[
O(P_r)>O(Q_r).
\]

## Assumptions and scope
The data are pairwise species presence–absence data.

Each comparison has positive overlap:
\[
a>0.
\]
Zero-overlap pairs satisfy
\[
J=O=0
\]
and cannot participate in a strict reversal against another zero-overlap pair.

Gamma richness means the union size
\[
a+b+c.
\]
The sharp finite statement bounds the union size of each comparison separately.

Site labels inside a comparison are immaterial, so signatures are normalized by
\[
b\le c.
\]

The theorem compares Jaccard and the standard binary Ochiai coefficient. It does not cover abundance-weighted extensions, functional or phylogenetic generalizations, or similarity measures that incorporate joint absences.

## Proof
Write
\[
u=\frac{b+c}{a}
\]
and
\[
v=\frac{bc}{a^2}.
\]
Then
\[
J
=
\frac{1}{1+u}.
\]

For Ochiai,
\[
O^2
=
\frac{a^2}{(a+b)(a+c)}
=
\frac{1}{(1+b/a)(1+c/a)}
=
\frac{1}{1+u+v}.
\]

Both functions
\[
x\mapsto\frac1{1+x}
\]
are strictly decreasing on the nonnegative reals. Therefore two comparisons reverse exactly when the Jaccard key \(u\) and the squared-Ochiai key \(u+v\) order them oppositely:
\[
(u-U)(u+v-U-V)<0.
\]

This proves the general necessary-and-sufficient criterion.

For the finite boundary, every pair of nonempty communities with positive overlap and gamma richness at most \(N\) is represented uniquely up to site swap by an integer signature
\[
(a,b,c)
\]
satisfying
\[
a\ge1,\qquad
0\le b\le c,\qquad
a+b+c\le N.
\]

The numbers of such signatures for
\[
N=1,2,3,4,5
\]
are
\[
1,\ 3,\ 7,\ 13,\ 22.
\]

Exact pairwise comparison gives strict-reversal counts
\[
0,\ 0,\ 0,\ 0,\ 1.
\]

At \(N=5\), the single reversing pair is
\[
(1,0,4)
\quad\text{and}\quad
(1,1,2),
\]
with the values displayed above.

The same finite domain is independently reconstructed from all ordered pairs of nonempty subsets of an \(N\)-species universe and then quotiented by site swap; this produces exactly the same signatures.

For the infinite family,
\[
J(P_r)=\frac1{r+3},
\qquad
J(Q_r)=\frac1{r+2},
\]
so
\[
J(P_r)<J(Q_r).
\]
Also
\[
O(P_r)^2=\frac1{r+3},
\]
whereas
\[
O(Q_r)^2=\frac1{2(r+1)}.
\]
Their difference is
\[
O(P_r)^2-O(Q_r)^2
=
\frac{r-1}{2(r+1)(r+3)}>0
\]
for every
\[
r\ge2.
\]
Therefore
\[
O(P_r)>O(Q_r)
\]
for all such \(r\).

## Verification
The embedded `verify_jaccard_ochiai_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

It constructs the finite signature domain in two independent ways:
- direct enumeration of all integer triples satisfying the signature constraints;
- all ordered pairs of nonempty subsets of an \(N\)-species universe, reduced to Venn counts and then normalized by site swap.

The two constructions agree exactly through the checked range.

The verifier compares Jaccard directly and compares Ochiai through \(O^2\), which has exactly the same ordering because square root is strictly increasing.

It checks:
- signature counts
  \[
  1,\ 3,\ 7,\ 13,\ 22
  \]
  through gamma-richness bounds \(1\) to \(5\);
- weak-order mismatch counts
  \[
  0,\ 0,\ 1,\ 5,\ 12;
  \]
- strict-reversal counts
  \[
  0,\ 0,\ 0,\ 0,\ 1;
  \]
- the unique first weak split at gamma richness \(3\);
- the unique first strict reversal at gamma richness \(5\);
- the algebraic ordering criterion for every checked signature pair;
- the infinite family for
  \[
  2\le r\le500
  \]
  as a finite consistency test.

The general criterion and the infinite family are proved algebraically above; the exhaustive replay establishes the complete finite first boundary.

Run:

`python3 verify_jaccard_ochiai_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Jackson, Somers and Harvey directly compared Jaccard and Ochiai coefficients on ecological presence–absence data. Their fish-community study emphasizes that Jaccard behaves as a co-occurrence measure with a pronounced occurrence-frequency or size effect, whereas Ochiai is less affected by that size influence. That distinction motivates asking when the two coefficients can actually reverse pairwise similarity rankings.

Pavoine later treats Jaccard and Ochiai together in a common ecological-similarity framework, gives their matching-component formulas, and compares their behavior on theoretical and empirical community data. Her full text makes clear that the coefficients share the same presence–absence ingredients but normalize them differently.

The prior literature therefore establishes the ecological relevance of comparing these two similarities and the mechanism by which they respond differently to richness and frequency structure. The inspected sources do not state the exact cross-comparison criterion
\[
(u-U)(u+v-U-V)<0,
\]
the first weak-order split at gamma richness \(3\), the sharp first strict reversal at gamma richness \(5\), the uniqueness of the first pair, or the infinite family above.

Targeted searches using Jaccard/Ochiai aliases, rank-reversal language, exact Venn signatures, nested-community language, and minimum-species language did not locate those statements.

## Limitations
The theorem concerns binary pairwise community similarity.

The finite boundary is a Venn-signature statement and does not classify the joint labeled geometry of several communities considered simultaneously.

The result does not claim that either coefficient is ecologically preferable in every setting.

The exact criterion is an elementary consequence of the published formulas, so an unindexed exercise, software test, or specialist note could contain an equivalent observation even though the sharp boundary theorem was not located.

## References
1. D. A. Jackson, K. M. Somers and H. H. Harvey, “Similarity Coefficients: Measures of Co-Occurrence and Association or Simply Measures of Occurrence?”, *The American Naturalist* 133(3), 436–453, published 1 March 1989. DOI: 10.1086/284927.
2. S. Pavoine, “Functional and phylogenetic similarity among communities”, *Methods in Ecology and Evolution* 5, 666–675, 2014. DOI: 10.1111/2041-210X.12193.
