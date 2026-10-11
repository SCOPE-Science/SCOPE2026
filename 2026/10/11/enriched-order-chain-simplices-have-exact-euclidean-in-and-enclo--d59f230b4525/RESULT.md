# Enriched-order chain simplices have exact Euclidean in- and enclosing radii
## Finding
Let
\[
P_n=\{1<2<\cdots<n\}
\]
be the \(n\)-element chain, and let
\[
\mathcal O^{(e)}(P_n)\subset\mathbb R^n
\]
be its enriched order polytope in the standard Euclidean realization.

Define
\[
N_m=\sqrt{\frac{4^{m+1}-1}{3}}
\qquad
(m\ge0).
\tag{1}
\]

Then \(\mathcal O^{(e)}(P_n)\) is the simplex with vertices
\[
u=(1,\ldots,1)
\tag{2}
\]
and
\[
v_k=-e_k+\sum_{j=k+1}^n e_j,
\qquad
1\le k\le n.
\tag{3}
\]

Its exact Euclidean inradius is
\[
\boxed{
r_n=
\frac{2^n}{
N_{n-1}+\displaystyle\sum_{k=1}^n2^{k-1}N_{n-k}
}.
}
\tag{4}
\]
Equivalently,
\[
\boxed{
r_n=
\frac{\sqrt3}{
2\sqrt{1-4^{-n}}
+
\displaystyle\sum_{j=1}^{n-1}\sqrt{1-4^{-j}}
}.
}
\tag{5}
\]

The incenter is unique. Writing
\[
c=(c_1,\ldots,c_n),
\]
its coordinates are
\[
\boxed{
c_{n-m}
=
1-\frac{r_n}{2^m}
\left(
N_m+
\sum_{t=0}^{m-1}2^{m-1-t}N_t
\right),
\quad
0\le m\le n-1.
}
\tag{6}
\]
The empty sum is \(0\). In particular,
\[
c_1=0.
\tag{7}
\]

The unique minimum enclosing Euclidean sphere has center
\[
\boxed{
q_n=
\left(
\frac12-2^{-1},
\frac12-2^{-2},
\ldots,
\frac12-2^{-n}
\right)
}
\tag{8}
\]
and squared radius
\[
\boxed{
R_n^2=
\frac n4+\frac43-2^{-n}-\frac13\,4^{-n}.
}
\tag{9}
\]
Every simplex vertex is a contact point.

As \(n\to\infty\),
\[
\boxed{
r_n\sim\frac{\sqrt3}{n},
\qquad
R_n\sim\frac{\sqrt n}{2},
\qquad
\frac{R_n}{r_n}
\sim
\frac{n^{3/2}}{2\sqrt3}.
}
\tag{10}
\]

For the same chain, the enriched chain polytope is the crosspolytope
\[
\operatorname{conv}\{\pm e_1,\ldots,\pm e_n\},
\]
whose Euclidean inradius and minimum-enclosing radius are respectively
\[
\frac1{\sqrt n}
\quad\text{and}\quad
1.
\tag{11}
\]
Thus the two enriched poset polytopes have the same Ehrhart polynomial under the published enriched transfer theory, but their canonical Euclidean aspect ratios have different growth orders.

## Assumptions and scope
The metric is the standard Euclidean metric in the coordinate realization used to define enriched order polytopes.

The statement holds for every integer
\[
n\ge1.
\]
For \(n=1\), the enriched order polytope is the interval \([-1,1]\), and the formulas give
\[
r_1=R_1=1.
\]

The minimum enclosing sphere is the smallest Euclidean ball containing the whole polytope. Since a ball is convex, it is enough to contain all simplex vertices.

No Euclidean invariance under the enriched transfer map or under arbitrary unimodular transformations is assumed.

## Proof
The 2020 geometry-classified source defines the enriched order polytope as the convex hull of functions
\[
f:P\to\{-1,0,1\}
\]
whose support is an order filter and for which a value \(-1\) can occur only at a minimal element of the support.

For a chain, every nonempty order filter is a suffix
\[
\{k,k+1,\ldots,n\}.
\]
Hence the defining point set consists of \(0\) and, for each \(k\),
\[
u_k=e_k+\cdots+e_n,
\qquad
v_k=-e_k+e_{k+1}+\cdots+e_n.
\tag{12}
\]
For \(k\ge2\),
\[
u_k=\frac{u_{k-1}+v_{k-1}}2,
\tag{13}
\]
and
\[
0=\frac{u_n+v_n}{2}.
\tag{14}
\]
Therefore
\[
\mathcal O^{(e)}(P_n)
=
\operatorname{conv}\{u_1,v_1,\ldots,v_n\}.
\tag{15}
\]
The \(n\) vectors \(v_k-u_1\) form a triangular matrix with diagonal entries \(-2\), so these \(n+1\) points are affinely independent. This proves (2)--(3).

For
\[
1\le k\le n,
\]
define
\[
a_k
=
2^{n-k}e_k
-
\sum_{j=k+1}^n2^{n-j}e_j,
\tag{16}
\]
and define
\[
b
=
-\sum_{j=1}^n2^{n-j}e_j.
\tag{17}
\]
Direct substitution into the vertices shows that
\[
a_k\cdot x\le1
\tag{18}
\]
is the facet opposite \(v_k\), while
\[
b\cdot x\le1
\tag{19}
\]
is the facet opposite \(u_1\). Hence these are the complete \(n+1\) facets of the simplex.

Their norms are
\[
\|a_k\|=N_{n-k},
\qquad
\|b\|=N_{n-1},
\tag{20}
\]
because
\[
4^{n-k}+\sum_{r=0}^{n-k-1}4^r
=
\frac{4^{n-k+1}-1}{3}.
\]

The facet normals satisfy the positive dependence
\[
b+\sum_{k=1}^n2^{k-1}a_k=0.
\tag{21}
\]
If \(c\) is the incenter and \(r\) the inradius, tangency to every facet gives
\[
a_k\cdot c=1-rN_{n-k},
\qquad
b\cdot c=1-rN_{n-1}.
\tag{22}
\]
Multiplying (22) by the positive coefficients in (21) and summing eliminates \(c\). Since
\[
1+\sum_{k=1}^n2^{k-1}=2^n,
\]
we obtain (4). A simplex has a unique incenter, so this radius is globally maximal.

Dividing the denominator of (4) by \(2^n\) and using
\[
\frac{N_m}{2^{m+1}}
=
\frac1{\sqrt3}\sqrt{1-4^{-(m+1)}}
\tag{23}
\]
gives (5).

Solving the equations \(a_k\cdot c=1-r_nN_{n-k}\) backward from \(k=n\) gives (6). The case \(m=n-1\), together with (4), simplifies to \(c_1=0\).

We now compute the minimum enclosing sphere.

Let
\[
q_j=\frac12-2^{-j},
\qquad
1\le j\le n.
\tag{24}
\]
The first two vertices \(u_1\) and \(v_1\) differ only in coordinate \(1\), so their perpendicular bisector forces \(q_1=0\). For \(2\le k\le n\),
\[
v_k-v_{k-1}=e_{k-1}-2e_k
\tag{25}
\]
and
\[
\|v_k\|^2-\|v_{k-1}\|^2=-1.
\tag{26}
\]
The perpendicular-bisector equation therefore reads
\[
2(q_{k-1}-2q_k)=-1,
\]
or
\[
q_k=\frac12q_{k-1}+\frac14.
\tag{27}
\]
Starting at \(q_1=0\), this gives exactly (24). Thus all \(n+1\) simplex vertices lie on one sphere centered at \(q_n\).

Using the vertex
\[
v_n=-e_n,
\]
the squared radius is
\[
\|q_n+e_n\|^2
=
\|q_n\|^2+2q_n(n)+1.
\]
Now
\[
\sum_{j=1}^n
\left(\frac12-2^{-j}\right)^2
=
\frac n4-\frac23+2^{-n}-\frac13\,4^{-n},
\]
and (9) follows.

The coordinates in (24) satisfy
\[
0=q_1<q_2<\cdots<q_n<1.
\]
Hence \(q_n\) belongs to the ordinary order polytope of the chain, and the source explicitly includes the ordinary order polytope in the enriched order polytope. Thus
\[
q_n\in\mathcal O^{(e)}(P_n).
\tag{28}
\]
Write \(q_n\) as a convex combination of simplex vertices. Since all those vertices have common distance \(R_n\) from \(q_n\), for any other candidate center \(y\) the weighted parallel-axis identity gives
\[
\sum_i\lambda_i\|v_i-y\|^2
=
R_n^2+\|y-q_n\|^2.
\tag{29}
\]
Therefore some vertex has distance at least the square root of the right side. The sphere centered at \(q_n\) is consequently the unique minimum enclosing sphere.

Finally, (5) has \(n+1+O(1)\) in its denominator after division by \(\sqrt3\), so
\[
r_n\sim\frac{\sqrt3}{n}.
\]
Equation (9) gives
\[
R_n\sim\frac{\sqrt n}{2},
\]
and (10) follows.

For the enriched chain polytope of a chain, the only nonempty antichains are singletons. Its defining signed antichain vectors are therefore exactly
\[
\pm e_1,\ldots,\pm e_n,
\]
which proves (11).

## Verification
The arbitrary-\(n\) proof is symbolic.

The source-dependent facts were inspected in the primary full text: the signed-filter definition of the enriched order polytope, the inclusion of the ordinary order polytope, the enriched transfer theorem, and the complete facet theorem. The earlier introducing paper was inspected at its enriched-order construction and facet section and contains no inradius or circumradius statement.

The accompanying `verify.py` checks
\[
1\le n\le12
\]
with exact symbolic arithmetic. It verifies the simplex vertex reduction from the signed-filter definition, every facet incidence, the positive normal dependence, the exact incenter equations and both inradius forms, the circumcenter recurrence, the radius formula, and the order-polytope membership inequalities for the enclosing center. These finite checks are corroborative only.

## Relationship to prior work
Ohsugi and Tsuchiya introduced enriched order polytopes, proved reflexivity and Ehrhart equivalence with enriched chain polytopes, and derived their facet representations. Their inspected full text contains no inradius, circumradius, sphere, or Chebyshev-center theorem.

Okada and Tsuchiya later gave an enriched transfer map, explicit unimodular triangulations, and a geometric treatment of the defining inequalities. That paper has primary MSC \(52B12\) and is the geometry-classified source used to assign this result. It does not state the Euclidean radius formulas above.

The chain specialization is especially revealing because the enriched chain polytope becomes the standard crosspolytope while the enriched order polytope becomes the simplex (15). The published transfer map proves equal Ehrhart polynomials but is piecewise linear rather than Euclidean-isometric. Equations (4) and (9) quantify the resulting metric separation:
\[
\frac{R_n}{r_n}
\sim
\frac{n^{3/2}}{2\sqrt3},
\]
whereas the crosspolytope has radius ratio \(\sqrt n\).

Targeted searches under “enriched order polytope”, “inradius”, “circumradius”, “minimum enclosing sphere”, “chain poset”, “enriched Hibi polytope”, and “enriched order simplex” did not locate a theorem implying the stated formulas.

## Limitations
The theorem concerns only the chain-poset specialization of enriched order polytopes.

It uses the canonical coordinate realization and is not invariant under arbitrary unimodular transformations.

No formula is asserted here for inradii or minimum enclosing spheres of enriched order polytopes of arbitrary posets.

The facet computation is elementary once the chain specialization is isolated. The mathematical value lies in the complete exact metric profile of a natural reflexive simplex family and in the quantified Euclidean separation from its Ehrhart-equivalent enriched chain partner.

## References
1. Hidefumi Ohsugi and Akiyoshi Tsuchiya, *Enriched order polytopes and Enriched Hibi rings*, arXiv:1903.00909, first public version 2019-03-03; European Journal of Mathematics 7 (2021), 48--68, DOI 10.1007/s40879-020-00403-2.
2. Soichi Okada and Akiyoshi Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271, first public version 2020-03-27; Annals of Combinatorics 28 (2024), 257--282, DOI 10.1007/s00026-023-00679-7.
