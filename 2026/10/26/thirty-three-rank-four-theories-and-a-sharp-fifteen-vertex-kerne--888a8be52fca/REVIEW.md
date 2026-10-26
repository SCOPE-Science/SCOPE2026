# Scientific review: rank-four pentagon blow-ups

## Correctness

**PASS.** Every graph in the claimed family admits the part-preserving four-move game reduction to five clone sizes at most four. Exact tuple types are defined inductively from complete atomic diagrams and sets of one-point extension types; this recurrence is equivalent to quantifier-rank equivalence. Quotienting only by permutations of unused vertices inside a part is exact, because selected vertices are fixed and all remaining vertices in that part have identical adjacency to every selected vertex. The resulting 1024-element exhaustive classification gives exactly 33 types, with every type realized at clone sizes at most three. Every class has a representative of order at most 15; the only class with shortest order 15 is the one containing the vector \((3,3,3,3,3)\). Direct labelled-graph recursion separately checks all 243 three-clipped graphs and all 29,403 unordered pairs of them. The code and its output are included.

## Originality

**PASS, with residual risks.** Hatami et al. (arXiv:1102.1634, Section 2.3 and Theorems 3.1–4.2) define this pentagon blow-up construction and solve an extremal five-cycle counting problem, but neither enumerate first-order rank-four types nor establish the representative cutoff. Balogh et al. (arXiv:1411.4645, Theorems 1–2 and Sections 2–4) study inducibility and iterated blow-ups, not elementary equivalence. Brown and Hoshino (Ars Combinatoria 83, Theorems 3.1 and 3.9) analyze games on pure paths and cycles, not variable-size clones. Indexed published research records contain nearby quantifier-rank classifications but no examined statement implying this pentagon-blow-up census. Broad unindexed literature and results formulated in an unexpected equivalent graph-class language remain possible overlap risks. Nonmatches are supported by comparison of mathematical statements, not by failed keyword searches alone.

## Value

**PASS.** The nonempty pentagon blow-ups form a natural five-parameter family arising in extremal triangle-free graph theory. A complete exact classification of their low-depth first-order observable behaviour, including 33 distinct classes, the unexpected stabilization at three clones per part (rather than the a priori four), and a sharp 15-vertex testing bound, is a motivated finite-model-theoretic invariant. It gives a finite exact decision procedure for rank-four satisfiability/validity over this infinite family, not merely a computation on a chosen small graph.

## Scope and risks

The result is not a classification of all triangle-free graphs, of richer signatures naming the parts, or of five-cycle substitutions by arbitrary graphs. The underlying logical-type recurrence and generic four-pebble truncation are standard; the novelty assessed here is the exact 33-class outcome, collapse to three-clipped vectors, and sharp bound. The logical proof and computations are included, but independent external audit is pending. Relevant full text was examined for the closest comparison sources; some other possible historical overlap remains unindexed.

Self-review: passed. Independent audit: not yet performed.
