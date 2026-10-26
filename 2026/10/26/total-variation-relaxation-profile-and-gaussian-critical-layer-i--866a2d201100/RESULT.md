# Total-variation relaxation profile and Gaussian critical layer in nested stochastic resetting

## Finding
Consider equal-rate nested Brownian resetting on the real line, starting with every particle at the origin. Let \(\mu_{n,t}\) be the position law of particle \(n\) at time \(t\), and let \(\pi_n\) be its stationary position law. For every \(r,D>0\), set \(d_n(t)=d_{\mathrm{TV}}(\mu_{n,t},\pi_n)\), with the total-variation convention \(d_{\mathrm{TV}}(\mu,\nu)=\sup_A|\mu(A)-\nu(A)|\). The following statements hold.

1. For each finite integer \(n\ge1\) and \(t>0\), the difference between the two even spatial densities is strictly positive on one central interval and strictly negative outside that interval. There is exactly one positive crossing.
2. For every fixed \(0<\theta<1\),
   \[
   \lim_{n\to\infty}d_n(\theta n/r)
   =F(\theta):=2\left[\Phi\!\left(\sqrt{\frac{\log(1/\theta)}{1-\theta}}\right)-\Phi\!\left(\sqrt{\frac{\theta\log(1/\theta)}{1-\theta}}\right)\right].
   \]
   For each fixed \(\theta\ge1\) the limit is zero. For every \(\theta>1\) and all \(n\ge1\),
   \[
   d_n(\theta n/r)\le \exp\{-n[\theta-1-\log\theta]\}.
   \]
3. For any fixed real \(s\), whenever \(n+s\sqrt n>0\),
   \[
   \lim_{n\to\infty}\sqrt n\,d_n\!\left(\frac{n+s\sqrt n}{r}\right)
   =\phi(1)\left[\phi(s)-s(1-\Phi(s))\right],
   \]
   where \(\phi\) and \(\Phi\) are the standard normal density and distribution function. In particular, \(\sqrt n\,d_n(n/r)\to e^{-1/2}/(2\pi)\).

The middle statement is a macroscopic relaxation **profile**, not a conventional sharp mixing cutoff: at a fixed fraction of \(n/r\) less than one, the distance has a nonzero nonunit limit. The last statement describes the diminishing residual distance in an \(O(\sqrt n/r)\) time window.

## Assumptions and scope
There are at least \(n\) one-dimensional Brownian coordinates, each with diffusion coefficient \(D>0\) (free generator \(D\partial_{xx}\)). Independent Poisson clocks of common rate \(r>0\) govern resets: particle \(1\) goes to the fixed location \(0\), and particle \(i\ge2\) instantaneously copies particle \(i-1\). All initial coordinates equal \(0\). The theorem concerns **one tagged particle's position marginal**, not the joint law of the chain. The integer \(n\) is arbitrary and may tend to infinity with fixed \(r,D\). The density \(G_D(x,v)=(4\pi Dv)^{-1/2}\exp[-x^2/(4Dv)]\) is the free Brownian propagator for \(v>0\). Set \(G_D(\cdot,0)=\delta_0\). The exponential and Gamma distributions here use rate rather than scale parametrization.

## Proof
**Exact random clock, credited starting formula.** Equation (2.10) of Britton, Le Jeune, Alston, Bressloff and Bertrand (2026) gives the full transient density as a Gamma-weighted Gaussian integral and an unreset Gaussian term. If \(T_n\) is Gamma with integer shape \(n\), rate \(r\), this can equivalently be written
\[
\mu_{n,t}=\mathbb E\,G_D(\cdot,\min(T_n,t)),\qquad \pi_n=\mathbb E\,G_D(\cdot,T_n).
\]
These identities are existing exact distributional formulas, not the novelty claim. They also follow from the published renewal equation, because \(\mathbb P(T_n>t)=e^{-rt}\sum_{j=0}^{n-1}(rt)^j/j!\). Scaling space by \(\sqrt{2Dn/r}\), time by \(n/r\), and defining \(U_n=rT_n/n\sim\mathrm{Gamma}(n,\text{rate }n)\), total variation is unchanged and the two densities become \(p_{n,c}=\mathbb E g_{\min(U_n,c)}\) and \(q_n=\mathbb E g_{U_n}\), where \(c=rt/n\), \(g_v(y)=(2\pi v)^{-1/2}e^{-y^2/(2v)}\).

**Finite-index crossing.** For any \(c>0\),
\[
p_{n,c}(y)-q_n(y)=\mathbb E[\mathbf1_{\{U_n>c\}}(g_c(y)-g_{U_n}(y))].
\]
After division by \(g_c(y)>0\), the expression is
\[
\mathbb P(U_n>c)-\mathbb E\left[\mathbf1_{\{U_n>c\}}\sqrt{\frac c{U_n}}\exp\!\left(\frac{y^2}{2}\left(\frac1c-\frac1{U_n}\right)\right)\right].
\]
For \(y\ge0\), the second term is continuous and strictly increasing in \(y\). At zero it is strictly less than \(\mathbb P(U_n>c)\); it diverges as \(y\to\infty\) by monotone convergence, since the Gamma law assigns positive mass to any interval above \(c\). Therefore exactly one positive zero occurs; parity gives symmetric zeros. Integrating the positive central difference yields exactly the total variation, and the central-interval identity is an exact finite-index formula.

**Fixed fractional time.** Since \(\mathbb E U_n=1\) and \(\mathrm{Var}(U_n)=1/n\), the clocks converge in probability to one. If \(0<\theta<1\), then \(p_{n,\theta}\to g_\theta\) and \(q_n\to g_1\) in \(L^1(\mathbb R)\): continuity of Gaussian densities in their positive variance parameter in \(L^1\), together with concentration of \(U_n\) and the norm bound two, gives dominated convergence. The two limiting normal densities cross at \(\pm a_\theta\), where \(a_\theta^2=\theta\log(1/\theta)/(1-\theta)\). Their total variation is precisely \(F(\theta)\) above. For \(\theta=1\), the same \(L^1\) concentration gives limit zero. For \(\theta>1\), the clock coupling yields
\[
d_n(\theta n/r)\le \mathbb P(U_n>\theta)\le e^{-n(\theta-1-\log\theta)},
\]
where the last step minimizes the Gamma moment-generating-function Chernoff bound at its positive optimum. At \(t=0\), \(\mu_{n,0}=\delta_0\) while \(\pi_n\) is absolutely continuous, hence total variation is one.

**Critical window with coefficient.** Take \(c_n=1+s/\sqrt n\). Set \(H_n=\sqrt n(U_n-1)\); the central-limit theorem for an average of independent exponential variables gives \(H_n\Rightarrow Z\sim N(0,1)\). The \(L^2\) bound \(\sup_n\mathbb E H_n^2=1\) guarantees uniform integrability of the positive part and
\[
\sqrt n\,\mathbb E(U_n-c_n)_+\to\mathbb E(Z-s)_+=\phi(s)-s[1-\Phi(s)].
\]
For each variance \(v>0\), write \(g'_v=\partial_v g_v\). The signed density difference satisfies
\[
p_{n,c_n}-q_n=-\mathbb E\left[\mathbf1_{\{U_n>c_n\}}\int_{c_n}^{U_n}g'_v\,dv\right].
\]
On \(\{U_n\ge1/2\}\) and for large \(n\), both \(c_n\ge1/2\) and the intervening variances exceed \(1/2\). Since \(\sup_{v\ge1/2}\|\partial_v^2g_v\|_1<\infty\), replacing \(g'_v\) by \(g'_1\) costs at most a constant times \(\mathbb E[(U_n-1)^2+(c_n-1)^2]=O(n^{-1})\) in \(L^1\). On the complementary event, \(\mathbb P(U_n<1/2)\le e^{-cn}\) for some \(c>0\), and the original two-density difference has norm at most two, so it is negligible even after multiplication by \(\sqrt n\). Hence in \(L^1(\mathbb R)\),
\[
\sqrt n(p_{n,c_n}-q_n)\longrightarrow-[\phi(s)-s(1-\Phi(s))]g'_1.
\]
Now \(g'_1(y)=\tfrac12(y^2-1)\phi(y)\), and an elementary Gaussian integral gives \(\tfrac12\|g'_1\|_1=\phi(1)\). Taking half the \(L^1\) norm proves the critical-window formula. For \(s=0\), use \(\phi(0)\phi(1)=e^{-1/2}/(2\pi)\).

## Verification
The accompanying standalone `verify.py` uses Python 3, SciPy and NumPy, with deterministic high-accuracy quadrature (no random sampling). Run `python verify.py` from its own directory. Its 84 assertions compare independent quadrature against the finite-index characteristic function; inspect precritical and critical-window numerical sequences; check the total-variation crossing numerically; verify the Gamma upper-tail coupling inequality; and verify the critical coefficient. An exact characteristic-function identity used in the code is
\[
\mathbb E[e^{ikY}]=e^{-k^2c/2}Q(n,nc)+(1+k^2/(2n))^{-n}P(n,nc+k^2c/2),
\]
with \(Y=X_n(t)/\sqrt{2Dn/r}\), and regularized upper/lower incomplete-Gamma functions \(Q,P\). Numerical comparisons do not establish the universal quantifiers, root uniqueness, or limits; the proof above supplies those arguments.

## Relationship to prior work
Britton et al., *Approach to Steady-State in Nested Resetting Processes* (arXiv:2609.25252v1, 2026), derives the exact transient solution used as input here in its equations (2.9)–(2.14) and studies local spatial accumulation times and heterogeneous resetting. Alston, Britton and Bertrand (arXiv:2502.03225v1, 2025) establishes the stationary marginal and correlations of the nested chain. Bressloff (arXiv:2104.09365v1, 2021) treats accumulation-time relaxation of a single resetting particle. None of those exact densities, stationary formulas or local accumulation-time laws is presented as new here. The claim assessed here is instead the global *total-variation* profile and critical-order coefficient in the joint particle-index/time limit, accompanied by a finite-index one-crossing theorem. These results are mathematical consequences requiring further analysis of the established exact formula; broader implicit coverage in literature on normal variance mixtures remains a caveat.

## Limitations
The conclusions apply to the tagged marginal for one-dimensional free Brownian motion with equal, positive Poisson rates and all-zero initial data, not the joint many-particle mixing distance, unequal-rate hierarchies, confinement, state-dependent resetting or nonzero arbitrary initial laws. The bounds are for fixed \(D,r\) and stated asymptotic scales, not an explicit finite-\(n\) uniform error in \(s\) or \(\theta\). No claim of a traditional total-variation cutoff is made. Published closed-form densities make implicit derivation possible; the precise originality of the resulting quantified theorem requires independent evaluation.

## References
1. C. Britton, B. Le Jeune, H. Alston, P. C. Bressloff and T. Bertrand, *Approach to Steady-State in Nested Resetting Processes*, arXiv:2609.25252v1 (first posted 2026-09-21), https://arxiv.org/abs/2609.25252.
2. H. Alston, C. Britton and T. Bertrand, *Nested Stochastic Resetting: Nonequilibrium Steady-states and Exact Correlations*, arXiv:2502.03225v1 (2025), https://arxiv.org/abs/2502.03225.
3. P. C. Bressloff, *Accumulation Time of Stochastic Processes with Resetting*, arXiv:2104.09365v1 (2021), https://arxiv.org/abs/2104.09365.
