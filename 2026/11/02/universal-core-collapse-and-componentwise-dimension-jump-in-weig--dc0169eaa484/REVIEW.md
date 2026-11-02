# Scientific review — weighted trust-game core phase diagram

## Correctness: PASS
The proof derives the exact deletion identity for each omitted vertex and uses its summed core upper bounds to exclude every nonzero graph below the half-weight threshold. At the threshold, a feasible incoming-degree allocation saturates all deletion bounds, enforcing uniqueness. Above it, a translated graphical edge-splitting zonotope supplies feasible core points. The positive-support incidence rank establishes the dimension lower bound; component/co-component coalition constraints give matching independent affine equations. Explicit allocations for every restricted subgame establish total balancedness. The all-zero graph and coefficient endpoints are treated separately. Exact-rational independent finite checks cover 2,555 parameter instances; they are supporting tests, not an infinite proof.

## Originality: PASS, with stated limitations
Bandhana–Kroupa–García (AAMAS 2024) studied only the equal-coefficient sum. Ryzák–Kroupa (arXiv:2605.18157v1, Sections 5–6) establish its singleton core and total balancedness and explicitly leave parametric mixing as a direction. A separate pre-existing general aggregation-operator insertion criterion already implies the total-balancedness side of the present threshold; accordingly that implication is background, not the novelty claim. Neither of those compared claims entails the every-graph core-collapse inequality below the threshold or the exact \(n-c\) affine-dimension law above it. Graphical zonotope literature supplies an ingredient but not these mixed-game consequences without the deletion and component arguments. No equivalent published theorem was located. Residual risk: unindexed or other unpublished work may contain equivalent geometric classification.

## Mathematical value: PASS
The sharp transition resolves the cited concrete parametric stability question for every finite weighted directed graph and identifies the full affine dimension of stable payoff freedom, distinguishing connected from disconnected trust networks. A sharp universal collapse combined with component-dependent growth is structural information not supplied by a generic existence theorem or by the single original equal-mixture allocation. The strict-inclusion example distinguishes the core geometry from a routine direct rescaling of the induced-edge zonotope. The theorem does not classify vertices or volume of the resulting higher-dimensional core.

## Scope and closest literature
The primary comparator is Ryzák–Kroupa (2026), arXiv:2605.18157v1; the model originated in Bandhana–Kroupa–García (2024). The proof is restricted to nonnegative loopless weighted networks, convex mixing coefficients, and ordinary transferable-utility cores. Supporting finite computations do not establish uniqueness in the broader literature.

Self-review: passed. Independent audit: not yet performed.
