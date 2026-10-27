# Dimensional ordering and second-order resetting threshold for small spherical targets

## Finding

For every integer spatial dimension \(d\ge2\), set \(\nu=d/2-1\) and define
\[
J_d(x)=\frac{1}{x^{\nu+2}K_\nu(x)},\qquad x>0,
\]
where \(K_\nu\) is the positive modified Bessel function of the second kind. Let \(\gamma_d\) be its unique minimizer. For the classical Brownian stochastic-resetting search with a small spherical absorbing target, \(\gamma_d\) is the optimal dimensionless reset intensity for the **leading small-target mean-first-passage-time term** [1]. The following three statements hold simultaneously:
\[
\boxed{\gamma_{d+1}>\gamma_d,\quad 2(d-2)<\gamma_d^2<2d\quad(d\ge2),}
\]
\[
\boxed{\gamma_d^2=2(d-2)+\frac{8}{d-2}+O(d^{-2})\quad(d\to\infty).}
\]
The second box is an iterated-limit statement: first take the target-radius ratio to zero at each fixed dimension, *then* increase dimension. In physical units, the optimizer of the leading small-target coefficient has rate \(r_{d,\mathrm{lead}}^*=(D/R^2)\gamma_d^2\).

## Assumptions and scope

The free particle follows \(d\)-dimensional isotropic Brownian motion with diffusivity \(D>0\), independently reset at the constant Poisson rate \(r>0\) to its starting point a distance \(R>a>0\) from the center of an absorbing sphere of radius \(a\). Write \(\epsilon=a/R\) and \(x=R\sqrt{r/D}\). For fixed \(d>2\), the exact mean first-passage time [1, equations (65)–(73)] has leading term equal to a positive \(d,\epsilon\)-dependent multiple of \(J_d(x)\) as \(\epsilon\downarrow0\); at \(d=2\), it is a positive multiple of \(\log(1/\epsilon)J_2(x)\) [1, equations (75)–(77)]. The optimization in this result concerns **these leading coefficients**, not an assertion of a uniform joint high-dimensional and small-target limit, and not the precise optimizer of finite-radius mean time.

Use the order convention \(\nu=d/2-1\ge0\) throughout, notwithstanding the alternative signed order in earlier sections of [1]. The source already gives the critical equation and examples; novelty is **not** claimed for that equation or general Bessel-ratio monotonicity.

## Proof

**1. Unique root and minimizer.** Write
\[
F_\nu(x)=x\frac{K_{\nu-1}(x)}{K_\nu(x)}>0.
\]
The derivative and recurrence identities for \(K\) give
\[
F_\nu'(x)=\frac{F_\nu(x)^2+2\nu F_\nu(x)-x^2}{x}.
\]
As \(x\downarrow0\), \(F_\nu(x)\downarrow0\) and its derivative is positive; as \(x\to\infty\), \(F_\nu(x)=x+O(1)\), so its derivative is positive. At any possible stationary point the Riccati equation implies \(F_\nu''(x)=-2\), hence the point would be a strict local maximum and a derivative sign change from positive to negative. There cannot be a later return to a positive derivative, because every stationary point would again change positive to negative. Thus \(F_\nu'(x)>0\) everywhere. The derivative of \(x^{\nu+2}K_\nu(x)\) has the sign of \(2-F_\nu(x)\). Consequently \(F_\nu(\gamma_d)=2\) has exactly one solution and \(J_d\) has exactly one global minimizer.

**2. Strict dimension ordering.** From
\[
K_\nu(x)=\int_0^\infty e^{-x\cosh t}\cosh(\nu t)\,dt
\]
and the strictly positive second derivative of \(\log\cosh(\nu t)\) with respect to \(\nu\) for \(t>0\), together with Hölder, the mapping \(\nu\mapsto K_\nu(x)\) is strictly log-convex for fixed \(x>0\). Hence \(\nu\mapsto K_{\nu-1}(x)/K_\nu(x)\) is strictly decreasing. Since \(F_\nu\) is strictly increasing in \(x\), its level-two root increases strictly with \(\nu\), proving \(\gamma_{d+1}>\gamma_d\).

**3. Nonasymptotic bounds.** At \(x=\gamma_d\), the Riccati equation and strict positivity of \(F_\nu'\) yield \(4+4\nu-x^2>0\). From
\[
K_\nu(x)=K_{\nu-2}(x)+\frac{2(\nu-1)}{x}K_{\nu-1}(x)
\]
we obtain the exact identity
\[
F_{\nu-1}(x)=\frac{x^2}{F_\nu(x)}-2(\nu-1).
\]
Because \(F_{\nu-1}(x)>F_\nu(x)=2\), we infer \(x^2>4\nu\). Thus \(4\nu<\gamma_d^2<4(\nu+1)\), exactly the first boxed bounds.

**4. The first nonzero high-dimensional correction.** For \(\nu>0\), the Schläfli/Gamma integral represents the same Bessel ratio in terms of \(U\sim\operatorname{Gamma}(\nu,1)/\nu\):
\[
F_\nu(2\sqrt{\nu z})=2z\,\frac{\mathbb E[U^{-1}e^{-z/U}]}{\mathbb E[e^{-z/U}]}.
\]
For \(z\) in a fixed compact neighborhood of \(1\), Taylor expansion at \(U=1\), using the Gamma central moments and controlled remainder, gives uniformly
\[
F_\nu(2\sqrt{\nu z})=2z+\frac{2z-2z^2}{\nu}+\frac{2z-8z^2+4z^3}{\nu^2}+O(\nu^{-3}).\tag{*}
\]
To make the remainder explicit, apply the sixth-order Taylor formula to the two smooth functions \(u\mapsto e^{-z/u}\) and \(u\mapsto u^{-1}e^{-z/u}\) on \(u>0\). Their first seven derivatives are uniformly bounded over the compact set of \(z\)'s, due to exponential damping as \(u\downarrow0\) and polynomial behavior as \(u\to\infty\). The standardized Gamma variable satisfies \(\mathbb E(U-1)^2=\nu^{-1}\), \(\mathbb E(U-1)^3=2\nu^{-2}\), \(\mathbb E(U-1)^4=3\nu^{-2}+6\nu^{-3}\), the fifth and sixth moments are \(O(\nu^{-3})\), and the absolute seventh moment is \(O(\nu^{-7/2})\). Algebraic division of the two Taylor series yields (*); the coefficients can also be derived independently from the Riccati equation, as verified by the accompanying checker.

Set \(z_\nu=\gamma_d^2/(4\nu)\). Step 3 ensures \(1<z_\nu<1+1/\nu\). Substituting \(z_\nu=1+\delta_\nu\) into (*) with \(F_\nu(\gamma_d)=2\) first shows \(\delta_\nu=O(\nu^{-2})\), then
\[
0=2\delta_\nu-\frac{2}{\nu^2}+O(\nu^{-3}),\qquad z_\nu=1+\nu^{-2}+O(\nu^{-3}).
\]
Consequently \(\gamma_d^2=4\nu+4/\nu+O(\nu^{-2})\), which is the second boxed formula because \(\nu=(d-2)/2\).

## Verification

The included standalone `check.py` uses symbolic recurrence algebra and Gamma central moments to reproduce all three coefficients of (*). It numerically solves the Bessel-ratio equation and checks the strict bounds for dimensions \(2,3,4,5,6,8,12,20,50,100\). The numerical outputs and the source code are both embedded; these finite checks illustrate the infinite argument but do not replace it. The analytically exact benchmark \(\gamma_3=2\) from [1] is recovered.

## Relationship to prior work

Evans–Majumdar [1] derive the exact finite-target mean time, the leading small-target objective and root equation \(F_\nu(\gamma_d)=2\) (their equations (67), (71), (73), (76), (77)). Those are prerequisites, not new discoveries here. Segura [2] develops stronger general Bessel-ratio Riccati monotonicity and inequalities; the argument here specializes established methods, so Bessel monotonicity by itself is not claimed as novel. The new target-specific conclusion is the **strict ordering and two-sided dimension brackets coupled with the explicitly computed subleading term \(8/(d-2)\)** in the continuum small-target optimal reset intensity. Bressloff [3] studies stochastic gating in a related spherical search, while Hartmann–Majumdar [4] obtain dimension scaling for a discrete lattice search; neither is the same continuum small-target Bessel-root expansion. DLMF [5] provides classical large-order special-function machinery from which related expansions may also be derivable.

## Limitations

The result is for the leading coefficient at fixed dimension as \(\epsilon\downarrow0\), then high-dimensional asymptotics of that coefficient's optimizer; it does not provide error bounds uniform as \(d\to\infty\) jointly with \(\epsilon\downarrow0\), and it does not characterize the finite-\(\epsilon\) optimizer. Special-function literature contains extensive bounds and asymptotics; priority for closely equivalent implicit-root expansions remains a residual risk despite the source-specific comparisons. Independent review has not been conducted.

## References

[1] M. R. Evans and S. N. Majumdar, *Diffusion with resetting in arbitrary spatial dimension*, arXiv:1404.4574v1 (17 April 2014), equations (65)–(77), https://arxiv.org/html/1404.4574v1 .

[2] J. Segura, *Monotonicity properties for ratios and products of modified Bessel functions and sharp trigonometric bounds*, arXiv:2105.02524 (2021), section 2, https://arxiv.org/abs/2105.02524 .

[3] P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739 (2020), https://arxiv.org/html/2009.02739v1 .

[4] A. K. Hartmann and S. N. Majumdar, *Diffusion with stochastic resetting on a lattice*, *Physical Review E* 112, 034102 (2025), https://doi.org/10.1103/1xkk-7q63 .

[5] NIST Digital Library of Mathematical Functions, section 10.41, https://dlmf.nist.gov/10.41 .
