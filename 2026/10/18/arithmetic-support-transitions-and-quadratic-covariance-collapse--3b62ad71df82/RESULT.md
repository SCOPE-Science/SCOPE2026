# Arithmetic support transitions and quadratic covariance collapse for two-kick stochastic exponential quadrature

## Finding

Consider additive-noise, underdamped Langevin dynamics. A natural two-piece right-endpoint approximation of its stochastic convolution has an exact number-theoretic dichotomy: a rational internal splitting fraction creates infinitely many step sizes at which the invariant Gaussian covariance has rank one; an irrational fraction avoids rank loss at **every** positive step. Two independent within-step Gaussian increments are the smallest possible number allowing an all-step, full-support invariant law in this scalar-driven oscillator family. At each rational resonance, the smallest covariance eigenvalue collapses quadratically with an explicit positive coefficient, and the numerical stationary law becomes mutually singular with the exact stationary law.

For reduced \(\alpha=a/q\) with integers \(0<a<q\), the rank-loss steps are exactly \(h=kq\pi/\omega\) for \(k\ge1\). At an arbitrary oscillator resonance \(h=m\pi/\omega\), let \(r=e^{-2\gamma h}\). Then
\[
\det P_h=\left(\frac{h\sigma^2}{1-r}\right)^2\frac{\alpha(1-\alpha)r^{\alpha}}{\omega^2}\sin^2(m\pi\alpha).
\]
In particular, the elementary equal split \(\alpha=1/2\) removes all odd resonances of the single-kick method but leaves the even ones.

## Assumptions and scope

Let \(\gamma>0\), \(\omega>0\), \(\sigma>0\), and \(\Omega^2=\gamma^2+\omega^2\). Set
\[
A=\begin{pmatrix}0&1\\-\Omega^2&-2\gamma\end{pmatrix},\qquad
b=\begin{pmatrix}0\\1\end{pmatrix},\qquad E_t=e^{tA}.
\]
The Itô stochastic oscillator is \(\mathrm dZ_t=A Z_t\,\mathrm dt+\sigma b\,\mathrm dW_t\), where \(Z_t=(q_t,v_t)^\mathsf T\) and \(W\) is a real standard Brownian motion. Fix arbitrary \(h>0\) and an internal split fraction \(0<\alpha<1\). With \(t_n=nh\), define independent increments from the **same Brownian path** by
\[
\Delta W_{n,1}=W_{t_n+(1-\alpha)h}-W_{t_n},\qquad
\Delta W_{n,2}=W_{t_n+h}-W_{t_n+(1-\alpha)h}.
\]
Their variances are \((1-\alpha)h\) and \(\alpha h\). The right-endpoint stochastic-convolution quadrature is
\[
Z_{n+1}=E_hZ_n+\sigma\bigl(E_{\alpha h}b\,\Delta W_{n,1}+b\,\Delta W_{n,2}\bigr).
\]
All arithmetic and matrix exponentials are exact. No statement concerns adaptive steps, nonlinear potentials, overdamped dynamics, correlations between increments from different steps, or attainable exact irrational numbers in finite precision.

Its one-step innovation covariance is
\[
Q_h=h\sigma^2\bigl((1-\alpha)E_{\alpha h}bb^\mathsf T E_{\alpha h}^\mathsf T+\alpha bb^\mathsf T\bigr).
\]
The matrix \(P_h\) is the unique solution of \(P_h=E_hP_hE_h^\mathsf T+Q_h\). The exact continuous-time invariant covariance is
\[
P_{\mathrm{ct}}=\begin{pmatrix}\sigma^2/(4\gamma\Omega^2)&0\\0&\sigma^2/(4\gamma)\end{pmatrix}\succ0.
\]
The total-variation convention is \(\operatorname{TV}(\mu,\nu)=\sup_B|\mu(B)-\nu(B)|\in[0,1]\).

## Proof

**1. Existence, uniqueness, and the reachability Gramian.** The eigenvalues of \(A\) are \(-\gamma\pm i\omega\); hence the spectral radius of \(E_h\) is \(e^{-\gamma h}<1\). Iterating the affine Gaussian recursion and summing geometric covariances yields exactly one invariant Gaussian measure \(\mathcal N(0,P_h)\), where
\[
P_h=h\sigma^2\sum_{j=0}^{\infty}\left[\alpha E_h^jbb^\mathsf T(E_h^j)^\mathsf T +(1-\alpha)E_{(j+\alpha)h}bb^\mathsf T E_{(j+\alpha)h}^\mathsf T\right].
\]
Because every scalar weight is positive, its range is the span of \(E_{jh}b\) and \(E_{(j+\alpha)h}b\), for integers \(j\ge0\). This is the standard controllability-Gramian observation, not itself claimed as new.

**2. Complete rank classification.** Direct exponentiation gives
\[
E_t b=e^{-\gamma t}\begin{pmatrix}\sin(\omega t)/\omega\\ \cos(\omega t)-\gamma\sin(\omega t)/\omega\end{pmatrix}.
\]
If \(\sin(\omega h)\ne0\), \(b\) and \(E_hb\) are linearly independent, so \(P_h\succ0\) regardless of \(\alpha\). If \(\omega h=m\pi\) with \(m\ge1\), \(E_h=(-1)^m e^{-\gamma h}I_2\); all powers \(E_h^j\) are scalars, and \(P_h\) is full rank precisely when the two vectors \(b\) and \(E_{\alpha h}b\) are independent. Their determinant is \(-e^{-\gamma\alpha h}\sin(\alpha m\pi)/\omega\). Therefore rank loss is equivalent to the simultaneous conditions \(\omega h=m\pi\) and \(m\alpha\in\mathbb Z\). If \(\alpha=a/q\) is in lowest terms, the latter means \(q\mid m\). For irrational \(\alpha\), it is impossible at every integer \(m\). At a rank-loss step, the range equals \(\operatorname{span}\{b\}\), i.e. the velocity axis.

At any resonant step, the matrix \(E_h\) is scalar. Thus
\[
P_h=\frac{h\sigma^2}{1-r}\left[\alpha bb^\mathsf T+(1-\alpha)E_{\alpha h}bb^\mathsf T E_{\alpha h}^\mathsf T\right],\qquad r=e^{-2\gamma h}.
\]
The determinant of the sum of two rank-one positive matrices is the product of their scalar weights times the squared two-vector determinant. Applying the determinant above proves the displayed exact determinant law. Conversely, with only one independent Gaussian increment at any fixed within-step exponential phase \(\beta\), the innovation covariance is rank one and, at every resonant step, \(E_h\) is scalar, so the invariant covariance remains rank one. Therefore at least two independent kicks are necessary for an all-step full-rank construction, and the irrational two-piece scheme attains this minimum.

**3. Exact quadratic degeneracy.** Let \(h_*=m\pi/\omega\) be a singular step with \(m\alpha\in\mathbb Z\), and set \(\delta=h-h_*\). Define \(r_*=e^{-2\gamma h_*}\), \(w_0=\alpha\), \(w_{\alpha}=(1-\alpha)r_*^{\alpha}\), and \(W=(w_0+w_{\alpha})/(1-r_*)\). At resonance each vector \(E_{(j+s)h_*}b\), with \(s\in\{0,\alpha\}\), is a signed multiple of \(b\). After removing that harmless sign, its horizontal-to-vertical slope has expansion \((j+s)\delta+O((j+s)^2\delta^2)\). The signed vertical amplitude is \(r_*^{(j+s)/2}\) at \(\delta=0\).

The leading small eigenvalue of this positive Gramian is the total weighted mass multiplied by the weighted variance of these slopes. The weights are \(w_0r_*^j\) for \(s=0\) and \(w_{\alpha}r_*^j\) for \(s=\alpha\). Their total mass is \(W\). The integer index \(j\), distributed with geometric weights \((1-r_*)r_*^j\), has variance \(r_* /(1-r_*)^2\). The independent two-point phase index \(s\in\{0,\alpha\}\) has variance \(w_0w_{\alpha}\alpha^2/(w_0+w_{\alpha})^2\). Consequently
\[
\boxed{\lambda_{\min}(P_h)=h_*\sigma^2 W\left(\frac{r_*}{(1-r_*)^2}+\frac{w_0w_{\alpha}\alpha^2}{(w_0+w_{\alpha})^2}\right)\delta^2+o(\delta^2).}
\]
This coefficient is strictly positive. The expansion is legitimate under the infinite sum: for \(h\) near \(h_*>0\), derivatives of the summands are bounded by a polynomial in \(j\) times a uniform geometric factor. Equivalently, one can expand \(\det P_h/\operatorname{tr}P_h\), since its other eigenvalue approaches \(h_*\sigma^2W>0\).

**4. The exact Gaussian-law obstruction.** Solving the continuous Lyapunov equation \(AP_{\mathrm{ct}}+P_{\mathrm{ct}}A^\mathsf T+\sigma^2bb^\mathsf T=0\) yields the positive-definite diagonal matrix in the assumptions. At a discrete singular step, \(\mathcal N(0,P_h)\) gives probability one to the velocity axis; the continuous invariant Gaussian gives it probability zero. Their total-variation distance therefore equals one. At all nonsingular steps the two centered Gaussians have everywhere-positive Lebesgue densities, so their total-variation distance is strictly less than one (not necessarily small). Along nonresonant steps tending to a singular step, the smallest variance tends to zero quadratically; a shrinking strip around the velocity axis captures asymptotically all numerical mass and asymptotically no exact stationary mass, giving total-variation limit one.

## Verification

The accompanying standalone `verify.py` computes \(E_h\) in closed form, solves the three-dimensional linear system equivalent to the discrete matrix Lyapunov equation, checks the exact resonant determinants and tests the predicted quadratic eigenvalue scaling. It also verifies the elementary rational-denominator criterion and the small-step stationary covariance limit. It passed 3,655 deterministic checks on its packaged source. The infinity- and irrationality-quantified assertions are established by the proof, **not** by these finite numerical checks.

For a numerical reproduction, choose \(\gamma=0.2\), \(\omega=1.3\), \(\sigma=1.17\), \(\alpha=1/2\), and \(h_*=2\pi/\omega=4.83321946706122\ldots\). At this exact resonance, the position variance vanishes and the velocity variance is approximately \(5.338718097851207\); the coefficient of \((h-h_*)^2\) in the smallest eigenvalue is approximately \(1.322167202261677\). Floating-point output around a theoretical zero can show rounding-level residues.

## Relationship to prior work

The source by Arara, Debrabant and Kværnø (2023) develops B-series and order conditions for a broad class of stochastic exponential integrators, including its general semi-linear form in Section 4. The damped stochastic-wave invariant-measure analysis by Lei, Bréhier and Gan (2023) studies an exponential Euler method and convergence of invariant distributions. The earlier stochastic trigonometric scheme of Cohen, Larsson and Sigg (2012) establishes strong finite-time error estimates and a trace formula for an undamped wave equation. None of those checked formulations supplies the stated arithmetic all-step rank classification together with the exact stationary determinant and quadratic collapse coefficient.

Classical sampled controllability theory, including Hautus (1972) and nonuniform sampling constructions by Hamidoğlu and Mahmudov (2020), already explains qualitatively why sampled input directions can lose or recover reachability. These general insights and the reachability-Gramian equivalence are prior art. They should **not** be read as novelty claims. The contribution tested here is the specific Brownian two-subinterval numerical covariance, its complete rational/irrational stationary-support phase diagram, the explicit covariance determinant and eigenvalue asymptotic, and the resulting total-variation obstruction. The potentially relevant complete 2020 sampling article was not available for full-text comparison; an equivalent quantitative result there or elsewhere cannot be excluded.

## Limitations

The conclusions concern a real scalar-driven two-dimensional underdamped oscillator, exact independent Brownian subincrements, a fixed internal fraction, and exact arithmetic. The result does not establish accuracy superiority of irrational fractions, nor a uniform covariance condition number or robust finite-precision nondegeneracy; practical irrational fractions are represented approximately. At small steps, the method remains a consistent stochastic convolution approximation even for rational fractions: Ito isometry yields a local mean-square integral error of order \(O(h^{3/2})\), and the exceptional positive resonant steps stay away from zero for each fixed rational fraction. The construction does not contradict standard small-step weak convergence of invariant-measure schemes. No claim is made about general nonnormal or multidimensional stochastic systems or arbitrary split-step methods. Originality requires independent human literature review, especially of classical sampling constructions.

## References

- A. A. Arara, K. Debrabant, A. Kværnø, *B-series for SDEs with application to exponential integrators for non-autonomous semi-linear problems*, first preprint 2023-10-13, arXiv:2310.09179, https://arxiv.org/abs/2310.09179 . Primary MSC 65C30 (publisher classification).
- Z. Lei, C.-E. Bréhier, S. Gan, *Numerical approximation of the invariant distribution for a class of stochastic damped wave equations*, first preprint 2023-06-24, arXiv:2306.13998, https://arxiv.org/abs/2306.13998 .
- D. Cohen, S. Larsson, M. Sigg, *A trigonometric method for the linear stochastic wave equation*, arXiv:1203.3668, https://arxiv.org/abs/1203.3668 .
- M. L. J. Hautus, *Controllability and stabilizability of sampled systems*, IEEE Transactions on Automatic Control 17 (1972), 528–531, doi:10.1109/TAC.1972.1100045.
- A. Hamidoğlu, E. N. Mahmudov, *On construction of sampling patterns for preserving observability/controllability of linear sampled-data systems*, International Journal of Control, published online 2020, doi:10.1080/00207179.2020.1787523 (full-text comparison unresolved).
