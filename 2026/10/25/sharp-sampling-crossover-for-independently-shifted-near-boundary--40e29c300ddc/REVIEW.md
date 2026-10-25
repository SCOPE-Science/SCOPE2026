# Scientific review

## Correctness — PASS

The single Poisson-kernel theorem is reconstructed with exact quantifiers: arbitrary integer grid counts and independent shift replications, any radii satisfying \(r_k^{N_k}\to1\). Fourier orthogonality gives both the exact aliasing identity and variance. Rare-core avoidance plus a tail expectation estimate proves zero-in-probability when \(m_k(1-r_k^{N_k})\to0\); the critical Laplace transforms converge to the finite-mean Poisson integral by dominated convergence; an explicit maximum-summand estimate establishes Lindeberg's condition above threshold. A compact subsequence argument proves that the work threshold is necessary, not merely sufficient. The total-work approximation uses logarithmic equivalences valid under the specified near-boundary condition. The standalone checker passed 475 numeric and deterministic assertions, without being used as a substitute for the infinite proofs.

## Originality — PASS, with priority qualifications

Classical periodic Fourier aliasing and the Poisson kernel are established ingredients. The closest motivating randomized quadrature paper, Goda–Kazashi–Suzuki (arXiv:2212.11476v1), analyzes integration of fixed Gaussian-Sobolev integrands on the line and proves worst-case RMSE bounds under that different object and scope; those bounds do not imply a three-phase weak-limit classification for a family of Poisson kernels narrowing with mesh spacing. Bao–Hua–Lai–Zhang (arXiv:2305.05855) and af Klinteberg (arXiv:2304.11865) analyze deterministic near-singular correction schemes, without this independent-shift triangular-array limiting law. Trefethen–Weideman's classical trapezoidal aliasing analysis motivates rather than subsumes the near-boundary statistical threshold. Related prior work on Poisson shot-noise limits establishes abstract techniques, not the stated sharp parameter, exact variance, and full grid-quadrature trichotomy as one theorem.

Targeted mathematical-record and open-literature searches, plus comparison against other preceding mathematical statements, disclosed no covering published statement. A preceding claim gives an unshifted Cauchy-mixture trapezoidal formula and parity/scale conditions, not independent random phase averaging or the critical Poisson limit. The finite search does not establish global novelty: alternative formulations or inaccessible numerical-analysis literature remain possible, and publication priority has not been independently established. Some broad classical-source full texts were only partially accessible, so the assessment does not call them exhaustively noncovering.

## Value — PASS

A standard remedy for phase aliasing in periodic trapezoidal integration is independent random shifting. For a naturally near-singular positive analytic test kernel, this result gives a necessary-and-sufficient quantitative work criterion, an exact finite-sample variance, and a critical distribution describing the failure of concentration. The especially relevant zero-in-probability but exactly unbiased regime warns against interpreting unbiasedness or fixed-integrand RMSE theory as a guarantee of typical accuracy under boundary-layer refinement. The exact Poisson/Gaussian transition provides a reproducible stress benchmark for quadrature software and a design rule for the sampling budget. This is more than a substitution in the classical alias formula because the adaptive sample-budget regime and nondegenerate critical shot-noise distribution need separate probabilistic analysis.

## Scope, checks, and risks

The result is one theorem for the precisely defined circular Poisson family, not a universal optimal scheme. Classical aliasing is expressly not presented as novel. Exhaustive priority cannot be proved by negative search results; the full Trefethen–Weideman PDF and portions of the broader applied point-process literature could not be fully read, a residual originality risk. No peer or independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
