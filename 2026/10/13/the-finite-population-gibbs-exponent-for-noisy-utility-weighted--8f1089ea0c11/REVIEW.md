# Scientific review: The finite-population Gibbs exponent for noisy utility-weighted opinion averaging

## Correctness — PASS

The exact utility-asymmetric pair update yields a mean increment proportional to the squared selected opinion difference. Orthogonal centering gives the neutral contraction factor \(a=1-4\mu(1-\mu)/(N-1)\) and its unique stationary quadratic moment. For a fixed finite population, the fourth-moment contraction and stopped-process estimates keep all pair distances below the confidence radius with probability tending to one on each accelerated finite horizon. Martingale summation by parts replaces the fast quadratic observable by its exact neutral equilibrium mean. The resulting weak limit has drift \( (N-1)\ell'/[N(1-\mu)]\) and diffusion coefficient \(1/N\) in its generator. The one-dimensional invariant density follows by solving the stationary zero-flux equation. The standalone exact-rational checker validates the matrix and moment identities for 45 \((N,\mu)\) combinations; no infinite proof is inferred from these tests.

## Originality — PASS, subject to explicit remaining risks

The 2026 motivating paper explicitly drops finite-population anticorrelation in Supplementary Appendix A and uses an approximate representative-agent variance closure in Appendix F, obtaining the leading exponent \(N/(1-\mu)\). Its full accessible text does not establish the exact fixed-population exponent \((N-1)/(1-\mu)\) together with convergence of the scaled microscopic mean. Xing and Johansson study gossip with stubborn agents and concentration over graph randomness, not this utility-weighted diffusion limit. General nonlinear gossip and stochastic-approximation papers do not, in the material inspected, give the claimed finite-population exponent. The result may be encompassed by a more general stochastic-homogenization theorem, and only abstracts were obtained for two peripheral comparison papers. Absence of an indexed match is not proof of worldwide priority.

## Mathematical value — PASS

The precise \(N-1\) correction controls equilibrium selection in small finite groups, not merely a cosmetic remainder in a descriptive approximation. It supplies an asymptotically exact finite-population Gibbs exponent for an explicitly defined new opinion model and separates the justified finite-time diffusion conclusion from the unproved stationary-law interchange. At \(N=2\), \(\mu=1/2\), and \(U(x)=(1+x^2)^{-1}\), the corrected power is \(2\), versus \(4\) in the leading large-population closure, illustrating a substantive distinction. The proof needs exact fast-mode covariance and nontrivial controlled stochastic averaging.

## Closest prior literature and limits

- Siebenmorgen and Restrepo, arXiv:2605.21844v1, model Eq. (1), main Eqs. (5)--(15), Supplementary Appendices A--F: same microscopic model, different approximate finite-population closure.
- Xing and Johansson, arXiv:2301.05352v4, Sections 2 and 4: random-graph stubborn-agent concentration, not the target weak-noise mean law.
- Acemoğlu, Como, Fagnani and Ozdaglar, arXiv:1009.2653; Mathkar and Borkar, DOI:10.1137/140992588: only abstract-level access for this comparison. Their different models reduce direct-overlap concern but the full texts were not excluded.

The accepted theorem does not prove stationary distribution convergence for the original finite-noise model, nor a uniform-in-time stochastic approximation. Independent external scientific review is unperformed.

Self-review: passed. Independent audit: not yet performed.
