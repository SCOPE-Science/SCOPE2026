# Sharp drift–isotropy synthesis for orientationally reset active Brownian particles

## Finding

A planar active Brownian particle can have a **strictly nonzero directed mean velocity and exactly isotropic centered displacement covariance at every positive observation time**. For arbitrary independently sampled reset angles, the complete attainable effective-diffusivity tensors at any prescribed mean velocity form an explicit closed disk. The disk determines a sharp maximum directed speed compatible with isotropic fluctuations and a transition between symmetric and antipodal optimal reset protocols at the dimensionless resetting rate \(\lambda/D_{\rm rot}=1/2\).

Let \(v>0\), \(D_{\rm rot}>0\), \(\lambda>0\), \(D\ge0\), and put
\[
 t=\frac{\lambda}{D_{\rm rot}},\qquad a=\frac{t}{1+t},\qquad b=\frac{t}{4+t},\qquad k=D_{\rm rot}+\lambda.
\]
For a probability measure \(\nu\) of absolute resetting orientations on the unit circle, write \(\mu=\int e^{i\theta}\,d\nu(\theta)\) and \(\eta=\int e^{2i\theta}\,d\nu(\theta)\). Identify complex numbers with planar vectors, and define \(H(z)=\left(\begin{smallmatrix}\Re z&\Im z\\\Im z&-\Re z\end{smallmatrix}\right)\). With stationary angular initialization, the mean displacement is \(vT a(\Re\mu,\Im\mu)\), while
\[
 \operatorname{Cov}(X_T-X_0)
 =2DT I_2+v^2\,G_k(T)\left[(1-a^2|\mu|^2)I_2+H(b\eta-a^2\mu^2)\right],
 \qquad G_k(T)=\frac{T}{k}-\frac{1-e^{-kT}}{k^2}.
\]
In particular, the long-time effective diffusion tensor is
\[
 K=D I_2+\frac{v^2}{2k}\left[(1-a^2|\mu|^2)I_2+H(b\eta-a^2\mu^2)\right].
\]

**Exact attainability.** At any prescribed \(\mu\) with \(|\mu|\le1\), the traceless coefficient \(z=b\eta-a^2\mu^2\) ranges over precisely
\[
 \boxed{\quad |z-(b-a^2)\mu^2|\le b(1-|\mu|^2).\quad}
\]
Every disk boundary point is realized by a reset law supported on at most two angles; every interior point is realized with at most four angles. Thus the display is a complete, constructive characterization, not merely an inequality.

**Sharp isotropic-drift threshold.** Put
\[
 q_*(t)=\frac{b}{b+|b-a^2|},\qquad s_*(t)=v a\sqrt{q_*(t)}.
\]
For any prescribed mean drift vector \(\mathbf w\), an angle-reset law having drift \(\mathbf w\) and isotropic centered displacement covariance at *every* \(T>0\) exists **if and only if** \(|\mathbf w|\le s_*(t)\). At nonzero extremal speed \(|\mathbf w|=s_*(t)\), orient the \(x\)-axis along \(\mathbf w\), and set \(m=\sqrt{q_*(t)}\). The unique reset law is

* if \(0<t<1/2\), two equal masses at angles \(\pm\arccos m\);
* if \(t=1/2\), a single mass at angle \(0\);
* if \(t>1/2\), masses \((1+m)/2\) and \((1-m)/2\) at angles \(0\) and \(\pi\).

At the transition the maximum isotropic directed speed is \(v/3\) and the effective tensor is \(K=[D+8v^2/(27D_{\rm rot})]I_2\). For an explicit non-extremal example, take \(\lambda=D_{\rm rot}=v=1\) and assign reset masses \(37/64\), \(5/64\), \(11/64\), \(11/64\) at angles \(0,\pi,\pi/2,-\pi/2\); then the drift is \((1/4,0)\) and \(K=(D+15/64)I_2\).

## Assumptions and scope

Let \(X_T\in\mathbb R^2\) solve \(dX_T=v(\cos\Theta_T,\sin\Theta_T)dT+\sqrt{2D}\,dB_T\), with independent standard planar Brownian motion \(B_T\). Between resets, \(\Theta_T\) undergoes circular Brownian motion with generator \(D_{\rm rot}\partial_\theta^2\). The resets form a homogeneous Poisson process of rate \(\lambda\), and each reset replaces \(\Theta\) by a new independent sample from a *fixed* probability measure \(\nu\) on the circle. The spatial position remains unchanged. The angular process is initialized in its unique stationary distribution, independently of spatial noise; \(X_0\) is deterministic. The reset measure may have atoms. Statements for drift speed zero include \(\mu=0\); sharp optimizer uniqueness is asserted only at \(s_*(t)>0\). Isotropy means the two eigenvalues of **centered** spatial displacement covariance agree, not radial symmetry of the full spatial distribution.

## Proof

**1. Stationary angular moments and temporal covariance.** The angular generator acts on any bounded twice differentiable periodic function as
\[
 \mathcal L f(\theta)=D_{\rm rot}f''(\theta)+\lambda\left[\int f(\varphi)d\nu(\varphi)-f(\theta)\right].
\]
For the nonzero integer harmonics \(f_n=e^{in\theta}\), the stationary equation \(\mathbb E_\pi\mathcal L f_n=0\) yields
\[
 \mathbb E_\pi e^{in\Theta}=\frac{\lambda}{\lambda+n^2D_{\rm rot}}\int e^{in\varphi}d\nu(\varphi).
\]
In particular \(c_1=a\mu\), \(c_2=b\eta\). Let \(u(\theta)=(\cos\theta,\sin\theta)\) and \(\bar u=(\Re c_1,\Im c_1)\). The Markov generator gives, for \(s\ge0\),
\[
 \mathbb E[u(\Theta_s)\mid\Theta_0]
 =\bar u+e^{-ks}\big(u(\Theta_0)-\bar u\big).
\]
Consequently the matrix lag covariance in stationarity is \(e^{-ks}\Sigma\), where \(\Sigma=\operatorname{Cov}_\pi(u)\). An elementary complex moment calculation gives
\[
 2\Sigma=(1-|c_1|^2)I_2+H(c_2-c_1^2).
\]
The two-time integrals in \(X_T-X_0\) are absolutely integrable on finite intervals. Using independence of translational Brownian motion and \(\Theta\),
\[
 \operatorname{Cov}(X_T-X_0)
 =2DT I_2+2v^2\int_0^T(T-s)e^{-ks}ds\,\Sigma.
\]
The integral is \(G_k(T)>0\) for every \(T>0\), proving both finite-time and long-time tensor formulas; the mean formula follows from stationarity.

**2. Sharp complex moment disk.** Put \(Z=e^{i\vartheta}\) for \(\vartheta\sim\nu\). Then \(\mathbb EZ=\mu\), \(\mathbb EZ^2=\eta\), and
\[
 |\eta-\mu^2|=|\mathbb E(Z-\mu)^2|
 \le\mathbb E|Z-\mu|^2=1-|\mu|^2.
\]
For sufficiency when \(|\mu|<1\), choose any unit complex direction \(h\) and consider the real line \(\mu+\mathbb Rh\). Its two intersections with the unit circle determine a two-point probability law with mean \(\mu\), uniquely fixing the probabilities. For that law, \(Z-\mu\in\mathbb Rh\) and \(\eta-\mu^2=(1-|\mu|^2)h^2\). Since every boundary phase \(h^2\) is attained, mixing the two chord laws with phases \(\pm e^{i\phi}\) and suitable probabilities gives every \(\eta\) inside the disk using at most four reset angles. At \(|\mu|=1\), the only reset law is the Dirac mass at \(\arg\mu\), and \(\eta=\mu^2\). The affine mapping \(\eta\mapsto b\eta-a^2\mu^2\) proves the exact tensor disk.

**3. Threshold, rigidity, and protocol bifurcation.** Because \(G_k(T)>0\), the centered covariance is isotropic for one (equivalently every) \(T>0\) exactly when \(b\eta=a^2\mu^2\). Substituting \(\eta=(a^2/b)\mu^2\) into the sharp disk yields
\[
 \frac{|b-a^2|}{b}|\mu|^2\le1-|\mu|^2
 \quad\Longleftrightarrow\quad |\mu|^2\le q_*(t),
\]
which proves the if-and-only-if drift bound and guarantees a constructive realization. Direct subtraction gives
\[
 b-a^2=\frac{t(1-2t)}{(4+t)(1+t)^2}.
\]
At equality and \(t\ne1/2\), the complex moment disk inequality is saturated. Equality in \(|\mathbb E(Z-\mu)^2|\le\mathbb E|Z-\mu|^2\) forces \(Z-\mu\) to lie almost surely on a fixed real line. Therefore the resetting measure is uniquely the mean-preserving probability on the two intersections of that line with the circle. If \(t<1/2\), then \(a^2/b-1<0\), so the centered complex second moment is negative along the drift axis. The chord is perpendicular to the drift, giving the unique equal-weight symmetric-angle protocol. If \(t>1/2\), the centered second moment has positive phase along the drift axis, so the chord is parallel and the unique protocol is antipodal with probabilities \((1\pm m)/2\). At \(t=1/2\), the threshold has \(q_*=1\), and the resetting law is uniquely deterministic. The tensor and drift at that rate follow by substituting \(a=1/3\), \(b=1/9\).

## Verification

The standard-library-only program `verify.py` reconstructs chord reset laws, numerically tests the exact feasible disk with mixtures of at most four angles, checks optimal protocols on both sides of the critical ratio, compares the fixed-angle diffusion coefficients with equations (19)–(20) of Baouche et al. (2024), checks the exact example, and samples the independently computable stationary first two angular harmonics. It passed 8,472 finite numerical assertions. The analytic proof above, rather than these finite experiments, establishes all infinite-family claims. In particular, the arbitrary-law implication and equality-case uniqueness use the sharp complex-moment inequality, not numerical optimization. The program is run with `python verify.py`; no third-party packages are needed.

## Relationship to prior work

Kumar, Sadekar and Basu (2020) first analyze fixed-angle orientational resetting of planar active Brownian motion. Baouche, Franosch, Meiners and Kurzthaler (2024) develop its renewal formulation further, allow a general reset-angle law in the model statement, and derive transport quantities specifically for deterministic reset direction. Their equations (17)–(20) provide the fixed-direction special case of the present tensor calculation; their concluding discussion proposes varying the reset-angle distribution. The contribution here is the **complete fixed-drift tensor attainability disk, its constructive finite-support synthesis, the sharp nonzero-drift isotropy boundary at every time, and uniqueness plus structural switching of extremal protocols**, not the original resetting model or its deterministic-angle moment formulas.

Olsen and Löwen (2024) derive moment and optimized diffusion properties for **relative tumbling angles** (each tumble adds an independent angular increment to the existing angle) in a chiral particle, rather than the absolute-orientation redraws here. Ghosh and Mandal (2025) analyze an intrinsically shape-anisotropic swimmer and deterministic orientation resets, without the arbitrary angular-law synthesis considered here. The classical finite trigonometric moment disk is used as a mathematical ingredient, not claimed as a newly proved general theorem.

## Limitations

The result concerns one noninteracting particle, isotropic translational noise, Brownian angular diffusion without intrinsic angular drift, independent Poisson resets of **orientation only**, and stationary angular initial conditions. It says nothing about an isotropic *full displacement law*, interaction-induced anisotropy, correlated resets, or resetting the spatial position. At a fixed nonstationary starting orientation the finite-time tensor need not obey this stationary formula, although its large-time diffusivity has the same limit. Uniformity over every reset distribution is proved analytically; numerical sampling tests selected parameter sets only. The priority comparison cannot categorically exclude a reformulation hidden in broader angular Markov-process moment or optimal-design literature; independent scientific assessment remains to be performed.

## References

1. Y. Baouche, T. Franosch, M. Meiners, C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting* (2024), arXiv:2405.06769, https://arxiv.org/abs/2405.06769 (originally public 2024-05-10).
2. K. Stølevik Olsen, H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations* (2024), arXiv:2405.14326, https://arxiv.org/abs/2405.14326.
3. A. Ghosh, S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting* (2025), arXiv:2501.05149, https://arxiv.org/abs/2501.05149.
4. V. Kumar, O. Sadekar, U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting* (2020), arXiv:2008.03294, https://arxiv.org/abs/2008.03294.
5. K. S. Olsen, *Steady-state moments under resetting to a distribution* (2023), arXiv:2310.04840, https://arxiv.org/abs/2310.04840.
