# Universal drift-orbital memory and the node–focus sign boundary in planar Gaussian transport

## Finding
Consider an arbitrary stable planar linear stochastic flow with constant positive-definite diffusion. Its *drift-only orbital angular activity*, defined using the deterministic velocity field rather than a noise-contaminated time derivative, is a distinguished quadratic observable: after centering, it is an exact eigenfunction of the Markov generator. Consequently, its entire stationary autocovariance is a **single positive exponential** with rate equal to the trace of the drift matrix, even for irreversible, nonnormal, or oscillatory dynamics. The same observable has a complete sign-support classification determined solely by the node–focus discriminant of that matrix. These two conclusions share an exact planar algebraic identity but are logically distinct from the distribution of discretized stochastic angular momentum.

Specifically, let \(B=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\) be real with \(k=a+d>0\) and \(\det B>0\), and let \(D=D^{\mathsf T}>0\). Let \(X_t=(X_{1,t},X_{2,t})^{\mathsf T}\) be the stationary solution of
\[
 dX_t=-B X_t\,dt+\sqrt{2D}\,dW_t.
\]
Define the drift-only oriented orbital activity
\[
 T_t=X_{1,t}(-BX_t)_2-X_{2,t}(-BX_t)_1=X_t^{\mathsf T}QX_t,
 \qquad Q=\begin{pmatrix}-c&(a-d)/2\\(a-d)/2&b\end{pmatrix}.
\]
Let \(S=\mathbb E[X_0X_0^{\mathsf T}]\), the unique positive-definite solution of \(BS+SB^{\mathsf T}=2D\), and write \(\mu=\operatorname{tr}(QS)\) and \(V=2\operatorname{tr}(QSQS)\). Then, for every real lag \(t\),
\[
\boxed{\operatorname{Cov}(T_0,T_t)=V\,e^{-k|t|}.}
\]
If \(Q\ne0\), then \(V>0\), and the normalized autocorrelation is precisely \(e^{-k|t|}\), independently of all other drift and noise parameters. The variance of the time-integrated centered activity has the exact finite-time form
\[
 \operatorname{Var}\!\left(\int_0^L(T_t-\mu)\,dt\right)
 =2V\left(\frac{L}{k}-\frac{1-e^{-kL}}{k^2}\right),\quad L\ge0.
\]
The one-time characteristic function is
\[
 \boxed{\mathbb E[e^{isT_0}]=\det(I-2isSQ)^{-1/2}
 =\left(1-2is\mu-4s^2\det(S)\det(Q)\right)^{-1/2}.}
\]
The square-root branch is continuous at \(s=0\) and takes value one there. Put \(\Delta=k^2-4\det B\). If \(\Delta>0\), the activity takes strictly positive and strictly negative values with positive probabilities. If \(\Delta<0\), it has a fixed nonzero sign almost surely. If \(\Delta=0\), it has a fixed nonzero sign almost surely unless \(B\) is a scalar multiple of the identity, in which case \(T_t=0\) identically. Thus the sign support changes exactly at the real-versus-complex eigenvalue discriminant, including the defective repeated-root boundary.

## Assumptions and scope
The drift matrix is constant, real and \(2\times2\); its two eigenvalues have positive real part, equivalently \(\operatorname{tr} B>0\) and \(\det B>0\). The noise matrix \(D\) is symmetric positive definite, \(W\) is standard two-dimensional Brownian motion, and the process is initialized in its unique centered stationary Gaussian distribution. All results are for the *deterministic drift contribution* \(T_t=X_t\wedge(-BX_t)\), not for the full increment-based angular momentum \(X_{1,t}\dot X_{2,t}-X_{2,t}\dot X_{1,t}\); Brownian paths have no ordinary pointwise derivatives. There is no assumption of detailed balance, symmetric mobility, diagonal noise, or distinct drift eigenvalues.

## Proof
**Stationary covariance and positivity.** Stability gives the convergent formula \(S=2\int_0^\infty e^{-Bt}De^{-B^{\mathsf T}t}\,dt\), which is positive definite and solves the Lyapunov equation. Therefore the stationary law gives positive probability to every nonempty open subset of the plane.

**Exact quadratic eigenfunction.** For the displayed \(Q\), direct multiplication gives the planar matrix identity
\[
 B^{\mathsf T}Q+QB=(\operatorname{tr}B)Q.
\]
This can also be deduced from the Cayley–Hamilton identity for \(2\times2\) matrices applied to the wedge product \(x\wedge Bx\). With the generator \(\mathcal Lf(x)=-(Bx)\cdot\nabla f(x)+D:\nabla^2f(x)\), the quadratic rule yields
\[
 \mathcal LT(x)=-kT(x)+2\operatorname{tr}(DQ).
\]
Stationarity gives \(0=\mathbb E[\mathcal LT]\), hence \(\mu=2\operatorname{tr}(DQ)/k=\operatorname{tr}(QS)\). Thus \(\mathcal L(T-\mu)=-k(T-\mu)\). Polynomial moment finiteness and the conditional polynomial dynamics imply \(\mathbb E[T_t-\mu\mid X_0]=e^{-kt}(T_0-\mu)\) for \(t\ge0\). Multiplication by \(T_0-\mu\) and stationarity prove the covariance formula. Stationarity also implies symmetry between positive and negative time lags for this scalar covariance.

**Variance and full stationary law.** Wick's fourth-moment formula for a centered Gaussian vector gives \(V=2\operatorname{tr}(QSQS)\). Since \(S>0\), this equals \(2\operatorname{tr}[(S^{1/2}QS^{1/2})^2]\), which is strictly positive exactly when \(Q\ne0\). The Gaussian quadratic-form transform gives \(\det(I-2isSQ)^{-1/2}\). Expanding a \(2\times2\) determinant proves the scalar transform shown above. Integrating the stationary autocovariance over the square \([0,L]^2\) gives the stated integrated-activity variance, including \(L=0\).

**Sharp sign boundary.** Expanding the determinant of \(Q\) yields
\[
 \boxed{\det Q=\det B-\frac14(\operatorname{tr}B)^2=-\frac{\Delta}{4}.}
\]
For \(\Delta>0\), \(Q\) is indefinite; positivity of the stationary Gaussian density makes both strict sign events have positive probability. For \(\Delta<0\), \(Q\) is positive or negative definite, so \(T_t\) has its corresponding strict sign almost surely. For \(\Delta=0\), either \(Q=0\), which forces \(b=c=0\) and \(a=d\), or \(Q\) has rank one and one nonzero eigenvalue. The latter case is one-sided with no atom at zero because the stationary Gaussian is nondegenerate. This proves completeness and the boundary cases.

## Verification
Run `python check_torque.py` using SymPy, NumPy, and SciPy. The included standalone checker verifies the arbitrary-symbolic quadratic eigenfunction identity and discriminant identity; checks generator action; solves five independent rational Lyapunov systems spanning stable real-node, stable focus, repeated-root Jordan, scalar, and nonnormal cases; compares direct Gaussian-Wick two-time calculations with the single-exponential law at four lags each; and reproduces the coupled-ellipsoid special-case mean, variance, and soft-mode covariance limits. It passed 77 deterministic assertions. These checks are not replacements for the quantified analytic proof above.

For comparison with a familiar Brownian gyrator, put \(B=\alpha\begin{psmallmatrix}1&\varepsilon\\\varepsilon&1\end{psmallmatrix}\), \(D=\operatorname{diag}(D_1,D_2)\), with \(\alpha,D_1,D_2>0\), \(|\varepsilon|<1\). Then
\[
 T_t=\alpha\varepsilon(X_{2,t}^2-X_{1,t}^2),\quad
 \mu=-\varepsilon(D_1-D_2),\quad
 V=\varepsilon^2\left(\frac{(D_1+D_2)^2}{1-\varepsilon^2}+(D_1-D_2)^2\right),
\]
and \(\operatorname{Corr}(T_0,T_t)=e^{-2\alpha|t|}\) whenever \(\varepsilon\ne0\). Even as one positional relaxation mode approaches zero for \(|\varepsilon|\uparrow1\), this observable's *normalized* memory time remains \(1/(2\alpha)\); its variance diverges. The limiting boundary itself has no stationary distribution and is **not included** in the main theorem. The physical dissipative-coupling approximation motivating this matrix may require small coupling, so the approach to its stability boundary is a mathematical extrapolation, not a claim about experimental validity.

## Relationship to prior work
Godrèche and Luck (first circulated in 2018, arXiv:1807.00694) developed the general multivariate Gaussian Ornstein–Uhlenbeck stationary covariance, two-time coordinate correlations, and irreversible-current framework. Their general Gaussian framework supplies ingredients from which quadratic statistics can be computed, but its planar presentation does not state the universal generator eigenfunction for the *drift-only wedge observable* or the associated complete sign-support classification. This claim is therefore specifically about those derived structural properties, not about newly solving the Ornstein–Uhlenbeck equation.

Dutta and Saha (arXiv:2308.02085) supplied a dissipatively coupled chiral Brownian-ellipsoid model and analyzed its mean gyration. Viot, Argun, Volpe, Imparato, Rondoni, and Oshanin (arXiv:2307.05248, full text, especially Sections 2–3) analyzed the *total increment-based* angular momentum and angular velocity of a Brownian gyrator; that observable explicitly includes Brownian increments and has discretization-dependent fluctuation size. Their characteristic functions and tails do not imply equality with the present drift-only quadratic observable. The two observables have different definitions even in the same underlying diffusion.

The matrix identity here is elementary once the correct observable is isolated; wider Gaussian-polynomial and stochastic-thermodynamics literature may already contain an equivalent formulation. No claim of exhaustive priority, independence, or external certification is made.

## Limitations
The one-sided sign theorem concerns the drift-only orbital activity, not the noisy measured instantaneous angular momentum. An exact positive/negative sign almost surely says nothing about the sign of the stochastic pathwise increment. The normalized exponential correlation is undefined in the scalar-drift case \(Q=0\), although the unnormalized zero covariance formula remains valid. Results assume two spatial dimensions, additive white Gaussian noise, a time-homogeneous stable linear drift, and stationary initialization. No claim is made for nonlinear drift, nonstationary noise, or higher-dimensional coordinate-pair projections. General covariance theory can be combined with Gaussian moment formulas to derive aspects of the result; assessing whether this combination has previously been explicitly recognized requires independent literature review.

## References
1. Claude Godrèche and Jean-Marc Luck, *Characterising the nonequilibrium stationary states of Ornstein–Uhlenbeck processes*, arXiv:1807.00694 (first public 2018-07-02), especially Sections 2.1–2.2, 2.6, 2.10.
2. Soham Dutta and Arnab Saha, *Microscopic Gyration with Dissipative Coupling*, arXiv:2308.02085 (first public 2023-08-03).
3. Pascal Viot et al., *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (first public July 2023), subsequently *Soft Matter* **20** (2024), 3154–3160, DOI:10.1039/D3SM01606D.
