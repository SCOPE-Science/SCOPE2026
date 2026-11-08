# Exact brightness profile of the cubic threefold-projection exception

## Finding

Let \(K_\varepsilon\subset\mathbb R^3\) have support function
\[
h_\varepsilon(u)=1+\varepsilon u_1u_2u_3,\qquad u\in S^2,
\]
for any real \(\varepsilon\) for which this is a convex-body support function. For every unit normal \(n=(n_1,n_2,n_3)\), the ordinary two-dimensional area of its orthogonal shadow satisfies
\[
b_{K_\varepsilon}(n)=\operatorname{area}_2(K_\varepsilon\mid n^\perp)
=\pi-\frac{\pi\varepsilon^2}{4}\prod_{i=1}^{3}(1-n_i^2).
\]
In particular,
\[
\pi\left(1-\frac{2\varepsilon^2}{27}\right)\le b_{K_\varepsilon}(n)\le\pi.
\]
**For \(\varepsilon\ne0\)** the upper endpoint occurs exactly at the six coordinate-axis normals (three unoriented projection planes), whose shadows are unit disks; the lower endpoint occurs exactly when \(|n_1|=|n_2|=|n_3|=1/\sqrt3\) (four unoriented body-diagonal planes). **For \(\varepsilon=0\)**, \(K_0\) is the unit ball and \(b_{K_0}(n)=\pi\) for *every* normal; no direction is an exclusive maximizer or minimizer. The formula and inequalities include this degenerate case.

## Assumptions and scope

The normal \(n\) is a unit vector and opposite normals identify the same plane. The sole parameter condition is that \(h_\varepsilon\) be a support function; sufficiently small \(|\varepsilon|\) are admissible by Myroshnychenko--Ryabogin--Saroglou, and the exact convexity range has been treated separately in published work on the cubic family. This statement does not assert or reprove that range. For nonzero admissible \(\varepsilon\), the body is the non-spherical constant-width cubic exception with threefold-symmetric planar projections up to translation. For zero parameter it is the sphere. Projection area is Euclidean, not a section area.

## Proof

Fix \(n\in S^2\) and an oriented orthonormal basis \(e_1,e_2\) of \(n^\perp\). Parametrize the unit circle of the plane by
\[
u(\theta)=e_1\cos\theta+e_2\sin\theta.
\]
The cubic \(H(u)=u_1u_2u_3\) restricts to a homogeneous cubic in \(\cos\theta,\sin\theta\), so the only Fourier frequencies are 1 and 3. Set \(z=e_1-i e_2\). The identity
\[
u(\theta)=\tfrac12(ze^{i\theta}+\overline z e^{-i\theta})
\]
shows that the coefficient of \(e^{3i\theta}\) in \(H(u(\theta))\) is \(z_1z_2z_3/8\). Hence, writing the third harmonic as \(C\cos3\theta+D\sin3\theta\), we obtain
\[
R^2:=C^2+D^2=\frac1{16}|z_1z_2z_3|^2
=\frac1{16}\prod_{i=1}^3(1-n_i^2),
\]
because orthonormality of \((e_1,e_2,n)\) implies \(|z_i|^2=e_{1,i}^2+e_{2,i}^2=1-n_i^2\).

The first Fourier harmonic is precisely a translation of the planar support function and contributes no area. After translating, the support is \(p(\theta)=1+\varepsilon R\cos(3\theta-\phi)\) for a suitable phase \(\phi\) (when \(R=0\), the phase is irrelevant). The planar support-function area identity gives
\[
\begin{aligned}
\operatorname{area}_2(K_\varepsilon\mid n^\perp)
&=\frac12\int_0^{2\pi}\left(p(\theta)^2-p'(\theta)^2\right)d\theta\\
&=\pi-4\pi\varepsilon^2R^2
=\pi-\frac{\pi\varepsilon^2}{4}\prod_{i=1}^3(1-n_i^2).
\end{aligned}
\]
The identity holds for the convex support under the stated assumption, including at possible curvature-degenerate parameter endpoints.

To classify extrema, put \(a_i=n_i^2\ge0\), with \(a_1+a_2+a_3=1\). Then
\[
0\le \prod_{i=1}^3(1-a_i)
\le \left(\frac{\sum_i(1-a_i)}3\right)^3
=\frac8{27}.
\]
The upper product bound is an equality exactly for \(a_1=a_2=a_3=1/3\); the product is zero exactly if one \(a_i=1\), forcing \(n\) onto a coordinate axis. If \(\varepsilon\ne0\), multiplication by the strictly negative coefficient \(-\pi\varepsilon^2/4\) makes these exactly the indicated brightness extrema. Along a coordinate normal, the cubic vanishes on the projection plane, and the projection support is exactly 1, so its shadow is a unit disk. If \(\varepsilon=0\), the coefficient vanishes instead: the entire brightness function equals \(\pi\), and every normal attains both bounds. This last distinction is necessary; without it the asserted uniqueness of extremizers would be false.

## Verification and limitations

The checked finite symbolic examples include normal vectors \((0,0,1)\), \((1,1,1)/\sqrt3\) and \((1,2,2)/3\), with third-harmonic squared amplitudes \(0\), \(1/54\) and \(25/1458\), respectively. These are consistency checks, not proofs for all normals. The universal result follows from the Fourier coefficient calculation above. The \(\varepsilon=0\) case is verified directly as the unit ball.

The theorem is specific to the canonical cubic family and its fixed coordinate axes; it neither characterizes all threefold-projection exceptions nor proves a general brightness-reconstruction theorem or stability theorem. No sharp convexity interval is newly claimed.

## Relationship to prior work

Myroshnychenko--Ryabogin--Saroglou identify the cubic exception and prove its great-circle first/third-mode restriction and threefold projection symmetry, but their exceptional-case argument does not compute the directionwise third-harmonic amplitude or shadow area. The separately published sharp convexity-threshold result treats support-function admissibility, not brightness. General brightness/lightness theory and averaged constant-width identities do not state this coordinate-product profile. A separately published axially symmetric cubic brightness formula concerns a different spherical harmonic and has a different directional invariant. The public indexed record of this same finding is its own dissemination record, not independent preexisting prior art.

## References

1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1 (2026), particularly Proposition 5.1 and Theorem 5.4.
2. S. Campi, R. J. Gardner, P. Gronchi, M. Kiderlen, *Lightness functions*, Advances in Mathematics 231 (2012), 3118--3146, DOI 10.1016/j.aim.2012.08.015.
3. M. Zwierzyński, *Mixed Volumes, the Wigner Caustic, and Isoperimetric Inequalities*, arXiv:2608.11068v1 (2026).
