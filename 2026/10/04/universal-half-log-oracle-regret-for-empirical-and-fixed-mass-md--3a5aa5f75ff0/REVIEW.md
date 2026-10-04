# Same-model scientific review

## Correctness
PASS. The proof reconstructs the population and predictive optimization problems from the bounded-mean betting factor. The score identity \(M'(\lambda)=P h_\lambda\) and curvature identity \(-M''(\lambda)=P h_\lambda^2\) are exact. At an interior optimum, the score has mean zero, so its variance equals the curvature. Bounded support together with \(c<1\) gives uniform derivative bounds. Fixed endpoint-score separation makes boundary optimizer events exponentially unlikely; local score linearization plus bounded-summand moment control yields \(n\mathbb E(\widehat\lambda-\lambda^\star)^2\to J^{-1}\) and a negligible third-order remainder. The fixed-mass MDP term contributes only \(O(n^{-1})\) to the score uniformly over predictable bounded-support prior components. The deterministic Bernoulli verifier checks the finite-sample calculation without simulation.

## Originality
PASS with stated residual risk. The closest same-object source, arXiv:2605.07964v1, proves first-order log-optimality and an \(O(n^{-1/2})\) expected Wasserstein rate for MDP, not a second-order half-log oracle-regret law. Grünwald's discussion, DOI 10.1093/jrsssb/qkad128, explicitly says half-log GRAPA regret is suspected by parametric analogy and calls for further analysis. Orabona--Jun use a universal-portfolio mixture and a best-fixed-in-hindsight comparator; Wang--Agrawal--Ramdas prove almost-sure null bankruptcy. Targeted mathematical-database searches found no equivalent statement in the inspected indexed records. A generic sequential M-estimation theorem could conceivably imply the empirical special case under different terminology; no inspected result also covers the arbitrary predictable fixed-mass MDP perturbation.

## Value
PASS. This is not merely a routine consistency refinement: it resolves the leading regret coefficient in a gap explicitly identified in the bounded-mean betting literature and shows that fixed prior predictive mass is asymptotically neutral at second order. It improves the motivating MDP paper's directly available quantitative cumulative guarantee from square-root order to a sharp logarithmic leading law under the interior-oracle condition, and it yields an expected null-bankruptcy rate.

## Closest literature and limitations
The most relevant sources are Kilian--Cortinovis--Caron (2026), Grünwald (2024), Waudby-Smith--Ramdas (2024), Orabona--Jun (2024), and Wang--Agrawal--Ramdas (2026). The theorem does not cover boundary oracle bets, growing prior mass, pathwise regret, confidence-sequence width expansions, or an additive \(O(1)\) remainder. Public HTML full text of the 2026 null-bankruptcy paper was unavailable, so only its abstract-level scope was used in that comparison.

Same-model review: passed. Independent audit: not yet performed.
