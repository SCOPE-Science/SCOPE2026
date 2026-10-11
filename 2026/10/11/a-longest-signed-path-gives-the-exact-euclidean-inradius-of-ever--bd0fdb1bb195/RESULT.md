# A longest signed path gives the exact Euclidean inradius of every signed order polytope
## Finding
Let \(P\) be a signed poset on \([n]\). Beck and Hlavacek define its signed order polytope by
\[
\mathcal O_P
=
\left\{x\in[-1,1]^n:\langle\alpha,x\rangle\ge0\ \text{for every }\alpha\in P\right\}.
\tag{1}
\]
Let
\[
\operatorname{minrep}(P)
\]
be Reiner's unique minimal representation of \(P\). The source proves that an irredundant facet description is
\[
\langle\alpha,x\rangle\ge0
\quad
(\alpha\in\operatorname{minrep}(P)),
\tag{2}
\]
together with
\[
x_i\le1
\quad
(i\in\operatorname{pmax}(P))
\tag{3}
\]
and
\[
x_i\ge-1
\quad
(i\in\operatorname{nmax}(P)).
\tag{4}
\]

We convert this facet system into a weighted acyclic graph.

The vertices of \(D(P)\) are
\[
\{-n,\ldots,-1,0,1,\ldots,n\}.
\]
For a literal \(\sigma i\), where \(\sigma\in\{\pm1\}\), write
\[
z_{\sigma i}=\sigma x_i,
\qquad
z_0=0.
\tag{5}
\]

For a unit root
\[
\sigma e_i\in\operatorname{minrep}(P),
\]
put the two arcs
\[
-\sigma i\longrightarrow0,
\qquad
0\longrightarrow\sigma i,
\tag{6}
\]
each of weight \(1\).

For a two-coordinate root
\[
\alpha=\sigma_i e_i+\sigma_j e_j
\in\operatorname{minrep}(P),
\]
put the two arcs
\[
-\sigma_jj\longrightarrow\sigma_ii,
\qquad
-\sigma_ii\longrightarrow\sigma_jj,
\tag{7}
\]
each of weight \(\sqrt2\).

These are precisely generating relations of the Fischer representation of the signed poset, restricted to the minimal representation. Hence \(D(P)\) is acyclic. Moreover every arc
\[
u\longrightarrow v
\]
is paired with
\[
-v\longrightarrow-u
\]
of the same weight.

A nonzero vertex is called a **source** if its indegree is zero and a **sink** if its outdegree is zero. Define
\[
H(P)
=
\max_{\gamma}W(\gamma),
\tag{8}
\]
where \(\gamma\) ranges over all directed paths from a nonzero source to a nonzero sink, and \(W(\gamma)\) is the sum of its arc weights. A length-zero path is allowed, so \(H(P)=0\) for the empty signed poset.

Then
\[
\boxed{
 r_{\mathrm{in}}(\mathcal O_P)
 =
 \frac{2}{2+H(P)}.
}
\tag{9}
\]

This is an exact longest-path formula for every signed order polytope.

There is also a canonical incenter. For a nonzero literal \(v\), let
\[
d(v)
=
\max\{W(\gamma):\gamma\text{ is a directed path from a nonzero source to }v\}.
\tag{10}
\]
Every nonzero vertex is reachable from a nonzero source. If
\[
r=\frac{2}{2+H(P)},
\]
then
\[
\boxed{
 c_i^*
 =
 \frac r2\bigl(d(i)-d(-i)\bigr)
 \qquad(1\le i\le n)
}
\tag{11}
\]
is an incenter.

The complete incenter set is
\[
\boxed{
\begin{aligned}
\operatorname{Cent}(\mathcal O_P)=\{c\in\mathbb R^n:\;&
\langle\alpha,c\rangle\ge r\|\alpha\|_2
&&\text{for every }\alpha\in\operatorname{minrep}(P),\\
&c_i\le1-r
&&\text{for }i\in\operatorname{pmax}(P),\\
&c_i\ge-1+r
&&\text{for }i\in\operatorname{nmax}(P)
\}.
\end{aligned}
}
\tag{12}
\]

Every maximum-weight source-to-sink path is also a tangency certificate: at every incenter, all signed-order facets represented along that path and the two terminal box facets are tangent to the insphere.

If the minimal representation contains no unit roots, every arc has weight \(\sqrt2\). Therefore, if \(h(P)\) is the largest number of arcs in a source-to-sink path,
\[
\boxed{
 r_{\mathrm{in}}(\mathcal O_P)
 =
 \frac{2}{2+h(P)\sqrt2}.
}
\tag{13}
\]

## Assumptions and scope
The metric is the standard Euclidean metric in \(\mathbb R^n\).

The theorem uses the source's irredundant facet description, not the generally redundant system containing every root in \(P\). This matters metrically: a redundant root hyperplane is not a supporting facet and must not be treated as an independent distance constraint.

A literal \(+i\) is a sink of \(D(P)\) exactly when every root adjacent to coordinate \(i\) has positive \(e_i\)-coefficient, which is precisely
\[
i\in\operatorname{pmax}(P).
\]
Similarly, \(-i\) is a sink exactly when
\[
i\in\operatorname{nmax}(P).
\]
The antipode sends sinks to sources.

The auxiliary vertex \(0\) has no box constraint. If no unit root occurs it is isolated and plays no role.

## Proof
A ball of radius \(\rho\) centered at \(c\) lies in \(\mathcal O_P\) exactly when its center has normalized clearance at least \(\rho\) from every facet in (2)--(4).

For a unit root \(\alpha=\sigma e_i\),
\[
\|\alpha\|_2=1.
\]
The shifted facet inequality is
\[
\sigma c_i\ge\rho.
\tag{14}
\]
In the literal variables (5), each of the two arcs in (6) says exactly (14):
\[
z_0-z_{-\sigma i}\ge\rho,
\qquad
z_{\sigma i}-z_0\ge\rho.
\tag{15}
\]
They are the same physical facet written in the two antipodal literal coordinates.

For a two-coordinate root
\[
\alpha=\sigma_i e_i+\sigma_j e_j,
\]
we have
\[
\|\alpha\|_2=\sqrt2.
\]
For either arc in (7), the literal difference equals the same root functional:
\[
z_{\sigma_ii}-z_{-\sigma_jj}
=
\sigma_i c_i+\sigma_jc_j
=
\langle\alpha,c\rangle.
\]
Thus both paired arc inequalities are
\[
z_v-z_u\ge\rho\sqrt2.
\tag{16}
\]

For a sink \(+i\), the source facet is
\[
c_i\le1,
\]
so the shifted inequality is
\[
z_i\le1-\rho.
\tag{17}
\]
Its antipodal source \(-i\) satisfies the equivalent lower bound
\[
z_{-i}\ge-1+\rho.
\tag{18}
\]
The same statement with signs reversed holds for a sink \(-i\).

Therefore the inball problem is equivalent to finding an **antisymmetric potential**
\[
z_{-v}=-z_v,
\qquad
z_0=0,
\tag{19}
\]
which satisfies
\[
z_v-z_u\ge\rho w(u,v)
\tag{20}
\]
for every arc, together with
\[
z_a\ge-1+\rho
\tag{21}
\]
for every nonzero source and
\[
z_b\le1-\rho
\tag{22}
\]
for every nonzero sink.

Let
\[
a=v_0\to v_1\to\cdots\to v_k=b
\]
be any source-to-sink path of total weight \(W\). Summing (20) and using (21)--(22) gives
\[
\rho W
\le
z_b-z_a
\le
2-2\rho.
\]
Hence
\[
\rho\le\frac{2}{2+W}.
\tag{23}
\]
Taking a maximum over paths proves
\[
\rho\le\frac{2}{2+H(P)}.
\tag{24}
\]

It remains to prove feasibility at equality.

Let \(d(v)\) be the longest source-to-\(v\) path weight from (10). Because \(D(P)\) is a finite acyclic graph,
\[
d(v)\ge d(u)+w(u,v)
\tag{25}
\]
for every arc \(u\to v\). Put
\[
q_v=-1+\rho+\rho d(v)
\tag{26}
\]
for vertices in nontrivial components. If \(0\) is isolated, set \(q_0=0\).

At a source, \(d=0\), so (21) holds with equality. At a sink,
\[
d(b)\le H(P),
\]
and therefore, for
\[
\rho=\frac{2}{2+H(P)},
\]
we have
\[
q_b
\le
-1+\rho+\rho H(P)
=
1-\rho.
\tag{27}
\]
Equation (25) gives every arc inequality (20). Thus \(q\) is a feasible potential if we temporarily ignore antisymmetry.

Define the involution
\[
(Tq)_v=-q_{-v}.
\tag{28}
\]
Because every arc \(u\to v\) is paired with \(-v\to-u\) with the same weight, and because sources and sinks are paired antipodally, \(Tq\) is feasible whenever \(q\) is feasible. Convexity therefore makes
\[
\bar q=\frac{q+Tq}{2}
\tag{29}
\]
feasible. By construction,
\[
\bar q_{-v}=-\bar q_v,
\qquad
\bar q_0=0.
\]
Consequently \(\bar q\) comes from a point \(c^*\in\mathbb R^n\), and (26)--(29) give exactly
\[
c_i^*=\frac\rho2(d(i)-d(-i)).
\]
This proves feasibility at (24), hence (9) and (11).

Once \(r\) is fixed at the optimum, the normalized facet-clearance conditions are exactly (12), proving the complete incenter description.

Finally, suppose a source-to-sink path has total weight \(H(P)\). At radius \(r\), the summed lower endpoint, arc, and upper endpoint inequalities are equalities because
\[
rH(P)=2-2r.
\]
Every constituent slack is nonnegative, so every slack must be zero. Hence every physical facet represented along a maximum path is tangent at every incenter.

## Verification
The proof is symbolic for every signed poset.

The source-dependent ingredients were checked in the full primary text: the definition of signed order polytopes, the unique minimal representation, the irredundant facet description using \(\operatorname{minrep}(P)\), \(\operatorname{pmax}(P)\), and \(\operatorname{nmax}(P)\), and the Fischer representation that makes the doubled relation graph acyclic.

The accompanying `verify.py` checks deterministic signed-poset minimal representations including the empty case, type-A chains, unit-root chains, and genuinely signed two-coordinate examples. It constructs \(D(P)\), computes the longest-path formula and canonical center, and independently solves the full Chebyshev linear program by active-set enumeration using the actual irredundant facets. Every case agrees.

The finite replay is corroborative only.

## Relationship to prior work
Beck and Hlavacek introduced signed order and chain polytopes as type-B analogues of Stanley's poset polytopes. Their main results give convex-hull and halfspace descriptions, unimodular triangulations, Ehrhart \(h^*\)-polynomials, a Gorenstein criterion via the Fischer representation, and signed chain polytopes.

Their irredundant order-polytope description is the essential input here. The present metric result adds a Euclidean normalization: unit roots contribute path length \(1\), two-coordinate type-B roots contribute \(\sqrt2\), and the cube facets contribute the two endpoint clearances.

The Fischer representation is used in the source for Gorenstein grading. Here its order-reversing antipodal symmetry instead gives a Chebyshev-center construction by symmetrizing a longest-path potential.

The ordinary order-polytope situation appears only as a special signed-poset pattern. General signed posets allow sign-changing relations, unit roots, and two-sided literal paths, so their controlling invariant is the weighted doubled path height \(H(P)\), not ordinary poset height.

Targeted searches under “signed order polytope”, “type-B order polytope”, “inradius”, “Chebyshev center”, “largest inscribed ball”, and “Fischer representation” did not locate a theorem implying (9)--(12).

## Limitations
The theorem concerns the standard Euclidean realization used in the source.

It uses the actual irredundant facet system. Replacing \(\operatorname{minrep}(P)\) by all roots in the positive-linear closure can introduce redundant hyperplanes and destroy the metric interpretation.

The result determines the inradius, a canonical incenter, every incenter, and forced tangent facets on longest paths. It does not separately classify when the incenter is unique, nor does it determine minimum enclosing spheres or extremal ellipsoids.

The proof is a specialized longest-path argument for the signed-order facet system. A general theorem on Chebyshev centers of antipodally doubled difference-constraint systems could subsume it under different terminology; no such dominating statement was located in the targeted comparison.

## References
1. Matthias Beck and Max Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409, first public version 2023-11-08.
2. Victor Reiner, *Signed posets*, *Journal of Combinatorial Theory, Series A* 62 (1993), 324--360.
3. Steven D. Fischer, *Signed poset homology and q-analog Möbius functions*, Ph.D. thesis, University of Michigan, 1993.
