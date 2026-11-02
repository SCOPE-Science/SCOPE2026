# Exact Gaussian calibration and time-average variance gap for two stochastic Runge–Kutta samplers

## Finding

Consider the two- and three-gradient overdamped stochastic Runge–Kutta samplers called SRK-I and SRK-II in Ye (2026), originally introduced by Yang and Wang (2026). On **every** symmetric positive-definite quadratic potential, they coincide pathwise under identical Brownian data. Their common scalar mode has a unique nonzero step-size resonance with the *exact* invariant Gaussian variance, yet at that very step its physical-time linear-observable sampling variance is exactly \(7/3\) times the continuous-time value. For all other positive stable steps, physical-time linear-observable sampling variance is strictly greater than the continuous-time value, even though a first-order Euler–Maruyama chain has the *exact* continuous-time coefficient for every stable step.

Precisely, if \(H\in\mathbb R^{d\times d}\) is symmetric positive definite with eigenvalues \(\lambda_i>0\), the schemes are stable exactly for \(0<h\lambda_i<2\) for every \(i\). Their invariant covariance agrees with \(H^{-1}\) precisely when \(H=(4/(3h))I\). In any stable mode \(x=h\lambda\), the relative physical-time asymptotic time-average variance of a linear observable is
\[
1+\frac{x^2}{3(2-x)^2}>1.
\]

## Assumptions and scope

Fix integer \(d\geq1\), real symmetric positive-definite \(H\), and positive step \(h\). Let \(U(z)=\frac12 z^\top Hz\), and let the target Langevin diffusion satisfy \(dX_t=-HX_t\,dt+\sqrt2\,dB_t\), with target distribution \(\mathcal N(0,H^{-1})\). Let \(\Delta B_k=B_{(k+1)h}-B_{kh}\) and \(J_k=\int_{kh}^{(k+1)h}(B_s-B_{kh})\,ds\); successive pairs are independent, and within each pair
\[
\operatorname{Cov}(\Delta B_k)=hI,\quad
\operatorname{Cov}(J_k)=h^3I/3,\quad
\operatorname{Cov}(\Delta B_k,J_k)=h^2I/2.
\]

Define **SRK-I** by stage \(A=z-\frac{3h}{4}Hz+\frac{3\sqrt2}{2h}J\) and update \(z'=z-\frac h3Hz-\frac{2h}3HA+\sqrt2\Delta B\). Define **SRK-II** by stages \(A_\pm=z-\frac h2Hz+\frac{\sqrt2}{h}(1\pm1/\sqrt2)J\) and update \(z'=z-\frac h2 H(A_++A_-)+\sqrt2\Delta B\). Compare their stationary time averages \(N^{-1}\sum_{k=0}^{N-1}w^\top Z_k\) for deterministic nonzero \(w\). The time-average variance is multiplied by elapsed physical time \(Nh\); this is **not** a comparison at equal gradient-evaluation cost, and it uses a stationary initial chain.

## Proof

**Step 1: exact common recursion.** Substitute the linear gradient into SRK-I and use \(\frac13+\frac23=1\), \(\frac23\cdot\frac34=\frac12\), and \(\frac23\cdot\frac{3}{2}=1\). In SRK-II, average \(A_+\) and \(A_-\); the coefficients \(1\pm1/\sqrt2\) sum to \(2\). Both methods therefore give, pathwise and in all dimensions,
\[
Z_{k+1}=P(hH)Z_k+\sqrt2\bigl(\Delta B_k-HJ_k\bigr),
\qquad P(x)=1-x+\frac{x^2}{2}.
\]
The innovation is Gaussian with covariance \(2h\,q(hH)\), where \(q(x)=1-x+x^2/3>0\), because the covariance of \(\Delta B-HJ\) is \(hI-h^2H+h^3H^2/3\). Equivalently the innovation can be generated using independent standard Gaussian vectors \(G,K\) as \(\sqrt{2h}[(I-hH/2)G-hHK/\sqrt{12}]\). All matrices here commute because they are polynomials in \(H\).

**Step 2: stability and invariant measure.** Diagonalize \(H\) orthogonally. Each coordinate has AR(1) multiplier \(p=P(x)=1-x+x^2/2\) and innovation variance \(2h q(x)\). For \(x>0\), \(|p|<1\) if and only if \(0<x<2\); indeed \(p\geq1/2\), \(p<1\) exactly on that interval. Since every innovation variance is positive, a finite invariant second moment exists exactly when every eigenvalue lies in this interval. In that case the stationary law is uniquely \(\mathcal N(0,\Sigma_h)\), with diagonal modal variance
\[
v(\lambda,h)=\frac{2h q(x)}{1-P(x)^2},\qquad x=h\lambda.
\]
A direct expansion supplies the exact *sign certificate*
\[
2xq(x)-[1-P(x)^2]=\frac{x^3(3x-4)}{12}.
\]
Since \(1-P(x)^2>0\) in the stable interval, the ratio of invariant variance to target variance \(1/\lambda\) is below one for \(0<x<4/3\), equals one exactly at \(x=4/3\), and exceeds one for \(4/3<x<2\). Simultaneous equality in every mode requires \(h\lambda_i=4/3\) for all \(i\), equivalently \(H=(4/(3h))I\). Thus no anisotropic \(H\) can have exact invariant covariance under a single common positive stable step.

**Step 3: time-average variance.** In stationarity, the lag-\(j\) modal covariance is \(v p^j\) for \(j\geq0\). For a scalar coordinate, multiplying the variance of the empirical mean by \(Nh\) and taking \(N\to\infty\), absolute summability gives
\[
\lim_{N\to\infty}Nh\operatorname{Var}\left(\frac1N\sum_{k=0}^{N-1}Z_k\right)
=h\,v\frac{1+p}{1-p}
=\frac{2h^2q(x)}{[1-P(x)]^2}
=\frac{2}{\lambda^2}\frac{q(x)}{(1-x/2)^2}.
\]
The last factor equals
\[
\frac{q(x)}{(1-x/2)^2}=1+\frac{x^2}{3(2-x)^2}.
\]
Writing \(H=V\operatorname{diag}(\lambda_i)V^\top\) and \(\alpha_i=(V^\top w)_i\), the independent modes thus yield
\[
\lim_{N\to\infty}Nh\operatorname{Var}\!\left(\frac1N\sum_{k=0}^{N-1}w^\top Z_k\right)
=2\sum_{i=1}^d\frac{\alpha_i^2}{\lambda_i^2}
\left[1+\frac{(h\lambda_i)^2}{3(2-h\lambda_i)^2}\right].
\]
For the continuous-time stationary Ornstein–Uhlenbeck process, integration of covariance \(\alpha_i^2e^{-\lambda_i t}/\lambda_i\) shows the corresponding physical-time coefficient is exactly \(2\sum_i\alpha_i^2/\lambda_i^2\); the difference is strictly positive for nonzero \(w\) and every positive stable \(h\).

**Step 4: sharp resonance and Euler comparison.** At \(x=4/3\), \(P(x)=5/9\), the invariant Gaussian matches the target, but \(q(x)/(1-x/2)^2=7/3\). For Euler–Maruyama on the same quadratic, one step is \(z'=(I-hH)z+\sqrt2\Delta B\). For any stable Euler mode \(0<x<2\), its stationary variance is \(2h/[1-(1-x)^2]\) (not the target variance except in the zero-step limit), whereas its physical-time time-average coefficient is \(h\cdot2h/[1-(1-x)]^2=2/\lambda^2\). This comparison concerns **linear** observables and equal physical-time horizon only.

## Verification

Run the standalone file `verify.py` with Python 3; it uses only the standard library. It checks exact rational polynomial/factorization identities, stable-boundary values, the resonance, a grid of scalar Brownian-driven pathwise scheme equalities, innovation covariance polynomials, and finite-versus-infinite covariance-sum consistency. A passing run reported **11052 checks**. Numerical tests are supplementary: the proof of all-domain stability, exact calibration, strict variance inflation, and uniqueness is given in the algebra and covariance identities above.

## Relationship to prior work

Yang and Wang (2026), originally posted May 8, specify the two- and three-gradient Langevin schemes and prove general convergence bounds; Ye (2026), posted September 10, gives their paired Brownian data and establishes general nonasymptotic mean-square time-average bounds. Both source manuscripts were inspected at the schemes and their convergence and numerical-evaluation sections. The finding here instead characterizes the **exact** Gaussian stationary covariance, the **complete** modewise variance-sign transition, the exact **physical-time** linear time-average variance, and the finite-step invariant-accurate resonance. It does not claim the general AR(1) variance formulas, Gaussian target, or Euler’s scalar variance identity as individually new; their particular combination for these two schemes provides an explicit structural benchmark beyond an order bound. An earlier three-gradient SRK-LD scheme (Li et al., 2019) is different, and the underdamped UBU-type samplers and their Gaussian covariance analyses concern other transition kernels. Broader specialist coverage of harmonic stochastic Runge–Kutta methods remains a priority uncertainty.

## Limitations

The analysis is limited to real SPD quadratic potentials, the stated Brownian-path pair sampled **jointly** with exact Gaussian covariance, fixed positive step sizes, stationary-chain variance, and linear test functions. The equal-time comparison does not account for the schemes’ different gradient-evaluation costs. There is no general claim for nonlinear potentials, nonconstant steps, higher-order observables, or ergodic variance of a nonstationary finite chain. The special resonance is a finite-step scalar/homogeneous-spectrum fact and does not imply superior overall numerical accuracy.

## References

1. Yang and Wang (2026), *Accelerating Langevin Monte Carlo via Efficient Stochastic Runge–Kutta Methods beyond Log-Concavity*, arXiv:2605.07939v1, https://arxiv.org/html/2605.07939v1, §2.2 and §3–4 (first public May 8, 2026).
2. Ye (2026), *Mean Square Error Analysis of Stochastic Runge–Kutta Integrators*, arXiv:2609.11528v1, https://arxiv.org/abs/2609.11528, §2.2, §4–5 (first public September 10, 2026).
3. Li and collaborators (2019), *Stochastic Runge–Kutta Accelerates Langevin Monte Carlo and Beyond*, arXiv:1906.07868, https://arxiv.org/abs/1906.07868 (different earlier Langevin SRK scheme).
