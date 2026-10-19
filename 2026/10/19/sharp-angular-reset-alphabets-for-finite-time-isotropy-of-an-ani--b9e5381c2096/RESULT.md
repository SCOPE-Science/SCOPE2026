# Sharp angular-reset alphabets for finite-time isotropy of an anisotropic Brownian colloid

## Finding

Consider a passive planar anisotropic Brownian particle whose position is never reset, but whose orientation undergoes Poisson resetting to an independently sampled *unoriented axis*. Exact isotropy of displacement tensors through a prescribed even order requires, and is implied by, the vanishing of precisely the corresponding initial Fourier coefficients of the reset-axis distribution. In particular, the minimum number of distinct reset axes needed for directional moments through order \(2m\) to be isotropic at **every positive observation time** is \(m+1\). Every size-minimal protocol is, up to common rotation and relabeling, uniform on the regular \((m+1)\)-gon of unoriented axes.

Here is the exact statement. Let \(D_{\rm rot},r,d_0>0\), \(0<|\delta|<d_0\), and let \(\nu\) be an arbitrary probability distribution on the circle of unoriented axes \(\mathbb R/\pi\mathbb Z\). An angular process \(\theta_t\) undergoes Brownian rotation with generator \(D_{\rm rot}\partial_\theta^2\) and, independently at rate \(r\), replaces \(\theta\) by an independent draw from \(\nu\). Initialize \(\theta_0\) in its unique stationary law \(\pi\). With a two-dimensional Brownian motion \(W\) independent of the entire angular dynamics, define \(X_0=0\) and
\[
 dX_t=\sqrt{2\mathsf D(\theta_t)}\,dW_t,\qquad
 \mathsf D(\theta)=d_0 I_2+\delta
 \begin{pmatrix}\cos(2\theta)&\sin(2\theta)\\\sin(2\theta)&-\cos(2\theta)\end{pmatrix}.
\]
The positive matrix square root is used; \(d_0>|\delta|\) ensures uniform ellipticity. For unit direction \(u_\varphi=(\cos\varphi,\sin\varphi)\), put \(Z_\varphi(t)=u_\varphi\cdot X_t\), and \(\nu_j=\int e^{2ij\theta}\nu(d\theta)\). For each fixed integer \(m\ge1\), the following conditions are equivalent:

1. For every \(t>0\) and every \(1\le k\le m\), the moment \(\mathbb E[Z_\varphi(t)^{2k}]\) is independent of \(\varphi\).
2. \(\nu_1=\nu_2=\cdots=\nu_m=0\).

Every odd spatial moment is zero, so the first condition is equivalent to rotational invariance of all spatial moment tensors of total order at most \(2m\), at every \(t>0\). For a reset law supported on \(N\) distinct axes, these equivalent conditions imply \(N\ge m+1\). Equality holds precisely for
\[
\nu=\frac1{m+1}\sum_{j=0}^{m}\delta_{\theta_*+j\pi/(m+1)}\quad\text{on }\mathbb R/\pi\mathbb Z.
\]
Consequently no protocol supported on finitely many axes can make every spatial moment isotropic at all positive times.

The order-four diagnostic is explicit. Assume \(\nu_1=0\), and define
\[
\omega=r+4D_{\rm rot},\qquad
\zeta=\frac{r}{r+16D_{\rm rot}}\nu_2,\qquad
H(t)=\frac{t}{\omega}-\frac{1-e^{-\omega t}}{\omega^2}>0.
\]
Then the variance and fourth cumulant of the directional displacement satisfy, for all \(t>0\),
\[
\operatorname{Var}(Z_\varphi(t))=2d_0t,\qquad
\operatorname{cum}_4(Z_\varphi(t))=
12\delta^2H(t)\left[1+\operatorname{Re}(\zeta e^{-4i\varphi})\right].
\]
Thus covariance isotropy need not imply fourth-order isotropy. Under the unique three-axis minimal protocol for \(m=2\), the fourth cumulant is isotropic but strictly positive, \(12\delta^2H(t)\), despite isotropic covariance. For its axes \(\theta_*+j\pi/3\), even the sixth moment reveals its residual symmetry: as \(t\downarrow0\), the *direction-dependent component* of \(\mathbb E[Z_\varphi(t)^6]\) is
\[
30\delta^3\frac{r}{r+36D_{\rm rot}}t^3\cos\bigl(6(\varphi-\theta_*)\bigr)+o(t^3),
\]
where the remainder is uniform in \(\varphi\). In particular the difference between sixth moments in directions \(\theta_*\) and \(\theta_*+\pi/6\) equals
\[
60\delta^3\frac{r}{r+36D_{\rm rot}}t^3+o(t^3).
\]

## Assumptions and scope

The particle is passive; there is no self-propulsion, interaction, confining force, or spatial resetting. Orientations are modulo \(\pi\), because an anisotropic Brownian rod is invariant under axis reversal. Resets choose **absolute** axes independently from the same law \(\nu\), rather than rotating the previous orientation by a random increment. Rotational and translational Brownian noises and the Poisson process are independent. Initial orientation is sampled from the stationary distribution; without stationary initialization, the Fourier-vanishing criterion for all times requires an additional condition on the initial law. The parameters satisfy \(D_{\rm rot},r,d_0>0\) and \(0<|\delta|<d_0\); \(\delta=0\) is excluded because isotropy then holds regardless of the resetting protocol. All direction-dependent moments mentioned here are moments of the unconditional displacement distribution, with averaging over all rotational and translational noise and reset angles. The claims concern finite-time moments and not finite-time equality of the full displacement law with a rotationally invariant law.

## Proof

**Step 1: stationary angular harmonics and the Gaussian-mixture representation.** For integer \(n\), set \(\nu_n=\int e^{2in\theta}\nu(d\theta)\) and similarly \(\pi_n\). Applying the stationary angular generator to \(e^{2in\theta}\) yields
\[
\pi_0=1,\qquad \pi_n=\frac{r}{r+4n^2D_{\rm rot}}\nu_n\quad(n\ne0).
\]
The rotational Brownian motion on the compact axis circle has a unique stationary law; resetting preserves ergodicity. For a fixed full angular path the directional displacement is a centered Gaussian of variance
\[
 2\bigl(d_0t+\delta A_\varphi(t)\bigr),\qquad
 A_\varphi(t)=\int_0^t\cos\bigl(2(\theta_s-\varphi)\bigr)\,ds.
\]
Since \(|A_\varphi(t)|\le t\), this is positive. Hence, for every integer \(k\ge1\),
\[
 \mathbb E[Z_\varphi(t)^{2k}]=(2k-1)!!\,2^k\,
 \mathbb E\left[(d_0t+\delta A_\varphi(t))^k\right]. \tag{1}
\]
Conditioned odd moments vanish; the same holds without conditioning.

**Step 2: necessity.** Angular paths are right-continuous and \(A_\varphi(t)/t\to\cos(2(\theta_0-\varphi))\) almost surely as \(t\downarrow0\). Bounded convergence in (1) implies that isotropy of the order-\(2k\) moment for all \(t>0\) forces the function
\[
 \varphi\longmapsto\int\bigl[d_0+\delta\cos(2(\theta-\varphi))\bigr]^k\pi(d\theta)
\]
to be constant. The coefficient of \(e^{-2ik\varphi}\) in its Fourier expansion is \((\delta/2)^k\pi_k\), since that is the sole degree-\(k\) contribution to the top harmonic. Thus \(\pi_k=0\), and consequently \(\nu_k=0\), for each \(1\le k\le m\).

**Step 3: sufficiency for every positive time.** To avoid replacing a finite-time statement with a small-time argument, set
\[
 U_{j,n}(t,\varphi)=\mathbb E\left[A_\varphi(t)^j e^{2in\theta_t}\right]
\]
for nonnegative \(j\), integer \(n\), and \(j+|n|\le m\). The Markov generator and the chain rule give a closed finite triangular system
\[
\begin{aligned}
\dot U_{j,n}={}&-(r+4n^2D_{\rm rot})U_{j,n}+r\nu_n U_{j,0}\\
&+\frac j2\left(e^{-2i\varphi}U_{j-1,n+1}+e^{2i\varphi}U_{j-1,n-1}\right),
\end{aligned}\tag{2}
\]
where the last line is absent for \(j=0\); \(U_{0,n}(0,\varphi)=\pi_n\), and \(U_{j,n}(0,\varphi)=0\) for \(j>0\). All appearing index pairs remain within \(j+|n|\le m\). Suppose \(\nu_1=\cdots=\nu_m=0\). By conjugation the same holds for negative indices. Therefore for \(n\ne0\) in this finite system the inhomogeneous resetting term vanishes. Inducting on \(j\) in (2), uniqueness of the linear ODE gives
\[
U_{j,n}(t,\varphi)=e^{2in\varphi}c_{j,n}(t),\qquad j+|n|\le m,
\]
with coefficients independent of \(\varphi\). The claim starts at \(j=0\), where \(U_{0,0}=1\) and \(U_{0,n}=0\) for nonzero \(|n|\le m\). In the induction, each forcing term has the indicated phase, and for \(n=0\) the resetting term is \(rU_{j,0}\). In particular \(U_{j,0}=\mathbb E[A_\varphi(t)^j]\) is angle-independent for every \(j\le m\) and \(t\ge0\). Equation (1) proves all the required directional moment isotropies. A symmetric tensor in two dimensions is determined by its contractions against repeated unit directions, so the directional statement is equivalent to rotational invariance of all spatial moment tensors through order \(2m\).

**Step 4: sharp support and equality.** If \(\nu\) has atoms \(z_\ell=e^{2i\theta_\ell}\) with weights \(w_\ell>0\), \(\ell=1,\ldots,N\), then the Hermitian Toeplitz matrix with indices \(j,k\in\{0,\ldots,m\}\) obeys
\[
T_{jk}=\nu_{j-k}=\delta_{jk}=\sum_{\ell=1}^N w_\ell z_\ell^j\overline{z_\ell^k}.
\]
It is the identity matrix of rank \(m+1\), but is also the sum of \(N\) rank-one positive semidefinite matrices. Therefore \(N\ge m+1\). If equality holds, the square matrix \(B_{j\ell}=\sqrt{w_\ell}\,z_\ell^j\) is unitary. Its column norms give \((m+1)w_\ell=1\), and for distinct \(\ell,h\), orthogonality gives
\[
\sum_{j=0}^m(z_\ell\overline{z_h})^j=0.
\]
Each ratio is therefore a nontrivial \((m+1)\)-st root of unity. The nodes form a rotated complete regular \((m+1)\)-gon with equal weights. Conversely this protocol kills all harmonics \(1\le j\le m\). If a finite-alphabet protocol killed *every* positive harmonic, the rank argument for arbitrary \(m\) would require arbitrarily many axes, a contradiction.

**Step 5: the fourth cumulant.** If \(\nu_1=0\), then \(\pi_1=0\) and the angular semigroup applied to \(\cos(2(\theta-\varphi))\) decays as \(e^{-\omega s}\). Stationarity and \(\cos^2 x=(1+\cos(2x))/2\) give
\[
\operatorname{Cov}\left(\cos 2(\theta_0-\varphi),\cos 2(\theta_s-\varphi)\right)
=\frac12 e^{-\omega s}\left[1+\operatorname{Re}(\pi_2e^{-4i\varphi})\right].
\]
Double integration in time yields
\[
\operatorname{Var}(A_\varphi(t))=H(t)\left[1+\operatorname{Re}(\pi_2e^{-4i\varphi})\right],
\]
where \(H(t)=\int_0^t(t-s)e^{-\omega s}ds>0\). Conditional Gaussian moments imply \(\operatorname{cum}_4(Z)=3\operatorname{Var}(\operatorname{Var}(Z\mid\theta))=12\delta^2\operatorname{Var}(A_\varphi)\). Substituting \(\pi_2=\zeta\) proves the formula. Under the three-axis protocol \(\nu_2=0\), so the cumulant is strictly positive, proving that even its fourth-order-isotropic displacement is not Gaussian.

**Step 6: sixth-order leakage.** For the three-axis protocol, \(\nu_1=\nu_2=0\) and \(\nu_3=e^{6i\theta_*}\), whence \(\pi_3=[r/(r+36D_{\rm rot})]e^{6i\theta_*}\). By the right-continuity used in Step 2,
\[
\mathbb E[Z_\varphi(t)^6]=120t^3\int[d_0+\delta\cos(2(\theta-\varphi))]^3\pi(d\theta)+o(t^3)
\]
uniformly in \(\varphi\): the bound \(|A_\varphi(t)|/t\le1\) permits uniform control since the dependence on direction is a finite trigonometric polynomial. All nonconstant harmonics except the third vanish. Using \(\cos^3 x=(3\cos x+\cos 3x)/4\), the third-harmonic coefficient is \(120(\delta^3/4)\pi_3=30\delta^3\pi_3\). The displayed sixth-moment asymptotic and directional difference follow.

## Verification

A standalone Python program at `checks/angular_reset_checks.py` computes the exact finite triangular system (2) by high-accuracy ODE integration, independently extracts conditional-Gaussian even moments, and compares them with the fourth-cumulant identity. It also checks the sixth-moment asymptotic for the three-axis protocol and numerical Toeplitz identities for regular protocols through eight axes. It requires Python 3.10+, NumPy and SciPy and is run as `python checks/angular_reset_checks.py`. The completed program passed 103 numerical/algebraic assertions, including direction-by-direction checks at several positive times. This is reproducibility evidence, not a computer-assisted infinite proof; finite numerical tolerances and the approximate sixth-moment limiting test do not establish the general statements. The six analytic steps above supply the proof.

## Relationship to prior work

Chaki, Olsen and Löwen, *Anisotropic Brownian particles under resetting* (2024), formulate precisely the passive anisotropic translational Brownian and rotational dynamics and analyze orientational resetting to a **single predetermined angle** (Section V). They calculate second moments and long-time diffusion, not the all-orders finite-time equivalence for an arbitrary reset-axis law, the sharp alphabet classification, or the fourth-cumulant/sixth-harmonic diagnostics given here. Baouche and collaborators (2024) set out an orientational renewal formulation admitting a general resetting-angle law, but explicitly specialize their active swimmer with isotropic translational diffusion to a single reset direction and identify the angle-law generalization as a further question. Ghosh and Mandal (2025) investigate an **active** anisotropic swimmer with a fixed-angle reset and provide spatial second-moment analysis, not this passive finite-order isotropy result. Peherstorfer (2010) develops positive trigonometric quadrature and unit-circle moment formulas. The Toeplitz rank argument and regular-node extremizers are instances of established harmonic moment/quadrature theory; the static quadrature principle is **not** asserted as novel. Its connection to exact finite-time spatial moment isotropy, including the angular semigroup equivalence and non-Gaussian cumulant consequences, is the assessed contribution.

## Limitations

The statement depends on stationarity of the initial angle, Poisson resetting to independent absolute axes, nonzero diffusivity anisotropy, and the specific passive Gaussian-noise model. It does not claim a finite alphabet makes the *entire distribution* isotropic, nor that zero fourth cumulant implies Gaussianity. For the minimal three-axis design the fourth cumulant remains positive and sixth anisotropy is provable at sufficiently short times. The finite-time all-orders isotropy claim is an equivalence, not a claim that any finite alphabet achieves all orders. No microscopic hydrodynamic couplings or self-propulsion are modeled. Existing trigonometric quadrature theory gives the static support lemma, and a general result on Markov additive functionals may contain an implicit version of the dynamic equivalence; this is a residual originality risk requiring independent review. No independent scientific audit or certified error bounds for numerical ODE solutions have been performed.

## References

1. Subhasish Chaki, Kristian Stølevik Olsen, and Hartmut Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550, first publicly posted 25 June 2024, especially Section V, https://arxiv.org/html/2406.17550v2 .
2. Yanis Baouche, Thomas Franosch, Matthias Meiners, and Christina Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769, 2024, especially Sections II.1, II.4, and IV; its general reset-angle notation is specialized to a fixed direction for the reported results, https://arxiv.org/html/2405.06769v1 .
3. Anirban Ghosh and Sudipta Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149, 2025, especially orientational resetting, https://arxiv.org/html/2501.05149v1 .
4. Franz Peherstorfer, *Positive trigonometric Quadrature Formulas and quadrature on the unit circle*, arXiv:1001.2451, 2010, especially the unit-circle Fourier moment conditions in the introduction, https://arxiv.org/abs/1001.2451 .
