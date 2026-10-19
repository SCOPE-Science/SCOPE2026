# Universal Poisson-reset crossover in chiral-colloid excess dispersion

## Finding
Consider a passive planar Brownian colloid with nonzero hydrodynamic translation–rotation coupling. Its orientation is reset to a common direction at the events of a Poisson clock of rate \(r>0\), without resetting position. Write \(\delta>0\) for its rotational diffusivity, \(b\ne0\) for its orientation-release displacement vector, and \(\Sigma\) for its long-time positional covariance **rate** (rather than the conventional half-rate diffusion tensor). Subtract the independently identifiable thermal Schur-complement contribution \(\Sigma_{\mathrm{th}}\), and write \(\Gamma=\Sigma-\Sigma_{\mathrm{th}}\).

**Theorem.** The two eigenaxes of \(\Gamma\) are the drift direction \(e_\parallel=b/|b|\) and its perpendicular \(e_\perp=Je_\parallel\). With \(k=r/\delta\), their eigenvalues satisfy the exact sign law
\[
\boxed{\quad e_\perp^{\mathsf T}\Gamma e_\perp-e_\parallel^{\mathsf T}\Gamma e_\parallel
=\frac{2r|b|^2(k^3+k^2+k-2)}{(k+1)^3(k+4)}.\quad}
\]
The polynomial has one positive root, \(k_*=0.8105357137661368\ldots\). Below \(k_*\), the longitudinal excess variance rate is greater; above \(k_*\), the transverse excess rate is greater. Equality occurs only at \(r=k_*\delta\). The threshold is independent of the remaining entries of the positive-definite mobility matrix, the magnitude of the coupling, and the thermal energy. For deterministic orientation-reset intervals, in contrast, the transverse excess always exceeds the longitudinal excess. Thus randomness of reset times changes the ordering of the two fluctuation modes, not just their magnitudes.

An exact closed expression for the full covariance rate is given in the proof. These are long-time fluctuation statements, not claims about finite-time Gaussian distributions, net force, or finite-speed resetting mechanisms.

## Assumptions and scope
Let \(\Theta=k_{\mathrm B}T>0\) be thermal energy. Let the constant body-frame mobility be a real symmetric strictly positive-definite \(3\times3\) matrix
\[
M=\begin{pmatrix}A&u\\u^{\mathsf T}&c\end{pmatrix},
\qquad A=A^{\mathsf T}\in\mathbb R^{2\times2},\quad u\in\mathbb R^2\setminus\{0\},\quad c>0.
\]
Set \(C=A-uu^{\mathsf T}/c\succ0\), \(\delta=\Theta c\), \(b=Ju/c\), \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), and \(R(\phi)=e^{\phi J}\). Between resets, \((X_t,\phi_t)\in\mathbb R^2\times\mathbb R\) solves the **Stratonovich** equation
\[
d\begin{pmatrix}X\\\phi\end{pmatrix}
=\sqrt{2\Theta}\begin{pmatrix}R(\phi)&0\\0&1\end{pmatrix}
M^{1/2}\circ dW_t,
\]
where \(W\) is standard three-dimensional Brownian motion. At the times of a Poisson process of independent rate \(r>0\), set \(\phi\mapsto0\), leaving \(X\) continuous. Start with \(X_0=0\), \(\phi_0=0\); the asymptotic rates do not depend on a finite initial displacement.

The long-time drift and covariance rate are
\[
v=\lim_{t\to\infty}t^{-1}\mathbb E X_t,\qquad
\Sigma=\lim_{t\to\infty}t^{-1}\operatorname{Cov}(X_t).
\]
Both limits exist. Define the thermal covariance-rate baseline
\[
\Sigma_{\mathrm{th}}=\Theta\operatorname{tr}(C)I_2+
\frac{2\Theta r}{r+4\delta}
\left(C-\frac{\operatorname{tr}(C)}2I_2\right).
\]
It is the covariance rate of the translation noise conditionally independent of angular Brownian motion. In particular, it includes the usual orientationally averaged anisotropic translational mobility; it is **not** the covariance rate of the entire coupled colloid.

## Proof
**1. Exact separation of coupled and independent noise.** The Schur-complement identity gives an equivalent representation with independent planar Brownian motion \(B\) and scalar Brownian motion \(W_0\):
\[
\begin{split}
d\phi_t&=\sqrt{2\Theta c}\,dW_{0,t},\\
dX_t&=\Theta JR(\phi_t)u\,dt+
\sqrt{2\Theta}R(\phi_t)\left(\frac{u}{\sqrt c}\,dW_{0,t}+C^{1/2}dB_t\right).
\end{split}
\]
The displayed positional drift is the Stratonovich-to-Itô correction; ignoring it changes the physical model. For \(F(\phi)=-JR(\phi)u/c\), Itô's formula gives
\[
dF(\phi_t)=\Theta JR(\phi_t)u\,dt+
\sqrt{2\Theta}R(\phi_t)u/\sqrt c\,dW_{0,t}.
\]
Consequently, **on every interval without resets**,
\[
X_t-X_0=(I_2-R(\phi_t))b+
\sqrt{2\Theta}\int_0^tR(\phi_s)C^{1/2}dB_s,
\qquad \phi_s=\sqrt{2\delta}\,W_{0,s}.
\tag{1}
\]
The second term is centered conditional on the entire angular path and has conditional covariance \(2\Theta\int_0^tR(\phi_s)CR(\phi_s)^{\mathsf T}ds\). Thus it has zero covariance with the first term and with any reset waiting time independent of \(B,W_0\).

**2. Deterministic cycle statistics.** Brownian angular Fourier modes yield \(\mathbb E e^{im\phi_t}=e^{-m^2\delta t}\). Applying this to (1), and writing \(C_0=C-\tfrac12\operatorname{tr}(C)I_2\), gives
\[
\begin{split}
m(t)&=\mathbb E(X_t-X_0)=(1-e^{-\delta t})b,\\
\operatorname{Cov}(X_t-X_0)
&=2\Theta\left(\frac{t\operatorname{tr}(C)}2I_2+
\frac{1-e^{-4\delta t}}{4\delta}C_0\right)\\
&\quad+\frac{|b|^2}2(1-e^{-4\delta t})I_2+
(e^{-4\delta t}-e^{-2\delta t})bb^{\mathsf T}.
\end{split}
\tag{2}
\]
Indeed \(\mathbb E\cos\phi_t=e^{-\delta t}\), \(\mathbb E\cos2\phi_t=e^{-4\delta t}\), and the off-diagonal angular endpoint covariance vanishes by reflection symmetry.

**3. Renewal-reward covariance.** The reset clock partitions the process into independent cycles with waiting time \(L>0\) and displacement \(Y\). Let \(\mu=\mathbb EL\), assume \(\mathbb E L^3<\infty\), and put \(a_j=\mathbb E e^{-j\delta L}\). For such cycle laws, the renewal-reward law and covariance theorem (or a centered cycle-martingale argument with the incomplete-cycle remainder controlled by the third moment) give
\[
v=\frac{\mathbb EY}{\mu}=\frac{1-a_1}{\mu}b,
\qquad
\Sigma=\frac1\mu\mathbb E[(Y-vL)(Y-vL)^{\mathsf T}].
\tag{3}
\]
These formulas also hold for deterministic \(L\) (directly by independent increments). Write \(h=(1-a_1)/\mu\) and
\[
z_L^2=\mathbb E\bigl[(1-e^{-\delta L}-hL)^2\bigr].
\]
Here the bracket has mean zero. Conditioning on \(L\), inserting (2), and using the conditional independence of the residual translational martingale proves
\[
\begin{split}
\Sigma_{\mathrm{th}}&=\Theta\operatorname{tr}(C)I_2+
\frac{\Theta(1-a_4)}{2\delta\mu}C_0,\\
\Gamma&=\Sigma-\Sigma_{\mathrm{th}}
=\frac1\mu\left[\frac{|b|^2}2(1-a_4)I_2+
(a_4-a_2+z_L^2)bb^{\mathsf T}\right].
\end{split}
\tag{4}
\]
Equation (4) is a useful exact general renewal identity; the new classification below concerns the specified Poisson protocol.

**4. Poisson computation and unique crossover.** Set \(L\sim\operatorname{Exp}(r)\) and \(k=r/\delta\). Then \(\mu=1/r\), \(a_j=k/(k+j)\), \(h=r/(k+1)\), \(\mathbb EL^2=2/r^2\), and \(\mathbb E[Le^{-\delta L}]=r/(r+\delta)^2\). A direct expansion of the square in \(z_L^2\) therefore yields
\[
\boxed{z_L^2=\frac{2}{(k+1)^3(k+2)}.}
\tag{5}
\]
The exact drift and full covariance rate are
\[
\boxed{v=\frac{r}{k+1}b,}
\qquad
\boxed{\begin{split}
\Sigma&=\Theta\operatorname{tr}(C)I_2+
\frac{2\Theta r}{r+4\delta}C_0\\
&\quad+\frac{2r|b|^2}{k+4}I_2+
 r\left[\frac{k}{k+4}-\frac{k}{k+2}+
 \frac{2}{(k+1)^3(k+2)}\right]bb^{\mathsf T}.
\end{split}}
\tag{6}
\]
Since \(\Gamma\) is a scalar matrix plus a multiple of \(bb^{\mathsf T}\), its transverse-minus-longitudinal eigenvalue difference is
\[
\frac{|b|^2}{\mu}(a_2-a_4-z_L^2)
=\frac{2r|b|^2(k^3+k^2+k-2)}{(k+1)^3(k+4)}.
\tag{7}
\]
The polynomial \(p(k)=k^3+k^2+k-2\) satisfies \(p(0)=-2\), tends to positive infinity, and has strictly positive derivative \(p'(k)=3k^2+2k+1\) for \(k>0\). Hence there is precisely one positive root and the sign classification follows. Strictness needs \(u\ne0\) (equivalently \(b\ne0\)); otherwise all excess fluctuations vanish.

**5. Deterministic comparison.** For \(L\equiv\tau>0\), \(z_L^2=0\) and \(a_j=e^{-j\delta\tau}\). Formula (4) gives
\[
e_\perp^{\mathsf T}\Gamma e_\perp-
 e_\parallel^{\mathsf T}\Gamma e_\parallel
=\frac{|b|^2}{\tau}(e^{-2\delta\tau}-e^{-4\delta\tau})>0.
\]
Thus the Poisson long-interval regime has the opposite sign from every deterministic interval, which cannot be established simply by matching the mean reset time.

## Verification
The standalone `verify.py` establishes symbolically both (5) and the factorization (7), computes the unique real positive root, and compares the exact contrast with Monte Carlo samples of independent Poisson-duration displacement cycles. In the isotropic-Schur-complement specialization, the residual translational displacement at a given duration is exactly Gaussian with covariance \(2\Theta C L\), independently of the angular endpoint, so this simulation samples the cycle law without time discretization. Tested values of \(k\) are \(0.3,0.6,0.81,1.1,2,5\). All six signed differences agreed with the closed expression within five estimated Monte Carlo standard errors. The test checks finite-sample numerics; the infinite-time theorem is established by steps 1–5, not by simulation.

## Relationship to prior work
Cleuren and Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1 (first posted 2026-03-19), formulate the coupled positive-definite body-frame mobility, Stratonovich dynamics, and **periodic** orientation-only resetting, and derive the resulting **mean** sorting velocity (especially their equations 4–8). They suggest diffusion control and random-reset protocols but do not derive (6)–(7).

Chaki, Olsen and Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v2 (first posted 2024-06-25), compute the long-time diffusion tensor for **Poisson** orientation resets with independent rotational and translational noises in the body frame, meaning \(u=0\) in the current model. Their diffusion tensor agrees with the thermal term \(\Sigma_{\mathrm{th}}\) up to their diffusion-rate convention; it does not imply the coupling-generated \(\Gamma\) or its sign reversal for \(u\ne0\).

A previous fixed-period endpoint-displacement calculation for the coupled colloid is recorded under opaque identifier `5398fb95-45c2-4296-a3d5-00ccdae40c85`. Its cycle law for an isotropic Schur complement gives the deterministic comparison in step 5, but it neither assumes Poisson random cycle lengths nor gives renewal-time-induced longitudinal fluctuations, the universal cubic threshold, or the general-mobility covariance formula.

General renewal-reward covariance theory underlies (3) and is not itself claimed as new. The new result is the explicitly computed coupling-induced variance-mode reversal under stochastic rather than regular reorientation in this physical model.

## Limitations
The statement assumes free overdamped planar diffusion, constant body-frame mobility, instantaneous orientation-only resetting to a fixed angle, independent Poisson reset times, and no interactions, boundaries, flow, or external forces. The threshold applies to the **excess** covariance \(\Gamma\); the eigenvectors of the full measured covariance \(\Sigma\) need not align with \(b\) when \(C\) is anisotropic. If \(C\) is isotropic, the same sign crossover holds for the total covariance rate. The third-moment assumption in the supporting general renewal formula is sufficient, not claimed sharp.

## References
1. B. Cleuren and R. Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1, https://arxiv.org/html/2603.19430v1 (first publicly posted 2026-03-19).
2. S. Chaki, K. S. Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v2, https://arxiv.org/html/2406.17550v2 (first publicly posted 2024-06-25).
3. P. P. Ghosh et al., *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149v2, https://arxiv.org/html/2501.05149v2 (related active-particle orientation-reset model, not the hydrodynamically cross-coupled passive colloid).
4. Previous fixed-period one-cycle result, opaque identifier `5398fb95-45c2-4296-a3d5-00ccdae40c85` (scope restricted to fixed resetting intervals).
