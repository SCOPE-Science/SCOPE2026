# Independent mathematical audit

## correctness

PASS

A uniform balanced b-partition has (n/b)_r ordered r-block selections, all fully contained in a k-set with probability (k)_(br)/(n)_(br). Finite binomial inversion gives the exact Markov transition kernel. Conditional covariance between different retained-block indicators is nonpositive, so Var(K_s|K_{s-1}=k)<=b E[K_s|k]. At scaling n p^(b^t)->lambda with fixed p,b, prior mean a_(t-1) ~n^(1-1/b) diverges; uniform product expansion, Chebyshev and t=O(loglog n) give K_(t-1)/a_(t-1)->1. Conditional fixed-order factorial moments at final step ->(lambda/b)^r, hence Poisson(lambda/b). Independently enumerated all 15 balanced pairings of n=6,b=2, verifying all factorial moments from k=4. Exact integer-depth subsequence restriction is essential.

## originality

PASS

Qualified PASS: down-interpretation and equivalence-class lower approximation are explicitly prior (Martins et al and Pawlak). The new part is a uniform random balanced-partition multi-stage Markov kernel and Poisson critical depth, not the modal semantics alone. No same iterated stochastic law appeared in checked Resultary and published primary statements, although older random-partition/rough-set studies remain a plausible overlap risk.

## value

PASS

Provides an exact finite transition law and a sharp rare-survival Poisson window for a naturally defined repeated information-loss operator, relating balanced partitions, factorial moments and modal paths. The growing-depth law is an independently useful structural classification of a finite-state stochastic dynamical system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
