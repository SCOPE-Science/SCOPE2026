# Fourier-zero quadrature rigidity with an explicit square-root transport law

## Finding

For every integer \(N\ge3\), a probability measure on the circle with vanishing Fourier coefficients \(1,\ldots,N-1\) has a uniquely minimizing quadratic geodesic moment, and its deficit controls its transport distance to the regular \(N\)-point measure. Specifically, set \(s_N=(-1)^{N-1}\), \(\Theta_N=\{\theta:e^{iN\theta}=s_N\}\), and \(\nu_N=N^{-1}\sum_{\theta\in\Theta_N}\delta_\theta\). If
\[
\Delta_N(\nu)=\int d(\theta,0)^2\,d\nu(\theta)-\frac{\pi^2}{3}\left(1-\frac1{N^2}\right),
\]
then for every admissible \(\nu\),
\[
\Delta_N(\nu)\ge \frac{4}{N^2\binom{2N}{N}}\big(1-s_N\operatorname{Re}\widehat\nu(N)\big)\ge0,
\]
\[
\int d(\theta,\Theta_N)^2\,d\nu(\theta)\le\frac{\pi^2}{8}\binom{2N}{N}\Delta_N(\nu),
\]
\[
W_1^{\mathbb T}(\nu,\nu_N)\le\pi\left(1+\frac{\pi N(N-1)}4\right)\sqrt{\frac{\binom{2N}{N}\Delta_N(\nu)}8}.
\]
The baseline equality case is precisely \(\nu=\nu_N\). For each fixed \(N\), the transport exponent \(1/2\) cannot be increased.

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) with shortest-arc metric \(d\), the Fourier convention is \(\widehat\nu(k)=\int e^{ik\theta}\,d\nu(\theta)\), and \(W_1^{\mathbb T}\) is the 1-Wasserstein metric for \(d\). Measures are arbitrary Borel probability measures; no smoothness, discrete-support, or density assumption is made. The constraint is \(\widehat\nu(k)=0\) for EVERY \(1\le k<N\). The regular node set is centered at zero for odd \(N\) and consists of mid-arc roots for even \(N\). The explicit estimates hold simultaneously for every integer \(N\ge3\); constants are valid but not asserted optimal.

## Proof

**1. A universal Hermite minorant.** Set \(h(y)=(\arccos y)^2\) for \(-1\le y\le1\). With \(v=1-y\), write \(h(1-v)=\sum_{j\ge1}c_jv^j\). The elementary differential equation \((1-y^2)h''-yh'=2\) gives
\[
c_1=2,\qquad c_{j+1}=\frac{j^2}{(j+1)(2j+1)}c_j>0,\qquad c_N=\frac{2^{N+1}}{N^2\binom{2N}{N}}.
\]
This convergent positive-coefficient expansion, valid for \(0\le v<2\), proves \((-1)^Nh^{(N)}(y)\ge N!c_N\) for \(-1<y<1\). If \(N=2m\), let \(q\) be the degree-\(<N\) Hermite polynomial matching \(h,h'\) at \(\cos((2j-1)\pi/N)\), \(1\le j\le m\). If \(N=2m+1\), let \(q\) match \(h\) at \(y=1\) and \(h,h'\) at \(\cos(2\pi j/N)\), \(1\le j\le m\). The standard Hermite remainder (for \(-1<y<1\)) and the derivative sign imply
\[
h(y)-q(y)\ge c_N2^{1-N}\big(1-s_N T_N(y)\big),
\]
where \(T_N(\cos\theta)=\cos(N\theta)\). Indeed, the nonnegative nodal products are \(2^{1-N}(1-T_N(y))\) for odd \(N\), and \(2^{1-N}(1+T_N(y))\) for even \(N\). The inequality extends to \(y=-1\) and \(y=1\) by continuity. Thus
\[
d(\theta,0)^2-q(\cos\theta)\ge \frac4{N^2\binom{2N}{N}}\big(1-s_N\cos(N\theta)\big).
\]

**2. Exact deficit and rigidity.** Since \(q(\cos\theta)\) has Fourier frequencies at most \(N-1\), the moment constraint gives \(\int q(\cos\theta)d\nu=\int q(\cos\theta)d\nu_N\). Every node of \(\nu_N\) is a contact point; hence the latter is \(\int d(\theta,0)^2d\nu_N=\pi^2(1-N^{-2})/3\), by summing squares of centered equispaced angles. Integrating the preceding minorant proves the Fourier-mode remainder. If \(\Delta_N(\nu)=0\), then the remainder forces \(\cos(N\theta)=s_N\) almost surely. Such a measure lies on \(\Theta_N\), and discrete Fourier inversion using the original \(N-1\) zero modes forces all \(N\) masses to equal \(1/N\).

**3. Concentration near the node set.** Let \(\rho(\theta)=d(\theta,\Theta_N)\le\pi/N\). Then \(|e^{iN\theta}-s_N|=2\sin(N\rho(\theta)/2)\ge 2N\rho(\theta)/\pi\). Taking squares and expectations, \(\mathbb E|e^{iN\theta}-s_N|^2=2(1-s_N\operatorname{Re}\widehat\nu(N))\), gives the stated mean-square node-distance bound.

**4. Transport of masses.** Let \(R\) be a measurable nearest-node map, \(\nu'=R_\#\nu\), and \(\varepsilon=\int\rho\,d\nu\). Projection costs at most \(\varepsilon\) in \(W_1\), and \(\varepsilon\le\sqrt{\binom{2N}{N}\Delta_N/8}\,\pi\). For \(1\le k<N\),
\[
|\widehat\nu'(k)|\le k\varepsilon
\]
by the Lipschitz bound for a character and \(\widehat\nu(k)=0\). Inversion of the \(N\)-point discrete Fourier transform yields \(\|\nu'-\nu_N\|_{TV}\le\frac12\sum_{k=1}^{N-1}|\widehat\nu'(k)|\le N(N-1)\varepsilon/4\). Since the circle diameter is \(\pi\), \(W_1(\nu',\nu_N)\le\pi\|\nu'-\nu_N\|_{TV}\). Combine triangle inequality and the bound for \(\varepsilon\).

**5. Optimality of the exponent.** For \(0<h<\pi/(2N)\), put \(\nu_h=\frac12(\tau_h)_\#\nu_N+\frac12(\tau_{-h})_\#\nu_N\), where \(\tau_h(\theta)=\theta+h\). Its first \(N-1\) Fourier coefficients vanish. Each canonical representative of every regular node is more than \(h\) from the endpoints \(-\pi,\pi\), so direct expansion of squared angles gives \(\Delta_N(\nu_h)=h^2\). Coupling each shifted point to its generating node costs \(h\); the 1-Lipschitz test \(\theta\mapsto d(\theta,\Theta_N)\) has expectation \(h\) under \(\nu_h\) and zero under \(\nu_N\). Hence \(W_1(\nu_h,\nu_N)=h\), excluding any bound of order \(\Delta_N^\alpha\) for \(\alpha>1/2\) with fixed \(N\).

**6. Real-line consequence.** If a real random variable \(X\) has finite variance, mean \(m\), and \(\mathbb E e^{iktX}=0\) for \(k=1,\ldots,N-1\), with \(t\ne0\), then its centered residue law \(\nu\) under \(t(X-m)\bmod2\pi\) meets the hypotheses. Since \(d(t(X-m),0)^2\le t^2(X-m)^2\), one obtains
\[
t^2\operatorname{Var}(X)\ge\frac{\pi^2}3(1-N^{-2}),
\]
with equality only for the uniform law at \(m+\theta_j/t\), the canonical representatives of \(\Theta_N\), and near-equality quantitatively controls the centered residue law by the same transport bound with the variance deficit substituted for \(\Delta_N\).

## Verification

The standalone `checker.py` recomputes coefficient recurrence and Chebyshev polynomials in exact rational arithmetic for finitely many degrees and checks the proposed sharp exponent family numerically. These checks are diagnostic and are not a substitute for the all-degree Hermite proof. The nonstandard analytic steps are the positive-coefficient expansion, the two parity-sensitive nodal factorizations, and exact Fourier inversion, all derived above.

## Relationship to prior work

The Gaussian/Gauss–Radau quadrature and Hermite interpolation principles are classical. An (2026, Theorem 7.2) proves Wasserstein near-quadrature for a different, truncated-support moment problem arising from spherical self-polar geometry; it does not give a geodesic-squared Fourier-deficit estimate for arbitrary circle measures. Borda (2020, Theorem 1) controls transport by Fourier-transform discrepancy and a smoothing parameter, rather than by the nonnegative geodesic energy deficit under a block of vanishing frequencies. Huang (2025) studies a single first characteristic-function zero rather than the multi-zero rigidity and transport conclusion. The newly claimed part here is the explicit \(N\)-dependent coercive Fourier remainder together with complete center-anchored equality and sharp-order transport stability, for arbitrary circle measures; mere Gaussian-quadrature exactness is not claimed as new.

## Limitations

No optimality is claimed for the numerical coefficients in the Fourier remainder, squared-distance, or transport upper bounds. Those coefficients grow rapidly with \(N\). The square-root exponent, but not its constant, is sharp. The result only treats consecutive vanished frequencies beginning at one and the squared distance to a *fixed* reference point; it does not classify arbitrary missing-frequency sets or other costs. Historical priority beyond inspected relevant sources is not certified; independent assessment has not been performed.

## References

1. C. An, *Dual Geometry of Spherical Designs: Polarity, Self-Polar Rigidity, and Quadrature Structure*, arXiv:2609.02439v1 (public 2026-09-02), especially Theorem 7.2 (a distinct truncated-support moment problem), https://arxiv.org/pdf/2609.02439.
2. B. Borda, *Berry–Esseen smoothing inequality for the Wasserstein metric on compact Lie groups*, arXiv:2005.04925v2 (2020), Theorem 1 (Fourier smoothing rather than energy-deficit rigidity), https://arxiv.org/pdf/2005.04925.
3. Y. C. Huang, *Estimating the first zero of the characteristic function: a new approach based on the central moments* (public April 2025; DOI:10.13140/RG.2.2.18421.08165), https://www.researchgate.net/publication/390470415_Estimating_the_first_zero_of_the_characteristic_function_a_new_approach_based_on_the_central_moments.
4. Classical Gaussian and Gauss–Radau quadrature, Hermite interpolation, and elementary Chebyshev identities (background methods, not claimed new).
