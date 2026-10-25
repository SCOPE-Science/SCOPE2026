# An exact noise-blind area law for repeated polygon edge subdivision

## Finding
Let \(P_0\) be a counterclockwise convex planar \(n\)-gon, \(n\ge3\), with cyclic vertices \(z_j\in\mathbb C\), indexed modulo \(n\). At step \(s\ge1\), replace every vertex by a point on its outgoing edge:
\[
z_j^{(s)}=(1-\xi_{j,s})z_j^{(s-1)}+\xi_{j,s}z_{j+1}^{(s-1)}.
\]
Assume \(0\le\xi_{j,s}\le1\) and that, conditional on all previous subdivision steps, each \(\xi_{j,s}\) has the same deterministic mean \(\mu_s\in[0,1]\), and distinct edge variables are pairwise uncorrelated:
\[
\mathbb E(\xi_{j,s}\mid\mathcal F_{s-1})=\mu_s,\qquad
\mathbb E(\xi_{i,s}\xi_{j,s}\mid\mathcal F_{s-1})=\mu_s^2\quad(i\ne j).
\]
No identical distribution, joint independence, or moment assumption beyond boundedness is required.

Define deterministic averaged vertices \(b_j^{(0)}=z_j\) and
\[
b_j^{(s)}=(1-\mu_s)b_j^{(s-1)}+\mu_s b_{j+1}^{(s-1)}.
\]
Then the polygon area has the **exact noise-blind expectation identity**
\[
\boxed{\mathbb E\,\operatorname{Area}(P_t)
=\operatorname{Area}(b_0^{(t)},\ldots,b_{n-1}^{(t)})}\qquad(t=0,1,2,\ldots).
\]
In particular, the expected area depends on the random edge-split laws only through their per-step means, even after arbitrarily many dependent geometric iterations.

With \(\widehat z_k=n^{-1}\sum_{j=0}^{n-1}z_j\exp(-2\pi i kj/n)\), the exact finite-time spectral law is
\[
\boxed{\mathbb E\,\operatorname{Area}(P_t)
=\frac n2\sum_{k=0}^{n-1}|\widehat z_k|^2
\sin\frac{2\pi k}{n}
\prod_{s=1}^t\left(1-4\mu_s(1-\mu_s)\sin^2\frac{\pi k}{n}\right).}
\]
For a regular initial \(n\)-gon and constant \(\mu\in(0,1)\), this collapses to an exact single geometric rate,
\[
\frac{\mathbb E\,\operatorname{Area}(P_t)}{\operatorname{Area}(P_0)}
=\left(1-4\mu(1-\mu)\sin^2\frac\pi n\right)^t.
\]
If \(t_n=\lfloor\tau n^2\rfloor\) with \(\tau\ge0\) fixed, the same expected-area ratio converges to
\[
\boxed{\exp\bigl(-4\pi^2\mu(1-\mu)\tau\bigr).}
\]

## Assumptions and scope
Every polygon here is specified by a cyclically ordered vertex list. Selecting one point on each consecutive side of a convex polygon, in that order, produces another weakly convex polygon, so its unsigned Euclidean area equals the nonnegative shoelace signed area. Repeated vertices and zero-area limiting cases are allowed. At each step, the conditional first and cross-edge second moments above are deterministic; the full distributions may vary with the vertex and with time, and higher-order cross-edge dependence is allowed. The initial vertices are deterministic.

## Proof
**1. Conditional two-point relations.** Put \(C_d(s)=\mathbb E\sum_{j=0}^{n-1}\overline{z_j^{(s)}}z_{j+d}^{(s)}\) for \(d=0,\ldots,n-1\), with cyclic indices. For \(1\le d\le n-1\), the factors \(\xi_{j,s}\) and \(\xi_{j+d,s}\) belong to distinct edges. Conditional pairwise uncorrelatedness implies
\[
\begin{aligned}
\mathbb E[(1-\xi_{j,s})(1-\xi_{j+d,s})\mid\mathcal F_{s-1}]&=(1-\mu_s)^2,\\
\mathbb E[(1-\xi_{j,s})\xi_{j+d,s}\mid\mathcal F_{s-1}]&=\mu_s(1-\mu_s),\\
\mathbb E[\xi_{j,s}\xi_{j+d,s}\mid\mathcal F_{s-1}]&=\mu_s^2.
\end{aligned}
\]
Expanding the two substituted vertices, then summing over \(j\), gives
\[
C_d(s)=\bigl((1-\mu_s)^2+\mu_s^2\bigr)C_d(s-1)
+\mu_s(1-\mu_s)\bigl(C_{d-1}(s-1)+C_{d+1}(s-1)\bigr).
\]
At the two endpoints interpret \(C_n=C_0\). The value \(C_0(s)=\mathbb E\sum_j|z_j^{(s)}|^2\) need not obey the same recurrence, but it is always real.

**2. Antisymmetric cancellation.** Let \(I_d(s)=\operatorname{Im} C_d(s)\). Since \(I_0(s)=I_n(s)=0\), taking imaginary parts yields the closed tridiagonal evolution
\[
I_d(s)=\bigl(1-2c_s\bigr)I_d(s-1)
+c_s\bigl(I_{d-1}(s-1)+I_{d+1}(s-1)\bigr),
\quad 1\le d\le n-1,
\]
where \(c_s=\mu_s(1-\mu_s)\). The deterministic mean vertices \(b_j^{(s)}\) obey the **same** imaginary-correlation evolution, because their update is exactly the same edge formula with every split set to \(\mu_s\). Both evolutions have identical initial values. Induction in \(s\) therefore gives \(I_1(s)=\operatorname{Im}\sum_j\overline{b_j^{(s)}}b_{j+1}^{(s)}\). Multiplication by \(1/2\) gives the asserted equality of areas, by the shoelace formula. Crucially, unknown diagonal variances contribute only to the real \(C_0\) and cannot enter this antisymmetric system.

**3. Fourier diagonalization.** For the deterministic mean polygon, Fourier inversion gives
\[
b_j^{(t)}=\sum_{k=0}^{n-1}\widehat z_k\exp(2\pi i kj/n)
\prod_{s=1}^t\left(1-\mu_s+\mu_s\exp(2\pi i k/n)\right).
\]
Orthogonality of the \(n\) roots of unity in \(\sum_j\overline{b_j^{(t)}}b_{j+1}^{(t)}\) leaves only equal-frequency terms. Their modulus squares are precisely
\[
\prod_{s=1}^t\left|1-\mu_s+\mu_s\exp(2\pi i k/n)\right|^2
=\prod_{s=1}^t\left(1-4c_s\sin^2\frac{\pi k}{n}\right).
\]
Taking the imaginary part yields the stated spectral sum. For a counterclockwise regular polygon only the positive first Fourier mode is present; its area-normalized multiplier is the displayed single factor. Finally, \(n^2\sin^2(\pi/n)\to\pi^2\) and the logarithmic limit prove the diffusive scaling for fixed \(0<\mu<1\).

**4. Dependence boundary.** Pairwise decorrelation cannot simply be dropped: choose one shared fair Bernoulli variable \(B_s\) and set \(\xi_{j,s}=B_s\) for **all** edges \(j\). Every update either fixes or cyclically relabels the vertices, so the area stays exactly constant; the deterministic mean update with \(\mu_s=1/2\) strictly reduces the area of a nondegenerate regular polygon. Thus the conclusion is not a generic Jensen identity without hypotheses.

## Verification
The standalone script `verify_polygon_area.py` reproduces: an exact \(512\)-path rational-arithmetic computation using pairwise-independent but jointly dependent split variables; a \(120000\)-sample randomized four-stage test on an irregular pentagon with varying means and split distributions; Fourier reconstruction checks for polygon orders \(3\) through \(13\); regular-polygon rate checks through order \(14\); and the cross-edge dependence counterexample. The proof above, not finite testing, establishes all dimensions, all finite times, and all admissible conditional distributions.

## Relationship to prior work
Volkov, *Random geometric subdivisions* (first available 2011), studies random subdivision models, especially the almost-sure limiting shapes of triangles and quadrilaterals. Nguyen and Volkov, *A universal result for consecutive random subdivision of polygons* (first available 2015), define essentially the same independent-edge model and establish flattening and Lyapunov-rate results. Those results concern typical, rescaled geometry, not the unscaled **exact finite-time expectation** proved here. The earlier paper supplies the geometric stochastic setting, while the finite-time noise-blind identity, its conditional pairwise-uncorrelated extension and arbitrary-initial-polygon Fourier formula are the present statements. The deterministic Fourier multiplier is elementary and is not independently claimed as new.

## Limitations
This theorem computes the first moment of area, not its variance, full distribution, almost-sure exponent, or typical shape; mean and typical decay must not be conflated. It assumes cyclic edge updates with common conditional mean and zero cross-edge covariance at each time. General correlated edge choices need not satisfy the identity. The result makes no historical-priority claim beyond the stated comparisons; independent verification remains outstanding.

## References
1. S. Volkov, *Random geometric subdivisions*, first preprint 5 December 2011, arXiv:1112.0932, https://arxiv.org/abs/1112.0932.
2. T.-M. Nguyen and S. Volkov, *A universal result for consecutive random subdivision of polygons*, first preprint 16 June 2015, arXiv:1506.04942, https://arxiv.org/abs/1506.04942.
3. P. Diaconis and L. Miclo, *On barycentric subdivision*, Combinatorics, Probability and Computing 20 (2011), 213–237, https://doi.org/10.1017/S0963548310000441. (Distinct subdivision mechanism; background only.)
