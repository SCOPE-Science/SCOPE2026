# A three-regime limit theorem for generalized matching counts

## Finding

Consider the two-stage matching model in which each of the \(n\) items is correctly assigned independently with probability \(\theta_n\), and the remaining items are uniformly permuted. Let \(L_n\sim\operatorname{Bin}(n,\theta_n)\), let \(R_n=n-L_n\), and let \(K_r\) count fixed points of a uniform permutation of size \(r\), with \(K_0=0\). The total number of correct matches is

\[
K_n^*=L_n+K_{R_n}.
\]

The following parameter-boundary classification holds, with convergence in total variation in the first two cases:

1. If \(n\theta_n\to\lambda\in[0,\infty)\), then \(K_n^*\to\operatorname{Pois}(1+\lambda)\).
2. If \(n(1-\theta_n)\to\mu\in[0,\infty)\), then \(n-K_n^*\to W_\mu\), where \(R\sim\operatorname{Pois}(\mu)\) and, conditional on \(R=r\), \(W_\mu=r-K_r\). For \(\mu>0\), its exact mass function is
   \[
   \Pr(W_\mu=d)=e^{-\mu}\frac{D_d}{d!}\sum_{j=0}^{\infty}\frac{\mu^{d+j}}{(d+j)!j!},\qquad d=0,1,2,\ldots,
   \]
   where \(D_d\) is the number of derangements of \(d\) labels; for \(\mu=0\), \(W_0=0\) almost surely. In particular, \(\Pr(W_\mu=1)=0\).
3. If both \(n\theta_n\to\infty\) and \(n(1-\theta_n)\to\infty\), then
   \[
   \frac{K_n^*-(n\theta_n+1-\theta_n^n)}{\sqrt{n\theta_n(1-\theta_n)}}\ \xrightarrow{\ d\ }\ N(0,1).
   \]

These regimes classify every parameter sequence after passage to a subsequence: either one endpoint intensity has a finite limit, or both endpoint intensities diverge.

## Assumptions and scope

For each \(n\), the Bernoulli decisions determining which items are known correct are independent with common probability \(\theta_n\in[0,1]\). Conditional on the number \(R_n\) of unresolved items, their allocation is a uniform random permutation independent of the Bernoulli decisions beyond that conditioning. A uniform permutation of size zero has zero fixed points. The result is asymptotic as \(n\to\infty\), with the stated limits assumed; it does not assert a rate of convergence or a finite-\(n\) total-variation bound.

## Proof

Write \(q_n=1-\theta_n\). The exact representation \(K_n^*=L_n+K_{R_n}\) is the two-stage model, and \(R_n\sim\operatorname{Bin}(n,q_n)\). For a uniform permutation of size \(r\), the number of fixed points has probability
\[
\Pr(K_r=k)=\frac{D_{r-k}}{k!(r-k)!},\qquad 0\le k\le r,
\]
where \(D_s=s!\sum_{i=0}^{s}(-1)^i/i!\), with \(D_0=1\) and \(D_1=0\). For every fixed \(k\), this probability tends to \(e^{-1}/k!\) as \(r\to\infty\). Since the limiting Poisson probabilities sum to one, the discrete Scheffé lemma gives total-variation convergence \(K_r\to\operatorname{Pois}(1)\).

**Case 1.** If \(n\theta_n\to\lambda<\infty\), then \(L_n\to\operatorname{Pois}(\lambda)\) in total variation by the binomial-to-Poisson limit, and \(R_n=n-L_n\to\infty\) in probability. Conditional on \(L_n\), the law of \(K_{R_n}\) therefore approaches \(\operatorname{Pois}(1)\) in total variation in expectation. Thus the pair \((L_n,K_{R_n})\) approaches a pair of independent variables with laws \(\operatorname{Pois}(\lambda)\) and \(\operatorname{Pois}(1)\). Addition is a measurable map and cannot increase total variation, so their sum converges in total variation to \(\operatorname{Pois}(1+\lambda)\).

**Case 2.** If \(nq_n\to\mu<\infty\), then \(R_n\to R\sim\operatorname{Pois}(\mu)\) in total variation. Since \(n-K_n^*=R_n-K_{R_n}\), applying the same conditional random-permutation kernel to the converging integer-valued variable preserves total-variation convergence. For a permutation of size \(r\), exactly \(d\) points move precisely when one chooses the \(d\) moved labels and deranges them; hence
\[
\Pr(r-K_r=d)=\binom rd\frac{D_d}{r!}=\frac{D_d}{d!(r-d)!}.
\]
Mixing over \(R\sim\operatorname{Pois}(\mu)\), and writing \(r=d+j\), yields the displayed mass function. Because \(D_1=0\), exactly one mismatch is impossible. Also \(\mathbb E W_\mu=\mu-1+e^{-\mu}\), since \(\mathbb E K_r=1\) for every \(r\ge1\).

**Case 3.** Put \(\sigma_n^2=n\theta_nq_n\). If both endpoint intensities diverge, then \(\sigma_n^2\to\infty\), and the binomial central limit theorem gives \((L_n-n\theta_n)/\sigma_n\to N(0,1)\). Further, \(\mathbb E K_{R_n}=\Pr(R_n\ge1)=1-\theta_n^n\le1\), so \(K_{R_n}\) is tight by Markov's inequality. Consequently \((K_{R_n}-(1-\theta_n^n))/\sigma_n\to0\) in probability. Substituting the exact mean \(\mathbb E K_n^*=n\theta_n+1-\theta_n^n\) and applying Slutsky's theorem proves the normal limit.

## Verification

The accompanying `artifacts/verification.py` checks the exact finite-size convolution against the model definition for all \(n\le12\) and five rational parameter values, checks normalization and the impossible \(n-1\)-match event, verifies the exact mean identity, and checks the Poissonized moved-point mass formula against its defining mixture for finite truncations. These finite checks are consistency tests; the limiting claims follow from the analytical arguments above.

## Relationship to prior work

O'Neill introduced the same two-stage generalized matching model and derived its convolution formula, moment generating function, first four central moments, stochastic monotonicity, and a central limit theorem for fixed \(0<\theta<1\). The present result concerns triangular arrays \(\theta=\theta_n\), including both endpoint windows \(n\theta_n=O(1)\) and \(n(1-\theta_n)=O(1)\), and gives the explicit limiting mismatch law near perfect matching. The near-perfect endpoint is not a normal limit: its limiting mismatch count assigns zero probability to one, a constraint inherited from permutation structure. This statement is not implied by the fixed-parameter central limit theorem. The prior literature search was focused on the stated endpoint and triangular-array limits; it was not exhaustive, so no absolute priority claim is made.

## Limitations

No explicit convergence rate is established. The endpoint limits assume convergence of the corresponding intensity; oscillating intensities are handled only by subsequences. The normal regime assumes both endpoint intensities diverge. The exact mismatch law is a Poisson mixture of classical moved-point counts; related work on Poissonized permutation statistics may contain equivalent formulations not found in the inspected sources.

## References

Ben O'Neill, “A Generalised Matching Distribution for the Problem of Coincidences,” arXiv:2112.12442 (first public version 2021-12-23); *Methodology and Computing in Applied Probability* 25 (2023), article 93, DOI: 10.1007/s11009-023-10067-6. Sections 3–4 and Theorems 7–9 establish the model, convolution, moments, and fixed-parameter central limit theorem.
