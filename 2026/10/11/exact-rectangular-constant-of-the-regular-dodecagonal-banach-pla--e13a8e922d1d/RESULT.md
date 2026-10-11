# Exact rectangular constant of the regular dodecagonal Banach plane
## Finding
Let \(X_{12}=(\mathbb R^2,N_{12})\) be the real Banach plane whose unit ball is the Euclidean regular dodecagon circumscribed about the Euclidean unit disk. Then its Joly rectangular constant is
\[
\mu(X_{12})=5\sqrt3-7.
\]

Equivalently,
\[
\frac1{\mu(X_{12})}
=
\frac{7+5\sqrt3}{26}.
\]
The value is attained. Put
\[
r=2-\sqrt3.
\]
One maximizing triple is
\[
x=(1,-r),\qquad y=(0,1),\qquad \lambda=3-\sqrt3.
\]

## Assumptions and scope
All scalars are real. Normalize the dodecagon by its twelve outward Euclidean unit facet normals
\[
n_j=
\left(
\cos\frac{j\pi}{6},
\sin\frac{j\pi}{6}
\right),
\qquad 0\le j<12,
\]
so that
\[
N_{12}(z)=\max_{0\le j<12}\langle n_j,z\rangle.
\]
The unit ball is
\[
B_{12}=\bigcap_{j=0}^{11}\{z:\langle n_j,z\rangle\le1\}.
\]

For \(x,y\in S_{X_{12}}\), Birkhoff--James orthogonality \(x\perp_B y\) means
\[
N_{12}(x)\le N_{12}(x+\tau y)
\quad\text{for every }\tau\in\mathbb R.
\]
For a polygonal norm this is equivalent to the existence of a norming functional at \(x\) that vanishes on \(y\).

The rectangular constant is
\[
\mu(X)
=
\sup\left\{
\frac{1+\lambda}{\|x+\lambda y\|}:
x,y\in S_X,\ x\perp_B y,\ \lambda\ge0
\right\}.
\]
Writing
\[
t=\frac{\lambda}{1+\lambda}
\]
turns the quotient into
\[
\frac1{\|(1-t)x+ty\|}.
\]
By continuity, it is therefore enough to find the minimum norm on all line segments joining Birkhoff--James orthogonal unit pairs.

## Proof
Write
\[
r=2-\sqrt3.
\]
Let
\[
v_j
\]
denote the vertex at the intersection of the facets with normals \(n_j\) and \(n_{j+1}\), with indices modulo \(12\). The points needed below are
\[
v_{11}=(1,-r),\qquad
v_0=(1,r),\qquad
v_3=(-r,1),
\]
together with the facet-normal unit points
\[
e_3=(0,1),
\qquad
m_4=\left(-\frac12,\frac{\sqrt3}{2}\right).
\]

Every boundary point is either in the relative interior of an edge or is a vertex. Dihedral symmetry reduces all Birkhoff--James orthogonal chords to three triangles.

If \(x\) lies in the relative interior of the edge with norming functional \(n_0=(1,0)\), then \(x\perp_B y\) forces
\[
\langle n_0,y\rangle=0.
\]
Up to replacing \(y\) by \(-y\), this gives
\[
y=e_3.
\]
As \(x\) varies on the edge from \(v_{11}\) to \(v_0\), all chord points fill
\[
T_E=\operatorname{conv}\{v_{11},v_0,e_3\}.
\]

At the vertex \(v_0\), the norming functionals form the segment joining \(n_0\) and \(n_1\). Hence \(v_0\perp_B y\) precisely when
\[
\langle n_0,y\rangle\langle n_1,y\rangle\le0.
\]
After sign and reflection symmetry, the relevant unit-sphere arc runs from the \(90^\circ\) facet midpoint \(e_3\), through \(v_3\), to the \(120^\circ\) facet midpoint \(m_4\). The corresponding chord points fill
\[
T_1=\operatorname{conv}\{v_0,e_3,v_3\}
\]
and
\[
T_2=\operatorname{conv}\{v_0,v_3,m_4\}.
\]
Thus the reciprocal rectangular constant is the least value of \(N_{12}\) on
\[
T_E\cup T_1\cup T_2.
\]

Set
\[
d=\frac{7+5\sqrt3}{26}
\]
and
\[
c=\frac{17+\sqrt3}{26}.
\]
Since \(0<c<1\), every convex combination of two adjacent facet functionals has dual norm at most \(1\).

For \(T_E\), use
\[
h_E=cn_1+(1-c)n_2.
\]
Direct evaluation gives
\[
h_E(v_{11})=h_E(e_3)=d,
\]
while
\[
h_E(v_0)=\frac{5+11\sqrt3}{26}>d.
\]
Therefore
\[
N_{12}(z)\ge h_E(z)\ge d
\qquad(z\in T_E).
\]

For \(T_1\), the single facet functional \(n_2\) gives
\[
\langle n_2,v_0\rangle
=
\langle n_2,v_3\rangle
=
\sqrt3-1,
\]
and
\[
\langle n_2,e_3\rangle=\frac{\sqrt3}{2}.
\]
Hence
\[
N_{12}(z)\ge\sqrt3-1>d
\qquad(z\in T_1).
\]

For \(T_2\), use
\[
h_2=cn_2+(1-c)n_3.
\]
Then
\[
h_2(v_0)=h_2(m_4)=d,
\]
and
\[
h_2(v_3)=\frac{-5+15\sqrt3}{26}>d.
\]
Thus
\[
N_{12}(z)\ge d
\qquad(z\in T_2).
\]

It remains to show sharpness. On the segment from \(v_{11}\) to \(e_3\), put
\[
a=\frac1{4-\sqrt3}
=\frac{4+\sqrt3}{13}
\]
and
\[
z_*=av_{11}+(1-a)e_3.
\]
A direct simplification gives
\[
z_*=a(1,1).
\]
The ray through \((1,1)\) is a vertex direction of the regular dodecagon, and
\[
N_{12}(z_*)
=
\frac{1+\sqrt3}{2}a
=
d.
\]
Therefore the global minimum is exactly \(d\).

Finally, the convex-combination parameter satisfies
\[
\lambda=\frac{1-a}{a}=3-\sqrt3.
\]
Since
\[
z_*=a(x+\lambda y)
\]
for
\[
x=v_{11}=(1,-r),\qquad y=e_3=(0,1),
\]
we obtain
\[
\frac{1+\lambda}{N_{12}(x+\lambda y)}
=
\frac1{N_{12}(z_*)}
=
\frac1d
=
5\sqrt3-7.
\]
This proves the claimed value.

## Verification
The bundled `verify.py` uses exact symbolic arithmetic in \(\mathbb Q(\sqrt3)\). It reconstructs the twelve facet normals and vertices, verifies the active-facet descriptions used in the Birkhoff--James reduction, checks all three dual certificates vertex by vertex, and verifies the equality configuration.

In particular, it certifies
\[
d(5\sqrt3-7)=1,
\]
the exact equality
\[
N_{12}(z_*)=d,
\]
and
\[
\lambda=3-\sqrt3.
\]
No floating-point search is used as proof.

## Relationship to prior work
Baronti, Casini and Papini revisit the rectangular constant and its generalized forms, give general bounds and Hilbert/uniform-nonsquareness characterizations, and characterize the two-dimensional regular-hexagonal case. Their full open-access article defines
\[
\mu(X)
\]
in exactly the normalization used here and records
\[
\mu_p(X)=2^{1/p}
\]
for the regular hexagonal norm. The inspected full text contains no regular-dodecagonal computation.

A 2024 paper by Xie, Fu and Li introduces further generalized rectangular constants and, in the accessible abstract, develops general bounds and estimates on \(\ell_p\). Its full text was not publicly available in the checked route, so it is retained as a bibliographic residual risk rather than treated as a negative full-text comparison.

The present calculation differs structurally from the hexagonal case: regular dodecagonal Birkhoff--James orthogonality has both edge-interior and vertex strata, and the global lower envelope is certified by three distinct polygonal regions. The exact value is not implied by the general inequalities in the inspected defining paper.

## Limitations
The result is specific to the regular dodecagonal plane. It does not give a closed formula for the rectangular constant of every regular polygon, nor does it classify every maximizing triple.

The literature search cannot establish absolute uniqueness. A calculation under another affine normalization or in an inaccessible generalized-rectangular-constant source could duplicate the value; no such statement was found in the inspected primary full text, accessible later abstract, public semantic index, or the available prior research ledger.

## References
1. M. Baronti, E. Casini and P. L. Papini, “Revisiting the rectangular constant in Banach spaces,” *Bulletin of the Australian Mathematical Society* 105 (2022), 124–133, doi:10.1017/S0004972721000253. First published online 26 April 2021; primary MSC 46B20.
2. H. Xie, Y. Fu and Y. Li, “Generalized rectangular constant in Banach spaces,” *Analysis Mathematica* 50 (2024), 667–681, doi:10.1007/s10476-024-00034-9.
