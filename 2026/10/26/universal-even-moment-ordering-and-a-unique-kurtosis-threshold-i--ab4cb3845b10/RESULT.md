# Universal even-moment ordering and a unique kurtosis threshold in active rank diffusion

## Finding
Consider the zero-temperature attractive one-dimensional Coulomb (rank-interaction) run-and-tumble gas, in its centered large-population stationary state, with attraction strength \(\kappa>0\), reversal rate \(\gamma>0\), and self-propulsion speed \(v>\kappa/2\). Write \(b=v/\kappa\), and let \(X_b\) have its normalized limiting one-particle position distribution. For every integer \(m\ge2\), the dimensionless even-moment ratio
\[
R_m(b)=\frac{\mathbb E[|X_b|^{2m}]}{(\mathbb E[X_b^2])^m}
\]
is **strictly increasing throughout \(b\in(1/2,\infty)\)**, including the edge-cluster regime \(1/2<b<1\), the uniform-density junction \(b=1\), and the smooth infinite-support regime \(b>1\). All moments involved are finite and the variance is positive in this domain.

In particular, the excess kurtosis \(E(b)=R_2(b)-3\) is strictly increasing. It tends to \(-2\) as \(b\downarrow1/2\), equals \(-6/5\) at \(b=1\), tends to \(6/5\) as \(b\to\infty\), and vanishes at exactly one speed ratio:
\[
 b_*=\sqrt{1+t_*}=1.543593833794468779\ldots,
\quad \frac{\pi^4}{120}t_*^4-t_*^2-\frac23t_*-\frac2{15}=0,
\quad t_*>0.
\]
It is negative for \(1/2<b<b_*\) and positive for \(b>b_*\). Thus the kurtosis sign change is distinct from the previously known cluster and support transitions at \(b=1/2\) and \(b=1\).

## Assumptions and scope
The microscopic model is \(\dot x_i=(\kappa/N)\sum_{j=1}^N\operatorname{sgn}(x_j-x_i)+v\sigma_i(t)\), with \(\operatorname{sgn}(0)=0\), independent telegraph directions \(\sigma_i\in\{-1,+1\}\) reversing at rate \(\gamma\), no translational Brownian noise, and no external confining potential. The large-\(N\) stationary one-particle density/measure and its edge-cluster jump conditions are those established in Touzo and Le Doussal (2023), equations (17), (21), and the accompanying stationary phase analysis. Coordinates are centered at the collective center of mass before taking the stationary distribution limit. This result is an exact theorem **for that limiting stationary measure**, not a new derivation of propagation of chaos or a finite-\(N\) limit theorem.

Define \(U\sim\mathrm{Uniform}(0,1)\) and an independent fair sign \(\varepsilon\). The original stationary rank parametrization has the following equivalent quantile representation, valid for \(b>1/2\):
\[
 X_b\ \overset{d}=\ \frac\kappa\gamma\,\varepsilon Q_b(U),\qquad
 Q_b(u)=\begin{cases}
 u+(b^2-1)\operatorname{artanh}u,&b\ge1,\[2pt]
 z+(b^2-1)\operatorname{artanh}z,\quad z=\min\{u,2b-1\},&1/2<b<1.
 \end{cases}
\]
For \(b<1\), \(Q_b\) is constant for \(u\ge2b-1\), representing an atom of mass \(1-b\) at each edge; for \(b=1\) the law is uniform on \([-\kappa/\gamma,\kappa/\gamma]\). For \(b<1/2\), the stationary state is collapsed and has zero variance. At the boundary \(b=1/2\), the positive-speed-limit quantile also collapses; no critical finite-system dynamics is asserted. Normalized moment ratios are defined here only for \(b>1/2\).

## Proof
**1. Derive the quantile from the source stationary equations.** With rank \(r(x)=\int_{-\infty}^x\rho_s(dy)-1/2\), put \(u=2r\). In the smooth region the stationary relation (source equation (17)) is \(\gamma x/\kappa=u+(b^2-1)\operatorname{artanh}u\). Rank increments have unit-uniform quantiles, and symmetry supplies the independent sign. For \(1/2<b<1\), the original edge jump condition (source equation (21)) is \(r(x_e^-)=b-1/2\), hence the smooth region ends at \(u=2b-1\), and the remaining uniform rank interval is mapped to the edge atom. These facts yield the stated \(Q_b\). Its continuous branch has derivative \((b^2-u^2)/(1-u^2)>0\) for the ranges used, so \(Q_b\) is nondecreasing, strictly increasing before any edge plateau, and positive away from zero.

**2. Establish a parameterwise quantile-ratio order.** For \(0<u<1\), set \(H(u)=\operatorname{artanh}(u)/u\), which is strictly increasing because \(H(u)=\int_0^1(1-u^2z^2)^{-1}dz\). Fix \(1/2<b_1<b_2\). On the interval before the first edge plateau, where both quantiles are given by the untruncated formula, their ratio equals
\[
\frac{Q_{b_2}(u)}{Q_{b_1}(u)}=
\frac{1+(b_2^2-1)H(u)}{1+(b_1^2-1)H(u)}.
\]
Its derivative with respect to \(H\) is \((b_2^2-b_1^2)/[1+(b_1^2-1)H]^2>0\). If \(b_1<1\), beyond its edge point the denominator is constant and the numerator remains increasing until its own edge (if any); after that both are constant. Thus the ratio is nondecreasing for all \(u\in(0,1)\), and strictly increasing on a nonempty interval. This also covers comparisons straddling \(b=1\).

**3. Transfer the quantile-ratio order to every normalized even moment.** The following elementary monotone-likelihood lemma applies. Let \(p,q>0\) be nondecreasing functions on \((0,1)\), with \(q/p\) nondecreasing, and with finite required moments. For \(m>1\), set \(p_s=p^{1-s}q^s\), \(0\le s\le1\). Direct differentiation gives
\[
\frac d{ds}\log\frac{\int_0^1p_s^m}{(\int_0^1p_s)^m}
=m\left(\mathbb E_{p_s^m}[\log(q/p)]-\mathbb E_{p_s}[\log(q/p)]\right)\ge0.
\]
Here \(\mathbb E_w\) denotes expectation under density proportional to \(w(u)\). The inequality follows from nonnegative covariance of the two increasing functions \(p_s^{m-1}\) and \(\log(q/p)\), under the density proportional to \(p_s\). It is strict when both vary on an interval of positive length. The endpoint singularities of \(\operatorname{artanh}\) are logarithmic, so differentiation is justified by integrability. Apply this lemma to \(p=Q_{b_1}^2\) and \(q=Q_{b_2}^2\). All hypotheses hold by step 2, and strictness holds before the first plateau. Therefore \(R_m(b_1)<R_m(b_2)\) for every \(m\ge2\).

**4. Evaluate the unique kurtosis zero.** For \(b\ge1\), set \(t=b^2-1\ge0\), and let \(W\) be uniform on \((-1,1)\), \(T=\operatorname{artanh}W\). Then \(X_b\overset d=(\kappa/\gamma)(W+tT)\). The beta integral, under the substitution \(y=(1+W)/2\), gives, for \(|z|<2\),
\[
M_T(z)=\mathbb E[e^{zT}]=\Gamma(1+z/2)\Gamma(1-z/2)=\frac{\pi z/2}{\sin(\pi z/2)},
\]
\[
\mathbb E[W e^{zT}]=\tfrac z2 M_T(z),\quad
\mathbb E[W^2e^{zT}]=\tfrac{z^2+2}{6}M_T(z),\quad
\mathbb E[W^3e^{zT}]=\tfrac{z(z^2+8)}{24}M_T(z).
\]
Their derivatives at zero yield the exact moments \(M_2(t)=\mathbb E[(W+tT)^2]\) and \(M_4(t)=\mathbb E[(W+tT)^4]\):
\[
M_2(t)=\frac13+t+\frac{\pi^2}{12}t^2,
\]
\[
M_4(t)=\frac15+\frac43t+(2+\frac{\pi^2}{6})t^2+\frac{\pi^2}{2}t^3+\frac{7\pi^4}{240}t^4.
\]
Subtracting three times the squared variance cancels the cubic term and gives
\[
M_4(t)-3M_2(t)^2=\frac{\pi^4}{120}t^4-t^2-\frac23t-\frac2{15}.
\]
This polynomial is negative at zero and positive for sufficiently large \(t\). Its ordered nonzero coefficients have exactly one sign change, so Descartes' rule of signs gives exactly one positive root. Since \(M_2(t)>0\), this root determines the unique zero of excess kurtosis on \(b\ge1\). Strict monotonicity from step 3 shows the entire edge-cluster region has negative excess kurtosis as well. The endpoint limits follow from quantile convergence: a symmetric two-point law as \(b\downarrow1/2\), a centered uniform law at \(b=1\), and the logistic-quantile law \(T\) after scaling by \(b^2\) as \(b\to\infty\). In particular the fourth-to-second normalized ratio tends respectively to \(1\), \(9/5\), and \(21/5\).

## Verification
The accompanying standalone `verify.py` uses symbolic beta-polynomial identities and checks the exact quartic cumulant cancellation, then performs separate high-precision integrations of the stationary quantiles in both the edge-cluster and smooth regimes. The numerical tests include parameter values on either side of the unique root. Run with `python verify.py` (requires SymPy and mpmath). Numerical quadrature verifies representative instances; the proof of strict monotonicity for all parameters and orders is the analytic covariance argument above.

## Relationship to prior work
Touzo and Le Doussal, arXiv:2308.06118v1 (2023), derive the large-population stationary rank-field solution, the discontinuous edge clusters, the morphological boundaries \(b=1/2,1\), and an integral formula for moments of arbitrary order (supplement equations (160)–(164)); in particular, their second-moment expression agrees with \(M_2(t)\) above. Those facts are the input, and the stationary law itself is **not** new. The claim established here is the **global strict ordering of all standardized even moments across the two noncollapsed phases**, together with the resulting exact unique kurtosis sign boundary, neither of which is stated by that moment-integral representation. The later paper of Touzo and Le Doussal, arXiv:2502.09466v1 (2025), focuses on harmonic confinement and nonreciprocal interactions; its additional phase diagrams do not state this result for the original unconfined attractive model. General star/likelihood-ratio comparison principles are classical; originality is not asserted for that abstract comparison technique.

## Limitations
This is a theorem about a previously derived deterministic large-population stationary measure, not a proof that a finite interacting stochastic system has the same normalized moment ratios, nor a uniform convergence theorem in simultaneous large-population/large-speed limits. At \(b\le1/2\), the stationary limit is a single atom and standardized moments are undefined. The analysis does not address finite temperature, trapping forces, transient evolution, finite-population fluctuation corrections, or exact convergence rates. The new result relies on the correctness and applicability of the source's large-\(N\) stationary solution. An equivalent moment-ordering application in unindexed literature cannot be excluded by database searches alone.

## References
1. L. Touzo and P. Le Doussal, *Non-equilibrium phase transitions in active rank diffusions*, arXiv:2308.06118v1 (first posted 2023-08-11), especially equations (17), (21), and supplemental equations (160)–(164). https://arxiv.org/html/2308.06118v1
2. L. Touzo and P. Le Doussal, *Run-and-tumble particles with 1D Coulomb interaction: the active jellium model and the non-reciprocal self-gravitating gas*, arXiv:2502.09466v1 (first posted 2025-02-13). https://arxiv.org/abs/2502.09466
