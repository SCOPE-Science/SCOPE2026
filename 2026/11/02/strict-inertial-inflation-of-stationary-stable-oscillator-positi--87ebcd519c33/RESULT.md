# Strict inertial inflation of stationary stable-oscillator positions and a sharp small-mass rate

## Finding

For a one-dimensional harmonic Langevin oscillator driven by symmetric strictly \(\alpha\)-stable Lévy noise with \(1<\alpha<2\), increasing the mass throughout the nonoscillatory damping range strictly enlarges the stationary position law by a positive scale factor. In particular, the exact invariant-position Wasserstein distance from the overdamped law increases strictly from zero, and the small-mass convergence rate is **linear with a strictly positive explicit coefficient**, rather than merely the general \(m^{1/\alpha}\) upper bound.

Fix \(\gamma,\kappa,\eta>0\) and \(1<\alpha<2\). Let \(L\) be symmetric stable Lévy motion with \(\mathbb E e^{i\xi L_t}=e^{-t|\xi|^\alpha}\). Consider
\[
 dX_t=V_t\,dt,\qquad m\,dV_t=(-\gamma V_t-\kappa X_t)\,dt+\eta\,dL_t,
\]
for \(0<m\le m_c=\gamma^2/(4\kappa)\), and the overdamped process
\[
 dY_t=-(\kappa/\gamma)Y_t\,dt+(\eta/\gamma)\,dL_t.
\]
Their stationary position laws \(\mu_m\) and \(\mu_0\) are unique. If \(Z_\alpha\) has characteristic function \(e^{-|\xi|^\alpha}\), then
\[
 \mu_m=\operatorname{Law}(\eta I_m^{1/\alpha}Z_\alpha),\qquad
 \mu_0=\operatorname{Law}(\eta I_0^{1/\alpha}Z_\alpha),\qquad
 I_0=\frac{\gamma^{1-\alpha}}{\alpha\kappa}.
\]
For \(0<m<m_c\), define
\[
 \Delta=\sqrt{\gamma^2-4m\kappa},\qquad
 a=\frac{\alpha(\gamma-\Delta)}{2\Delta}.
\]
The exact scale is
\[
 I_m=\frac{m}{\Delta^{\alpha+1}}B(a,\alpha+1)
 =\frac{\gamma^{1-\alpha}}{\kappa}\frac{\Gamma(\alpha+1)}{\alpha^{\alpha+1}}
 (2a+\alpha)^{\alpha-1}\frac{\Gamma(a+1)}{\Gamma(a+\alpha)}.
\]
At the critically damped endpoint,
\[
 I_{m_c}=\frac{\gamma^{1-\alpha}}{\kappa}
 \frac{2^{\alpha-1}\Gamma(\alpha+1)}{\alpha^{\alpha+1}}.
\]
The function \(m\mapsto I_m\) is strictly increasing on \([0,m_c]\) (where the zero value means the continuous endpoint). Thus for any \(0\le m_1<m_2\le m_c\), the absolute stationary position \(|X|\) at \(m_2\) strictly stochastically dominates that at \(m_1\). In particular,
\[
 W_1(\mu_m,\mu_0)=\frac{2\eta\Gamma(1-1/\alpha)}{\pi}
 \big(I_m^{1/\alpha}-I_0^{1/\alpha}\big).
\]
Writing \(\psi\) for the digamma function and \(\gamma_E\) for Euler's constant, define
\[
 R_\alpha=2\alpha-1-\alpha\big(\psi(\alpha+1)+\gamma_E\big)>0.
\]
Then, as \(m\downarrow0\),
\[
 W_1(\mu_m,\mu_0)=C_\alpha m+O(m^2),\qquad
 C_\alpha=\frac{2\eta\Gamma(1-1/\alpha)}{\pi}
 \left(\frac{\gamma^{1-\alpha}}{\alpha\kappa}\right)^{1/\alpha}
 \frac{\kappa R_\alpha}{\alpha\gamma^2}>0.
\]
All constants use the displayed characteristic-function normalization; changing the noise normalization changes the scale factor accordingly.

## Assumptions and scope

The driving noise is additive, one-dimensional, symmetric, strictly stable, and satisfies \(1<\alpha<2\). The coefficients \(\gamma,\kappa,\eta\) are strictly positive, the confining force is exactly linear, and the mass lies in the closed nonoscillatory range \(0<m\le\gamma^2/(4\kappa)\). Only the **position marginal** of the invariant joint position–velocity law is compared; the overdamped process supplies the \(m=0\) endpoint. The invariant laws have finite first absolute moments because \(\alpha>1\). No claim concerns a nonlinear force or underdamped oscillatory masses beyond the stated endpoint.

## Proof

**1. Stationary stochastic convolution.** For \(m<m_c\), the stable deterministic matrix has two distinct negative eigenvalues
\[
 r_s=\frac{-\gamma+\Delta}{2m},\qquad r_f=\frac{-\gamma-\Delta}{2m}.
\]
The impulse response from force to position is
\[
 G_m(t)=\frac{e^{r_st}-e^{r_ft}}{\Delta}\quad(t\ge0).
\]
It is nonnegative, nonzero and exponentially integrable. At the critical endpoint the double-root limit is \(G_{m_c}(t)=t e^{-\gamma t/(2m_c)}/m_c\). Stability ensures that stochastic convolution over the infinite past defines the unique invariant law: any two trajectories under the same noise have deterministic differences that decay exponentially. The stable-integral characteristic function gives the position marginal with \(I_m=\int_0^\infty G_m(t)^\alpha dt\). The overdamped impulse is \(G_0(t)=\gamma^{-1}e^{-\kappa t/\gamma}\), so \(I_0=\gamma^{1-\alpha}/(\alpha\kappa)\).

**2. Exact beta and gamma formula.** Put \(u=e^{-\Delta t/m}\). Then
\[
 G_m(t)=\Delta^{-1}u^{(\gamma-\Delta)/(2\Delta)}(1-u),
 \qquad dt=-\frac m\Delta\frac{du}u.
\]
Direct integration yields \(I_m=m\Delta^{-\alpha-1}B(a,\alpha+1)\). The identities
\[
 \Delta=\frac{\gamma\alpha}{2a+\alpha},\qquad
 m=\frac{\gamma^2a(a+\alpha)}{\kappa(2a+\alpha)^2}
\]
transform it into the stated gamma quotient. Direct integration of the critical kernel produces the displayed endpoint value.

**3. Strict increase in mass.** The parameter \(a\) increases continuously and strictly from \(0\) to \(+\infty\) as \(m\) increases from zero to the critical value. The only mass-dependent factor in the gamma formula is
\[
 H(a)=(2a+\alpha)^{\alpha-1}
 \frac{\Gamma(a+1)}{\Gamma(a+\alpha)}.
\]
For every \(a\ge0\), differentiation and the standard integral representation of the digamma difference give
\[
 \frac{H'(a)}{H(a)}
 =\frac{\alpha-1}{a+\alpha/2}
 -\int_0^\infty e^{-(a+\alpha/2)t}
 \frac{\sinh((\alpha-1)t/2)}{\sinh(t/2)}\,dt.
\]
Since \(0<\alpha-1<1\), strict convexity of \(\sinh\) and \(\sinh(0)=0\) imply
\[
 0<\frac{\sinh((\alpha-1)t/2)}{\sinh(t/2)}<\alpha-1
 \quad(t>0).
\]
The integral is strictly less than \((\alpha-1)/(a+\alpha/2)\), so \(H'(a)>0\). The gamma-ratio asymptotic \(\Gamma(a+1)/\Gamma(a+\alpha)\sim a^{1-\alpha}\) extends this strict increase to the finite critical endpoint. At zero, the same formula gives \(I_0\) by continuity.

**4. Exact Wasserstein metric and stochastic order.** Stable laws with fixed index and zero location differ here only by positive dilation. Coupling the two distributions using the same \(Z_\alpha\) yields an upper bound \(\eta\mathbb E|Z_\alpha|\,|I_{m_2}^{1/\alpha}-I_{m_1}^{1/\alpha}|\) on \(W_1\). The one-Lipschitz test function \(x\mapsto|x|\) yields the matching lower bound. Since \(\mathbb E|Z_\alpha|=2\Gamma(1-1/\alpha)/\pi\), the exact distance follows. Strictly larger dilation also gives the asserted strict absolute-value stochastic order for every positive threshold, because nondegenerate symmetric stable laws have a positive continuous density on the real line.

**5. Sharp small-mass expansion.** Set \(\delta=\kappa m/\gamma^2\). Expansion of the square root in \(a\) gives \(a=\alpha\delta+O(\delta^2)\). The gamma formula is analytic in \(a\) near zero, so
\[
 \frac{I_m}{I_0}=1+R_\alpha\delta+O(\delta^2),
 \qquad R_\alpha=2\alpha-1-\alpha(\psi(\alpha+1)+\gamma_E).
\]
Indeed \(R_\alpha=\alpha H'(0)/H(0)>0\) by Step 3; this gives a direct proof of the strict sign without numerical estimates. Taking the positive \(\alpha\)-th root and multiplying by \(\eta\mathbb E|Z_\alpha|\) yields the claimed linear coefficient and \(O(m^2)\) remainder.

## Verification

The included standalone Python script `check.py` uses only the standard library. It compares the two exact integral representations; numerically integrates the impulse kernel independently; samples parameter grids to test predicted monotonicity, strict overdamped comparison, and critical endpoint bounds; checks the first-order coefficient and the Gaussian boundary. Its recorded reproducible output is in `check_output.txt`. These checks are finite illustrations, not proofs for all real parameters; the proof above establishes the quantified statements.

## Relationship to prior work

Jin and Tao, arXiv:2610.32217v1 (first posted 2026-10-23), prove a general bound \(W_1\le C m^{1/\alpha}\) between stable-noise Langevin invariant position and overdamped invariant laws, without the present exact harmonic small-mass rate or all-mass monotonicity theorem. The result here is a sharp **special-case refinement**, not a universal replacement for that bound.

Dybiec, Gudowska-Nowak and Sokolov, arXiv:1704.02119, equations (11)–(16), already give the harmonic oscillator Green function and the stationary stable position width as an integral of its \(\alpha\)-th power. This exact **integral representation is prior work**, and therefore is not itself an originality claim here. The evaluated beta/gamma parameterization supports the additional strict-mass inequality and nonzero Wasserstein derivative, which are not stated in their inspected analysis of stationary energy ratios and damping asymptotics.

Baldovin, Guéry-Odelin and Trizac, arXiv:2207.09357v1, obtain Fourier-space stationary descriptions and harmonic-trap driving protocols for stable noise in overdamped and underdamped regimes. Their inspected Sections II–III and Appendix B do not state the claimed mass-monotonicity or sharp small-mass Wasserstein coefficient.

F. Qi and R. P. Agarwal's 2019 open-access survey of gamma-ratio inequalities provides related general special-function monotonicity techniques. Such inequalities may streamline Step 3, and no independent priority is claimed for the digamma/sinh inequality considered in isolation; the probability-theoretic mass response and explicit \(W_1\) rate are the assessed findings.

## Limitations

Only the nonoscillatory mass range is covered. When \(m>m_c\), the impulse changes sign and the present beta-factor monotonic argument does not apply. When \(\alpha\le1\), invariant first moments diverge and \(W_1\) is generally not finite. The Gaussian boundary \(\alpha=2\) is exceptional: the stationary position scale is independent of mass (one can verify \(\int_0^\infty G_m(t)^2dt=1/(2\gamma\kappa)\)). The exact rate is for a *linear* force; broader stochastic systems can have slower error rates. Prior integral representations and possible unlocated gamma-ratio inequalities create historical-priority risk; this is a research claim, not independent mathematical certification.

## References

1. X. Jin and W. Tao, *Wasserstein bounds for invariant measures in the Smoluchowski-Kramers approximation with stable noise*, arXiv:2610.32217v1, first posted 2026-10-23. https://arxiv.org/html/2610.32217v1
2. B. Dybiec, E. Gudowska-Nowak and I. M. Sokolov, *Underdamped stochastic harmonic oscillator driven by Lévy noise*, Physical Review E 96 (2017), 042118; arXiv:1704.02119, equations (11)–(16). https://arxiv.org/pdf/1704.02119
3. M. Baldovin, D. Guéry-Odelin and E. Trizac, *Shortcuts To Adiabaticity for Lévy processes in harmonic traps*, Physical Review E 106 (2022), 054122; arXiv:2207.09357v1, Sections II–III and Appendix B. https://arxiv.org/html/2207.09357v1
4. F. Qi and R. P. Agarwal, *On complete monotonicity for several classes of functions related to ratios of gamma functions*, Journal of Inequalities and Applications 2019, article 36 (2019). https://link.springer.com/article/10.1186/s13660-019-1976-z
