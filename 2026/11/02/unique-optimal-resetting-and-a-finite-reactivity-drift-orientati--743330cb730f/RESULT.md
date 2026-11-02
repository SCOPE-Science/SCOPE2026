# Unique optimal resetting and a finite-reactivity drift-orientation gap

## Finding

For one-dimensional Brownian diffusion with a fixed nonzero-distance reset point, a finite-strength partially absorbing point sink, and arbitrary constant drift, the mean absorption time has **exactly one** positive, nondegenerate global optimal Poisson-reset rate. At equal nonzero drift magnitudes, resetting is strictly faster when the drift points away from the sink than when it points toward it. As drift magnitude increases without bound while diffusivity, reset distance, and *finite* sink reactivity remain fixed, the two optimal rates have a common leading term but a nonzero limiting separation:

\[
r_*^{\rm away}(v)=\frac v\ell+O(v^{-1}),\qquad
r_*^{\rm toward}(v)=\frac v\ell-\frac{\kappa}{e\ell}+O(v^{-1}),\qquad
\lim_{v\to\infty}(r_*^{\rm away}-r_*^{\rm toward})=\frac{\kappa}{e\ell}.
\]

In particular, the finite-reactivity contribution persists as a constant difference of optimal frequencies even when the drift is arbitrarily strong. The fully absorbing boundary is a singular different regime; the expansion is not asserted uniformly as \(\kappa\to\infty\).

## Assumptions and scope

Fix real parameters \(D>0\), \(\ell>0\), \(\kappa>0\), and \(\mu\in\mathbb R\). A particle starts at \(\ell\) and between resets solves \(dX_t=\mu\,dt+\sqrt{2D}\,dW_t\) on the full line. Independently of its position, at Poisson rate \(r>0\), each still-surviving particle jumps instantaneously back to \(\ell\). The sink at the origin removes mass through the forward term \(-\kappa p(0,t)\delta_0\), equivalently a killing hazard proportional to local time; crossing the origin does not automatically absorb. The measured time is the mean time until killing, not the first arrival time at the origin. All results refer to a **single** sink and a constant reset rate; the reset clock is independent of diffusion and sink killing.

The positive sign of \(\mu\) points **away** from the origin; the negative sign points **toward** it. For a fixed magnitude \(v>0\), set

\[
m=\frac{v\ell}{2D}>0,\quad \eta=\frac{2D}{\kappa\ell}>0,\quad
z=\ell\sqrt{r/D}>0,\quad w=\sqrt{m^2+z^2},\quad \sigma\in\{-1,+1\}.
\]

The exact renewal expression for the mean absorption time, already established in the motivating source, is

\[
T_{\sigma v}(r)=\frac{\ell^2}{D}
\frac{(1+\eta w)e^{w+\sigma m}-1}{z^2}.
\tag{1}
\]

At zero drift use \(m=0\) and the same expression with \(w=z\). The novel claims concern **global uniqueness at arbitrary drift**, the strict comparison of the two orientations for every nonzero magnitude, and the **strong-drift offset**.

## Proof

**1. Formula and coercivity.** The reset-free Laplace-space probability of absorption before an independent exponential time of rate \(r\) equals

\[
B(r)=\frac{\kappa}{\kappa+\sqrt{\mu^2+4Dr}}
\exp\!\left[-\frac{\mu\ell+\ell\sqrt{\mu^2+4Dr}}{2D}\right].
\]

The renewal identity gives \(T(r)=(1-B(r))/(rB(r))\), yielding (1). For each finite \(\kappa>0\), as \(r\downarrow0\), \(T(r)\to\infty\): when \(\mu\ne0\), \(B(0)<1\), so the divergence is at least order \(r^{-1}\); when \(\mu=0\), \(T(r)\) diverges at order \(r^{-1/2}\). At \(r\uparrow\infty\), the exponential in \(\sqrt r\) forces \(T(r)\to\infty\). Hence positive global minimizers exist.

**2. Exactly one stationary point when drift is nonzero.** Set \(y=w-m>0\), so \(z^2=y(y+2m)\), a strictly increasing bijection from \(y>0\) to \(r>0\). For either sign, define \(q=e^{-(\sigma+1)m}\in(0,1]\). Multiplying (1) by the positive constant \(e^{-(\sigma+1)m}D/\ell^2\) reduces its minimization to

\[
f(y)=\frac{F(y)}{y(y+2m)},\qquad
F(y)=(1+\eta(m+y))e^y-q.
\tag{2}
\]

Expand \(F(y)=F_0+\sum_{n\ge1}a_ny^n\), with

\[
F_0=1+\eta m-q>0,\qquad
a_n=\frac{1+\eta m+n\eta}{n!}>0.
\]

The derivative of (2) has the sign of \(N(y)=y(y+2m)F'(y)-(2y+2m)F(y)\). Exact coefficient collection gives

\[
\frac{N(y)}{y^2}=
-\frac{2mF_0}{y^2}-\frac{2F_0}{y}
 +(2ma_2-a_1)
 +\sum_{n\ge3}\left[(n-3)a_{n-1}+2m(n-1)a_n\right]y^{n-2}.
\tag{3}
\]

Every coefficient in the sum is strictly positive, as \(m>0\). All derivatives of the displayed negative reciprocal terms are also positive. Consequently \(N(y)/y^2\) is strictly increasing on \((0,\infty)\), with limits \(-\infty\) and \(+\infty\). It vanishes **once and only once**. The first derivative changes from negative to positive; because the crossing is strictly transverse, the minimizing stationary point has positive second derivative.

**3. Zero drift.** If \(m=0\), write \(F(y)=(1+\eta y)e^y-1=\sum_{n\ge1}a_ny^n\), where \(a_n=(1+n\eta)/n!\). The mean time is proportional to \(F(y)/y^2\). Its derivative has the sign of

\[
\frac{yF'(y)-2F(y)}{y}=-a_1+\sum_{n\ge3}(n-2)a_ny^{n-1},
\]

again strictly increasing from a negative value to infinity. The positive optimum is therefore unique and nondegenerate. No perfect-sink or small-drift approximation was used.

**4. Strict orientation ordering.** At equal \(v>0\), the exact dimensionless objective obeys

\[
\tau_{+}(z)=e^{2m}\tau_{-}(z)+\frac{e^{2m}-1}{z^2}.
\tag{4}
\]

At the unique minimizer \(z_-\) of \(\tau_-\), differentiation gives \(\tau_+'(z_-)=-2(e^{2m}-1)/z_-^3<0\). By the unique derivative sign-crossing proved in step 2, the unique minimizer of \(\tau_+\) lies strictly to the right. Since \(r=D z^2/\ell^2\), \(r_*^{\rm away}(v)>r_*^{\rm toward}(v)\) for every \(v>0\).

**5. Strong-drift optimizer and exact offset.** Write \(q_-=1\), \(q_+=e^{-2m}\), and use the positive rescaling (2). For \(m\ge1\), the pointwise bound

\[
f(y)\ge\frac{\eta m e^y}{y(2m+y)}\ge\frac{\eta e^y}{y(2+y)}
\]

holds in both orientations. The right-hand side tends to infinity at both ends \(y\downarrow0\) and \(y\to\infty\), while \(f(1)\) stays uniformly bounded for \(m\ge1\). Thus all minimizing \(y\)'s stay inside a common compact subset of \((0,\infty)\). Uniformly with derivatives on this compact set,

\[
f_\sigma(y)=\frac{\eta e^y}{2y}\left[
1+\frac{1/\eta+y/2-q_\sigma e^{-y}/\eta}{m}+O(m^{-2})
\right].
\tag{5}
\]

The leading profile \(\eta e^y/(2y)\) has its unique nondegenerate minimum at \(y=1\); compactness forces both exact optimizers to converge to one. Differentiating the logarithm of (5) and using the exact stationary equation yields

\[
y_+(m)=1-\frac1{2m}+O(m^{-2}),\qquad
y_-(m)=1-\frac{1/2+1/(e\eta)}{m}+O(m^{-2}).
\tag{6}
\]

Substitute into \(z^2=y(y+2m)\) to obtain

\[
z_+^2=2m+O(m^{-1}),\qquad
z_-^2=2m-\frac2{e\eta}+O(m^{-1}).
\tag{7}
\]

Because \(r=Dz^2/\ell^2\), \(2mD/\ell^2=v/\ell\), and \(2D/(e\eta\ell^2)=\kappa/(e\ell)\), equation (7) is precisely the asserted pair of expansions. All error terms hold for fixed positive \(D,\ell,\kappa\), not uniformly in a simultaneous perfect-reactivity limit.

## Verification

A standard-library-only Python program, `VERIFY.py`, numerically solves the stationary condition by sign-bracketing, checks strict local minimality and both orientation orderings over a grid of positive reaction strengths and drift magnitudes, compares the motivating article's published numerical optima at \(D=\ell=1\), \(\kappa=2\), \(\mu=\pm1\), and checks the strong-drift limiting coefficients. Run `python VERIFY.py` using Python 3.9 or newer. The saved program produced **1,386 passing finite assertions**. These numerical comparisons do not replace the coefficient argument or compactness and uniform-expansion proof.

## Relationship to prior work

Mazzolo (2026), equations (116) and (185), provides exactly the drifted MFPT (1) and dimensionless reduction. The source's Appendix A.2 proves uniqueness only for **zero** drift; Appendix A.5 gives a weak-drift correction, the one-dimensional arbitrary-drift optimization, and numerical evidence that reversing the drift shifts the optimum. The finite-drift global uniqueness theorem, strict all-magnitude orientation ordering, and fixed-reactivity strong-drift limiting gap above are not stated there. Its numerical examples are consistent with, but do not imply, these conclusions.

Whitehouse, Evans and Majumdar (2013), Section 4, prove partial-absorption formulas and discuss minimizing over reset rate **without drift**. Ray, Mondal and Reuveni (2019), Section IV and Appendix B, analyze optimal resetting under drift to a **perfectly absorbing boundary**; that process has a Péclet-controlled zero-reset phase, unlike the present finite-reactivity point sink, where every drift has a strictly positive optimum. Neither source directly supplies the fixed-finite-reactivity orientation gap. Published related results on other renewal and capture protocols are context rather than identical statements; absence of a detected match is not a general priority proof.

## Limitations

The result is confined to the scalar constant-drift full-line diffusion, a single local-time point sink, Poisson resetting to a fixed positive-distance point, and fixed finite reactivity. It does not establish asymptotics uniformly as \(\kappa\to\infty\), results for spatially varying drift, extended targets, or non-Poisson resetting. The analysis gives unique global optimal *rates*, not a new formula for the mean time, which was already derived in the motivating source. Literature-wide originality has not been independently certified.

## References

1. A. Mazzolo, “Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes,” arXiv:2609.22527v1, first posted 2026-09-18; https://arxiv.org/abs/2609.22527 . Especially Section III.3.2 and Appendix A.2–A.5.
2. J. Whitehouse, M. R. Evans, and S. N. Majumdar, “Effect of Partial Absorption on Diffusion with Resetting,” *Physical Review E* **87**, 022118 (2013); arXiv:1301.2489, https://arxiv.org/abs/1301.2489 . Especially Section 4.
3. S. Ray, D. Mondal, and S. Reuveni, “Péclet number governs transition to acceleratory restart in drift-diffusion,” *Journal of Physics A* **52**, 255002 (2019); arXiv:1811.08239, https://arxiv.org/abs/1811.08239 . Especially Section IV and Appendix B.
