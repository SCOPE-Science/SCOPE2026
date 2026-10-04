# The equilateral triangle is locally Rupert

## Finding

Every equilateral triangle, regarded as a flat polygon in \(\mathbb R^3\), is locally Rupert in the sense introduced by Scott.

Concretely, there is an orientation \(P\) of the triangle such that for every \(\varepsilon>0\) one can find a rotation \(Q\in SO(3)\), with rotation angle less than \(\varepsilon\), satisfying
\[
\pi(QP)\subset\operatorname{int}\pi(P),
\]
where \(\pi\) is orthogonal projection to the \(xy\)-plane.

As an immediate consequence of Scott's prism theorem, every right prism over an equilateral triangle, with arbitrary positive height, is locally reverse Rupert. In particular, this supplies the triangular-prism case excluded from the regular-prism family covered by the nontrivial-double-arch criterion.

## Assumptions and scope

Normalize the triangle to
\[
\Delta
=
\operatorname{conv}
\left\{
(0,1),
\left(-\frac{\sqrt3}{2},-\frac12\right),
\left(\frac{\sqrt3}{2},-\frac12\right)
\right\}.
\]
Uniform scaling commutes with rotations and projection, so this normalization loses no generality.

The triangle is treated as a flat polygon in \(\mathbb R^3\), as in Scott's framework. We are free to choose its orientation, including its translation relative to the origin about which rotations are represented.

Put
\[
q=(2\sqrt3-4,0).
\]
The locally Rupert orientation is the flat triangle
\[
P=\Delta+q
\]
at height \(0\).

The result is local: it gives passages whose rotation angle tends to \(0\). The prism corollary is local reverse Rupert, exactly the notion in Scott's Theorem 4.3.

## Proof

Write the normalized triangle as the intersection
\[
\Delta
=
\left\{
x\in\mathbb R^2:
N_i\cdot x\le\frac12,\quad i=0,1,2
\right\},
\]
with outward unit normals
\[
N_0=(0,-1),
\qquad
N_1=\left(-\frac{\sqrt3}{2},\frac12\right),
\qquad
N_2=\left(\frac{\sqrt3}{2},\frac12\right).
\]

Let \(R_z(\alpha)\) and \(R_x(\alpha)\) denote the usual rotations around the \(z\)- and \(x\)-axes. Define
\[
\phi=-\frac{5\pi}{12},
\qquad
\theta_t=\arccos(1-t)
\]
for \(0<t<1\), and set
\[
Q_t
=
R_z\left(\frac t4+\phi\right)
R_x(\theta_t)
R_z(-\phi).
\]
Because \(\theta_t\to0\),
\[
Q_t\longrightarrow I
\qquad(t\downarrow0).
\]
Thus the rotation angle of \(Q_t\) tends to \(0\).

For points initially in the \(xy\)-plane, the projected action of \(Q_t\) has linear part
\[
A_t
=
R_{t/4+\phi}
\begin{pmatrix}
1&0\\
0&1-t
\end{pmatrix}
R_{-\phi},
\]
where the \(R\)'s on the right are planar rotations. We have
\[
A_0=I.
\]
Let
\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
n=
\left(
\cos\frac{\pi}{12},
\sin\frac{\pi}{12}
\right).
\]
Differentiating at \(t=0\) gives
\[
B:=A'_0
=
\frac14J-nn^{\mathsf T}
=
\begin{pmatrix}
-\frac12-\frac{\sqrt3}{4}&-\frac12\\
0&-\frac12+\frac{\sqrt3}{4}
\end{pmatrix}.
\]

Subtract the fixed translation \(q\) after projection. The image of the normalized triangle is then given by the affine map
\[
F_t(v)
=
A_tv+(A_t-I)q.
\]
Hence
\[
F_0(v)=v
\]
and
\[
F'_0(v)=Bv+Bq.
\]
The chosen translation has the exact property
\[
Bq=\left(\frac12,0\right).
\]

It remains to check only the six vertex-side incidences that are active at \(t=0\). For every pair \((i,j)\) satisfying
\[
N_i\cdot v_j=\frac12,
\]
direct substitution yields
\[
N_i\cdot F'_0(v_j)
=
-\frac14+\frac{\sqrt3}{8}
=
-\frac{2-\sqrt3}{8}<0
\]
for five of the six incidences. For the remaining incidence,
\[
N_i\cdot F'_0(v_j)
=
-\frac14-\frac{5\sqrt3}{8}<0.
\]

Thus every side inequality that is tight at \(t=0\) becomes strictly satisfied to first order for \(t>0\). Every nonactive vertex-side inequality already has a strict margin at \(t=0\). Since there are only finitely many inequalities and all depend continuously on \(t\), there exists \(t_0>0\) such that for every \(0<t<t_0\),
\[
F_t(\Delta)\subset\operatorname{int}\Delta.
\]
Undoing the translation gives
\[
\pi(Q_tP)\subset\operatorname{int}\pi(P).
\]

Since \(Q_t\to I\), for every \(\varepsilon>0\) a sufficiently small \(t>0\) gives a Rupert rotation of angle below \(\varepsilon\). Therefore the equilateral triangle is locally Rupert.

Scott's Theorem 4.3 states that a right prism over a locally Rupert polygon is locally reverse Rupert. Applying it to the equilateral triangle proves the prism corollary.

## Verification

The standalone checker performs two independent types of checks.

First, it carries out the critical first-order certificate exactly in the quadratic field \(\mathbb Q(\sqrt3)\). It verifies
\[
Bq=\left(\frac12,0\right),
\]
enumerates all six active vertex-side incidences, and confirms exactly that five have inward derivative
\[
-\frac14+\frac{\sqrt3}{8}
\]
and one has inward derivative
\[
-\frac14-\frac{5\sqrt3}{8}.
\]

Second, it reconstructs the actual three-dimensional matrices \(Q_t\) for several decreasing positive values of \(t\), verifies orthogonality and determinant \(1\), and checks strict satisfaction of all nine vertex-side inequalities after projection.

The replay output is:

`VERIFY_OK equilateral triangle local Rupert passage`

The numerical finite-\(t\) checks are consistency tests only. The existence of a passage for every sufficiently small positive \(t\) follows from the exact derivative certificate and continuity.

## Relationship to prior work

Scott introduced the local Rupert framework and proved that every nontrivial double-arch flat polygon is locally Rupert. He observed that all regular polygons except the triangle satisfy that hypothesis. His prism theorem proves that a right prism over any locally Rupert polygon is locally reverse Rupert, but the survey of applications explicitly excludes the triangular prism from the regular-prism family.

The same paper identifies the triangle as a natural boundary case for further work, suggesting an extension of the double-arch argument to the triangle and other trivial double-arch polygons. The construction above supplies that omitted case directly, without changing the definition of local passage.

Steininger and Yurkevich's algorithmic work gives general decision and search methods for Rupert passages but does not state this local equilateral-triangle theorem or its local reverse triangular-prism consequence in the inspected material.

Later work by Steininger and Yurkevich exhibits a polyhedron that is Rupert but not locally Rupert. Thus the local conclusion used here is genuinely stronger than merely finding some Rupert passage.

Targeted searches for the equilateral triangle as a locally Rupert flat polygon, for a locally reverse Rupert triangular prism, and for the equivalent small-rotation formulation did not locate an equivalent theorem.

## Limitations

The explicit construction is for equilateral triangles. It does not assert that every triangle, or every trivial double-arch polygon, is locally Rupert.

The prism conclusion uses Scott's published prism theorem as a premise rather than re-proving the prism bootstrap.

The proof establishes existence for all sufficiently small \(t>0\) but does not optimize a quantitative clearance or a largest admissible rotation angle.

Because the construction is elementary once the correct translated orientation is found, an unindexed prior observation remains a residual originality risk.

## References

E. J. Scott, “Two Sufficient Conditions for a Polyhedron to be (Locally) Rupert,” arXiv:2208.12912, first submitted 2022-08-27, primary MSC 52B10.

J. Steininger and S. Yurkevich, “An algorithmic approach to Rupert's problem,” arXiv:2112.13754, first submitted 2021-12-27.

J. Steininger and S. Yurkevich, “A convex polyhedron without Rupert's property,” arXiv:2508.18475, first submitted 2025-08-25.
