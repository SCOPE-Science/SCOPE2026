# Largest-axis multiplicity determines long-chord tails of ellipsoids

## Finding
For every centered ellipsoid in Euclidean dimension \(d\ge2\), the near-diameter tail of its motion-invariant random affine-line chord law has an exponent that records the multiplicity of the longest semiaxis. In particular, if precisely \(k\) semiaxes attain the maximum \(a\), then
\[
\Pr\{L>2a(1-\varepsilon)\}\sim C_{d,k}(a_1,\ldots,a_d)\,\varepsilon^{(2d-k-1)/2},\qquad \varepsilon\downarrow0,
\]
with an explicit positive coefficient described below. This distinguishes triaxial and prolate three-dimensional ellipsoids (exponent \(2\)), oblate spheroids (exponent \(3/2\)), and spheres (exponent \(1\)), under the stated line-selection convention.

More strongly, the entire chord survival function has the exact sphere integral
\[
\Pr(L>t)=\frac1H\int_{S^{d-1}}\sqrt{Q(u)}\bigl(1-t^2Q(u)/4\bigr)_+^{(d-1)/2}\,d\sigma(u),\qquad 0\le t\le2a,
\]
where \(Q(u)=\sum_{i=1}^d u_i^2/a_i^2\), \(H=\int_{S^{d-1}}\sqrt{Q(u)}\,d\sigma(u)\), and \(d\sigma\) denotes *unnormalized* spherical surface measure.

## Assumptions and scope
Fix an integer \(d\ge2\) and positive semiaxes arranged as
\[
a_1=\cdots=a_k=a>a_{k+1}\ge\cdots\ge a_d>0
\]
for some \(1\le k<d\), or take \(k=d\) and all axes equal to \(a\). Let \(E=\{x:\sum_i x_i^2/a_i^2\le1\}\). An unoriented affine line is sampled from its Euclidean-motion-invariant measure, conditioned on meeting \(E\): for a direction \(u\) and its perpendicular displacement \(p\), the measure is spherical surface measure in \(u\) times Lebesgue measure in \(u^\perp\). Both \(u\) and \(-u\) represent the same geometric line; the factor of two cancels in every probability. In particular, uniform orientation conditional on intersection is *not* the correct distribution for nonspherical ellipsoids. Let \(L\) denote the full Euclidean chord length.

Write \(p=d-k\), \(\alpha=(2d-k-1)/2\), and \(\beta_j=a^2/a_j^2-1>0\) for \(j>k\). The sharp constant is
\[
C_{d,k}=\frac{|S^{k-1}|\,\pi^{p/2}\,\Gamma((d+1)/2)\,2^\alpha}
{aH\,\Gamma((2d-k+1)/2)}\prod_{j=k+1}^d\beta_j^{-1/2},
\]
using \(|S^{k-1}|=2\pi^{k/2}/\Gamma(k/2)\). If \(p=0\) the empty product equals one and the formula reduces to the sphere constant \(2^{(d-1)/2}\).

## Proof
Let \(A=\operatorname{diag}(a_1^{-2},\ldots,a_d^{-2})\). For a fixed unit direction \(u\), write points on a line as \(p+su\), where \(p\in u^\perp\). Completing the square gives
\[
(p+su)^TA(p+su)=Q(u)\left(s+\frac{u^TAp}{Q(u)}\right)^2+p^T\left(A-\frac{Auu^TA}{Q(u)}\right)p.
\]
The second quadratic form, restricted to \(u^\perp\), is positive definite, with determinant \(\det(A)/Q(u)\), by the Schur-complement determinant identity. The orthogonal projection of \(E\) to \(u^\perp\) therefore has \((d-1)\)-dimensional volume
\[
\kappa_{d-1}\left(\prod_i a_i\right)\sqrt{Q(u)}.
\]
For a uniformly selected translation inside this projected ellipsoid, the squared normalized radial coordinate \(R^2\) has distribution \(\Pr(R^2\le s)=s^{(d-1)/2}\) on \([0,1]\), since homothetic volumes scale by the \((d-1)\)-st power. The corresponding chord has length \(2\sqrt{1-R^2}/\sqrt{Q(u)}\). Weighting directions by the above projected volume, then integrating the translation variable, proves the exact survival function, including all normalization factors.

Assume \(k<d\). Around the set of maximum-length directions, parametrize the sphere by \(u=(\sqrt{1-\|z\|^2}\,v,z)\), with \(v\in S^{k-1}\), \(z\in\mathbb R^p\) and \(\|z\|<1\). Its surface element is
\[
d\sigma(u)=(1-\|z\|^2)^{(k-2)/2}\,d\sigma(v)\,dz.
\]
The crucial relation is *exact*:
\[
a^2Q(u)=1+\sum_{j=k+1}^d\beta_j z_j^2.
\]
Substitute \(t=2a(1-\varepsilon)\). Positive contributions require \(\sum_j\beta_jz_j^2<(1-\varepsilon)^{-2}-1\), so \(z_j=O(\sqrt\varepsilon)\) uniformly. Rescale \(z_j=\sqrt{2\varepsilon/\beta_j}\,y_j\). On the limiting Euclidean unit ball, the positive-part term divided by \((2\varepsilon)^{(d-1)/2}\) converges to \((1-\|y\|^2)_+^{(d-1)/2}\); the remaining smooth factors converge to \(1/a\). The rescaled domains are uniformly bounded, and the integrand admits an integrable uniform majorant, so dominated convergence applies. Since
\[
\int_{\|y\|<1}(1-\|y\|^2)^{(d-1)/2}\,dy
=\frac{\pi^{p/2}\Gamma((d+1)/2)}{\Gamma((p+d+1)/2)},
\]
the rescaled integral gives exactly \(C_{d,k}\varepsilon^{p/2+(d-1)/2}\), and \(p/2+(d-1)/2=(2d-k-1)/2\).

If \(k=d\), then \(Q(u)=a^{-2}\) for every direction, hence the exact tail is \(\bigl(1-t^2/(4a^2)\bigr)^{(d-1)/2}\). At \(t=2a(1-\varepsilon)\), this becomes \((2\varepsilon-\varepsilon^2)^{(d-1)/2}\), verifying the claimed sphere endpoint and constant without a limiting-coordinate argument.

## Verification
The included standalone `check_ellipsoid_chord_tails.py` runs with Python 3, NumPy, and SciPy. It compares independent spherical quadratures with endpoint constants at several small thresholds for four distinct three-dimensional axis-multiplicity patterns, and separately samples real affine lines from the motion-invariant line ensemble and directly intersects those lines with the ellipsoid quadratic equation. Passing numerical checks are not substitutes for the exact proof or a test of every dimension.

## Relationship to prior work
Gečiauskas (1967) develops general relations between chord and point-distance distributions in planar and spatial convex figures. Suwa (1977) studies ellipsoids probed by random test lines in stereological size-distribution estimation; its displayed density concerns a shape/size model and does not give an endpoint law resolved by maximal-axis multiplicity. Agimelen and collaborators (2014) derive optical chord-length distribution models from two-dimensional ellipsoidal projections, rather than a Haar/invariant-line law on three-dimensional ellipsoids. Related modern mathematical records treat random *central sections*, ellipsoid axis reconstruction from section volumes, or lengths of *center-passing* chords; these laws have different sampling measures. None of the inspected statements yields the explicit all-dimensional eigenvalue-multiplicity exponent and coefficient under the measure defined here. This absence is a comparison of reviewed statements, not proof of historical novelty.

## Limitations
The result is conditional on intersection under invariant affine-line measure; changing the rule to isotropic directions followed by a different translation law changes the distribution. The asymptotic is for a fixed nondegenerate ellipsoid and is not uniform as distinct semiaxes coalesce, where the exponent changes. Numerical checks sample only three dimensions. Some older chord-distribution literature was not available in full, so definitive priority remains open. Independent mathematical validation has not been conducted.

## References
- E. Gečiauskas, “The distribution function of the chord length of oval and ovaloid and its relation to distribution of a distance in an oval and ovaloid” (1967), Lithuanian Mathematical Journal, DOI: `10.15388/LMJ.1967.19983`.
- N. Suwa, “Estimation of the Distribution of Ellipsoids with Random Test Lines” (1977), Tohoku Journal of Experimental Medicine 121, 365–370, DOI: `10.1620/tjem.121.365`.
- I. F. Agimelen et al., “Estimation of Particle Size Distribution and Aspect Ratio of Non-Spherical Particles From Chord Length Distribution” (2014), `arXiv:1408.4399`.
- R. Coleman, “Random paths through convex bodies” (1969), DOI: `10.2307/3212012` (abstract inspected).
