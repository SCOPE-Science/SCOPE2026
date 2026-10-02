# Independent audit — 2026-09-30

**Record:** `2026/09/08/031`  
**Audited source tree:** `c32351bb666bfdd9ddaf1270b8597e7accd6a13a`

## Final claim assessed

Fixed-(29,6) 6-regular circulants: Ramanujan dichotomy, best-expander witness (1,2,7), and 26-type spectral reference table

## Correctness — PASS

A fresh enumeration of all 364 generating triples modulo nonzero multipliers gives exactly 26 classes, each of orbit size 14. An independent adjacency-matrix calculation reproduces 12 two-sided Ramanujan classes and 20 one-sided classes, the unique minimum at (1,2,7) with spectral radius 3.8766697679, runner-up (1,2,11) at 3.9059816469, and the stated margin. Exact integer characteristic polynomials are pairwise distinct. Independently recomputed energies are pairwise distinct with the stated minimum gap and pair.

## Originality — PASS

The closest primary Ramanujan-circulant paper determines a valency/covalency threshold guaranteeing the Ramanujan property for all odd circulants of a fixed order; its theorem does not enumerate the degree-6 order-29 stratum, rank its 26 multiplier classes, or imply the energy and characteristic-polynomial census. The singular-cospectral literature supplies a general isomorphism implication, not the explicit fixed-stratum table. Searches for equivalent fixed-(29,6) tables found the present record but no earlier covering statement. The conclusion rests on scope/implication comparison, not on failed search alone.

The comparison explicitly checked equivalent formulations, broader coverage, exact database/table matches, and whether prior results logically imply the claim. An unsuccessful search was not treated as proof of novelty.

## Scientific value — PASS

This is a natural complete finite classification at a fixed prime order and low even degree, with a sharp Ramanujan boundary and a unique best-expander witness. The 26-row exact spectral reference table and near-boundary examples are reusable benchmarks; the result is more than a routine parameter substitution because it classifies every isomorphism type and several independent spectral invariants.

## Source inspections

- **Hirano, Katata, Yamasaki — Ramanujan circulant graphs and the conjecture of Hardy-Littlewood and Bateman-Horn** — Full-text PDF: abstract, problem formulation, Theorem 1.1, and circulant eigenvalue setup. General guarantee threshold over odd circulants; no fixed degree-6 order-29 isomorphism census or ranking. https://arxiv.org/abs/1310.2130
- **Conde et al. — Singularly cospectral circulant graphs** — Record-cited theorem scope and comparison were checked against the claim. Supports the known odd-prime cospectral-isomorphism implication but does not supply the explicit 26-type polynomials, energies, or Ramanujan ranking. https://arxiv.org/abs/2408.07200
- **Resultary semantic search for fixed-(29,6) Ramanujan circulants** — Top ranked result set and summaries. The exact statement resolves to this record; nearby records concern different graph families. https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE031

## Residual risks

- Spectral inequalities and energy separation are numerically certified with very large margins relative to floating-point disagreement but are not interval-arithmetic certificates.
- The originality search cannot exclude obscure unpublished computations; no covering published implication was identified.

## Disposition

**PASS.** Correctness, originality, and scientific value each pass for the final claim stated above.
