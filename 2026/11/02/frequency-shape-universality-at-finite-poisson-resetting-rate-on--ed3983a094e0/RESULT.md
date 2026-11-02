# Frequency-shape universality at finite Poisson resetting rate on connected oscillator networks

## Finding
Consider an undirected connected weighted graph with at least two vertices, a designated vertex \(r\), graph Laplacian \(L\), coupling \(\kappa>0\), reset rate \(\lambda>0\), and constant forcing vector \(\omega\in\mathbb R^n\). Between reset times, the unwrapped linear phase vector obeys \(\dot\theta=\omega-\kappa L\theta\); at the times of one rate-\(\lambda\) Poisson process, only coordinate \(r\) is replaced by zero. This exact piecewise-deterministic linear system has a unique invariant probability measure with finite second moment, and every initial law with finite second moment converges to it exponentially in quadratic Wasserstein distance.

Write \(\Omega=\sum_i\omega_i\). There is a unique vector \(z\) satisfying
\[
 z_r=0,\qquad \kappa Lz=\omega-\Omega e_r.
\]
For any two forcing vectors with the same \(\Omega\), subtracting their respective \(z\)-vectors makes the *entire path laws*, and hence the invariant laws, identical. In particular the stationary mean is
\[
 \mathbb E\theta=z+\frac{\Omega}{\lambda}\mathbf 1,
\]
so the expected difference between any two phases is independent of the finite reset rate. The stationary covariance \(C\) is independent of the shape of \(\omega\) at fixed total \(\Omega\), and is the unique symmetric solution of
\[
 \kappa(LC+CL)+\lambda(C-QCQ)=\frac{\Omega^2}{\lambda}P,
 \qquad P=e_re_r^\mathsf T,\quad Q=I-P.
\]
When \(\Omega=0\), the invariant measure is exactly \(\delta_z\), despite the random reset times.

For the two-vertex, unit-weight edge with reset vertex \(1\), this yields
\[
 \mathbb E(\theta_2-\theta_1)=\frac{\omega_2}{\kappa},\qquad
 \operatorname{Var}(\theta_2-\theta_1)
 =\frac{(\omega_1+\omega_2)^2}{\lambda(3\kappa+\lambda)}.
\]
The exact finite-rate fluctuation is therefore positive precisely when the total drive is nonzero, despite the complete insensitivity of its value to how that total is distributed between the vertices.

## Assumptions and scope
Let \(n\ge2\) be an integer. For each unordered edge \(\{i,j\}\), let \(w_{ij}=w_{ji}>0\), and set \(w_{ij}=0\) otherwise. Assume the resulting finite graph is connected. Define \(L_{ij}=-w_{ij}\) for \(i\ne j\), and \(L_{ii}=\sum_{j\ne i}w_{ij}\). Choose \(r\in\{1,\ldots,n\}\). Let \(N_t\) be a homogeneous Poisson counting process of rate \(\lambda>0\), independent of the initial condition. At each jump of \(N_t\), use the deterministic reset \(\theta\mapsto Q\theta\), leaving all non-reset coordinates unchanged. Between jumps the system follows \(\dot\theta=\omega-\kappa L\theta\). All variables are real and unwrapped. No Brownian forcing, modulo-\(2\pi\) reduction, or sine nonlinearity is included in this exact theorem.

The quadratic Wasserstein metric \(W_2\) is taken on laws with finite second moment on \(\mathbb R^n\). The result concerns a single reset vertex, a common Poisson clock, and constant \(\omega\); it does not claim the same frequency-shape reduction for two or more reset vertices or for the nonlinear Kuramoto model.

## Proof
**1. Anchored potential and exact conjugacy.** A connected undirected graph Laplacian has kernel \(\operatorname{span}\{\mathbf 1\}\), and the matrix obtained by deleting row and column \(r\) is strictly positive definite. Since \(\sum_i(\omega_i-\Omega\mathbf 1_{i=r})=0\), this gives a unique \(z\) with \(z_r=0\) and \(\kappa Lz=\omega-\Omega e_r\). Put \(u=\theta-z\). Then between jumps
\[
 \dot u=\Omega e_r-\kappa Lu.
\]
At each reset, \(u^+=Q(u^-+z)-z=Qu^-\), because \(Pz=0\). The transformed process is therefore exactly the same for all \(\omega\) having the same sum \(\Omega\), including its finite-time transition kernels under corresponding shifted initial states. By linearity, the transformed process for general \(\Omega\) is the dilation by \(\Omega\) of the one with \(\Omega=1\) (and it is identically zero at stationarity when \(\Omega=0\)).

**2. Existence, uniqueness, and convergence.** Couple two solutions using the same Poisson clock. Their difference \(d\) solves \(\dot d=-\kappa Ld\) between jumps and \(d^+=Qd^-\) at jumps. The generator applied to \(\|d\|^2\) yields
\[
 \frac{d}{dt}\mathbb E\|d(t)\|^2
 =-\mathbb E\big[d(t)^\mathsf T(2\kappa L+\lambda P)d(t)\big].
\]
The symmetric matrix \(2\kappa L+\lambda P\) is strictly positive definite: its nullspace would have to lie simultaneously in \(\ker L=\operatorname{span}\{\mathbf1\}\) and in \(\{d:d_r=0\}\), whose intersection is \(\{0\}\). Let \(c>0\) be its smallest eigenvalue. Gronwall's inequality gives \(\mathbb E\|d(t)\|^2\le e^{-ct}\|d(0)\|^2\). Optimal initial coupling then implies \(W_2(\nu P_t,\eta P_t)\le e^{-ct/2}W_2(\nu,\eta)\). The affine flow and bounded linear reset map preserve finite second moments on each bounded time interval; thus \(P_t\) maps the complete metric space of probability measures with finite second moment to itself. For any fixed \(t_0>0\), Banach's theorem supplies a unique fixed point of \(P_{t_0}\). Since every \(P_s\) commutes with \(P_{t_0}\), uniqueness forces this fixed point to be invariant under every \(P_s\). The coupling inequality gives the stated global convergence and uniqueness.

**3. Mean and covariance.** For the transformed process, stationarity of its first moment gives \(0=\Omega e_r-\kappa Lm-\lambda Pm\). Summing coordinates yields \(\lambda m_r=\Omega\), and therefore \(Lm=0\), so \(m=(\Omega/\lambda)\mathbf1\). Translating back gives the mean formula. For the centered transformed variable \(v=u-m\), its between-jump drift is \(\Omega e_r-\kappa Lv\) and its jump is \(v^+=Qv^--(\Omega/\lambda)e_r\). Since \(\mathbb Ev=0\), the second-moment stationarity equation is exactly
\[
 \kappa(LC+CL)+\lambda(C-QCQ)=\frac{\Omega^2}{\lambda}P.
\]
Uniqueness of symmetric solutions follows from strict positivity of the associated linear operator \(\mathcal A\). In the Frobenius inner product, for symmetric \(D\),
\[
 \langle D,\mathcal A(D)\rangle_F
 =2\kappa\operatorname{tr}(LD^2)
 +\lambda(\|D\|_F^2-\|QDQ\|_F^2)\ge0.
\]
If equality holds then every column of \(D\) lies in \(\ker L\), hence symmetry makes \(D=a\mathbf1\mathbf1^\mathsf T\); the reset term forces \(a=0\). The invariant covariance therefore solves a uniquely invertible finite linear system. The equation depends on the frequency vector only through \(\Omega^2\).

**4. Two-vertex evaluation.** For a single unit-weight edge, put \(L=\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\) and \(r=1\). Solving the preceding symmetric matrix equation gives
\[
 C=\frac{\Omega^2}{\lambda^2(3\kappa+\lambda)}
 \begin{pmatrix}\kappa+\lambda&\kappa\\\kappa&\kappa\end{pmatrix}.
\]
The anchored equation has \(z_1=0\), \(z_2=\omega_2/\kappa\). Taking the quadratic form of \(C\) against \((-1,1)\) proves the stated relative-phase mean and variance. Both denominators are strictly positive for all permitted parameters.

## Verification
The standalone \(\texttt{verify.py}\) uses exact rational and symbolic arithmetic to check the anchored graph-Poisson identity, frequency redistribution invariance, stationary means, positive-semidefinite covariance and second-moment operator equations for 16 rooted weighted graph examples on two to four vertices, as well as the exact symbolic two-vertex covariance. An independently generated 180,000-event Poisson pre-reset numerical diagnostic agrees with the two-vertex analytic mean and covariance within the stated tolerances. The general existence/contraction proof and invariance of all path laws are mathematical arguments, not consequences of these finite checks. Run using \(\texttt{python verify.py}\); the program requires Python, SymPy and NumPy.

## Relationship to prior work
Paramero-Arias and Riascos (arXiv:2610.21842v1, first submitted 2026-10-15) formulate stochastic subsystem resetting on finite networks, but their analytical grounded-Laplacian reduction is derived in the **infinite-resetting-rate limit**, and their finite-rate nonlinear behavior is explored numerically. The present exact finite-rate statement concerns the independently specified unwrapped linearized network process, including its whole invariant law and its graph-specific covariance; it is not a claim about the full nonlinear Kuramoto equation.

Majumder, Chattopadhyay, and Gupta (arXiv:2402.14921) treat stochastic subsystem resetting in the globally coupled nonlinear Kuramoto model using a large-population approach, while Majumder, Acharya, and Gupta (arXiv:2604.04769) develop finite-rate self-consistency for stationary order parameters of generalized mean-field Kuramoto systems. Neither result directly gives the anchored spatial translation of finite-graph path laws or the specific finite-dimensional covariance equation. Bressloff (arXiv:2411.15534) studies a different subsystem-resetting configuration in which the external medium is not reset. Established generator and contraction methods underlie the proof; novelty is claimed for the exact structural reduction in this particular network-resetting model, not for those general methods.

## Limitations
This is an exact statement for the **linear, unwrapped, single-vertex-reset** piecewise-deterministic model. For finite reset rate, rare long waiting times can invalidate a globally small-angle approximation to the nonlinear phase model; no nonlinear synchronization or global stability claim follows. Results for different reset vertices or several simultaneously reset vertices require a new analysis. Neither uniqueness of priority nor an independent mathematical audit is established. The checked preprint and related studies do not eliminate the possibility of earlier linear hybrid-system results that imply this special identity.

## References
1. K. Paramero-Arias and A. P. Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842v1 (2026), https://arxiv.org/html/2610.21842.
2. R. Majumder, R. Chattopadhyay, and S. Gupta, *Kuramoto model subject to subsystem resetting: How resetting a part of the system may synchronize the whole of it*, arXiv:2402.14921 (2024), https://arxiv.org/abs/2402.14921.
3. R. Majumder, A. Acharya, and S. Gupta, *Analytical approach to subsystem resetting in generalized Kuramoto models*, arXiv:2604.04769 (2026), https://arxiv.org/abs/2604.04769.
4. P. C. Bressloff, *Kuramoto model with stochastic resetting and coupling through an external medium*, arXiv:2411.15534 (2024), https://arxiv.org/abs/2411.15534.
5. M. Sarkar and S. Gupta, *Synchronization in the Kuramoto model in presence of stochastic resetting*, arXiv:2203.00339 (2022), https://arxiv.org/abs/2203.00339.
