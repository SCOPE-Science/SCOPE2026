# Scientific review: certified Brownian reflection-rescaling first passage

## Correctness

**PASS.** The generator has a coercive quadratic Lyapunov drift and a uniformly elliptic Brownian component; these ensure finite point-hitting means. The Fourier resolvent iteration reconstructs the full transition resolvent. The standard point-hitting resolvent ratio, combined with its stationary-density pole, produces the expected hitting time from a difference of full-line resolvents. The \(1/2\)-Lipschitz bound for each convolution density justifies both the zero-Laplace limit and the geometric numerator remainder. Partial-fraction inversion is algebraic; the independent tail has a first absolute moment equal to a geometric sum, giving the denominator certificate. The finite verifier independently checks the full source Eq. (60), source Eq. (45), Fourier inversion and finite error enclosures. No finite computation is used as an infinite proof.

## Originality

**PASS, qualified.** The exact stationary product and the generic point-hitting identity are prior methods. In the fully read motivating publication, Sec. III.2 and Eq. (60) leave \(\kappa\) unknown and determine it numerically. The present claim supplies a convergent elementary series and certified finite error enclosure for that specific missing constant and all starting positions, not just a rederivation of the stationary distribution. Pierce treats nonnegative multipliers and does not solve this reflection case. Singh–Pal treats state-independent resetting, so cannot immediately imply the model-specific formula. Research-record searches did not identify a directly covering reflected full-line first-passage claim. Priority risk remains: a generic potential-theoretic identity could enable a different, unlocated implementation, and the searched literature cannot establish uniqueness.

## Mathematical value

**PASS.** The sign-reversing reset is a natural model exhibiting jumps across the target; the original analysis specifically identifies the unknown boundary value as the obstruction to a fully analytic mean first-passage formula. The new all-initial-position series determines the missing constant, including certified precision and exact treatment of jump-over events. It allows controlled physical parameter studies without stochastic calibration. The value is a resolved, explicitly published analytic gap, not a claim of a new general potential-theory principle.

## Limitations and risk

The analysis assumes a fixed negative contractive multiplier, a single target and Poisson reset times. Elementary partial fractions may suffer cancellation near the unit-modulus limit; arbitrary-precision evaluation is a computational concern. Exact priority cannot be certified by semantic search; an independent audit and additional specialist literature checks remain appropriate. Every correctness, originality and value conclusion here is only a self-review.

Self-review: passed. Independent audit: not yet performed.
