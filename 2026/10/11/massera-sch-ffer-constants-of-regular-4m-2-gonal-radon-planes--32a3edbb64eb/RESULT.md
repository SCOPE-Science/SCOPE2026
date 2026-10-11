# Massera--Schäffer constants of regular \(4m+2\)-gonal Radon planes
## Finding
For every integer \(m\ge1\), set
\[
N=4m+2,
\qquad
\alpha=\frac{\pi}{N}.
\]
Let \(X_N\) be the real two-dimensional Banach space whose unit ball is the Euclidean regular \(N\)-gon circumscribed about the Euclidean unit disk.

For the Fu--Li Massera--Schäffer Birkhoff constant
\[
MS_B(X)
=
\sup
\left\{
\frac{\max\{\|x\|,\|y\|\}}{\|x-y\|}
\left\|
\frac{x}{\|x\|}-\frac{y}{\|y\|}
\right\|:
x,y\ne0,\ x\perp_B y
\right\},
\]
one has the exact formula
\[
MS_B(X_N)
=
\begin{cases}
2\sin\!\left(\dfrac{\pi}{4}+\dfrac{\alpha}{2}\right),
&N\equiv2\pmod8,
\\[7pt]
2\sec\alpha\,
\sin\!\left(\dfrac{\pi}{4}+\dfrac{\alpha}{2}\right),
&N\equiv6\pmod8.
\end{cases}
\]

Thus
\[
MS_B(X_6)=2,
\]
while the regular decagonal plane satisfies
\[
MS_B(X_{10})
=
2\sin\frac{3\pi}{10}
=
\frac{1+\sqrt5}{2}.
\]
Both residue classes tend to the Hilbert value:
\[
MS_B(X_N)\longrightarrow\sqrt2
\qquad(N\to\infty,\ N\equiv2\pmod4).
\]

## Assumptions and scope
All spaces are real. Birkhoff orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x+\lambda y\|\ge\|x\|
\quad\text{for every }\lambda\in\mathbb R.
\]

The regular \(N\)-gon is normalized to have Euclidean inradius \(1\). Its outward unit facet normals have directions
\[
2j\alpha,
\qquad
j\in\mathbb Z,
\]
and its vertices are
\[
v_j
=
R\bigl(\cos((2j+1)\alpha),\sin((2j+1)\alpha)\bigr),
\qquad
R=\sec\alpha.
\]
For a nonzero Euclidean vector of direction \(\theta\),
\[
\|z\|_{X_N}
=
\|z\|_2\cos d(\theta,2\alpha\mathbb Z),
\tag{1}
\]
where
\[
0\le d(\theta,2\alpha\mathbb Z)\le\alpha
\]
is the angular distance to the nearest facet-normal ray.

The polar unit ball is the regular \(N\)-gon with vertices on the facet-normal rays and Euclidean circumradius \(1\). Because
\[
\frac{\pi}{2}=(2m+1)\alpha,
\]
a quarter-turn sends the polar's even-multiple directions to the primal polygon's odd-multiple vertex directions. More precisely,
\[
Q_{\pi/2}(B_{X_N}^{\circ})=\cos\alpha\,B_{X_N}.
\]
By the standard planar polar characterization, \(X_N\) is a Radon plane.

Fu and Li prove that on a polyhedral Radon plane,
\[
MS_B(X)
=
\sup
\left\{
\|x-y\|:
x,y\in\operatorname{ext}(B_X),\ x\perp_B y
\right\}.
\tag{2}
\]
Hence only Birkhoff-orthogonal vertex pairs need to be analyzed.

## Proof
By rotational symmetry it is enough to fix
\[
x=v_0,
\qquad
\arg x=\alpha.
\]
The norming functionals at \(v_0\) are exactly the convex combinations of the adjacent facet functionals whose normal directions are
\[
0
\quad\text{and}\quad
2\alpha.
\]
For a vertex \(v_\ell\), the condition
\[
v_0\perp_B v_\ell
\]
holds exactly when some normal direction in the interval
\[
[0,2\alpha]
\]
is Euclidean-perpendicular to \(v_\ell\). Since
\[
\frac{\pi}{2}=(2m+1)\alpha,
\]
this gives, modulo the central symmetry of the polygon,
\[
\ell=m
\quad\text{or}\quad
\ell=m+1.
\]
Changing the sign of \(v_\ell\) preserves Birkhoff orthogonality, so the four possible orthogonal extreme directions reduce to two chord norms.

The first chord uses
\[
y=v_m,
\qquad
\arg y=\frac{\pi}{2}.
\]
Its Euclidean length is
\[
\|x-y\|_2
=
2R\sin\!\left(\frac{\pi}{4}-\frac{\alpha}{2}\right),
\]
and the difference vector has direction
\[
-m\alpha
\]
modulo \(\pi\). Hence, by (1),
\[
D_-
=
\|x-y\|_{X_N}
=
\begin{cases}
2\sec\alpha\,
\sin\!\left(\dfrac{\pi}{4}-\dfrac{\alpha}{2}\right),
&m\text{ even},
\\[7pt]
2\sin\!\left(\dfrac{\pi}{4}-\dfrac{\alpha}{2}\right),
&m\text{ odd}.
\end{cases}
\tag{3}
\]

The second chord may be taken with
\[
y=v_{m+1},
\qquad
\arg y=\frac{\pi}{2}+2\alpha.
\]
Its Euclidean length is
\[
\|x-y\|_2
=
2R\sin\!\left(\frac{\pi}{4}+\frac{\alpha}{2}\right),
\]
and the difference direction is
\[
-(m-1)\alpha
\]
modulo \(\pi\). Therefore
\[
D_+
=
\begin{cases}
2\sin\!\left(\dfrac{\pi}{4}+\dfrac{\alpha}{2}\right),
&m\text{ even},
\\[7pt]
2\sec\alpha\,
\sin\!\left(\dfrac{\pi}{4}+\dfrac{\alpha}{2}\right),
&m\text{ odd}.
\end{cases}
\tag{4}
\]
The opposite choices \(-v_m\) and \(-v_{m+1}\) produce the same two values.

If \(m\) is odd, (4) is plainly larger than (3). If \(m\) is even, it remains to compare
\[
2\sin\!\left(\frac{\pi}{4}+\frac{\alpha}{2}\right)
\]
with
\[
2\sec\alpha\,
\sin\!\left(\frac{\pi}{4}-\frac{\alpha}{2}\right).
\]
After multiplying by \(\cos\alpha\), the difference is
\[
\cos\alpha\,
\sin\!\left(\frac{\pi}{4}+\frac{\alpha}{2}\right)
-
\sin\!\left(\frac{\pi}{4}-\frac{\alpha}{2}\right)
=
\cos\!\left(\frac{\pi}{4}+\frac{\alpha}{2}\right)\sin\alpha
>
0.
\]
Thus \(D_+\) is always the larger chord.

Finally,
\[
m\text{ even}
\quad\Longleftrightarrow\quad
N\equiv2\pmod8,
\]
and
\[
m\text{ odd}
\quad\Longleftrightarrow\quad
N\equiv6\pmod8.
\]
Substituting \(D_+\) into the Fu--Li reduction (2) proves the formula.

## Verification
The bundled `verify.py` reconstructs the inradius-one regular polygon from its facet normals for every
\[
1\le m\le100.
\]
For each polygon it enumerates every ordered pair of vertices, detects Birkhoff orthogonality from the exact sign-change criterion on the two adjacent norming facets, and computes the largest orthogonal vertex distance numerically. It agrees with the displayed two-branch formula to high precision for all tested values.

The script also verifies the two canonical chord formulas separately and checks the closed values
\[
MS_B(X_6)=2
\]
and
\[
MS_B(X_{10})=\frac{1+\sqrt5}{2}.
\]

The computation is a reproducibility check only. Exhaustiveness for every \(N=4m+2\) follows analytically from the Fu--Li extreme-point theorem and the two possible orthogonal vertex indices established in the proof.

## Relationship to prior work
Fu and Li introduced \(MS_B(X)\) and proved
\[
\sqrt2\le MS_B(X)\le2.
\]
Their Section 4 studies Radon planes. Theorem 4.4 proves exactly the reduction used here: on any Radon plane the constant is the supremum of \(\|x-y\|\) over unit Birkhoff-orthogonal pairs, and on a polyhedral Radon plane the supremum can be restricted to extreme points. Their subsequent explicit calculation concerns the conjugate Day--James family \(\ell_p-\ell_q\), rather than regular \(4m+2\)-gonal planes.

The regular hexagon gives the endpoint value \(2\), consistent with already known hexagonal examples. The new content is the full infinite regular-\(4m+2\) family and its modulo-\(8\) split. The split is geometric: the longer admissible vertex chord alternates between a facet-normal ray and a vertex ray, changing the radial norm factor by \(\cos\alpha\).

Targeted public-research searches used the exact \(MS_B\) notation, the Massera--Schäffer name, regular-polygon and regular-decagon aliases, the golden-ratio decagonal specialization, and the two trigonometric branch formulas. No covering statement was found. The closest indexed regular-decagon result concerns Banach--Mazur distance, while the closest regular-polygon records concern unrelated invariants.

## Limitations
The result covers Euclidean regular polygons with
\[
N\equiv2\pmod4.
\]
It does not compute \(MS_B\) for regular polygons outside the Radon residue class, nor for arbitrary affine deformations of these polygons.

The formula gives the constant but does not classify every maximizing ordered pair beyond the dihedral orbit implied by the proof.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent formula under another regular-polygon normalization or under an antinorm/Radon-curve description remains a residual literature risk.

## References
1. J. Alonso, H. Martini and S. Wu, “Orthogonality Types in Normed Linear Spaces,” in *Surveys in Geometry I*, pp. 97–170, Springer, 2022, doi:10.1007/978-3-030-86695-2_4. Public date: 18 November 2022.
2. Y. Fu and Y. Li, “The Massera-Schäffer inequality related to Birkhoff orthogonality in Banach spaces,” *Filomat* 38 (2024), no. 15, 5247–5259, doi:10.2298/FIL2415247F. Primary MSC 46B20.
