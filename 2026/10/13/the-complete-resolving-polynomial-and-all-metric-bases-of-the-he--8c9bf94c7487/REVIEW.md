# Self-review

## Correctness — PASS

The explicit Fano incidence construction proves that the 42 same-side vertex pairs have distinct equidistance sets, each of size eight; all opposite-side pairs have empty equidistance sets. The universal pairwise definition of metric resolution therefore becomes a complete finite forbidden-subset criterion. The proof independently characterizes every five-element resolving set via the Fano incidence classes and noncollinearity: 21 line pairs, four admissible point triples each, and 84 duals. The standalone code exhaustively enumerates all 16,384 subsets and checks the forbidden-set criterion against direct shortest-path distance signatures, then checks the 336 automorphisms and one base orbit. Counts are exact integers; no sampling or inferred infinite statement is used. Correctness depends on the program's transparent, fully included finite enumeration for polynomial coefficients.

## Originality — PASS, with residual priority risk

Héger--Takáts explicitly prove the minimum size five for the Fano plane in Remark 2.6 and provide general resolving-set decision criteria (Propositions 2.2--2.3), so neither the scalar metric dimension nor the existence of an abstract all-set characterization is claimed new. Their order-at-least-23 classification does not cover the Fano minimum-base multiplicity. Bailey's small-graph table likewise gives minimum size, not the polynomial or the exact 168-base single-orbit classification. published-finding corpus searches for exact Fano/Heawood ordinary metric-basis enumerations, resolving polynomials, and aliases found no equivalent record; related chain-graph resolving-polynomial work concerns different graphs. The finite geometric decomposition and exact all-size coefficient count require additional arguments beyond the scalar literature. Residual risk: an unindexed older census or a computational appendix may already give these counts.

## Value — PASS

Exact cardinality profiles and optimum symmetry types are natural, useful refinements of metric dimension: they count landmark configurations, quantify redundancy, and classify genuinely different optimal placements. The exceptional smallest projective plane is a motivated test case because its metric dimension is already distinguished in the source literature, while the explicit count and incidence-theoretic description were not supplied there. The structural 42-set obstruction also gives a reproducible route from geometry to the full polynomial. No extension to arbitrary projective planes or paper-sized downstream implication is asserted.

## Sources and limits

Primary full text inspected: Héger--Takáts, *Resolving sets and semi-resolving sets in finite projective planes*, arXiv:1207.5469, Propositions 2.2--2.3, Remark 2.6, and section on order at least 23; Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973, its Heawood entry and methods; Bailey, *On the metric dimension of imprimitive distance-regular graphs*, arXiv:1312.4971, the symmetric-design context. Computational enumeration is exhaustively finite; possible previously unindexed identical enumeration is an unresolved publication-priority risk.

Self-review: passed. Independent audit: not yet performed.
