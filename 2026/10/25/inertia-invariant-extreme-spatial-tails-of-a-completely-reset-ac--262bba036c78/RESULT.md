# Inertia-invariant extreme spatial tails of a completely reset active Brownian particle

## Finding

For a completely reset inertial active Brownian particle with strictly positive translational and rotational diffusion, the **ultimate spatial tail decay rate is exactly independent of inertia**. It is determined by the principal Mathieu eigenvalue of the rotational diffusion generator, despite a much stronger inertia-dependent suppression of the stationary variance.

Write \(\Lambda(k)\) for the largest eigenvalue of
\[
\mathcal L_k=D_r\partial_\theta^2+k v_0\cos\theta
\]
on real \(2\pi\)-periodic functions, and put \(\Psi(k)=Dk^2+\Lambda(k)\). For every positive reset rate \(r\), there is precisely one \(k_*>0\) with
\[
\boxed{\Psi(k_*)=r.}
\]
For the stationary horizontal displacement \(X_{\rm st}\), **both** of the following hold:
\[
\boxed{\mathbb E[e^{kX_{\rm st}}]<\infty\ \Longleftrightarrow\ |k|<k_*;}
\]
\[
\boxed{\lim_{x\to\infty}\frac{\log\Pr(X_{\rm st}>x)}x
=\lim_{x\to\infty}\frac{\log\Pr(X_{\rm st}<-x)}x=-k_*.}
\]
The equality at the moment boundary is *excluded*: both endpoint exponential moments are infinite. These assertions hold for any finite, positive inertial time \(\tau\), for both fixed-heading and uniformly randomized heading at complete resets.

The eigenvalue may equivalently be evaluated with the standard even Mathieu characteristic value,
\[
\Lambda(k)=-\frac{D_r}{4}\,a_0\!\left(-\frac{2kv_0}{D_r}\right).
\]
For fixed \(D,D_r,v_0,\tau>0\), the two useful endpoint laws are
\[
k_*(r)\sim\sqrt{\frac{r}{D+v_0^2/(2D_r)}}\quad (r\downarrow0),
\qquad k_*(r)\sim\sqrt{\frac rD}\quad (r\to\infty).
\]
In contrast, as \(r\to\infty\) at fixed \(\tau>0\),
\[
\operatorname{Var}(X_{\rm st})=\frac{4D}{\tau^2 r^3}+O(r^{-4}),\qquad
\frac{k_*^{-1}}{\sqrt{\operatorname{Var}(X_{\rm st})}}
\sim\frac{\tau r}{2}.
\]
Thus the exact far-tail length decays only as the inverse square root of reset rate while the typical stationary width decays as the inverse three-halves power. This identifies an increasingly pronounced, nonuniform separation between the distribution's narrow core and its remote tails.

## Assumptions and scope

Let \(D>0\), \(D_r>0\), \(v_0>0\), \(\tau>0\), \(r>0\). Between resets, a particle in the plane follows independent Itô Brownian noises:
\[
d\mathbf R_t=\mathbf V_t\,dt,\qquad
d\mathbf V_t=-\tau^{-1}(\mathbf V_t-v_0(\cos\theta_t,\sin\theta_t))\,dt
+\tau^{-1}\sqrt{2D}\,d\mathbf B_t,\qquad
d\theta_t=\sqrt{2D_r}\,dW_t.
\]
A rate-\(r\) Poisson clock, independent of all noises, resets \(\mathbf R=\mathbf V=\mathbf0\) and either fixes \(\theta=\theta_0\) or draws \(\theta\) independently uniformly on the circle. Both options restart independent excursions. Let \(X_{\rm st}\) be the first coordinate under the unique stationary renewal law. Only this full-reset protocol is asserted. Inertia \(\tau\), diffusion coefficients, and the propulsion speed are held fixed whenever \(r\) tends to zero or infinity.

The probability-tail statements concern **logarithmic** tails, not a claimed asymptotic probability prefactor or the pointwise stationary density. The conclusion concerns each *coordinate* separately, not an asserted radial density asymptotic. For fixed \(\theta_0\), positive and negative tails need not have the same prefactor despite having identical exponential rates.

## Proof

**1. Exact excursions and Gaussian comparison.** Start one reset-free excursion at \(\mathbf R=\mathbf V=\mathbf0\). Solving the linear velocity equation and integrating once gives
\[
X_t^\tau=v_0\int_0^t (1-e^{-(t-s)/\tau})\cos\theta_s\,ds+
\sqrt{2D}\int_0^t (1-e^{-(t-s)/\tau})\,dB_s.
\]
The Gaussian term is independent of the heading process, centered, and of variance \(2Dg_\tau(t)\), with
\[
g_\tau(t)=t-2\tau(1-e^{-t/\tau})+
\frac{\tau}{2}(1-e^{-2t/\tau}).
\]
For every \(t\ge0\),
\[
t-\frac{3\tau}{2}\le g_\tau(t)\le t,
\qquad
\left|v_0\int_0^t e^{-(t-s)/\tau}\cos\theta_s\,ds\right|\le v_0\tau.
\]
Consequently, for all real \(k\),
\[
e^{-|k|v_0\tau-\frac32Dk^2\tau}e^{Dk^2t}F_k(t)
\le \mathbb E[e^{kX_t^\tau}]
\le e^{|k|v_0\tau}e^{Dk^2t}F_k(t),
\tag{1}
\]
where \(F_k(t)=\mathbb E\exp(kv_0\int_0^t\cos\theta_s\,ds)\).

**2. The angular spectral exponent.** The generator \(\mathcal L_k\) is self-adjoint on the circle, with compact resolvent. Its positivity-improving Feynman–Kac semigroup has a simple largest real eigenvalue \(\Lambda(k)\) and a strictly positive normalized eigenfunction. For either deterministic initial heading or a uniform initial-heading distribution, spectral expansion gives
\[
F_k(t)=c_k e^{t\Lambda(k)}(1+o(1))\quad(t\to\infty),
\]
for some finite \(c_k>0\). Equation (1) proves, for each \(k\in\mathbb R\),
\[
\lim_{t\to\infty}\frac1t
\log\mathbb E[e^{kX_t^\tau}]=\Psi(k)=Dk^2+\Lambda(k).
\tag{2}
\]
Here \(\Lambda(0)=0\), \(\Lambda\) is real analytic and convex because it is a limit of log-moment-generating functions. Rotation by \(\pi\) conjugates \(\mathcal L_k\) to \(\mathcal L_{-k}\), so \(\Lambda\) and \(\Psi\) are even. The variational principle with the constant test function and the bounded potential imply \(0\le\Lambda(k)\le |k|v_0\). Convexity and evenness imply that \(\Lambda\) is nondecreasing for \(k\ge0\). Therefore \(Dk^2+\Lambda(k)\) is continuous, strictly increasing on \(k>0\), begins at zero, and diverges; thus \(k_*\) exists and is unique.

**3. Exact exponential-moment domain.** In stationarity the elapsed time since the most recent complete reset has the exponential law \(T\sim\mathrm{Exp}(r)\), independent of the restarted diffusion and heading. Accordingly,
\[
\mathbb E[e^{kX_{\rm st}}]=r\int_0^\infty e^{-rt}
\mathbb E[e^{kX_t^\tau}]\,dt.
\tag{3}
\]
The two-sided bounds (1), together with the positive eigenfunction coefficient in step 2, sandwich the integrand for all sufficiently large \(t\) between strictly positive constants times \(e^{-(r-\Psi(k))t}\). Thus (3) is finite exactly for \(r>\Psi(k)\). At equality, the lower integrand bound is a positive constant, so the moment diverges. Since \(\Psi\) is even and strictly increasing in \(|k|\), the domain is precisely \((-k_*,k_*)\).

**4. Logarithmic probability tails, including the lower bound.** Markov's inequality at any \(k\in(0,k_*)\) shows
\[
\limsup_{x\to\infty}x^{-1}\log\Pr(X_{\rm st}>x)\le-k_*.
\tag{4}
\]
Set \(k=k_*\) and \(v=\Psi'(k_*)>0\). Tilting the law of one excursion of length \(t\) by \(e^{kX_t^\tau}\) changes its normalized cumulant-generating function to
\[
\lim_{t\to\infty}\frac1t
\log\frac{\mathbb E[e^{(k+z)X_t^\tau}]}
{\mathbb E[e^{kX_t^\tau}]}
=\Psi(k+z)-\Psi(k).
\]
Differentiability of the analytic eigenvalue and elementary exponential Chebyshev bounds, applied to small positive and negative \(z\), give \(X_t^\tau/t\to v\) in probability under this tilted law. For any \(\epsilon\in(0,v/2)\), the tilted mass in \([(v-\epsilon)t,(v+\epsilon)t]\) tends to one, uniformly for sufficiently large \(t\). Undoing the tilt yields
\[
\Pr((v-\epsilon)t\le X_t^\tau\le(v+\epsilon)t)
\ge \exp(t[\Psi(k)-k(v+\epsilon)+o(1)]).
\]
Integrate this bound in (3)'s renewal mixture over ages
\(t\in[x/(v-\epsilon),\,x/(v-\epsilon)+1]\). Since \(r=\Psi(k)\), the exponent after multiplying by \(e^{-rt}\) is at least
\(-k(v+\epsilon)t+o(t)\). Hence
\[
\liminf_{x\to\infty}x^{-1}\log\Pr(X_{\rm st}>x)
\ge -k_*\frac{v+\epsilon}{v-\epsilon}.
\]
Let \(\epsilon\downarrow0\) and combine with (4). Repeating the argument with the negative tilt \(-k_*\), for which \(\Psi'(-k_*)=-v\), gives the negative-coordinate tail with exactly the same exponent. All estimates are valid for every finite \(\tau>0\) because the logarithmic cumulant limit (2) is independent of \(\tau\).

**5. Endpoint laws and the core-versus-tail separation.** Analytic perturbation at the constant angular ground state gives
\[
\Lambda(k)=\frac{v_0^2}{2D_r}k^2+O(k^4)\quad(k\to0).
\]
The eigenvalue bound \(0\le\Lambda(k)\le v_0|k|\) then gives the two asserted asymptotics for \(k_*(r)\). For the stationary coordinate variance, independence of thermal and angular noises and the excursion formula imply
\[
\operatorname{Var}(X_{\rm st})
=2D\,\mathbb E[g_\tau(T)]
+\operatorname{Var}\left(v_0\int_0^T(1-e^{-(T-s)/\tau})\cos\theta_s\,ds\right).
\]
Direct exponential integration gives
\[
2D\,\mathbb E[g_\tau(T)]
=\frac{4D}{r(1+r\tau)(2+r\tau)}.
\tag{5}
\]
The angular term is bounded in absolute value by \(v_0T^2/(2\tau)\), hence its variance is bounded above by
\(\frac{v_0^2}{4\tau^2}\mathbb E[T^4]=6v_0^2/(\tau^2r^4)\).
Thus (5) proves
\(\operatorname{Var}(X_{\rm st})=4D/(\tau^2r^3)+O(r^{-4})\).
Combined with \(k_*^{-1}\sim\sqrt{D/r}\), this proves the claimed ratio.

## Verification

The standalone `verify.py` independently diagonalizes the angular operator using real Fourier modes \(-N,\ldots,N\), locates the unique positive root by bracketing, checks Fourier-cutoff convergence and the evenness and bounds of \(\Lambda\), and verifies the separate exact Gaussian second-moment formula by numerical age integration. It also checks both limiting asymptotics. A complete package extraction and execution gave 449 passed deterministic assertions; these finite numerical tests support the explicitly written analytic proof and are not proofs of infinite-dimensional spectral statements or logarithmic-tail limits.

## Relationship to prior work

Patel and Shee (arXiv:2602.21134v1, 2026) introduce the same complete-reset inertial active particle and derive its exact stationary moments through order four. The \(r^{-3}\) high-rate scaling of the mean-squared displacement is already established in their article. Equation (5) and its extension to the active variance are therefore used as **known-context comparison**, not asserted as a new discovery.

Franke and Sokolov (2026) already establish exponential stationary displacement tails in an underdamped **passive** Brownian resetting model. The passive specialization \(v_0=0\) is not a novelty claim here. Kumar, Sadekar and Basu (2020) study overdamped active Brownian resetting and determine marginal position distributions in limiting resetting regimes; that work is a principal active-particle precedent.

The assessed specific contribution is the exact active \(v_0>0\) principal-Mathieu **all-rate** tail equation, the corresponding sharp exponential-moment threshold and two-sided logarithmic tail theorem at **every** finite inertia, and the quantitative divergence between its far-tail length and the strongly reset stationary width. A general tilted-generator/renewal principle may supply abstract antecedents; this specialized application should not be treated as independently certified priority.

## Limitations

Only the full position–velocity–orientation Poisson resetting model is covered. The result assumes \(D,D_r,v_0,\tau,r>0\), independent Gaussian noises, and a deterministic fixed or freshly uniform heading at each full reset. It does not establish comparable tail invariance for partial resets, non-Poisson waiting times, \(D=0\), or coupled rotational inertia. It makes no asymptotic claim about the stationary density's prefactor or about the radial law. The limits \(r\to\infty\) and \(\tau\to\infty\) are not asserted to commute or to be uniform. An external originality review and an independent mathematical audit have not been performed.

## References

1. M. Patel and A. Shee, *Controlling inertial active Brownian motion via stochastic resetting*, arXiv:2602.21134v1 (first public 2026-02-24), https://arxiv.org/abs/2602.21134; full HTML https://arxiv.org/html/2602.21134 .
2. H. Franke and I. M. Sokolov, *Resetting of underdamped Brownian motion*, Physical Review E 113, 064125 (2026), https://doi.org/10.1103/qyl8-6q9h .
3. V. Kumar, O. Sadekar and U. Basu, *Active Brownian motion in two dimensions under stochastic resetting*, Physical Review E 102, 052129 (2020), https://doi.org/10.1103/PhysRevE.102.052129; arXiv:2008.03294 .
4. Standard Feynman–Kac, principal-eigenvalue, and tilted-large-deviation tools are used in their elementary compact-state-space forms as described in the proof; no external certification is claimed.
