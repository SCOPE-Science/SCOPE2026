# Six translates block the regular cuboctahedron
## Finding
Let
\[
K
=
[-1,1]^3
\cap
\left\{
x\in\mathbb R^3:
|x_1|+|x_2|+|x_3|\le2
\right\}.
\]
This is the standard regular cuboctahedron, with vertices given by the signed coordinate permutations of
\[
(1,1,0).
\]

Its blocking number satisfies
\[
b(K)\le6.
\]

An explicit configuration is obtained from the six boundary points
\[
\begin{aligned}
z_1&=(1,-1/4,-1/4),&
z_2&=-z_1,\\
z_3&=(1/4,1,-1/4),&
z_4&=-z_3,\\
z_5&=(1/4,1/4,1),&
z_6&=-z_5.
\end{aligned}
\]
The corresponding blocking translates are
\[
K+2z_1,\ldots,K+2z_6.
\]

The covering has uniform rational clearance. Define
\[
K_{1/13}
=
\left\{
x:
|x_j|\le\frac{12}{13}\ \text{for }j=1,2,3,
\quad
|x_1|+|x_2|+|x_3|\le\frac{25}{13}
\right\}.
\]
Then
\[
\partial K
\subset
\bigcup_{i=1}^6(z_i+K_{1/13})
\subset
\bigcup_{i=1}^6(z_i+\operatorname{int}K).
\tag{1}
\]

Thus the six translates are not merely a limiting blocking arrangement: the scaled boundary-cover condition has positive slack.

## Assumptions and scope
For a convex body \(C\), a blocking configuration consists of non-overlapping translates of \(C\), each touching \(C\), such that no further non-overlapping translate can be added while still touching \(C\). Its least cardinality is the blocking number \(b(C)\).

The body \(K\) is centrally symmetric:
\[
K=-K.
\]
For centrally symmetric \(C\), the standard boundary-cover criterion can be written in the following scaled form. If
\[
z_i\in\partial C,
\qquad
z_i-z_j\notin\operatorname{int}C
\quad(i\ne j),
\]
and
\[
\partial C
\subset
\bigcup_i(z_i+\operatorname{int}C),
\tag{2}
\]
then the translates
\[
C+2z_i
\]
form a blocking configuration.

Indeed, touching translates of \(C\) have translation vectors on
\[
\partial(C-C)=\partial(2C),
\]
and after division by \(2\), condition (2) is exactly the boundary-cover characterization.

The result establishes only
\[
b(K)\le6.
\]
A conjectured general lower bound would make this sharp in dimension \(3\), but that conjecture is not assumed and equality is not asserted here.

## Proof
Each proposed point \(z_i\) lies on \(\partial K\). For example,
\[
z_1=(1,-1/4,-1/4)
\]
has
\[
\|z_1\|_\infty=1,
\qquad
\|z_1\|_1=\frac32\le2.
\]
The other five points follow by coordinate permutation and central symmetry.

For distinct indices \(i,j\), the difference
\[
z_i-z_j
\]
does not lie in \(\operatorname{int}K\). For antipodal pairs one coordinate has absolute value \(2\). For every non-antipodal pair, one coordinate has absolute value at least
\[
\frac54.
\]
Thus
\[
\|z_i-z_j\|_\infty\ge\frac54>1
\]
unless the pair is antipodal, in which case the same conclusion is even stronger. Therefore
\[
z_i-z_j\notin\operatorname{int}K.
\tag{3}
\]

It remains to prove the strict boundary covering. The boundary of \(K\) has fourteen facets: six square facets
\[
x_j=\pm1
\]
and eight triangular facets
\[
\pm x_1\pm x_2\pm x_3=2.
\]
All defining coefficients are integral.

Membership in a translated inset
\[
z_i+K_{1/13}
\]
is the conjunction of fourteen rational linear inequalities. Consequently, on any fixed facet \(F\), failure of membership is a union of fourteen rational half-planes in the two affine facet coordinates.

The supplied exact checker proves (1) by exhaustive polyhedral branching. For each of the fourteen facets it starts from an exact rational polygon representing \(F\). For center \(z_1\), every point not covered by
\[
z_1+K_{1/13}
\]
must violate at least one of its fourteen defining half-planes; the checker clips the facet polygon against every such possible violated inequality. It repeats this disjunctive decomposition successively for
\[
z_2,\ldots,z_6.
\]
After the sixth center, every branch polygon is empty on every facet.

All polygon vertices, line intersections, and comparisons are computed with exact rational arithmetic. Hence the computation is a finite exhaustive proof that there is no point
\[
x\in\partial K
\]
outside all six sets
\[
z_i+K_{1/13}.
\]
This establishes (1).

Since
\[
K_{1/13}\subset\operatorname{int}K,
\]
condition (1) implies (2). Together with (3) and the fact that
\[
z_i\in\partial K,
\]
the centrally symmetric boundary-cover criterion gives a blocking configuration consisting of
\[
K+2z_1,\ldots,K+2z_6.
\]
Therefore
\[
b(K)\le6.
\]

## Verification
The supplied `verify.py` uses only exact rational arithmetic.

It verifies the six boundary-center conditions, all fifteen pairwise non-overlap conditions, the fourteen inset half-spaces, and the coverage of all six square and eight triangular facets.

For each facet, the verifier records the number of surviving branch polygons after each successive center. In all fourteen cases the final count is exactly zero. The replay terminates with `VERIFY_OK`.

No random sampling, floating-point tolerance, or finite-grid inference is used.

## Relationship to prior work
Zong introduced blocking numbers of convex bodies and established the standard translate-intersection framework. The later open-problem literature highlighted blocking numbers as a continuing source of geometric questions and asked for further explicit results beyond the classical bodies whose values were already known.

A later treatment of blocking numbers gives the boundary-cover reformulation used above and records several three-dimensional exact or six-translate results, including the cross-polytope and other classical families. The inspected text does not state a six-blocker construction for the cuboctahedron.

The cuboctahedron is also a member of the natural cube--cross-polytope intersection family. Results for its ordinary illumination number do not imply the present bound: illumination and blocking are distinct invariants, and the standard comparison has the wrong implication direction for deriving a six-blocker configuration from a smaller illumination number.

Targeted searches for the regular cuboctahedron, rectified-cube language, cube--octahedron intersection language, six blocking translates, and blocking-number aliases did not locate the explicit configuration or the rational-clearance cover in (1).

## Limitations
The result is an upper bound:
\[
b(K)\le6.
\]
It does not prove the matching lower bound.

The explicit clearance
\[
\frac1{13}
\]
is a convenient certified value and is not claimed to be optimal.

The construction is for the regular cuboctahedron and its affine images. No assertion is made for the entire one-parameter cube--cross-polytope intersection family.

An older or differently indexed source may contain an equivalent cuboctahedral blocking construction; that remains the principal originality risk.

## References
1. C. Zong, *The Blocking Numbers of Convex Bodies*, Discrete & Computational Geometry 24 (2000), DOI: 10.1007/s004540010032.
2. *Open Problem Session*, Banach Center Publications 84 (2009), Problem 12.
3. Article on blocking numbers and the boundary-cover reformulation, DOI: 10.55016/ojs/cdm.v19i3.75983.
