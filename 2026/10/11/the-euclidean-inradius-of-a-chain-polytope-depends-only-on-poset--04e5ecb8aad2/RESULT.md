# The Euclidean inradius of a chain polytope depends only on poset height
## Finding
Let \(P\) be a nonempty finite poset, and let
\[
h=\max\{|C|:C\subseteq P\text{ is a chain}\}
\tag{1}
\]
be its height, counted by elements.

Its chain polytope is
\[
\mathcal C(P)
=
\left\{
x\in\mathbb R_{\ge0}^{P}:
\sum_{p\in C}x_p\le1
\text{ for every chain }C\subseteq P
\right\}.
\tag{2}
\]
Equivalently, it is enough to impose the upper inequalities for maximal chains.

In the standard Euclidean metric of \(\mathbb R^P\),
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathcal C(P)\bigr)
=
\frac1{h+\sqrt h}.
}
\tag{3}
\]

Set
\[
r=\frac1{h+\sqrt h}.
\tag{4}
\]
Then the complete incenter set is
\[
\boxed{
\operatorname{Cent}\bigl(\mathcal C(P)\bigr)
=
\left\{
x:
x_p\ge r\ \forall p,\quad
\sum_{p\in C}x_p
\le
1-r\sqrt{|C|}
\ \text{for every maximal chain }C
\right\}.
}
\tag{5}
\]

In particular,
\[
\boxed{
r\mathbf1
}
\tag{6}
\]
is always an incenter.

The incenter is unique exactly when every element of \(P\) belongs to at least one longest chain:
\[
\boxed{
\operatorname{Cent}\bigl(\mathcal C(P)\bigr)=\{r\mathbf1\}
\iff
P=\bigcup_{\substack{C\text{ chain}\\|C|=h}}C.
}
\tag{7}
\]

Thus the Euclidean inradius forgets all branching and width data and depends only on poset height, while uniqueness of the center detects whether the longest chains cover the poset.

## Assumptions and scope
The poset is finite and nonempty.

The chain polytope is taken in its standard coordinate realization in \(\mathbb R^P\), with the usual Euclidean norm. The statement is not affine-invariant.

Height means the number of elements in a longest chain, so an antichain has height \(1\).

The source recalls that chain-polytope inequalities are indexed by maximal chains. No purity or gradedness assumption is imposed.

## Proof
The source gives the chain polytope by nonnegativity together with
\[
\sum_{p\in C}x_p\le1
\tag{8}
\]
for maximal chains \(C\).

For a coordinate facet
\[
x_p=0,
\]
the Euclidean distance from a point \(x\) is simply
\[
x_p.
\tag{9}
\]

For a maximal-chain facet (8), the outward normal is the indicator vector
\[
\mathbf1_C,
\]
whose norm is
\[
\|\mathbf1_C\|=\sqrt{|C|}.
\]
Hence the Euclidean distance from \(x\) to that supporting hyperplane is
\[
\frac{1-\sum_{p\in C}x_p}{\sqrt{|C|}}.
\tag{10}
\]

Suppose a Euclidean ball of radius \(\rho\), centered at \(x\), is contained in \(\mathcal C(P)\). Every coordinate facet gives
\[
x_p\ge\rho
\qquad
(p\in P).
\tag{11}
\]

Choose a longest chain
\[
C_*
\]
with
\[
|C_*|=h.
\]
Its chain facet gives
\[
\sum_{p\in C_*}x_p+\rho\sqrt h\le1.
\tag{12}
\]
Using (11),
\[
h\rho+\rho\sqrt h\le1.
\]
Therefore
\[
\rho\le\frac1{h+\sqrt h}.
\tag{13}
\]

Now set \(r\) as in (4) and consider
\[
x=r\mathbf1.
\]
Every coordinate-facet distance is exactly \(r\).

If \(C\) is any maximal chain of cardinality
\[
k=|C|\le h,
\]
then its distance from \(r\mathbf1\) is
\[
\frac{1-kr}{\sqrt k}.
\tag{14}
\]
This is at least \(r\) precisely when
\[
1\ge r(k+\sqrt k).
\tag{15}
\]
Since
\[
k+\sqrt k
\]
is increasing in \(k\) and \(k\le h\),
\[
r(k+\sqrt k)
\le
r(h+\sqrt h)
=
1.
\]
Thus every chain facet is at distance at least \(r\), so the radius-\(r\) ball centered at \(r\mathbf1\) is contained in \(\mathcal C(P)\). Together with (13), this proves (3).

For a center \(x\), a radius-\(r\) ball is contained in \(\mathcal C(P)\) exactly when all normalized facet clearances are at least \(r\). Equations (9)--(10) give exactly the inequalities in (5), proving the complete incenter description.

It remains to characterize uniqueness.

Assume every element of \(P\) belongs to a longest chain. Let \(x\) be any incenter. On every longest chain \(C\),
\[
\sum_{p\in C}x_p
\le
1-r\sqrt h
=
hr.
\tag{16}
\]
But (5) also gives
\[
x_p\ge r
\]
for every \(p\). Since \(C\) has \(h\) elements, equality is forced term by term:
\[
x_p=r
\qquad
(p\in C).
\]
Because the longest chains cover \(P\), this forces
\[
x=r\mathbf1.
\]
So the incenter is unique.

Conversely, suppose some element
\[
q\in P
\]
belongs to no longest chain. Every maximal chain containing \(q\) then has cardinality strictly less than \(h\). At the center \(r\mathbf1\), each such chain has strictly positive slack in (15):
\[
1-r\bigl(|C|+\sqrt{|C|}\bigr)>0.
\tag{17}
\]
There are finitely many maximal chains containing \(q\). Choose
\[
0<\varepsilon
<
\min_{C\ni q}
\left[
1-r\bigl(|C|+\sqrt{|C|}\bigr)
\right].
\tag{18}
\]
Then
\[
x=r\mathbf1+\varepsilon e_q
\tag{19}
\]
still satisfies every inequality in (5): chains not containing \(q\) are unchanged, and chains containing \(q\) retain nonnegative slack by (18). Hence \(x\) is a second incenter. This proves (7).

## Verification
The arbitrary-poset proof is exact and uses only the published chain-polytope facet description and Euclidean distances to supporting hyperplanes.

The accompanying `verify.py` enumerates all naturally labeled posets on at most five elements by taking transitive closures of all forward relation sets. For every distinct poset it computes all maximal chains, verifies the height formula, checks the candidate center against every normalized facet distance, and checks the longest-chain coverage criterion for uniqueness. For every nonunique case it constructs an explicit positive coordinate perturbation preserving all radius-\(r\) clearances.

These finite checks are corroborative only; they are not used as an exhaustive proof for arbitrary posets.

## Relationship to prior work
Fang, Fourier, Litza, and Pegel study a continuous family of marked poset polytopes containing marked order and marked chain polytopes as extremal members. Their introduction recalls the standard chain-polytope inequalities and emphasizes Ehrhart equivalence and transfer maps between order- and chain-type realizations. Their results concern lattice structure, transfer maps, continuous degenerations, face numbers, tropical subdivisions, and vertices.

The inspected full text does not state a Euclidean inradius, largest-inscribed-ball, or Chebyshev-center theorem for chain polytopes. In particular, Ehrhart equivalence does not preserve Euclidean metric quantities.

The formula here shows that a standard metric invariant collapses to a single order-theoretic parameter:
\[
r_{\mathrm{in}}=\frac1{h+\sqrt h}.
\]
At the same time, the center set retains finer information: it is a singleton exactly when the longest chains cover every element.

Targeted searches for chain-polytope inradii, Chebyshev centers, largest inscribed Euclidean balls, and height-based radius formulas did not locate a statement implying (3)--(7).

## Limitations
The theorem is specific to the standard Euclidean realization of the ordinary chain polytope.

It does not compute Euclidean circumradii, John ellipsoids, or analogous radii for arbitrary marked or intermediate chain-order polytopes.

The inradius formula itself is elementary once the facet normals are normalized. The structural content is the all-poset formula together with the complete incenter set and the exact longest-chain coverage criterion for uniqueness.

A general theorem on Chebyshev centers of nonnegative packing polytopes could imply the same calculation under different terminology; no such dominating result was located in the targeted comparison.

## References
1. Xin Fang, Ghislain Fourier, Jan-Philipp Litza, and Christoph Pegel, *A Continuous Family of Marked Poset Polytopes*, arXiv:1712.01037, first public version 2017-12-04; SIAM Journal on Discrete Mathematics 34 (2020), 611--639, DOI 10.1137/18M1228529.
