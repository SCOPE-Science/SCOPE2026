# Exact transient circulation and sharp bath-switch reversal in a Brownian gyrator

## Finding
Let \(A=\begin{pmatrix}a&c\\c&b\end{pmatrix}\) be real symmetric and positive definite, with \(c\ne0\). Let \(T_x,T_y\) be positive almost everywhere, locally bounded measurable bath temperatures. For an overdamped harmonic gyrator with this fixed stiffness, let \(Q(t)=\int_{\mathbb R^2}(xj_y-yj_x)\,dx\,dy\) be its signed integrated angular current at positive times, extended to \(t=0\) by its raw-moment formula below. For any initial law with finite second moments,
\[
\dot Q+(a+b)Q=2c(T_y-T_x)\quad\text{a.e.},\qquad
Q(t)=e^{-(a+b)t}Q(0)+2c\int_0^t e^{-(a+b)(t-s)}[T_y(s)-T_x(s)]\,ds.
\]
In particular, the decay rate is the trace of \(A\), not the collection of decay rates of the full second-moment matrix.

If the starting law is stationary for a constant bath pair with difference \(\Delta_0>0\), and future differences obey \(\Delta(t)=T_y(t)-T_x(t)\ge -B\) a.e. for \(B>0\), the earliest possible zero of \(Q\) occurs at
\[
t_*=(a+b)^{-1}\log(1+\Delta_0/B).
\]
A constant difference \(-B\) attains the bound and reverses the sign exactly once. Swapping the initial temperatures thus reverses this current at \(\log 2/(a+b)\). This is a statement about an integrated current moment, not a radius-normalized angular velocity or full-state equilibration.

## Assumptions and scope
Use unit friction and the Itô dynamics \(dZ_t=-AZ_t\,dt+\sqrt{2D(t)}\,dW_t\), \(D=\operatorname{diag}(T_x,T_y)\), with independent standard Brownian coordinates and an initial law independent of the subsequent noise. Write \(Z_t=(X_t,Y_t)^\top\). The current for \(t>0\) is \(j=-Azp_t-D(t)\nabla p_t\), interpreted for a.e. time, with \(Q\) given its continuous moment representative. There is no bound on the common bath temperature other than the declared positivity and local boundedness, and the quench result constrains only the difference.

## Proof
**Current moment for arbitrary initial laws.** At fixed \(t>0\), write \(Z_t=\xi+U\) with \(\xi=e^{-At}Z_0\) and \(U\) independent and centered Gaussian of covariance \(2\int_0^t e^{-A(t-s)}D(s)e^{-A(t-s)}ds\). This covariance is positive definite since the integrand has strictly positive quadratic form on every fixed nonzero vector for almost every \(s\). If \(\phi\) is the Gaussian density of \(U\), then \(p_t=\mathbb E\phi(\cdot-\xi)\) and \(\nabla p_t=\mathbb E\nabla\phi(\cdot-\xi)\), by boundedness of the Gaussian derivatives. In particular
\[
\int |z|\,|\nabla p_t(z)|\,dz\le \mathbb E|\xi|\int|\nabla\phi(u)|du+\int |u|\,|\nabla\phi(u)|du<\infty.
\]
Thus Fubini applies to the diffusion contribution. For example, at each fixed shift \(\xi\), \(\int (u_x+\xi_x)\partial_{u_y}\phi(u)du=0\) by Gaussian integration in \(u_y\); the other term is the analogous crossed derivative. No Gaussian-tail hypothesis on \(p_t\) is made. The drift contribution is finite by the second moment, and hence
\[
Q=c(\mathbb E Y_t^2-\mathbb E X_t^2)+(a-b)\mathbb E[X_tY_t].
\]
This defines \(Q(0)\) even for an initial law without a density.

**Closure.** Itô's formula yields the a.e. equations for the absolutely continuous raw moments \(u=\mathbb E X^2,v=\mathbb E XY,w=\mathbb E Y^2\):
\[
u'=-2au-2cv+2T_x,\quad v'=-(a+b)v-c(u+w),\quad w'=-2bw-2cv+2T_y.
\]
The stochastic integrals have zero mean on finite time intervals since the temperatures are locally bounded and the second moments are locally bounded by the explicit linear solution. Substituting into \(Q=c(w-u)+(a-b)v\) gives the claimed scalar equation and variation of constants gives the response formula.

**Stationarity and fastest first zero.** For constant baths, \(e^{-At}\to0\) and the Gaussian noise covariance converges to its integral over the whole positive half-line. This yields the unique stationary Gaussian law and \(Q(0)=2c\Delta_0/(a+b)\) by stationarity of the scalar equation. Write \(s=a+b\), \(\sigma=\operatorname{sgn}(c)\). Positivity of the response kernel gives
\[
\sigma Q(t)\ge (2|c|/s)[-B+(\Delta_0+B)e^{-st}].
\]
The lower envelope is positive before \(t_*\); it is attained by choosing \(T_x=M+B/2,T_y=M-B/2\) with \(M>B/2\), and is strictly decreasing with a unique zero. Equality at \(t_*\) forces \(\Delta=-B\) almost everywhere before \(t_*\) by strict positivity of the kernel. The common temperature and the post-first-zero protocol need not be unique. Swapping the two initial temperatures corresponds to \(B=\Delta_0\).

## Verification and limitations
The accompanying `checker.py` uses NumPy and SciPy to compare complete moment dynamics with the scalar formula at selected fixed-bath quenches and checks examples of the sharp bound. Its 2,100 finite comparisons are diagnostics, not the proof of the response for measurable protocols or non-Gaussian laws. The law concerns the signed integrated angular current only, under fixed symmetric positive definite stiffness and diagonal diffusion.

## Relationship to prior work
Filliger and Reimann, [arXiv:0710.3735v1](https://arxiv.org/abs/0710.3735v1), give the stationary torque, which at equal friction is the steady current moment up to sign and units. Dotsenko, Maciołek, Vasilyev and Oshanin, [arXiv:1302.4056](https://arxiv.org/abs/1302.4056), consider steady spatial currents and an inverse-square-radius weighted angular velocity, distinct from \(Q\). Baldassarri, Puglisi and Sesta, [arXiv:2009.06989](https://arxiv.org/abs/2009.06989), and Patrón, Plata and Prados, [arXiv:2407.21110v2](https://arxiv.org/abs/2407.21110v2), study full-state transfer by changing the trap parameters; the latter's Section II gives covariance dynamics for that problem. Cerasoli, Dotsenko, Oshanin and Rondoni, [arXiv:2011.03124](https://arxiv.org/abs/2011.03124), study transient effective temperatures in a fixed-bath setting. Generic linear covariance dynamics are established machinery, and include the scalar projection once the observable is chosen. The present claim isolates that projection for arbitrary bath drives and derives the optimal bounded-difference first-zero result; it does not claim priority for the generic dynamics or for the stationary torque.
