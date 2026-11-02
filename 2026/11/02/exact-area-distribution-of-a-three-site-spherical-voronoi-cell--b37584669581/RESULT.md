# Exact area distribution of a three-site spherical Voronoi cell

## Finding
Take three independent area-uniform sites on the unit sphere and select one of their spherical nearest-site Voronoi cells by its site label. Its spherical area \(A\), measured in steradians, has the *complete* cumulative distribution function
\[
\mathbb P(A\le a)=
\begin{cases}
0,&a\le0,\\
\dfrac{a(2+\cos a)-3\sin a}{6\pi},&0<a<2\pi,\\
1,&a\ge2\pi.
\end{cases}
\]
The density on the interior is
\[
f_A(a)=\frac{2}{3\pi}\sin\left(\frac a2\right)\left[\sin\left(\frac a2\right)-\frac a2\cos\left(\frac a2\right)\right].
\]
In particular,
\[
\mathbb E A=\frac{4\pi}{3},\quad
\operatorname{Var}(A)=\frac{4\pi^2}{9}-\frac{10}{3},\quad
\mathbb P(A\le\pi)=\frac16.
\]
Every cell is almost surely a spherical lune whose intrinsic perimeter is **exactly** \(2\pi\), despite its nondegenerate area law. If \(A_1,A_2,A_3\) denote the three areas, then
\[
\operatorname{Cov}(A_i,A_j)=\frac53-\frac{2\pi^2}{9}\quad(i\ne j),
\]
by exchangeability and their fixed sum.

## Assumptions and scope
The sample space is \(S^2=\{x\in\mathbb R^3:\|x\|=1\}\), with the normalized rotation-invariant surface-area law. Let \(X_1,X_2,X_3\) be independent samples. For each \(i\in\{1,2,3\}\), define
\[
C_i=\{u\in S^2:u\cdot X_i\ge u\cdot X_j\text{ for all }j\in\{1,2,3\}\},\qquad A_i=\operatorname{area}(C_i).
\]
The set is the intrinsic nearest-site Voronoi cell because geodesic distance is \(\arccos(u\cdot X_i)\). Distinct-site and nondegenerate-normal events occur with probability one. The 'typical' cell is selected uniformly by **site label**, not by a uniformly selected sphere point (the latter induces area bias). All quantities refer to curvature-one spherical area and intrinsic great-circle perimeter.

## Proof
**1. Two bisector hemispheres.** By rotational invariance, fix \(X_1=e=(0,0,1)\). For \(j\in\{2,3\}\), set
\[
N_j=\frac{e-X_j}{\|e-X_j\|}.
\]
Then \(C_1=\{u\in S^2:u\cdot N_2\ge0,\ u\cdot N_3\ge0\}\). These two origin-centered hemispheres intersect in a spherical lune. Write \(\Theta=\arccos(N_2\cdot N_3)\in(0,\pi)\). The lune has opening angle \(\pi-\Theta\), so the spherical excess/longitude-area formula gives
\[
A_1=2(\pi-\Theta).
\]
The boundary comprises two great semicircles, each of length \(\pi\), hence its perimeter is \(2\pi\).

**2. The bisector-normal distribution.** For a uniform site \(X\in S^2\), its north coordinate \(H=e\cdot X\) is uniform on \([-1,1]\), independent of its uniform azimuth. The normalized difference \(N=(e-X)/\|e-X\|\) has north coordinate
\[
Z=e\cdot N=\sqrt{\frac{1-H}{2}}.
\]
Consequently, \(Z\) has density \(2z\) for \(0<z<1\), and \(N\) has uniform azimuth. Relative to spherical area measure \(d\sigma=d\phi\,dz\), its probability density is
\[
p_e(n)=\frac{(e\cdot n)_+}{\pi},\qquad (y)_+=\max\{y,0\}.
\]
In particular \(N_2,N_3\) are independent with this cosine-weighted hemisphere law.

**3. Angle convolution.** Let \(b,c\in S^2\) have angle \(\theta\in[0,\pi]\), and let \(U\) be uniform on \(S^2\). The following exact angular identity holds:
\[
\mathbb E[(U\cdot b)_+(U\cdot c)_+]
=\frac{\sin\theta+(\pi-\theta)\cos\theta}{6\pi}.
\]
To prove it, let \(G\) be a standard three-dimensional centered Gaussian and write \(G=\rho U\), with \(\rho\) independent of \(U\) and \(\mathbb E\rho^2=3\). In the plane spanned by \(b,c\), let the projected Gaussian have polar coordinates \((r,\psi)\), where \(\mathbb E r^2=2\) and \(\psi\) is uniform. The simultaneous positivity wedge is \(\theta-\pi/2<\psi<\pi/2\), and direct integration gives
\[
\mathbb E[(G\cdot b)_+(G\cdot c)_+]
=\frac1\pi\int_{\theta-\pi/2}^{\pi/2}\cos\psi\cos(\psi-\theta)\,d\psi
=\frac{\sin\theta+(\pi-\theta)\cos\theta}{2\pi}.
\]
Divide by \(\mathbb E\rho^2=3\) to obtain the identity. This angular Gaussian-kernel identity was known previously; its application here is to the *random Voronoi bisector normals*.

**4. The area law.** Under two independent uniform sphere normals, their mutual angle has density \(\frac12\sin\theta\) on \((0,\pi)\). The density of each cosine-weighted hemisphere normal relative to uniform probability measure is \(4(e\cdot n)_+\). Integrating the product of the two weights over a common uniformly rotated frame and using Step 3 yields
\[
f_\Theta(\theta)=\frac4{3\pi}\sin\theta\big[\sin\theta+(\pi-\theta)\cos\theta\big],\quad0<\theta<\pi.
\]
Under \(A_1=2(\pi-\Theta)\), substitution \(\theta=\pi-a/2\) with Jacobian magnitude \(1/2\) gives the stated \(f_A\). Integrating explicitly from \(0\) to \(a\) gives the stated CDF. The limiting CDF values at \(0\) and \(2\pi\) are \(0\) and \(1\), so there are no endpoint atoms.

**5. Moments and area covariance.** Direct integration by parts of the displayed CDF/density on \((0,2\pi)\) yields
\[
\int_0^{2\pi}a f_A(a)\,da=\frac{4\pi}3,\qquad
\int_0^{2\pi}a^2f_A(a)\,da=\frac{20\pi^2}9-\frac{10}3.
\]
Taking their difference gives the asserted variance; substituting \(a=\pi\) in the CDF gives the asserted probability. Since the cells tile the sphere up to zero-area edges, \(A_1+A_2+A_3=4\pi\) almost surely. The three cell areas are exchangeable, so
\(0=\operatorname{Var}(A_1+A_2+A_3)=3\operatorname{Var}(A_1)+6\operatorname{Cov}(A_1,A_2)\), giving the stated covariance. This proves all claims.

## Verification
The self-contained `verify.py` script uses exact symbolic integration for the CDF, density, first two moments, Gaussian angular convolution, and normalization. Independent experiments generate actual uniform sites, compute the difference normals and lune areas, and separately approximate Voronoi areas by random sphere point-membership integration. The completed checker reported `ALL_CHECKS_PASSED`. Finite simulations are diagnostics only; the preceding geometric and analytic derivation proves the full real-parameter law.

## Relationship to prior work
Kabluchko and Thäle [1] study the same spherical binomial-Voronoi sampling model and determine the typical cell's **face vector**, but their inspected full article does not give the cell-area CDF or variance. The present result supplements those combinatorial results with an exact metric law in the natural three-site case. Cho and Saul [2] already gave the order-one arc-cosine Gaussian angular kernel used in Step 3; the kernel itself is **not** claimed to be new, and, by itself, does not identify the spherical Voronoi bisector normal law or the area distribution. Li, Sui, Mu, and Qiu [3] study distance-to-nearest-site statistics for **prespecified** spherical sites, a distinct random variable and sampling model. No equivalence or stronger formula for this three-site area law was identified in the sources inspected; historical priority remains open to further independent literature review.

## Limitations
The theorem concerns exactly three independent rotation-uniform sites on the unit 2-sphere and site-labelled cell selection. It does not assert the same law for an area-biased cell, unequal site distributions, four or more sites, non-spherical surfaces, or cell shapes beyond area/perimeter. Correlation is only asserted pairwise through exchangeability and the fixed total area; a full joint area distribution is not derived. The cited Gaussian-kernel identity is prior work, not a new component. Publication-priority claims remain provisional; no independent mathematical audit has been performed.

## References
1. Z. Kabluchko and C. Thäle, *The Typical Cell of a Voronoi Tessellation on the Sphere*, arXiv:1911.07221, first posted 2019-11-17; *Discrete & Computational Geometry* 66 (2021). https://arxiv.org/abs/1911.07221
2. Y. Cho and L. Saul, *Kernel Methods for Deep Learning*, NeurIPS (2009), Section 2, equations (1)–(6). https://cseweb.ucsd.edu/~yoc002/paper/nips09_arccos.pdf
3. H. Li, J. Sui, S. Mu, and X. Qiu, *Stochastic Properties of Minimal Arc Distance and Cosine Similarity between a Random Point and Prespecified Sites on Sphere*, arXiv:2102.01221, first posted 2021-02-01; see the 2026 revision for expanded treatment. https://arxiv.org/abs/2102.01221
