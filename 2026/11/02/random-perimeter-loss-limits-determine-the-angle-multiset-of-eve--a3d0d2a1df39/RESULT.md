# Random perimeter-loss limits determine the angle multiset of every convex polygon

## Finding
Let \(K\) be any full-dimensional convex Euclidean polygon with \(m\ge3\) genuine vertices, perimeter \(P\), and interior angles \(\alpha_1,\ldots,\alpha_m\in(0,\pi)\). Let \(H_N\) be the convex hull of \(N\) independent points chosen uniformly in arclength on \(\partial K\). Define the dimensionless missing-perimeter statistic
\[
L_N=\frac{N}{P}\big(P-\operatorname{per}(H_N)\big).
\]
For \(U_i,V_i\) that are jointly independent standard exponential variables, put
\[
\ell_\alpha(u,v)=u+v-\sqrt{u^2+v^2-2uv\cos\alpha}.
\]
Then, as \(N\to\infty\),
\[
L_N\ \xrightarrow{\mathrm d}\ L_K:=\sum_{i=1}^m\ell_{\alpha_i}(U_i,V_i),
\]
and all fixed positive integer moments converge. More importantly, the **probability law of \(L_K\) determines exactly the unordered multiset of all interior angles**. Precisely, for two convex Euclidean polygons \(K,K'\), with any finite numbers of genuine vertices,
\[
L_K\stackrel{\mathrm d}=L_{K'}\quad\Longleftrightarrow\quad
\{\alpha_i(K)\}_i=\{\alpha_j(K')\}_j
\quad\text{as multisets}.
\]
Thus the limiting random perimeter deficit detects every interior angle with multiplicity even though it generally does **not** determine the polygon's edge lengths or its congruence class.

## Assumptions and scope
A genuine vertex has interior angle strictly between zero and \(\pi\); consecutive collinear sides are merged. The sampling law is normalized Euclidean boundary arclength, the sampled points are independent, and \(N\) tends to infinity with the polygon fixed. The perimeter of a degenerate hull of fewer than three noncollinear points is interpreted by its standard convex-set perimeter (equivalently the Cauchy width integral); such configurations do not affect the limit. No smooth-boundary assumption is made. All exponential variables displayed in the limit have mean one.

## Proof

**1. Exact corner decomposition.** Write the vertices in counterclockwise order \(v_1,\ldots,v_m\), with side lengths \(d_i>0\). Let \(E_N\) be the event that every open side contains at least one sampled point. Then
\[
\mathbb P(E_N^{\mathrm c})\le\sum_{i=1}^m(1-d_i/P)^N.
\]
On \(E_N\), take \(a_i\) and \(b_i\) to be the distances from vertex \(v_i\) along its two adjacent sides to the nearest sample on each respective side. The boundary of the random convex hull consists of straight sampled subsegments on the original sides and one chord cutting each original corner. The cosine rule gives the **exact** identity
\[
P-\operatorname{per}(H_N)
=\sum_{i=1}^m\ell_{\alpha_i}(a_i,b_i).
\]
The individual corner term is homogeneous of degree one and nonnegative. There is no contribution from the lengths of sides away from their endpoints.

**2. Independent exponential corner gaps.** Fix arbitrary nonnegative thresholds \(s_i,t_i\), with all short endpoint intervals disjoint for large \(N\). An individual sampled point avoids their union with probability \(1-(P/N)\sum_i(s_i+t_i)/P\), so
\[
\mathbb P\!\left(\frac{Na_i}{P}>s_i,\ \frac{Nb_i}{P}>t_i\ \text{for all }i\right)
=\left(1-\frac{\sum_i(s_i+t_i)}{N}\right)^N
\longrightarrow e^{-\sum_i(s_i+t_i)}.
\]
This identifies the full \(2m\)-component nearest-endpoint-gap limit as independent standard exponentials. By homogeneity of \(\ell_\alpha\), continuity, and \(\mathbb P(E_N)\to1\), the asserted distributional limit follows.

For fixed integer \(q>0\), \(0\le\ell_\alpha(a,b)\le a+b\). Each endpoint gap, capped at its containing side length, satisfies \(\mathbb P(Na_i/P>t)\le e^{-t}\) for its attainable range; the same holds for \(b_i\). The \(q\)-th moments of their sum are therefore bounded independently of \(N\). Off \(E_N\), monotonicity of perimeter under convex inclusion gives \(0\le L_N\le N\), and hence \(\mathbb E[L_N^q\mathbf1_{E_N^{\mathrm c}}]\le N^q\mathbb P(E_N^{\mathrm c})\to0\). Uniform bounds on moments of order \(q+1\) give uniform integrability of the \(q\)-th powers; convergence of all fixed integer moments follows.

**3. A one-corner moment-generating function.** By the exponential change of variables \(S=U+V\) and \(T=U/(U+V)\), \(S\) and \(T\) are independent; \(S\sim\operatorname{Gamma}(2,1)\) and \(T\sim\operatorname{Uniform}(0,1)\). Thus
\[
\ell_\alpha(U,V)=S b_\alpha(T),\qquad
b_\alpha(t)=1-\sqrt{1-4\cos^2(\alpha/2)t(1-t)}.
\]
Write \(s=\sin(\alpha/2)\) and \(c=\cos(\alpha/2)\); both lie strictly between zero and one. The weight \(b_\alpha(t)\) is nonnegative, has a unique maximum \(B_\alpha=1-s\) at \(t=1/2\), and its exact form about the maximum is
\[
b_\alpha(1/2+x)=1-\sqrt{s^2+4c^2x^2}.
\]
Consequently the one-corner moment-generating function is
\[
M_\alpha(z)=\mathbb E[e^{z\ell_\alpha(U,V)}]
=\int_0^1\big(1-z b_\alpha(t)\big)^{-2}\,dt,
\qquad z<z_\alpha:=\frac1{1-\sin(\alpha/2)}.
\]
It is finite for real \(z<z_\alpha\), and diverges as \(z\uparrow z_\alpha\). Expanding at the unique maximum gives
\[
1-zb_\alpha(1/2+x)
=\delta+\frac{2z_\alpha c^2}{s}x^2+O_\alpha(\delta x^2+x^4),
\quad \delta=1-z/z_\alpha\downarrow0.
\]
Scale \(x=\sqrt\delta\,y\) in the integral. Standard dominated convergence after separating a fixed neighborhood of \(x=0\) yields the precise algebraic singularity
\[
\boxed{
M_\alpha(z)\sim
\frac\pi2\sqrt{\frac{s}{2z_\alpha c^2}}\,
(1-z/z_\alpha)^{-3/2}
}\qquad(z\uparrow z_\alpha).
\]
The local domination follows from positive quadratic lower bounds on \(1-zb_\alpha\) near its maximum; away from that maximum the integrand is uniformly bounded. In particular \(z_\alpha\) is a strictly increasing continuous function of \(\alpha\in(0,\pi)\).

**4. Recover the full angle multiset.** Independence gives
\[
M_K(z):=\mathbb E[e^{zL_K}]=\prod_{i=1}^m M_{\alpha_i}(z)
\]
through the first positive singularity. If \(a=\min_i\alpha_i\) occurs \(r\) times, the first divergence is at \(z_a\) and the asymptotic formula above yields
\[
M_K(z)\sim C(1-z/z_a)^{-3r/2},\qquad C\in(0,\infty).
\]
All other factors are finite and strictly positive there. Therefore the first divergence determines \(z_a\), hence \(a\), while the logarithmic blowup exponent determines the integer \(r\). Given two polygons with identical limit laws, the products of their MGFs agree in a real neighborhood of zero and so share these two parameters. Divide the two product identities by the common positive factor \(M_a(z)^r\); the remaining products agree as real analytic functions around zero. The argument repeats for the next smallest angle. Finite induction recovers every angle and multiplicity; if one product is exhausted, the other cannot have extra factors because \(M_\alpha(z)>1\) for \(z>0\). Conversely, equal angle multisets yield the identical independent-sum law from Step 2.

**5. Why shape itself is not reconstructed.** The limit depends on the polygon only through the angle multiset. Every nondegenerate rectangle has four angles equal to \(\pi/2\); rectangles of different aspect ratios are not congruent but have the same limiting normalized perimeter-loss distribution.

## Verification
The companion `verify.py` independently checks exact polygonal corner decompositions against an explicit convex-hull implementation for triangles and polygons with four, five and seven vertices. Numerical quadrature checks the \(\alpha=\pi/2\) mean and variance; seeded finite-sample experiments compare rectangles with different aspect ratios. Additional high-precision local quadrature checks the \((1-z/z_\alpha)^{-3/2}\) moment-generating-function singularity for five distinct angles, and the prescribed multiplicity logic for three test multisets. Run with `python verify.py` (Python, NumPy, SciPy). These computations support but do not replace the proofs of the convergence and inverse theorem. The independent checks do not exhaust all polygons or all singularities.

## Relationship to prior work
Böröczky, Fodor and Hug (2011, arXiv:1103.4978v1) study expected intrinsic-volume deficits for boundary samples under a rolling-ball condition. Polygon corners violate that hypothesis; their results do not give this polygonal inverse theorem. Reitzner, Schütt and Werner (2019, arXiv:1911.05917v1) analyze boundary samples of simple polytopes and concentrate on expected volume deficits and face counts. Prochno, Schütt, Sonnleitner and Werner (2024, arXiv:2404.02870v1) establish local Poisson vertex-process convergence for boundary-sampled polygons to analyze **Hausdorff** approximation. Their local convergence is compatible with, and supplies an alternative route to, the forward random-perimeter limit here. The additional result retained here is **identification of every interior angle with multiplicity from the limiting perimeter-deficit law**, by its exact one-corner moment-generating singularities. No priority is claimed for exponential corner gaps, the cosine rule, or the general Poisson construction.

## Limitations
The theorem concerns the ideal full probability law of a limiting statistic, not reconstruction from finitely many noisy realizations. No numerical stability or finite-sample inversion rate is established. The limiting law does not reconstruct perimeter, side lengths, vertex order or shape up to congruence. The polygon and its number of vertices are fixed before the sample-size limit. Historical priority requires independent review; an earlier perimeter-specific result or an equivalent Laplace-transform inverse characterization could still exist.

## References
- K. J. Böröczky, F. Fodor, D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, arXiv:1103.4978v1, 2011-03-25. https://arxiv.org/abs/1103.4978
- M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917v1, 2019-11-14. https://arxiv.org/abs/1911.05917
- J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870v1, 2024-04-03. https://arxiv.org/abs/2404.02870
