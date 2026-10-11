# Exact Euclidean radii and contact-facet phase of complete-graph matching polytopes
## Finding
For an integer \(n\ge2\), let
\[
M_n=P_M(K_n)\subset\mathbb R^{\binom n2}
\]
be the matching polytope of the complete graph, in the canonical edge-incidence coordinates.

The Euclidean incenter is unique and has every edge coordinate equal to the inradius \(r_n\). Explicitly,
\[
r_2=\frac12,
\]
while
\[
r_n=
\frac1{n+\sqrt{2n/(n-1)}}
\qquad
\text{for }n\in\{3,5,7\},
\]
and
\[
r_n=
\frac1{n-1+\sqrt{n-1}}
\qquad
\text{for }n=4,6\text{ or }n\ge8.
\]

Every coordinate facet \(x_e=0\) is tangent to the maximal inscribed ball. The additional tangent facets undergo a finite phase change:
\[
\begin{array}{c|c}
n & \text{additional tangent facets}\\
\hline
2 & x_e=1\\
3,5,7 & \text{the global odd-set facet}\\
4 & \text{all degree facets and all triangle odd-set facets}\\
6\text{ or }n\ge8 & \text{all degree facets.}
\end{array}
\]

For the minimum enclosing ball, write
\[
m=\binom n2,
\qquad
k=\left\lfloor\frac n2\right\rfloor.
\]
For every \(n\ge3\), the unique circumcenter is
\[
\frac{k}{m}\mathbf1
\]
and the circumradius is
\[
R_n=\sqrt{k-\frac{k^2}{m}}.
\]
Equivalently,
\[
R_n^2=
\frac{n(n-2)}{2(n-1)}
\quad\text{when }n\ge4\text{ is even},
\]
and
\[
R_n^2=
\frac{(n-1)^2}{2n}
\quad\text{when }n\ge3\text{ is odd}.
\]
The vertices on the minimum enclosing sphere are exactly the maximum matchings. For \(n=2\), \(M_2=[0,1]\), so its circumcenter and circumradius are both \(1/2\).

## Assumptions and scope
The metric is the standard Euclidean metric on the edge-coordinate space \(\mathbb R^{\binom n2}\). The result concerns the full matching polytope, whose vertices are incidence vectors of all matchings, not the perfect-matching face.

For \(n\ge4\), the irredundant matching-polytope facets of \(K_n\) are the coordinate facets, the vertex-degree facets, and the odd-set facets. For \(n=3\), the degree inequalities are redundant and the noncoordinate facet is the single triangle odd-set facet. For \(n=2\), the polytope is a segment.

The radius formulas are realization-dependent Euclidean statements; they are not invariants under arbitrary affine equivalence.

## Proof
Let
\[
N=\binom n2.
\]
The full symmetric group on the vertices of \(K_n\) acts orthogonally on \(\mathbb R^N\) by permuting edge coordinates and preserves \(M_n\).

Suppose a ball \(B(c,r)\) is contained in \(M_n\). For every graph automorphism \(g\), the ball \(B(gc,r)\) is also contained in \(M_n\). Averaging all orbit centers gives
\[
\bar c=\frac1{|S_n|}\sum_{g\in S_n}gc.
\]
For every vector \(y\) with \(\|y\|\le r\), each point \(gc+y\) belongs to \(M_n\), and convexity therefore gives \(\bar c+y\in M_n\). Thus a largest inscribed ball may be centered at an invariant point. Every invariant point has a common edge coordinate, say \(q\).

For \(K_n\), the matching-polytope facet theorem gives:
\[
x_e\ge0,
\]
the degree facets
\[
\sum_{e\ni v}x_e\le1
\]
whenever the vertex is essential, and the odd-set facets
\[
x(E(S))\le\frac{|S|-1}{2}
\]
for induced factor-critical \(2\)-connected odd sets \(S\). In \(K_n\), every odd set of size at least \(3\) is of this type.

At the invariant point \(q\mathbf1\), the distance to a coordinate facet is
\[
d_0(q)=q.
\]
For \(n\ge4\), the distance to a degree facet is
\[
d_{\deg}(q)=
\frac{1-(n-1)q}{\sqrt{n-1}}.
\]
For an odd set of size \(s\ge3\), the distance to its facet is
\[
d_s(q)
=
\frac{(s-1)/2-\binom s2q}{\sqrt{\binom s2}}
=
\sqrt{\frac{s-1}{2s}}\,(1-sq).
\]

Hence the largest invariant inball radius is the largest \(q\) satisfying
\[
q\le d_{\deg}(q)
\]
for every degree facet and
\[
q\le d_s(q)
\]
for every odd-set facet. The balance values are
\[
q_{\deg}
=
\frac1{n-1+\sqrt{n-1}}
\]
and
\[
q_s
=
\frac1{s+\sqrt{2s/(s-1)}}.
\]
The denominator in \(q_s\) is strictly increasing with odd \(s\ge3\), so among odd-set facets only the largest odd \(s\le n\) can control the inradius.

If \(n\ge4\) is even, the largest odd size is \(s=n-1\). Comparing the two denominators gives equality at \(n=4\) and
\[
n-1+\sqrt{n-1}>
n-1+\sqrt{\frac{2(n-1)}{n-2}}
\]
for every even \(n\ge6\). Thus degree facets control for even \(n\ge6\), with a tie at \(n=4\).

If \(n\) is odd, the largest odd set is the whole vertex set. Direct comparison gives odd-set control for \(n=3,5,7\) and degree control for every odd \(n\ge9\). For the last assertion, writing \(q=n-1\), the difference
\[
\sqrt q-1-\sqrt{2(q+1)/q}
\]
is positive at \(q=8\) and strictly increasing for \(q\ge8\).

This proves the inradius formulas and the stated tangent-facet phase.

The incenter is unique. Every center of a ball of radius \(r_n\) must satisfy
\[
x_e\ge r_n
\]
for every edge. In the degree-controlled cases, the shrunken degree inequality is
\[
\sum_{e\ni v}x_e
\le
1-r_n\sqrt{n-1}
=
(n-1)r_n.
\]
Since the left side is already at least \((n-1)r_n\), every incident coordinate equals \(r_n\), and therefore every coordinate does. In the odd-set-controlled cases \(n=3,5,7\), the shrunken global odd-set inequality similarly forces
\[
x(E)=Nr_n,
\]
while every coordinate is at least \(r_n\), so again every coordinate equals \(r_n\). The cases \(n=2\) and \(n=4\) are immediate from the tangent upper facet or tangent degree facets.

For the circumradius, the same group averaging argument may be applied to the convex function
\[
c\longmapsto\max_{v\in\operatorname{vert}(M_n)}\|v-c\|.
\]
Thus an optimal center may be taken to be \(q\mathbf1\). A matching of cardinality \(j\) has incidence vector with \(j\) ones and \(N-j\) zeros, so its squared distance from \(q\mathbf1\) is
\[
D_j(q)^2
=
j(1-q)^2+(N-j)q^2
=
j(1-2q)+Nq^2.
\]
For \(n\ge3\), the minimizing value lies below \(1/2\), so the farthest vertices are maximum matchings of size
\[
k=\left\lfloor\frac n2\right\rfloor.
\]
Minimizing
\[
k(1-2q)+Nq^2
\]
gives
\[
q=\frac{k}{N}
\]
and
\[
R_n^2
=
k-\frac{k^2}{N}.
\]
Because \(q<1/2\), equality occurs exactly for matchings of cardinality \(k\), proving the outer-sphere classification.

Finally, the circumcenter is unique because
\[
c\longmapsto
\max_{v\in\operatorname{vert}(M_n)}
\|v-c\|^2
\]
is the sum of the strictly convex function \(\|c\|^2\) and a convex function. The case \(n=2\) is the segment \([0,1]\).

## Verification
The accompanying `verify.py` enumerates all matchings of \(K_n\) for \(2\le n\le8\). It checks the exact vertex cardinalities, evaluates the proposed circumcenter against every matching vertex, evaluates the proposed incenter against every facet orbit in the matching-polytope description, and confirms the tangent-facet phase numerically to high precision.

These finite calculations are corroborative only. The proof above establishes the formulas for every \(n\ge2\).

## Relationship to prior work
Eisley, Matsushita, and Vindas-Meléndez study matching polytopes as lattice polytopes. Their paper gives the matching-polytope definition and records the irredundant facet theorem used above: nonnegativity facets, essential-vertex degree facets, and induced \(2\)-connected factor-critical odd-set facets. Their principal results concern Gorensteinness and the integer decomposition property.

The inspected full text contains no occurrence of “inradius,” “circumradius,” “Euclidean,” or “radius.” Targeted searches for complete-graph matching-polytope inradii, circumradii, Chebyshev centers, blossom-facet distances, and the displayed radical forms did not locate a theorem covering these formulas or the contact-facet phase.

The classical matching-polytope facet theorem is therefore used as an input rather than presented as new. The new assertion is the Euclidean optimization over those facets and vertices for the highly symmetric family \(P_M(K_n)\).

## Limitations
The theorem is specific to complete graphs. For a general graph, automorphism averaging need not reduce the center to one coordinate orbit, and the closest facet family can depend on the detailed factor-critical induced subgraphs.

The result uses the canonical edge-incidence coordinates and the standard Euclidean norm. Different affine realizations can change both radii.

The originality assessment is based on the inspected exact-object source plus targeted database and literature searches. It does not exclude an equivalent formula hidden in unindexed or differently normalized matching-polytope literature.

## References
1. Benjamin Eisley, Koji Matsushita, and Andrés R. Vindas-Meléndez, *Matching Polytopes, Gorensteinness, and the Integer Decomposition Property*, arXiv:2407.08820, first public version 2024-07-11; Graphs and Combinatorics 41 (2025), article 58, DOI 10.1007/s00373-025-02923-8.
2. William Pulleyblank and Jack Edmonds, *Facets of 1-matching polyhedra*, Lecture Notes in Mathematics 411 (1974), 214–242.
