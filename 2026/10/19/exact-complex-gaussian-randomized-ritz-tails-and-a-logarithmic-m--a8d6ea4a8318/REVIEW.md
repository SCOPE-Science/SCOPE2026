# Scientific assessment

## Correctness — PASS

For the specified three-dimensional diagonal Hermitian matrix and two-dimensional trial space, the compressed pencil is exactly lower triangular after multiplying by the almost-surely invertible square Gaussian sketch. Its eigenbranch and corresponding normalized eigenvector admit closed rational expressions. Unitary invariance identifies the Gaussian-nullspace ratios with ratios of three independent circular Gaussians. An orthogonal Gaussian linear combination gives independent exponential numerator and denominator; direct integration establishes the exact CDF and mean. The explicit radial tail yields divergence of the second absolute moment, and a small-angle Taylor expansion gives the coefficient of the logarithmic mean squared-angle penalty. The standalone computation checks representative identities but is not relied on for the universal claim.

## Originality — PASS, with bibliographic risk

Shao's *Stabilizing the Rayleigh–Ritz procedure by randomization* (arXiv:2604.01037v1), including its algorithm, main high-probability eigenpair results, and numerical study, was compared directly: this analysis uses the proposed square complex-Gaussian test pencil but supplies an exact complex-projective distribution and expectation/tail classification, not merely the same high-probability conclusion. Nakatsukasa–Tropp's full sketched Rayleigh–Ritz treatment analyzes embedding/oversampled sketches and spectral approximation; Haas–Nakatsukasa (arXiv:2506.01207) derives deterministic approximate-eigenvalue bounds. Neither inspected material asserts the specific exact noncentralized angle distribution, its logarithmic expectation, and the unrefined eigenvalue's infinite second moment for this trial-space model. Published mathematical records and related result summaries were queried for Cauchy, exponential-ratio, random-test-space, tail, and implication-equivalent formulations; no dominating prior claim was identified. Classical Gaussian ratio laws are acknowledged; an older equivalent specialized result remains possible, and failed database retrieval does not certify uniqueness.

## Mathematical value — PASS

The explicit model exposes a concrete limitation of translating an important randomized Rayleigh–Ritz high-probability guarantee into a mean-square guarantee. The model has an elementary positive-semidefinite diagonal Hermitian matrix with a simple extremal eigenvalue, and the same trial space yields a deterministic squared-angle error of order \(\theta^2\) but a randomized expected error of order \(\theta^2\log(1/\theta)\). The exact finite-sample CDF quantifies rare large-angle outcomes, and the unrefined eigenvalue has no finite second moment even as it converges in probability. This distinguishes eigenvector and eigenvalue reliability metrics and motivates oversampling, robust refinement and tail-aware numerical reporting, without asserting results for those modifications.

## Closest prior literature and limitations

N. Shao, arXiv:2604.01037v1, Sections 1, 4 and 5, https://arxiv.org/html/2604.01037v1; Y. Nakatsukasa and J. A. Tropp, *Fast Randomized Algorithms for Linear Systems and Eigenvalue Problems*, §§1.3 and 6, https://tropp.caltech.edu/drafts/NT21-Fast-Accurate-draft.pdf; I.-B. Haas and Y. Nakatsukasa, arXiv:2506.01207, https://arxiv.org/pdf/2506.01207. The result treats one fixed square complex-Gaussian sketch pencil; alternate trial spaces, oversampling, postprocessed Rayleigh quotients, and real Gaussian sketches can have different distributions. Classical complex-Gaussian ratio probability is not claimed new.

Self-review: passed. Independent audit: not yet performed.
