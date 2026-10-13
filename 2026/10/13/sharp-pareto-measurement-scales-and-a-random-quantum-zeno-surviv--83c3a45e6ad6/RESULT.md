# Sharp Pareto measurement scales and a random quantum-Zeno survival law

## Finding

A two-level system undergoing randomly spaced projective survival measurements has a sharp change in its surviving-probability fluctuations when the tail exponent of the observation intervals crosses two. For a fixed number of observations, the correctly normalized survival probability has a nondegenerate Poisson-point-process limit below the quadratic-moment threshold, a logarithmically corrected deterministic limit exactly at the threshold, and a finite-variance deterministic limit above it. These are three regimes of one explicitly defined physical protocol, not claims about a fixed total observation time.

**Theorem.** Let \(\Omega>0\), \(\alpha>0\), and \(c>0\). Let \(X_1,X_2,\ldots\) be independent with Pareto tail \(\Pr\{X_j>x\}=x^{-\alpha}\) for \(x\ge1\). Begin a qubit in \(|0\rangle\), evolve with Hamiltonian \(H=\hbar\Omega\sigma_x\) between observations, and perform \(m\) successive projective tests onto \(|0\rangle\) at independent intervals \(\tau_{m,j}=b_mX_j/\Omega\), where

\[
 r_m=\begin{cases}
 m^{-1/\alpha},&0<\alpha<2,\\
 (m\log m)^{-1/2},&\alpha=2,\quad m\ge2,\\
 m^{-1/2},&\alpha>2,
 \end{cases}\qquad b_m=c r_m.
\]

The probability that all tests succeed, **conditional on the sampled intervals**, is the random variable

\[
 P_m=\prod_{j=1}^{m}\cos^2(b_mX_j).
\]

As \(m\to\infty\):

1. If \(0<\alpha<2\), then \(P_m\) converges in distribution to \(P_{\alpha,c}\in(0,1)\), almost surely positive and nonconstant. If \(\mathcal N_{\alpha,c}\) is a Poisson point process on \((0,\infty)\) with intensity \(\alpha c^\alpha z^{-1-\alpha}\,dz\), then

\[
P_{\alpha,c}\ \overset{d}=\ \prod_{z\in\mathcal N_{\alpha,c}}\cos^2 z,
\quad
\mathbb E[P_{\alpha,c}^{s}]
=\exp\left\{-\alpha c^\alpha\int_0^\infty
(1-|\cos z|^{2s})z^{-1-\alpha}\,dz\right\},\quad s>0.
\]

The infinite product converges to a strictly positive random variable, and, writing
\(K_\alpha=\pi 2^{\alpha-2}/[\Gamma(\alpha)\sin(\pi\alpha/2)]\), its two leading moments are

\[
\mathbb E P_{\alpha,c}=e^{-c^\alpha K_\alpha},\qquad
\mathbb E P_{\alpha,c}^{2}
=e^{-c^\alpha K_\alpha(1+2^{\alpha-2})}.
\]

In particular, its variance is strictly positive for every \(0<\alpha<2\) and \(c>0\).

2. If \(\alpha=2\), then \(P_m\to e^{-c^2}\) in probability.

3. If \(\alpha>2\), then \(P_m\to e^{-c^2\alpha/(\alpha-2)}\) in probability.

These normalizations are **sharp** in the following sense: for any positive sequence \(b_m\to0\), with \(r_m\) as above, if \(b_m/r_m\to0\) then \(P_m\to1\) in probability, while if \(b_m/r_m\to\infty\) then \(P_m\to0\) in probability.

## Assumptions and scope

The quantum state is a single isolated qubit, the unitary Hamiltonian is time independent, the tests are ideal rank-one projective survival tests, and the sampled inter-observation durations are independent Pareto variables with an \(m\)-dependent common physical scale. The random variable \(P_m\) is the **conditional success probability** given the observation times, rather than the individual Bernoulli outcome of one experimental run. The number of tests is fixed, not the total laboratory time. For \(\alpha\le1\), even the raw waiting time has infinite mean; no finite-mean renewal assumption is invoked. In the sharpness assertion, the scale sequence is positive and tends to zero. All convergence statements are for \(m\to\infty\), with \(\alpha,c,\Omega\) fixed.

## Proof

**Step 1: Exact conditional survival and scale of the single-interval loss.** The survival amplitude after an interval \(\tau\) is \(\langle0|e^{-i\Omega\tau\sigma_x}|0\rangle=\cos(\Omega\tau)\). A successful measurement resets the state to \(|0\rangle\), so multiplication gives the stated \(P_m\) exactly. Let \(v(b)=\mathbb E\sin^2(bX_1)\). Using the Pareto density and substituting \(z=bx\) gives

\[
v(b)=\alpha b^\alpha\int_b^\infty\sin^2z\;z^{-1-\alpha}\,dz.
\]

For \(0<\alpha<2\), dominated convergence after dividing by \(b^\alpha\) yields \(v(b)\sim K_\alpha b^\alpha\), where the integral is finite at zero because \(\sin^2 z=O(z^2)\). For \(\alpha=2\), split the integral at one to obtain \(v(b)=2b^2\log(1/b)+O(b^2)\). For \(\alpha>2\), dominated convergence applied to \(\sin^2(bX_1)/b^2\) gives \(v(b)\sim b^2\mathbb E X_1^2=\alpha b^2/(\alpha-2)\). The constant follows from the standard convergent cosine integral

\[
\int_0^\infty\frac{1-\cos(tz)}{z^{1+\alpha}}\,dz
=\frac{\pi t^\alpha}{2\Gamma(1+\alpha)\sin(\pi\alpha/2)},
\qquad 0<\alpha<2,\quad t>0.
\]

Here \(K_\alpha=\alpha\int_0^\infty\sin^2z\,z^{-1-\alpha}\,dz\).

**Step 2: Limit below two.** For every \(s>0\), independence gives

\[
\mathbb E P_m^{s}=\left[1-\alpha b_m^\alpha
\int_{b_m}^\infty(1-|\cos z|^{2s})z^{-1-\alpha}\,dz\right]^m.
\]

When \(b_m=cm^{-1/\alpha}\), the integral converges as its lower endpoint tends to zero: \(1-|\cos z|^{2s}=O_s(z^2)\) there, and it is bounded by one at infinity. Since \(mb_m^\alpha=c^\alpha\), the displayed moments converge to the formula in the theorem. To identify the limit, take a Poisson point process with the stated intensity. Its Laplace functional applied to the nonnegative test \(-s\log(\cos^2 z)\) produces exactly those moments. This test is integrable near zero, and the intensity has finite mass away from any neighborhood of zero; the process almost surely hits none of the discrete zeros of cosine. Thus the sum of the logarithmic losses is finite and the infinite product is strictly positive. Its value is less than one almost surely because the process has infinitely many points near zero, none concentrated on cosine extrema. The limiting law on \([0,1]\) is determined by its integer moments, so convergence of moments establishes weak convergence.

The identity \(\cos^4z=(3+4\cos2z+\cos4z)/8\), together with the cosine integral above, gives
\(\alpha\int_0^\infty(1-\cos^4z)z^{-1-\alpha}\,dz=K_\alpha(1+2^{\alpha-2})\). Hence the two moments. Since \(2^{\alpha-2}<1\), their difference \(e^{-c^\alpha K_\alpha(1+2^{\alpha-2})}-e^{-2c^\alpha K_\alpha}\) is positive.

**Step 3: Borderline exponent two.** Write \(b=b_m=c/\sqrt{m\log m}\). Fix \(0<\varepsilon<\pi/4\). The probability that any \(bX_j>\varepsilon\) is at most \(m(b/\varepsilon)^2=c^2/(\varepsilon^2\log m)\to0\). Define the truncated squared-angle sum

\[
S_m=b^2\sum_{j=1}^{m}X_j^2\mathbf 1_{\{bX_j\le\varepsilon\}}.
\]

For sufficiently large \(m\), the exact Pareto integrals give \(\mathbb E S_m=2mb^2\log(\varepsilon/b)\to c^2\), while

\[
\operatorname{Var}(S_m)\le mb^4\mathbb E[X_1^4\mathbf 1_{\{X_1\le\varepsilon/b\}}]
=mb^4((\varepsilon/b)^2-1)\le c^2\varepsilon^2/\log m\to0.
\]

On the event that every angle is at most \(\varepsilon\), the Taylor estimate \(-\log(\cos^2z)=z^2[1+O(\varepsilon^2)]\) holds uniformly. Thus \(-\log P_m\to c^2\) in probability after first letting \(m\to\infty\), then \(\varepsilon\downarrow0\).

**Step 4: Exponent above two.** For \(\alpha>2\) and \(b=cm^{-1/2}\), a union bound gives
\(\Pr\{\max_j bX_j>\varepsilon\}\le\varepsilon^{-\alpha}c^\alpha m^{1-\alpha/2}\to0\). The weak law for the integrable \(X_1^2\) yields \(b^2\sum_jX_j^2\to c^2\alpha/(\alpha-2)\) in probability. The same uniform Taylor estimate for \(-\log(\cos^2z)\) proves the third limit.

**Step 5: Sharpness.** Independence supplies \(\mathbb E P_m=(1-v(b_m))^m\). By Step 1, \(m v(b_m)\to0\) when \(b_m/r_m\to0\), and \(m v(b_m)\to\infty\) when \(b_m/r_m\to\infty\) and \(b_m\to0\). For the borderline case the latter fact follows from \(mb_m^2\log(1/b_m)\to\infty\): if \(b_m\ge r_m\), the function \(b^2\log(1/b)\) is increasing for small \(b\), and an unbounded ratio forces a divergent normalized product (split according as the ratio is below or above \(m^{1/8}\)). Therefore \(\mathbb E P_m\to1\) or zero respectively. Since \(0\le P_m\le1\), convergence in expectation to an endpoint implies convergence in probability, completing the proof.

## Verification

The standalone program `verify_pareto_zeno.py` numerically compares survival-product moments with the analytic limit for two infinite-variance Pareto exponents and a non-unit amplitude, samples both deterministic regimes, and independently integrates the Fourier formula at exponent one. The program is a reproducible **finite check** using NumPy and SciPy; the asymptotic and infinite-product conclusions rest on the proof above, not those simulations.

## Relationship to prior work

Shushin's 2010 analysis (arXiv:1011.1542v1) treats random-time measurements and heavy-tailed renewal distributions, particularly through an averaged stochastic Liouville evolution at fixed elapsed time. Gherardini and colleagues (arXiv:1509.08122v1, Sections 2–4 and 6 and their appendices) derive the conditional product formula and analyze a fixed interval distribution with large-deviation tools. Their power-tail numerical study explicitly assumes finite second moments, while their quantum-Zeno-limit discussion states a condition for tail exponent greater than two. These are antecedents, not claimed here as new results. The present theorem concerns a different **triangular-array**, fixed-test-count scaling and supplies its non-self-averaging Poisson limit, the exact critical logarithm, explicit moments, and the scale trichotomy. It neither contradicts nor strengthens the earlier fixed-total-time dynamics statements by implication.

## Limitations

The model uses ideal projective observations, an isolated two-level Hamiltonian, independent exact Pareto times, a deterministic number of tests, and no detector imperfections. The protocol's total elapsed time is random and generally grows with the test count: no fixed-total-duration Zeno conclusion is inferred. The point-process law is characterized by its Mellin moments and infinite product, not by an elementary density. The work is a self-contained mathematical treatment, not a demonstration of experimental feasibility or a classification of arbitrary heavy-tailed renewal laws. Priority against all other literature remains unverified independently.

## References

1. A. I. Shushin, *The effect of measurements, randomly distributed in time, on quantum systems. Stochastic quantum Zeno effect*, arXiv:1011.1542v1 (first posted 6 November 2010), https://arxiv.org/abs/1011.1542.
2. S. Gherardini, S. Gupta, F. S. Cataliotti, A. Smerzi, F. Caruso and S. Ruffo, *Stochastic Quantum Zeno by Large Deviation Theory*, arXiv:1509.08122v1 (first posted 27 September 2015); New J. Phys. 18, 013048 (2016), https://arxiv.org/abs/1509.08122, doi:10.1088/1367-2630/18/1/013048.
3. P. Facchi and M. Ligabò, *Large-time limit of the quantum Zeno effect*, arXiv:1702.04284v1 (2017), https://arxiv.org/abs/1702.04284. This reference concerns periodic observations and different time scaling; its abstract was reviewed, but not its entire text.
