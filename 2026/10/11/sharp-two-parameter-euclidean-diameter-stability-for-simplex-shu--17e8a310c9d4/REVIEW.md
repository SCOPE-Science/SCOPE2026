# Scientific review

## Correctness — PASS

The ambient Euclidean norm and unscaled Minkowski-sum realization are fixed explicitly. Equation (1) follows from maximizing a convex squared norm over independent segment and simplex parameters, including degenerate zero weights. The two key deficit inequalities are checked symbolically by counting mixed columns and mixed rows; they hold for all finite sign matrices of every admitted size. The all-positive sign matrix attains the baseline in the subcritical rectangle, while a flipped entire row or column proves strict excess outside it. Exhaustive independent vertex-coordinate and signed-matrix calculations agree for 49 rational test cases. Risks: the finite verifier alone cannot prove the universal theorem, and the formula above thresholds is bounded below rather than determined exactly; both limitations are explicit.

## Originality — PASS with residual discovery risk

Chapoton–Pilaud [1] introduce the shuffle with exactly this complete-bipartite zonotope, but their inspected definition, construction, and combinatorial theorems give neither an ambient Euclidean diameter nor sharp weight cutoffs. Agnarsson–Morris [2] classify structural features of Minkowski sums of simplices, not this diameter. Deza–Pournin [3] work with edge-graph distances: their similarly titled diameter results do not imply the Euclidean formula. Pilaud–Poullot [4] work with normal-fan equivalence rather than Euclidean distances. Semantic searches of published mathematical findings and targeted literature queries yielded no statement with equivalent quantitative thresholds. This supports but cannot certify historical novelty; an exact specialization hidden under other geometric terminology is an acknowledged residual risk. Source comparisons are recorded in AUDIT.json.

## Value — PASS

The result computes a natural ambient metric invariant for a canonical shuffle construction and gives the entire sharp stability rectangle, not just one numerical diameter. The sharp thresholds depend separately on both dimensions and identify the exact point where a coherent opposing sign pattern ceases to maximize separation. The deficit–oscillation lemma is a reusable structural inequality for complete-bipartite cut-sign data. Although the unweighted complete-bipartite zonotope diameter is a known corner case, the sharp independent weight thresholds and explicit supercritical witnesses are meaningful for stability of Euclidean realizations of generalized permutohedra. No paper-scale application is claimed.

Same-model review: passed. Independent audit: not yet performed.
