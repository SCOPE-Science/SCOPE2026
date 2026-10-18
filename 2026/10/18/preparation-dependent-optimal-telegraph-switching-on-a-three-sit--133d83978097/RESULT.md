# Preparation-dependent optimal telegraph switching on a three-site quantum chain

## Finding
For a three-site continuous-time quantum walk whose two hopping amplitudes are independently multiplied by stationary symmetric random-telegraph signs, the optimal switching rate for long-time **ensemble-averaged position relaxation depends on the initial vertex**. With nonzero hopping magnitude \(a\), an endpoint preparation has a uniquely optimal switching rate \(\lambda_{\mathrm e}=\sqrt{2}|a|\), whereas a center preparation has the different, uniquely optimal rate \(\lambda_{\mathrm c}=t_*|a|\), where \(t_*=2.300811817200\ldots\) is the unique positive root of
\[
32-21t^2+24t^4-4t^6=0.
\]
The corresponding optimal logarithmic population relaxation exponents are \(\sqrt2|a|\) and \(2.505998025926\ldots|a|\), respectively. The center optimum occurs exactly where two slow roots of the associated cubic meet, producing a defective-mode (exceptional-point) transition.

## Assumptions and scope
Let the vertices be \(1,2,3\). The Hamiltonian is
\[
H(t)=a\bigl[\xi_1(t)(|1\rangle\langle2|+|2\rangle\langle1|)+\xi_2(t)(|2\rangle\langle3|+|3\rangle\langle2|)\bigr],
\]
where \(a\in\mathbb R\setminus\{0\}\). The independent signals \(\xi_j\) take values \(\pm1\), flip with the same rate \(\lambda>0\), and begin independently at their stationary equiprobable distribution. At time zero the walker is localized at vertex \(k\in\{1,2,3\}\); the environmental signs and state are independent. The density matrix follows unitary Schrödinger evolution on each sample path. Define \(p_j^{(k)}(t)=\mathbb E\langle j|\rho(t)|j\rangle\), and the observable relaxation exponent
\[
\Delta_k(\lambda)=-\limsup_{t\to\infty}\frac1t\log\!\left(\sum_{j=1}^3|p_j^{(k)}(t)-1/3|\right).
\]
The limsup accommodates oscillatory zeros and polynomial prefactors at multiple spectral roots. All stated rates optimize this exponent among positive \(\lambda\), not finite-time mixing, coherence norms, or a nonstationary initial noise environment.

## Proof
**1. Exact closed subsystem.** For \(\alpha,\beta\in\{0,1\}\), let \(R^{\alpha\beta}(t)=\mathbb E[\xi_1(t)^\alpha\xi_2(t)^\beta\rho(t)]\). The sign-flip generator damps these moments at rate \(2\lambda(\alpha+\beta)\); multiplication by each sign toggles its exponent mod two. Using the imaginary nearest-neighbor coherence coordinates \(c_{12}\) and \(c_{23}\) and the real next-nearest-neighbor coherence \(D\), the initially occupied invariant real subsystem obeys
\[
\begin{aligned}
\dot p_1&=2ac_{12},& \dot p_2&=-2ac_{12}+2ac_{23},&\dot p_3&=-2ac_{23},\\
\dot c_{12}&=a(-p_1+p_2-D)-2\lambda c_{12},&
\dot c_{23}&=a(-p_2+p_3+D)-2\lambda c_{23},\\
\dot D&=a(c_{12}-c_{23})-4\lambda D.
\end{aligned}
\]
The initial condition is \(p_j(0)=\mathbf1_{j=k}\), \(c_{12}(0)=c_{23}(0)=D(0)=0\). This identity follows by applying the full stochastic Liouville generator to the noise-weighted coherences, not by assuming a Markovian master equation for the averaged density matrix.

**2. Reflection decomposition and convergence.** Set \(d=p_1-p_3\), \(q=c_{12}+c_{23}\), \(s=p_1+p_3-2p_2\), and \(r=c_{12}-c_{23}\). Then
\[
\dot d=2aq,\quad\dot q=-ad-2\lambda q;
\qquad
\dot s=6ar,\quad\dot r=-a(s+2D)-2\lambda r,\quad\dot D=ar-4\lambda D.
\]
Consequently the six-dimensional population subsystem has characteristic polynomial \(zQ_\lambda(z)P_\lambda(z)\), with
\[
Q_\lambda(z)=z^2+2\lambda z+2a^2,
\qquad
P_\lambda(z)=z^3+6\lambda z^2+(8\lambda^2+8a^2)z+24a^2\lambda.
\]
The quadratic has roots in the open left half-plane. The cubic has positive coefficients and satisfies the strict Routh--Hurwitz inequality \(6\lambda(8\lambda^2+8a^2)>24a^2\lambda\). Hence \(p_j(t)\to1/3\) for every \(\lambda>0\).

**3. Strict ordering of slow roots.** Let \(\delta_Q\) and \(\delta_P\) be minus the largest real parts of the roots of \(Q_\lambda\) and \(P_\lambda\). Directly,
\[
\delta_Q(\lambda)=\begin{cases}\lambda,&0<\lambda\le\sqrt2|a|,\\
\lambda-\sqrt{\lambda^2-2a^2},&\lambda\ge\sqrt2|a|.\end{cases}
\]
For \(\lambda\le\sqrt2|a|\), the shifted polynomial \(P_\lambda(w-\lambda)\) has coefficients \(1,3\lambda,8a^2-\lambda^2,\lambda(16a^2-3\lambda^2)\); all are positive and the Routh--Hurwitz difference is \(8a^2\lambda>0\). For \(\lambda\ge\sqrt2|a|\), set \(\delta=\lambda-\sqrt{\lambda^2-2a^2}\), so \(a^2=\lambda\delta-\delta^2/2\) and \(0<\delta\le\lambda\). The coefficients of \(P_\lambda(w-\delta)\) are
\[
1,\quad 6\lambda-3\delta,\quad 8\lambda^2-4\lambda\delta-\delta^2,
\quad \delta(8\lambda-3\delta)(2\lambda-\delta).
\]
All are strictly positive and their Routh--Hurwitz difference is \(4\lambda(6\lambda-5\delta)(2\lambda-\delta)>0\). Thus **\(\delta_P>\delta_Q\) for every positive switching rate**. Each endpoint has nonzero \(d(0)\), and its quadratic sector cannot vanish identically; therefore \(\Delta_1=\Delta_3=\delta_Q\). The displayed formula shows its unique global maximum at \(\lambda=\sqrt2|a|\).

**4. Center-only cubic and its unique optimum.** For a center preparation, \(d(0)=q(0)=0\), \(s(0)=-2\), and \(r(0)=D(0)=0\). The Laplace transform is
\[
\widehat s(z)=-2\frac{(z+2\lambda)(z+4\lambda)+2a^2}{P_\lambda(z)}.
\]
The numerator cannot share a root with \(P_\lambda\): a common root would force \(z=-4\lambda\), where the numerator equals \(2a^2\ne0\). Consequently all cubic modes contribute (with the appropriate nonzero principal part at coalescence), and \(\Delta_2=\delta_P\).

Scaling \(\lambda=t|a|\), the discriminant of \(P_\lambda\) is
\[
-64a^6(32-21t^2+24t^4-4t^6).
\]
Writing \(x=t^2\), the parenthetical polynomial has two positive stationary points \(x=1/2\) and \(x=7/2\), at which it equals \(27\) and \(81\), respectively. It has exactly one positive zero, \(t_*>\sqrt{7/2}\). For \(0<\lambda<t_*|a|\), the cubic has one real root \(-u\) with \(3\lambda<u<4\lambda\), and a complex-conjugate pair with common real part \(-3\lambda+u/2\). Hence \(\delta_P=3\lambda-u/2\). The real root satisfies
\[
u^3-6\lambda u^2+(8\lambda^2+8a^2)u-24a^2\lambda=0.
\]
Its derivative is positive by implicit differentiation: the derivative of \(\delta_P\) has the sign of \(6F_u+F_\lambda\), with \(F\) the left-hand polynomial. Eliminating \(a^2\) using \(F=0\) and writing \(w=u/\lambda-3\in(0,1)\) gives
\[
6F_u+F_\lambda=\frac{\lambda^2}{w}(9w^3+7w^2-9w+9)>0.
\]
At \(t=t_*\), the depressed cubic in \(y=z+2\lambda\) acquires a double positive root \(y_*=|a|\sqrt{(4t_*^2-8)/3}\). It follows that
\[
\delta_P(t_*|a|)=|a|\left(2t_*-\sqrt{\frac{4t_*^2-8}{3}}\right).
\]
For \(\lambda>t_*|a|\), the three roots are distinct and real, and the slowest is \(-g\) with \(0<g<2\lambda\). Implicit differentiation of \(P_\lambda(-g)=0\) yields \(g'=P_{\lambda,\lambda}(-g)/P_{\lambda,z}(-g)\). The denominator is positive because \(-g\) is the largest simple root; using the root equation, the numerator becomes
\[
P_{\lambda,\lambda}(-g)=-\frac{g(3g^2-16\lambda g+24\lambda^2)}{3\lambda-g}<0,
\]
since the quadratic bracket is positive (negative discriminant). Thus \(\delta_P=g\) strictly decreases after the double-root point. Continuity yields a **unique global maximum** at \(t_*|a|\). The double root can introduce a polynomial time prefactor; it does not change the logarithmic exponent.

## Verification
Run `python verify.py` with the versions specified in `requirements.txt`. The script constructs the full four-environment-state stochastic Liouvillian (a \(36\)-dimensional complex system), compares its averaged position probabilities with the derived \(6\)-dimensional real subsystem at 100 parameter/initial-condition/time combinations, checks the characteristic factorization and discriminant, then tests spectral-gap inequalities over a 220-point parameter grid. It reports `VERIFY_OK dense_populations=100 cubic_gap_grid=220 critical_rate=2.300811817200 center_gap=2.505998025927 end_gap=1.414213562373`. These calculations check finite instances; the all-rate and all-time assertions follow from the preceding analytic arguments.

## Relationship to prior work
Benedetti, Buscemi, Bordone and Paris (arXiv:1510.08652, first posted 2015-10-29) study continuous-time quantum walks with independently fluctuating telegraph hopping links on substantially larger lattices; the published treatment uses numerical noise averaging and does not provide this three-site population-specific spectral factorization or the two global switching-rate optimizers. Rossi and collaborators (arXiv:1707.01441) investigate spatially correlated dynamic lattice noise and numerical transport behavior, a different noise regime. Kurt, Rossi and Piilo (arXiv:1909.00167) analyze a three-site transport system with telegraph fluctuations of site energies and additional baths; their noise acts diagonally rather than independently on the two hoppings. The stochastic Liouville construction and cubic discriminants are standard methods, not claimed as innovations. The comparison concerns the **combined exact observable-sector theorem and preparation-dependent optimum**, not merely the telegraph model. Publication priority remains subject to independent scrutiny.

## Limitations
The two switching signals must be independent and identically distributed, initially stationary and symmetric; the two bond magnitudes must be equal. There are no additional baths, static site energies, or correlated sign flips. Relaxation is of ensemble-averaged **populations**, not convergence of single trajectories nor the full density matrix. The logarithmic exponent does not optimize finite-time detection, total variation mixing thresholds, or experimental readout with overhead. A general spectral method elsewhere could imply this specialization despite the focused comparisons.

## References
1. C. Benedetti, F. Buscemi, P. Bordone, M. G. A. Paris, *Non-Markovian continuous-time quantum walks on lattices with dynamical noise*, arXiv:1510.08652 (2015), https://arxiv.org/abs/1510.08652.
2. M. Rossi et al., *Continuous-time quantum walks on spatially correlated noisy lattices*, arXiv:1707.01441 (2017), https://arxiv.org/abs/1707.01441.
3. A. Kurt, M. A. C. Rossi, J. Piilo, *Efficient quantum transport in a multi-site system combining classical noise and quantum baths*, arXiv:1909.00167 (2019), https://arxiv.org/abs/1909.00167.
