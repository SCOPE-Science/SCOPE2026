# Good symmetric Newton polytopes have an exact one-dimensional minimum-sphere formula
## Finding
Let
\[
F(x_1,\ldots,x_m)
\]
be a good symmetric polynomial in the sense of Nguyen--Nguyen--Dang--Do. Its defining data include endpoint partitions
\[
\alpha=(\alpha_1,\ldots,\alpha_m)
\le
\beta=(\beta_1,\ldots,\beta_m).
\tag{1}
\]
For
\[
0\le i\le m,
\]
put
\[
\lambda^{(i)}
=
(\beta_1,\ldots,\beta_i,\alpha_{i+1},\ldots,\alpha_m),
\tag{2}
\]
with
\[
\lambda^{(0)}=\alpha,
\qquad
\lambda^{(m)}=\beta.
\]

The source proves that the Newton polytope
\[
P=\operatorname{Newton}(F)
\tag{3}
\]
can be written as
\[
P
=
\operatorname{conv}
\left(
\bigcup_{i=0}^{m}
\operatorname{Newton}(s_{\lambda^{(i)}})
\right),
\tag{4}
\]
and that
\[
\operatorname{Newton}(s_\lambda)
=
\operatorname{conv}(S_m\lambda).
\tag{5}
\]
Thus the possibly large exponent support reduces, for convex-hull purposes, to at most \(m+1\) permutation orbits.

Define
\[
h_j=\frac{\alpha_j+\beta_j}{2}
\qquad
(1\le j\le m).
\tag{6}
\]
Because both endpoint vectors are partitions,
\[
h_1\ge h_2\ge\cdots\ge h_m.
\tag{7}
\]
Define the one-variable function
\[
\boxed{
\Phi(c)
=
\sum_{j=1}^m
\max\!\left\{
(\alpha_j-c)^2,\,
(\beta_j-c)^2
\right\}.
}
\tag{8}
\]

Then the unique minimum enclosing Euclidean ball of \(P\) has center
\[
\boxed{
c_*\mathbf1,
}
\tag{9}
\]
where \(c_*\) is the unique minimizer of \(\Phi\), and radius
\[
\boxed{
R_*=\sqrt{\Phi(c_*)}.
}
\tag{10}
\]

The minimizer is completely explicit by a finite scan. Put
\[
h_0=+\infty,
\qquad
h_{m+1}=-\infty,
\tag{11}
\]
and
\[
c_i
=
\frac1m
\left(
\sum_{j=1}^i\beta_j
+
\sum_{j=i+1}^m\alpha_j
\right)
\qquad
(0\le i\le m).
\tag{12}
\]
Then \(c_*\) is characterized by one of the following two alternatives:
\[
h_{i+1}\le c_i\le h_i,
\qquad
c_*=c_i,
\tag{13}
\]
for some \(0\le i\le m\), or
\[
c_{i-1}\le h_i\le c_i,
\qquad
c_*=h_i,
\tag{14}
\]
for some \(1\le i\le m\).
When equalities create several valid descriptions, they all give the same number \(c_*\).

The contact points are exactly the permutations of the active source layers:
\[
\boxed{
\bigcup_{\substack{0\le i\le m\\
\|\lambda^{(i)}-c_*\mathbf1\|=R_*}}
S_m\lambda^{(i)}.
}
\tag{15}
\]

Therefore the Euclidean minimum enclosing sphere of every good symmetric Newton polytope depends only on its two endpoint partitions and is computable by an \(O(m)\) scan.

For the source example
\[
F=G_{2,(3,1,0)},
\]
the endpoint partitions are
\[
\alpha=(3,1,0),
\qquad
\beta=(3,3,3).
\]
The scan gives
\[
\boxed{
c_*=2,
\qquad
R_*=\sqrt6.
}
\tag{16}
\]
The contacts are precisely the permutations of
\[
(3,1,0)
\quad\text{and}\quad
(3,3,0),
\]
whereas
\[
(3,3,3)
\]
is strictly inside the minimum sphere.

## Assumptions and scope
The metric is the standard Euclidean metric in the exponent-coordinate space
\[
\mathbb R^m.
\]

The theorem uses the source definition of a good symmetric polynomial and, critically, the source reduction (4) to the distinguished partitions (2). It does not assert the same formula for an arbitrary symmetric polynomial whose degree layers fail the good-polynomial hypotheses.

Repeated coordinates or repeated layers are allowed. They merely collapse some permutation orbits or create redundant descriptions in the scan.

The result concerns the minimum enclosing Euclidean ball. It does not determine the Euclidean inradius, John ellipsoid, lattice width, or Ehrhart invariants.

## Proof
We first prove that the center must lie on the diagonal.

For every compact set in Euclidean space, the minimum enclosing ball has a unique center. Indeed, if distinct centers \(u,v\) both enclosed a set with radius \(R\), then for every point \(x\),
\[
\left\|x-\frac{u+v}{2}\right\|^2
=
\frac{\|x-u\|^2+\|x-v\|^2}{2}
-
\frac{\|u-v\|^2}{4}
<
R^2,
\]
contradicting minimality.

The polytope \(P\) is invariant under every coordinate permutation. Uniqueness therefore forces its minimum-enclosing center to be fixed by \(S_m\), hence to have the form
\[
c\mathbf1.
\tag{17}
\]

For such a center, all points in one permutation orbit have the same squared distance. By (2), define
\[
R_i(c)^2
=
\|\lambda^{(i)}-c\mathbf1\|^2
=
\sum_{j=1}^i(\beta_j-c)^2
+
\sum_{j=i+1}^m(\alpha_j-c)^2.
\tag{18}
\]
Equations (4)--(5) imply
\[
\max_{x\in P}\|x-c\mathbf1\|^2
=
\max_{0\le i\le m}R_i(c)^2.
\tag{19}
\]

Now compare consecutive layers:
\[
\begin{aligned}
R_i(c)^2-R_{i-1}(c)^2
&=
(\beta_i-c)^2-(\alpha_i-c)^2\\
&=
(\beta_i-\alpha_i)
(\alpha_i+\beta_i-2c)\\
&=
2(\beta_i-\alpha_i)(h_i-c).
\end{aligned}
\tag{20}
\]
Since
\[
\beta_i-\alpha_i\ge0
\]
and the \(h_i\) are weakly decreasing, the sequence \(R_i(c)^2\) first weakly increases and then weakly decreases. Hence the maximizing layer chooses \(\beta_j\) exactly where that endpoint is at least as far from \(c\) as \(\alpha_j\). Therefore
\[
\max_iR_i(c)^2
=
\sum_{j=1}^m
\max\!\left\{
(\alpha_j-c)^2,
(\beta_j-c)^2
\right\}
=
\Phi(c).
\tag{21}
\]

Each summand in (8) is the maximum of two quadratics with the same positive quadratic coefficient. More explicitly,
\[
\max\{(\alpha_j-c)^2,(\beta_j-c)^2\}
=
c^2+
\max\{\alpha_j^2-2\alpha_jc,\beta_j^2-2\beta_jc\}.
\]
Thus
\[
\Phi(c)-mc^2
\]
is convex, so \(\Phi\) is strongly convex and has one unique minimizer \(c_*\). Equations (17), (19), and (21) prove (9)--(10).

It remains to justify the scan.

On the interval
\[
h_{i+1}\le c\le h_i,
\tag{22}
\]
the farther endpoint in coordinate \(j\) is \(\beta_j\) for \(j\le i\) and \(\alpha_j\) for \(j>i\). Hence
\[
\Phi(c)=R_i(c)^2
\]
throughout this interval. Its unconstrained minimizer is
\[
c_i
=
\frac1m
\left(
\sum_{j=1}^i\beta_j
+
\sum_{j=i+1}^m\alpha_j
\right),
\]
which proves (13) whenever \(c_i\) lies in its own interval.

The sequence \(c_i\) is weakly increasing, while the boundary sequence \(h_i\) is weakly decreasing. If no unconstrained minimizer lies in its interval, strong convexity forces the minimum to occur at a boundary \(h_i\). The one-sided derivatives there have opposite signs exactly when
\[
c_{i-1}\le h_i\le c_i,
\]
which is (14).

For the contact statement, every source orbit in (4) lies in the radius-\(R_*\) ball. Equation (19) shows which source orbit points lie on its boundary. Since a Euclidean ball is strictly convex, no nontrivial convex combination of distinct points in the ball can lie on its boundary. Hence there are no additional contacts, proving (15).

For the source example, the distinguished layers are
\[
(3,1,0),
\quad
(3,3,0),
\quad
(3,3,3),
\]
up to a repeated initial layer. Their midpoint thresholds are
\[
3,\quad2,\quad\frac32.
\]
Condition (14) gives
\[
c_*=2.
\]
The three squared layer radii are
\[
6,\quad6,\quad3,
\]
which proves (16) and the stated contact classification.

## Verification
The source-dependent structural statement was checked in the primary full text. The proof of its main theorem shows
\[
\operatorname{Newton}(F)
=
\operatorname{conv}
\left(
\bigcup_{i=0}^{m}
\operatorname{Newton}(s_{\lambda^{(i)}})
\right)
\]
for the endpoint-derived partitions (2), and recalls that each Schur Newton polytope is the convex hull of the coordinate-permutation orbit of its partition.

The source also gives the inflated symmetric Grothendieck example used in (16), with endpoint partitions
\[
(3,1,0)
\quad\text{and}\quad
(3,3,3),
\]
and identifies the relevant vertex orbits.

The accompanying `verify.py` uses exact rational arithmetic for the scan and independently expands all distinct coordinate permutations of every source layer in deterministic examples. It then solves the full minimum-enclosing-ball problem numerically in the ambient space and compares the center and radius with the closed formula. The finite computation is corroborative only; the proof above covers all good symmetric polynomials.

## Relationship to prior work
Nguyen, Nguyen, Dang, and Do introduce good symmetric polynomials and prove that their Newton polytopes have saturated Newton polytope and the integer decomposition property. Their proof contains the crucial reduction to the endpoint-derived permutation-orbit layers, but it does not study Euclidean enclosing balls.

Bayer, Goeckner, Hong, McAllister, Olsen, Pinckney, Vega, and Yip study Schur and inflated symmetric Grothendieck Newton polytopes, focusing on saturation, integer decomposition, reflexivity, Gorenstein properties, and Ehrhart theory. Their full text likewise contains no Euclidean radius or minimum-enclosing-sphere theorem.

The fixed-degree case of a single Schur polynomial is only one permutation orbit. The present theorem is different: good symmetric polynomials can be inhomogeneous, so their Newton polytopes contain several trace layers. The minimum sphere must balance those layers, and its center need not equal the mean of either endpoint partition.

Generic minimum-enclosing-ball theory gives uniqueness of the center but does not exploit the source's ordered orbit structure. The object-specific reduction (20)--(21) turns a potentially very large exponent set into the scalar function (8), and then into the finite scan (13)--(14).

Targeted searches under “good symmetric polynomial”, “inflated symmetric Grothendieck”, “Newton polytope”, “minimum enclosing ball”, “circumradius”, “Chebyshev center”, and “permutation orbit layers” did not locate a statement implying (8)--(15).

## Limitations
The result depends on the source's good-polynomial layer structure. It does not provide a minimum-sphere formula for arbitrary unions of Schur supports.

The scan computes the enclosing sphere exactly, but it does not by itself describe the full face lattice or Euclidean inradius of the Newton polytope.

A broader theorem about minimum enclosing balls of nested or layered permutation orbitopes could subsume the argument under different terminology. No such dominating statement was located in the targeted comparisons.

The reciprocal arithmetic and lattice properties of the source family are not used in the Euclidean proof except to identify the relevant orbit layers.

## References
1. Duc-Khanh Nguyen, Nguyen Thi Ngoc Giao, Dang Tuan Hiep, and Do Le Hai Thuy, *Newton polytope of good symmetric polynomials*, arXiv:2205.03903, first public version 2022-05-08; *Comptes Rendus Mathématique* 361 (2023), 767--775, DOI 10.5802/crmath.430.
2. Margaret Bayer, Bennet Goeckner, Su Ji Hong, Tyrrell McAllister, McCabe Olsen, Casey Pinckney, Julianne Vega, and Martha Yip, *Lattice polytopes from Schur and symmetric Grothendieck polynomials*, arXiv:2005.09628, first public version 2020-05-19; *Electronic Journal of Combinatorics* 28 (2021), P2.45, DOI 10.37236/9621.
