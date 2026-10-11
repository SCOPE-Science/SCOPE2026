# Gumbel transition and second-order Hausdorff error for randomly inscribed regular polygons

## Finding

Let \(m\ge4\) be an integer, and let \(Q_m\subset\mathbb R^2\) be any regular \(m\)-gon of perimeter \(P_m>0\). For each integer \(n\ge3\), take \(n\) independent arclength-uniform points of \(\partial Q_m\), let \(Q_{m,n}\) be their convex hull, and put \(H_{m,n}=d_H(Q_m,Q_{m,n})\). Define the sequential-limit variable and mean
\[
T_m=\lim_{n\to\infty}^{\mathrm{law}}\frac{nH_{m,n}}{P_m},\qquad
c_m=\lim_{n\to\infty}\frac{n\mathbb E H_{m,n}}{P_m}=\mathbb E T_m.
\]
Both limits exist for every fixed \(m\). Let \(G\) have the standard Gumbel distribution, \(\Pr(G\le t)=\exp(-e^{-t})\), and let \(\gamma\) be Euler's constant. The sharp double-limit theorem is
\[
\frac{2m}{\pi}T_m-\log m-\frac12\log\log m-\frac12\log\pi+\log2
\ \xrightarrow[m\to\infty]{\mathrm{law}}\ G,
\]
and
\[
\boxed{\ \frac{2m}{\pi}c_m=\log m+\frac12\log\log m+
\frac12\log\pi-\log2+\gamma+o(1)\ }.
\]
The number of sampled points tends to infinity **first**, with the polygon fixed; the number of polygon vertices tends to infinity **second**. No claim is made about a simultaneous limit in which \(m\) and \(n\) grow at comparable rates.

## Assumptions and scope

Distances are Euclidean Hausdorff distances between nonempty compact sets. Since \(Q_{m,n}\subseteq Q_m\), the error is the maximal distance from points of \(Q_m\) to \(Q_{m,n}\), attained at a vertex of \(Q_m\). All \(n\) samples are independent and uniform with respect to boundary arclength. Homogeneity removes the choice of perimeter. A unit exponential is an exponential random variable of rate \(1\). Throughout the large-\(m\) limit, \(\delta_m=2\pi/m\) denotes the exterior angle.

For each \(m\), take \(2m\) independent unit exponentials \(X_1,Y_1,\ldots,X_m,Y_m\) and set
\[
D_m(x,y)=\frac{xy\sin\delta_m}{\sqrt{(x+y)^2-4xy\sin^2(\delta_m/2)}}.
\]
The fixed-\(m\) law has the exact representation
\[
T_m\ \stackrel{\mathrm{law}}=\ \max_{1\le i\le m}D_m(X_i,Y_i).
\]
The representation is a known type of polygonal vertex-limit law; the new assertion here is the **sharp large-number-of-vertices Gumbel and expectation expansion**, not the existence of the fixed-polygon limit.

## Proof

**1. Polygonal vertex reduction.** For every convex polygon \(Q\) and convex subset \(K\subseteq Q\), the function \(x\mapsto\operatorname{dist}(x,K)\) is convex. Thus its maximum over \(Q\) occurs at a vertex. At a vertex with interior angle \(\pi-\delta_m\ge\pi/2\), let the nearest sampled points on the two incident edges be at arclength distances \(x\) and \(y\) from the vertex. Once the samples are sufficiently dense, the chord joining these points supports the sampled hull at the vertex. The perpendicular projection from the vertex falls inside the chord because the interior angle is at least \(\pi/2\). The altitude to the chord is exactly
\[
\frac{xy\sin(\pi-\delta_m)}{\sqrt{x^2+y^2-2xy\cos(\pi-\delta_m)}}
=D_m(x,y).
\]
For fixed \(m\), disjoint shrinking neighborhoods of the vertices have independent Poisson point-process limits under the length scaling \(n/P_m\). Consequently the nearest-point distances on all \(2m\) incident edge germs converge jointly to independent unit exponentials. The continuous-mapping theorem gives the displayed law for \(T_m\).

Convergence of expectations follows from uniform integrability: a point on either incident edge within arclength \(rP_m/n\) of a vertex places the vertex at Euclidean distance at most \(rP_m/n\) from the hull. For \(r\) below a fixed multiple of \(n\), the probability that no such point appears on either incident edge is at most \(e^{-2r}\). Beyond this range, absence of samples in fixed positive-length neighborhoods has exponentially small probability in \(n\); the rescaled error is at most a fixed multiple of \(n\). Summation over finitely many vertices yields uniform integrability. This also follows from the fixed-polygon expectation theorem in the second reference below.

**2. A uniform reduction to a harmonic exponential statistic.** Define \(Z(x,y)=xy/(x+y)\), \(Z_i=Z(X_i,Y_i)\), and \(M_m=\max_{1\le i\le m}Z_i\). Since \(0<4xy/(x+y)^2\le1\), the chord formula gives the pointwise inequalities, valid for every \(m\ge4\) and \(x,y>0\),
\[
\sin\delta_m\,Z(x,y)\le D_m(x,y)\le2\sin(\delta_m/2)\,Z(x,y).
\]
In particular, \(T_m=\delta_m M_m(1+O(\delta_m^2))\), with deterministic multiplicative bounds independent of the sample. Since \(Z_i\le\min(X_i,Y_i)\), and the minimum of two independent unit exponentials has rate \(2\),
\[
\mathbb E M_m\le\frac12\sum_{j=1}^m\frac1j=O(\log m).
\]
It follows that
\[
\left|c_m-\delta_m\mathbb E M_m\right|
=O\!\left(\frac{\log m}{m^3}\right),
\qquad
\frac4{\delta_m}T_m-4M_m=o_{\Pr}(1).
\]

**3. Exact tail and its decisive square-root factor.** For independent unit exponentials \(X,Y\), let \(Z=XY/(X+Y)\). Conditioning on \(X=x\), the inequality \(Z>z\) is equivalent to \(x>z\) and \(Y>zx/(x-z)\). Therefore
\[
\begin{aligned}
\Pr(Z>z)&=\int_z^\infty\exp\!\left(-x-\frac{zx}{x-z}\right)\,dx\\
&=e^{-2z}\int_0^\infty\exp\!\left(-u-\frac{z^2}{u}\right)\,du\\
&=2ze^{-2z}K_1(2z),\qquad z>0,
\end{aligned}
\]
where \(K_1\) is the modified Bessel function of the second kind. Laplace's method about the unique saddle \(u=z\), equivalently the standard \(K_1\) asymptotic, yields
\[
\Pr(Z>z)=\sqrt{\pi z}\,e^{-4z}\left(1+O(z^{-1})\right)
\quad(z\to\infty).
\]
The factor \(\sqrt z\) is essential; it produces the nonzero \(\frac12\log\log m\) correction.

**4. Extreme-value normalization.** Put
\[
b_m=\frac14\left(\log m+\frac12\log\log m+
\frac12\log\pi-\log2\right).
\]
For every fixed real \(t\), the tail estimate shows
\[
m\Pr\!\left(Z>b_m+\frac t4\right)\longrightarrow e^{-t}.
\]
Independence implies
\[
\Pr(4M_m-4b_m\le t)=
\left(1-\Pr\!\left(Z>b_m+\frac t4\right)\right)^m
\longrightarrow\exp(-e^{-t}).
\]
The pointwise comparison in Step 2 transfers this convergence to \(\frac4{\delta_m}T_m-4b_m\). Since \(4/\delta_m=2m/\pi\), this is the asserted Gumbel limit.

**5. Mean convergence.** The same tail asymptotic implies uniform integrability of the centered maxima. Explicitly, for some absolute positive constants and all sufficiently large \(m\), the upper deviations have \(\Pr(4M_m-4b_m>t)\le Ce^{-t/2}\) for \(t\ge0\). For \(0\le t\le2b_m\), the negative tail is bounded by \(\exp(-c e^t)\); for \(2b_m<t\le4b_m\) it is bounded by \(\exp(-c m^{1/2})\) after harmless logarithmic adjustments; for \(t>4b_m\) the negative-tail event is empty. These estimates follow from two-sided bounds \(c\sqrt{1+z}e^{-4z}\le\Pr(Z>z)\le C\sqrt{1+z}e^{-4z}\), valid for all \(z\ge0\). Integrating the tails gives convergence of centered expectations. The standard Gumbel mean is \(\gamma\), so
\[
4\mathbb E M_m=4b_m+\gamma+o(1).
\]
Finally Step 2 yields
\[
\frac{2m}{\pi}c_m=4\mathbb E M_m+o(1)
=\log m+\frac12\log\log m+\frac12\log\pi-\log2+\gamma+o(1),
\]
as claimed.

## Verification

The included standard-library-only program `verify.py` checks the independent gamma/ratio and conditional-exponential integral representations of the tail, the geometric chord-altitude formula against a direct closest-point computation, the uniform deterministic bounds, and numerical finite-size Gumbel limits. It completed 2,894 finite checks with output `VERIFY_OK 2894 finite checks`. The infinite-dimensional and asymptotic assertions are consequences of the five analytical proof steps, not of the numerical runs.

The exact CDF of the auxiliary statistic may alternatively be verified using independent \(S=X+Y\sim\mathrm{Gamma}(2,1)\) and \(U=X/(X+Y)\sim\mathrm{Uniform}(0,1)\):
\[
\Pr(Z>z)=\int_0^1 e^{-z/[u(1-u)]}
\left(1+\frac{z}{u(1-u)}\right)\,du.
\]
This supplies a second reproducible route without special-function software.

## Relationship to prior work

Fodor, Hug and Ziebarth (2014) provide an archival framework for asymptotic convex-body approximation by random polytopes, chiefly with smoothness and mean-width/volume functionals. Prochno, Schütt, Sonnleitner and Werner (first circulated 2024; journal 2025) rigorously establish fixed-polygon limiting Hausdorff error distributions and expected values and give only an order-of-magnitude estimate proportional to \((\log m)/m\) for the regular-\(m\)-gon constants. Their exact fixed-polygon integral is acknowledged; it is not itself a new discovery here. The result proved above adds a distinct sequential **large-\(m\) limit theorem**, its exact centering, the square-root exponential-tail mechanism, and a sharp two-term expectation expansion. Sonnleitner (2025) proves Gumbel approximation laws for fixed smooth positive-curvature bodies under a different sampling limit; that theorem does not apply directly to the polygon-corner limit used here.

## Limitations

The limits must be taken in the stated order. There is no simultaneous \(m,n\) regime, no claimed general convex-polygon version of the sharp Gumbel constants, and no claim of independent validation or comprehensive historical exhaustiveness. Exact fixed-polygon limit distributions and coarse regular-polygon estimates are previously known. More extensive historical literature may contain equivalent higher-order asymptotics not located in the inspected sources. A finite numerical checker cannot prove the tail expansion, Poisson convergence, or extreme-value theorem. The centering explicitly includes \(\frac12\log\log m\); treating the original first-order \(\asymp\) estimate as this sharper statement would be incorrect.

## References

1. F. Fodor, D. Hug, I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105, version first public 29 September 2014. https://arxiv.org/abs/1409.8105
2. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870, first public 3 April 2024; journal title *Random approximation of convex bodies in Hausdorff distance*, Mathematische Annalen 392 (2025), 4525–4542, doi:10.1007/s00208-025-03186-7. https://arxiv.org/abs/2404.02870
3. M. Sonnleitner, *A limit theorem for Hausdorff approximation by random inscribed polytopes*, arXiv:2508.16442, first public 22 August 2025. https://arxiv.org/abs/2508.16442
4. V.-E. Brunel, *Uniform Behaviors of Random Polytopes under the Hausdorff Metric*, arXiv:1503.01504, first public 5 March 2015. https://arxiv.org/abs/1503.01504
