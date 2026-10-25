# Exact spectral tomography and a sharp transport–dissipation frontier for a nonreciprocal Brownian pair

## Finding

For two periodic, nonreciprocally interacting overdamped Brownian particles, their entire stationary **unwrapped cross-displacement covariance curve** determines the Fourier *power spectrum* of the interaction and its entropy-production rate. At fixed positive entropy production, the same result gives a sharp displacement-covariance bound at **every** positive observation time. The unique optimizing potential, modulo spatial phase and an additive constant, is the fundamental sinusoid.

Write \(d=D_1+D_2\), \(c=D_1^{-1}+D_2^{-1}\), \(k_n=2\pi n/L\), \(\lambda_n=dk_n^2\), and \(\widehat V_n=L^{-1}\int_0^L V(z)e^{-ik_nz}\,dz\). Set \(h_t(\lambda)=t/\lambda-(1-e^{-\lambda t})/\lambda^2\). If \(\Delta X_t=X_t-X_0\), \(\Delta Y_t=Y_t-Y_0\) are the **unwrapped** displacements, then for every \(t\ge0\)

\[
C(t):=\operatorname{Cov}(\Delta X_t,\Delta Y_t)
=2\sum_{n\ne0}k_n^2|\widehat V_n|^2h_t(\lambda_n),
\qquad
\operatorname{Cov}\binom{\Delta X_t}{\Delta Y_t}
=\begin{pmatrix}2D_1t+C(t)&C(t)\\ C(t)&2D_2t+C(t)\end{pmatrix}.
\]

In particular,

\[
C''(t)=2\sum_{n\ne0}k_n^2|\widehat V_n|^2e^{-\lambda_nt},
\qquad
\sigma=\frac c2 C''(0),
\qquad
\Delta D=\lim_{t\to\infty}\frac{C(t)}{2t}=\frac{\operatorname{Var}_{\rm Haar}(V)}{d}.
\]

Here \(\sigma\) denotes steady total entropy-production rate in the convention with unit mobility and Boltzmann constant, and \(\Delta D\) is the common enhancement of each diagonal long-time diffusion coefficient and the asymptotic off-diagonal coefficient. Exact knowledge of \(C(t)\) for all positive \(t\), together with \(D_1,D_2,L\), uniquely determines each \(|\widehat V_n|^2\) for \(n\ge1\) and therefore \(\sigma\), but does **not** identify Fourier phases.

For a fixed \(\sigma>0\) and every \(t>0\),

\[
0<C(t)\le\frac{2\sigma}{c}h_t(dk_1^2),
\qquad
\Delta D\le\frac{\sigma}{c d k_1^2}
=\frac{\sigma D_1D_2L^2}{4\pi^2(D_1+D_2)^2}.
\]

Equality in either bound holds if and only if \(V(z)=v_0+A\cos(k_1z+\phi)\) with \(A\ne0\), arbitrary \(v_0,\phi\), and \(A^2=2\sigma/(c k_1^2)\). At \(\sigma=0\), only constant potentials are admissible and \(C(t)=0\).

## Assumptions and scope

Let \(L>0\), \(D_1,D_2>0\), and a real \(L\)-periodic \(V\in C^2(\mathbb R/L\mathbb Z)\) be fixed. On real-valued lifts of two circle coordinates, consider independent standard Brownian motions \(W_1,W_2\) and the Itô equations

\[
\begin{split}
 dX_t&=-V'(X_t-Y_t)\,dt+\sqrt{2D_1}\,dW_{1,t},\\
 dY_t&=-V'(X_t-Y_t)\,dt+\sqrt{2D_2}\,dW_{2,t}.
\end{split}
\]

Initially \((X_0\bmod L,Y_0\bmod L)\) is distributed according to the **uniform joint stationary measure** on the two-torus and is independent of future Brownian increments. No confining interaction, external drift, multiplicative noise, or feedback is assumed. The forces have the **same sign** on both particles; this is the two-particle equal-magnitude attractive–repulsive (chase-and-run) case rather than a reciprocal pair. Covariances are over both stationary initial conditions and Brownian paths. The admissible optimization class is all such real \(C^2\) periodic potentials with the prescribed entropy-production rate.

## Proof

**1. Decoupled relative diffusion and stationary state.** Let \(R_t=(X_t-Y_t)\bmod L\). Subtracting the equations cancels their common drift identically:

\[
 dR_t=\sqrt{2D_1}\,dW_{1,t}-\sqrt{2D_2}\,dW_{2,t}\pmod L.
\]

Thus \(R_t\) is Brownian motion on the circle with generator \(d\,\partial_z^2\), where \(d=D_1+D_2\). Uniform \(R_0\) is invariant; simultaneously, the constant two-torus density \(L^{-2}\) is stationary because \((\partial_x+\partial_y)V'(x-y)=0\). The two steady currents are both \(-V'(x-y)/L^2\).

**2. Exactly one common random drift.** Put \(F=-V'\) and \(A_t=\int_0^tF(R_s)\,ds\). Then

\[
\Delta X_t=A_t+\sqrt{2D_1}W_{1,t},\qquad
\Delta Y_t=A_t+\sqrt{2D_2}W_{2,t}.
\]

For every *fixed* realization of both Brownian paths, integrating over the independent uniform \(R_0\) gives \(\mathbb E_{R_0}[F(R_s)]=0\) for every \(s\): a circle translation preserves Haar measure and \(\int F=0\). Therefore \(\mathbb E[A_t\mid W_1,W_2]=0\), so \(A_t\) is uncorrelated with each Brownian endpoint. Consequently the displayed displacement covariance matrix follows with \(C(t)=\operatorname{Var}(A_t)\). This cancellation is essential: uniform marginal stationarity by itself would not justify removing cross noise–drift covariances.

**3. Exact Fourier formula.** For \(n\in\mathbb Z\) let \(k_n=2\pi n/L\). The generator diagonalizes on \(e^{ik_nz}\); writing \(\widehat F_n=-ik_n\widehat V_n\) and using Haar stationarity gives the stationary force autocorrelation

\[
K(s)=\mathbb E[F(R_0)F(R_s)]
=\sum_{n\ne0}k_n^2|\widehat V_n|^2e^{-dk_n^2s}\quad(s\ge0).
\]

By Fubini, \(C(t)=2\int_0^t(t-s)K(s)\,ds\). Integrating each exponential yields the asserted \(h_t\) series. Parseval and \(V\in C^2\) ensure \(\sum k_n^2|\widehat V_n|^2<\infty\), so differentiation twice is justified, including the right second derivative at \(t=0\). Dominated convergence after dividing by \(2t\) yields

\[
\Delta D=\sum_{n\ne0}\frac{k_n^2|\widehat V_n|^2}{dk_n^2}
=\frac1d\sum_{n\ne0}|\widehat V_n|^2
=\frac{\operatorname{Var}_{\rm Haar}(V)}d.
\]

**4. Thermodynamics and inverse identification.** For the uniform stationary density \(\rho=L^{-2}\), stationary diffusion thermodynamics gives \(\sigma=\int(j_X^2/(D_1\rho)+j_Y^2/(D_2\rho))\,dx\,dy\). Using the currents of Step 1,

\[
\sigma=\left(D_1^{-1}+D_2^{-1}\right)\frac1L\int_0^L(V'(z))^2\,dz
=c\sum_{n\ne0}k_n^2|\widehat V_n|^2=\frac c2C''(0).
\]

This thermodynamic identity for the chase-and-run stationary state was already computed in the motivating source and is *not* claimed as a new standalone result. Since \(\lambda_1<\lambda_2<\cdots\), the positive exponential series

\[
C''(t)=4\sum_{n\ge1}k_n^2|\widehat V_n|^2e^{-\lambda_nt}
\]

uniquely determines its coefficients: multiply by \(e^{\lambda_1t}\) and let \(t\to\infty\) to extract the first, subtract the first exponential and iterate. All coefficient sums are finite at \(t=0\), hence each subtraction/limit is valid. This determines moduli only; phases, spatial translations, reflections and other phase ambiguities cannot be recovered.

**5. Sharp constrained optimum.** For each \(t>0\), \(h_t(\lambda)=\int_0^t(t-s)e^{-\lambda s}\,ds\) is strictly decreasing in \(\lambda>0\). Holding \(\sigma\) fixed means holding the nonnegative total mode weight \(\sum_{n\ne0}k_n^2|\widehat V_n|^2=\sigma/c\) fixed. Since every nonzero frequency satisfies \(\lambda_n\ge\lambda_1\),

\[
C(t)=2\sum_{n\ne0}k_n^2|\widehat V_n|^2h_t(\lambda_n)
\le 2(\sigma/c)h_t(\lambda_1).
\]

Strict monotonicity forces every nonzero coefficient to have \(|n|=1\) for equality. Reality then forces exactly one sinusoid plus a constant, whose amplitude follows by imposing \(\sigma\). At \(t\to\infty\), the same weighted argument uses \(h_t(\lambda)/t\to1/\lambda\), proving the second bound with the same equality case. Positivity is strict when \(\sigma>0\). This completes the theorem.

## Verification

A standalone `verify.py` independently checks Fourier normalization, the covariance series against stationary-force double-time quadrature, \(\sigma=cC''(0)/2\), strict mode-by-mode optimization, and a reproducible direct Euler–Maruyama particle simulation for a two-harmonic potential. The deterministic algebra identifies the exact coefficients; finite-step simulation is a consistency check and does not establish the theorem. Run with `python verify.py` in an environment with NumPy installed. No external data or private file is required.

## Relationship to prior work

Zhang and Garcia-Millan (arXiv:2209.09721, especially their Eqs. (1), (4), (8) and (9)) established the underlying chase-and-run model, uniform stationary distribution, and entropy-production formula. Their stationary position-correlation result is **not** the all-time covariance of unwrapped increments. Those facts are used here as inputs, not presented as new. Benois and collaborators (arXiv:2307.05408) studied tracer diffusivity enhancement in nonreciprocal mixtures, including a reduced two-body analysis, and therefore provide important overlapping context for the **long-time diffusion** corollary. The present joint time-dependent covariance, exact mode-power inversion and sharp fixed-entropy optimum for arbitrary smooth periodic forces are not supplied by the inspected statements of those papers. In a broader mathematical sense Fourier semigroups, Green–Kubo relations and spectral/variational arguments are standard; the asserted contribution is their exact joint inverse-and-optimal-transport classification in this particular nonreciprocal stochastic model.

## Limitations

The result treats exactly two particles, stationary uniform initial torus data, equal common interaction drift, periodic smooth forces and known positive diffusion constants. It does **not** handle multiple chasers, driven relative motion, multiplicative noise, arbitrary pair forces, or experimental finite-time/finite-precision inversion. Entropy production is the full two-coordinate pathwise irreversible rate with the given thermodynamic convention, not an observed coarse-grained current entropy. Fourier *phases* remain unidentifiable. Exponential spectral inversion is ill-conditioned under noisy data, even though mathematically unique with an exact continuum covariance curve. Generic Taylor-dispersion spectral theory could yield related mathematical structures; no global uniqueness claim about the wider literature is made. There is no assertion of independent scientific certification.

## References

1. Z. Zhang and R. Garcia-Millan, *Entropy production of non-reciprocal interactions*, arXiv:2209.09721 (first submitted 20 September 2022), especially Secs. I and III and the chase-and-run equations. https://arxiv.org/html/2209.09721v2
2. A. Benois, M. Jardat, V. Dahirel, V. Démery, J. Agudo-Canalejo, R. Golestanian and P. Illien, *Enhanced diffusion of tracer particles in nonreciprocal mixtures*, arXiv:2307.05408 (first submitted 11 July 2023), including the reduced two-body description and dispersion treatment. https://arxiv.org/html/2307.05408v2
3. F. Jiménez-Urias and T. W. N. Haine, *An exact solution to dispersion of a passive scalar by a periodic shear flow*, arXiv:2101.05406 (general spectral-dispersion context; abstract only inspected). https://arxiv.org/abs/2101.05406
