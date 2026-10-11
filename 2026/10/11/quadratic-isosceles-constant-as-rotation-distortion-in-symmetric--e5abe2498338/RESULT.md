# Quadratic isosceles constant as rotation distortion in symmetric planes
## Finding
Let \(X\) be a real symmetric Minkowski plane with a pair of unit axes \(e_1,e_2\). Declare \(e_1,e_2\) Euclidean-orthonormal and let \(Q_\theta\) be the corresponding coordinate rotation through \(\theta\).

For the Baronti–Bertella quadratic isosceles constant
\[
H_2(X)=
\sup\left\{
\frac{\sqrt{1+\lambda^2}}{\|x+\lambda y\|}:
x,y\in S_X,\ x\perp_I y,\ \lambda\ge0
\right\},
\]
one has the structural identity
\[
H_2(X)=\sup_{0\le\theta\le\pi/4}\|Q_\theta\|_{X\to X}.
\]

Consequently, if the unit circle is an affine regular \(4n\)-gon, \(n\ge1\), then
\[
H_2(X)=\sec\left(\frac{\pi}{4n}\right).
\]
For the regular octagon,
\[
H_2(X_8)=\sec\left(\frac{\pi}{8}\right)
=\sqrt{4-2\sqrt2}.
\]

## Assumptions and scope
All spaces and scalars are real. Isosceles orthogonality means
\[
x\perp_I y
\quad\Longleftrightarrow\quad
\|x+y\|=\|x-y\|.
\]
A symmetric Minkowski plane is used in the standard sense of Balestro–Martini–Teixeira: it has a pair of axes \(e_1,e_2\in S_X\) for which coordinate sign changes and coordinate interchange preserve the norm.

The affine-regular polygon statement is invariant under linear isometry, so its proof may normalize the unit circle to the usual Euclidean regular \(4n\)-gon circumscribed about the Euclidean unit circle.

## Proof
A theorem of Balestro, Martini and Teixeira states that in a symmetric Minkowski plane every unit isosceles-orthogonal pair is, up to sign,
\[
x=\alpha e_1+\beta e_2,
\qquad
y=\beta e_1-\alpha e_2.
\]
If \(R\) is quarter-turn in these coordinates, this says \(y=\pm Rx\).

Baronti and Bertella prove that the parameter in the definition of \(H_p\) may be reduced to \(0<\lambda\le1\) after interchanging the ordered pair. Put
\[
\lambda=\tan\theta,
\qquad
0\le\theta\le\frac{\pi}{4}.
\]
For \(y=Rx\),
\[
x+\lambda y
=
x+\tan\theta\,Rx
=
\sec\theta\,Q_\theta x.
\]
Hence
\[
\frac{\sqrt{1+\lambda^2}}{\|x+\lambda y\|}
=
\frac1{\|Q_\theta x\|}.
\]
Taking the supremum over \(x\in S_X\) gives
\[
\sup_{x\in S_X}\frac1{\|Q_\theta x\|}
=
\|Q_{-\theta}\|_{X\to X}.
\]
The choice \(y=-Rx\) yields the opposite rotation. Reflection in either axis is an isometry of a symmetric plane and conjugates \(Q_\theta\) to \(Q_{-\theta}\), so their operator norms agree. This proves
\[
H_2(X)=\sup_{0\le\theta\le\pi/4}\|Q_\theta\|_{X\to X}.
\]

Now suppose the unit circle is a regular \(4n\)-gon. Set
\[
a=\frac{\pi}{4n},
\qquad
\phi=2a=\frac{\pi}{2n}.
\]
With inradius normalized to \(1\), the supporting normals have angles in \(\phi\mathbb Z\). Every vertex has Euclidean radius \(\sec a\) and direction \(a+k\phi\).

For fixed \(\theta\), the convex function \(x\mapsto\|Q_\theta x\|\) attains its maximum on the polygon at a vertex. Rotational symmetry makes all vertex values equal. Thus, for a vertex \(v\) in direction \(a\),
\[
\|Q_\theta\|_{X\to X}
=
\|Q_\theta v\|
=
\frac{\cos d(\theta)}{\cos a},
\]
where
\[
d(\theta)
=
\operatorname{dist}\!\left(a+\theta,\phi\mathbb Z\right)
\]
is chosen in \([0,a]\). Therefore
\[
\|Q_\theta\|_{X\to X}\le\sec a.
\]
At \(\theta=a\), the rotated vertex lies on a supporting-normal direction, so \(d(a)=0\) and equality holds. Hence
\[
H_2(X)=\sec a
=
\sec\left(\frac{\pi}{4n}\right).
\]

Sharpness can also be read directly from the axes. With
\[
x=e_1,\qquad y=e_2,\qquad \lambda=\tan a,
\]
the vector \(x+\lambda y\) is exactly a polygon vertex, so its norm is \(1\), while
\[
\sqrt{1+\lambda^2}=\sec a.
\]

## Verification
The proof is analytic and does not infer an infinite statement from finite sampling. The two non-elementary inputs were checked in their primary full texts: the definition and parameter-reduction proposition for \(H_p\), and the symmetric-plane classification of unit isosceles-orthogonal pairs.

The polygon step uses only the explicit support-normal description of a regular \(4n\)-gon. The operator norm is reduced to vertices by convexity; rotational symmetry makes one vertex representative sufficient; the remaining bound is the elementary inequality \(\cos d\le1\).

As a consistency check, \(n=1\) gives the square value \(\sqrt2\), \(n=2\) gives the regular-octagon value \(\sqrt{4-2\sqrt2}\), and the values decrease to the Hilbert value \(1\) as \(n\to\infty\).

## Relationship to prior work
Baronti and Bertella introduced \(H_p\), proved its basic symmetries and parameter reductions, and studied Hilbert and uniform-nonsquareness characterizations. Their inspected full text does not compute affine-regular polygonal planes.

Balestro, Martini and Teixeira had earlier proved the classification of isosceles-orthogonal pairs in symmetric Minkowski planes and computed several different trigonometric constants for affine regular \(4n\)-gons, including their \(D\), \(c_E\), and \(c_D\) constants. Their work predates the definition of \(H_p\) and does not state the rotation-distortion identity or the displayed \(H_2\) formula.

Published-record searches under \(H_2\), \(p\)-isosceles constant, symmetric Minkowski plane, affine regular \(4n\)-gon, regular octagon, and the exact secant formula found no statement implying this result. The closest same-invariant-family record concerns \(H_4\) on a specially constructed hexagonal plane, while several regular-octagon records concern different geometric constants.

## Limitations
The structural identity is proved only for symmetric Minkowski planes, where unit isosceles-orthogonal partners are controlled by the axis quarter-turn. The polygon formula is for affine regular \(4n\)-gons; it does not claim an analogous secant law for arbitrary centrally symmetric polygons.

The literature search cannot establish absolute novelty. A differently named equivalent formulation could exist outside the inspected sources. No independent audit has been performed.

## References
1. M. Baronti and V. Bertella, “A Generalization of the Isosceles Constant in Banach Spaces,” Mediterranean Journal of Mathematics 21 (2024), Article 113, doi:10.1007/s00009-024-02654-9. Published online 4 May 2024; primary MSC 46B20.
2. V. Balestro, H. Martini and R. Teixeira, “Optimal Constants in Normed Planes,” Journal of Convex Analysis 26 (2019), 89–104, doi:10.68381/jca26006. See Theorem 4.1 and the regular \(4n\)-gonal discussion in Section 4.
