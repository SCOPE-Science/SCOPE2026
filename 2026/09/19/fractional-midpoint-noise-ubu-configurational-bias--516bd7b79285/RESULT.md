# Fractional midpoint noise creates configurational superconvergence in UBU-type Langevin sampling

## Result

Consider underdamped Langevin dynamics
\[
dX_t=V_t\,dt,\qquad dV_t=-\alpha\nabla U(X_t)\,dt-\gamma V_t\,dt+\sqrt{2\gamma\alpha}\,dW_t,
\]
with quadratic target \(U(x)=\tfrac12x^THx\), \(H\succ0\), whose invariant position covariance is \(H^{-1}\). The recent LC-UBU construction in arXiv:2609.20713 replaces the stochastic UBU midpoint used for the force evaluation by a noise-free predictor. Interpolate between the two by retaining a fraction \(\theta\) of the classical midpoint position noise:
\[
X_{k+1/2}^{(\theta)}=X_k+\frac h2\phi(h/2)V_k+\theta\xi_{k+1/2},\qquad 0\le\theta\le1.
\]
Thus \(\theta=0\) is LC-UBU and \(\theta=1\) is classical UBU, while the remainder of the UBU update is unchanged.

For every stable quadratic mode, the deterministic transition matrix is independent of \(\theta\). Only the one-step noise covariance varies, and it is quadratic in \(\theta\). Consequently the stationary covariance is exactly quadratic in \(\theta\). Its small-step position block is
\[
\boxed{
\Sigma_X(\theta,h)=H^{-1}-\frac{\alpha(3\theta-1)}{12}h^2I
+\frac{\alpha\gamma(\theta-1)}{24}h^3I
+\frac{\alpha h^4}{2880}\Big((26-15\theta)\gamma^2I+120\alpha(\theta^2-\theta)H\Big)+O(h^5).
}
\]

This gives three concrete consequences.

First, LC-UBU and UBU have opposite leading configurational biases:
\[
\Sigma_X^{\rm LC}=H^{-1}+\frac{\alpha}{12}h^2I-\frac{\alpha\gamma}{24}h^3I+O(h^4),
\qquad
\Sigma_X^{\rm UBU}=H^{-1}-\frac{\alpha}{6}h^2I+O(h^4).
\]
Deleting the midpoint noise therefore flips the sign of the leading Gaussian position-covariance bias and halves its magnitude, without changing deterministic stability or contraction on the quadratic target.

Second, the universal choice
\[
\boxed{\theta=\frac13}
\]
cancels the complete \(O(h^2)\) term for every SPD Hessian:
\[
\boxed{
\Sigma_X(1/3,h)=H^{-1}-\frac{\alpha\gamma}{36}h^3I
+\frac{\alpha}{8640}(63\gamma^2I-80\alpha H)h^4+O(h^5).
}
\]
Thus the configurational covariance is third-order accurate on every Gaussian target, with no spectral tuning.

Third, the friction-only correction
\[
\boxed{\theta(h)=\frac13-\frac{\gamma h}{9}}
\]
cancels both the second- and third-order terms simultaneously across all modes:
\[
\boxed{
\Sigma_X(\theta(h),h)=H^{-1}+\frac{\alpha}{8640}(23\gamma^2I-80\alpha H)h^4+O(h^5).
}
\]
Hence this family has fourth-order stationary position-covariance accuracy on arbitrary SPD Gaussian targets. It is not low-cost in the LC-UBU sense because any \(\theta\ne0\) requires the midpoint Gaussian.

For a scalar mode \(U(x)=\lambda x^2/2\), write \(k=\alpha\lambda\). For all sufficiently small stable \(h\), there is a unique exact-zero-bias root \(\theta_*(h)\in(0,1)\) near \(1/3\), with
\[
\boxed{
\theta_*(h)=\frac13-\frac{\gamma h}{9}+\left(\frac{23\gamma^2}{2160}-\frac{k}{27}\right)h^2+O(h^3).
}
\]
The Hessian eigenvalue enters first at this order, explaining why a single spectrum-independent scalar can cancel through \(O(h^3)\) but cannot generally make every anisotropic mode exactly unbiased at finite step size.

## Derivation

Diagonalize \(H\). For a scalar eigenmode, set \(q=e^{-\gamma h/2}\). All members of the \(\theta\)-family have deterministic matrix
\[
A=\begin{pmatrix}
1-\frac{kh(1-q)}\gamma & \frac{1-q^2}{\gamma}-\frac{kh(1-q)^2}{\gamma^2}\\
-khq & q^2-\frac{khq(1-q)}\gamma
\end{pmatrix}.
\]
If \(Q_0\) is the LC-UBU one-step noise covariance, \(c\) is the coefficient of the midpoint position noise in the final state, \(r\) its cross-covariance with the retained full-step noise, and \(V_m\) its variance, then
\[
Q_\theta=Q_0+\theta(cr^T+rc^T)+\theta^2V_mcc^T.
\]
For \(\rho(A)<1\), the discrete Lyapunov equation
\[
\Sigma_\theta=A\Sigma_\theta A^T+Q_\theta
\]
has a unique solution. Since the inverse Lyapunov operator depends on \(A\) but not \(\theta\), \(\Sigma_\theta\) is exactly quadratic in \(\theta\). Expanding this solution in \(h\) gives the formula above.

For the exact one-mode branch, define \(F(\theta,h)=[\lambda(\Sigma_\theta)_{xx}-1]/h^2\). The expansion extends smoothly to \(h=0\), where
\[
F(\theta,0)=-\frac{k(3\theta-1)}{12},\qquad \partial_\theta F(1/3,0)=-\frac{k}{4}\ne0.
\]
The implicit-function theorem gives the local exact root, and coefficient matching yields its expansion.

## Verification

The accompanying script solves the discrete Lyapunov equation directly. For \(\gamma=3\), \(\alpha=\lambda=1\), at \(h=0.025\) it gives
\[
\frac{\operatorname{Var}_{LC}(X)-1}{h^2}=0.0802589,
\quad
\frac{\operatorname{Var}_{1/3}(X)-1}{h^3}=-0.0819232,
\]
\[
\frac{\operatorname{Var}_{UBU}(X)-1}{h^2}=-0.1666452,
\quad
\frac{\operatorname{Var}_{\theta(h)}(X)-1}{h^4}=0.0152418,
\]
approaching the predicted constants \(1/12,-1/12,-1/6,127/8640\). The same script verifies fourth-order simultaneous decay for Hessian eigenvalues \(\{0.5,1,3\}\). At \(h=0.1\), the exact variance root is \(\theta_*=0.300713011807\), versus the asymptotic value \(0.300587962963\).

## Originality boundary and limitations

Configurational superconvergence for Langevin splittings, harmonic stationary-covariance calculations, and UBU itself are prior art and are not claimed here. The claimed contribution is restricted to this LC-UBU/UBU relation: the common deterministic matrix, the \(+1/12\) versus \(-1/6\) leading covariance constants, the universal one-third cancellation law, the friction-only fourth-order covariance correction across arbitrary SPD Gaussian targets, and the local exact-variance branch. Searches of the recent UBU/LC-UBU literature and older configurational-sampling literature did not locate these formulas.

The result concerns invariant configurational covariance for quadratic targets, not higher-order strong or weak trajectory accuracy for nonlinear potentials. The \(\theta\ne0\) schemes require the midpoint Gaussian and therefore do not preserve LC-UBU's reduced random-number count. The motivating preprint is very recent, so contemporaneous follow-up remains an originality risk.

## References

1. W. Lyu, X. Wang, B. Yang, *A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New*, arXiv:2609.20713 (2026).
2. J. M. Sanz-Serna, K. C. Zygalakis, *Wasserstein distance estimates for the distributions of numerical approximations to ergodic stochastic differential equations*, JMLR 22 (2021).
3. D. Paulin, P. A. Whalley, *Correction to “Wasserstein distance estimates for the distributions of numerical approximations to ergodic stochastic differential equations”*, JMLR 25 (2024), arXiv:2402.08711.
4. B. Leimkuhler, C. Matthews, *Robust and efficient configurational molecular sampling via Langevin dynamics*, J. Chem. Phys. 138 (2013).
5. A. Alamo, J. M. Sanz-Serna, *A Technique for Studying Strong and Weak Local Errors of Splitting Stochastic Integrators*, SIAM J. Numer. Anal. 54 (2016), 3239–3257.
