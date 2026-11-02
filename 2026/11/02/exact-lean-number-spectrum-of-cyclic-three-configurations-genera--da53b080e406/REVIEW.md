# Scientific review

## Correctness — PASS

The all-equal-or-rainbow condition on three colors is equivalent to a mod-three linear sum, with constants removed because two colors cannot form a nontrivial connected lean coloring. The kernel dimension follows from a cyclic polynomial gcd; the quadratic factor of \(1+t+t^3\) has roots of order eight, giving nullity one or three and therefore exactly zero or 24 nontrivial ternary assignments. The explicit eight-periodic words account for every such assignment and its monochromatic-edge frequency. Four concrete cyclic four-color blocks satisfy the local triple condition, and all concatenation boundaries were checked. The Fano Steiner property supplies the separate order-seven five-color optimum and its exact count. The standalone verifier passed 560 gcd-vs-rank comparisons, 56 direct assignments comparisons, exhaustive Fano counts, periodic cases and 293 constructive checks. Finite tests are not substituted for the general proof.

## Originality — PASS, with historical-priority risk

Piehowski's 2026 work establishes the lean-number definition and general theory, but the inspected connected-uniform, overlap-construction and future-work material does not state this all-order cyclic-generator classification or the 24/840 named optimum counts. A further directly relevant primary comparison is Erskine (2021), Theorems 2.5 and 3.4: it treats these exact cyclic triples and proves blocking-set and **strong-coloring** theorems, including the all-order strong chromatic spectrum. Strong coloring imposes rainbow triples on every edge; its results do not imply the lean spectrum, its sharp four-color constructions for lengths not divisible by four, or the 24/840 optimal counts. The classical cyclic configuration source identifies the Fano and Möbius–Kantor instances and studies another invariant, splittability. Fox tricoloring already supplies the elementary mod-three conversion, explicitly excluded from novelty. Searches comparing cyclic coloring, ternary kernel, and hypergraph lean terminology did not identify a statement implying the three-part spectrum and counts. Equivalent work under older ternary coding/Latin tricoloring terminology is an unresolved priority risk.

## Mathematical value — PASS

This is an all-order, complete minimum-color classification of a natural family linking the first two classical cyclic three-configurations, with a sharp divisibility transition, exact number and structure of the ternary optima, an exceptional Fano boundary, explicit constructions in the complementary lengths, and an infinite strict separation from strong coloring. These conclusions are stronger than isolated computation or a routine renaming of the Fox congruence.

## Constraints on the claim

There is no claim of a general formula for arbitrary cyclic generators, a count of all optimum four-color configurations, a knot-theoretic result, or external verification.

Self-review: passed. Independent audit: not yet performed.
