# Periodically reoriented colloids: an exact fluctuation tensor and a universal peak of coupling-induced anisotropy

## Finding

For a two-dimensional freely diffusing colloid with nonzero translation–rotation hydrodynamic coupling, periodic resetting of orientation (but not position) yields a closed, exact long-time spatial covariance-growth tensor. This tensor supplements the known mean transport law. Unexpectedly, even when the *unreset translational mobility block is isotropic*, coupling to the rotating degree of freedom creates a strictly positive, drift-aligned anisotropy in the centered dispersion. The anisotropy has exactly one optimal nonzero reset period.

Write the symmetric positive-definite body-frame mobility as
\[
\mu=\begin{pmatrix}K&h\\h^{\mathsf T}&m\end{pmatrix},\qquad
K=K^{\mathsf T}\in\mathbb R^{2\times2},\quad h\in\mathbb R^2,\quad m>0,
\]
and put \(\Theta=k_{\mathrm B}T>0\), \(D_r=\Theta m\), \(E=K-hh^{\mathsf T}/m\succ0\). Let \(R(\phi)\) denote a planar counterclockwise rotation, \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), \(\phi_0\) the reset angle, \(\tau>0\) the reset period, \(z=D_r\tau\), and
\[
a=R(\phi_0)(-Jh/m).
\]

Denote the laboratory position by \(X_t\in\mathbb R^2\). Then
\[
\frac{X_t}{t}\longrightarrow v_\tau=\frac{e^{-z}-1}{\tau}\,a\quad\text{almost surely},
\]
and
\[
\frac{X_t-v_\tau t}{\sqrt t}\ \Longrightarrow\ \mathcal N(0,\Gamma_\tau),
\]
where the exact covariance-growth matrix is
\[
\boxed{\displaystyle
\begin{aligned}
\Gamma_\tau={}&\frac{1}{\tau}\left[
\frac{|a|^2(1-e^{-4z})}{2}I_2+(e^{-4z}-e^{-2z})aa^{\mathsf T}\right]\\
&+2\Theta\left[
\frac{\operatorname{tr}E}{2}I_2+
\frac{1-e^{-4z}}{4z}R(\phi_0)
\left(E-\frac{\operatorname{tr}E}{2}I_2\right)
R(\phi_0)^{\mathsf T}\right].
\end{aligned}}
\]
In particular,
\[
\operatorname{tr}\Gamma_\tau
=2\Theta\operatorname{tr}E+
\frac{|a|^2}{\tau}(1-e^{-2z}).
\]

**Isotropic-translation special case and sharp optimum.** Suppose \(K=kI_2\), \(h\ne0\), and \(k>|h|^2/m\). Let \(e=a/|a|\) and \(e_\perp=Je\). These are principal axes of \(\Gamma_\tau\), and the centered longitudinal–transverse covariance-growth gap is
\[
\boxed{\displaystyle
\Delta_\tau:=e^{\mathsf T}\Gamma_\tau e
-e_\perp^{\mathsf T}\Gamma_\tau e_\perp
=\frac{|h|^2}{2m^2\tau}(1-e^{-2D_r\tau})^2>0.}
\]
It has a unique maximizer \(\tau_*=z_*/D_r\), where \(z_*\approx0.628215604313\) is the **unique strictly positive** solution of \(e^{2z}=1+4z\). At that period,
\[
\boxed{\displaystyle
\Delta_{\max}=0.407264377589\ldots\,\frac{D_r|h|^2}{m^2}.}
\]
As \(\tau\downarrow0\), \(\Delta_\tau\sim2|h|^2D_r^2\tau/m^2\); as \(\tau\uparrow\infty\), \(\Delta_\tau\sim |h|^2/(2m^2\tau)\). This is an optimum for *anisotropy of centered diffusion*, not necessarily for sorting velocity, separation fidelity, or a signal-to-noise objective.

## Assumptions and scope

The mobility \(\mu\) is constant in the **body** frame, real, symmetric and strictly positive definite. Between consecutive resetting instants \(n\tau\), \(n\in\mathbb N\), the laboratory coordinates \((X,\phi)\) obey the overdamped, force-free Stratonovich Langevin system from the colloidal setup of Cleuren–Eichhorn:
\[
\begin{pmatrix}dX_t\\d\phi_t\end{pmatrix}
=\sqrt{2\Theta}\,\begin{pmatrix}R(\phi_t)&0\\0&1\end{pmatrix}\mu^{1/2}\circ dW_t^{(3)}.
\]
The orientation is reset instantaneously to the same deterministic \(\phi_0\) at every \(n\tau\), while the spatial coordinate is continuous and never reset. Fresh independent Brownian increments act during each cycle. The initial orientation is \(\phi_0\); an arbitrary fixed initial position makes no difference to the limits. Angular coordinates may be understood modulo \(2\pi\). No background force, active propulsion, interparticle interactions, or reset-duration cost is included. All matrix expressions use laboratory Cartesian coordinates.

The normal limit uses the standard convention that \(\Gamma_\tau=\lim_{t\to\infty}t^{-1}\operatorname{Cov}(X_t)\), i.e. twice the effective diffusion tensor under the common \(\operatorname{Cov}(X_t)\sim2D_{\mathrm{eff}}t\) convention.

## Proof

**Step 1: independent noise decomposition and an exact bounded displacement component.** Since \(\mu\succ0\), its Schur complement \(E=K-hh^{\mathsf T}/m\) is strictly positive definite. A Gaussian covariance factorization realizes the Langevin system, on one reset interval, with independent standard planar and scalar Brownian motions \(W^\perp,B\) as
\[
\begin{aligned}
d\phi_t&=\sqrt{2D_r}\,dB_t,\\
dX_t&=\Theta R(\phi_t)Jh\,dt
+\frac{R(\phi_t)h}{m}\,d\phi_t
+\sqrt{2\Theta}\,R(\phi_t)E^{1/2}\,dW_t^\perp.
\end{aligned}
\]
The displayed equations are in Itô form; the translational Itô drift \(\Theta R(\phi)Jh\) is precisely the Stratonovich-to-Itô correction. Define \(F(\phi)=R(\phi)(-Jh/m)\). Because \(F'(\phi)=R(\phi)h/m\) and \(F''(\phi)=-F(\phi)\), Itô's formula gives
\[
dF(\phi_t)=\frac{R(\phi_t)h}{m}\,d\phi_t-D_rF(\phi_t)\,dt
=\frac{R(\phi_t)h}{m}\,d\phi_t+\Theta R(\phi_t)Jh\,dt.
\]
Thus, on a complete reset cycle,
\[
Y:=X_\tau-X_0=F(\phi_\tau)-F(\phi_0)+M_\tau,
\qquad
M_\tau=\sqrt{2\Theta}\int_0^\tau R(\phi_s)E^{1/2}\,dW_s^\perp.
\]
The two pieces are uncorrelated: conditional on the entire angular Brownian path, \(\mathbb E[M_\tau\mid\phi_\cdot]=0\). The angular term is bounded, and the martingale has finite moments of every order for fixed \(\tau\).

**Step 2: mean and covariance of one increment.** With \(\phi_t=\phi_0+\sqrt{2D_r}B_t\), the first and second Fourier harmonics have expectations \(e^{-D_rt}\) and \(e^{-4D_rt}\). In particular \(\mathbb E F(\phi_\tau)=e^{-z}a\), so
\[
\mathbb EY=(e^{-z}-1)a.
\]
For any symmetric planar matrix \(H\), harmonic averaging yields
\[
\mathbb E[R(\phi_s)H R(\phi_s)^{\mathsf T}]
=\frac{\operatorname{tr}H}{2}I_2+
 e^{-4D_rs}R(\phi_0)
\left(H-\frac{\operatorname{tr}H}{2}I_2\right)R(\phi_0)^{\mathsf T}.
\]
The angle-induced endpoint displacement has exact covariance
\[
\operatorname{Cov}(F(\phi_\tau))
=\frac{|a|^2(1-e^{-4z})}{2}I_2+
(e^{-4z}-e^{-2z})aa^{\mathsf T}.
\]
The martingale Itô isometry, conditional zero-mean property and preceding harmonic average yield
\[
\operatorname{Cov}(M_\tau)=2\Theta\left[
\frac{\tau\operatorname{tr}E}{2}I_2+
\frac{1-e^{-4z}}{4D_r}R(\phi_0)
\left(E-\frac{\operatorname{tr}E}{2}I_2\right)R(\phi_0)^{\mathsf T}\right].
\]
Adding the two covariances and dividing by \(\tau\) proves the stated \(\Gamma_\tau\), including the trace identity. Positive definiteness follows from \(E\succ0\).

**Step 3: long-time limit theorems.** Resetting restores the same orientation, and increments of the driving Brownian motions after deterministic times are independent. Therefore complete-cycle displacements \(Y_1,Y_2,\dots\) are identically distributed and independent. The strong law and multivariate iid central limit theorem give the drift and covariance-growth result at multiples of \(\tau\). For an arbitrary time \(t=n\tau+s\), \(0\le s<\tau\), the remaining partial-cycle displacement has a uniformly bounded fourth moment (bounded \(F\) plus a Brownian integral with uniformly bounded coefficients). It is \(o_{\mathbb P}(\sqrt t)\); by a maximal fourth-moment estimate and Borel–Cantelli, it is \(o(t)\) almost surely. Consequently the stated limits hold for all real \(t\to\infty\).

**Step 4: induced anisotropy and unique optimum.** If \(K=kI_2\), then \(E=kI_2-hh^{\mathsf T}/m\). Since \(a\) is perpendicular to the lab-frame vector \(R(\phi_0)h\), the orthonormal pair \((e,e_\perp)\) diagonalizes both traceless covariance contributions. Their directional difference simplifies to
\[
\begin{aligned}
\Delta_\tau
&=\frac{|a|^2}{\tau}(e^{-4z}-e^{-2z})
+\frac{\Theta|h|^2}{2mD_r\tau}(1-e^{-4z})\\
&=\frac{|a|^2}{2\tau}(1-2e^{-2z}+e^{-4z}),
\end{aligned}
\]
using \(D_r=\Theta m\) and \(|a|^2=|h|^2/m^2\). The formula shows positivity for every finite \(\tau>0\). After setting \(z=D_r\tau\), maximizing \(\Delta_\tau\) reduces to maximizing \(f(z)=(1-e^{-2z})^2/z\) over \(z>0\). Elementary differentiation gives \(f'(z)=0\) exactly when \(e^{2z}=1+4z\). The function \(g(z)=e^{2z}-1-4z\) is strictly convex, has \(g(0)=0\), \(g'(0)=-2<0\), and tends to \(+\infty\), hence has exactly one positive root. Since \(f(z)\to0\) at both endpoints and its derivative changes sign from positive to negative at that root, this root is the unique global maximum. The asymptotic endpoint expansions and the displayed numerical coefficients follow directly.

## Verification

The standalone script `verify_transport.py` reproduces the closed covariance formula, tests the isotropic-block gap, positivity and trace identities on a finite parameter grid, and finds the unique positive optimizer numerically. It also simulates the *independent Brownian decomposition*, rather than applying a numerically ambiguous correlated-noise discretization. Using 90,000 simulated cycles of a nonsingular example mobility, the cycle drift and covariance agree with the analytic expressions at sampling precision. The script reports 56 exact/tolerance-controlled matrix and optimization identities, plus finite Monte Carlo diagnostics. The asymptotic LLN and CLT and the global maximization are proved above; finite simulations do not independently certify them.

For one example with \(\Theta=4\), \(m=0.02501\), \(\tau=0.1\), \(\phi_0=0\), \(K=\left(\begin{smallmatrix}0.05962&0.002094\\0.002094&0.05494\end{smallmatrix}\right)\) and \(h=(-0.001775,-0.002674)^{\mathsf T}\), the analytic covariance growth is approximately
\[
\Gamma_\tau=\begin{pmatrix}0.47658030&0.01640636\\0.01640636&0.43986696\end{pmatrix}.
\]
To reproduce from this package: install the two entries in `requirements.txt`, then run `python verify_transport.py`.

## Relationship to prior work

Cleuren and Eichhorn [1] introduce this periodically orientation-reset planar colloid with full translation–rotation hydrodynamic mobility and determine its mean drift, precisely the first-moment formula recovered in Step 2. They also identify second moments and selective diffusion enhancement as a prospective use of the scheme. Their analysis does not state the centered covariance-growth tensor, the isotropic-translational-block anisotropy formula, or the nonzero unique optimum found here.

Chaki, Olsen and Löwen [2], notably Secs. II and V, calculate an effective anisotropic diffusion tensor under **Poisson** orientational resetting, but their model assumes independent body-frame translational and rotational Brownian drivers, with no off-diagonal translation–rotation mobility vector. Their anisotropy is induced by anisotropic **translational** mobilities. The special case here has an isotropic translational block \(K=kI_2\) but nonzero cross mobility \(h\); therefore it is not included in their independent-noise formulation. Earlier unreset boomerang-colloid studies [3] treat hydrodynamic translation–rotation coupling without this periodic resetting protocol. Standard Gaussian covariance decomposition and iid limit theorems are used as tools, not claimed as novel mathematics.

## Limitations

The theorem assumes a force-free constant body-frame SPD mobility, a deterministic fixed-period perfect orientation reset to one angle, no spatial jump on reset, and no hydrodynamic interactions between particles. The covariance limit is centered around the drift: uncentered second moments also include ballistic growth. The optimum concerns only the difference of the two covariance-growth eigenvalues when the bare translational block is isotropic; it does **not** optimize mean drift, absolute dispersion, sorting error, cost, or finite-horizon classification. For a generic anisotropic \(K\), the exact tensor remains valid but the simple universal optimum need not persist. The finite verification script is not a proof of the limit theorems. Possible unexamined literature on general periodic Markov-additive functionals or hydrodynamic colloids may rederive portions of these formulas.

## References

[1] B. Cleuren and R. Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1 (first public 19 March 2026), https://arxiv.org/abs/2603.19430 and full text https://arxiv.org/html/2603.19430v1 .

[2] S. Chaki, K. Stølevik Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v2 (2024), https://arxiv.org/html/2406.17550v2 .

[3] S. Chakrabarty et al., *Brownian Motion of Arbitrarily Shaped Particles in Two Dimensions*, arXiv:1410.6057 (2014), https://arxiv.org/abs/1410.6057 .
