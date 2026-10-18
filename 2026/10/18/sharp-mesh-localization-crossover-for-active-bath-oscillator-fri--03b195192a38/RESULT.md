# Sharp mesh–localization crossover for active-bath oscillator friction

## Finding

For a cyclic chain of \(n\geq3\) oscillators coupled to a run-and-tumble bath through the von Mises interaction of concentration \(p>0\), the leading-order bath-induced friction has a unique, explicitly calculable zero as a function of the tumbling rate \(\alpha>0\) in each nonconstant discrete Fourier mode. More importantly, the critical rate has two distinct sharp asymptotic laws depending on the ratio of lattice size to interaction bandwidth. In a lattice small relative to \(\sqrt p\), the threshold grows like \(p^{1/4}\sqrt n\), while at lattice size comparable to \(\sqrt p\), it grows like \(\sqrt p\) and has an explicit theta-series profile. The first law includes fixed finite chains and implies that, within the second-order reduced-friction coefficients, every fixed-rate nonconstant mode becomes negatively damped as the interaction approaches a point coupling.

Let \(L,v_0,\mu_z,N,\zeta,F_0>0\) be the ring circumference, bath particle speed, mobility, bath population, coupling and interaction amplitude. For integers \(1\leq k\leq n-1\), put
\[
 A_{n,k}(p)=\sum_{m\in\mathbb Z}\left[\frac{I_{|k+mn|}(p)}{I_0(p)}\right]^2,
 \qquad
 B_{n,k}(p)=\sum_{m\in\mathbb Z}\frac{1}{(k+mn)^2}
 \left[\frac{I_{|k+mn|}(p)}{I_0(p)}\right]^2.
\]
Here \(I_j\) is the modified Bessel function. Both sums converge, and \(A_{n,k},B_{n,k}>0\). The published weak-coupling friction formula gives its second-order coefficient exactly as
\[
 \nu^{(2)}_{n,k}(p,\alpha)=
 \frac{n\zeta^2N\mu_zF_0^2}{v_0^2}
 \left[\left(\frac{\alpha L}{\pi v_0}\right)^2B_{n,k}(p)-A_{n,k}(p)\right].
\]
Its unique zero is
\[
 \alpha_{n,k}^{\mathrm{crit}}(p)
 =\frac{\pi v_0}{L}\sqrt{\frac{A_{n,k}(p)}{B_{n,k}(p)}}.
\]
The coefficient is negative below and positive above this threshold.

**Unresolved interaction on a comparatively coarse mesh.** For any sequence \(p\to\infty\) with \(n=n(p)\geq3\), \(n/\sqrt p\to0\), and \(k=k(p)\in\{1,\dots,n-1\}\) satisfying \(k/n\to x\in(0,1)\),
\[
 \frac{A_{n,k}(p)}{\sqrt p/n}\longrightarrow\sqrt\pi,
 \qquad
 n^2B_{n,k}(p)\longrightarrow
 \frac{\pi^2}{\sin^2(\pi x)},
\]
and therefore
\[
 \boxed{\displaystyle
 \frac{\alpha_{n,k}^{\mathrm{crit}}(p)}{p^{1/4}\sqrt n}
 \longrightarrow\frac{v_0}{L}\pi^{1/4}\sin(\pi x).}
\]
For fixed \(n,k\) and fixed \(\alpha\), this also yields the **mode-independent leading negative friction**
\[
 \boxed{\displaystyle
 \frac{\nu^{(2)}_{n,k}(p,\alpha)}{\sqrt p}
 \longrightarrow -\frac{\zeta^2N\mu_zF_0^2\sqrt\pi}{v_0^2}.}
\]
The corresponding leading-order mode noise intensity, by contrast, has the finite positive limit
\[
 \lim_{p\to\infty}\widetilde B^{(2)}_{n,k}(p,\alpha)
 =\frac{\zeta^2NL^2\alpha F_0^2}
 {2v_0^2n^2\sin^2(\pi k/n)}.
\]

**Resolved critical mesh.** Suppose instead that \(n/\sqrt p\to\rho\in(0,\infty)\), and \(k/n\to x\in(0,1)\). Define the positive, absolutely convergent theta-type sums
\[
 \Theta(\rho,x)=\sum_{m\in\mathbb Z}e^{-\rho^2(m+x)^2},
 \qquad
 \Psi(\rho,x)=\sum_{m\in\mathbb Z}
 \frac{e^{-\rho^2(m+x)^2}}{(m+x)^2}.
\]
Then \(A_{n,k}(p)\to\Theta(\rho,x)\), \(pB_{n,k}(p)\to\rho^{-2}\Psi(\rho,x)\), and
\[
 \boxed{\displaystyle
 \frac{\alpha_{n,k}^{\mathrm{crit}}(p)}{\sqrt p}
 \longrightarrow\frac{\pi v_0}{L}\rho
 \sqrt{\frac{\Theta(\rho,x)}{\Psi(\rho,x)}}.}
\]
The profile interpolates continuously between the small-mesh \(p^{1/4}\sqrt n\) law as \(\rho\downarrow0\) and the nearest-aliased-harmonic law as \(\rho\uparrow\infty\):
\[
 \rho\sqrt{\Theta/\Psi}
 \sim\frac{\sin(\pi x)}{\pi^{3/4}}\sqrt\rho
 \quad(\rho\downarrow0),\qquad
 \rho\sqrt{\Theta/\Psi}
 \sim\rho\,\mathrm{dist}(x,\mathbb Z)
 \quad(\rho\uparrow\infty).
\]
These last two asymptotics are statements about the explicit theta profile, with fixed \(x\in(0,1)\), not interchanges of the separate lattice limits.

## Assumptions and scope

All parameters \(L,v_0,\mu_z,N,\zeta,F_0\) are strictly positive; \(N\) is a positive integer, \(n\geq3\) an integer, \(1\leq k\leq n-1\), and the interaction is the von Mises periodic kernel
\[
 F_p(y)=F_0e^{p\cos(2\pi y/L)}/I_0(p),\qquad p>0.
\]
The coefficients are the exact quadratic-in-\(\zeta\) terms of the weak-coupling Markovian reduction presented in Beyen, Maes and Santra (2026), Sections III.1–III.2 and Appendix C. They are not asserted to equal the friction or stationary behavior of the full microscopic model uniformly in \(p\). In particular, taking \(p\to\infty\) at fixed \(\zeta\) is a statement about the formally defined second-order coefficient, not a justified interchange with the weak-coupling expansion.

## Proof

**1. Fourier diagonalization and exact threshold.** The cited linear-response expression has positive- and negative-frequency harmonic contributions proportional to \(|\widetilde F_j|^2[(\alpha L/(\pi v_0j))^2-1]\), where \(\widetilde F_j=F_0I_{|j|}(p)/I_0(p)\). For each nonzero discrete Fourier mode, sampling the kernel at \(n\) sites aliases precisely the harmonics \(j=k+mn\), \(m\in\mathbb Z\); the eigenvalue has the prefactor shown in the finding. Since \(p>0\), every Bessel coefficient is positive, and the eigenvalue is a strictly increasing affine function of \(\alpha^2\) with exactly one positive zero. The quadratic noise coefficient equals \(\zeta^2NL^2\alpha F_0^2 B_{n,k}/(2\pi^2v_0^2)\).

**2. Uniform Bessel-localization estimate.** From the integral representation
\[
 I_j(p)=\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{p\cos t}e^{-ijt}\,dt,
\]
Laplace's method, using \(u=\sqrt p\,t\), gives the local central-limit statement
\[
 \frac{I_{j(p)}(p)}{I_0(p)}\longrightarrow e^{-y^2/2}
 \quad\text{whenever }j(p)/\sqrt p\longrightarrow y.
\]
The convergence is uniform when \(y\) stays in a compact set. Contour shifting by imaginary distance \(s>0\), together with \(I_0(p\cosh s)/I_0(p)\leq e^{p(\cosh s-1)}\), gives
\[
 \frac{I_j(p)}{I_0(p)}\leq
 \exp\{-j s+p(\cosh s-1)\}
\]
for \(j\geq0\). Optimizing at \(s=\operatorname{arsinh}(j/p)\) yields an exponential envelope bounded by \(\exp[-c\min(j^2/p,j)]\) for a fixed positive constant \(c\) and all sufficiently large \(p\). This controls the tails in the sums below; the claimed local limit is not being substituted into an infinite sum without domination.

**3. Coarse mesh.** If \(n/\sqrt p\to0\) and \(k/n\to x\in(0,1)\), write \(j=k+mn\). On compact intervals of \(j/\sqrt p\), the squared Bessel ratio equals \(e^{-j^2/p}+o(1)\) uniformly. The grid spacing in that variable is \(n/\sqrt p\to0\). Dominated Riemann summation, using step 2, yields \(nA_{n,k}/\sqrt p\to\int_{\mathbb R}e^{-u^2}du=\sqrt\pi\). Meanwhile
\[
 n^2B_{n,k}(p)=\sum_{m\in\mathbb Z}
 \frac{[I_{|k+mn|}(p)/I_0(p)]^2}{(k/n+m)^2}
 \longrightarrow\sum_{m\in\mathbb Z}\frac{1}{(x+m)^2}
 =\pi^2\csc^2(\pi x).
\]
The limit follows by dominated convergence because the denominator is uniformly bounded below by a constant times \((1+|m|)^2\), while the squared Bessel ratio lies in \([0,1]\). Substitution into the exact threshold gives the first scaling law. For fixed \(n,k,\alpha\), the negative \(-A_{n,k}\) term dominates the bounded positive \(\alpha^2B_{n,k}\) term, giving the universal friction limit; the noise limit follows from the limiting series.

**4. Critical mesh.** If \(n/\sqrt p\to\rho>0\) and \(k/n\to x\in(0,1)\), each aliased harmonic obeys \((k+mn)/\sqrt p\to\rho(x+m)\). Step 2 gives the pointwise limit of each squared Bessel ratio and a summable tail bound uniform in large \(p\). Therefore the sum defining \(A_{n,k}\) converges to \(\Theta\), while that defining \(pB_{n,k}\) converges to \(\rho^{-2}\Psi\). Substituting proves the second scaling law. For \(\rho\downarrow0\), Poisson summation of the Gaussian gives \(\Theta\sim\sqrt\pi/\rho\), while dominated convergence gives \(\Psi\to\pi^2\csc^2(\pi x)\). For \(\rho\uparrow\infty\), the smallest distance \(|x+m|\) dominates both series (two equally dominant terms at \(x=1/2\)), giving \(\Theta/\Psi\to\operatorname{dist}(x,\mathbb Z)^2\). This completes all claimed limits.

## Verification

A standalone Python program, `verify.py`, computes independently the original site-space cosine friction kernel and its cyclic Fourier eigenvalues and compares them with the aliased-sum representation. It checks the finite roots-of-unity Bessel identity, the exact modewise threshold, finite-size limits, and the theta-profile crossover using scaled Bessel functions. It passed 492 deterministic assertions (465 finite-mode assertions and 27 critical-scaling assertions). These numerical comparisons confirm finite examples but are not used to establish the infinite-parameter asymptotics.

## Relationship to prior work

Beyen, Maes and Santra, *An agitated oscillator chain* (arXiv:2605.16209v1, first public 15 May 2026; full later version arXiv:2605.16209v2), established the weak-coupling stochastic chain and Fourier friction/noise formulas; these input formulas and the sufficient all-mode anti-damping condition \(\alpha<\pi v_0/L\) are not claimed as new. Beyen, Maes and Pei, *Coupling an elastic string to an active bath: the emergence of inverse damping* (arXiv:2505.18665), derived the continuum-string friction coefficients, which likewise do not supply the present simultaneous finite-lattice/point-interaction resolution profile. The contribution assessed here is the sharp joint mesh-localization classification and its explicit theta-series interpolation, not the underlying perturbative reduction. Fourier aliasing and standard Bessel asymptotics remain established techniques.

## Limitations

The asymptotic threshold is for the quadratic weak-coupling coefficient only. Higher-order remainder bounds are not established uniformly as \(p\to\infty\), nor when \(n\) changes with \(p\); the theorem gives neither full microscopic instability nor saturation, stationary probability laws, or thermodynamic-limit interchange. The critical-mesh profile assumes \(x\in(0,1)\), so it does not describe modes with \(k/n\to0\) or \(1\). The lattice size is finite at each \(p\), and the radial interpolation limits of \(\Theta/\Psi\) are not assertions of uniformity across arbitrary rate combinations.

## References

1. A. Beyen, C. Maes, I. Santra, *An agitated oscillator chain*, arXiv:2605.16209, first submitted 2026-05-15, Sections II–III and Appendix C. https://arxiv.org/html/2605.16209v2
2. A. Beyen, C. Maes, J.-H. Pei, *Coupling an elastic string to an active bath: the emergence of inverse damping*, arXiv:2505.18665, first submitted 2025-05-24, Sections II–IV. https://arxiv.org/abs/2505.18665
3. Standard modified-Bessel integral representation, Gaussian Laplace asymptotics, Fourier roots-of-unity filtering and Mittag–Leffler cosecant-square identity; proofs of the required limiting steps are reproduced above.
