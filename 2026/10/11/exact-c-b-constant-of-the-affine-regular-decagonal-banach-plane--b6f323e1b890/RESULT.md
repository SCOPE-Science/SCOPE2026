# Exact \(C_B\) constant of the affine-regular decagonal Banach plane
## Finding
Let \(X_{10}\) be the real Banach plane whose unit ball is an affine image of a Euclidean regular decagon. For the Du--Li constant
\[
C_B(X)
=
\sup\left\{
\frac{\|x+y\|^2-\|x-y\|^2}{4}:
x,y\in S_X,\ x\perp_B y
\right\},
\]
one has
\[
C_B(X_{10})
=
\frac{5\sqrt5-9}{8}.
\]

In the regular-decagon normalization below, equality is attained by
\[
x=
\left(1,\tan\frac{\pi}{10}\right),
\qquad
y=
\left(0,\sec\frac{\pi}{10}\right).
\]
For this pair,
\[
\|x+y\|=\frac{1+\sqrt5}{2},
\qquad
\|x-y\|=\sqrt5-1.
\]

## Assumptions and scope
All spaces are real. The constant \(C_B\) is the cosine-type Birkhoff-orthogonality constant introduced by Du and Li:
\[
C_B(X)
=
\sup\left\{
\frac{\|x+y\|^2-\|x-y\|^2}{4}:
x,y\in S_X,\ x\perp_B y
\right\}.
\]
The displayed expression is unchanged by linear isometries, so it is enough to use the Euclidean regular decagon circumscribed about the Euclidean unit disk.

Put
\[
\alpha=\frac{\pi}{10}.
\]
Let
\[
n_j=
\left(
\cos\frac{j\pi}{5},
\sin\frac{j\pi}{5}
\right),
\qquad
0\le j<10,
\]
and define
\[
\|z\|_{10}
=
\max_{0\le j<10}\langle n_j,z\rangle.
\]
The unit ball is the regular decagon with inradius \(1\). Its facet with outward normal \(n_0=(1,0)\) is
\[
E_0=
\{(1,t):-\tan\alpha\le t\le\tan\alpha\}.
\]
The vertical unit vertex is
\[
v=
(0,\sec\alpha).
\]

We use the standard support-functional characterization
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\text{there is a norming functional \(f\) for \(x\) with \(f(y)=0\)}.
\]

## Proof
Write
\[
F(x,y)
=
\frac{\|x+y\|_{10}^2-\|x-y\|_{10}^2}{4}.
\]
The expression \(F\) is symmetric in \(x,y\).

Consider first a point \(x\) in the relative interior of a facet. By a dihedral isometry of the regular decagon we may put
\[
x=(1,t),
\qquad
-\tan\alpha<t<\tan\alpha.
\]
Its unique norming functional is
\[
f(s,t)=s.
\]
Thus \(x\perp_B y\) forces \(y\) to lie on the kernel of \(f\). The two unit points on that line are
\[
y=\pm(0,\sec\alpha).
\]

Now let \(x\) be a vertex. Its norming functionals form the segment joining the two adjacent facet normals. Their kernels sweep exactly the directions of one decagonal facet. Because \(10=4\cdot2+2\), the normal of that swept facet is perpendicular to the original vertex direction; hence its norming functional annihilates \(x\). Thus every such \(y\) also satisfies \(y\perp_B x\). Since \(F(x,y)=F(y,x)\), every vertex-first Birkhoff pair, after swapping \(x\) and \(y\), is again of the facet--vertex form above. This directly exhibits the symmetry of Birkhoff orthogonality in the regular decagonal plane.

Consequently every value of \(F\) on a Birkhoff-orthogonal unit pair is, up to sign and dihedral symmetry, obtained from
\[
x=(1,t),
\qquad
-\tan\alpha\le t\le\tan\alpha,
\qquad
y=(0,\sec\alpha).
\tag{1}
\]

Put
\[
c=\cos\frac{\pi}{5},
\qquad
s=\sin\frac{\pi}{5},
\qquad
R=\sec\alpha.
\]
For the pair in (1), the direction of \(x+y\) ranges from \(2\alpha\) to \(3\alpha\), because
\[
R-\tan\alpha=\tan(2\alpha),
\qquad
R+\tan\alpha=\tan(3\alpha).
\]
Thus throughout the interval the active supporting facet for \(x+y\) may be taken to be \(n_1\), with a tie only at the endpoint \(3\alpha\). Similarly the active supporting facet for \(x-y\) may be taken to be \(n_9\). Therefore
\[
\|x+y\|_{10}
=
c+s(R+t),
\]
and
\[
\|x-y\|_{10}
=
c+s(R-t).
\]
It follows that
\[
F(x,y)
=
\frac{(c+sR+st)^2-(c+sR-st)^2}{4}
=
(c+sR)st.
\]
This is affine and increasing in \(t\), so its maximum occurs at
\[
t=\tan\alpha.
\]

At that endpoint,
\[
x=
\left(1,\tan\alpha\right),
\qquad
y=(0,\sec\alpha),
\]
and direct trigonometric simplification gives
\[
\|x+y\|_{10}
=
\frac{1+\sqrt5}{2},
\qquad
\|x-y\|_{10}
=
\sqrt5-1.
\]
Hence
\[
C_B(X_{10})
=
\frac14
\left[
\left(\frac{1+\sqrt5}{2}\right)^2
-
(\sqrt5-1)^2
\right]
=
\frac{5\sqrt5-9}{8}.
\]

## Verification
The bundled `verify.py` checks the proof-critical exact identities symbolically. It reconstructs the ten facet normals, verifies the endpoint directions of \(x+y\) and \(x-y\), checks that the claimed active facets dominate at both endpoints and therefore on the entire affine parameter interval, and simplifies the objective to a positive constant times \(t\).

It separately checks the two equality norms and the final radical
\[
\frac{5\sqrt5-9}{8}.
\]
The script also verifies the facet/vertex incidence underlying the Birkhoff-pair reduction for all ten dihedral copies. No finite sampling is used as a substitute for the continuum argument.

## Relationship to prior work
Du and Li introduced \(C_B(X)\) as a cosine-type measure of the discrepancy between Birkhoff and isosceles orthogonality. Their full paper proves
\[
0\le C_B(X)\le\frac34,
\]
relates \(C_B\) to the orthogonality-difference constant \(D(X)\), to \(A_2(X)\), and to other classical geometric constants, and characterizes the extremal Radon-plane value
\[
C_B(X)=\frac34
\]
by the affine-regular hexagonal unit sphere. The inspected article contains no decagonal computation.

Mizuguchi's earlier full paper proves
\[
A_2(X)\le\frac32
\]
for Radon planes and characterizes equality by the affine-regular hexagon. That result is part of the background used by Du and Li, but it does not determine \(C_B\) for a nonhexagonal Radon plane. In particular, its \(A_2\) bound is an inequality for a different two-vector objective and does not imply the exact decagonal value above.

Targeted searches under \(C_B\), the cosine-of-\(i\)-angle formulation, Radon-plane terminology, affine-regular-decagon terminology, the exact radical, and the related \(D(X)\) formulation found no statement covering the displayed value. The closest public decagon results concern Banach--Mazur distance and other geometric constants.

## Limitations
The theorem computes \(C_B\) only for the affine-regular decagonal plane. It does not give a closed formula for every regular \(4n+2\)-gonal Radon plane and does not classify all maximizing Birkhoff pairs.

The proof uses the special facet/vertex incidence of the regular decagon. Bibliographic and semantic searches cannot establish absolute novelty, so an equivalent computation under a different affine normalization or under the cosine-of-\(i\)-angle notation remains a residual literature risk.

## References
1. D. Du and Y. Li, “Some Geometric Constants Related to the Sine Function and Cosine Function in Banach Spaces,” Vietnam Journal of Mathematics 54, 1–17, doi:10.1007/s10013-024-00696-w. Published online 14 June 2024. Mathematics Subject Classification: 46B20.
2. H. Mizuguchi, “The von Neumann–Jordan and another constants in Radon planes,” Monatshefte für Mathematik 195 (2021), 307–322, doi:10.1007/s00605-021-01540-w. Published online 3 March 2021.
