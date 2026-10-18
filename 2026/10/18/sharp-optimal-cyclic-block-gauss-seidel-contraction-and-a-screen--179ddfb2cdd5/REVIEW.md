# Scientific review

## Correctness — PASS

The claim is an exact **one-step** squared-energy minimax statement. The block normal equation gives the exact energy-drop identity and a symmetric eigenvalue optimization. The constant vector bounds the attainable worst-case reduction from above under *every* probability distribution, while the uniform average of the block maps is an entrywise nonnegative symmetric circulant matrix. A row-sum/spectral-radius argument proves the constant vector is its slowest mode. The tridiagonal Dirichlet recurrence gives the explicit Green sum; the critical scaling follows from the exact formula. All dimensions, coupling bounds, and limiting quantifiers are spelled out in `RESULT.md`. `verify.py` checks the exact finite equations; it is not substituted for the universal proof.

## Originality — PASS, with risks

The 2026 Xie–Yang preprint develops batch-coordinate sampling and general upper convergence bounds, but the inspected main theorems and numerical sections do not provide this complete optimal fixed-distribution rate, periodic tridiagonal block Green sum, or critical screened-Poisson crossover. The 2017 Tu et al. work treats accelerated block Gauss–Seidel, and its separate circulant/tridiagonal examples are not this matched periodic block model. Wu's 2018 block-Gauss–Seidel paper is relevant but only abstract-level access was available: full-document comparison remains a residual bibliographic risk. The nearby available mathematical results address single-coordinate optimal sampling, stochastic delays, or different Gaussian and block methods; neither the general theory nor those available specific statements imply the explicit new minimax value without the nontrivial positive-map/Green-function argument.

## Value — PASS

Choosing a fixed distribution over overlapping consecutive blocks is a concrete scheduling decision for batch coordinate descent on a standard discretized periodic screened operator. The exact all-size rate and globally optimal policy give a quantitative benchmark against learned and heuristic sampling. The nonconstant crossover \(F(s)\) identifies when near-singular coupling defeats small blocks and establishes the correlation-length scale needed to recover an efficient fraction of the ideal block improvement. It is a structural, sharp classification of a natural numerical family, not a single unmotivated finite example.

## Scope and unresolved matters

This does not optimize adaptive sampling, prove an exact multistep rate, extend to arbitrary cyclic/stochastic Hessians, or evaluate hardware cost. General block-projection identities and the existence of linear convergence are established prior results. Full-text access to every older relevant article was not achieved, so a prior equivalent result outside the inspected literature cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
