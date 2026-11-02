# Sharp small-tempering trichotomy for Weibull-tailed Langevin diffusions

## Finding
Let \(V:\mathbb R\to[0,\infty)\) be an even, twice continuously differentiable confining potential, \(V(0)=0\), and suppose for some \(\eta>0\) that, as \(x\to\infty\),
\[
 V(x)\sim x^\eta,\qquad V'(x)\sim\eta x^{\eta-1},\qquad
 \frac{V''(x)}{V'(x)^2}\longrightarrow0,
\]
with \(V'(x)>0\) eventually. For \(0\le\ell\le1/2\), consider the diffusion whose generator is
\[
 \mathcal L_\ell f(x)=e^{2\ell V(x)}[f''(x)-(1-2\ell)V'(x)f'(x)].
\]
This uses the *unnormalized* target weight \(\rho(x)=e^{-V(x)}\); the invariant probability density is \(\rho/\int\rho\). Let \(\tau_0\) be its first hitting time of zero and set \(M_\ell=\sup_{x\in\mathbb R}\mathbb E_x\tau_0\). Then, writing
\[
 H(y)=e^{V(y)}\int_y^\infty e^{-V(z)}\,dz,
\]
we have the exact formula \(M_\ell=\int_0^\infty H(y)e^{-2\ell V(y)}dy\), and the following **sharp three-regime small-tempering law** as \(\ell\downarrow0\):
\[
 \begin{array}{ll}
 0<\eta<2:&\displaystyle M_\ell\sim
 \frac{\Gamma(2/\eta-1)}{\eta^2}(2\ell)^{1-2/\eta},\\[5pt]
 \eta=2:&\displaystyle M_\ell\sim\frac14\log(1/\ell),\\[5pt]
 \eta>2:&\displaystyle M_0-M_\ell\sim
 \frac{\Gamma(2/\eta)}{\eta(\eta-2)}(2\ell)^{1-2/\eta}.
 \end{array}
\]
In particular \(M_\ell<\infty\) for every \(\ell>0\), while \(M_0<\infty\) if and only if \(\eta>2\). For \(0\le\ell\le1/2\), this is also the exact threshold for uniform total-variation ergodicity. For \(\eta>2\), the improvement from infinitesimal tempering has a non-differentiable Hölder cusp at \(\ell=0\). The mapping \(\ell\mapsto M_\ell\) is strictly decreasing and strictly convex on \((0,1/2]\).

## Assumptions and scope
The coefficients are defined by the displayed generator, equivalently \(dX_t=-(1-2\ell)e^{2\ell V(X_t)}V'(X_t)dt+\sqrt2\,e^{\ell V(X_t)}dB_t\). The fixed noise normalization is essential for the numerical constants. The assumptions permit the smooth family \(V_\eta(x)=(1+x^2)^{\eta/2}-1\) for every \(\eta>0\). All expected times refer to the minimal diffusion on the full real line with \(X_0=x\); the supremum ranges over all finite initial locations. The assertions concern \(0\le\ell\le1/2\) unless explicitly stated otherwise.

The exponent \(\eta=2\) separates divergence of the worst-case mean at zero tempering from a finite mean with singular first-order response. These results concern fixed-target hitting of the origin, not hitting of an independent stationary-random target.

## Proof
**Scale, speed and existence.** Since \(\mathcal L_\ell=\rho^{-1}(\rho^{1-2\ell}\partial_x)'\), scale and speed densities, up to matching reciprocal constants, are \(s_\ell'(x)=e^{(1-2\ell)V(x)}\) and \(m_\ell(x)=e^{-V(x)}\). The speed is integrable; for \(\ell\le1/2\), scale has infinite endpoints. The Feller boundary test therefore gives non-explosion and recurrence, with invariant probability proportional to \(m_\ell\). Standard one-dimensional hitting-time Green formulas (or direct solution of \(\mathcal L_\ell u=-1\)) yield, for \(x\ge0\),
\[
 u_\ell(x)=\mathbb E_x\tau_0
 =\int_0^x e^{(1-2\ell)V(y)}\left(\int_y^\infty e^{-V(z)}dz\right)dy.
\]
Indeed \(u'_\ell=e^{(1-2\ell)V}\int_x^\infty e^{-V}\), and \((e^{-(1-2\ell)V}u'_\ell)'=-e^{-V}\). The positive monotone solution is the hitting-time expectation by the stopped Green representation and the natural/entrance boundary condition. By evenness the same formula with \(x\) replaced by \(|x|\) applies from the negative side. Monotone convergence gives the asserted exact formula for \(M_\ell\).

**Tail asymptotics.** Put \(S(x)=\int_x^\infty e^{-V(z)}dz\). L'Hôpital's rule, using the displayed condition on \(V''/(V')^2\), gives
\[
 S(x)\sim e^{-V(x)}/V'(x),\qquad
 H(x)\sim(\eta x^{\eta-1})^{-1}.
\]
Thus \(H\) is regularly varying with index \(1-\eta\), and \(V\) with index \(\eta\). For \(0<\eta<2\), a Laplace integral scaling \(u=2\ell x^\eta\), with standard Potter bounds splitting compact and far-tail regions, yields
\[
 M_\ell\sim\frac{1}{\eta^2}(2\ell)^{1-2/\eta}
 \int_0^\infty u^{2/\eta-2}e^{-u}du.
\]
For \(\eta=2\), \(H(x)\sim1/(2x)\), and the integration window \(1\ll x\ll\ell^{-1/2}\) gives \(M_\ell\sim\frac14\log(1/\ell)\); the compact and exponentially cut-off tails give lower-order terms.

For \(\eta>2\), \(H\) is integrable, so \(M_0<\infty\); similarly the other cases have \(M_0=\infty\). Subtracting the convergent integrals and applying the same regular-variation argument gives
\[
 M_0-M_\ell\sim\frac{(2\ell)^{1-2/\eta}}{\eta^2}
 \int_0^\infty u^{-2+2/\eta}(1-e^{-u})du
 =\frac{\Gamma(2/\eta)}{\eta(\eta-2)}(2\ell)^{1-2/\eta}.
\]
The last integral converges at both endpoints exactly for \(\eta>2\). Differentiation under the integral for \(\ell>0\) gives \(M'_\ell=-2\int VH e^{-2\ell V}<0\) and \(M''_\ell=4\int V^2H e^{-2\ell V}>0\).

**Uniform ergodicity.** When \(M_\ell<\infty\), Markov's inequality and repeated stopping at zero give a uniformly exponentially decaying tail for \(\tau_0\). For any fixed \(t_0>2M_\ell\), \(\inf_x\Pr_x(\tau_0\le t_0)>0\). The transition densities from zero over times in \([t_0,2t_0]\) share a positive lower bound on one common compact interval by strict ellipticity there. The strong Markov property gives a uniform Doeblin minorization of \(P_{2t_0}\), hence uniform total-variation convergence to stationarity. Conversely, if \(\ell=0\) and \(\eta\le2\), then \(|V'(x)|\le C(1+|x|)\). A Brownian-path/Gronwall comparison implies that \(X_t\to+\infty\) in probability for each fixed \(t\) as \(X_0=x\to+\infty\); hence uniform total-variation convergence is impossible.

**Exponential endpoint outside the theorem.** If \(\ell>1/2\), then scale has finite limits at both ends while speed is integrable. The Feller boundary test makes both endpoints accessible exits; the minimal process leaves \(\mathbb R\) in finite time almost surely. Thus the nonexplosive range stated above cannot be enlarged in this model.

## Verification
The included `verify_tempering.py` independently checks a power-potential scale–speed identity against a hypergeometric form, the exact Gaussian expression, endpoint constants, monotonicity, and sample values using high-precision arithmetic; 187 checks passed. The source and recorded output are included, with pinned `mpmath` version in `requirements.txt`.

For the auxiliary power potential \(V(x)=|x|^\eta\) on \(x>0\) (the model can be interpreted in scale–speed form at zero for non-smooth exponents), direct order reversal gives the exact check
\[
 M_\ell=\frac{\Gamma(2/\eta)}{\eta^2}\int_0^1
 v^{1/\eta-1}\big[1-(1-2\ell)v\big]^{-2/\eta}dv
 =\frac{\Gamma(2/\eta)}{\eta}
 {}_2F_1(2/\eta,1/\eta;1+1/\eta;1-2\ell).
\]
For \(\eta=2\), this specializes to \(M_\ell=\operatorname{artanh}(\sqrt{1-2\ell})/[2\sqrt{1-2\ell}]\) on \(0<\ell<1/2\), continuously extended by \(M_{1/2}=1/2\). These calculations test constants; no finite computation is used as proof of a statement for all potentials or all parameters.

## Relationship to prior work
Mijatović and Xie (arXiv:2610.30024v1, first publicly available 21 October 2026) analyze temperature thresholds for **polynomial-tailed** tempered Langevin targets, explicitly separating their assumptions from rapidly decaying targets. The displayed diffusion uses their tempering architecture but introduces a Weibull-tail class with a different zero-temperature response. Bansaye et al. (arXiv:1711.08603) analyze general diffusions coming down from infinity; Pinsky (arXiv:1903.12005) gives general diffusion hitting-time Green formulas and entrance-boundary criteria. Cattiaux and Guillin (arXiv:1604.06336) give broad Lyapunov/hitting-time uniform ergodicity theory. Douc, Fort and Guillin (arXiv:math/0605791) discuss convergence rates of Langevin-type diffusions and related state-dependent diffusion coefficients. Arapostathis, Pang and Sandrić (arXiv:1907.05250, Section 3.1) analyze polynomial-tailed tempered Langevin diffusions and Wasserstein convergence rates. None of the general entrance/Green identities is claimed as new. The specific three-regime **sharp small-tempering equivalences with constants**, including the superquadratic nonanalytic response, are the focus here.

## Limitations
Only one-dimensional even smooth potentials meeting the stated regular-variation and derivative assumptions are treated. Higher dimensions, asymmetric potentials, non-regularly varying tails, and uniform estimates over a varying class of potentials are not established. The uniform-ergodicity argument gives no optimal mixing rate. The auxiliary pure-power calculation for \(\eta<2\) concerns a half-line scale–speed realization rather than a globally \(C^2\) potential. The constants rely on the generator's unnormalized-target time convention. Historical priority is not independently certified; sufficiently broad earlier diffusion Tauberian results might imply the special asymptotics after specialization.

## References
1. A. Mijatović and H. Xie, *Tempered Langevin diffusions with polynomial-tailed targets: explosions, moment thresholds and ergodicity*, arXiv:2610.30024v1 (21 October 2026), https://arxiv.org/html/2610.30024v1.
2. V. Bansaye, P. Collet, S. Martinez, S. Méléard and J. San Martin, *Diffusions from Infinity*, arXiv:1711.08603 (2017), https://arxiv.org/abs/1711.08603.
3. R. G. Pinsky, *Kemeny's constant for one-dimensional diffusions*, arXiv:1903.12005 (2019), https://arxiv.org/abs/1903.12005.
4. P. Cattiaux and A. Guillin, *Hitting times, functional inequalities, Lyapunov conditions and uniform ergodicity*, arXiv:1604.06336 (2016), https://arxiv.org/abs/1604.06336.
5. R. Douc, G. Fort and A. Guillin, *Subgeometric rates of convergence of \(f\)-ergodic strong Markov processes*, arXiv:math/0605791 (2006), https://arxiv.org/abs/math/0605791.
6. A. Arapostathis, G. Pang and N. Sandrić, *Subexponential upper and lower bounds in Wasserstein distance for Markov processes*, arXiv:1907.05250 (2019), https://arxiv.org/abs/1907.05250.
