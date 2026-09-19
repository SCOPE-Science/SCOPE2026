# The Euclidean Jung constant is the universal local Hausdorff–Gromov–Hausdorff constant

## Result

Let \((M,g)\) be a closed connected Riemannian \(n\)-manifold, \(n\ge 2\), and put
\[
c_n:=\sqrt{\frac{n+1}{2n}}.
\]
For a nonempty compact subset \(A\subset M\), write
\[
h(A):=d_{\mathrm H}(A,M).
\]

There are constants \(C_M<\infty\) and \(h_0>0\) such that every compact \(A\subset M\) with \(0<h:=h(A)<h_0\) satisfies
\[
\boxed{\quad d_{\mathrm{GH}}(A,M)\ge c_n h-C_Mh^3.\quad}
\]
The leading constant is sharp on every \(M\). More precisely, for every \(a\in M\), if
\[
A_r:=M\setminus B_r(a),
\]
then as \(r\downarrow0\),
\[
\boxed{\quad d_{\mathrm{GH}}(A_r,M)=c_n r+O_M(r^3),\qquad
d_{\mathrm H}(A_r,M)=r.\quad}
\]

Consequently, if
\[
\mathcal C_M(h):=
\inf\left\{
\frac{d_{\mathrm{GH}}(A,M)}{d_{\mathrm H}(A,M)}:
A\subset M\text{ compact},\ d_{\mathrm H}(A,M)=h
\right\},
\]
then
\[
\boxed{\quad \mathcal C_M(h)=c_n+O_M(h^2),\qquad
\lim_{h\downarrow0}\mathcal C_M(h)=\sqrt{\frac{n+1}{2n}}.\quad}
\]

Thus the optimal infinitesimal converse constant relating Gromov–Hausdorff and Hausdorff distance is the Euclidean Jung constant in every closed Riemannian manifold, independently of the sign of sectional curvature.

## A scale-sensitive lower bound

The lower estimate is a quantitative refinement of the preceding limit.

Let
\[
\kappa_+:=\max\{0,\sup_M\sec_g\},
\]
and define, for \(q\ge0\),
\[
\alpha_n(q):=
\begin{cases}
c_n,&q=0,\\[4pt]
c_n\,
\dfrac{\sin\!\left(\frac{\pi}{2}\sqrt{\frac{q}{q+1}}\right)}
{\frac{\pi}{2}\sqrt{\frac{q}{q+1}}},&q>0.
\end{cases}
\]
Choose any fixed
\[
0<\delta<\frac{\pi}{4(c_n+1)}.
\]
Then, after decreasing \(h_0\) if necessary,
\[
\boxed{\quad
\frac{d_{\mathrm{GH}}(A,M)}{h(A)}
\ge
\alpha_n\!\left(\frac{\kappa_+h(A)^2}{\delta^2}\right)
\quad}
\]
for every compact \(A\subset M\) with \(0<h(A)<h_0\).

Since
\[
\alpha_n(q)=c_n\left(1-\frac{\pi^2}{24}q+O_n(q^2)\right)
\qquad(q\downarrow0),
\]
this gives the cubic lower error above. In the nonpositively curved case \(\kappa_+=0\), it recovers the exact lower coefficient \(c_n\).

## Proof of the lower bound

Adams–Frick–Majhi–McBride prove the following bound for a closed Riemannian \(n\)-manifold with sectional curvature bounded above by \(q\ge0\):
\[
d_{\mathrm{GH}}(X,M)
\ge
\min\left\{
\alpha_n(q)d_{\mathrm H}(X,M),
\frac{\alpha_n(q)\tau}{2\alpha_n(q)+2}
\right\},
\]
where, for \(q>0\),
\[
\tau=\min\left\{\rho(M),\frac{\pi}{2\sqrt{q+1}}\right\},
\]
and \(\rho(M)\) is the convexity radius. Their published theorem is stated for a fixed metric, so for positive curvature its displayed coefficient is strictly smaller than \(c_n\).

The key observation is to optimize that theorem under a change of scale.

Let \(h=d_{\mathrm H}(A,M)>0\), fix \(\delta\) as above, and rescale the Riemannian metric by
\[
g_h=\lambda^2g,\qquad \lambda=\frac{\delta}{h}.
\]
Under this rescaling,
\[
d_{\mathrm H}^{g_h}(A,M)=\delta,\qquad
d_{\mathrm{GH}}^{g_h}(A,M)=\lambda d_{\mathrm{GH}}^g(A,M),
\]
the curvature upper bound becomes
\[
q_h=\frac{\kappa_+}{\lambda^2}
=\frac{\kappa_+h^2}{\delta^2},
\]
and the convexity radius becomes \(\lambda\rho(M)\).

If \(\kappa_+>0\), the corresponding cutoff satisfies
\[
\tau_h
=
\min\left\{
\frac{\delta\rho(M)}h,\,
\frac{\pi}{2\sqrt{1+q_h}}
\right\}
\longrightarrow \frac{\pi}{2}.
\]
Also \(\alpha_n(q_h)\to c_n\). Because
\[
\delta<\frac{\pi}{4(c_n+1)}
=
\lim_{h\downarrow0}
\frac{\tau_h}{2(\alpha_n(q_h)+1)},
\]
for all sufficiently small \(h\) the first term in the minimum is the smaller one. Hence
\[
\lambda d_{\mathrm{GH}}^g(A,M)
\ge
\alpha_n(q_h)\delta.
\]
Dividing by \(\lambda=\delta/h\) gives
\[
\frac{d_{\mathrm{GH}}^g(A,M)}h
\ge
\alpha_n\!\left(\frac{\kappa_+h^2}{\delta^2}\right).
\]
If \(\kappa_+=0\), use curvature upper bound \(0\); after rescaling the cutoff coming from the convexity radius tends to infinity, and the same conclusion holds with \(\alpha_n(0)=c_n\).

The Taylor expansion follows from \(\sin x/x=1-x^2/6+O(x^4)\).

## Cubic upper bound from a deleted geodesic ball

Paul Schott recently constructed, for every point \(a\) of a Riemannian manifold and all sufficiently small \(r\), a correspondence between \(M\) and
\[
A_r=M\setminus B_r(a)
\]
obtained by transporting the Euclidean optimal correspondence through normal coordinates. His estimate yields, for every fixed \(L>1\),
\[
d_{\mathrm{GH}}(A_r,M)\le Lc_n r
\]
for small enough \(r\).

Tracking the normal-coordinate distortion gives the sharper error needed here.

For a closed smooth Riemannian manifold, the normal-coordinate expansion
\[
g_{ij}(x)=\delta_{ij}+O_M(|x|^2)
\]
implies that for sufficiently small \(r\), the inverse exponential map on \(\overline{B_r(a)}\) is \(K_r\)-bilipschitz with
\[
K_r=1+O_M(r^2).
\]
Indeed, the upper metric estimate follows by transporting Euclidean line segments in the tangent ball; for the lower estimate, a minimizing geodesic joining two points of \(B_r(a)\) stays in a fixed multiple of that ball, where the same normal-coordinate estimate applies.

Schott's Euclidean correspondence has
\[
\operatorname{dis}(R_r)=r\ell_n,\qquad
\operatorname{Mot}(R_r)\le r\ell_n,
\qquad
\ell_n=\sqrt{\frac{2(n+1)}n}=2c_n.
\]
After transport to \(M\), his proof gives
\[
\operatorname{Mot}(R_r^M)\le rK_r\ell_n
\]
and
\[
\operatorname{dis}(R_r^M)
\le
r\left(K_r\ell_n+2(K_r-K_r^{-1})\right).
\]
Therefore
\[
d_{\mathrm{GH}}(A_r,M)
\le
\frac r2\left(K_r\ell_n+2(K_r-K_r^{-1})\right)
=
c_n r+O_M(r^3).
\]
For \(r\) below the injectivity radius,
\[
d_{\mathrm H}(A_r,M)=r.
\]
Combining this upper estimate with the scale-sensitive lower bound proves
\[
d_{\mathrm{GH}}(A_r,M)=c_nr+O_M(r^3)
\]
and then the asserted asymptotic formula for \(\mathcal C_M(h)\).

## Context and improvement direction

Adams–Frick–Majhi–McBride proved a lower Hausdorff-to-Gromov–Hausdorff bound on closed Riemannian manifolds with a coefficient \(\alpha(n,\kappa)\) depending on a fixed upper sectional-curvature bound. For \(\kappa>0\), their displayed coefficient is smaller than \(c_n\).

Schott subsequently proved that the Euclidean coefficient \(c_n\) is attained exactly by the complement of a ball in Euclidean space and transferred that construction to arbitrary Riemannian manifolds, obtaining an upper ratio arbitrarily close to \(c_n\). He explicitly identified tightness with the earlier lower bound in the nonpositive-curvature case.

The result above closes the remaining leading-order gap for positive curvature: after optimizing the earlier lower theorem under metric rescaling, the relevant curvature parameter is \(\kappa_+h^2\), not the fixed ambient \(\kappa_+\). Hence positive curvature affects only higher-order terms as the sample becomes dense. The normal-coordinate refinement of Schott's correspondence shows that the two sides meet to order \(O(h^2)\) in the ratio.

## Checks and limiting cases

- In Euclidean space, Schott's deleted-ball model has the exact ratio \(c_n\), consistent with the leading term.
- If \(\sec\le0\), the scale-sensitive lower bound is exactly \(c_n h\), agreeing with the known nonpositive-curvature sharp constant.
- On positively curved manifolds, the fixed-metric coefficient of Adams–Frick–Majhi–McBride can be strictly below \(c_n\), while the new estimate tends to \(c_n\) because the dimensionless curvature seen at Hausdorff scale \(h\) is \(O(\kappa h^2)\).
- Dimension \(1\) is excluded from the statement because the circle has a stronger exact small-scale equality \(d_{\mathrm{GH}}=d_{\mathrm H}\).

## Limitations

The theorem identifies the universal leading constant and an \(O(h^2)\) error in the ratio, but it does not identify the optimal second-order coefficient. The deleted-ball correspondence is not claimed to be exactly optimal on a curved manifold. No classification of all asymptotically extremizing subsets is given. The result concerns smooth closed Riemannian manifolds; extensions to manifolds with boundary, singular spaces, or weaker curvature structures are not asserted.

## References

1. H. Adams, F. Frick, S. Majhi, N. McBride, *Hausdorff vs Gromov–Hausdorff Distances*, Discrete & Computational Geometry 75 (2026), 1217–1246. DOI: https://doi.org/10.1007/s00454-025-00722-9 ; arXiv: https://arxiv.org/abs/2309.16648
2. P. Schott, *A converse bound for \(d_{\mathrm{GH}}\) vs. \(d_{\mathrm H}\) for Euclidean space and Riemannian manifolds*, arXiv:2609.12625 (2026). https://arxiv.org/abs/2609.12625
3. H. Adams, S. A. Bogatyi, F. Frick, D. A. Ilyukhin, A. O. Ivanov, I. N. Mikhailov, A. A. Tuzhilin, A. A. Vikhrov, *Gromov–Hausdorff distance and Jung constant of finite-dimensional normed spaces*, arXiv:2607.18447 (2026). https://arxiv.org/abs/2607.18447
