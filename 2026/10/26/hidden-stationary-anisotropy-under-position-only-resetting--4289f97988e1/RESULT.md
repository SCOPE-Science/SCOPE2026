# Hidden stationary anisotropy under position-only resetting

## Finding
For a passive planar Brownian colloid with unequal body-frame diffusivities and rotational Brownian motion, Poisson resetting of **position alone** produces an exactly rotationally invariant stationary spatial law, but does **not** eliminate the microscopic diffusivity contrast from its fourth moments. Put
\[
\bar D=\frac{D_{\parallel}+D_{\perp}}2,\qquad
\delta=\frac{D_{\parallel}-D_{\perp}}2.
\]
For every unit vector \(e\) and the stationary projected position \(Z=e\cdot X\),
\[
\mathbb E[Z^2]=\frac{2\bar D}{r},\qquad
\mathbb E[Z^4]=\frac{24\bar D^2}{r^2}+\frac{12\delta^2}{r(r+4q)}.
\]
Consequently its excess kurtosis is exactly
\[
K=\frac{\mathbb E[Z^4]}{(\mathbb E[Z^2])^2}-3
=3+3\left(\frac{D_{\parallel}-D_{\perp}}{D_{\parallel}+D_{\perp}}\right)^2\frac{r}{r+4q}.
\]
The stationary projection has the ordinary symmetric exponential (Laplace) law with diffusivity \(\bar D\) **if and only if** \(D_{\parallel}=D_{\perp}\). For unequal positive diffusivities \(3<K<6\), and the upper bound \(6\) is a sharp, unattained supremum over the positive-parameter class. When the reset and angular-diffusion rates are known, \(K\) determines the magnitude of the body-frame diffusivity contrast relative to their sum, but cannot distinguish the two axis labels.

## Assumptions and scope
Let \(D_{\parallel},D_{\perp},q,r\) be strictly positive. An angular variable \(\Theta_t\in\mathbb R/(2\pi\mathbb Z)\) follows Brownian rotation with generator \(q\partial_{\theta\theta}\). Conditional on its path, the planar position evolves between resets with zero drift and diffusion matrix
\[
\mathcal D(\theta)=R_{\theta}
\begin{pmatrix}D_{\parallel}&0\\0&D_{\perp}\end{pmatrix}
R_{\theta}^{\mathsf T},\qquad
\mathrm dX_t=\sqrt{2}\,\mathcal D(\Theta_t)^{1/2}\,\mathrm dW_t.
\]
Here \(W\) and the angular Brownian driver are independent. At the times of an independent rate-\(r\) homogeneous Poisson process, \(X\) is replaced by the origin while \(\Theta\) is left unchanged. All expectations refer to the unique joint stationary law, not an initial orientation held fixed forever. The conclusion does not concern resetting orientation, applying a drift, self-propulsion, interactions, or zero angular diffusivity.

## Proof
**Stationarity, uniqueness, and finite moments.** Construct a two-sided stationary circle Brownian motion, a two-sided independent Poisson process of rate \(r\), and an independent planar Brownian motion. The present position is its stochastic integral from the last reset to the present. The last-reset age \(T\) is exponential with rate \(r\), and the conditional covariance of position is bounded by \(2D_{\max}T I_2\), where \(D_{\max}=\max(D_{\parallel},D_{\perp})\); thus all polynomial moments are finite. Since \(q>0\), the angle has the unique uniform invariant distribution on the circle. Exponential loss of the pre-reset position and angular mixing establish uniqueness of the joint stationary law. Jointly rotating space and angle preserves the equations and the stationary law, so the position marginal is rotationally invariant. In particular all unit projections have the same even moments.

**Moment generator.** Fix a unit direction at angle \(\varphi\), let \(z=e\cdot X\) and \(c(\theta)=\cos(2(\theta-\varphi))\). Put \(a(\theta)=\bar D+\delta c(\theta)\). The projected generator acts on smooth polynomial/trigonometric observables by
\[
\mathcal L f=a(\theta)\partial_{zz}f+q\partial_{\theta\theta}f+r[f(0,\theta)-f(z,\theta)].
\]
With stationary \(\mathbb E[c]=0\) and \(\mathbb E[c^2]=1/2\), the identities \(\mathbb E[\mathcal L z^2]=0\) and \(\mathbb E[\mathcal L(z^2c)]=0\) give
\[
r\mathbb E[z^2]=2\bar D,\qquad
(r+4q)\mathbb E[z^2c]=2\mathbb E[ac]=\delta.
\]
Next \(\mathbb E[\mathcal L z^4]=0\) yields
\[
r\mathbb E[z^4]=12\mathbb E[z^2a]
=12\left(\bar D\frac{2\bar D}{r}+\delta\frac{\delta}{r+4q}\right),
\]
proving the second- and fourth-moment formulas, without an uncontrolled moment closure.

**Sharp bounds and the Laplace criterion.** Because \(0\le |\delta|/\bar D<1\) and \(0<r/(r+4q)<1\), the exact kurtosis formula gives \(K=3\) exactly for \(\delta=0\), and \(3<K<6\) otherwise. Taking a sequence with \(D_{\perp}/D_{\parallel}\to0\) and \(q/r\to0\) makes \(K\to6\), establishing sharpness. For \(\delta=0\), projected motion between resets is constant-diffusivity Brownian motion, whose stationary characteristic function is \(r/(r+\bar D k^2)\), the symmetric exponential distribution of rate \(\sqrt{r/\bar D}\). For \(\delta\ne0\), its fourth moment exceeds that symmetric exponential's fourth moment at the same variance by the strictly positive amount \(12\delta^2/[r(r+4q)]\), excluding equality of laws. The excess kurtosis identifies the ratio \(|D_{\parallel}-D_{\perp}|/(D_{\parallel}+D_{\perp})\) via
\[
\sqrt{\frac{(K-3)(r+4q)}{3r}}.
\]

**Independent age-mixture derivation.** Conditional on the last-reset age \(T\) and the angular trajectory, \(Z\) is a centered Gaussian whose variance equals \(2\bar DT+2\delta I\), with \(I=\int_0^T c(\Theta_{-s})\,\mathrm ds\). Since \(\mathbb E[c(\Theta_0)c(\Theta_s)]=\tfrac12e^{-4q|s|}\),
\[
\mathbb E[T^2]=\frac2{r^2},\qquad
\mathbb E[TI]=0,\qquad
\mathbb E[I^2]=\frac1{r(r+4q)}.
\]
The conditional Gaussian fourth-moment identity yields exactly the same fourth moment. This is an independent route to the delicate coefficient \(12\), with the same diffusion normalization.

## Verification
The accompanying `VERIFY.py` tests the three independent stationary generator identities and the last-reset-age integral using exact symbolic arithmetic, 240 physically admissible rational parameter sets, high-precision quadrature, and independent transient moment ODE integration. At the explicit admissible point \((D_{\parallel},D_{\perp},r,q)=(3,1,2,1/2)\), the predictions are \(\mathbb E[Z^2]=2\), \(\mathbb E[Z^4]=25.5\), and \(K=3.375\); constant diffusivity \(\bar D=2\) instead gives fourth moment \(24\) and \(K=3\). Code checks reinforce but do not replace the analytic proof.

## Relationship to prior work
Chaki, Olsen, and Löwen (first publicly available June 25, 2024) introduced the same passive anisotropic-colloid resetting protocols. Their position-only-resetting section derives stationary variances \(2\bar D/r\) and zero cross-covariance, then infers a symmetric exponential position marginal independent of diffusivity contrast; the discussion generalizes that inference to the spatial stationary distribution. The present fourth-moment identity shows that isotropy of **second moments** does not entail the proposed equality of **distributions**: a strictly positive shape-dependent fourth-moment discrepancy survives. Their general renewal identity for arbitrary moments is foundational but does not supply the free fourth moment, the displayed closed evaluation, or the sharp characterization above. Evans and Majumdar's constant-diffusivity resetting distribution supplies the equality case. Related work on orientation-only resetting of anisotropic colloids has different state updates and cannot furnish the position-only-reset stationary law. General fourth-order moment methods may be used to rederive the answer, so a broader undiscovered equivalent remains a priority risk.

## Limitations
This is a stationary fourth-order and shape-identification theorem, not a finite-time density formula or finite-sample inference guarantee. When \(q=0\), the joint process can have nonunique angle-invariant measures; that boundary is excluded. The contrast sign is unidentifiable from rotationally invariant stationary position statistics. Strict positive diffusivities imply \(K<6\), with supremum approached only in singular parameter limits. The theorem is proved for the stated passive model and no others.

## References
- S. Chaki, K. Stølevik Olsen, and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550 (first version June 25, 2024), https://arxiv.org/abs/2406.17550 ; published as *Dynamics of a single anisotropic particle under various resetting protocols*, J. Phys.: Condens. Matter 37, 115101 (2025), DOI 10.1088/1361-648X/ada336.
- M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, Phys. Rev. Lett. 106, 160601 (2011), arXiv:1102.2704, https://arxiv.org/abs/1102.2704.
- A. Ghosh, S. Mandal, and S. Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149 (2025), https://arxiv.org/abs/2501.05149. This includes self-propulsion and is not used to establish the passive theorem.
