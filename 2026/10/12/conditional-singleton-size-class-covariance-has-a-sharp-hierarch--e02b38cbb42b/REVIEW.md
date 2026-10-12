# Review of the conditional block-size covariance transition

## Correctness — PASS

The exact three marked-block moment counts follow from removing disjoint distinguished blocks. A conditional zero-truncated Poisson representation translates the remaining problem into a bivariate saddlepoint calculation. The strictly aperiodic analytic coefficient expansion gives the needed second cumulant per block, not merely convergence in distribution. The sign numerator is a strictly convex normalized function with one positive root for each class size at least three; derivative arguments give the ordered thresholds. `verify.py` independently passed 270 exact and finite numerical checks. The result does not assert behavior at a critical density.

## Originality — PASS, with residual historical uncertainty

Timashev (2003) studies marginal counts in exactly the same fixed-block-count partition model, while Arratia and DeSalvo (2016) give a broader conditional assembly representation. These tools are acknowledged. Their inspected results do not state the mixed class-size covariance sign classification or the ordered thresholds. Barbour and Gnedin (2008) concern infinite-box occupancy, a distinct ensemble. A generic multivariate saddle expansion may implicitly encode the covariance; historical priority is not exhaustively settled.

## Mathematical value — PASS

The result distinguishes the persistent repulsion of singleton and doubleton block counts from a positive-correlation phase for singleton and larger fixed-size classes when many blocks are forced. Every fixed class has a natural unique transition, and the thresholds form a rigorously ordered reciprocal hierarchy. These facts describe a dependence phenomenon useful for interpreting constrained random partitions, not merely an isolated coefficient identity.

## Limits

Only fixed class size and interior fixed block density are treated. The critical rays and exact finite-sample sign transitions remain open. Experimental checks do not certify the infinite statements.

Self-review: passed. Independent audit: not yet performed.

