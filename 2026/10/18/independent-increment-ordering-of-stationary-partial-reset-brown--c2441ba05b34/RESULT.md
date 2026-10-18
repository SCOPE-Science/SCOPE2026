# Independent-increment ordering of stationary partial-reset Brownian laws

## Finding

Let \(X^{(c)}\) be standard Brownian motion on the real line, with rate-one Poisson reset times independent of the motion, and with every reset replacing the position \(x\) by \(cx\). Let \(\pi_c\) be its unique invariant probability law for \(0\le c<1\). Then **all invariant distributions are ordered by independent additive noise**: for any \(0\le a<b<1\), one can construct independent variables \(U\sim\pi_a\) and \(Z_{a,b}\) such that \(U+Z_{a,b}\sim\pi_b\).

More explicitly, let \(L_j\), for \(j\ge1\), be independent centered Laplace variables of scale \(b^j/\sqrt2\), let \(B_j\) be independent Bernoulli variables of parameter \(1-(a/b)^{2j}\), independent of all \(L_j\), and define
\[
Z_{a,b}=\sum_{j=1}^{\infty}B_jL_j.
\]
This series converges almost surely and in \(L^2\), and gives the required independent noise. For \(a=0\), the Bernoulli parameters are one. The noise is nondegenerate and infinitely divisible, with explicit Lévy measure
\[
\nu_{a,b}(dx)=\frac{1}{|x|}\sum_{j=1}^{\infty}
\left(\exp(-\sqrt2|x|/b^j)-\exp(-\sqrt2|x|/a^j)\right)\,dx,
\quad x\ne0,
\]
where \(\exp(-\sqrt2|x|/0)=0\) for \(x\ne0\).

**Strict distribution-wide consequences:** For every \(r>0\),
\[
\mathbb P_{\pi_a}(|X|\le r)>\mathbb P_{\pi_b}(|X|\le r).
\]
Consequently \(\mathbb P_{\pi_a}(|X|>r)<\mathbb P_{\pi_b}(|X|>r)\) at *every* threshold, not only at the variance scale. For every convex function \(h:\mathbb R\to\mathbb R\) with the requisite finite expectations, \(\mathbb E_{\pi_a}h\le\mathbb E_{\pi_b}h\); the inequality is strict for strictly convex \(h\). In addition, there exists a centered independent-increment process \((M_c)_{0\le c<1}\), a martingale in parameter \(c\), whose marginal law at parameter \(c\) is \(\pi_c\).

## Assumptions and scope

The diffusion has generator acting on smooth test functions as \(\mathcal G_cf(x)=\frac12f''(x)+f(cx)-f(x)\). The reset times form an independent rate-one Poisson process. There is no drift and the Brownian variance per time is one. The endpoints \(a=0\) and any \(0<b<1\) are included; \(c=1\) is excluded because ordinary Brownian motion on the whole line has no invariant probability distribution. The measures \(\pi_c\) are **unconditioned** stationary distributions. All conclusions compare the laws, not trajectories driven by a common Brownian path.

## Proof

**1. Existence and stationary transform.** The displacement of a standard Brownian motion during an independent unit exponential time has the centered Laplace density \(x\mapsto e^{-\sqrt2|x|}/\sqrt2\), with characteristic function \((1+t^2/2)^{-1}\). Conditioning successively on reset intervals gives the stationary perpetuity
\[
X_c\stackrel d=\sum_{j=0}^{\infty}c^jY_j,
\qquad \mathbb E e^{itY_j}=(1+t^2/2)^{-1},
\]
where the \(Y_j\) are independent. The series converges almost surely and in \(L^2\) since the sum of its variances is \((1-c^2)^{-1}\). The memorylessness of Poisson resets yields invariance; uniqueness also follows from synchronously coupling two starts, whose separation at time \(t\) is multiplied by \(c^{N_t}\to0\) in probability. Therefore
\[
\widehat\pi_c(t)=\prod_{j=0}^{\infty}(1+c^{2j}t^2/2)^{-1}.
\tag{1}
\]
For \(c=0\), only the \(j=0\) nontrivial factor remains.

**2. Constructive factorization.** Fix \(0\le a<b<1\), put \(q_j=(a/b)^{2j}\) for \(j\ge1\), and let the independent variables \(B_j,L_j\) have the laws described above. Direct calculation gives, for all real \(t\),
\[
\mathbb E e^{itB_jL_j}
=q_j+\frac{1-q_j}{1+b^{2j}t^2/2}
=\frac{1+a^{2j}t^2/2}{1+b^{2j}t^2/2}.
\tag{2}
\]
Each term is centered with variance \(b^{2j}-a^{2j}\). Hence \(\sum_{j\ge1}B_jL_j\) converges almost surely (independent centered square-summable variances) and in \(L^2\). Multiplying (2) over \(j\ge1\) and using (1) yields
\[
\widehat\pi_a(t)\,\mathbb E e^{itZ_{a,b}}=\widehat\pi_b(t).
\]
This proves the independent additive-noise factorization.

**3. Infinite divisibility and explicit Lévy kernel.** For every \(s>0\), the elementary Fourier integral is
\[
\int_{\mathbb R\setminus\{0\}}(\cos(tx)-1)\frac{e^{-|x|/s}}{|x|}\,dx
=-\log(1+s^2t^2).
\tag{3}
\]
Consequently the stationary law \(\pi_c\) has symmetric Lévy density
\[
\frac1{|x|}\sum_{j=0}^{\infty}e^{-\sqrt2|x|/c^j},
\quad x\ne0,
\]
where at \(c=0\) only the \(j=0\) term remains. Subtracting the Lévy exponents for \(b\) and \(a\) gives the displayed \(\nu_{a,b}\). Every summand is strictly positive for \(x\ne0\). It is a valid Lévy measure: since \(1\wedge x^2\le x^2\), its small/large-jump integrability is controlled by
\[
\int_{\mathbb R}(1\wedge x^2)\nu_{a,b}(dx)
\le \sum_{j=1}^{\infty}(b^{2j}-a^{2j})<\infty.
\]
Indeed the second-moment integral of the symmetric density difference is precisely the corresponding variance difference. Thus \(Z_{a,b}\) is an infinitely divisible centered symmetric variable with exactly the stated positive Lévy measure and no Gaussian part.

**4. Parameter-indexed martingale.** The characteristic functions \(\widehat\pi_b/\widehat\pi_a\) define probability distributions for every \(a<b\), and the ratios multiply consistently for successive parameters. Assign independent increments with these distributions on each finite ordered parameter set and start at \(M_0\sim\pi_0\). Consistent finite-dimensional laws give a process by the extension theorem. Each increment has mean zero, and its variance is \((1-b^2)^{-1}-(1-a^2)^{-1}\). Thus \(M_c\) is an integrable independent-increment martingale and \(M_c\sim\pi_c\) for every \(0\le c<1\). No claim about equality of sample paths with the original resetting diffusion is made.

**5. Strict peakedness and convex order.** A centered Laplace density is symmetric and log-concave. Finite convolutions of symmetric log-concave laws retain these properties, as does a weak limit; hence \(\pi_a\) has a symmetric unimodal (indeed log-concave) density. For each \(r>0\), the map \(z\mapsto\mathbb P(|U+z|\le r)\) is maximal at \(z=0\). Its value tends to zero as \(|z|\to\infty\), whereas its value at zero is positive. The independent variable \(Z_{a,b}\) has unbounded support: already \(B_1L_1\) is a nonzero-weight Laplace component with unbounded support, independent of the remaining summands. Averaging over \(Z_{a,b}\) therefore gives a *strict* decrease of every symmetric interval probability. Finally, conditional Jensen applied to \(U+Z_{a,b}\), using \(\mathbb E Z_{a,b}=0\), proves the convex-order assertion; for strictly convex finite-expectation tests the inequality is strict since the noise is nondegenerate.

## Verification

The companion `checker.py` uses exact rational arithmetic to verify all finite Bernoulli/Laplace characteristic-function factorizations and the additive variance identities for multiple rational parameter pairs and truncation lengths. It also checks the Lévy logarithm integral numerically against its closed analytic form and the strict positivity of representative Lévy density differences. Run from the directory containing this document using `python3 checker.py`. Finite numerical checks validate identities at sampled inputs; the universal statements and parameter-indexed construction follow from the proof above, not from enumeration.

## Relationship to prior work

Tal-Friedman, Roichman and Reuveni (2022) established the Laplace-series representation of the invariant distribution and computed its variance and kurtosis. Di Bello, Chechkin, Hartmann, Palmowski and Metzler (2023) derived explicit time-dependent and stationary densities for partially reset Brownian and stable processes. Grzywny, Palmowski, Szczypkowski and Trojan (first preprint 2024) studied general stationary states of stable processes with partial resetting. Kolb and Wübker (2026) established the invariant-law representation, spectral convergence and conditioning-to-survive results for the Brownian model. None of the specifically inspected portions of these sources presents the parameter-indexed **independent-increment convolution factorization**, its positive *increment* Lévy kernel, and the strict every-threshold symmetric-tail comparison as one result. Their established stationary distributions, moment identities and density formulas are used as premises, not claimed as discoveries here. The underlying general theory of infinitely divisible laws and convolution orders is classical; an unlocated stronger theorem may subsume this application.

## Limitations

The claim applies to symmetric driftless Brownian motion with a deterministic contraction factor, Poisson reset rate one, and fixed Brownian variance normalization. It does not assert the same order for biased diffusions, nonsymmetric stable drivers, state-dependent resets, finite-time distributions, or the conditioned-to-stay-positive process. The existence of an additive martingale concerns an auxiliary process indexed by the reset multiplier, not an independent-increment representation of the physical dynamics in time. Unexamined general convolution-order results and incompletely accessible portions of broader stable-resetting literature remain priority risks. Independent originality and proof auditing have not been performed.

## References

1. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with partial resetting*, Physical Review E **106** (2022), 054116. DOI: 10.1103/PhysRevE.106.054116. First arXiv version: 2205.03363 (May 6, 2022).
2. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, New Journal of Physics **25** (2023), 082002. DOI: 10.1088/1367-2630/aced1d.
3. T. Grzywny, K. Szczypkowski, Z. Palmowski and B. Trojan, *Stationary states for stable processes with partial resetting*, Annals of Applied Probability **36** (2026), 1110–1177; first arXiv version: 2412.15626 (December 20, 2024).
4. M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, Bulletin of the London Mathematical Society **58** (2026), e70314. DOI: 10.1112/blms.70314. First verified public date: March 5, 2026.
5. C. Di Bello et al., *Partial versus total resetting for Lévy flights in d dimensions: Similarities and discrepancies*, Chaos **35** (2025), 043129. DOI: 10.1063/5.0255695.
