# Reentrant non-Gaussianity in intermittent run-and-tumble diffusion

## Finding
Consider a one-dimensional intermittent particle with active velocities \(+1,-1\), unit reversal rate, and a passive Brownian state with diffusivity \(D\ge 0\). Let active-to-passive switching occur at rate \(b>0\), and passive-to-active switching at rate \(c>0\), choosing the new active direction fairly. Let \(X_t\) denote displacement, and define excess kurtosis \(\mathcal K_t=\kappa_4(X_t)/\kappa_2(X_t)^2\). For any initial internal-state distribution and deterministic finite \(X_0\),

\[
\lim_{t\to\infty}t\mathcal K_t
=\frac{6cP_{b,c}(D)}{(b+2)(b+c)[c+b(b+2)D]^2},
\]
where
\[
P_{b,c}(D)=b(b+2)^3D^2-b(b+2)(4+3b+c)D+b(b+2)-c(b+c).
\]
The two distinct real roots are
\[
D_{\pm}=\frac{4+3b+c\pm(b+c)\sqrt{(8+5b)/b}}{2(b+2)^2},\qquad D_-<D_+.
\]
Write \(c_*(b)=[\sqrt{b(8+5b)}-b]/2\). If \(0<c<c_*(b)\), both roots are positive, and the long-time excess-kurtosis coefficient is strictly positive for \(0\le D<D_-\), strictly negative for \(D_-<D<D_+\), and strictly positive for \(D>D_+\). If \(c=c_*(b)\), the lower root is \(D_-=0\); the coefficient is negative on \(0<D<D_+\) and positive for \(D>D_+\). If \(c>c_*(b)\), only \(D_+\) is positive, with a negative coefficient below it and a positive coefficient above it. It vanishes at the displayed roots; no sign assertion is made for finite-time kurtosis exactly at those roots.

In particular, equal active-to-passive and passive-to-active rates \(b=c=r\) admit **two positive sign reversals exactly when \(0<r<2\)**. For \(r=1\),
\[
\lim_{t\to\infty}t\mathcal K_t=\frac{27D^2-24D+1}{(3D+1)^2},\qquad D_\pm=\frac{4\pm\sqrt{13}}9.
\]
Meanwhile the effective diffusivity \(\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)=[c+b(b+2)D]/[(b+2)(b+c)]\) increases strictly with \(D\). Therefore this two-step sign reversal occurs without nonmonotone mean-square dispersion.

## Assumptions and scope
The internal chain \(J_t\in\{+,-,0\}\) has row generator
\[
Q=\begin{pmatrix}-(1+b)&1&b\\1&-(1+b)&b\\c/2&c/2&-c\end{pmatrix}.
\]
Conditional on \(J_t=+,-,0\), the particle has respective displacement increments \(+dt,-dt,\sqrt{2D}\,dW_t\), with independent standard Brownian motion \(W_t\). There is no spatial resetting and no boundary. All statements concern the long-time, fixed-parameter limit \(t\to\infty\), and \(D\ge0\) includes an immobile passive phase. The unit speed and reversal-rate conventions fix the natural time and length scales. The moment-generating function exists near the origin for every finite time.

## Proof
The finite, irreducible internal chain permits an analytic simple dominant eigenvalue \(\lambda(k)\), near \(k=0\), of the Feynman–Kac tilted generator \(M(k)=Q+\operatorname{diag}(k,-k,Dk^2)\). Symmetry gives \(\lambda(k)=L_2k^2+L_4k^4+O(k^6)\). Its characteristic determinant, with \(z=k^2\), is exactly
\[
\begin{aligned}
F(\lambda,z)={}&[c+b(b+2)D]z-Dz^2-(b+2)(b+c)\lambda\\
&+[1+2(b+1)D]z\lambda-(2+2b+c)\lambda^2\\
&+Dz\lambda^2-\lambda^3.
\end{aligned}
\]
Matching the coefficients of \(z\) and \(z^2\) gives
\[
L_2=\frac{c+b(b+2)D}{(b+2)(b+c)}>0,\qquad
L_4=\frac{cP_{b,c}(D)}{(b+2)^3(b+c)^3}.
\]
Perron–Frobenius perturbation for an irreducible finite-state generator (or its spectral projection) gives \(\log\mathbb E e^{k(X_t-X_0)}=t\lambda(k)+O(1)\) with locally analytic, differentiable remainder for any nonzero initial probability vector. Therefore \(\kappa_2(X_t)=2tL_2+O(1)\) and \(\kappa_4(X_t)=24tL_4+O(1)\), yielding the asserted limit \(6L_4/L_2^2\).

The discriminant of the quadratic \(P_{b,c}(D)\) equals \(b(b+2)^2(b+c)^2(8+5b)>0\); the quadratic opens upward and has strictly negative linear coefficient. Its larger root is positive. The constant coefficient \(b(b+2)-c(b+c)\) has the same sign as \(c_*(b)-c\), proving the complete nonnegative-diffusivity root and sign classification. Substituting \(b=c=r\) gives \(r<2\) as the exact two-positive-root criterion, and the stated special case follows by substitution. Finally \(\partial_D L_2=b/(b+c)>0\).

A physically distinct consistency check isolates the quadratic \(D^2\) contribution: writing \(T_0(t)\) for passive occupation time, the passive Brownian displacement conditioned on the internal path is Gaussian with variance \(2DT_0(t)\). For stationary internal state, \(\operatorname{Cov}(\mathbf1_{\{J_0=0\}},\mathbf1_{\{J_s=0\}})=bc(b+c)^{-2}e^{-(b+c)s}\), hence \(\lim_{t\to\infty}\operatorname{Var}(T_0(t))/t=2bc/(b+c)^3\). The \(D^2\) coefficient in \(\kappa_4(X_t)/t\) must consequently equal \(24bc/(b+c)^3\), precisely the coefficient of \(24L_4\). In particular the high-passive-diffusivity sign is necessarily positive.

## Verification
The standalone script `verify.py`, using SymPy, NumPy and SciPy, reconstructs the exact determinant and cumulant coefficients, factors the quadratic discriminant, verifies both roots, and compares the three-state resolvent with the renewal propagator of the primary source (including its equal-rate specialization). It checks the passive-occupation variance coefficient independently and propagates the first four conditional raw moments of the forward generator for 42 numerical finite-time cases. Run `python verify.py` from a directory with those libraries available. These finite-time tests support, but do not replace, the complete analytic proof. For \(b=c=1\), the two threshold diffusivities are approximately \(0.0438276361\) and \(0.8450612528\).

## Relationship to prior work
Santra, Olsen and Gupta (arXiv:2408.16643, first public version August 29, 2024) introduced the alternating active/passive model and its Fourier–Laplace renewal transform, computed dispersion and discussed higher cumulants. Their exact equal-rate Fourier–Laplace transform (Section 5) is reproduced independently by the tilted internal-state generator here; it is not claimed as new. The present result is the complete explicit two-root physical diffusivity classification, its sharp switching threshold, and the associated nonmonotone sign versus monotone effective diffusion. Their displayed fourth-cumulant asymptotic expression was not used as a premise: direct expansion of their equal-rate transform and independent conditional-moment propagation yield the coefficient proved here, including a strictly positive quadratic dependence on \(D\) required by passive-occupation fluctuations. The printed coefficient should therefore not be assumed equivalent without reconciliation. Datta, Beta and Großmann (arXiv:2406.15277) analyze a broader intermittent self-propelled run/turn model mainly through velocity correlations and second-order transport; their model and results do not state this two-root long-time fourth-cumulant boundary. General finite-state additive-process spectral methods are standard; the new claim is the model-specific complete sign law and its physical interpretation.

## Limitations
The result does not classify finite-time excess kurtosis at the two asymptotic zeros, higher cumulants, general non-Poisson switching, or asymmetric reversal/speed rules. An explicit published generator or cumulant formula might implicitly entail this classification; publication priority is not independently established. The observed mismatch between the source's displayed long-time cumulant expression and its own exact equal-rate transform is a literature-comparison risk, not a premise on which the proof relies. The result does not claim experimentally observed transitions or non-Gaussian stationary position distributions (the process is spatially unconfined).

## References
1. I. Santra, K. S. Olsen and D. Gupta, *Dynamics of switching processes: general results and applications to intermittent active motion*, arXiv:2408.16643, first public version 2024-08-29, https://arxiv.org/abs/2408.16643; *Soft Matter* **20** (2024), 9360–9372, https://doi.org/10.1039/D4SM01054J.
2. A. Datta, C. Beta and R. Großmann, *The random walk of intermittently self-propelled particles*, arXiv:2406.15277, first public version 2024-06-21, https://arxiv.org/abs/2406.15277.
