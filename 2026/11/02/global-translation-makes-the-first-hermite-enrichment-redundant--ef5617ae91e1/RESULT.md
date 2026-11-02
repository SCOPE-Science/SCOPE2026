# Global translation makes the first Hermite enrichment redundant for positive Gaussian mixtures

## Finding

For every finite, nonzero, positive Borel measure \(\nu\) on \(\mathbb R\), let
\[
u_\nu(x)=\int_{\mathbb R}\phi_0(x-t)\,d\nu(t),
\qquad
\phi_0(x)=\pi^{-1/4}e^{-x^2/2}.
\]
Here \(\nu\) denotes the mixing measure and \(u_\nu\) the target function. For each translation \(b\in\mathbb R\), let \(P_{m,b}\) be the orthogonal \(L^2(\mathbb R)\) projector onto the span of the first \(m+1\) normalized Hermite functions translated by \(b\). Then
\[
\boxed{\inf_b\|u_\nu-P_{0,b}u_\nu\|_2^2
=\inf_b\|u_\nu-P_{1,b}u_\nu\|_2^2.}
\]
The complete sets of optimal translation parameters are identical for the two approximation spaces. If \(\nu\) is not a single positive point mass, then
\[
\boxed{\inf_b\|u_\nu-P_{2,b}u_\nu\|_2^2
<\inf_b\|u_\nu-P_{1,b}u_\nu\|_2^2.}
\]
Thus the first added Hermite degree gives no best-error improvement once the center is freely optimized, while the second added degree gives a strictly positive improvement for every genuine positive mixture.

For an equal-weight two-Gaussian target with centers \(\pm a\), the common optimal center exhibits the sharp bifurcation \(a=\sqrt2\): it is uniquely zero for \(0<a\le\sqrt2\) and consists of exactly two nonzero symmetric translations for \(a>\sqrt2\).

## Assumptions and scope

All functions and inner products are real and on \(L^2(\mathbb R)\). Set
\[
\phi_n(x)=\frac{H_n(x)e^{-x^2/2}}{(2^n n!\sqrt\pi)^{1/2}},\quad n\in\mathbb N_0,
\]
using physicists' Hermite polynomials. Write
\[
V_m(b)=\operatorname{span}\{\phi_0(\cdot-b),\ldots,\phi_m(\cdot-b)\},
\qquad P_{m,b}:L^2\longrightarrow V_m(b).
\]
The Gaussian width is fixed at one, and only the translation \(b\) is optimized. The target is a Gaussian location mixture \(u_\nu=\phi_0*\nu\) of a finite nonzero **positive** measure; \(\nu\) need not be discrete, compactly supported, or symmetric. Finiteness ensures \(u_\nu\in L^2\) because \(\|u_\nu\|_2\le\nu(\mathbb R)\). Results do not apply to arbitrary sign-changing targets or to free simultaneous width optimization.

## Proof

**1. Exact coefficients.** Put
\[
c_j(b)=\langle u_\nu,\phi_j(\cdot-b)\rangle.
\]
A direct Gaussian integral (or the Hermite translation generating function) gives, with \(d=t-b\),
\[
\begin{aligned}
c_0(b)&=\int e^{-d^2/4}\,d\nu(t)>0,\\
c_1(b)&=\frac{1}{\sqrt2}\int d\,e^{-d^2/4}\,d\nu(t),\\
c_2(b)&=\frac{1}{2\sqrt2}\int d^2e^{-d^2/4}\,d\nu(t)\ge0.
\end{aligned}
\]
Positivity of the integrand shows \(c_2(b)=0\) if and only if \(\nu\) is concentrated at the single point \(b\). These expressions are smooth in \(b\); dominated convergence is valid on compact \(b\)-sets because Gaussian-weighted polynomials are uniformly bounded in \(t\). Moreover each tends to zero as \(|b|\to\infty\), since the integrands are bounded and converge pointwise to zero for each fixed \(t\). Hence all captured energies considered below attain their positive global maxima.

**2. Derivative cancellation.** Orthogonality gives
\[
Q_0(b):=\|P_{0,b}u_\nu\|_2^2=c_0(b)^2,
\qquad
Q_1(b):=\|P_{1,b}u_\nu\|_2^2=c_0(b)^2+c_1(b)^2.
\]
Differentiating the coefficient formulas yields
\[
c_0'(b)=\frac{c_1(b)}{\sqrt2},
\qquad
c_1'(b)=c_2(b)-\frac{c_0(b)}{\sqrt2}.
\]
The cross-terms cancel exactly:
\[
Q_0'(b)=\sqrt2\,c_0(b)c_1(b),
\qquad
\boxed{Q_1'(b)=2c_1(b)c_2(b).}
\]
At any global maximizer \(b_*\) of \(Q_1\), stationarity implies either \(c_1(b_*)=0\) or \(c_2(b_*)=0\). In the latter case positivity of \(\nu\) forces \(\nu\) to be a point mass at \(b_*\), which also implies \(c_1(b_*)=0\). Thus every maximizer of \(Q_1\) has \(c_1(b_*)=0\), and therefore \(Q_1(b_*)=Q_0(b_*)\le\max_b Q_0(b)\). Because \(Q_1\ge Q_0\) pointwise, their global maxima coincide. Conversely, at any global maximizer of \(Q_0\), positivity of \(c_0\) and \(Q_0'=0\) force \(c_1=0\), so this center also maximizes \(Q_1\). The argmax sets are equal. Subtracting the common maximal captured energy from \(\|u_\nu\|_2^2\) establishes the equality of globally minimal squared errors.

**3. Degree two is strictly useful.** If the measure is not a point mass, then \(c_2(b)>0\) at every \(b\). At any common optimal center \(b_*\),
\[
Q_2(b_*):=\|P_{2,b_*}u_\nu\|_2^2
=Q_1(b_*)+c_2(b_*)^2>\max_b Q_1(b).
\]
Taking the maximum over \(b\) on the left gives a strict increase in best captured energy and hence a strict decrease in best squared error. For a single point mass the target already lies in \(V_0\) at the mass location, so strictness is correctly excluded.

**4. Exact symmetric two-Gaussian bifurcation.** For \(\nu=\delta_{-a}+\delta_a\), \(a>0\),
\[
c_0(b)=2e^{-(a^2+b^2)/4}\cosh(ab/2),
\quad
c_1(b)=\sqrt2e^{-(a^2+b^2)/4}\big[a\sinh(ab/2)-b\cosh(ab/2)\big].
\]
Because \(Q_0=c_0^2\), its stationarity equation is
\[
\boxed{b=a\tanh(ab/2).}
\]
For positive \(b\), \(\tanh z/z\) strictly decreases from one to zero. Hence for \(a^2\le2\), there are no positive stationary centers, and the unique maximizer is \(b=0\). For \(a^2>2\), there exists exactly one positive stationary center \(b_a\in(0,a)\); symmetry supplies \(-b_a\). Here \(b=0\) is a strict local minimum, and the two nonzero stationary centers are the only global maxima. A Taylor expansion of the defining equation gives
\[
b_a=\sqrt{3(a^2-2)}\,[1+o(1)]\quad\text{as }a\downarrow\sqrt2.
\]
At the critical threshold the energy profile has a flat quartic maximum:
\[
Q_0(b)=4e^{-1}\left(1-\frac{b^4}{24}+O(b^6)\right),\quad a=\sqrt2.
\]
The same optimizers and maximal energy apply to \(Q_1\). For \(0<a\le\sqrt2\), the two best squared errors are explicitly
\[
\boxed{2+2e^{-a^2}-4e^{-a^2/2}.}
\]
At \(b=0\), the extra degree-two captured energy is \(c_2(0)^2=(a^4/2)e^{-a^2/2}>0\), providing a concrete strict improvement.

**5. Positivity boundary.** For the sign-changing Hermite target \(u=\phi_1\), the one-mode maximal captured energy is \(1/e\), as the overlap squared is \((b^2/2)e^{-b^2/2}\). However \(u\in V_1(0)\) and the two-mode captured energy is one. Thus the equality can fail without the nonnegative-mixture hypothesis.

## Verification

The standalone standard-library Python script `verify.py` checks the Gaussian-Hermite coefficient identities against direct quadrature for fifteen cases, the captured-energy derivatives over sixty-three cases, independent finite-grid optimizations for four multi-center positive mixtures, the symmetric-doublet stationary equations across five parameter regimes, and the sign-changing boundary example. Run `python3 verify.py` from the extracted package directory. The observed output was:

```
VERIFY_OK: 15 overlap quadratures, 63 energy derivative checks, 4 multi-peak optimizer comparisons, 5 sharp doublet regimes, signed boundary
```

The all-measure assertion, global optimization and uniqueness at the doublet threshold rest on the analytic arguments above, not on finite numerical sampling.

## Relationship to prior work

Chou, Shao and Xia (2022) introduce an adaptive Hermite spectral method with basis movement and rescaling; Xia, Shao and Chou (2020) study scaling and moving techniques for unbounded-domain spectral approximation. These works motivate selection of the spatial center. Their inspected formulations and convergence/indicator results do not state that an optimally translated first Hermite enrichment is redundant for all positive Gaussian location mixtures, nor the strict minimal degree-two remedy.

Gaussian kernel mode-finding/mean-shift theory studies the stationary equation for \(c_0\) and can imply the explicit double-Gaussian center equation. The claimed result is **not** novelty of that stationary equation. The assessed distinction is the exact equality of two independently optimized Hermite subspace errors for *all* positive mixtures together with the strict next-degree boundary. The bifurcation supplies a sharp concrete example, not a claim that multimodal Gaussian mode-splitting is new. Existing general coherent-state and approximation identities are acknowledged as mathematical tools. Related specialized literature may contain equivalent implications; independent priority checking remains necessary.

## Limitations

Only the one-dimensional standard-width Gaussian translation family and ordinary exact \(L^2\) orthogonal projections are treated. Optimizing translation can cost computation and is not synonymous with a practical moving-grid heuristic. Fixed-center enrichment, signed mixtures, scale-varying Hermite bases, other norms, nonlinear approximation and time-dependent PDE error are not covered. The squared-error equality does not say that the subspaces themselves coincide or that a first-degree mode is useless before center optimization. The nonzero improvement at degree two is not furnished with a universal lower bound for arbitrary positive measures. Independent validation and publication-priority assessment have not been performed.

## References

1. T. Chou, S. Shao, M. Xia, *Adaptive Hermite Spectral Methods in Unbounded Domains*, first submitted 2022-03-29, arXiv:2203.15630, https://arxiv.org/abs/2203.15630 .
2. M. Xia, S. Shao, T. Chou, *Efficient Scaling and Moving Techniques for Spectral Methods in Unbounded Domains*, 2020, arXiv:2009.13170, https://arxiv.org/abs/2009.13170 .
3. Hao Hu, Haijun Yu, *Scaling Optimized Hermite Approximation Methods*, 2024, arXiv:2412.08044, https://arxiv.org/abs/2412.08044 .
4. D. Comaniciu, P. Meer, *Mean Shift: A Robust Approach Toward Feature Space Analysis*, IEEE TPAMI 24 (2002), https://doi.org/10.1109/34.1000236 .
