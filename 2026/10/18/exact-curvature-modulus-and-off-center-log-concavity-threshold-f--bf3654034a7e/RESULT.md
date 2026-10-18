# Exact curvature modulus and off-center log-concavity threshold for symmetric triple-Gaussian mixtures

## Finding

Consider an equal-variance Gaussian location mixture with a central mass and two equal side masses. Its global potential-convexity modulus admits a closed formula, giving a complete and sharp log-concavity phase diagram. There is a transition from a central worst-curvature point to two off-center worst-curvature points. In particular, a strictly unimodal mixture can fail log-concavity at two off-center locations, even while arbitrarily close in total variation to a single Gaussian.

Precisely, let \(a>0\), \(\sigma>0\), and \(0<w<1\). Put
\[
 f(y)=w\varphi_\sigma(y)+\frac{1-w}{2}\bigl(\varphi_\sigma(y-a)+\varphi_\sigma(y+a)\bigr),\qquad
 \varphi_\sigma(y)=\frac{e^{-y^2/(2\sigma^2)}}{\sqrt{2\pi}\,\sigma}.
\]
Set \(s=a/\sigma\) and \(c=w e^{s^2/2}/(1-w)\). For the potential \(U=-\log f\), define its optimal global convexity modulus \(\kappa=\inf_{y\in\mathbb R}U''(y)\). Then
\[
\boxed{\kappa=\frac{1-s^2 M(c)}{\sigma^2}},\qquad
M(c)=\begin{cases}\dfrac1{1+c},&0<c\le2,\\[3pt]
\dfrac{c^2}{4(c^2-1)},&c\ge2.
\end{cases}
\]
The worst-curvature location is \(y=0\) for \(c\le2\); for \(c>2\) it consists exactly of the two points
\[
 y=\pm\frac{\sigma}{s}\operatorname{arcosh}\left(c-\frac2c\right).
\]
Consequently, \(f\) is log-concave exactly in the following cases:
\[
\boxed{\begin{array}{c|c}
\text{normalized separation }s&\text{required }c\\ \hline
0<s\le1&\text{every }c>0\\
1<s\le\sqrt3&c\ge s^2-1\\
\sqrt3<s<2&c\ge \dfrac2{\sqrt{4-s^2}}\\
s\ge2&\text{no finite }c>0.
\end{array}}
\]
In the middle two lines, the equivalent threshold for the central mixture weight is \(w\ge c_*(s)/(c_*(s)+e^{s^2/2})\), with \(c_*(s)\) given by the applicable formula. On the critical curve \(\kappa=0\) the density is log-concave but is not strongly log-concave. Where \(\kappa>0\), it is strongly log-concave with exact modulus \(\kappa\).

## Assumptions and scope

All assertions cover every \(a>0\), \(\sigma>0\), \(0<w<1\) and every real observation \(y\). All three Gaussian components have the same strictly positive variance, and the side weights are equal. The excluded degenerate case \(w=1\) is a single Gaussian; limits in \(w\) do not authorize substituting \(w=1\) into the finite-mixture classification.

## Proof

**1. An exact expression for the potential curvature.** Rescale \(u=y/\sigma\). The three normal densities combine into
\[
 f(\sigma u)=\frac{(1-w)e^{-s^2/2}}{\sqrt{2\pi}\,\sigma}\,e^{-u^2/2}
 \bigl(c+\cosh(su)\bigr).
\]
This is a strictly positive, normalized density, because the defining mixture weights sum to one. Twice differentiating gives
\[
 \sigma^2U''(\sigma u)=1-s^2R_c(\cosh(su)),\qquad
 R_c(z)=\frac{1+cz}{(c+z)^2},\quad z\ge1.
\]
Since \(u\mapsto\cosh(su)\) ranges over \([1,\infty)\), finding the best global curvature constant reduces exactly to maximizing \(R_c\) over that half-line.

**2. Global optimization with exact algebraic certificates.** Differentiate:
\[
 R_c'(z)=\frac{c^2-cz-2}{(c+z)^3}.
\]
For \(0<c\le2\), the function decreases over \([1,\infty)\), so its maximum occurs at \(z=1\). More explicitly,
\[
 \frac1{1+c}-R_c(z)
 =\frac{(z-1)(z+1+c-c^2)}{(1+c)(c+z)^2}\ge0,
\]
because \(z+1+c-c^2\ge(2-c)(1+c)\ge0\). If \(c\ge2\), completing the square yields
\[
 \frac{c^2}{4(c^2-1)}-R_c(z)
 =\frac{(c^2-cz-2)^2}{4(c^2-1)(c+z)^2}\ge0.
\]
Its equality point is \(z_*=c-2/c\). This is in \([1,\infty)\) exactly when \(c\ge2\); for \(c>2\) it corresponds to the stated two nonzero locations. The two branches agree at \(c=2\). This proves the global infimum formula with attainment, not merely a local curvature test.

**3. The exact phase diagram.** Log-concavity of the everywhere-positive twice differentiable density is equivalent to \(U''(y)\ge0\) for all \(y\), namely \(s^2M(c)\le1\). On \(c\le2\), this is \(c\ge s^2-1\). On \(c\ge2\), it is
\[
 (4-s^2)c^2\ge4.
\]
Combining the inequalities at \(c=2\) gives the cases \(0<s\le1\), \(1<s\le\sqrt3\), \(\sqrt3<s<2\), and \(s\ge2\) exactly as stated. At \(s=2\), the second inequality would require \(0\ge4\), and the first is impossible; hence there is no overlooked equality case. Critical equality gives \(\kappa=0\), whereas \(\kappa>0\) is exactly the largest valid uniform strong-convexity parameter.

At the branch junction \(s=\sqrt3\), \(c=2\), Taylor expansion of the exact expression shows, as \(u\to0\),
\[
 (\log f(\sigma u))''_{u}=-\frac{u^4}{4}+O(u^6).
\]
Thus the critical worst-curvature contact is quartic at the center. For \(\sqrt3<s<2\) on the critical curve, the zero-curvature points instead lie strictly off-center.

**4. Strict unimodality does not save global log-concavity.** The normalized log-density derivative is
\[
 \frac{d}{du}\log f(\sigma u)=-u+\frac{s\sinh(su)}{c+\cosh(su)}.
\]
If \(c>\sinh(s^2)\), then for \(0<u\le s\), monotonicity of \(v\mapsto\sinh(v)/v\) gives
\[
\frac{s\sinh(su)}{c+\cosh(su)}
<\frac{s\sinh(su)}c\le u\frac{\sinh(s^2)}c<u.
\]
For \(u\ge s\), the same positive term is smaller than \(s\le u\). Symmetry yields a strictly positive derivative for negative \(u\), hence a unique global mode at zero.

Take \(s=2\), \(c=32\), corresponding to \(w=32/(32+e^2)\). Since \(e<11/4\), we have \(\sinh4<e^4/2<32\), so this mixture is strictly unimodal. But the exact curvature formula gives
\[
 \sigma^2U''(0)=\frac{29}{33}>0,\qquad
 \min_{y}\sigma^2U''(y)=-\frac1{1023}<0,
\]
with the negative minimum at \(y=\pm(\sigma/2)\operatorname{arcosh}(511/16)\). It is therefore strictly unimodal but not log-concave, with loss of convexity away from its mode.

More generally, hold any \(s\ge2\) fixed and let \(c\to\infty\). Then \(w=c/(c+e^{s^2/2})\to1\), the total variation distance to \(N(0,\sigma^2)\) is at most \(1-w\to0\), and the density is strictly unimodal eventually because \(c>\sinh(s^2)\). Nonetheless \(\kappa<0\) for every finite \(c\), and its off-center worst-curvature locations tend to infinity. Hence the loss of log-concavity can be confined to increasingly remote tails under an arbitrarily small contamination.

## Verification

All global conclusions follow from the displayed rational identities and inequalities. The standalone script `verify.py` checks both factorization identities with exact rational arithmetic, an independent evaluation of the original Gaussian mixture's curvature against the derived expression at deterministic test points, and the exact special-example constants. These finite checks are secondary checks of the derivations, not substitutes for the all-parameter proof. Running `python3 verify.py` requires only the Python standard library.

## Relationship to prior work

Cule, Samworth, and Stewart (2010, Section 2) discuss the sharp two-component equal-variance normal location-mixture log-concavity threshold; it does not classify the symmetric three-component mixture. Lau, Liu, and Pock (arXiv:2305.15988, Sections 2.1 and 6.1 and Appendix 1) give general Gaussian-mixture potentials and Hessian identities for sampling experiments, but not their exact global curvature extrema in this family. Cheng, Wang, Zhang, and Zhu (arXiv:2306.10506, Section 4.3.1 and Lemma 4) establish local sampling and nonsharp general Hessian bounds for equal-covariance mixtures, not the best curvature modulus or its phase transition. The present calculation specializes those broad contexts to an exact three-point distribution and determines the full parameter boundary and extremizing locations.

## Limitations

This is a one-dimensional, symmetric, equal-variance, three-component family; no classification is claimed for unequal side weights, unequal component variances, or larger supports. The curvature modulus is a pointwise global constant; it does not independently establish a mixing-time theorem for any numerical sampler. The total-variation approximation statement does not claim preservation of log-concavity under convergence. Search-based comparison cannot exclude an equivalent earlier result under different terminology.

## References

1. M. Cule, R. Samworth, and M. Stewart, *Maximum likelihood estimation of a multi-dimensional log-concave density*, Journal of the Royal Statistical Society: Series B **72** (2010), 545–607, Section 2. DOI: 10.1111/j.1467-9868.2010.00753.x. https://doi.org/10.1111/j.1467-9868.2010.00753.x
2. T. T.-K. Lau, H. Liu, and T. Pock, *Non-Log-Concave and Nonsmooth Sampling via Langevin Monte Carlo Algorithms*, first publicly posted 25 May 2023, arXiv:2305.15988, Sections 2.1, 6.1 and Appendix 1. https://arxiv.org/abs/2305.15988
3. X. Cheng, B. Wang, J. Zhang, and Y. Zhu, *Fast Conditional Mixing of MCMC Algorithms for Non-log-concave Distributions*, first publicly posted 18 June 2023, arXiv:2306.10506, Section 4.3.1. https://arxiv.org/abs/2306.10506
