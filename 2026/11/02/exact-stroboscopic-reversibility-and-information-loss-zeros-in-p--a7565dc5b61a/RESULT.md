# Exact stroboscopic reversibility and information-loss zeros in planar Ornstein–Uhlenbeck dynamics

## Finding

For every stable, two-dimensional Ornstein–Uhlenbeck (OU) diffusion with strictly positive definite constant diffusion matrix, we give the exact relative entropy between its stationary two-time law and the law with observation order reversed. For genuinely irreversible dynamics this quantity vanishes at a positive observation lag if and only if the drift has a nonreal conjugate eigenvalue pair. In that case the **complete** set of vanishing lags consists of positive integer multiples of half the oscillation period. At every such lag the entire equally spaced stationary sampled process, not merely a scalar correlation, satisfies detailed balance. Near each zero, the observed irreversibility has a strictly positive, explicitly computable quadratic coefficient.

As an application, the equal-self-anchoring conformist–contrarian two-agent dynamics of Dey (2026) has exact invisible sampling lags even while its physical continuous-time entropy-production rate is strictly positive. In its short-foresight regime, the first such lag diverges inversely in the planning time, but the physical entropy produced over the lag approaches a positive constant.

## Assumptions and scope

Let \(B\in\mathbb R^{2\times2}\) have eigenvalues with strictly positive real parts, and let \(D\in\mathbb R^{2\times2}\) be symmetric positive definite. Consider the stationary solution of
\[
 dX_t=-BX_t\,dt+\sqrt{2D}\,dW_t.
\]
Its unique stationary covariance \(S\) is the symmetric positive definite solution of \(BS+SB^{\mathsf T}=2D\). Define the covariance-whitened drift \(K=S^{-1/2}BS^{1/2}\), the lag transition \(F_t=e^{-Bt}\), and \(G_t=S^{-1/2}F_tS^{1/2}=e^{-Kt}\). The stationary normalized process is \(Y_t=S^{-1/2}X_t\), which has covariance \(I_2\). For every \(t>0\), let
\[
\mathcal I(t)=D_{\mathrm{KL}}\bigl(\mathcal L(Y_0,Y_t)\,\|\,\mathcal L(Y_t,Y_0)\bigr),
\]
using natural logarithms; swapping observations does not reverse odd-under-time-reversal physical velocity variables because these are two positional coordinates. Let \(\Delta=K_{12}-K_{21}\), \(\mu=\tfrac12\operatorname{tr}B\), and \(q_t=e^{-2\mu t}\).

**Exact two-time formula.** For every \(t>0\),
\[
\boxed{\mathcal I(t)=\frac{(G_{t,12}-G_{t,21})^2\bigl(1-\det G_t\bigr)}{\det(I_2-G_tG_t^{\mathsf T})}.}
\tag{1}
\]
Its denominator is strictly positive. Thus \(\mathcal I(t)=0\) if and only if the sampled transition satisfies stationary detailed balance.

**Complete zero-lag classification.** If \(BS=SB^{\mathsf T}\), then \(\mathcal I(t)=0\) for all positive lags. Suppose instead \(BS\ne SB^{\mathsf T}\). If \(\det B\le\mu^2\) (real eigenvalues, including a repeated or defective root), then \(\mathcal I(t)>0\) at every \(t>0\). If \(\det B>\mu^2\), write \(\Omega=\sqrt{\det B-\mu^2}>0\). Then
\[
\boxed{\{t>0:\mathcal I(t)=0\}=\{k\pi/\Omega:k=1,2,\ldots\}.}
\tag{2}
\]
At these lags \(t_k=k\pi/\Omega\),
\[
 F_{t_k}=(-1)^ke^{-\mu t_k}I_2,
\]
and the stationary sequence \((X_{nt_k})_{n\in\mathbb Z}\) is a reversible Gaussian autoregressive Markov chain. Moreover,
\[
\boxed{\mathcal I(t_k+h)=\frac{q_{t_k}\Delta^2}{1-q_{t_k}}h^2+O(h^3)}\quad(h\to0).
\tag{3}
\]
The coefficient is strictly positive. The power-law remainder is at fixed drift and diffusion coefficients.

**Rotational special case.** For \(B=\alpha I_2+\omega\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), \(D=d I_2\), and \(\alpha,d>0\), \(\omega\ne0\), the exact law simplifies to
\[
\boxed{\mathcal I(t)=\frac{4e^{-2\alpha t}\sin^2(\omega t)}{1-e^{-2\alpha t}},\qquad \lim_{t\downarrow0}\frac{\mathcal I(t)}t=\frac{2\omega^2}{\alpha}>0.}
\tag{4}
\]
Thus every invisible sampling lag hides a **strictly positive** continuous-time physical entropy-production rate.

**Two-agent consequence.** The symmetry-compatible stable Nash branch for Dey's (2026) equal-self-anchoring conformist–contrarian case has drift \(B=r^{-1}\left(\begin{smallmatrix}A&C\\-C&A\end{smallmatrix}\right)\) with \(A>0\), \(C\ne0\), common noise covariance \(D=dI_2\), and positive game constants \(a,b,r\). Its exactly reversible sampling lags are \(t_k=k\pi r/|C|\), even though its continuous-time stationary rate is \(\sigma=2C^2/(rA)>0\). On the short-foresight stable branch, the source gives \(A=(a+b)\tau+O(\tau^3)\) and \(C=-a\tau+O(\tau^3)\), so
\[
\boxed{t_1\sim \frac{\pi r}{a\tau},\qquad \sigma t_1\longrightarrow\frac{2\pi a}{a+b}>0}\quad(\tau\downarrow0).
\tag{5}
\]
The first statement is about observation-grid invisibility, not vanishing physical dissipation.

## Proof

**Step 1: nondegenerate stationary transitions.** The stationary covariance has the integral representation \(S=\int_0^\infty e^{-Bs}(2D)e^{-B^{\mathsf T}s}\,ds\), hence is positive definite. In whitened coordinates the lag innovation covariance equals
\[
Q_t=I_2-G_tG_t^{\mathsf T}=S^{-1/2}\left(\int_0^t e^{-Bs}(2D)e^{-B^{\mathsf T}s}\,ds\right)S^{-1/2}>0.
\]
Therefore the stationary joint two-time covariance \(\Sigma_t=\left(\begin{smallmatrix}I_2&G_t^{\mathsf T}\\G_t&I_2\end{smallmatrix}\right)\) is positive definite.

**Step 2: exact KL identity.** Simultaneously rotating the two whitened observations by one orthogonal matrix leaves their forward/reversed divergence invariant. Such a rotation diagonalizes the symmetric part of the real \(2\times2\) matrix \(G_t\). Hence write \(G_t=\left(\begin{smallmatrix}u&k\\-k&v\end{smallmatrix}\right)\). The reversed covariance is \(\Sigma_t^{\mathrm{rev}}=P\Sigma_tP\), where \(P\) exchanges the two two-dimensional blocks. For centered nondegenerate Gaussians,
\[
\mathcal I(t)=\tfrac12\bigl(\operatorname{tr}[(\Sigma_t^{\mathrm{rev}})^{-1}\Sigma_t]-4\bigr)
\]
because forward and reversed covariance determinants agree. Direct block inversion, valid by \(Q_t>0\), gives
\[
\operatorname{tr}[(\Sigma_t^{\mathrm{rev}})^{-1}\Sigma_t]-4
=\frac{8k^2(1-uv-k^2)}{\det(I_2-G_tG_t^{\mathsf T})}.
\]
Since \(2k=G_{t,12}-G_{t,21}\) and \(uv+k^2=\det G_t\), this is (1). Also \(\det G_t=e^{-t\operatorname{tr}B}<1\), proving strict positivity off the symmetric-transition locus. Symmetry of \(G_t\) is equivalent to \(F_tS=SF_t^{\mathsf T}\), the detailed-balance condition for the stationary sampled Gaussian kernel.

**Step 3: spectral classification without diagonalizability assumptions.** Cayley–Hamilton implies \((B-\mu I_2)^2=(\mu^2-\det B)I_2\). Therefore \(F_t=a_tI_2+b_tB\), where
\[
b_t=-e^{-\mu t}\begin{cases}
\sinh(\kappa t)/\kappa,&\det B<\mu^2,\quad\kappa=\sqrt{\mu^2-\det B},\\
t,&\det B=\mu^2,\\
\sin(\Omega t)/\Omega,&\det B>\mu^2,\quad\Omega=\sqrt{\det B-\mu^2}.
\end{cases}
\]
Whitening yields \(G_t=a_tI_2+b_tK\); hence \(G_{t,12}-G_{t,21}=b_t\Delta\). The continuous-time process satisfies detailed balance if and only if its stationary current \((DS^{-1}-B)x\,\pi(x)\) vanishes, equivalently \(BS=SB^{\mathsf T}\), equivalently \(K=K^{\mathsf T}\) or \(\Delta=0\). If it is irreversible, \(\Delta\ne0\) and (1) vanishes precisely at the positive zeros of \(b_t\). The first two branches have no positive zeros; the oscillatory branch has exactly (2). Substituting the sine zeros into the matrix exponential yields the scalar form of \(F_{t_k}\) and thus reversibility of the entire equally spaced stationary Gaussian Markov chain.

**Step 4: quadratic local profile.** In the oscillatory branch, \(b_{t_k+h}=(-1)^{k+1}e^{-\mu t_k}h+O(h^2)\). At the zero, \(G_{t_k}=(-1)^ke^{-\mu t_k}I_2\); hence \(\det(I_2-G_{t_k}G_{t_k}^{\mathsf T})=(1-q_{t_k})^2\). Inserting these expansions into (1) gives (3), including its strictly positive coefficient.

**Step 5: specialization and physical dissipation.** For the rotational drift and isotropic noise, the stationary covariance is \(S=(d/\alpha)I_2\), and \(G_t=e^{-\alpha t}\left(\begin{smallmatrix}\cos(\omega t)&\sin(\omega t)\\-\sin(\omega t)&\cos(\omega t)\end{smallmatrix}\right)\), up to orientation. Formula (1) immediately gives (4). Independently, the stationary probability current is the rotational field \(-\omega Jx\,\pi(x)\) (with \(J\) the planar rotation matrix), so the continuous-time entropy-production rate computed from \(\int j^{\mathsf T}(D\pi)^{-1}j\,dx\) is \(2\omega^2/\alpha\). Finally insert Dey's explicit symmetric-branch matrix and the paper's short-foresight coefficients to get (5).

## Verification

Run `python verify.py` with the package's `requirements.txt`. The program independently evaluates relative entropy from the two \(4\times4\) joint Gaussian covariance matrices (rather than from formula (1)), compares it with the claimed closed form for hundreds of randomly generated stable drift/diffusion pairs, checks zero-lag transitions for anisotropic diffusion matrices, tests the quadratic coefficient near these zeros, confirms the isotropic trigonometric expression and small-lag physical rate, and tests a real-eigenvalue example. Its recorded run completed 2,120 floating-point assertions and sign checks. The proof above is algebraic and does not rely on numeric sampling. Verification tests are finite and do not certify global originality.

## Relationship to prior work

Dey (arXiv:2610.30189v1, 2026) derives the two-agent Nash-induced OU drift, stationary covariance, probability current and continuous-time entropy production; its Section 5 and appendices identify the symmetry-compatible conformist–contrarian branch and its small-planning-time coefficients. It does not derive the finite-lag reversed-pair relative entropy, complete invisible-lag classification, or the product limit in (5). The presently studied lag is an observation choice, not a new Nash equilibrium.

Nagayama, Kolchinsky and Ito (arXiv:2606.07263, 2026) derive the established oscillatory/nonnormal decomposition of continuous-time OU entropy production, so the existence of circulating OU currents and oscillatory spectra is not claimed as new. Their observable is steady-state physical entropy-production rate; the present exact *sampled two-time KL* and its vanishing times are different and are not a direct consequence of that rate alone.

Bauer, Seifert and van der Meer (arXiv:2412.15642, 2024) establish stroboscopic generator identifiability issues and entropy-production inference for finite-state Markov networks; their work is especially relevant conceptual prior art on sampling aliases and complex eigenvalues. The present statement is a diffusion-specific exact Gaussian divergence and **if-and-only-if** classification for all positive-definite planar noise, including defective real drifts and a quadratic information-recovery profile. The general stroboscopic alias phenomenon itself is therefore not claimed as new.

Lucente, Baldassarri, Puglisi, Vulpiani and Viale (Phys. Rev. Research, 2022) establish that any stationary *scalar* Gaussian observation is time reversible even when the underlying multidimensional system dissipates. That projection-induced invisibility is different from the present full-two-coordinate, unprojected, *cadence-specific* exact reversibility. We do not claim scalar-Gaussian invisibility as a new phenomenon.

## Limitations

The classification uses full-state stationary observations of a two-dimensional linear diffusion with constant positive-definite noise. It does not extend as stated to partial observation, measurement error, nonstationary initialization, higher-dimensional dynamics, degenerate noise, nonlinear drifts, or a time-reversal operation that flips odd dynamical coordinates. A zero of the sampled KL means that the **sampled** Markov law is reversible; it does not imply that the continuous-time path law is reversible or dissipates no entropy. The quoted two-agent short-foresight conclusions are conditional on the stabilizing symmetry-compatible Nash branch established in the motivating paper and do not prove global uniqueness of game equilibria. The literature comparison supports a qualified best-knowledge novelty assessment, not independent priority certification.

## References

1. A. Dey, *Foresight-dependent entropy production in stochastic two-agent dynamics*, arXiv:2610.30189v1, first publicly submitted 20 October 2026. https://arxiv.org/html/2610.30189v1
2. R. Nagayama, A. Kolchinsky and S. Ito, *Oscillatory-nonnormal decomposition of dissipation in Ornstein-Uhlenbeck processes*, arXiv:2606.07263, first publicly submitted 5 June 2026. https://arxiv.org/abs/2606.07263
3. M. T. Bauer, U. Seifert and J. van der Meer, *Stroboscopic measurements in Markov networks: Exact generator reconstruction vs. thermodynamic inference*, arXiv:2412.15642, first publicly submitted 20 December 2024. https://arxiv.org/abs/2412.15642
4. F. A. Cisneros, N. Fakhri and J. M. Horowitz, *Dissipative timescales from coarse-graining irreversibility*, J. Stat. Mech. 073201 (2023), arXiv:2305.16197. https://arxiv.org/abs/2305.16197
5. D. Lucente, A. Baldassarri, A. Puglisi, A. Vulpiani and M. Viale, *Inference of time irreversibility from incomplete information: Linear systems and its pitfalls*, Phys. Rev. Research 4, 043103 (2022). https://doi.org/10.1103/PhysRevResearch.4.043103
