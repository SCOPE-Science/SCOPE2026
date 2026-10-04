# Same-model review
## Correctness
PASS. The source Bernstein expansion makes the lower comparison \(K_n\le S_n\) immediate. If \(A_{k_*}=S_n\), evaluation at \(\lambda=k_*/n\) gives \(K_n\ge b_{n,k_*}S_n\), so the only global constant needed is the minimum of the binomial point masses \(b_{n,k}\). Their exact adjacent ratio is the ratio of two terms \((1+1/r)^r\), which places the minimum at the center. The sparse family with \(k\) coordinates equal to \(L\) and the rest zero has a uniformly convergent normalized product objective, giving the matching limiting ratio. The capped p-value corollary follows by elementary case splitting.

## Originality
PASS. The motivating paper proves only the one-sided inequality \(K_n\le S_n\) and states that SymPol yields a no-larger p-value than KL-inf. Its inspected theorem, proof, algorithmic section, and conclusion do not state a reverse multiplicative comparison, a sharp constant, or a square-root worst-case ratio. The later Gaffke paper compares a third merger to SymPol under independence rather than quantifying the SymPol/KL-inf gap. Targeted published-finding corpus and web searches for the exact ratio, central-binomial factor, Bernstein-coefficient formulation, and square-root p-value gap returned no equivalent statement. The underlying Bernstein-basis maximum is classical, so an equivalent approximation-theoretic inequality may exist under different terminology; this is retained as a residual risk rather than treating failed search as novelty proof.

## Value
PASS. The motivating work advertises SymPol as a uniformly stronger replacement for optimized constant betting but leaves the possible magnitude of that improvement unspecified. The exact best factor answers that finite-sample design question completely: the improvement can be as large as order \(\sqrt n\), cannot be larger, and the extremal scale is realizable by genuine nonnegative e-value vectors. This provides an interpretable worst-case calibration of how much is gained by computing SymPol instead of the simpler optimized product statistic.

## Closest literature and limitations
The closest source is Ming et al., arXiv:2603.10329, especially Theorem 3.3, equation (14), and the conclusion comparing SymPol with KL-inf. Ming et al., arXiv:2607.18661, is the closest later comparison because it shows Gaffke's p-value is no larger than SymPol under independence. The present result is only a worst-case deterministic comparison of SymPol and KL-inf; it does not claim a comparable power ratio or dominance over other mergers.

Same-model review: passed. Independent audit: not yet performed.
