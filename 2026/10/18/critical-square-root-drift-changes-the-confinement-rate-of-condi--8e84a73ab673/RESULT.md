# Critical square-root drift changes the confinement rate of conditioned Brownian motion

## Finding

Let \(x\in\mathbb R\), \(\theta>0\), and \(\mu_T\in\mathbb R\) satisfy \(\mu_T^2/T\to c^2\in[0,\infty)\). For each \(T>0\), put \(W_s^{(T)}=x+\mu_Ts+B_s\) and \(Z_T=\int_0^T(W_s^{(T)})^2\,ds\). Denote by \(\mathsf Q_T\) its law conditional on \(Z_T\le\theta T\), restricted initially to \([0,T]\). Define \(\gamma=\gamma(c,\theta)>0\) as the unique solution of
\[
 2\theta\gamma^3-\gamma^2=c^2,\qquad \gamma\ge \frac1{2\theta}.
\]
Then for every finite \(t>0\), the restriction of \(\mathsf Q_T\) to \(C([0,t])\) converges **in total variation** to the law of the Ornstein--Uhlenbeck diffusion
\[
 dX_s=d\widetilde B_s-\gamma X_s\,ds,\qquad X_0=x.
\]
In particular, these restrictions converge weakly consistently on \(C([0,\infty))\). The limit depends on the squared critical drift amplitude \(c^2\) but not on its sign: \(\gamma(0,\theta)=1/(2\theta)\), while \(\gamma(c,\theta)>1/(2\theta)\) for \(c>0\). The convergence holds without assuming the sign of \(\mu_T\) converges.

An accompanying sharp hard-budget small-deviation asymptotic, with \(S\to\infty\), \(\nu_S^2/S\) bounded, \(y_S/S\to\theta>0\), and fixed initial point \(a\), is as follows. Define \(g_S>0\) by
\[
 \frac{y_S}{S}=\frac{1}{2g_S}+\frac{\nu_S^2}{2Sg_S^3},\quad
 \ell_S=\frac{g_S^2}{2},\quad
 v_S=\frac{1}{2g_S^3}+\frac{3\nu_S^2}{2Sg_S^5}.
\]
Then, uniformly when \(a\) and \(y_S/S\) range over fixed compact sets with the latter bounded away from zero,
\[
\begin{split}
 \Pr_a^{\nu_S}\!\left(\int_0^S W_s^2ds\le y_S\right)
 &\sim\frac{\sqrt 2}{\ell_S\sqrt{2\pi S v_S}}
 \exp\left(\ell_S y_S-\frac{g_SS}{2}+\frac{\nu_S^2}{2g_S}
 -\frac{\nu_S^2 S}{2}-\nu_Sa-\frac{g_Sa^2}{2}\right).
\end{split}
\]
This formula supplies the probability ratios needed for the conditional process result; it is not asserted for growing initial points or for \(\nu_S^2/S\to\infty\).

## Assumptions and scope

Brownian motions are real, have variance rate one, and start from deterministic \(x\). The drift is deterministic, constant over each observation horizon, and may depend on the horizon. The conditioning is the *hard* event \(Z_T\le\theta T\), not independent exponential killing. The fixed-window result requires \(\mu_T^2/T\to c^2<\infty\). The source paper's subcritical result corresponds to \(c=0\) but was established under stricter growth assumptions. If \(\mu_T^2/T\) has several finite accumulation points, the corresponding subsequences have the indicated Ornstein--Uhlenbeck limits, potentially with different rates.

## Proof

**1. Exact transform.** For a constant drift \(\nu\), initial point \(a\), horizon \(S\), and \(\operatorname{Re}\lambda>0\), set \(g=\sqrt{2\lambda}\) with \(\operatorname{Re}g>0\). The Feynman--Kac equation with potential \(\lambda a^2\), or a direct quadratic-exponential ansatz, gives the exact identity
\[
 M_S(\lambda;a,\nu)=\mathbb E_a^{\nu}\exp\!\left(-\lambda\int_0^S W_s^2ds\right)
 =\frac{\exp\!\left(-\nu a-\frac{\nu^2S}{2}
 -\frac{g^2a^2-\nu^2}{2g}\tanh(gS)+\frac{\nu a}{\cosh(gS)}\right)}{\sqrt{\cosh(gS)}}.
\]
For example, the Gaussian ansatz \(M=\exp(Aa^2+Ba+C)\) gives \(A=-g\tanh(gS)/2\), \(B=\nu(\operatorname{sech}(gS)-1)\), and \(C=-\nu^2S/2+\nu^2\tanh(gS)/(2g)-(1/2)\log\cosh(gS)\). These satisfy the Feynman--Kac PDE, the initial condition, and the required real-parameter boundedness.

**2. A uniform complex saddle.** For the small-deviation asymptotic choose \(g_S\) and \(\ell_S\) as in the statement. The saddle equation is uniquely soluble, since \(g\mapsto1/(2g)+\nu_S^2/(2Sg^3)\) decreases strictly from infinity to zero. When \(y_S/S\) stays in a compact positive interval and \(\nu_S^2/S\) remains bounded, \(g_S\) and \(\ell_S\) remain in positive compact intervals.

Use the Bromwich inversion formula for the continuous distribution of the nonnegative quadratic functional:
\[
 F_S(y_S)=\frac{1}{2\pi}\int_{\mathbb R}
 \frac{e^{(\ell_S+iu)y_S}M_S(\ell_S+iu;a,\nu_S)}{\ell_S+iu}\,du.
\]
For \(u\in\mathbb R\) write \(g(u)=\sqrt{g_S^2+2iu}\). The real part satisfies \(\operatorname{Re}g(u)>g_S\) for \(u\ne0\), and \(\operatorname{Re}(1/g(u))\le 1/g_S\). Since \(\operatorname{Re}g(u)\ge g_S>0\), uniformly over the entire vertical contour the exact transform admits the multiplicative asymptotic
\[
 M_S(\ell_S+iu;a,\nu_S)
 =\sqrt2\exp\left[-\nu_Sa-\frac{\nu_S^2S}{2}
 -\frac{Sg(u)}2-\frac{a^2g(u)}2+\frac{\nu_S^2}{2g(u)}\right]\bigl(1+o(1)\bigr).
\]
The error is uniform in \(u\), because \(\tanh(g(u)S)-1\) and \(\operatorname{sech}(g(u)S)\) are bounded by constants times \(e^{-g_SS}\), while \(\nu_S^2=O(S)\). After division by its value at \(u=0\), the modulus of the leading exponential is at most
\[
 \exp\left[-\frac S2\{\operatorname{Re}g(u)-g_S\}\right],
\]
with additional factors of modulus at most one contributed by the \(\nu_S^2/(2g(u))\) and \(-a^2g(u)/2\) terms. Here the strict positive gap off zero and \(\operatorname{Re}g(u)\asymp\sqrt{|u|}\) at infinity provide exponentially small remote tails, uniformly in the indicated compact parameter sets.

The phase derivative vanishes at zero by the saddle equation. Taylor expansion gives
\[
 iu y_S-\frac S2\{g(u)-g_S\}+
 \frac{\nu_S^2}{2}\left(\frac1{g(u)}-\frac1{g_S}\right)
 =-\frac{Sv_Su^2}{2}+O(S|u|^3),
\]
where \(v_S=1/(2g_S^3)+3\nu_S^2/(2Sg_S^5)>0\). With \(u=q/\sqrt S\), the extra endpoint term \(-a^2(g(u)-g_S)/2\) is \(o(1)\), and \((\ell_S+iu)^{-1}=\ell_S^{-1}(1+o(1))\). A dominated Gaussian integral, using the preceding off-zero bounds, yields precisely the prefactor and exponent stated in the finding. It also yields the same saddle approximation when the horizon is changed from \(S\) to \(S-t\) and the budget from \(\theta S\) to \(\theta S-z\), for any *fixed* \(t,z\): the old saddle then has residual first derivative \(O(1)\), whose contribution at Gaussian scale is \(o(1)\). This avoids discarding a potentially order-one shift of the exponent.

**3. Probability ratio at a fixed prefix.** Put \(S=T\), \(\nu_S=\mu_T\), \(y_S=\theta T\), and let \(g_T\) solve
\[
 \theta=\frac{1}{2g_T}+\frac{\mu_T^2}{2Tg_T^3}.
\]
Then \(g_T\to\gamma\). For every fixed \(t\ge0\), \(z\ge0\), and \(w\in\mathbb R\), the uniform saddle formula, using the *same* saddle for numerator and denominator, gives
\[
\frac{\Pr_w^{\mu_T}(Z_{T-t}\le\theta T-z)}{\Pr_x^{\mu_T}(Z_T\le\theta T)}
=\exp\left[\frac{g_Tt}{2}-\frac{g_T^2z}{2}
 +\frac{g_T(x^2-w^2)}{2}+\mu_T(x-w)+\frac{\mu_T^2t}{2}\right](1+o(1)).
\]
The displayed ratio is pointwise in \((w,z)\); it is not assumed uniform over Brownian paths.

**4. Cancellation of the diverging drift.** On \(C([0,t])\), use the *fixed*, driftless Wiener law \(\mathsf P_x^0\) as a reference. For a path \(\omega\) define \(z(\omega)=\int_0^t\omega_s^2ds\). The conditional law has the exact Radon--Nikodym density
\[
 f_{T,t}(\omega)=\exp\left[\mu_T(\omega_t-x)-\frac{\mu_T^2t}{2}\right]
 \frac{\Pr_{\omega_t}^{\mu_T}(Z_{T-t}\le\theta T-z(\omega))}{\Pr_x^{\mu_T}(Z_T\le\theta T)},
\]
where the numerator is zero when its remaining budget is negative. Each \(f_{T,t}\) is nonnegative with \(\int f_{T,t}\,d\mathsf P_x^0=1\), by Girsanov's theorem and the Markov property. For every fixed continuous prefix, substitution of the ratio gives the pointwise limit
\[
 f_t(\omega)=\exp\left[\frac{\gamma t}{2}
 +\frac{\gamma(x^2-\omega_t^2)}2
 -\frac{\gamma^2}{2}\int_0^t\omega_s^2ds\right].
\]
By Itô's formula, \(\int_0^t\omega_s\,d\omega_s=(\omega_t^2-x^2-t)/2\) under the driftless Wiener measure, so \(f_t\) is the classical change-of-drift density for the Ornstein--Uhlenbeck SDE with drift \(-\gamma\omega_s\). It integrates to one (equivalently, the finite-horizon Ornstein--Uhlenbeck transition law is a probability measure). Scheffé's lemma therefore yields \(\int|f_{T,t}-f_t|\,d\mathsf P_x^0\to0\). This is total variation convergence of the entire *path law* on each fixed \([0,t]\), not merely convergence of finite-dimensional distributions. Consistency and the standard projective tightness argument give weak convergence on \(C([0,\infty))\).

**5. Boundary and monotonicity.** The defining function for \(\gamma\) has exactly one positive root for each \(c^2\ge0\) on \([1/(2\theta),\infty)\), since \(2\theta\gamma^3-\gamma^2\) is strictly increasing there. In particular, \(\gamma=1/(2\theta)\) at \(c=0\), and \(\gamma>1/(2\theta)\) otherwise. Only \(\mu_T^2/T\) enters this equation, proving sign-independence.

## Verification

The accompanying standalone `verify.py` recomputes the saddle equation, the second derivative of the complex phase, the exact Feynman--Kac PDE residual, and the exponent-ratio cancellation on independent parameter grids. It uses only the Python standard library. Checks on finite grids supplement rather than replace the global contour bounds and analytical proof above. The accepted statement is about weak and total variation convergence in a specified critical regime; no almost-sure coupling or total-variation convergence on the *entire* infinite time axis is asserted.

## Relationship to prior work

Aurzada, Dutta, and Wiegand, *Brownian motion with drift conditioned to have restricted L²-norm* (arXiv:2610.12354v1, publicly submitted 2026-10-08), establish a drift-independent Ornstein--Uhlenbeck limit under \(\mu_T^2\le MT^\beta\) with \(\beta<1/2\), and give small-deviation asymptotics in that range. Their §1.1 explicitly poses the critical scale \(\mu_T\sim c\sqrt T\) as an open direction (their discussion just before §1.1 Related work). Their exact Laplace transform (equation (48)) is a valid starting ingredient, but their Theorem 2's stated parameter range does not cover \(\mu_T^2/T\to c^2>0\); the saddle itself must move at leading order. The present result supplies that moving saddle, its sharp rate and prefactor, and the critical conditioned diffusion law.

Aurzada, Lifshits, and Schickentanz, *Brownian motion conditioned to have restricted L₂-norm* (arXiv:2312.12982), treat the driftless baseline. Schmidt, *Conditioned Brownian motion and local equivalence of path ensembles* (arXiv:2608.19744), treats a broad class of confining potentials and ground-state diffusion limits; its available abstract concerns the untilted Brownian base process rather than a horizon-dependent drift of order \(\sqrt T\). Its full text was not accessible in this investigation, leaving some risk of implicitly subsuming the result. Classical sharp large-deviation/saddlepoint and path-ensemble ideas underlie the method; novelty is claimed only for this critical moving-drift theorem, not for those methods.

## Limitations

The mathematical conclusion is proved only for \(\theta>0\), fixed \(x\), deterministic constant-on-horizon drifts, and \(\mu_T^2/T\) with a finite limit. The asymptotic probability formula requires compactness assumptions and fixed starting points. It makes no statement about longer observation windows growing with \(T\), unbounded effective drift ratios, or nonquadratic confinement. The theorem is a self-reviewed mathematical finding, not an independently audited or externally certified result. The relevant Schmidt preprint could not be fully inspected in this run; accessible descriptions do not establish the present drift-critical theorem, but this limits the originality search.

## References

1. F. Aurzada, Y. Dutta, and M. Wiegand, *Brownian motion with drift conditioned to have restricted L²-norm*, arXiv:2610.12354v1 (2026-10-08). https://arxiv.org/html/2610.12354v1 ; especially Theorems 1–2, §1.1, and Eq. (48).
2. F. Aurzada, M. Lifshits, and D. T. Schickentanz, *Brownian motion conditioned to have restricted L₂-norm*, arXiv:2312.12982 (2023-12-20). https://arxiv.org/abs/2312.12982 .
3. T. Schmidt, *Conditioned Brownian motion and local equivalence of path ensembles*, arXiv:2608.19744 (2026-08-20). https://arxiv.org/abs/2608.19744 .
4. B. Bercu, F. Gamboa, and M. Lavielle, *Sharp Large Deviations for Gaussian Quadratic Forms with Applications*, ESAIM Probability and Statistics 4 (2000), 1–24 (background sharp large deviations).
