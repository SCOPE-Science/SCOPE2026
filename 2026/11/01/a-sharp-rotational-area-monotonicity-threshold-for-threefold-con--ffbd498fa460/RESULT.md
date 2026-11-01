# A sharp rotational-area monotonicity threshold for threefold constant-width ovals

## Finding

For real \(a,b\), and nonzero real \(\varepsilon\) satisfying \(|\varepsilon|(8|a|+80|b|)<1\), define the smooth strictly convex planar body \(K\) by its support function
\[
h(\phi)=1+\varepsilon\bigl(a\cos(3\phi)+b\cos(9\phi)\bigr).
\]
It has constant width \(2\) and dihedral threefold symmetry. Let \(R_\theta\) be planar rotation by \(\theta\), and set \(M_\theta=(K+R_\theta K)/2\). Its exact area, on the natural fundamental interval \(0\le\theta\le\pi/3\), is
\[
A(\theta)=\pi-\frac{\pi\varepsilon^2}{2}\left(8a^2\cos^2\frac{3\theta}{2}+80b^2\cos^2\frac{9\theta}{2}\right).
\]
The area increases strictly throughout this interval **if and only if** \(a^2\ge30b^2\). If \(a^2<30b^2\), it has exactly two interior stationary points, a strict local maximum followed by a strict local minimum:
\[
\theta_-=\frac13\arcsin\sqrt{\frac{a^2+90b^2}{120b^2}},\qquad
\theta_+=\frac\pi3-\theta_-.
\]
It strictly increases on \((0,\theta_-)\), decreases on \((\theta_-,\theta_+)\), and increases on \((\theta_+,\pi/3)\). These formulas include \(a=0\), \(b\ne0\), but the all-zero pair is excluded because it gives the disk and a constant area profile. The endpoint \(A(\pi/3)=\pi\) is globally maximal, since the Minkowski mean is the radius-one disk. For all parameters the complementary-angle identity holds:
\[
A(\theta)+A(\pi/3-\theta)=A(0)+\pi.
\]
In particular the strictly convex oval \(h(\phi)=1+\frac1{100}(\cos3\phi+\cos9\phi)\) is a concrete threefold-symmetric constant-width counterexample to monotonic growth of rotational-Minkowski-average area, despite the known monotonicity of the Reuleaux triangle.

## Assumptions and scope

All bodies lie in the Euclidean plane. The support function is taken about the dihedral symmetry center. The curvature radius \(h+h''=1-\varepsilon(8a\cos3\phi+80b\cos9\phi)\) is strictly positive by hypothesis, so the support function indeed defines a smooth, strictly convex body. Its antipodal sum is identically \(2\), giving constant width \(2\). The first two admissible nontrivial odd Fourier harmonics consistent with dihedral threefold symmetry are degrees \(3\) and \(9\). Normalizations and angular interval are exact; scaling the width rescales every area by the square of the width ratio.

## Proof

For a smooth strictly convex planar body with support function \(p\), the exact Euclidean area identity is
\[
\operatorname{area}(K_p)=\frac12\int_0^{2\pi}(p(\phi)^2-p'(\phi)^2)\,d\phi.
\]
The support function of \(M_\theta\) is the arithmetic mean \(p_\theta(\phi)=[h(\phi)+h(\phi-\theta)]/2\). Its harmonic of degree \(j\) has squared amplitude \(\varepsilon^2c_j^2\cos^2(j\theta/2)\). Orthogonality of the two distinct modes gives the claimed area formula because \(\int_0^{2\pi}(\cos^2 j\phi-j^2\sin^2 j\phi)\,d\phi=\pi(1-j^2)\).

Differentiation yields the exact factorization
\[
A'(\theta)=6\pi\varepsilon^2\sin(3\theta)
\left[a^2+90b^2-120b^2\sin^2(3\theta)\right],\qquad 0<\theta<\pi/3.
\]
The first factor is strictly positive. The bracket is minimized at \(\theta=\pi/6\) with value \(a^2-30b^2\). Hence it is nonnegative everywhere exactly when \(a^2\ge30b^2\); equality yields a single isolated zero of the derivative, so the area remains strictly increasing. If \(a^2<30b^2\), necessarily \(b\ne0\), and the bracket vanishes at exactly two angles given by the displayed formula. Since its sign is positive, negative, positive across those angles, the complete monotonicity classification follows. At the endpoint, \(\cos(3\pi/6)=\cos(9\pi/6)=0\), so \(M_{\pi/3}\) is exactly the unit disk. Finally, for each of the two frequencies, \(j\pi/3\) is an odd multiple of \(\pi\); thus \(\cos^2(j(\pi/3-\theta)/2)=1-\cos^2(j\theta/2)\), giving the complementary-angle formula.

## Verification

Run `python verify.py` using standard Python 3. The bundled verifier passed 3,618 independently evaluated numerical checks, including direct support-function area integration rather than reliance on the displayed closed formula, strict convexity and constant width, complementary-angle symmetry, the derivative factorization, and test parameters on both sides of the exact threshold. These finite checks corroborate the analytic identity and classification; the proof handles all real parameters subject to the hypothesis.

## Relationship to prior work

Falcó and Myroshnychenko, arXiv:2608.05125 (2026-08-05), classify minimum-area constant-width bodies under dihedral symmetries. This motivates studying area behavior under an additional rotational Minkowski averaging operation while retaining those symmetries; their extrema classification does not state this rotation threshold. A previously reported exact area profile of a Reuleaux triangle and a rotated copy establishes strict increase up to its half-symmetry angle. The present result shows that that attractive monotonicity does **not** extend to all smooth threefold-symmetric constant-width bodies, and determines the sharp threshold for the first two admissible Fourier modes. A separate analysis of static two-harmonic area minima uses the same Fourier family but does not, in its retrieved theorem statement, classify rotational monotonicity or the two interior critical angles. All harmonic support-function area identities used here are classical.

## Limitations

The threshold \(a^2=30b^2\) concerns the two-frequency family, not arbitrary constant-width bodies or arbitrary Fourier supports. The smallness hypothesis is sufficient for positive curvature, not necessary for convexity. The counterexample refutes only monotonicity of area along rotations, not the disk's global area-maximizing property. Search cannot establish historical uniqueness, especially for earlier literature on mixed areas of Fourier support functions; independent mathematical audit is not performed.

## References

1. J. Falcó and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width*, arXiv:2608.05125, first public 2026-08-05, https://arxiv.org/abs/2608.05125.
2. *Exact rotational Minkowski-average area profile of the Reuleaux triangle*, mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-rotational-minkowski-average-area-profile-of-the-reuleaux--53c190e0340e.
3. *Sharp two-harmonic area minimum for dihedrally invariant constant-width bodies*, mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-two-harmonic-area-minimum-for-dihedrally-invariant-constan--0094d4f2c8a9.
