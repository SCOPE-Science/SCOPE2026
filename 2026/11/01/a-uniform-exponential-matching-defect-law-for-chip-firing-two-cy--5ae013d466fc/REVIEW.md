# Scientific review

## Correctness — PASS

For ordinary synchronous degree-threshold chip firing on connected graphs, any primitive two-cycle has exactly one firing at each vertex across its two phases, because the graph Laplacian annihilates the two-step firing-number vector and its connected kernel is the span of constants. Each nontrivial firing-set cut contributes exactly the product of vertex cross-cut degrees, and time reversal divides the configuration count by two. For a complete graph with a matching deleted, split missing edges subtract one from the two relevant cross degrees and yield the stated triple binomial sum.

For the new asymptotic claim, weighted complete-graph cuts concentrate exponentially on shores of size at least one quarter of the vertices. Conditional on shore size, the number of deleted matching edges crossing the shore has first and second factorial moments given by exact hypergeometric probabilities. The rescaled count has mean exactly \(2k/(N-1)\) and variance \(O(N^{-1})\), uniformly for all admissible \(k\). The logarithmic replacement error of the cut-weight multiplier is also \(O(N^{-1})\) there. The tail is exponentially small. These estimates prove a uniform \(O(N^{-1})\) orbit-ratio error rather than extrapolating a numerical fit.

The packaged independent direct update program checked 2,375,520 small-graph chip vectors. The other checker compares exact triple sums with direct weighted-cut enumeration for every matching size through graph order ten and produces independent small-case counts. These are independent corroborating tests; the arbitrary-order proof is mathematical, not experimental.

## Originality — PASS, qualified

The general cut parametrization of chip-firing period-two configurations and complete-graph mass enumeration are prior knowledge and are explicitly excluded from the novelty claim; the finite matching specialization follows by applying the known cut identity. A previously established uniform bounded-degree deletion law on complete bipartite graphs gives a different exponent and a different typical shore-size regime. That bipartite result does not imply the complete-graph matching-defect ratio or its quantitative error estimate. The substantive assessed claim is the uniform ratio \(Q_{N,k}/Q_{N,0}=e^{-2k/N}+O(N^{-1})\). Levine's complete-graph activity classification, Jiang's graph-period results, and Jiang–Scully–Zhang's firing-pattern restrictions do not supply matching-deletion orbit-count asymptotics. Literature and published-result searches also compared equivalent formulations (chip-firing two-cycles and cut-weight enumerations) and superficially adjacent parity automata and matching-deletion graph invariants. No checked statement implies the uniform exponential defect law. A paper not indexed by the searches could still establish a stronger result; this residual priority risk is not equated to uniqueness proof.

## Value — PASS

Removing an entire perfect matching changes only a vanishing proportion of dense graph edges, yet the number of primitive chip-firing two-cycle orbits falls by an asymptotic fraction \(1-e^{-1}\). This detects a quantifiable boundary between combinatorial perturbation size and recurrent-state sensitivity. The law is uniform across every matching size, not merely a single numerically chosen family, and exposes a striking cancellation of the conditional cut-size dependence.

## Closest literature and limitations

- Lionel Levine, *Parallel chip-firing on the complete graph: Devil's staircase and Poincaré rotation number*, arXiv:0811.2800v1; inspected complete-graph period/activity discussion, noting its self-loop-inclusive convention.
- Tian-Yi Jiang, *On the period lengths of the parallel chip-firing game*, arXiv:1003.0943v1; inspected period-theoretic statements for complete bipartite/multipartite graphs.
- Tian-Yi Jiang, Ziv Scully and Yan X. Zhang, *Motors and impossible firing patterns in the parallel chip-firing game*, arXiv:1211.6786v1; inspected constraints on patterns rather than matching-defect orbit enumeration.

The conclusion applies to counts of primitive temporal period-two orbits, not an initial-state attraction probability. Computational tests alone cannot establish the uniform asymptotic. There is no claim of exhaustive worldwide coverage or independent review.

Self-review: passed. Independent audit: not yet performed.
