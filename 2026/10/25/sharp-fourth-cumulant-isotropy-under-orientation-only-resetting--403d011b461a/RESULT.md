# Sharp fourth-cumulant isotropy under orientation-only resetting of an anisotropic Brownian particle

## Finding

For a passive planar anisotropic Brownian particle whose orientation alone is reset at Poisson rate \(r>0\) toward a fixed angle and undergoes rotational diffusion at rate \(q>0\), the projected displacement fourth cumulant has an exact, nonzero, direction-dependent formula at every positive observation time when the angular dynamics starts stationary. Its directional maxima and minima exchange places at one sharp rate \(r=2q\). Precisely at this rate the entire fourth-cumulant tensor is rotationally invariant for **every finite positive time**, although the displacement covariance remains strictly anisotropic whenever the body-frame diffusivities differ. This is fourth-*cumulant* isotropy, not fourth-raw-moment isotropy or Gaussianity.

Let \(Z_\phi(t)=e_\phi\cdot(X_t-X_0)\), \(e_\phi=(\cos\phi,\sin\phi)\), \(D_0=(D_\parallel+D_\perp)/2\), \(\delta=(D_\parallel-D_\perp)/2\), and \(\psi=\theta_*-\phi\). Set
\[
A=\frac{r}{r+4q},\qquad B=\frac{r}{r+16q},\qquad \lambda=r+4q,
\qquad V_\phi=\frac{1-A^2+(B-A^2)\cos(4\psi)}{2}.
\]
For stationary initial angle, for each \(t>0\) and every \(\phi\in\mathbb R\),
\[
\operatorname{Var}(Z_\phi(t))=2t[D_0+\delta A\cos(2\psi)],
\]
\[
\boxed{\kappa_4(Z_\phi(t))=24\delta^2 V_\phi
\left(\frac{t}{\lambda}-\frac{1-e^{-\lambda t}}{\lambda^2}\right).}
\]
Here \(\kappa_4(Z)=\mathbb E[Z^4]-3(\mathbb E[Z^2])^2\), since \(\mathbb E Z=0\). In particular, if \(D_\parallel\ne D_\perp\), the cumulant is strictly positive for every \(t>0\).

The sign determining angular ordering is exactly
\[
\boxed{B-A^2=\frac{8rq(2q-r)}{(r+16q)(r+4q)^2}.}
\]
For \(0<r<2q\), the maximum of \(\kappa_4\) occurs for \(\phi=\theta_*\pmod{\pi/2}\) and the minimum for \(\phi=\theta_*+\pi/4\pmod{\pi/2}\). The strict inequalities reverse for \(r>2q\). At the unique positive rate \(r=2q\), \(A=1/3\), \(B=1/9\), \(V_\phi=4/9\) independently of direction; thus all projected fourth cumulants are identical at each fixed \(t>0\). Yet their variances differ: at \(r=2q\),
\[
\operatorname{Var}(Z_{\theta_*}(t))-\operatorname{Var}(Z_{\theta_*+\pi/2}(t))=\frac{4\delta t}{3}\ne0.
\]
The common fourth-cumulant growth coefficient at this rate is \(\lim_{t\to\infty}\kappa_4(Z_\phi(t))/t=16\delta^2/(9q)>0\).

If the orientation instead starts at the reset angle \(\Theta_0=\theta_*\), the same rate-dependent directional formula holds for the **leading cumulant growth**: \(\kappa_4(Z_\phi(t))=24\delta^2 V_\phi t/(r+4q)+O(1)\) as \(t\to\infty\), for each fixed set of parameters and direction. Finite-time exact angular isotropy is not asserted for this deterministic preparation.

## Assumptions and scope

All statements are for \(r,q>0\) and fixed \(D_\parallel,D_\perp>0\), with \(D_\parallel\ne D_\perp\) for strictness. Let \(\Theta_t\in\mathbb R/(2\pi\mathbb Z)\) be circle-valued rotational Brownian motion with generator \(q\partial_\theta^2\), independently reset to \(\theta_*\in\mathbb R/(2\pi\mathbb Z)\) at Poisson rate \(r\). The joint Markov process has orientation generator
\[
\mathcal L_\theta f(\theta)=qf''(\theta)+r[f(\theta_*)-f(\theta)].
\]
The freely diffusing particle has no propulsion, restoring force, or position reset; its displacement obeys the Itô equation
\[
dX_t=\sqrt2\,R_{\Theta_t}\begin{pmatrix}\sqrt{D_\parallel}&0\\0&\sqrt{D_\perp}\end{pmatrix}dW_t,
\]
where \(W\) is a standard independent two-dimensional Brownian motion. The conditional spatial diffusivity is \(D(\theta)=R_\theta\operatorname{diag}(D_\parallel,D_\perp)R_\theta^{\mathsf T}\). Hence the projected conditional diffusivity is \(D_0+\delta\cos2(\theta-\phi)\). The canonical exact finite-time statement assumes \(\Theta_0\) has the unique stationary angular distribution, independently of \(W\). The separate large-time extension allows deterministic \(\Theta_0=\theta_*\). Positions are not stationary and spread diffusively.

## Proof

**Stationary harmonics.** Let \(\pi\) denote the invariant distribution of \(\Theta\). A representation by its most recent reset age is
\[
\pi=\int_0^\infty re^{-ra}\,P_a(\theta_*,\cdot)\,da,
\]
where \(P_a\) is the rotational heat kernel. On Fourier characters \(e^{ik\theta}\), the heat semigroup has eigenvalue \(e^{-qk^2a}\), so for every integer \(k\),
\[
\mathbb E_\pi e^{ik(\Theta-\theta_*)}=\frac{r}{r+qk^2}.
\]
This also establishes uniqueness because a Poisson reset couples any two angular starts after their first common reset.

**Exact angular covariance.** Put \(f_\phi(\theta)=\cos2(\theta-\phi)\). The preceding Fourier formula gives \(\mu_\phi=\mathbb E_\pi f_\phi=A\cos2\psi\) and
\[
\mathbb E_\pi f_\phi^2=\frac{1+B\cos4\psi}{2};\quad
\operatorname{Var}_\pi(f_\phi)=V_\phi.
\]
The generator identity \(\mathcal L_\theta(f_\phi-\mu_\phi)=-(r+4q)(f_\phi-\mu_\phi)\) yields the exact conditional semigroup
\[
\mathbb E[f_\phi(\Theta_{s+t})\mid\Theta_s]
=\mu_\phi+e^{-\lambda t}(f_\phi(\Theta_s)-\mu_\phi).
\]
Thus stationarity implies \(\operatorname{Cov}(f_\phi(\Theta_s),f_\phi(\Theta_u))=V_\phi e^{-\lambda|u-s|}\), with no Gaussian approximation to the angular dynamics.

**Gaussian-variance mixture.** Conditional on the entire orientation path, \(Z_\phi(t)\) is centered normal with variance
\[
Q_t=2D_0t+2\delta\int_0^t f_\phi(\Theta_s)\,ds.
\]
It follows exactly that \(\operatorname{Var}(Z_\phi)=\mathbb E Q_t\) and \(\kappa_4(Z_\phi)=3\operatorname{Var}(Q_t)\): the latter identity is conditional Gaussian Wick calculus, not an assumption that the unconditional displacement is normal. Moreover,
\[
\operatorname{Var}\left(\int_0^t f_\phi(\Theta_s)ds\right)
=2V_\phi\int_0^t(t-u)e^{-\lambda u}du
=2V_\phi\left(\frac{t}{\lambda}-\frac{1-e^{-\lambda t}}{\lambda^2}\right).
\]
Substitution gives both announced moments. The bracket is strictly positive for every \(t>0\). Since the angular heat kernel makes \(\pi\) positive on the entire circle and \(f_\phi\) is nonconstant, \(V_\phi>0\); therefore \(\kappa_4>0\) when \(\delta\ne0\).

**Sharp rate and non-Gaussian isotropy.** Algebra gives
\[
B-A^2=\frac{r}{r+16q}-\frac{r^2}{(r+4q)^2}
=\frac{8rq(2q-r)}{(r+16q)(r+4q)^2}.
\]
All other factors multiplying \(\cos4\psi\) in \(\kappa_4\) are strictly positive. Therefore this single factor establishes the exhaustive angular maximum/minimum exchange and unique interior isotropy rate. At \(r=2q\), \(A=1/3\), \(B=1/9\), and the variance difference is \(4\delta t/3\), which stays nonzero. The growth coefficient follows by dividing the explicit \(\kappa_4\) formula by \(t\) and letting \(t\to\infty\).

**Deterministic initial orientation.** For \(\Theta_0=\theta_*\), the same conditional semigroup gives, for \(u\ge s\), \(\operatorname{Cov}(f_\phi(\Theta_s),f_\phi(\Theta_u))=e^{-\lambda(u-s)}\operatorname{Var}(f_\phi(\Theta_s))\). The Fourier relaxation for angular harmonics of orders two and four implies \(\operatorname{Var}(f_\phi(\Theta_s))=V_\phi+O(e^{-cs})\) with \(c=\min\{r+4q,r+16q\}>0\). The time-integrated difference from stationary covariance is bounded uniformly in \(t\); hence \(\kappa_4(Z_\phi(t))=24\delta^2 V_\phi t/\lambda+O(1)\). There is no assertion of finite-time exact isotropy under this alternative preparation.

## Verification

The standalone script `verify.py` independently evolves the projected displacement second and fourth moments through a finite angular-Fourier moment hierarchy. It does not use the covariance-integral derivation to compute its numerical reference. For six rotational/reset parameter pairs, three observation times and five observation directions, its 90 fourth- and second-moment predictions match the theorem within the explicit numerical tolerance; additional exact rational checks verify the factorization \(B-A^2\), and angular tests verify the unique transition and the complete critical directional cancellation. Run `python verify.py` with `numpy` and `scipy` installed. Numerical ODE comparisons corroborate but do not substitute for the proof.

## Relationship to prior work

Chaki, Olsen and Löwen (arXiv:2406.17550v1, Section V, especially equations 47–65) give the same passive anisotropic particle and orientation-only resetting protocol, derive the mean-square displacement and anisotropic effective diffusion tensor, and discuss Gaussian late-time scaling. These established second-order conclusions are inputs and are not claimed as new. The complete accessible arXiv text was checked for the projected fourth cumulant, the exact angular fourth-cumulant tensor, and the unique \(r=2q\) cancellation; those results were not located.

Ghosh, Mandal and Chaki (arXiv:2501.05149v1, Section III.3 and Appendix C) treat a related **self-propelled** anisotropic particle under the same three reset protocols, giving mean/variance results; an active drift changes higher cumulants and its calculated second moments do not entail this passive fourth-cumulant classification. Ten Hagen, van Teeffelen and Löwen (arXiv:1005.1343) calculate fourth moments of anisotropic or propelled Brownian particles without this orientation-reset mechanism; their expressions do not directly imply the present rate threshold. Position-only resetting and propelled-particle reorientation are distinct protocols; their spatial stationary laws and propulsion-correlation observables do not imply the present cumulant theorem.

## Limitations

The exact finite-time formula assumes stationary orientation at the start of the displacement measurement; setting the initial angle equal to the reset angle gives the stated large-time growth coefficient, not the exact finite-time angular cancellation. Fourth-cumulant isotropy does not imply covariance or fourth-moment isotropy: the variance remains direction-dependent at the critical rate. The normalized excess kurtosis likewise remains direction-dependent because its denominator contains anisotropic variance. No stationary spatial law exists without positional confinement or resetting. There is no claim for self-propulsion, random reset orientations, direction-dependent rotational diffusivity, coupled translational/rotational driving noises, or nonlinear mechanical forces. A mathematically equivalent fourth-cumulant result may exist in broader diffusivity-switching literature; priority is not independently established.

## References

1. S. Chaki, K. Stølevik Olsen, H. Löwen, *Anisotropic Brownian particles under resetting*, first public arXiv version 25 June 2024, arXiv:2406.17550v1, https://arxiv.org/html/2406.17550v1 (physical model; Section V).
2. A. Ghosh, S. Mandal, S. Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, first public arXiv version 9 January 2025, arXiv:2501.05149v1, https://arxiv.org/html/2501.05149v1 (related active model; Section III.3 and Appendix C).
3. B. ten Hagen, S. van Teeffelen, H. Löwen, *Brownian motion of a self-propelled particle*, first public arXiv version 8 May 2010, arXiv:1005.1343v1, https://arxiv.org/abs/1005.1343 (older non-reset fourth-moment analysis).
