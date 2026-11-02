# Self-review

## Correctness

**PASS.** The statement is quantified for all integers \(n\ge2\) and real \(b\). The exact Hermite–Laguerre identity (1) fixes the normalization. Consecutive Laguerre zeros are simple, positive and interlacing, so every combination has the required real zero structure before lifting \(t=x^2/2\). The positive-residue partial fraction expansion of consecutive monic Laguerre ratios proves strict monotonicity of the negative-axis coefficient function. Its value and derivative at zero, together with its affine behavior at infinity, prove the sharp threshold, multiplicities, nonreal zero count, sharp global bounds, convex escape trajectory and both asymptotics. The finite checker passed 195 assertions; it is not used as a substitute for proof of the quantified claim.

## Originality

**PASS relative to inspected sources and accessible records.** Li and Gutman's complete 2000 paper states only \(|b|\le n-1\) as part of a general sufficient bound on Hermite gap mixtures, and does not classify all real coefficients or give imaginary-root escape inequalities. Durán's 2025 Hermite Theorem 1.2 establishes eventual real-rootedness without an exact degree/parameter threshold; his Laguerre 2025 results address general normalized combinations but do not state the parity-dependent Hermite threshold or sharp quantitative escape bounds. Their standard interlacing framework is acknowledged. The closest indexed mathematical records and existing related claims were checked for equivalent and stronger formulations. Earlier unindexed specializations of the Laguerre ratio identity remain possible.

## Value

**PASS.** This is the complete real-zero versus imaginary-pair classification for the natural two-gap Hermite family that appears in graph-matching-polynomial perturbations and recent Hermite-combination work. Its parity-dependent transition extends the uniform sufficient range in a sharp way; the global two-sided imaginary-escape estimate is nontrivial and optimal at two different scales. This is a natural all-degree classification, not an arbitrary finite calculation.

## Scope and risks

No higher-gap or complex-coefficient case is treated. The conclusion does not assert uniform asymptotics as the degree varies. Earlier equivalent facts might be implicit in general ratio theory or unindexed Hermite papers. The analytical proof was checked in the self-review only; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
