# Self-review

## Correctness — PASS
The proof establishes the exact stationary common-scale Gaussian representation, the covariance decomposition, exact Gaussian order moments for two, three and four particles, and a uniform \(\operatorname{Cov}(A_N,B_N)\le1/N\) using Gaussian interpolation and opposite-monotone association. The elementary strict inequalities complete the classification for every integer \(N\ge2\). Gaussian Poincaré and normal extreme asymptotics give the logarithmic covariance and limiting correlation. `verify.py` independently reconstructs the finite Gaussian integrals; it is not a replacement for the infinite-population proof.

## Originality — PASS, qualified
The directly relevant prior works arXiv:2211.00563, arXiv:2307.15351 and arXiv:2509.06658 establish the stationary joint law, its general conditional-independence structure, marginal extreme-value statistics and nearest-neighbor gaps. None of the materially inspected passages states or settles the simultaneous leftmost/rightmost covariance sign boundary. Related public studies of finite-support order-statistic correlations and Gaussian bridge maxima do not cover this stationary common-reset model. Publication priority is not independently certified, and existing broad joint-density formulas contain the raw information from which additional calculations can in principle recover this theorem.

## Mathematical value — PASS
An exact four-particle sign change and the strong asymptotic anticorrelation of opposite edges are motivated finite-size and large-system effects in a published solvable Brownian gas. The result clarifies how a common random observation age competes with within-snapshot Gaussian order correlations, despite zero pairwise particle covariance. The theorem applies only to the stated reset protocol, not arbitrary interactions or renewal distributions.

## Closest literature and limitations
Biroli et al., *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting* (2022/2023), arXiv:2211.00563; Biroli et al., *Exact extreme, order and sum statistics in a class of strongly correlated system* (2023), arXiv:2307.15351; de Mauro et al., *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols* (2025), arXiv:2509.06658. Independent literature-priority and external mathematical validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
