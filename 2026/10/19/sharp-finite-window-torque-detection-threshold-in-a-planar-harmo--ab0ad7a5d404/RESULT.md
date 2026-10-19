# Sharp finite-window torque detection threshold in a planar harmonic Brownian gyrator

## Finding

**Theorem (drift-torque fluctuation and sharp bath-optimized observation window).** Let \(A,D\) be real symmetric positive-definite \(2\times2\) matrices. Let \(A\) have distinct eigenvalues \(\lambda_1,\lambda_2>0\), and let \(X_t\) be the unique stationary solution of
\[
dX_t=-AX_t\,dt+\sqrt{2D}\,dW_t.
\]
The physical observable in this theorem is the **deterministic force torque**, not the noisy instantaneous angular velocity or stochastic angular momentum:
\[
\tau_t=X_{1,t}(-AX_t)_2-X_{2,t}(-AX_t)_1,
\qquad
\bar\tau_T=\frac1T\int_0^T\tau_t\,dt \quad (T>0).
\]
Write \(k=\lambda_1+\lambda_2\), \(\alpha=2\sqrt{\lambda_1\lambda_2}/k\) and \(z=kT\). Then:

1. For all real \(t\), the stationary covariance is exactly
\[
\operatorname{Cov}(\tau_0,\tau_t)=\operatorname{Var}(\tau_0)e^{-k|t|},
\qquad
\operatorname{Var}(\bar\tau_T)=\operatorname{Var}(\tau_0)F(z),
\quad F(z)=\frac{2(z-1+e^{-z})}{z^2}.
\]
2. With \(\mathrm{SNR}^2(T,D)=|\mathbb E\bar\tau_T|^2/\operatorname{Var}(\bar\tau_T)\), the **sharp, nonattained** supremum over every positive-definite diffusion matrix is
\[
\sup_{D\succ0}\mathrm{SNR}^2(T,D)
=\frac{\alpha^2}{1+\alpha^2}\frac{z^2}{2(z-1+e^{-z})}.
\]
3. There is a unique \(z_c(\alpha)>0\) characterized by
\[
\frac{2(z_c-1+e^{-z_c})}{z_c^2}=\frac{\alpha^2}{1+\alpha^2}.
\]
For fixed \(A,T\), a strictly positive-definite \(D\) exists with \(\mathrm{SNR}(T,D)>1\) **if and only if** \(z>z_c(\alpha)\). At the equality boundary, every permitted \(D\) has \(\mathrm{SNR}(T,D)<1\). Moreover \(z_c(\alpha)\sim2/\alpha^2\) when \(\alpha\downarrow0\).

The normalized covariance is a single exponential although the coordinates have two distinct relaxation eigenvalues. The optimized signal-to-noise threshold captures an independent, nontrivial spectral penalty as one eigenmode becomes soft.

## Assumptions and scope

The process is initialized in its stationary centered Gaussian distribution, with independent two-dimensional standard Brownian increments and constant diffusion \(D\succ0\). The matrix \(A=A^{\mathsf T}\succ0\) has distinct eigenvalues. The ratio uses the **variance of the deterministic drift torque**; the formal white-noise derivative in instantaneous angular momentum is deliberately excluded. There is no inertial dynamics, time-dependent forcing or filtering of the stochastic angular-velocity noise. The supremum varies \(D\) while keeping \(A\) and the observation duration fixed, and its optimizing limit can be singular even though every admissible matrix is strictly positive definite.

## Proof

**Step 1: Exact stationary covariance.** Choose an orientation-preserving orthogonal \(U\) with \(U^{\mathsf T}AU=\operatorname{diag}(\lambda_1,\lambda_2)\) and define \(Z=U^{\mathsf T}X\), \(\widetilde D=U^{\mathsf T}DU\), \(\delta=\lambda_1-\lambda_2\). Orientation preservation makes \(\tau_t=\delta Z_{1,t}Z_{2,t}\). The stationary Lyapunov equation gives
\[
S_{11}=v_1=\frac{\widetilde D_{11}}{\lambda_1},\qquad
S_{22}=v_2=\frac{\widetilde D_{22}}{\lambda_2},\qquad
S_{12}=c=\frac{2\widetilde D_{12}}{\lambda_1+\lambda_2}.
\]
Since \(D\succ0\), the stationary covariance \(S\succ0\), so \(v_1v_2>c^2\). Wick's rule immediately gives
\[
\mu=\mathbb E\tau=\delta c,\qquad
\sigma^2=\operatorname{Var}\tau=\delta^2(v_1v_2+c^2)>0.
\]

**Step 2: Universal memory clock.** For \(t\ge0\), the two-time cross covariance is
\(\mathbb E[Z_i(0)Z_j(t)]=S_{ij}e^{-\lambda_jt}\). Pair the four centered Gaussian factors in
\(\operatorname{Cov}(Z_1(0)Z_2(0),Z_1(t)Z_2(t))\). The disconnected pair cancels. The two remaining pairs each contribute a factor \(e^{-kt}\), giving
\[
\operatorname{Cov}(\tau_0,\tau_t)=\delta^2(v_1v_2+c^2)e^{-kt}.
\]
Stationarity makes the covariance even for this real scalar observable. Integrating over the square \([0,T]^2\) proves
\[
\operatorname{Var}(\bar\tau_T)=\frac{2\sigma^2}{T^2}\int_0^T(T-t)e^{-kt}dt
=\sigma^2\frac{2(z-1+e^{-z})}{z^2}.
\]
For reference, the two-sided power spectral density of the centered torque is the Lorentzian \(2k\sigma^2/(k^2+\omega^2)\); this is a Fourier transform of the proved covariance.

**Step 3: Sharpness over the bath covariance.** Positive definiteness of \(\widetilde D\) implies
\(\widetilde D_{12}^2<\widetilde D_{11}\widetilde D_{22}\), so
\[
\frac{c^2}{v_1v_2}<\frac{4\lambda_1\lambda_2}{(\lambda_1+\lambda_2)^2}=\alpha^2.
\]
The function \(s\mapsto s/(1+s)\) is strictly increasing on \([0,\infty)\); therefore
\[
\frac{\mu^2}{\sigma^2}=\frac{c^2}{v_1v_2+c^2}<\frac{\alpha^2}{1+\alpha^2}.
\]
The strict bound is sharp: in the eigenbasis take \(\widetilde D_{11}=d_1>0\), \(\widetilde D_{22}=d_2>0\), \(\widetilde D_{12}=(1-\varepsilon)\sqrt{d_1d_2}\), with \(0<\varepsilon<1\), and let \(\varepsilon\downarrow0\). Each matrix is positive definite and the bound is approached. Since \(\mathbb E\bar\tau_T=\mu\), division by \(F(z)>0\) gives the exact nonattained time-window supremum.

**Step 4: A sharp observation-time boundary.** One has the positive integral representation
\[
F(z)=2\int_0^1(1-s)e^{-zs}\,ds.
\]
Hence \(F\) is strictly decreasing on \((0,\infty)\), with limits \(F(0+)=1\) and \(F(\infty)=0\). Since \(0<\alpha<1\), the equation \(F(z_c)=\alpha^2/(1+\alpha^2)\) has a unique positive root. Below or at the root the strict bound proves every \(\mathrm{SNR}<1\); above it the sharpness family from Step 3 has \(\mathrm{SNR}>1\) for sufficiently small positive \(\varepsilon\). Finally \(F(z)\sim2/z\) at infinity; taking \(\alpha\downarrow0\) yields \(z_c\sim2/\alpha^2\).

**Classical two-bath specialization.** Set
\[
A=\begin{pmatrix}1&-u\\-u&1\end{pmatrix},\qquad
D=\operatorname{diag}(T_x,T_y),\qquad
0<|u|<1,\quad T_x,T_y>0.
\]
Then \(\tau=u(X^2-Y^2)\), \(\lambda_{1,2}=1\mp u\), \(k=2\), \(\alpha^2=1-u^2\). Directly from the stationary covariance,
\[
\mu=u(T_x-T_y),\qquad
\sigma^2=u^2\left[\frac{(T_x+T_y)^2}{1-u^2}+(T_x-T_y)^2\right].
\]
Consequently \(\operatorname{Corr}(\tau_0,\tau_t)=e^{-2|t|}\) and
\[
\sup_{T_x,T_y>0}\frac{|\mathbb E\bar\tau_T|^2}{\operatorname{Var}(\bar\tau_T)}
=\frac{1-u^2}{2-u^2}\frac{(2T)^2}{2(2T-1+e^{-2T})}.
\]
The supremum is approached when one of the two bath temperatures tends to zero relative to the other. The least observation time at which *some strictly positive bath pair* yields \(\mathrm{SNR}>1\) is a strict threshold \(T>z_c(\sqrt{1-u^2})/2\). In particular,
\[
T_c\sim\frac1{1-u^2}\quad\text{as }|u|\uparrow1,
\]
even though the normalized deterministic torque autocovariance always decays at rate \(2\).

## Verification

The standalone file `verify.py` (Python 3, NumPy, SciPy) runs **455 deterministic assertions**. It computes stationary covariance matrices directly in Cartesian coordinates by an independent Lyapunov solver, compares fourth-order matrix-trace formulas against the diagonal-mode identities, checks the entire time-lag covariance against matrix exponentials, independently integrates the time-window variance, tests the two-temperature specialization, checks the product-normal moment integrals, examines sharpness sequences, and independently brackets the unit-SNR time threshold. Execute `python verify.py` after installing the packages named in `requirements.txt`. Finite numeric tests only corroborate: the all-time, all-positive-definite-matrix theorem is proved above analytically.

## Relationship to prior work

The Brownian gyrator's model and its nonzero **mean torque** are established; Viot et al. evaluate PDFs of *stochastic* time-discretized angular momentum and angular velocity, which have different fluctuations from the deterministic force torque studied here [1]. Cerasoli et al. supply two-time **coordinate** covariance formulas and spectral densities [2]. Those formulas, combined with the classical Gaussian Wick rule, already imply that force-torque covariances can in principle be calculated; no novelty is claimed for Wick's theorem or the underlying OU covariance. Du Buisson and Touchette give general quadratic-observable large-deviation machinery and asymptotic variance formulas [3]; the long-window variance coefficient is an implied specialization, not claimed as an independently novel theorem. Movilla Miangolarra et al. motivate mechanical time averaging by a flywheel but study a distinct coupled engine [4]. The assessed result is the explicit **sharp positive-definite-bath supremum at every finite window**, the complete necessary-and-sufficient unit-SNR time boundary, and its soft-mode divergence, tied to a single-mode exact torque covariance. We did not identify this composite optimized statement in the inspected sources; equivalently specialized prior results remain possible.

## Limitations

The diffusion must be stationary, Gaussian, overdamped, two-dimensional, and have symmetric positive-definite drift and noise matrices; nonnormal drift is not covered. The torque is the deterministic drift contribution only and is not a physical claim about instantaneous noisy angular momentum or engine work output. The sharp boundary optimizes over freely variable positive-definite diffusion matrices: it does not guarantee that an experimentally constrained pair of baths attains near-optimal noise. Equality of the SNR supremum is excluded by positive definiteness. These formulas do not establish finite-sample confidence intervals or the distribution of the time average.

## References

[1] P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (first public 2023-07-11), https://arxiv.org/abs/2307.05248.

[2] S. Cerasoli, S. Ciliberto, E. Marinari, G. Oshanin, L. Peliti, L. Rondoni, *Spectral fingerprints of non-equilibrium dynamics: The case of a Brownian gyrator*, arXiv:2201.04903, https://arxiv.org/abs/2201.04903.

[3] J. du Buisson and H. Touchette, *Dynamical large deviations of linear diffusions*, arXiv:2212.12022, Section III.2 (quadratic observables), https://arxiv.org/abs/2212.12022.

[4] O. Movilla Miangolarra, A. Taghvaei, R. Fu, Y. Chen, T. T. Georgiou, *Thermodynamic engine powered by anisotropic fluctuations*, arXiv:2203.07573, https://arxiv.org/abs/2203.07573.
