# A unique isotropic reset period and diffusion-axis reversal for coupled Brownian colloids

## Finding

A two-dimensional passive Brownian colloid with hydrodynamically coupled translation and rotation is reoriented to angle zero every \(\tau>0\), leaving its position unchanged. The full long-time displacement covariance per unit time is computed exactly. Its traceless part has the simple form
\[
\operatorname{dev}\Sigma_\tau=2\beta h(u)\bigl(S_0-\gamma(u)H\bigr),\quad h(u)=\frac{1-e^{-4u}}{4u},\quad\gamma(u)=\frac{2m}{1+e^{2u}},\quad u=\beta m\tau.
\]
The matrices \(S_0,H\), and the positive constants \(\beta,m\), are defined below. If the translation–rotation coupling is nonzero, a **finite isotropic diffusion tensor** occurs precisely when \(S_0=\alpha H\) for some \(0<\alpha<m\). The isotropic reset period is unique and equals
\[
\tau_*=\frac{1}{2\beta m}\log\left(\frac{2m}{\alpha}-1\right).
\]
At this period the principal diffusion axis rotates through a right angle: it is transverse to the mean sorting drift for \(\tau<\tau_*\) and parallel to that drift for \(\tau>\tau_*\). Independently, the trace of the displacement covariance decreases strictly with the reset period whenever coupling is nonzero, with exact endpoints and an exact drift–dispersion identity. These statements hold for every positive-definite coupled mobility matrix, subject to the explicitly stated isotropy condition where required.

## Assumptions and scope

Let \(\beta=k_{\mathrm B}T>0\) be the thermal energy. Let the constant body-frame mobility matrix be
\[
\mathsf M=\begin{pmatrix}A&c\\c^\top&m\end{pmatrix}\succ0,
\qquad A=A^\top\in\mathbb R^{2\times2},\quad c\in\mathbb R^2,\quad m>0.
\]
Thus the Schur complement \(S=A-cc^\top/m\) is symmetric and positive definite. Write \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), and let \(R(\theta)\) be the usual two-dimensional rotation matrix. Between resets, define the unwrapped orientation \(\theta\) and planar position \(X\) by the Itô equations
\[
\begin{aligned}
 d\theta_t&=\sqrt{2\beta m}\,dW_t^{(0)},\\
 dX_t&=\beta R(\theta_t)Jc\,dt+\sqrt{2\beta}\,R(\theta_t)\left(\frac{c}{\sqrt m}\,dW_t^{(0)}+S^{1/2}d\mathbf W_t\right),
\end{aligned}
\]
where \(W^{(0)}\) and the two components of \(\mathbf W\) are independent standard Brownian motions. Equivalently, this is the Stratonovich body-mobility Langevin model with noise matrix \(\sqrt{2\beta}\operatorname{diag}(R(\theta),1)\mathsf M^{1/2}\), as used for planar colloids in the motivating source. At deterministic times \(\tau,2\tau,\ldots\), reset \(\theta\) to zero *without resetting or shifting* \(X\). Successive driving Brownian increments are independent. The particle is passive, with no external forcing, interactions, or swimming velocity.

Define the observable drift \(V_\tau=\lim_{t\to\infty}\mathbb E[X_t]/t\), and the uncentered-time convention for the asymptotic **centered** covariance \(\Sigma_\tau=\lim_{t\to\infty}t^{-1}\operatorname{Cov}(X_t)\). For all \(t=n\tau\) these limits already hold exactly after dividing by \(t\). Write
\[
 f=-Jc/m,\quad H=ff^\top-\tfrac12\|f\|^2I,\quad S_0=S-\tfrac12\operatorname{tr}(S)I,\quad u=\beta m\tau.
\]
There is no assumption that \(A\) or \(S\) has aligned eigenvectors, except in the explicit classification of exact isotropization.

## Proof

**1. Independent cycle increments.** At the beginning of every period, the angle is zero and the position does not enter the coefficients. The displacement of each complete cycle is consequently independent and identically distributed, with finite moments of every fixed order. Set \(F(\theta)=R(\theta)f=-R(\theta)Jc/m\). Then \(F'(\theta)=R(\theta)c/m\) and \(F''(\theta)=R(\theta)Jc/m\). Itô's formula gives
\[
 dF(\theta_t)=\beta R(\theta_t)Jc\,dt+\sqrt{2\beta/m}\,R(\theta_t)c\,dW_t^{(0)}.
\]
Therefore a cycle displacement, denoted \(Y\), decomposes **exactly** as
\[
 Y=F(\theta_\tau)-F(0)+M_\tau,\qquad M_\tau=\sqrt{2\beta}\int_0^\tau R(\theta_s)S^{1/2}\,d\mathbf W_s.
\]
Conditionally on the full angular trajectory, \(M_\tau\) has zero mean and covariance \(2\beta\int_0^\tau R(\theta_s)S R(\theta_s)^\top ds\). Hence its cross-covariance with \(F(\theta_\tau)\) is zero.

**2. Exact tensor.** Angular diffusion gives \(\mathbb E[e^{ik\theta_t}]=e^{-k^2\beta m t}\) for integers \(k\). In particular, \(\mathbb E F(\theta_\tau)=e^{-u}f\) and
\[
\begin{aligned}
 \operatorname{Cov}(F(\theta_\tau))={}&\frac{\|f\|^2}{2}(1-e^{-4u})I+(e^{-4u}-e^{-2u})ff^\top,\\
 \frac1\tau\int_0^\tau\mathbb E[R(\theta_s)S R(\theta_s)^\top]ds={}&\frac{\operatorname{tr}S}{2}I+h(u)S_0.
\end{aligned}
\]
The exact mean and centered covariance rates are thus
\[
\boxed{V_\tau=\frac{1-e^{-u}}{m\tau}Jc=-\frac{1-e^{-u}}\tau f}
\]
and
\[
\boxed{\displaystyle
\Sigma_\tau=2\beta\left(\frac{\operatorname{tr}S}{2}I+h(u)S_0\right)
+\frac{\|f\|^2(1-e^{-4u})}{2\tau}I
+\frac{e^{-4u}-e^{-2u}}\tau ff^\top.}
\]
By independence, for all positive integers \(n\), \(\mathbb E X_{n\tau}=n\tau V_\tau\) and \(\operatorname{Cov}(X_{n\tau})=n\tau\Sigma_\tau\), for a deterministic initial position zero. The classical i.i.d. central-limit theorem yields \((X_t-V_\tau t)/\sqrt t\Rightarrow\mathcal N(0,\Sigma_\tau)\) as \(t\to\infty\), including nonmultiples of \(\tau\), since the bounded-length last partial cycle divided by \(\sqrt{t}\) vanishes in probability. The same holds with arbitrary fixed initial position after centering.

**3. Unique isotropization and axis reversal.** Taking the traceless part of the exact tensor and using \(u=\beta m\tau\) reduces its coefficient to
\[
\frac{e^{-4u}-e^{-2u}}{2\beta\tau h(u)}=-\frac{2m}{1+e^{2u}}=-\gamma(u).
\]
Therefore \(\operatorname{dev}\Sigma_\tau=2\beta h(u)(S_0-\gamma(u)H)\). For \(c\ne0\), the matrix \(H\ne0\). The scalar \(\gamma(u)\) is strictly decreasing from \(m\) to zero on \(u\in(0,\infty)\). Consequently \(\Sigma_\tau\) is isotropic at a finite reset period if and only if \(S_0=\alpha H\) with \(\alpha\in(0,m)\), and the unique solution is the stated \(\tau_*\). In that case
\[
 \operatorname{dev}\Sigma_\tau=2\beta h(u)(\alpha-\gamma(u))H.
\]
The matrix \(H\) has positive eigenvalue along \(f\) and negative eigenvalue along \(Jf\). For \(\tau<\tau_*\), the coefficient is negative, so the fastest-diffusing direction is \(Jf\), perpendicular to the mean drift. For \(\tau>\tau_*\), the coefficient is positive, so it is \(f\), parallel to the drift. If \(c=0\), then \(H=0\); the tensor is isotropic at all finite periods if and only if \(S\) is already isotropic, and otherwise never isotropic.

**4. Trace and limiting regimes.** The trace of the angular endpoint covariance is \(\|f\|^2(1-e^{-2u})\), giving
\[
\boxed{\operatorname{tr}\Sigma_\tau=2\beta\operatorname{tr}S+\frac{\|c\|^2}{m^2}\frac{1-e^{-2u}}\tau.}
\]
The function \(\tau\mapsto(1-e^{-2\beta m\tau})/\tau\) is strictly decreasing for \(\tau>0\), since \(e^z>1+z\) for \(z>0\). Thus if \(c\ne0\),
\[
 2\beta\operatorname{tr}S<\operatorname{tr}\Sigma_\tau<2\beta\operatorname{tr}A,
\quad\lim_{\tau\downarrow0}\Sigma_\tau=2\beta A,
\quad\lim_{\tau\to\infty}\Sigma_\tau=\beta\operatorname{tr}S\,I.
\]
For \(c=0\), the trace is constant. Finally, using \(\|V_\tau\|=\|f\|(1-e^{-u})/\tau\), one obtains the exact identity
\[
\boxed{\operatorname{tr}\Sigma_\tau-2\beta\operatorname{tr}S
=\|f\|(1+e^{-u})\|V_\tau\|.}
\]
This is a drift–dispersion relation independent of the anisotropic part of \(S\). The long-time covariance rate is positive definite, since it contains the positive-definite term \((2\beta/\tau)\int_0^\tau\mathbb E[R(\theta_s)S R(\theta_s)^\top]ds\).

## Verification

Run `python verify.py` with Python 3, NumPy, and SymPy. The standalone program checks the angular-harmonic and traceless-coefficient identities, the positive-definite regime, fast- and slow-reset tensor limits, the scalar trace and drift–dispersion laws, a unique finite isotropization witness with a principal-axis swap, and independent time-discretized simulations of the original Itô SDE for three coupled or uncoupled parameter sets. It produces 96 successful assertion groups using fixed random seeds. The simulations corroborate the analytic identities; the infinite-time conclusions follow from the proof and the i.i.d. cycle CLT, not from finite numerical sampling.

For an explicit exact-isotropy example take \(\beta=1.2\), \(m=0.9\), \(c=(0.65,-0.2)^\top\), \(f=-Jc/m\), \(\alpha=m/2\), and \(S=1.2I+\alpha H\). Then \(S\succ0\), \(\mathsf M\succ0\), and \(\tau_*=\log 3/(2\beta m)\), approximately \(0.5086168003\). The diffusion eigenvectors exchange dominance across this finite reset period, while the drift direction remains fixed.

## Relationship to prior work

Cleuren and Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1, Section (ii), Eqs. (4)–(8), introduces exactly the coupled body-frame mobility model, its Stratonovich interpretation, and periodic angle resets. Their Eq. (8) is the drift formula recovered above. Their concluding discussion mentions possible sorting by selectively enhanced diffusion, without the full coupled diffusion tensor, an isotropy threshold, or the axis-switch classification proved here. The model, drift, and orientation-resetting mechanism are not claimed as new.

Chaki, Olsen and Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v1, analyzes orientational resetting and effective diffusion, but its setup explicitly assumes independent rotational and translational noises in a three-diagonal-mobility formulation. That model has \(c=0\), for which the coupled mechanism producing the finite anisotropy-axis reversal is absent. Its complete arXiv HTML Section V explicitly gives a Poisson-reset diffusion tensor for this independent-noise model, but no coupled-noise finite-period axis-reversal threshold. General indirect coverage remains a priority risk. Chakrabarty et al., *Effects of translation-rotation coupling on the displacement probability distribution functions of boomerang colloidal particles* (2016), establishes the physical relevance of nonzero translation–rotation coupling without the present periodic reorientation protocol. The present result requires both effects simultaneously.

## Limitations

This theorem concerns unbounded passive planar Brownian motion with constant symmetric positive-definite body-frame mobility, deterministic instantaneous angular resets to a common reference orientation, and no positional displacement at resets. It does not address Poisson or other renewal resetting times, angular reset noise, external forces, interactions, finite observation-time departures from complete cycles, or physical costs of performing resets. The covariance is the centered long-time covariance, not the raw second moment (which also contains the squared ballistic drift). The isotropy-threshold classification is mathematically conditional on the explicit alignment relation \(S_0=\alpha H\); a generic mobility tensor has no exactly isotropic finite period. Independent scientific validation and priority assessment have not been performed.

## References

1. B. Cleuren and R. Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1 (first public posting 2026-03-19), Section (ii), Eqs. (4)–(8), Appendix B. https://arxiv.org/abs/2603.19430
2. S. Chaki, K. Stølevik Olsen, and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v1 (2024). https://arxiv.org/abs/2406.17550
3. A. Chakrabarty, F. Wang, K. Sun, and Q.-H. Wei, *Effects of translation-rotation coupling on the displacement probability distribution functions of boomerang colloidal particles*, Soft Matter **12** (2016), 4318–4323. https://doi.org/10.1039/c6sm00568c
