# Random affine Laplace profiles and a sharp kurtosis trough in slowly reset harmonic chains

## Finding
For every fixed integer \(n\ge2\), the stationary position vector of a damped, nearest-neighbour harmonic chain driven by two **independently Poisson-reset Brownian boundary walls** has a universal low-reset-rate limit. Let \(\varepsilon\downarrow0\), with wall reset rates \(\varepsilon\lambda_L\) and \(\varepsilon\lambda_R\), and put \(\eta_\sigma=D_\sigma/\lambda_\sigma>0\). For \(1\le i\le n\), define
\[
a_i=\frac{n+1-i}{n+1},\qquad b_i=\frac{i}{n+1}.
\]
The stationary vector obeys, in distribution with convergence of every joint moment of total degree at most four,
\[
\sqrt\varepsilon\,(x_1,\ldots,x_n)\ \Longrightarrow\ (a_1L_L+b_1L_R,\ldots,a_nL_L+b_nL_R),
\]
where \(L_L,L_R\) are independent centered Laplace variables with \(\mathbb E e^{itL_\sigma}=(1+\eta_\sigma t^2)^{-1}\). Equivalently the limiting joint characteristic function is
\[
\Phi(t_1,\ldots,t_n)=\frac{1}{\left[1+\eta_L(\sum_i a_it_i)^2\right]\left[1+\eta_R(\sum_i b_it_i)^2\right]}.
\]
Thus an \(n\)-dimensional stationary displacement field collapses, under this specified order of limits, onto a random **affine** profile governed by only two Laplace amplitudes. Its limiting covariance matrix
\[
\lim_{\varepsilon\downarrow0}\varepsilon\operatorname{Cov}(x_i,x_j)=2\eta_La_ia_j+2\eta_Rb_ib_j
\]
has rank exactly two; the limiting joint fourth-cumulant tensor is
\[
\lim_{\varepsilon\downarrow0}\varepsilon^2\operatorname{cum}(x_i,x_j,x_p,x_q)
=12\eta_L^2 a_i a_j a_p a_q+12\eta_R^2 b_i b_j b_p b_q.
\]
Consequently the limiting **excess** kurtosis of each site is
\[
K_i=3\,\frac{\eta_L^2a_i^4+\eta_R^2b_i^4}{(\eta_La_i^2+\eta_Rb_i^2)^2},\qquad \frac32\le K_i<3.
\]
For the continuous interpolation coordinate \(u=i/(n+1)\), the associated kurtosis curve has its unique minimum \(3/2\) at
\[
u_*=\frac{\sqrt{\eta_L}}{\sqrt{\eta_L}+\sqrt{\eta_R}}.
\]
On the discrete chain, its minimum is attained at one or both of the two lattice sites bracketing \(u_*\); equality with \(3/2\) holds precisely when one sampled site has coordinate \(u_*\). In particular, equal effective wall strengths give the exact center minimum \(3/2\) whenever \(n\) is odd.

There is an exact second-order indistinguishability contrast. If each resetting Brownian wall is replaced by an independent stationary Ornstein–Uhlenbeck wall \(dY_\sigma=-\varepsilon\lambda_\sigma Y_\sigma\,dt+\sqrt{4D_\sigma}\,dW_\sigma\), **all stationary two-time position and velocity covariance functions agree for every** \(\varepsilon>0\), but all Ornstein–Uhlenbeck-driven stationary position distributions are Gaussian (zero fourth cumulants). Their rescaled limiting profile is Gaussian with the *same* rank-two covariance as above, whereas the resetting-wall profile has the strictly positive fourth cumulants displayed above. Hence even complete second-order observations cannot discriminate these two specified reservoir mechanisms; fourth-order displacement statistics can.

## Assumptions and scope
Fix \(n\ge2\), oscillator mass \(m>0\), common spring stiffness \(k>0\), boundary damping \(\gamma>0\), wall diffusion coefficients \(D_L,D_R>0\), and fixed \(\lambda_L,\lambda_R>0\). Optional, independent boundary thermal Langevin baths have arbitrary fixed finite temperatures \(T_L,T_R\ge0\). For each \(\varepsilon>0\), take stationary, independent two-sided Brownian-reset wall motions \(X_L,X_R\) with generators \(D_\sigma\partial_{xx}+\varepsilon\lambda_\sigma[f(0)-f(x)]\). All Brownian noises, reset clocks and thermal baths are independent.

Let \(\mathbf x(t)\in\mathbb R^n\), \(\mathbf v(t)=\dot{\mathbf x}(t)\), let \(M\) be the \(n\times n\) tridiagonal matrix with diagonal entries \(2\) and nearest-neighbour entries \(-1\), and let \(\Gamma\) be diagonal with \(\Gamma_{11}=\Gamma_{nn}=\gamma\), all other entries zero. The chain dynamics (in the standard stochastic differential interpretation for the white-noise terms) is
\[
d\mathbf x=\mathbf v\,dt,\quad
m\,d\mathbf v=[-kM\mathbf x-\Gamma\mathbf v+k\mathbf e_1X_L+k\mathbf e_nX_R]dt
+\sqrt{2\gamma T_L}\,\mathbf e_1dB_L+\sqrt{2\gamma T_R}\,\mathbf e_ndB_R.
\]
Here \(\mathbf e_j\) denotes the standard basis vector. The walls themselves reset to zero, **not** the oscillator coordinates. The assertion is for the unique stationary law at each positive \(\varepsilon\), with \(n,m,k,\gamma,D_\sigma,\lambda_\sigma,T_\sigma\) held fixed before \(\varepsilon\to0\). It does not interchange this limit with \(n\to\infty\).

## Proof
**1. Stability and static transfer.** The homogeneous oscillator has energy \(E=(m/2)\sum_i v_i^2+(k/2)\mathbf x^TM\mathbf x\) and \(\dot E=-\gamma(v_1^2+v_n^2)\). Every eigenvector of \(M\) has components proportional to \(\sin(i\pi j/(n+1))\) and is nonzero at the first site. An undamped imaginary-axis mode would therefore force the first component of a normal mode to vanish, an impossibility. Zero is not an eigenvalue because \(M\) is positive definite. The finite-dimensional oscillator drift matrix is Hurwitz, so each position is a stable linear convolution of the two wall positions plus an independent stationary Gaussian thermal component:
\[
x_i(t)=\sum_{\sigma\in\{L,R\}}\int_0^\infty h_{i\sigma}(s)X_\sigma(t-s)\,ds+G_i(t),\qquad h_{i\sigma}\in L^1(0,\infty),
\]
with exponentially decaying kernels. Their integrals are their zero-frequency gains, found from static equilibrium \(M\mathbf z=\mathbf e_1X_L+\mathbf e_nX_R\):
\[
\int_0^\infty h_{iL}(s)ds=a_i,\qquad \int_0^\infty h_{iR}(s)ds=b_i.
\]
These follow from the unique discrete harmonic interpolation solving \(2z_i-z_{i-1}-z_{i+1}=0\) inside, \(2z_1-z_2=X_L\), and \(2z_n-z_{n-1}=X_R\).

**2. Reset walls and fourth-moment adiabatic bound.** The age \(A_\sigma\) since a wall's last reset is exponential with parameter \(r_\sigma=\varepsilon\lambda_\sigma\). Conditioned on \(A_\sigma=a\), the stationary wall displacement is centered Gaussian of variance \(2D_\sigma a\). Consequently
\[
\mathbb E\exp[it\sqrt\varepsilon X_\sigma(0)]
=\frac{\lambda_\sigma}{\lambda_\sigma+D_\sigma t^2}=\frac{1}{1+\eta_\sigma t^2},
\]
and its scaled fourth and eighth moments are bounded uniformly in \(\varepsilon\). For every fixed \(s\ge0\), let \(E_s\) be the event of at least one reset in \((-s,0]\). Its probability is at most \(\varepsilon\lambda_\sigma s\). On \(E_s^c\), the wall increment is a Brownian increment, so its scaled fourth moment tends to zero. On \(E_s\), Hölder's inequality and the uniform scaled eighth-moment bound give
\[
\mathbb E\left[\left|\sqrt\varepsilon\,(X_\sigma(-s)-X_\sigma(0))\right|^4\mathbf1_{E_s}\right]
\le C\,\mathbb P(E_s)^{1/2}\longrightarrow0.
\]
Therefore \(\|\sqrt\varepsilon[X_\sigma(-s)-X_\sigma(0)]\|_4\to0\) for fixed \(s\). The same norm is uniformly bounded in \(s,\varepsilon\) by the triangle inequality and stationarity. Minkowski's integral inequality and dominated convergence against \(|h_{i\sigma}(s)|ds\) imply
\[
\left\|\sqrt\varepsilon\,x_i(0)-a_i\sqrt\varepsilon X_L(0)-b_i\sqrt\varepsilon X_R(0)\right\|_4\longrightarrow0.
\]
The fixed-variance thermal Gaussian component disappears under multiplication by \(\sqrt\varepsilon\). These bounds hold jointly over the finite collection of sites, giving convergence of all joint moments through total degree four.

**3. Exact limiting spatial law and sharp kurtosis.** Independence of the wall processes gives the product characteristic function. A centered Laplace variable with characteristic function \((1+\eta t^2)^{-1}\) has variance \(2\eta\) and fourth cumulant \(12\eta^2\). Additivity of independent cumulants proves the covariance and fourth-order tensor formulas. The two gain vectors \((a_i)\) and \((b_i)\) are linearly independent for \(n\ge2\), so the covariance has rank two. Write
\[
p(u)=\frac{\eta_L(1-u)^2}{\eta_L(1-u)^2+\eta_Ru^2}.
\]
Then \(K(u)=3[p(u)^2+(1-p(u))^2]\), with \(p(u)\) strictly decreasing from one to zero on \((0,1)\). The unique minimum occurs at \(p=1/2\), which gives \(u_*\) as displayed, and the sharp range \(3/2\le K(u)<3\) for interior coordinates.

**4. Complete covariance matching with a Gaussian reservoir.** A stationary resetting Brownian wall has \(\operatorname{Cov}(X_\sigma(0),X_\sigma(t))=(2D_\sigma/r_\sigma)e^{-r_\sigma|t|}\): if a reset occurs in the lag, the conditional covariance vanishes, and otherwise it equals the initial variance. The displayed Ornstein–Uhlenbeck wall has precisely the same autocovariance. Independent walls and identical optional thermal baths therefore drive the *same* two-time covariances of every pair of linear position/velocity observables, by the stationary convolution representation. Unlike resetting walls, stationary Ornstein–Uhlenbeck inputs and thermal noises are jointly Gaussian, so all finite-rate oscillator vectors are Gaussian. The scaled Ornstein–Uhlenbeck increment \(\sqrt\varepsilon[Y_\sigma(-s)-Y_\sigma(0)]\) tends to zero in fourth mean at fixed \(s\), since its variance is \(4\eta_\sigma(1-e^{-\varepsilon\lambda_\sigma s})\). Repeating step 2 gives the stated Gaussian affine limiting field with identical covariance but zero fourth cumulants.

## Verification
`CHECK.py` is a complete standalone reproducibility checker. Run `python CHECK.py` in an environment with Python, NumPy, SymPy and SciPy; it checks exact tridiagonal static gains and rational Laplace moment/cumulant identities for multiple chain lengths and unequal wall strengths, verifies covariance matching algebraically, and numerically solves the augmented Ornstein–Uhlenbeck Lyapunov equation as an independent finite-rate second-moment test. The recorded run passed 487 assertions; exact signs, full joint convergence and all real parameters rest on the proof above, not finite parameter sampling.

## Relationship to prior work
Sarkar, Santra and Basu (arXiv:2210.09035) established linear active-reservoir harmonic-chain Green functions and the dependence of all second-order statistics on the driving covariance. Sarkar and Roy (arXiv:2307.06127) studied precisely the Poisson-resetting Brownian-wall chain and derived stationary velocity correlations, energy-current statistics and numerical finite-size velocity kurtosis. Guéneau, Majumdar and Schehr (arXiv:2306.09453) derived an active-limit Laplace distribution for a single overdamped particle driven by resetting Brownian noise under a different forcing normalization. These are antecedents, not claims of novelty here. The new evaluated claim is the **complete, finite-chain, joint slow-reset displacement law** and its rank-two and sharp spatial fourth-cumulant consequences, together with the covariance-indistinguishable matched-OU comparison. The latter comparison uses prior covariance principles but yields the stated explicit limiting fourth-order separation. Searches of available mathematical records and the accessible literature found no identical evaluated finite-chain spatial theorem; a hidden derivation in broader linear-response or active-bath literature remains a priority risk.

## Limitations
The limit first fixes finite \(n\); a joint limit with the chain length, nonlinear springs, interacting walls, state-dependent resetting, or non-Poissonian reset ages is not established. The result is an asymptotic stationary theorem, not a finite-\(\varepsilon\) displacement distribution, finite-sample statistical guarantee, or a statement about velocity kurtosis. The OU comparison establishes identical *second-order* laws, not pathwise equivalence, and assumes independent Gaussian OU reservoirs exactly matched in covariance. The finite computations check algebra and representative parameters but do not prove infinite parameter ranges. Scholarly originality is subject to independent priority assessment.

## References
1. R. Sarkar, I. Santra, and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035, first posted 2022-10-17. https://arxiv.org/abs/2210.09035
2. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453, first posted 2023-06-15. https://arxiv.org/abs/2306.09453
3. R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127, first posted 2023-07-12. https://arxiv.org/abs/2307.06127
