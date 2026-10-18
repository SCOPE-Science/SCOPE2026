# Scientific review

## Correctness — PASS

The circular coverage-set definition is explicit and tests factors of all lengths from one to the whole word. The proof calculates exact coverage sets for four words, shows every other factor's coverage set contains at least one of those four by a complete case split, and then reduces all two-position solutions to two interval-intersection inequalities. The case \(q=1\) (empty ordinary gaps), case \(m=2\) (no interior one positions), case \(s=1\) (Christoffel boundary), and case \(s>q\) (no interior pair choices) are all included. Direct literal exhaustive testing over 252 parameter triples validates set equality, all one-point exclusions, and the four-factor dominance property. The infinite scope rests on proof, not experiments.

## Originality — PASS within inspected evidence

Mantaci et al. 2021, Theorem 34, characterizes existence of **consecutive** two-position circular attractors for primitive standard Sturmian conjugates; it neither gives all position pairs nor covers the general single enlarged gap. Romana 2023 establishes verification algorithms and NP-completeness, not this formula. Banbara et al. 2026 counts all ordinary attractors for Fibonacci, period-doubling, and Thue–Morse words; this proof handles different objects, circular factor coverage, and three arbitrary positive parameters. The closest public research records concern antipalindromic pseudostandard, Thue–Morse, Fibonacci, or period-doubling word families, none of which imply the present exact classification. Targeted alias/formula/reduction searches found no direct antecedent. An unindexed equivalent statement remains possible; absence of a search result is not treated as proof of novelty.

## Value — PASS

The 2026 all-optimum-attractor classification program asks for meaningful structure beyond the minimum attractor size. Here a natural one-defect perturbation of a periodic circular word yields an exact family-wide optimal-pair classification, an explicit phase transition in multiplicity, and a constant-size factor testing basis valid for arbitrary marked-set cardinalities. This provides a controlled model for understanding how one exceptional zero gap alters the geometry of optimal circular attractors, including the Christoffel boundary. It is a parameterized structural theorem, not a renamed definition or isolated computational slice.

## Scope and risk

The result does not address two or more anomalous gaps, linear string attractors, or independent historical priority. Computation is finite corroboration only. Public literature comparisons are not an exhaustive search of all unpublished sources.

Self-review: passed. Independent audit: not yet performed.
