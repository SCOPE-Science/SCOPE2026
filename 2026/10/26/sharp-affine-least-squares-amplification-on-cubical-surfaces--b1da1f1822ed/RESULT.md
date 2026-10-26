# Sharp affine least-squares amplification on cubical surfaces

## Finding
For every integer \(d\ge 2\), give the boundary \(\partial Q_d\) of \(Q_d=[-1,1]^d\) normalized \((d-1)\)-dimensional surface measure \(\sigma_d\). Let \(P_d:L^2(\sigma_d)\to\operatorname{span}\{1,y_1,\ldots,y_d\}\) be orthogonal projection, considered on both endpoint spaces by its integral kernel. Put
\[
c_d=\frac{3d}{d+2},\qquad a_d=\frac{d+2}{3d},\qquad k=d-1.
\]
For integers \(k\ge1\) and rational \(t\ge0\), define the finite expression
\[
H_k(t)=t+\frac{4}{(k+1)!}\sum_{j=0}^{\lfloor(k-t)/2\rfloor}(-1)^j\binom{k}{j}\left(\frac{k-t}{2}-j\right)^{k+1},
\]
where an upper summation bound below zero means an empty sum. Then the exact sharp norms are
\[
\boxed{\|P_d\|_{L^\infty\to L^\infty}=\|P_d\|_{L^1\to L^1}
=\frac{c_d}{2}\left[H_{d-1}(1+a_d)+H_{d-1}(1-a_d)\right].}
\]
In particular, the norms are rational for every integer \(d\), and \(\|P_2\|=5/3\), \(\|P_3\|=94/45\). All vertices are maximizing evaluation points; a sign-valued bounded input attains the endpoint norm.

The sharp high-dimensional expansion is
\[
\boxed{\|P_d\|=\sqrt{\frac{6d}{\pi}}\left(1-\frac{47}{60d}+O(d^{-2})\right).}
\]
For comparison, let \(V_d\) be affine \(L^2\) projection with **normalized volume measure** on the filled cube \(Q_d\). Independent computation gives
\[
\|V_d\|=\sqrt{\frac{6d}{\pi}}\left(1+\frac{13}{60d}+O(d^{-2})\right),\qquad
\boxed{\|V_d\|-\|P_d\|=\sqrt{\frac{6}{\pi d}}+O(d^{-3/2}).}
\]
Thus normalized surface sampling is asymptotically less amplifying than volume sampling at an explicit, nonzero first comparison order. No pointwise-in-dimension sign comparison is asserted in the theorem.

## Assumptions and scope
The cube has unit half-side length; affine rescaling of the whole cube does not affect the norm. The measure is normalized Euclidean **facet surface area**, not volume measure, uniform vertex measure, or a product measure. The norm acts on real or complex \(L^1\) and \(L^\infty\), and all \(d\ge2\) are covered. The finite-expression evaluation and the asymptotic comparison are both exact mathematical statements, not numerical fits.

## Proof
**Kernel and maximizing evaluations.** Sampling \(Y\sim\sigma_d\) is equivalent to selecting a coordinate uniformly among \(d\), pinning it to a symmetric sign \(\varepsilon\in\{-1,1\}\), and sampling the other \(d-1\) coordinates independently uniformly on \([-1,1]\). Symmetry gives \(\mathbb EY_i=0\), \(\mathbb EY_iY_j=0\) for distinct indices and
\[
\mathbb EY_i^2=\frac1d+\frac{d-1}{3d}=\frac{d+2}{3d}.
\]
Therefore the orthogonal-projection kernel is
\[
K_d(x,y)=1+c_d\sum_{i=1}^d x_i y_i.
\]
The absolute-kernel integral \(F_d(x)=\int|K_d(x,y)|\,d\sigma_d(y)\) is convex in \(x\). Every point of \(Q_d\) is a convex combination of vertices, so \(F_d(x)\le\max_{v\in\{-1,1\}^d}F_d(v)\). Invariance under coordinate sign changes makes all vertex values equal. Although vertices have zero surface measure, they are approached by positive-measure patches on facets, so their values give the essential supremum. The input \(f(y)=\operatorname{sgn}K_d(v,y)\) realizes that value (and its complex analogue does also). Self-adjointness and kernel symmetry give equality of \(L^1\) and \(L^\infty\) norms.

**Exact evaluation.** With \(U_i\) independent uniform \([-1,1]\), let \(S_k=\sum_{i=1}^k U_i\), independent of \(\varepsilon\). The maximizing kernel has law \(1+c_d(S_{d-1}+\varepsilon)\), so
\[
\|P_d\|=\frac{c_d}{2}\left(\mathbb E|S_k+1+a_d|+\mathbb E|S_k+1-a_d|\right).
\]
Both shifts are nonnegative. For any \(t\ge0\), put \(T=\sum_{i=1}^k (U_i+1)/2\), a sum of \(k\) independent uniform \([0,1]\) variables, and \(b=(k-t)/2\). The identity \(|z|=z+2(-z)_+\), combined with the Irwin--Hall truncated-power distribution function, gives
\[
\mathbb E|S_k+t|=t+4\mathbb E(b-T)_+
=t+\frac4{(k+1)!}\sum_{j=0}^{\lfloor b\rfloor}(-1)^j\binom{k}{j}(b-j)^{k+1}=H_k(t).
\]
This proves the closed finite formula, with the empty-sum convention when \(b<0\). The displayed rational benchmarks follow by substitution.

**Asymptotics of sums of uniforms.** The centered uniform variable has characteristic function \(\sin z/z\), with
\[
\log\frac{\sin z}{z}=-\frac{z^2}{6}-\frac{z^4}{180}+O(z^6).
\]
Fourier inversion and the identity \(\mathbb E|X|=(2/\pi)\int_0^\infty(1-\Re\varphi_X(t))t^{-2}\,dt\) yield, for \(k\to\infty\),
\[
\mathbb E|S_k|=\sqrt{\frac{2k}{3\pi}}\left(1+\frac{1}{20k}+O(k^{-2})\right),\qquad
\sup_{|s|\le2} \left|f_k(s)-\sqrt{\frac{3}{2\pi k}}\right|=O(k^{-3/2}),
\]
where \(f_k\) is the density of \(S_k\) (the density estimate is for \(k\ge2\)). For completeness, these error bounds follow by scaling \(z\) by \(k^{-1/2}\), expanding the logarithm on \(|z|\le k^{1/10}\), integrating polynomially weighted Gaussian errors, and bounding the complement with \(|\sin z/z|\le\min\{1,1/|z|\}\) and strict decay away from zero. The Gaussian moment \(\int_0^\infty e^{-u^2/2}u^2\,du\) produces the coefficient \(1/20\).

For a symmetric random variable \(X\), \(\mathbb E|X+h|=\mathbb E|X|+\mathbb E(|h|-|X|)_+\). Apply this with \(X=c_dS_{d-1}\) and \(h=1\pm c_d\). The density estimate, uniformly for bounded \(h\), gives
\[
\mathbb E(|h|-c_d|S_{d-1}|)_+=\frac{h^2}{c_d}\sqrt{\frac{3}{2\pi(d-1)}}+O(d^{-3/2}).
\]
Averaging the two shifts uses \(\big((1+c_d)^2+(1-c_d)^2\big)/2=1+c_d^2\). The mean-absolute first term has expansion
\[
c_d\mathbb E|S_{d-1}|=\sqrt{\frac{6d}{\pi}}\left(1-\frac{49}{20d}+O(d^{-2})\right),
\]
while the two-shift correction is
\[
\sqrt{\frac{6d}{\pi}}\left(\frac5{3d}+O(d^{-2})\right).
\]
Their sum yields \(-49/20+5/3=-47/60\).

For normalized volume sampling, the kernel is \(1+3\sum_{i=1}^d x_i y_i\), and its norm is \(\mathbb E|1+3S_d|\) at a vertex by the same convexity argument. The symmetric-shift identity yields
\[
\mathbb E|1+3S_d|=3\mathbb E|S_d|+\mathbb E(1-3|S_d|)_+.
\]
Its first term has relative correction \(1/(20d)\); the second equals \(\frac13\sqrt{3/(2\pi d)}+O(d^{-3/2})\), with relative correction \(1/(6d)\). Hence the volume correction is \(13/60\). Subtraction gives the asserted surface-volume gap.

## Verification
The accompanying `verify.py` evaluates the closed formulas using exact rational arithmetic, checks \(\|P_2\|\) and \(\|P_3\|\), independently integrates the Irwin--Hall density along the two types of facets using high precision for dimensions two through ten, and tests convergence to the two independently derived first correction coefficients. It uses `mpmath` for independent quadrature. On the prepared package, all 60 assertions passed. These finite checks corroborate, rather than certify by enumeration, the all-dimensional proof.

## Relationship to prior work
Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, publicly posted May 13, 2010) develop general \(L^p\)-stability theory for least-squares kernel projectors on manifolds. Their proof framework does not give the present sharp facet-surface affine polynomial formula. Białas-Cież, Kenne, Sommariva and Vianello (arXiv:2311.18656, 2023) bound or numerically evaluate Lebesgue constants for discrete polynomial sampling on cubes, simplices and balls; their discrete measures differ from the continuous facet-area measure here. Defant and collaborators (arXiv:2609.22050, 2026) study minimal projections on compact homogeneous group spaces such as tori and spheres; the cubical facet-surface space is not a homogeneous transitive sampling space under its finite symmetry group. Volume-cube affine projection constants and planar polygon-boundary examples are related but do not imply the new all-dimensional facet-surface formula or the asymptotic surface-volume difference, since the sampling measures and Gram moments differ. This is a comparison with examined statements, not a claim to have exhaustively indexed the literature.

## Limitations
The result does not compute projection norms for higher-degree polynomials, nonuniform facet densities, general polytope boundaries, or a pointwise ordering of surface and volume norms in every dimension. The asymptotic comparison proves the surface norm is smaller only for sufficiently large dimensions. Literature coverage is not exhaustive and independent bibliographic priority verification has not been performed.

## References
1. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The L-infinity-norm of the L2-projector*, arXiv:1005.2424 (first public version May 13, 2010), https://arxiv.org/abs/1005.2424.
2. L. Białas-Cież, D. J. Kenne, A. Sommariva, M. Vianello, *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex and ball*, arXiv:2311.18656 (2023), https://arxiv.org/abs/2311.18656.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, P. Zadunaisky, *Projection Constants of Polynomial Spaces via Representation Theory*, arXiv:2609.22050 (2026), https://arxiv.org/abs/2609.22050.
