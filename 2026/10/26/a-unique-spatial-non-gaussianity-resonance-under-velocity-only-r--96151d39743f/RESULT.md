# A unique spatial non-Gaussianity resonance under velocity-only resetting

## Finding
For the one-dimensional, thermally forced harmonic oscillator undergoing independent Poisson resets of its **velocity alone**, the stationary positional non-Gaussian parameter is strictly positive at every finite positive resetting rate, yet tends to zero at both zero and infinite resetting rates. It has exactly one global maximizer for every choice of positive friction and trap strength. Specifically, writing \(\gamma>0\) for friction, \(\kappa>0\) for trap stiffness per unit mass, \(T>0\) for thermal velocity variance, and \(r>0\) for the velocity-resetting rate, define
\[
D(r)=r^3+9\gamma r^2+(26\gamma^2+10\kappa)r+24\gamma^3+32\gamma\kappa.
\]
For the unique stationary law \(\pi_r\), with \(\langle\cdot\rangle=\mathbb E_{\pi_r}\), let \(\alpha_X=\langle X^4\rangle/(3\langle X^2\rangle^2)-1\). Then
\[
\boxed{\alpha_X(r)=\frac{6\kappa r}{D(r)}.}
\]
Its unique maximizer \(r_*>0\) is characterized **exactly** by
\[
\boxed{2r_*^3+9\gamma r_*^2=24\gamma^3+32\gamma\kappa.}
\]
In contrast, the velocity non-Gaussian parameter satisfies
\[
\alpha_V(r)=\frac{r(r^2+5\gamma r+6\gamma^2+6\kappa)}{D(r)},
\qquad\lim_{r\to\infty}\alpha_V(r)=1.
\]
Thus the *normalized* positional fourth moment asymptotically returns to its Gaussian value under frequent **velocity** resets, although the normalized velocity fourth moment does not. The ordinary excess kurtoses are \(3\alpha_X\) and \(3\alpha_V\), respectively.

## Assumptions and scope
Between reset times, the state \((X_t,V_t)\in\mathbb R^2\) evolves according to the Itô equations
\[
dX_t=V_t\,dt,\qquad dV_t=(-\kappa X_t-\gamma V_t)\,dt+\sqrt{2\gamma T}\,dW_t,
\]
where \(W\) is standard Brownian motion. At each event of an independent homogeneous Poisson clock of rate \(r\), the state changes instantaneously by \((X,V)\mapsto(X,0)\). Neither the position nor the trap is reset. All parameters \(\kappa,\gamma,T,r\) are strictly positive and finite; there are no active forces, refractory periods or time-dependent protocols. For the boundary \(r=0\) the ordinary equilibrium Gaussian oscillator law is understood. The stated stationary quantities concern the unique invariant probability measure and not a finite-time distribution.

## Proof
**Existence, uniqueness and moments.** Let \(A=\begin{pmatrix}0&1\\-\kappa&-\gamma\end{pmatrix}\), let \(R=\operatorname{diag}(1,0)\) be the reset map, and use the energy norm \(\|(x,v)\|_E^2=\kappa x^2+v^2\). A deterministic segment evolves by \(e^{At}\), with \(d\|(x,v)\|_E^2/dt=-2\gamma v^2\le0\); a reset cannot increase this energy. Because \(\kappa>0\), no nonzero deterministic oscillator trajectory has velocity identically zero on a nonzero interval. Compactness of the energy unit sphere therefore gives a strict contraction \(\|e^{A h}z\|_E\le q_h\|z\|_E\) for each fixed \(h>0\), with \(q_h<1\). On successive independent length-\(h\) clock blocks, the no-reset event has probability \(e^{-rh}>0\); in those blocks the difference of two trajectories driven by the same noise and reset times is contracted by \(q_h\), while in all other blocks it is nonexpansive. The binomial law gives exponentially decaying *expected squared* differences at block endpoints and hence uniqueness of any stationary law and convergence in distribution from finite-second-moment starts.

The ordinary oscillator's equilibrium Gaussian covariance is \(\Sigma_0=\operatorname{diag}(T/\kappa,T)\). Start in this Gaussian equilibrium and condition on the full sequence of reset times: the law stays centered Gaussian, with covariance \(\Sigma\preceq\Sigma_0\) at all times, since between jumps the Ornstein–Uhlenbeck covariance evolution preserves Loewner order and fixes \(\Sigma_0\), while at jumps \(\Sigma\mapsto R\Sigma R^\top\preceq\Sigma_0\). In particular, the laws are tight and have uniformly bounded moments of every fixed order. The Feller property and time averaging yield an invariant law; the synchronous contraction makes it unique. All stationary polynomial identities through degree four are therefore legitimate. This argument also shows the invariant law is a mixture of centered Gaussian distributions conditioned on the past Poisson clock.

**Moment equations.** The exact generator on a polynomial \(f\) is
\[
\mathcal L f=v\partial_x f-(\kappa x+\gamma v)\partial_v f+\gamma T\partial_{vv}f+r[f(x,0)-f(x,v)].
\]
For nonnegative integers \(i,j\), its action on \(x^iv^j\) gives the stationary recurrence
\[
0=i\langle X^{i-1}V^{j+1}\rangle-j\kappa\langle X^{i+1}V^{j-1}\rangle -(j\gamma+r\mathbf1_{j>0})\langle X^iV^j\rangle+j(j-1)\gamma T\langle X^i V^{j-2}\rangle,
\]
where terms with negative exponents or zero coefficients are omitted. Stationary means vanish by symmetry. At degree two the three equations yield
\[
\langle XV\rangle=0,\qquad \langle V^2\rangle=\frac{2\gamma T}{2\gamma+r},\qquad \langle X^2\rangle=\frac{2\gamma T}{\kappa(2\gamma+r)}.
\]
At degree four the five equations yield
\[
\langle X^4\rangle=\frac{12\gamma^2T^2(12\gamma^2+7\gamma r+16\kappa+r^2)}{\kappa^2(2\gamma+r)D(r)},
\]
\[
\langle V^4\rangle=\frac{24\gamma^2T^2(6\gamma^2+5\gamma r+8\kappa+r^2)}{(2\gamma+r)D(r)},
\]
\[
\langle X^3V\rangle=0,\quad\langle XV^3\rangle=\frac{12\gamma^2T^2r}{(2\gamma+r)D(r)},\quad\langle X^2V^2\rangle=\frac{4\gamma^2T^2(12\gamma^2+7\gamma r+16\kappa+r^2)}{\kappa(2\gamma+r)D(r)}.
\]
All displayed denominators are strictly positive on the parameter domain. Substituting in \(\langle X^4\rangle/(3\langle X^2\rangle^2)-1\) and its velocity analogue proves the two closed forms above.

**Sharp optimization and limits.** Direct differentiation, without numerical root selection, gives
\[
\alpha_X'(r)=\frac{6\kappa}{D(r)^2}\,[24\gamma^3+32\gamma\kappa-9\gamma r^2-2r^3].
\]
The bracket strictly decreases on \(r>0\), is positive at zero and tends to minus infinity; hence it has exactly one positive zero. That zero is the unique global maximum since \(\alpha_X(r)>0\) and the two boundary limits are zero. Explicitly,
\[
\lim_{r\downarrow0}\frac{\alpha_X(r)}r=\frac{6\kappa}{24\gamma^3+32\gamma\kappa},\quad
\lim_{r\to\infty}r^2\alpha_X(r)=6\kappa,\quad
\lim_{r\to\infty}\alpha_V(r)=1.
\]
The claim does not assert full Gaussian convergence of the standardized positional law: only the proven fourth-moment statement is used.

## Verification
Run the standalone Python/SymPy program \(\texttt{verification/check.py}\) from the extracted package directory. It independently builds the full degree-two and degree-four generator matrices, solves the finite linear systems, checks the symbolic identities for the stationary moments, differentiates the non-Gaussian parameter and tests exact-rational specializations. The included script is a finite algebra check, not a substitute for the analytical existence, uniqueness or one-root arguments supplied above.

## Relationship to prior work
Evans and Majumdar's original 2011 stochastic-resetting diffusion model resets *position* to a distinguished location and establishes a non-Gaussian stationary state. It supplies the archival motivation but neither an underdamped harmonic trap nor the velocity-only protocol. Olsen (2023) treats harmonic trapping with *position* resetting to a distribution and a corresponding stationary-moment framework; its displayed state variable and reset operation are different. Olsen and Löwen (2024) develop partial/velocity resetting for inertial transport; their explicit Fourier–Laplace solution and moment hierarchy require spatial homogeneity (their equation (4)), and the worked underdamped dynamics (their equations (26)–(27)) has no restoring term \(-\kappa X\). A harmonic trap violates spatial homogeneity, and the stationary positional fourth-moment resonance established here is not implied by their transport coefficient formulas. Gupta's inertial resetting model (arXiv:1812.07227) resets position while retaining velocity. General affine-jump or polynomial-generator techniques may recover the finite moment equations, but do not on their own provide the sharp rate optimization and distinct spatial versus velocity asymptotics proved here.

## Limitations
The theorem concerns one harmonic mode with velocity reset exactly to zero and independent Poisson times. Neither higher-dimensional coupled traps, nonzero reset velocity, arbitrary reset distributions, nor non-Poisson clocks is classified. The normalized spatial fourth moment returning to its Gaussian value does not establish distributional Gaussianity, particularly because the unstandardized position variance shrinks to zero as \(r\to\infty\). A full literature priority guarantee is not possible; the closest primary works and their explicit hypotheses were compared, but an unlocated specialized calculation may exist. No independent audit has been performed.

## References
1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704v1 (first public 2011-02-14), Physical Review Letters **106**, 160601 (2011), https://arxiv.org/abs/1102.2704.
2. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840v1 (first public 2023-10-07), Physical Review E **108**, 044120 (2023), https://doi.org/10.1103/PhysRevE.108.044120.
3. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685v1 (first public 2024-01-23), Journal of Statistical Mechanics **2024**, 033210 (2024), https://doi.org/10.1088/1742-5468/ad319a. Author-hosted primary text: https://user.thphy.uni-duesseldorf.de/hlowen/doc/op/op0503.pdf.
4. D. Gupta, *Stochastic resetting in underdamped Brownian motion*, arXiv:1812.07227v1 (first public 2018-12-18), https://arxiv.org/abs/1812.07227.
