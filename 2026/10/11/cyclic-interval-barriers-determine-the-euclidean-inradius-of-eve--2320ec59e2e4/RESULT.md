# Cyclic interval barriers determine the Euclidean inradius of every chainlink polytope
## Finding
Let
\[
s\ge2,
\]
let
\[
\bar a=(a_1,\ldots,a_s)
\]
be a composition with positive integer parts, and let
\[
l\in\mathbb Z_{\ge0},
\qquad
2l\le\min_i a_i.
\]
The chainlink polytope introduced by Kantarcı Oğuz, Özel, and Ravichandran is
\[
\mathrm{CL}(\bar a,l)
=
\left\{
x\in\mathbb R^s:
0\le x_i\le a_i,\quad
x_i-x_{i+1}\le a_i-l
\ \text{for all }i
\right\},
\tag{1}
\]
where indices are cyclic.

For a cyclic interval
\[
I(i,m)=\{i,i+1,\ldots,i+m-1\},
\qquad
1\le m\le s,
\tag{2}
\]
define
\[
R_{i,m}
=
\frac{
\displaystyle\sum_{q=0}^{m-1}a_{i+q}-(m-1)l
}{
2+(m-1)\sqrt2
}.
\tag{3}
\]
Also define the full-cycle barrier
\[
R_{\mathrm{cyc}}
=
\frac{
\displaystyle\sum_{i=1}^s a_i-sl
}{
s\sqrt2
}.
\tag{4}
\]

Then the exact Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathrm{CL}(\bar a,l)\bigr)
=
\min\left(
R_{\mathrm{cyc}},
\min_{\substack{1\le i\le s\\1\le m\le s}}R_{i,m}
\right).
}
\tag{5}
\]

Writing the value in (5) as \(r\), the complete incenter set is
\[
\boxed{
\operatorname{Cent}\bigl(\mathrm{CL}(\bar a,l)\bigr)
=
\left\{
c:
r\le c_i\le a_i-r,\quad
c_i-c_{i+1}\le a_i-l-r\sqrt2
\ \text{for all }i
\right\}.
}
\tag{6}
\]

The minimizing barriers also certify tangencies. If a cyclic interval
\[
I(i,m)=\{i,\ldots,j\}
\]
attains (5), then every incenter is tangent to
\[
x_i=0,
\qquad
x_j=a_j,
\]
and to every chainlink facet
\[
x_k-x_{k+1}=a_k-l
\]
along the interval from \(i\) to \(j\). If \(R_{\mathrm{cyc}}\) attains (5), every chainlink facet is tangent.

For the homogeneous family
\[
\bar a=(a,\ldots,a),
\]
formula (5) collapses to
\[
\boxed{
r_{\mathrm{in}}
=
\min\left\{
\frac a2,
\frac{a-l}{\sqrt2}
\right\}.
}
\tag{7}
\]
If
\[
\frac a2<\frac{a-l}{\sqrt2},
\]
the incenter is unique:
\[
\boxed{
c=\frac a2\mathbf1.
}
\tag{8}
\]
If
\[
\frac{a-l}{\sqrt2}<\frac a2,
\]
then
\[
\boxed{
\operatorname{Cent}
=
\left\{
t\mathbf1:
r\le t\le a-r
\right\}.
}
\tag{9}
\]
Thus the homogeneous family has a sharp transition from a unique box-controlled center to a one-dimensional link-controlled center set.

## Assumptions and scope
The metric is the standard Euclidean metric in the source realization
\[
\mathbb R^s.
\]

The parameter restriction
\[
2l\le\min_i a_i
\]
is the natural regime emphasized in the source for the chainlink-poset and complementary-section theory. The proof of (5) uses only the defining inequalities and remains valid whenever the displayed polytope is full-dimensional and the barrier expressions are interpreted for that realization.

The source parameters are integral. The metric proof itself works verbatim for positive real \(a_i\) and real \(l\) in the same nondegenerate regime.

## Proof
A Euclidean ball of radius \(\rho\), centered at
\[
x=(x_1,\ldots,x_s),
\]
is contained in (1) exactly when its distance to every defining supporting hyperplane is at least \(\rho\).

The coordinate normals have norm \(1\), while the normal
\[
e_i-e_{i+1}
\]
of a chainlink inequality has norm
\[
\sqrt2.
\]
Therefore radius-\(\rho\) feasibility is equivalent to
\[
\rho\le x_i\le a_i-\rho,
\tag{10}
\]
\[
x_i-x_{i+1}
\le
a_i-l-\rho\sqrt2
\qquad
(1\le i\le s).
\tag{11}
\]

Put
\[
y_i=x_i-\rho,
\]
and abbreviate
\[
U_i=a_i-2\rho,
\qquad
A_i=a_i-l-\rho\sqrt2.
\tag{12}
\]
Then (10)--(11) become
\[
0\le y_i\le U_i,
\tag{13}
\]
\[
y_i-y_{i+1}\le A_i.
\tag{14}
\]

We use the elementary difference-constraints lemma: a finite system
\[
z_v-z_u\le w(u,v)
\]
is feasible if and only if every directed cycle in its constraint graph has nonnegative total weight.

For completeness, necessity follows by summing the inequalities around a directed cycle. Conversely, if there is no negative directed cycle, adjoin a source with zero-weight edges to every vertex and let \(z_v\) be the shortest-path distance from the source. Shortest-path triangle inequalities give every constraint.

Apply this lemma to vertices
\[
0,1,\ldots,s.
\]
The inequalities (13)--(14) are represented by edges
\[
0\longrightarrow i
\quad\text{of weight }U_i,
\]
\[
i\longrightarrow0
\quad\text{of weight }0,
\]
and
\[
i+1\longrightarrow i
\quad\text{of weight }A_i,
\tag{15}
\]
with cyclic indices.

The simple directed cycles of this graph have only two forms.

First, a cycle can pass through \(0\). It leaves \(0\) at some endpoint \(j\), follows the directed ring backward through a cyclic interval
\[
I(i,m)=\{i,\ldots,j\},
\]
and returns from \(i\) to \(0\). Its weight is
\[
U_j+\sum_{k=i}^{j-1}A_k.
\]
Using (12), this is
\[
\sum_{k\in I(i,m)}a_k
-
(m-1)l
-
\rho\bigl(2+(m-1)\sqrt2\bigr).
\tag{16}
\]
Nonnegativity of (16) is exactly
\[
\rho\le R_{i,m}.
\tag{17}
\]

Second, the cycle can be the full directed ring. Its weight is
\[
\sum_{i=1}^s A_i
=
\sum_i a_i-sl-s\rho\sqrt2.
\tag{18}
\]
Its nonnegativity is exactly
\[
\rho\le R_{\mathrm{cyc}}.
\tag{19}
\]

There are no other simple directed cycles: outside vertex \(0\), every ring vertex can continue only to its predecessor or return to \(0\).

Thus a radius \(\rho\) is feasible if and only if it satisfies every bound in (17) and (19). The largest feasible value is precisely (5).

At the optimal value \(r\), conditions (10)--(11) are necessary and sufficient for a center. This proves (6).

The tangency statements follow from a zero-weight minimizing cycle. Summing the corresponding shifted facet inequalities around that cycle gives total slack zero. Since every individual slack is nonnegative, each inequality on the cycle is an equality. For an interval cycle these are the lower facet at its start, the upper facet at its end, and all intervening chainlink facets. For the full ring, every chainlink inequality is an equality.

Now suppose
\[
a_1=\cdots=a_s=a.
\]
For an interval of length \(m\), put \(q=m-1\). Then
\[
R_{i,m}
=
\frac{a+q(a-l)}{2+q\sqrt2}.
\tag{20}
\]
As a function of \(q\ge0\), this linear-fractional expression is monotone; its two endpoint comparison values are
\[
\frac a2
\quad\text{and}\quad
\frac{a-l}{\sqrt2}.
\]
The full-cycle barrier equals the second value. Hence (7).

In the box-limited phase, (6) forces
\[
c_i=a/2
\]
for every coordinate, proving (8). In the link-limited phase, the shifted chainlink inequalities in (6) become
\[
c_i\le c_{i+1}
\]
cyclically, so all coordinates are equal. The remaining box clearances give exactly (9).

## Verification
The proof above is exact for arbitrary dimension and all parameters in the stated regime.

The source-dependent premise was checked in the primary full text: chainlink polytopes are introduced with the coordinate and cyclic-difference inequalities in (1), and the paper develops their integrality, sections, poset models, Ehrhart quasipolynomials, and rank-symmetry properties. Targeted full-text checks found no Euclidean inradius, radius, sphere, or Chebyshev-center theorem.

The accompanying `verify.py` performs an independent finite replay. For deterministic compositions in dimensions two through four, it solves the full \((s+1)\)-variable Chebyshev linear program by generic active-set enumeration and Gaussian elimination, without using the cycle formula in the optimizer. It compares the resulting optimum with (5). It also checks the homogeneous phase formulas in dimensions up to twelve.

The finite replay is corroborative only; the difference-constraints proof establishes (5)--(9) in all dimensions.

## Relationship to prior work
Kantarcı Oğuz, Özel, and Ravichandran introduced chainlink polytopes in 2022 to build polyhedral models for circular-fence and chainlink-poset rank symmetry. Their paper studies integrality, half-integral sections, Ehrhart quasipolynomial symmetry, volume symmetry, and unimodality phenomena.

The present result uses the same defining inequalities but asks a different realization-sensitive question: the largest Euclidean ball. Normalizing the cyclic-difference facets introduces the factor
\[
\sqrt2,
\]
and the Chebyshev problem becomes a cyclic difference-constraints system.

Generic difference-constraints theory supplies the feasibility criterion in terms of negative directed cycles. The object-specific content is that the chainlink constraint graph has only interval cycles and one full ring, which turns the optimization into the explicit finite barrier family (3)--(4). Each minimizing interval simultaneously identifies a forced tangent chain of facets.

Targeted searches under “chainlink polytope”, “inradius”, “Chebyshev center”, “insphere”, “largest inscribed ball”, and broader difference-constraints terminology did not locate a statement implying (5)--(9).

## Limitations
The theorem concerns the standard Euclidean realization of chainlink polytopes.

It does not determine minimum enclosing spheres, John or Löwner ellipsoids, or Euclidean radii of the source's fixed-sum sections.

The barrier family can contain many ties, so (6) is a complete center description but not a closed combinatorial classification of the dimension of the incenter set for every composition.

Generic shortest-path theory is an essential proof tool. A broader published theorem on Chebyshev centers of boxes with cyclic difference constraints could subsume the calculation under different terminology; no such dominating statement was located in the targeted comparison.

## References
1. Ezgi Kantarcı Oğuz, Cem Yalım Özel, and Mohan Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382, first public version 2022-11-15; *Annals of Combinatorics* 28 (2024), 1141--1166, DOI 10.1007/s00026-023-00683-x.
