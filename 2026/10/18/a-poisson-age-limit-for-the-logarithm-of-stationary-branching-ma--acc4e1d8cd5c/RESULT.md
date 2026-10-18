# A Poisson-age limit for the logarithm of stationary branching mass under rare immigration

## Finding

For the stationary continuous-state branching process with immigration described below, as \(\alpha\downarrow0\) the logarithmic population process
\[
L_t^{(\alpha)}=-\alpha\log Z^{(\alpha)}_{t/\alpha},\qquad t\in\mathbb R,
\]
converges in **finite-dimensional distributions** to the stationary age process of a homogeneous rate-one Poisson process. Specifically, if \(\mathcal P\) is a rate-one Poisson point process on the entire real line and
\[
A_t=t-\sup\{s\le t:s\in\mathcal P\},
\]
then, for every positive integer \(m\) and deterministic \(t_1,\ldots,t_m\in\mathbb R\),
\[
(L_{t_1}^{(\alpha)},\ldots,L_{t_m}^{(\alpha)})\Longrightarrow (A_{t_1},\ldots,A_{t_m}).
\]
This can be quantified by constructing the processes on a common probability space so that, for every \(\eta>0\),
\[
\Pr\!\left(\max_{1\le j\le m}|L_{t_j}^{(\alpha)}-A_{t_j}|>\eta\right)
\le m\left[\alpha+\left(1+\frac{e^{1+\eta}}{\alpha}\right)e^{-\eta/\alpha}\right]. \tag{1}
\]
The bound holds for all \(0<\alpha<1\) and all deterministic observation times (it need not be smaller than one to be valid).

The limiting process has stationary distribution \(\operatorname{Exp}(1)\), rises with deterministic unit slope between Poisson epochs, and jumps to zero at each epoch. Its transition kernel, for \(s>0\), is
\[
\Pr(A_{t+s}\in dy\mid A_t=a)=e^{-s}\delta_{a+s}(dy)
+\mathbf1_{\{0<y<s\}}e^{-y}\,dy.\tag{2}
\]
For continuously differentiable test functions its generator is \(Gf(a)=f'(a)+f(0)-f(a)\).

## Assumptions and scope

Fix \(0<\alpha<1\). Let \(Z^{(\alpha)}\) be the **two-sided stationary** subcritical continuous-state branching process with immigration established by Harris, Johnston and Pardo (2026), with rate
\[
\lambda_\alpha=\frac{\alpha}{1-\alpha}
\]
of immigration times, independent \(\operatorname{Gamma}(1-\alpha,1)\) immigration masses, and an independent subcritical continuous-state branching process for each immigrant family. For an isolated family started from mass \(x\), its one-time Laplace transform is
\[
\mathbb E_x e^{-\theta Y_r^{(\alpha)}}=e^{-x u_r^{(\alpha)}(\theta)},\qquad
u_r^{(\alpha)}(\theta)=\left[1+e^{-r}\big((1+\theta)^{1-\alpha}-1\big)\right]^{1/(1-\alpha)}-1.
\]
In particular \(\mathbb E_xY_r^{(\alpha)}=xe^{-r}\). The stationary law is \(Z_t^{(\alpha)}\sim\operatorname{Gamma}(\alpha,1)\), so \(Z_t^{(\alpha)}>0\) almost surely at every fixed time. No assertion concerns a simultaneous limit in the original Galton–Watson explosion-scale parameter.

## Proof

**Immigrant-age representation.** Denote by \(S_\alpha(v)\) the most recent immigration time at or before real time \(v\), and define the *rescaled immigration age*
\[
D_t^{(\alpha)}=\alpha\big(t/\alpha-S_\alpha(t/\alpha)\big).
\]
The points \(\alpha S\) of the rescaled immigration process form a homogeneous Poisson process of rate \(\lambda_\alpha/\alpha=1/(1-\alpha)\). Consequently \(D_t^{(\alpha)}\) has \(\operatorname{Exp}(1/(1-\alpha))\) law and its finite-dimensional distributions converge to those of \(A_t\).

**Conditional law at the last arrival.** Fix \(t\) and condition on \(D_t^{(\alpha)}=a\ge0\), so the last immigration occurred \(r=a/\alpha\) physical time units ago. The stationary population just before that event has \(\operatorname{Gamma}(\alpha,1)\) law. This uses the Poisson-arrivals-see-time-averages (Palm) identity: immigration times are exogenous, so conditioning on an arrival does not bias the pre-arrival state. Conditioning that no further immigration occurs during the following interval of length \(r\) does not alter that state because the driving Poisson process has independent future increments. Adding the independent \(\operatorname{Gamma}(1-\alpha,1)\) immigrant mass gives a total \(\operatorname{Gamma}(1,1)\) population at the last immigration epoch. This entire population evolves for time \(r\) as a single branching process, without further immigration. Therefore its exact conditional Laplace transform is
\[
\mathbb E\left[e^{-\theta Z^{(\alpha)}_{t/\alpha}}\mid D_t^{(\alpha)}=a\right]
=\frac1{1+u_{a/\alpha}^{(\alpha)}(\theta)}
=\left[1+e^{-a/\alpha}\big((1+\theta)^{1-\alpha}-1\big)\right]^{-1/(1-\alpha)}.\tag{3}
\]
In particular the conditional mean is
\[
\mathbb E\left[Z^{(\alpha)}_{t/\alpha}\mid D_t^{(\alpha)}=a\right]=e^{-a/\alpha}.\tag{4}
\]
The process also contains the descendants \(C_r\) of the most recent immigrant alone. The immigrant's initial mass has \(\operatorname{Gamma}(1-\alpha,1)\) law, and \(0<C_r\le Z^{(\alpha)}_{t/\alpha}\) almost surely. Its exact Laplace transform, conditional on age \(a\), is
\[
\mathbb E e^{-\theta C_r}
=\big[1+u_r^{(\alpha)}(\theta)\big]^{-(1-\alpha)}
=\frac1{1+e^{-r}\big((1+\theta)^{1-\alpha}-1\big)}.\tag{5}
\]

**Exponential logarithmic tracking.** Fix \(\eta>0\). By (4) and Markov's inequality,
\[
\Pr(L_t^{(\alpha)}<a-\eta\mid D_t^{(\alpha)}=a)
=\Pr\left(Z^{(\alpha)}_{t/\alpha}>e^{-(a-\eta)/\alpha}\mid D_t^{(\alpha)}=a\right)
\le e^{-\eta/\alpha}.\tag{6}
\]
For the other side take \(\theta=e^{(a+\eta)/\alpha}\). If \(L_t^{(\alpha)}>a+\eta\), then \(C_r<\theta^{-1}\), hence \(e^{-\theta C_r}>e^{-1}\). Formula (5) and Markov's inequality imply
\[
\Pr(L_t^{(\alpha)}>a+\eta\mid D_t^{(\alpha)}=a)
\le \frac{e}{1+e^{-a/\alpha}((1+\theta)^{1-\alpha}-1)}.
\]
Since \((1+\theta)^{1-\alpha}\ge\theta^{1-\alpha}\) and \(1-e^{-a/\alpha}\ge0\), the denominator is at least
\[
e^{-a/\alpha}\theta^{1-\alpha}=e^{\eta/\alpha-a-\eta}.
\]
Thus the probability is at most \(e^{1+a+\eta-\eta/\alpha}\). Averaging this over \(D_t^{(\alpha)}\sim\operatorname{Exp}(1/(1-\alpha))\) gives
\[
\mathbb E e^{D_t^{(\alpha)}}=\frac1\alpha,
\]
and therefore
\[
\Pr\left(|L_t^{(\alpha)}-D_t^{(\alpha)}|>\eta\right)
\le\left(1+\frac{e^{1+\eta}}\alpha\right)e^{-\eta/\alpha}.\tag{7}
\]

**Comparison with the unit-rate age process.** Couple the rescaled rate-\(1/(1-\alpha)\) immigration point process as the union of an independent rate-one Poisson point process \(\mathcal P\) and an independent rate-\(\alpha/(1-\alpha)\) Poisson point process. The most recent point comes from the extra process with probability exactly \(\alpha\), by competing backward exponential waiting times. Hence \(\Pr(D_t^{(\alpha)}\ne A_t)=\alpha\). Combining this fact with (7) and the union bound across \(m\) observation times yields (1). Since its right-hand side tends to zero as \(\alpha\downarrow0\), finite-dimensional convergence follows. Formula (2) follows by splitting the event of no rate-one Poisson arrival in an interval of length \(s\) from the density of its last arrival; differentiation gives the generator.

## Verification

The supporting `verify.py` independently evaluates (3), (5), and the small-\(\theta\) derivative yielding (4); it integrates (3) over the exponential age distribution and compares the result against the known stationary \(\operatorname{Gamma}(\alpha,1)\) Laplace transform. It also checks the exact relation between the two Poisson rates and the thinning mismatch probability. All 308 deterministic assertions passed using the supplied script in the present package. These finite computations check algebraic/numerical consistency only; the proof of (1) for all parameters and observation times is the analytic argument above.

## Relationship to prior work

Harris, Johnston and Pardo (2026, arXiv:2610.01810v1) derive the fixed-\(\alpha\) stationary branching–immigration process, its clan decomposition, branching Laplace exponent, and \(\operatorname{Gamma}(\alpha,1)\) stationary law. Those facts are **used as previously known**, not claimed as new. The finding here is the singular **\(\alpha\downarrow0\)** multi-time limit after accelerating time by \(1/\alpha\), together with the explicit logarithmic coupling estimate (1), age kernel (2), and conditional identity (3). A one-time small-shape Gamma limit alone cannot specify temporal dependence.

Foucart and Yuan (2024, arXiv:2311.04045v2) consider weak limits of continuous-state branching with **large immigration**, including immigration measures without a logarithmic moment and extremal shot-noise limits. Their displayed regime does not imply the present finite-Gamma-jump, vanishing-intensity, jointly changing mechanism and stationary long-time scaling. Mitov and Yanev (2025, arXiv:2501.03270v1) study critical discrete-particle branching with nonhomogeneous vanishing immigration intensity and infinite-mean immigrants; their model, normalization, and limits differ. These comparisons do not exclude an unlocated general rare-immigration theorem that could subsume this result.

## Limitations

This is a finite-dimensional convergence theorem, **not** a claim of Skorokhod path-space convergence or convergence of all random-time observables. The model is the stationary continuous-state branching–immigration limit after the original near-explosion scaling has been taken at fixed \(\alpha\); no joint limit in those two parameters is asserted. The quantitative bound concerns fixed deterministic time evaluations. Novelty is assessed against accessible sources and awaits independent priority checking.

## References

1. S. C. Harris, S. G. G. Johnston and J.-C. Pardo (2026), *Behaviour near explosion in continuous-time Galton–Watson trees*, arXiv:2610.01810v1, initially public 2026-10-01; Sections 2.2.2 and 5.2–5.5. https://arxiv.org/html/2610.01810v1
2. C. Foucart and X. Yuan (2024), *Weak convergence of continuous-state branching processes with large immigration*, arXiv:2311.04045v2. https://arxiv.org/html/2311.04045v2
3. K. V. Mitov and N. M. Yanev (2025), *Markov branching process with infinite variance and non-homogeneous immigration with infinite mean*, arXiv:2501.03270v1. https://arxiv.org/html/2501.03270v1
