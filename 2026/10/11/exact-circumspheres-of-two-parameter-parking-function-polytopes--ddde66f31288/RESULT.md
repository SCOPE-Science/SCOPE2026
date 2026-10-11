# Exact circumspheres of two-parameter parking-function polytopes
## Finding
Let
\[
n\ge2,
\qquad
a,b\in\mathbb Z_{>0},
\]
and let
\[
\mathfrak X_n(a,b)\subset\mathbb R^n
\]
be the \((a,b,\ldots,b)\)-parking-function polytope of Hanada--Lentfer--Vindas-Meléndez.

Put
\[
d=a-1,
\qquad
\lambda_j=d+jb
\quad
(0\le j<n),
\]
and for
\[
0\le k\le n
\]
define
\[
S_k=\sum_{j=k}^{n-1}\lambda_j,
\qquad
T_k=\sum_{j=k}^{n-1}\lambda_j^2.
\]
For
\[
1\le k\le n
\]
set
\[
D_k=2S_k-n\lambda_{k-1}.
\tag{1}
\]
Since
\[
D_{k+1}-D_k=-b(2k+n)-2d<0,
\]
the sequence \(D_k\) is strictly decreasing. Define
\[
K=
\min\{k\in\{1,\ldots,n\}:D_k\le nb\}.
\tag{2}
\]
Finally put
\[
s_*=
\begin{cases}
S_K/n,&D_K\ge0,\\[4pt]
\lambda_{K-1}/2,&D_K<0.
\end{cases}
\tag{3}
\]

Then the Euclidean minimum enclosing ball of \(\mathfrak X_n(a,b)\) has the unique center
\[
\boxed{
c_*=(1+s_*)\mathbf1
}
\tag{4}
\]
and squared radius
\[
\boxed{
R^2
=
n s_*^2-2S_Ks_*+T_K.
}
\tag{5}
\]

The source vertex layers are
\[
V_k=
\operatorname{Orb}_{\mathfrak S_n}
\left(
\underbrace{1,\ldots,1}_{k},
a+kb,a+(k+1)b,\ldots,a+(n-1)b
\right),
\qquad
0\le k\le n.
\tag{6}
\]
After coincident layers are identified, the vertices on the circumsphere are exactly:
- the permutations in \(V_K\) if
  \[
  0<D_K<nb;
  \]
- the permutations in \(V_{K-1}\cup V_K\) if
  \[
  D_K\le0;
  \]
- the permutations in \(V_K\cup V_{K+1}\) if
  \[
  D_K=nb.
  \]

When \(a=1\), the first two displayed source layers coincide as sets, so this convention does not double-count their vertices.

For the classical parking-function polytope
\[
a=b=1,
\]
equation (2) becomes
\[
K_n
=
\left\lceil
\frac{
\sqrt{(n-1)(5n-1)}-(n-1)
}{2}
\right\rceil.
\tag{7}
\]
Consequently
\[
\boxed{
\frac{K_n}{n}
\longrightarrow
\frac{\sqrt5-1}{2}.
}
\tag{8}
\]
Thus the outer Euclidean geometry of the classical family is controlled asymptotically by a golden-ratio vertex layer.

## Assumptions and scope
The parameters are positive integers and \(n\ge2\), exactly as in the defining two-parameter family of the cited source.

The metric is the standard Euclidean metric in \(\mathbb R^n\). Circumradius means the radius of the smallest Euclidean ball containing the whole polytope.

The result is specific to this canonical coordinate realization. Integral equivalence, combinatorial equivalence, or general affine equivalence does not preserve Euclidean circumradius.

## Proof
Translate the polytope by \(-\mathbf1\). By the published vertex description, its vertices are all permutations of
\[
v_k=
\left(
\underbrace{0,\ldots,0}_{k},
\lambda_k,\lambda_{k+1},\ldots,\lambda_{n-1}
\right),
\qquad
0\le k\le n.
\tag{9}
\]

A compact set in Euclidean space has a unique minimum enclosing ball. Indeed, if two distinct centers \(c_1,c_2\) gave the same minimum radius \(R\), then for every point \(x\),
\[
\left\|
x-\frac{c_1+c_2}{2}
\right\|^2
=
\frac{\|x-c_1\|^2+\|x-c_2\|^2}{2}
-\frac{\|c_1-c_2\|^2}{4}
<
R^2,
\]
contradicting minimality.

The translated polytope is invariant under all coordinate permutations. Uniqueness therefore forces its circumcenter to be fixed by \(\mathfrak S_n\), hence to have the form
\[
s\mathbf1.
\]
Since every vertex coordinate is nonnegative, increasing \(s\) toward \(0\) strictly decreases every vertex distance whenever \(s<0\). Thus an optimal \(s\) is nonnegative.

For a vertex in layer \(k\), the squared distance to \(s\mathbf1\) is
\[
Q_k(s)
=
k s^2
+
\sum_{j=k}^{n-1}(\lambda_j-s)^2
=
n s^2-2S_ks+T_k.
\tag{10}
\]
All permutations in one layer have the same distance.

The adjacent difference is
\[
Q_k(s)-Q_{k+1}(s)
=
\lambda_k(\lambda_k-2s).
\tag{11}
\]
Because the \(\lambda_k\) are strictly increasing except for the harmless initial value \(\lambda_0=0\) when \(a=1\), the sequence
\[
Q_0(s),Q_1(s),\ldots,Q_n(s)
\]
first increases and then decreases. Hence, for
\[
\frac{\lambda_{k-1}}2
\le
s
\le
\frac{\lambda_k}2,
\tag{12}
\]
the largest layer distance is \(Q_k(s)\), with the expected equality of adjacent layers at the endpoints.

Thus the minimization of the enclosing radius is a one-dimensional convex piecewise-quadratic problem. On the interval (12), the unconstrained minimizer of \(Q_k\) is
\[
s_k=\frac{S_k}{n}.
\tag{13}
\]
The two endpoint tests are
\[
2n\left(
s_k-\frac{\lambda_{k-1}}2
\right)
=
D_k
\tag{14}
\]
and
\[
2n\left(
\frac{\lambda_k}2-s_k
\right)
=
nb-D_k.
\tag{15}
\]
Therefore
\[
s_k\in
\left[
\frac{\lambda_{k-1}}2,
\frac{\lambda_k}2
\right]
\]
if and only if
\[
0\le D_k\le nb.
\tag{16}
\]

Moreover,
\[
D_{k+1}-D_k
=
-b(2k+n)-2d<0.
\tag{17}
\]
So the convex objective has exactly two possible optimal forms. At the first index \(K\) with
\[
D_K\le nb,
\]
either \(D_K\ge0\), in which case the unconstrained minimum \(S_K/n\) lies in the active interval, or \(D_K<0\), in which case the objective is minimized at the shared boundary
\[
\lambda_{K-1}/2
\]
between layers \(K-1\) and \(K\). This proves (2)--(3).

Substitution into (10) gives (5). Translating the center back by \(\mathbf1\) gives (4).

The contact-layer classification follows directly from (11)--(16): an interior minimizer has only layer \(K\) active; a left boundary has layers \(K-1,K\) active; a right boundary, equivalently \(D_K=nb\), has layers \(K,K+1\) active.

For the classical family \(a=b=1\), one has
\[
d=0,
\qquad
D_k=n^2-k(k+n-1).
\]
Condition
\[
D_k\le n
\]
is therefore
\[
k(k+n-1)\ge n(n-1).
\]
Solving the corresponding quadratic inequality gives (7), and division by \(n\) gives (8).

## Verification
The proof is symbolic and valid for all stated parameters.

The accompanying `verify.py` checks the result over a large finite parameter box. For each triple \((n,a,b)\), it reconstructs every source vertex layer, computes all candidate breakpoints and layer-parabola minima independently, and verifies that the packaged formula gives the global minimum of the maximum layer distance. It also checks the predicted contact layers and the classical formula (7).

This finite replay is corroborative only; the arbitrary-parameter proof is the piecewise-quadratic argument above.

## Relationship to prior work
Hanada, Lentfer, and Vindas-Meléndez introduce and study the two-parameter family \(\mathfrak X_n(a,b)\). Their Proposition 3.4 gives exactly the vertex layers used in (6), while Proposition 3.6 gives a minimal inequality description. The paper studies face structure, combinatorial equivalence, volume, lattice-point questions, and relations to partial permutohedra and Pitman--Stanley polytopes.

A later paper by Bayer and collaborators treats parking-function polytopes for an arbitrary positive parameter vector. It gives vertex and facet descriptions, proves generalized-permutahedron and polymatroid structure, and determines combinatorial and circuit diameters. Those diameters are graph/circuit-walk invariants, not Euclidean minimum-enclosing-ball radii.

The inspected full texts contain no occurrence of “circumradius”, “circumcenter”, or “radius” in the relevant Euclidean sense. Targeted searches for parking-function-polytope circumradii, circumcenters, minimum enclosing balls, generalized parking-function outer radii, and the golden-ratio layer phenomenon did not locate a theorem implying (2)--(8).

The previously known partial-permutohedron inradius result is not covering: it concerns an inscribed ball, not a circumsphere, and even in the overlap \(b=1\) it does not determine which vertex layer is farthest from the optimal outer center.

## Limitations
The theorem concerns only the two-parameter family \((a,b,\ldots,b)\), not the full arbitrary-\(\mathbf b\) parking-function-polytope family.

The exact formula is piecewise because the controlling vertex layer changes discretely with \(n,a,b\). No claim is made here about John ellipsoids, widths, or affine-invariant metric quantities.

A residual originality risk remains that a general theorem about minimum enclosing balls of symmetric polymatroids or generalized permutahedra specializes to the same formula under terminology not exposed by the searches.

## References
1. Mitsuki Hanada, John Lentfer, and Andrés R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885, first public version 2022-12-13; Annals of Combinatorics 28 (2024), 575--613, DOI 10.1007/s00026-023-00671-1.
2. Margaret M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first public version 2024-03-12.
3. Aruzhan Amanbayeva and Danielle Wang, *The Convex Hull of Parking Functions of Length \(n\)*, arXiv:2104.08454, first public version 2021-04-17.
