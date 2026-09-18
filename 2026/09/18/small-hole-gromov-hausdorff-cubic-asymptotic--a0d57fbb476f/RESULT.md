# Universal cubic-error Gromov--Hausdorff asymptotic for a deleted geodesic ball

## Statement

Let \((M^n,g)\) be a connected closed smooth Riemannian manifold and let \(a\in M\). For \(r>0\), put
\[
X_r=M\setminus B_r(a),
\]
equipped with the subspace metric inherited from \(M\), and set
\[
c_n=\sqrt{\frac{n+1}{2n}}.
\]

If \(n\ge 2\), then as \(r\downarrow0\),
\[
\boxed{\quad d_{\mathrm{GH}}(X_r,M)=c_n r+O_{M,a}(r^3).\quad}
\]
Since \(d_{\mathrm H}(X_r,M)=r\) for all sufficiently small \(r\), equivalently
\[
\boxed{\quad
\frac{d_{\mathrm{GH}}(X_r,M)}{d_{\mathrm H}(X_r,M)}
=c_n+O_{M,a}(r^2),
\qquad
\lim_{r\downarrow0}\frac{d_{\mathrm{GH}}(X_r,M)}r=c_n.
\quad}
\]

For \(n=1\), a connected closed Riemannian manifold is a circle and, for all sufficiently small \(r\),
\[
d_{\mathrm{GH}}(X_r,M)=d_{\mathrm H}(X_r,M)=r,
\]
which is the same leading formula because \(c_1=1\).

Thus the Euclidean sharp constant for deleting a ball is the universal first-order coefficient on every closed Riemannian manifold; curvature first enters only at cubic order in this estimate.

## Context

Schott proved in arXiv:2609.12625 (Theorem 3.1) that for
\[
A^n=\mathbb R^n\setminus B_1(0)
\]
one has
\[
d_{\mathrm H}(\mathbb R^n,A^n)=1,\qquad
d_{\mathrm{GH}}(\mathbb R^n,A^n)=c_n.
\]
He also proved (Theorem 3.6) that for every connected Riemannian manifold without boundary, every \(a\), and every fixed \(L>1\), sufficiently small deleted balls satisfy
\[
d_{\mathrm{GH}}(M\setminus B_r(a),M)\le Lc_n r,
\qquad
d_{\mathrm H}(M\setminus B_r(a),M)=r.
\]
That theorem gives the sharp Euclidean coefficient up to an arbitrary fixed multiplicative loss, but does not state an exact small-hole asymptotic or an error order.

Adams--Frick--Majhi--McBride (arXiv:2309.16648, Theorem 4) give, for a connected closed \(n\)-manifold with convexity radius \(\rho\) and sectional-curvature upper bound \(\kappa\),
\[
d_{\mathrm{GH}}(X,M)\ge
\min\left\{
\alpha(n,\kappa)d_{\mathrm H}(X,M),
\frac{\alpha(n,\kappa)\tau}{2\alpha(n,\kappa)+2}
\right\}
\]
when \(Y=M\), where
\[
\alpha(n,\kappa)=
\begin{cases}
c_n,&\kappa\le0,\\[3pt]
c_n\,\dfrac{\sin\!\left(\frac{\pi}{2}
\sqrt{\frac{\kappa}{\kappa+1}}\right)}
{\frac{\pi}{2}\sqrt{\frac{\kappa}{\kappa+1}}},
&\kappa>0,
\end{cases}
\]
and
\[
\tau=
\begin{cases}
\rho,&\kappa\le0,\\
\min\{\rho,\pi/(2\sqrt{\kappa+1})\},&\kappa>0.
\end{cases}
\]

The point here is that applying this lower bound after a scale depending on the hole radius makes the effective curvature tend to zero while keeping the deleted ball at a fixed small size. This matches Schott's Euclidean correspondence to second order in the ratio.

## Proof

### 1. Hausdorff distance

For \(r\) below the injectivity radius at \(a\), radial geodesics show
\[
d_{\mathrm H}(X_r,M)=r.
\]
Indeed \(a\) is exactly distance \(r\) from \(X_r\), while every point of \(B_r(a)\) is at distance at most \(r\) from the complement.

### 2. A quadratic normal-coordinate bilipschitz estimate

Fix normal coordinates centered at \(a\), identifying \(T_aM\) with \(\mathbb R^n\). The standard normal-coordinate expansion gives
\[
g_{ij}(x)=\delta_{ij}+O(|x|^2).
\]
After shrinking the radius below the convexity radius, minimizing geodesics between points of \(\overline B_r(a)\) remain in that ball, while Euclidean line segments in \(B_r(0)\) remain in \(B_r(0)\). Comparing lengths in both directions therefore yields a constant \(C\) and
\[
K_r=1+O_{M,a}(r^2)
\]
such that
\[
K_r^{-1}|u-v|
\le d_M(\exp_a u,\exp_a v)
\le K_r|u-v|
\qquad (|u|,|v|\le r).
\]
Equivalently, \(\exp_a^{-1}\) is \(K_r\)-bilipschitz on \(\overline B_r(a)\).

### 3. Upper bound with cubic error

Write
\[
\ell_n=\sqrt{\frac{2(n+1)}n}=2c_n.
\]
Schott's Euclidean correspondence for \(\mathbb R^n\) and
\(\mathbb R^n\setminus B_r(0)\) has distortion \(\ell_n r\), and its non-fixed pairs have motion at most \(\ell_n r\). Transport this correspondence to \(\overline B_r(a)\) by the exponential map and fix \(X_r\) pointwise, exactly as in the proof of Schott's Theorem 3.6.

Using the \(K_r\)-bilipschitz estimate and Schott's elementary bilipschitz distortion inequality gives
\[
\operatorname{dis}(R_r^M)
\le
r\Bigl(K_r\ell_n+2(K_r-K_r^{-1})\Bigr).
\]
Hence
\[
d_{\mathrm{GH}}(X_r,M)
\le
\frac r2\Bigl(K_r\ell_n+2(K_r-K_r^{-1})\Bigr).
\]
Since \(K_r=1+O(r^2)\),
\[
d_{\mathrm{GH}}(X_r,M)
\le c_n r+O_{M,a}(r^3).
\]

### 4. Lower bound by curvature-vanishing rescaling

Let
\[
\kappa=\max\{0,\sup_M\operatorname{sec}_g\}.
\]
For \(n\ge2\), choose once and for all a constant
\[
0<h<\frac{\pi}{8(c_n+1)}.
\]
For each sufficiently small \(r\), scale the Riemannian metric by
\[
g_r=\left(\frac hr\right)^2g.
\]
Distances, Hausdorff distances, and Gromov--Hausdorff distances all scale by \(h/r\). Moreover,
\[
X_r=M\setminus B_h^{g_r}(a),
\qquad
d_{\mathrm H}^{g_r}(X_r,M)=h.
\]
An upper sectional-curvature bound for \(g_r\) is
\[
\kappa_r=\kappa\left(\frac rh\right)^2,
\]
and the convexity radius is multiplied by \(h/r\).

Apply Adams--Frick--Majhi--McBride Theorem 4 to \((M,g_r)\), with \(X=X_r\) and \(Y=M\). If \(\kappa=0\), the second branch of their minimum tends to infinity. If \(\kappa>0\), its parameter \(\tau_r\) tends to \(\pi/2\). Our fixed choice of \(h\) is strictly below the limiting threshold
\[
\frac{\pi}{4(c_n+1)},
\]
so for all sufficiently small \(r\) the first branch is the smaller one. Therefore
\[
d_{\mathrm{GH}}^{g_r}(X_r,M)\ge \alpha(n,\kappa_r)h.
\]
Scaling back gives
\[
d_{\mathrm{GH}}^g(X_r,M)\ge \alpha(n,\kappa_r)r.
\]

When \(\kappa=0\), \(\alpha(n,\kappa_r)=c_n\). When \(\kappa>0\), put
\[
z_r=\frac{\pi}{2}\sqrt{\frac{\kappa_r}{1+\kappa_r}}.
\]
Since \(\sin z/z=1-z^2/6+O(z^4)\),
\[
\alpha(n,\kappa_r)
=
c_n\left(
1-\frac{\pi^2}{24}\kappa_r+O(\kappa_r^2)
\right)
=
c_n-O_{M,n}(r^2).
\]
Consequently,
\[
d_{\mathrm{GH}}(X_r,M)\ge c_n r-O_{M,n}(r^3).
\]

Together with the upper bound,
\[
d_{\mathrm{GH}}(X_r,M)=c_n r+O_{M,a}(r^3).
\]

### 5. Dimension one

After rescaling, every connected closed one-dimensional Riemannian manifold is a circle. Adams--Frick--Majhi--McBride Theorem 2 gives
\[
d_{\mathrm{GH}}(X,M)\ge
\min\{d_{\mathrm H}(X,M),\,\operatorname{length}(M)/12\}.
\]
For \(X=X_r\) and sufficiently small \(r\), this lower bound is \(r\), while the inclusion in the common ambient circle gives
\[
d_{\mathrm{GH}}(X_r,M)\le d_{\mathrm H}(X_r,M)=r.
\]
Thus equality holds.

## Consequences

1. **Universal tangent-hole coefficient.** The limit depends only on the dimension:
   \[
   \lim_{r\downarrow0}\frac{d_{\mathrm{GH}}(M\setminus B_r(a),M)}r
   =\sqrt{\frac{n+1}{2n}}.
   \]

2. **Quadratic convergence of the ratio.**
   \[
   \frac{d_{\mathrm{GH}}(M\setminus B_r(a),M)}
   {d_{\mathrm H}(M\setminus B_r(a),M)}
   =
   \sqrt{\frac{n+1}{2n}}+O(r^2).
   \]

3. **Euclidean calibration.** In Euclidean space the same deleted-ball family attains \(c_n\) exactly at every scale. On a smooth manifold, normal-coordinate distortion is quadratic and the rescaled sectional curvature is quadratic, explaining why this proof loses only a cubic term in the unnormalized distance.

## Limitations

- Closedness is used for the global lower bound through Adams--Frick--Majhi--McBride Theorem 4. The upper \(c_n r+O(r^3)\) estimate is local and does not require compactness.
- The \(O(r^3)\) estimate does not identify a curvature-dependent cubic coefficient and does not assert that the cubic order is optimal.
- The statement concerns the subspace metric on the complement, not its intrinsic path metric.
- The motivating converse paper is very recent, so unindexed parallel work remains a residual originality risk.

## References

- Paul Schott, *A converse bound for \(d_{\mathrm{GH}}\) vs. \(d_{\mathrm H}\) for Euclidean space and Riemannian manifolds*, arXiv:2609.12625v1, 2026. https://arxiv.org/abs/2609.12625
- Henry Adams, Florian Frick, Sushovan Majhi, Nicholas McBride, *Hausdorff vs Gromov--Hausdorff distances*, arXiv:2309.16648v5, 2025. https://arxiv.org/abs/2309.16648
- Henry Adams, Semeon A. Bogatyi, Florian Frick, Daniil A. Ilyukhin, Alexander O. Ivanov, Ivan N. Mikhailov, Alexey A. Tuzhilin, Anton A. Vikhrov, *Gromov--Hausdorff distance and Jung constant of finite-dimensional normed spaces*, arXiv:2607.18447v1, 2026. https://arxiv.org/abs/2607.18447
