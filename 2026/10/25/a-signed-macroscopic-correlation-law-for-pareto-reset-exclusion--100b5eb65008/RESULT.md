# A signed macroscopic correlation law for Pareto-reset exclusion

## Finding

Consider the symmetric simple exclusion process (SSEP) on \(\mathbb Z\), with nearest-neighbor exchanges at rate one per bond and initial step \(\eta_x^*=\mathbf1_{\{x\leq0\}}\). Independently reset **the entire configuration** to this step after successive Pareto interarrival times with shape \(\alpha>1\) and minimum duration \(R>0\). Observe the process in its stationary renewal regime. For each real \(y\), set \(x_R(y)=\lfloor y\sqrt R\rfloor\).

Let \(U\) have the probability density
\[
 w_\alpha(u)=\frac{\alpha-1}{\alpha}
 \begin{cases}
 1,&0<u<1,\\
 u^{-\alpha},&u\geq1,
 \end{cases}
\]
and define \(h(y,u)=\tfrac12\operatorname{erfc}(y/(2\sqrt u))\). For every pair of **distinct** real numbers \(y,z\),
\[
 \boxed{\lim_{R\to\infty}\operatorname{Cov}\bigl(\eta_{x_R(y)},\eta_{x_R(z)}\bigr)
 =K_\alpha(y,z):=\operatorname{Cov}\bigl(h(y,U),h(z,U)\bigr).}
\]
The covariance on the left is evaluated in the stationary reset process with cutoff \(R\). The right side is an explicit, absolutely convergent one-dimensional integral:
\[
 K_\alpha(y,z)=\int_0^\infty w_\alpha(u)h(y,u)h(z,u)\,du
 -\left(\int_0^\infty w_\alpha(u)h(y,u)\,du\right)
 \left(\int_0^\infty w_\alpha(u)h(z,u)\,du\right).
\]
It has the **strict sign classification**
\[
 \boxed{K_\alpha(y,z)>0\ \text{if }yz>0,\qquad
 K_\alpha(y,z)<0\ \text{if }yz<0,\qquad
 K_\alpha(y,z)=0\ \text{if }yz=0.}
\]
Thus equal-time correlations remain macroscopic and positive between sites on the same side of the resetting front, **despite the nonpositive correlations of ordinary SSEP at every fixed elapsed time**. Sites on opposite sides have a strictly negative limiting correlation.

More strongly, couple all stationary models using the same variable \(U\), and for any bounded interval \(I\subset\mathbb R\) set
\[
 M_R(I)=R^{-1/2}\sum_{x:\,x/\sqrt R\in I}\eta_x,
 \qquad F_I(U)=\int_Ih(y,U)\,dy.
\]
Then \(M_R(I)\to F_I(U)\) in \(L^2\), jointly for any fixed finite family of intervals. Consequently the stationary macroscopic density profile is **random**, rather than the averaged deterministic profile. Its nonzero block fluctuations are solely due to the common renewal age at leading order. Intervals strictly on the same side have positive limiting covariance, whereas intervals on opposite sides have negative limiting covariance.

## Assumptions and scope

The state space is \(\{0,1\}^{\mathbb Z}\). Every nearest-neighbor bond has an independent exponential clock of rate one; at a ring the two occupations are exchanged, implementing SSEP. Between resets, motion starts from the deterministic occupation step. Reset interarrivals are iid, independent of the exchange clocks, with survival function \(\Pr(\tau_R>t)=1\) for \(0\leq t<R\), and \((R/t)^\alpha\) for \(t\geq R\). The mean interarrival is \(\mu_R=\alpha R/(\alpha-1)\), finite because \(\alpha>1\). A two-sided stationary renewal construction gives the stationary observation law. There is no particle reservoir and no independent resetting of individual particles. The thermodynamic lattice is taken first; the limit is then \(R\to\infty\) with spatial locations scaled by \(\sqrt R\). The result concerns two different sites (or macroscopic blocks), not the diagonal Bernoulli variance of a single site.

## Proof

**1. Renewal age.** At stationarity, the age \(A_R\) since the last complete reset has density \(\Pr(\tau_R>t)/\mu_R\). Therefore \(A_R=RU\) in distribution, where \(U\) has precisely the stated density. Conditional on \(U=u\), the observed occupation field has the law of ordinary unreset SSEP started from \(\eta^*\) and run for time \(Ru\). The normalization \(\int w_\alpha=1\) follows from \(1+\int_1^\infty u^{-\alpha}\,du=\alpha/(\alpha-1)\).

**2. One-point scaling.** Write \(\rho_x(t)=\mathbb E_{\eta^*}\eta_x(t)\). The exclusion generator implies the discrete heat equation \(\partial_t\rho_x=\rho_{x-1}+\rho_{x+1}-2\rho_x\), with \(\rho_x(0)=\mathbf1_{\{x\leq0\}}\). Thus
\[
 \rho_x(t)=\sum_{j\leq0}p_t(x-j),\qquad p_t(k)=e^{-2t}I_{|k|}(2t),
\]
where \(I_n\) is the modified Bessel function. The central limit theorem for the continuous-time simple random walk (variance \(2t\)) gives, for every \(u>0\) and \(y\in\mathbb R\),
\[
 \lim_{R\to\infty}\rho_{x_R(y)}(Ru)
 =\tfrac12\operatorname{erfc}\!\left(\frac{y}{2\sqrt u}\right)=h(y,u).
\]
Since \(0\leq\rho\leq1\), averaging over \(U\) is justified by dominated convergence.

**3. Exclusion correlations decay when conditioned on age.** For distinct \(i<j\), put \(C_{ij}(t)=\mathbb E_{\eta^*}[\eta_i(t)\eta_j(t)]-\rho_i(t)\rho_j(t)\). The two-site exclusion generator \(\mathcal L^{(2)}\), acting on functions of ordered distinct sites, gives the exact inhomogeneous equation
\[
 \partial_tC_{ij}=(\mathcal L^{(2)}C)_{ij}
 -\mathbf1_{\{j=i+1\}}\bigl(\rho_{i+1}(t)-\rho_i(t)\bigr)^2,
 \qquad C_{ij}(0)=0.
\]
For nonadjacent sites both coordinates undergo the free discrete Laplacian; at adjacent sites moves attempting to collide are suppressed. The negative source is obtained directly by subtracting the derivatives of the two one-point means from the derivative of \(\mathbb E[\eta_i\eta_{i+1}]\). Positivity of the two-particle semigroup immediately yields \(C_{ij}(t)\leq0\) at all times.

For the step, the discrete gradient telescopes exactly to \(\rho_{i+1}(s)-\rho_i(s)=-p_s(i)\). In the two-particle exclusion walk the gap \(D_t=j_t-i_t\in\{1,2,\ldots\}\) jumps up and down at rate two away from one, and from one it can only jump to two at rate two. Let \(q_t(k)=e^{-4t}I_{|k|}(4t)\), the heat kernel for the rate-two walk on \(\mathbb Z\). Reflection at the boundary gives
\[
 \Pr(D_v=1\mid D_0=d)=q_v(d-1)+q_v(d)\leq 2q_v(0).
\]
Standard Fourier integral bounds give \(\sup_kp_s(k)\leq c(1+s)^{-1/2}\) and \(q_v(0)\leq c(1+v)^{-1/2}\). Duhamel's formula consequently yields a uniform, position-independent estimate
\[
 0\leq-C_{ij}(t)\leq c\int_0^t\frac{ds}{(1+s)\sqrt{1+t-s}}
 \leq c'\frac{1+\log(1+t)}{\sqrt{1+t}},\qquad t\geq0.
\]
(The final estimate follows by splitting the integral at \(s=t/2\).) In particular, conditional pair correlations vanish as \(Ru\to\infty\) for every \(u>0\), even with sites located at macroscopically separated scaled positions.

**4. Stationary pair limit.** For distinct \(y,z\), the two sites \(x_R(y),x_R(z)\) are distinct for all sufficiently large \(R\). By step 3 and the one-point scaling,
\[
 \mathbb E_{\eta^*}[\eta_{x_R(y)}(Ru)\eta_{x_R(z)}(Ru)]
 \longrightarrow h(y,u)h(z,u)
\]
for every \(u>0\). All terms lie in \([0,1]\), so dominated convergence under \(w_\alpha\) identifies the stationary first and second moments and proves the displayed formula for \(K_\alpha\).

**5. Random macroscopic profile.** Given \(U=u\), the variance of a sum of occupations over \(m\) distinct sites is at most \(m/4\), because every one-site Bernoulli variance is at most \(1/4\) and all off-diagonal covariances are nonpositive by step 3. Thus the conditional variance of \(M_R(I)\) is at most \((|I|\sqrt R+2)/(4R)\), uniformly over \(u\). The conditional mean is a Riemann sum of \(\rho_x(Ru)\) and converges to \(F_I(u)\) for every \(u>0\). Boundedness of the means on bounded intervals and dominated convergence over \(U\) give \(L^2\) convergence. Joint convergence follows by summing finitely many \(L^2\) errors.

**6. Strict signs.** For \(u>0\), direct differentiation yields
\[
 \frac{\partial h(y,u)}{\partial u}=
 \frac{y}{4\sqrt\pi\,u^{3/2}}\exp\!\left(-\frac{y^2}{4u}\right).
\]
Hence \(h(y,\cdot)\) is strictly increasing if \(y>0\), strictly decreasing if \(y<0\), and constant if \(y=0\). For an independent copy \(U'\), the identity
\[
 2\operatorname{Cov}(f(U),g(U))=
 \mathbb E[(f(U)-f(U'))(g(U)-g(U'))]
\]
proves each strict sign because \(U\) is nonatomic and nondegenerate. Applying the same reasoning to integrals \(F_I(U)\) gives the block-covariance assertions.

## Verification

The included standalone `check_stdlib.py` runs without third-party packages. It performs 70 deterministic checks using exact state enumeration of the four-site SSEP, one- and two-particle dual generators, a numerical evaluation of the specified Pareto-age covariance integrals, and their strict sign tests. Run `python3 check_stdlib.py`; the archived output is `check_output.txt`. For example, \(K_{3/2}(1,2)\approx0.0182786826692\) and \(K_{3/2}(-1,2)\approx-0.0182786826692\). These numerical tests do not prove the limit or its strict sign; the generator/Duhamel and monotonicity arguments above do.

## Relationship to prior work

Mishra and Basu's [2022 preprint](https://arxiv.org/abs/2211.14120), published publicly on 25 November 2022, studies the same resetting family on finite periodic exclusion lattices and derives stationary one-point density and current laws by renewal methods. Its equation (13) supplies the known stationary renewal mixture used in step 1, but it does not state or derive the signed macroscopic equal-time covariance limit or random hydrodynamic profile proved here.

Basu, Kundu, and Pal's [2019 work](https://arxiv.org/abs/1906.11801) concerns a single Poisson complete-reset configuration and computes densities and currents. Sadekar and Basu's [2020 work](https://arxiv.org/abs/2004.00951), especially Section 5.3, explicitly studies finite-ring spatial density correlations under **dichotomous Poisson resets** and notes the difficulty of obtaining analytic pair correlations; it does not calculate the Pareto single-step diffusive scaling limit. Biroli, Larralde, Majumdar, and Schehr's [2022 preprint](https://arxiv.org/abs/2211.00563) identifies correlations arising from a common reset age in a gas of *independent Brownian particles*. That known common-age mechanism is not claimed as new; the exclusion-specific sign theorem and proof that dynamical anticorrelations vanish in the diffusive scaling are the assessed contribution. Santra and Singh's [2023 preprint](https://arxiv.org/abs/2311.04097) concerns correlations of tagged particles in the different random-average single-file process.

## Limitations

The limit holds for \(\alpha>1\) with a stationary renewal construction; it does not extend as stated to infinite-mean interarrival distributions or independently reset particles. The result assumes a deterministic step reset, nearest-neighbor symmetric exclusion, and the scale \(\sqrt R\); microscopic-distance corrections, finite-ring boundary effects, and temporal covariance are not determined. Common-age-induced correlations in other models are known, and the literature comparison cannot exclude every equivalent theorem in general interacting-particle hydrodynamics. This is an analytic self-review result, not an independently audited publication.

## References

1. S. Mishra and U. Basu, *Symmetric Exclusion Process under Stochastic Power-law Resetting*, arXiv:2211.14120 (first public version 25 November 2022), https://arxiv.org/abs/2211.14120.
2. U. Basu, A. Kundu, and A. Pal, *Symmetric Exclusion Process under Stochastic Resetting*, arXiv:1906.11801 (2019), https://arxiv.org/abs/1906.11801.
3. O. Sadekar and U. Basu, *Zero-current Nonequilibrium State in Symmetric Exclusion Process with Dichotomous Stochastic Resetting*, arXiv:2004.00951 (2020), https://arxiv.org/abs/2004.00951.
4. M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Extreme Statistics and Spacing Distribution in a Brownian Gas Correlated by Resetting*, arXiv:2211.00563 (2022), https://arxiv.org/abs/2211.00563.
5. S. Santra and P. Singh, *Exact Fluctuation and Long-range Correlations in a Single-file Model under Resetting*, arXiv:2311.04097 (2023), https://arxiv.org/abs/2311.04097.
