# Exact aperture blow-up above the Hausdorff–Choquet rough-maximal threshold

## Finding

Let \(n\ge2\), \(0<\alpha\le n-1\), and let
\[
u_{\theta,r}
=
\frac{\mathbf 1_{B(\theta,r)}}{\sigma(B(\theta,r))}
\]
be the normalized kernel of a geodesic cap \(B(\theta,r)\subset\mathbb S^{n-1}\). Define
\[
\mathfrak C_{n,\alpha}(r)
=
\sup_{f\ne0}
\frac{\|\mathcal M_{u_{\theta,r}}f\|_{L^{1,\infty}(\mathbb R^n)}}
{\|u_{\theta,r}\|_{\mathcal{HC}_\alpha}\,\|f\|_{L^1(\mathbb R^n)}}.
\]
For all sufficiently small \(r\), uniformly in \(\theta\),
\[
\mathfrak C_{n,\alpha}(r)
\asymp_{n,\alpha}
r^{\,n-1-2\alpha}.
\]
Hence the supercritical failure of the Hausdorff–Choquet weak-type estimate has an exact aperture law:
\[
\alpha>\frac{n-1}{2}
\quad\Longrightarrow\quad
\mathfrak C_{n,\alpha}(r)
\asymp_{n,\alpha}
r^{-(2\alpha-(n-1))}.
\]
At the critical exponent the cap constant stays of order one; below it, the normalized cap ratio tends to zero.

Equivalently, for \(\alpha>(n-1)/2\), if cap kernels are regularized by imposing a minimum angular radius \(\varepsilon\), the optimal normalized weak-type constant over those caps grows exactly like
\[
\varepsilon^{-(2\alpha-(n-1))}
\]
as \(\varepsilon\downarrow0\).

## Assumptions and scope

The rough maximal operator is
\[
\mathcal M_\Omega f(x)
=
\sup_{R>0}
\frac1{R^n}
\int_{|y|<R}
|f(x-y)|
\left|\Omega\!\left(\frac y{|y|}\right)\right|\,dy.
\]
The Hausdorff–Choquet quasi-norm is the scale \(\mathcal{HC}_\alpha\) introduced in the primary source. The weak norm is
\[
\|F\|_{L^{1,\infty}}
=
\sup_{\lambda>0}
\lambda\,|\{x:|F(x)|>\lambda\}|.
\]
No assertion is made about arbitrary supercritical kernels after an angular cutoff. The result concerns the canonical normalized cap family, which is exactly the family used to detect the sharp exponent in the source.

## Proof

The primary source proves two estimates for the same normalized cap kernel.

First, its single-geodesic-ball theorem gives a radius- and center-independent weak-type estimate
\[
\|\mathcal M_{u_{\theta,r}}f\|_{L^{1,\infty}}
\le
C_n\|f\|_1.
\]
Thus the ordinary weak operator norm
\[
W_{\theta,r}
:=
\sup_{f\ne0}
\frac{\|\mathcal M_{u_{\theta,r}}f\|_{L^{1,\infty}}}{\|f\|_1}
\]
satisfies \(W_{\theta,r}\le C_n\).

Second, the source proves for every \(0<\alpha\le n-1\) that
\[
\|u_{\theta,r}\|_{\mathcal{HC}_\alpha}
\asymp_{n,\alpha}
r^{2\alpha-(n-1)}
\]
for small caps.

A matching lower bound for \(W_{\theta,r}\) is already contained in the source's sharpness test. Let
\[
f=\mathbf 1_{B_{\mathbb R^n}(0,2)}.
\]
For every \(x\in B_{\mathbb R^n}(0,1)\), choosing radial scale \(R=1\) gives
\[
\mathcal M_{u_{\theta,r}}f(x)\ge c_n,
\]
because \(f(x-y)=1\) whenever \(|y|<1\) and the cap kernel has spherical integral one. Therefore
\[
\|\mathcal M_{u_{\theta,r}}f\|_{L^{1,\infty}}
\ge
\frac{c_n}{2}|B_{\mathbb R^n}(0,1)|.
\]
Since \(\|f\|_1=|B_{\mathbb R^n}(0,2)|\), this yields
\[
W_{\theta,r}\ge c'_n>0
\]
uniformly in \(\theta\) and \(r\).

Consequently
\[
W_{\theta,r}\asymp_n1.
\]
Dividing by the exact cap quasi-norm gives
\[
\mathfrak C_{n,\alpha}(r)
=
\frac{W_{\theta,r}}
{\|u_{\theta,r}\|_{\mathcal{HC}_\alpha}}
\asymp_{n,\alpha}
r^{n-1-2\alpha}.
\]
For \(\alpha>(n-1)/2\), this is
\[
r^{-(2\alpha-(n-1))}.
\]
The minimum-aperture formulation follows because this power is decreasing in \(r\) throughout the supercritical regime, so among \(r\ge\varepsilon\) the worst small cap occurs at scale comparable to \(\varepsilon\).

## Verification

The full primary text was inspected at the single-cap theorem and at the sharp Hausdorff–Choquet exponent argument. The single-cap theorem states that the weak-\((1,1)\) constant is independent of both cap location and cap radius. The cap quasi-norm computation gives the precise power \(r^{2\alpha-(n-1)}\). The sharpness proof uses the same normalized cap kernel and the same fixed indicator test used above, so the lower weak operator norm is radius-independent.

All three ingredients are inequalities with constants depending only on the displayed structural parameters. No numerical experiment, limiting heuristic, or interpolation argument is used.

## Relationship to prior work

Chen and Ji prove that \(\alpha=(n-1)/2\) is the sharp Hausdorff–Choquet exponent for a uniform weak-\((1,1)\) theorem. Above the threshold they show nonexistence of a finite uniform constant by taking normalized caps with radius tending to zero. Separately, they prove a uniform weak bound for every single normalized cap and compute its \(\mathcal{HC}_\alpha\) quasi-norm.

The finding combines those two quantitative statements with the fixed indicator lower test to identify the exact power of divergence, rather than only the qualitative failure of a uniform constant. Targeted searches using the source identifier, normalized cap kernels, aperture dependence, Hausdorff–Choquet supercriticality, and equivalent weak-norm formulations did not locate this two-sided rate as a published statement.

The older Christ–Rubio de Francia theorem concerns the \(L\log L\) angular condition and does not contain the Hausdorff–Choquet aperture parameter. It therefore does not imply the rate above.

## Limitations

The two-sided law is for normalized geodesic-cap kernels. It is not a classification of all supercritical \(\mathcal{HC}_\alpha\) kernels.

The implicit constants are not optimized.

The result quantifies failure of the Hausdorff–Choquet normalization above the critical dimension; it does not resolve Stein's open weak-\((1,1)\) problem for arbitrary \(L^1\) angular kernels.

## References

1. Y. Chen and Z. Ji, *Hausdorff–Choquet Angular Spaces and Weak-Type \((1,1)\) Bounds for Rough Maximal Operators*, arXiv:2609.03785v1, 2026.
2. M. Christ and J. L. Rubio de Francia, *Weak type \((1,1)\) bounds for rough operators. II*, Inventiones Mathematicae 93 (1988), 225–237.
