# Scientific review

## Correctness — PASS

Uniform half-edge pairing gives the one-, two-, and three-pair event probabilities used in the exact moment calculation. Conditioning on each potential loop decreases the corresponding vertex's available half-edge pairs by \(2d_i-3\). The expression for \(\operatorname{Cov}(L,P)\) follows by subtracting the product of marginal means. A separate expansion into two- and three-vertex contributions yields the sign certificate. The triple term is nonnegative by a six-term AM–GM inequality; all negative degree-two pair contributions are compensated by a distinct triple with a fixed high-degree vertex. The degree-one boundary is resolved by parity. Independent exhaustive matching enumeration and rational computations check every admissible small profile tested, but are not substituted for the all-size proof.

## Originality — PASS, qualified

The standard model, both defect statistics, marginal means, indicator overlap probabilities, and asymptotic Poisson independence are prior results of Janson (arXiv:math/0609802) and Angel–van der Hofstad–Holmgren (arXiv:1603.07172). The original contribution assessed here is the **complete finite-size sign characterization over arbitrary degree sequences**, not the use of conditioning or the basic moments. Primary full texts were compared at the exact statistics, conditional overlap/Poisson sections and conclusions, and no statement of the two-regular-only positive sign law was identified. The exact mixed-moment formula may also be recoverable from their underlying indicator calculations; this is a residual originality risk, not evidence that their published asymptotic theorem states the sign classification. Wormald's broader 1999 survey was available only through bibliographic abstract material, leaving a historical-priority limitation. Relevant published-result searches were also compared, without a covering claim found. Independent priority verification is still needed.

## Value — PASS

Loops and parallel-edge pairs are the two standard defects governing simplicity of configuration models. Asymptotic independence does not resolve the sign of their finite-size covariance. The sharp contrast between positive covariance for exactly two-regular pairings and negative covariance for *all* other degree sequences is structural, covers irregular and degree-one cases, and rules out zero covariance whenever both defects are nontrivial. The decomposition explains the transition rather than reporting a small numerical curiosity.

## Scientific limits

The theorem assumes distinguishable half-edges paired uniformly and uses the count of unordered parallel-edge pairs, excluding loops. It does not cover the alternative number of excess parallel edges or total half-edge count four. The original claim has not received independent expert assessment; earlier broad methods could imply parts of the algebraic formula.

Self-review: passed. Independent audit: not yet performed.
