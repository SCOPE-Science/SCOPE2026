# Minimal-matroid base polytopes have a one-exception minimum-sphere transition
## Finding
Let
\[
1\le r<n,
\qquad
t=n-r.
\]
Let \(T_{r,n}\) denote the minimal connected matroid of rank \(r\) on \(n\) elements. In the graphical realization used by Ferroni, label the \(r\) ordinary cycle edges by
\[
A=[r]
\]
and the \(t\) parallel replacement edges by
\[
B=\{r+1,\ldots,n\}.
\]

The bases are one exceptional basis
\[
A
\]
and the \(rt\) one-for-one exchanges
\[
(A\setminus\{i\})\cup\{j\},
\qquad
i\in A,\ j\in B.
\]
Hence the base polytope has vertices
\[
v_0=\mathbf1_A,
\qquad
v_{ij}=v_0-e_i+e_j.
\tag{1}
\]

The unique minimum enclosing Euclidean ball has a sharp two-phase description.

If
\[
rt\le n,
\]
then
\[
\boxed{
c=\frac rn\mathbf1,
\qquad
R^2=\frac{rt}{n}.
}
\tag{2}
\]
Every one of the \(rt+1\) vertices lies on the minimum sphere.

If
\[
rt\ge n,
\]
then
\[
\boxed{
c=
\frac{r-1}{r}\mathbf1_A
+
\frac1t\mathbf1_B,
\qquad
R^2=
2-\frac{n}{rt}.
}
\tag{3}
\]
The center in (3) is the barycenter of the \(rt\) exchange vertices.

When
\[
rt>n,
\]
the contact set is exactly
\[
\boxed{
\{v_{ij}:i\in A,\ j\in B\},
}
\tag{4}
\]
while \(v_0\) lies strictly inside the minimum sphere.

At the boundary
\[
rt=n,
\]
the two formulas coincide and every vertex is a contact. In positive integers,
\[
rt\le r+t
\]
occurs only when \(r=1\), \(t=1\), or \((r,t)=(2,2)\). Thus, apart from the simplex ranks and the isolated \(T_{2,4}\) boundary case, the exceptional basis is strictly interior to the minimum sphere.

Equivalently, put
\[
q_*=
\min\left\{
1,\frac{rt}{n}
\right\}.
\tag{5}
\]
Then the center is
\[
\boxed{
c=
\left(1-\frac{q_*}{r}\right)\mathbf1_A
+
\frac{q_*}{t}\mathbf1_B.
}
\tag{6}
\]

## Assumptions and scope
The realization is the standard matroid base-polytope realization
\[
\mathcal P(T_{r,n})
=
\operatorname{conv}
\{\mathbf1_C:C\text{ is a basis}\}
\subset\mathbb R^n
\]
with the ordinary Euclidean metric inherited from \(\mathbb R^n\).

Ferroni proves that \(T_{r,n}\) is the unique connected rank-\(r\), size-\(n\) matroid with the minimum possible number
\[
rt+1
\]
of bases, and gives the graphical cycle-with-parallel-edge realization from which (1) follows.

The theorem concerns the minimum enclosing Euclidean ball of the vertex set, equivalently of the whole convex base polytope. It does not concern the intrinsic inradius, John ellipsoid, or Ehrhart data.

## Proof
A compact set in Euclidean space has a unique minimum-enclosing-ball center. The group
\[
S_r\times S_t
\]
acts isometrically on the realization by permuting the coordinates inside \(A\) and inside \(B\). It fixes \(v_0\) and acts transitively on the exchange vertices \(v_{ij}\). Therefore the unique minimum-enclosing center must be constant on each block.

Every block-constant point in the affine hull
\[
\sum_{k=1}^n x_k=r
\]
can be written uniquely as
\[
c(q)
=
\left(1-\frac qr\right)\mathbf1_A
+
\frac qt\mathbf1_B
\tag{7}
\]
for some real \(q\).

Put
\[
a=\frac{n}{rt}.
\tag{8}
\]
The squared distance from \(c(q)\) to the exceptional vertex is
\[
\begin{aligned}
d_0(q)^2
&=
r\left(\frac qr\right)^2
+
t\left(\frac qt\right)^2\\
&=
a q^2.
\end{aligned}
\tag{9}
\]

For an exchange vertex
\[
v_{ij}=v_0-e_i+e_j,
\]
all choices of \(i,j\) give the same distance. Since
\[
\|-e_i+e_j\|^2=2,
\]
one obtains
\[
\boxed{
d_1(q)^2
=
2+a q^2-2a q.
}
\tag{10}
\]
Thus the full minimum-enclosing-ball problem reduces exactly to
\[
\min_{q\in\mathbb R}
\max\{a q^2,\ 2+a q^2-2a q\}.
\tag{11}
\]

The two quadratics are equal exactly at
\[
q=\frac1a=\frac{rt}{n}.
\tag{12}
\]

Suppose first that
\[
a\ge1,
\]
equivalently
\[
rt\le n.
\]
Then the crossing point \(1/a\) lies in \((0,1]\). Before that point the exchange-orbit distance is the larger term and is decreasing; after that point the exceptional-vertex distance is the larger term and is increasing. Hence the unique minimizer is
\[
q_*=\frac1a=\frac{rt}{n}.
\]
Substituting into (7) gives
\[
c(q_*)=\frac rn\mathbf1,
\]
and (9)--(10) give
\[
R^2=\frac1a=\frac{rt}{n}.
\]
Both orbit distances are equal, so all vertices are contacts.

Now suppose
\[
a\le1,
\]
equivalently
\[
rt\ge n.
\]
The crossing point \(1/a\) lies at or beyond \(1\). Up to the crossing point the larger term in (11) is
\[
d_1(q)^2.
\]
This quadratic has its unique minimum at
\[
q=1.
\]
Consequently
\[
q_*=1,
\]
which gives the center in (3), and
\[
R^2=d_1(1)^2=2-a=2-\frac{n}{rt}.
\]
At this center,
\[
d_0(1)^2=a=\frac{n}{rt}.
\]
Therefore \(v_0\) is strictly interior precisely when
\[
rt>n,
\]
whereas equality gives the common boundary case.

For a geometric minimality certificate in the second phase, observe that
\[
c(1)
=
\frac1{rt}
\sum_{i\in A}\sum_{j\in B}v_{ij}.
\tag{13}
\]
Thus the proposed center lies in the convex hull of equal-radius contact points. For any competing center \(y\), averaging the squared distances from \(y\) to those contacts gives
\[
R^2+\|y-c(1)\|^2.
\]
At least one contact is therefore no closer than this average, proving global minimality and uniqueness directly.

In the first phase,
\[
c(q_*)
=
(1-q_*)v_0
+
\frac{q_*}{rt}
\sum_{i,j}v_{ij},
\tag{14}
\]
and
\[
0<q_*\le1.
\]
Since all vertices are equidistant from this convex-combination center, the same squared-distance identity proves global minimality and uniqueness.

Finally,
\[
rt\le r+t
\iff
(r-1)(t-1)\le1.
\]
For positive integers this occurs exactly when \(r=1\), \(t=1\), or \(r=t=2\), giving the stated discrete phase classification.

## Verification
The source-dependent vertex description was checked directly in the primary full text. Ferroni proves that \(T_{r,n}\) is the unique connected matroid of its rank and size with \(r(n-r)+1\) bases, realizes it as a cycle with one edge replaced by \(n-r\) parallel copies, and explicitly counts the one all-black spanning tree together with the \(r(n-r)\) spanning trees obtained by choosing one parallel edge and omitting one black edge.

The same paper gives the equivalent base-polytope inequality description and identifies the duality
\[
T_{r,n}^*\cong T_{n-r,n}.
\]
The final radius formula is symmetric under this rank-corank exchange.

The accompanying `verify.py` constructs every vertex for all
\[
2\le n\le30
\]
and every rank, checks the claimed center, shell radii, and contact phase directly, and independently minimizes the exact one-variable max-of-quadratics objective numerically. These finite checks are corroborative only; the proof above is valid for all parameters.

## Relationship to prior work
Ferroni studies minimal matroid polytopes because they have the fewest bases among connected matroids of fixed rank and cardinality. The paper develops their graphical realization, facet description, Ehrhart polynomial, \(h^*\)-polynomial, real-rootedness, and their role in circuit-hyperplane relaxation.

Fan and Li later recover minimal matroids as a special case of Schubert matroids in their Ehrhart theory. Their full text likewise treats lattice-point enumeration rather than Euclidean minimum-enclosing balls.

Direct full-text searches of these same-object papers for “circumradius”, “radius”, “Euclidean”, and “minimum enclosing” did not locate the metric theorem above. Targeted searches under “minimal matroid polytope”, “minimum enclosing ball”, “circumradius”, “Chebyshev center”, and the notation \(T_{r,n}\) did not locate an implication-equivalent statement.

A previously known general inradius formula for connected matroid base polytopes does not cover the present invariant: the minimum enclosing ball is controlled by the vertex configuration rather than by facet clearances.

## Limitations
The theorem is for the standard indicator-vector realization of the minimal matroid base polytope.

The two-orbit reduction depends on the full
\[
S_r\times S_t
\]
symmetry of this canonical realization. An arbitrary affine image need not preserve the formulas.

No claim is made about the John or Löwner ellipsoid, intrinsic inradius, or analogous minimum spheres for all Schubert or panhandle matroids.

The proof becomes short once the one-exception vertex structure is recognized, so an equivalent observation could exist under root-polytope or Schubert-matroid terminology not surfaced by the targeted searches.

## References
1. Luis Ferroni, *On the Ehrhart Polynomial of Minimal Matroids*, arXiv:2003.02679, first public version 2020-03-05; *Discrete & Computational Geometry* 68 (2022), 255--273, DOI 10.1007/s00454-021-00313-4.
2. Neil J. Y. Fan and Yao Li, *On the Ehrhart Polynomial of Schubert Matroids*, arXiv:2110.11549, first public version 2021-10-22; *Discrete & Computational Geometry* 70 (2023), 946--967, DOI 10.1007/s00454-023-00495-z.
