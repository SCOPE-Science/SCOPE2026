# Two-observable protocol tomography and a sharp reachable region for driven Brownian gyrators

## Finding

**Theorem (two-observable, bath-independent tomography; exact reachable region and sharp conditioning).** Consider a two-coordinate overdamped stochastic system with a deterministic symmetric harmonic drift whose stiffness and coupling may vary arbitrarily in time. Let \(C(t,s)\) be its *ordered* two-time covariance matrix for \(t>s\), and let the reference-time variance contrast be \(d_s=\operatorname{Var}(X_s)-\operatorname{Var}(Y_s)\). Define the two observable contrasts
\[
D(t,s)=C_{11}(t,s)-C_{22}(t,s),\qquad
A(t,s)=C_{12}(t,s)-C_{21}(t,s).
\]
If \(d_s\ne0\), the integrated stiffness \(K_{s,t}\) and coupling \(U_{s,t}\) are uniquely recovered from only these two lagged covariance contrasts and one equal-time variance contrast:
\[
\boxed{U_{s,t}=\operatorname{artanh}\!\left(\frac{A}{D}\right),\qquad
K_{s,t}=-\frac12\log\!\left(\frac{D^2-A^2}{d_s^2}\right).}
\]
These population-level identities do not require knowing either thermal-bath temperature, the noise correlations, or the distribution of the initial position. On a fixed observation window of duration \(\tau>0\), assume also that the controls obey \(0\le k(v)\le k_{\max}\), \(|u(v)|\le k(v)\) almost everywhere, where \(k_{\max}>0\). Then a pair of real contrasts \((D,A)\) is attainable *if and only if*
\[
\boxed{0<p:=\frac{D+A}{d_s}\le1,\qquad
0<q:=\frac{D-A}{d_s}\le1,\qquad
pq\ge e^{-2k_{\max}\tau}.}
\]
Every attainable pair can be realized by constant controls, so these inequalities characterize the *entire* reachable set, including its boundary. The Jacobian of \((K,U)\mapsto(D,A)\) has singular values \(|d_s|e^{-K+|U|}\) and \(|d_s|e^{-K-|U|}\). Hence the exact Euclidean inverse sensitivity is \(e^{K+|U|}/|d_s|\), and its condition number is \(e^{2|U|}\).

The contrast requirement is sharp *for these two channels*: if \(d_s=0\) then \(D(t,s)=A(t,s)=0\) for every future observation time, regardless of the controls. This does not claim that all other covariance measurements lose identifiability. In the standard Brownian gyrator with constant unequal bath temperatures and any initially stationary stable trap, the initial contrast is nonzero and its sign persists for all future times even under arbitrarily driven controls, so this degeneracy is excluded.

## Assumptions and scope

Let \(I\) denote the two-by-two identity and let \(J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). For \(t\ge0\), let \(Z_t=(X_t,Y_t)^\mathsf T\) be the unique adapted finite-second-moment solution of
\[
\mathrm d Z_t=-[k(t)I+u(t)J]Z_t\,\mathrm dt+\mathrm d M_t,
\]
where \(k,u\) are deterministic locally Lebesgue-integrable real functions and \(M\) is a square-integrable vector martingale whose stochastic increments have mean zero conditional on the past. Its covariance, initial law and noise amplitudes are unrestricted except for these integrability and adaptedness requirements; in particular, Gaussianity and constant or independent bath temperatures are **not** needed for the primary theorem. The covariance \(C(t,s)\) is defined as \(\mathbb E[(Z_t-\mathbb E Z_t)(Z_s-\mathbb E Z_s)^\mathsf T]\), so the order of its indices is essential. The integrated controls are
\[
K_{s,t}=\int_s^t k(v)\,\mathrm dv,\qquad
U_{s,t}=\int_s^t u(v)\,\mathrm dv.
\]
The two-observable inverse is stated only for \(d_s\ne0\), and pointwise instantaneous control recovery is asserted only at almost every time where derivatives exist. Its sensitivity claims concern ideal population covariances; finite-data statistical consistency and sampling errors are not addressed.

The bounded-control reachable-set assertion is conditional on the *given initial covariance* at time \(s\), with \(\tau=t-s\), \(0<k_{\max}<\infty\), and almost-everywhere \(0\le k\le k_{\max}\), \(|u|\le k\). The inequalities \(|u|\le k\) describe the nonnegative-semidefinite harmonic stiffness matrix, including semidefinite boundary controls. A strictly positive-definite trap at every instant would require stronger open conditions on some boundary points.

For the thermal specialization, use \(\mathrm dM_t=(\sqrt{2T_x}\,\mathrm dW_{x,t},\sqrt{2T_y}\,\mathrm dW_{y,t})^\mathsf T\) with fixed \(T_x,T_y>0\), independent standard Brownian motions, and \(T_x\ne T_y\). At the initial time, prepare the unique stationary distribution of constant \(k_0>|u_0|\). The coefficients here have units of inverse time; if the physical drift is scaled by an unknown friction coefficient, the recovered parameters are the *friction-normalized* controls, not absolute stiffness and friction separately.

## Proof

**1. Propagation and noise cancellation.** The matrices \(k(v)I+u(v)J\) commute at any two times because \(J^2=I\) and \(IJ=JI\). Therefore the deterministic propagator is exact even for nonsmooth piecewise or continuously driven controls:
\[
G(t,s)=\exp[-K_{s,t}I-U_{s,t}J]
=e^{-K_{s,t}}\begin{pmatrix}\cosh U_{s,t}&-\sinh U_{s,t}\\-\sinh U_{s,t}&\cosh U_{s,t}\end{pmatrix}.
\]
Variation of constants gives \(Z_t=G(t,s)Z_s+\int_s^tG(t,v)\,\mathrm dM_v\). Since \(G\) is deterministic, the latter integral is orthogonal in expectation to every square-integrable \(\mathcal F_s\)-measurable centered random variable. After centering, it follows that
\[
C(t,s)=G(t,s)\Sigma_s,\qquad \Sigma_s=\operatorname{Cov}(Z_s,Z_s).
\]
This is the standard linear-response covariance identity. Crucially, it is not restricted to stationarity or Gaussian noise. Write \(\Sigma_s=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)\) and \(d_s=a-c\). Direct multiplication shows
\[
D=e^{-K}d_s\cosh U,\qquad A=e^{-K}d_s\sinh U,
\qquad D+A=d_se^{-K+U},\quad D-A=d_se^{-K-U}.
\]
The equal-time off-diagonal covariance \(b\) cancels in both contrasts. A potentially nonzero cross-time antisymmetric covariance \(A\) does **not** require a nonreversible stationary probability current: it may arise simply from a symmetric coupled drift and an anisotropic initial covariance.

**2. Global uniqueness and instantaneous inversion.** If \(d_s\ne0\), then \(D^2-A^2=d_s^2e^{-2K}>0\) and \(|A/D|<1\). Consequently the displayed logarithmic and inverse-hyperbolic formulas are real and give exactly \(U\) and \(K\). Conversely these values reconstruct \(D\) and \(A\) uniquely. With a fixed reference \(s\), the observed functions are absolutely continuous in \(t\) on compact intervals. At almost every \(t>s\),
\[
\frac{\mathrm dD}{\mathrm dt}=-k(t)D+u(t)A,\qquad
\frac{\mathrm dA}{\mathrm dt}=-k(t)A+u(t)D.
\]
Solving the two-by-two linear system yields the instantaneous formulas
\[
\boxed{k(t)=-\frac{DD'-AA'}{D^2-A^2},\qquad u(t)=\frac{DA'-AD'}{D^2-A^2}.}
\]
If \(d_s=0\), both contrasts vanish identically by the first-step identities, establishing the precise degeneracy for the chosen two observables.

**3. Exact bounded-control reachable set.** Define \(p=e^{-(K-U)}\) and \(q=e^{-(K+U)}\). The control constraints are precisely \(k-u\ge0\), \(k+u\ge0\), and \(k\le k_{\max}\). Integration gives \(0<p,q\le1\) and \(pq=e^{-2K}\ge e^{-2k_{\max}\tau}\); the corresponding observable ratios are \(p=(D+A)/d_s\) and \(q=(D-A)/d_s\). Conversely take any \(p,q\) satisfying these inequalities and choose the constant controls
\[
 k(v)=-\frac{\log(pq)}{2\tau},\qquad
 u(v)=\frac{\log(p/q)}{2\tau} \quad (s\le v\le t).
\]
Since \(\log p,\log q\le0\), one has \(k\ge|u|\), and the product bound gives \(k\le k_{\max}\). This protocol realizes the desired contrasts exactly. The boundary cases are genuine because the original control constraints allow equality. No time-dependent protocol enlarges this region.

**4. Exact sensitivity.** The derivative of \((D,A)\) with respect to \((K,U)\) is
\[
H=\begin{pmatrix}-D&A\\-A&D\end{pmatrix}.
\]
Its singular values are \(|D+A|=|d_s|e^{-K+U}\) and \(|D-A|=|d_s|e^{-K-U}\), with their order depending on the sign of \(U\). Therefore the larger and smaller singular values are respectively \(|d_s|e^{-K+|U|}\) and \(|d_s|e^{-K-|U|}\). Since \(d_s\ne0\), the inverse exists, with Euclidean operator norm \(\|H^{-1}\|_2=e^{K+|U|}/|d_s|\) and condition number \(\kappa_2(H)=e^{2|U|}\). This establishes a *sharp local* deterministic sensitivity, not a statistical minimax bound.

**5. Unequal thermal baths give a persistent reference contrast.** In the standard Brownian thermal model described above, the covariance satisfies the Lyapunov equation
\[
\dot\Sigma_t=-[k(t)I+u(t)J]\Sigma_t-\Sigma_t[k(t)I+u(t)J]
+2\operatorname{diag}(T_x,T_y).
\]
Subtracting its two diagonal equations cancels the coupling exactly:
\[
\dot d_t=-2k(t)d_t+2(T_x-T_y).
\]
The stationary preparation at \(k_0>|u_0|\) has \(d_0=(T_x-T_y)/k_0\ne0\). Variation of constants gives
\[
 d_t=e^{-2\int_0^t k(v)\,\mathrm dv}d_0
 +2(T_x-T_y)\int_0^t e^{-2\int_w^t k(v)\,\mathrm dv}\,\mathrm dw.
\]
Both summands have the sign of \(T_x-T_y\), proving \(d_t\ne0\) for every finite \(t\), even with a time-dependent coupling and time-dependent stiffness obeying the stated integrability assumptions.

## Verification

Run \(\texttt{python3 verify.py}\) with standard-library Python 3. No external scientific packages or downloads are needed. The executable performs 6,015 checks, including exact rational two-time matrix identities, multistage propagator composition, bounded-control realizability and singular-value comparisons, a sharp zero-contrast degeneration check, and *independent* numerical Runge–Kutta integration of both the driven equal-time Lyapunov equation and the time-ordered cross-covariance equation. Its recorded output is:

```text
PASS: 6012 deterministic assertions
PASS: 6015 assertions including independently integrated driven covariance
```

The analytic proof, not the finite diagnostic checks, establishes the identities for arbitrary integrable time protocols, all admissible parameters, and the full continuum of reachable contrasts. The independent integration checks one nontrivial multi-stage driven example with time-dependent bath temperatures; they cannot certify untested controls or finite-sample measurement performance.

## Relationship to prior work

Patrón, Plata and Prados (arXiv:2407.21110, first version July 30, 2024) formulate bounded stiffness/coupling control of a Brownian gyrator and derive its equal-time covariance dynamics and time-minimizing protocols. The control triangle used here is their physical constraint, not a new model. The present finding instead characterizes the entire two-lag *observation* region under these controls and recovers the integrated protocol from two particularly selected covariance contrasts, without knowing thermal bath temperatures.

Baldassarri, Puglisi and Sesta (arXiv:2009.06989) use inverse engineering of Brownian gyrator stiffness and coupling from equal-time covariance/precision dynamics and known bath parameters. That is an important earlier control-inference mechanism. It does not provide the present minimal two-contrast lagged reconstruction or exact reachable-observation geometry as stated in the accessible primary text. Ferreira, Metz and Barucca (arXiv:2409.01262) explicitly use the standard lagged Ornstein–Uhlenbeck covariance propagator for a different setting with heterogeneous temperatures and stationary dynamics; the generic identity \(C=G\Sigma\) is therefore **not claimed new**. The contribution is its noise-cancelling compression under a driven symmetric gyrator, exact global inverse, bounded-control geometry, and sharp condition numbers. Cerasoli and collaborators (arXiv:2011.03124) study evolving effective temperatures and one-time gyrator statistics, not these cross-time inverse observables. General linear-system identification may contain equivalent or stronger implicit consequences, so publication priority remains qualified.

## Limitations

The theorem requires deterministic drift of the specific simultaneously diagonalizable symmetric form. General nonsymmetric two-dimensional drifts, independently driven anisotropic diagonal stiffnesses, nonlinear traps, memory kernels, and non-martingale future noise are not covered. The result reconstructs the two *time integrals* of the controls; recovering their instantaneous paths additionally requires time-resolved differentiable covariance data. It does not infer separately an unknown friction coefficient. When \(d_s=0\) the specified two channels vanish, but other lagged covariance entries could still carry information. The attainable region uses ideal population covariances at a fixed reference time with a specified initial covariance; it is not a finite-data confidence region. No independent scientific audit or comprehensive theorem-priority certification has been performed.

## References

1. A. Patrón, C. A. Plata, A. Prados, *Minimum time connection between non-equilibrium steady states: the Brownian gyrator*, arXiv:2407.21110 (first public version 2024-07-30), https://arxiv.org/abs/2407.21110.
2. A. Baldassarri, A. Puglisi, L. Sesta, *Engineered Swift Equilibration of a Brownian Gyrator*, arXiv:2009.06989 (2020-09-15), https://arxiv.org/abs/2009.06989.
3. A. Ferreira, F. L. Metz, P. Barucca, *Random matrix ensemble for covariance matrix of Ornstein-Uhlenbeck processes with heterogeneous temperatures*, arXiv:2409.01262 (2024-09-02), https://arxiv.org/abs/2409.01262.
4. S. Cerasoli and collaborators, *Time-dependence of effective temperatures of a two-dimensional Brownian gyrator with cold and hot components*, arXiv:2011.03124 (2020-11-05), https://arxiv.org/abs/2011.03124.
