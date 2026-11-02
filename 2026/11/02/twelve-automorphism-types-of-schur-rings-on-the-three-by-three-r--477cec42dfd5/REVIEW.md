# Scientific review: three-by-three rectangular-band Schur rings

## Correctness — PASS
The class-sum product coefficient is exactly the product of the row count of the first class and column count of the second. Summation over all partition classes gives the necessary and sufficient profile-equality criterion. Restricted-growth strings enumerate each of the 21,147 set partitions exactly once. Two standalone programs implement independent direct multiplication and profile calculations, both obtaining 42 Schur partitions and the same rank distribution. The direct program also enumerates all 60 subgroups of the order-36 automorphism group, finds 42 distinct orbit partitions, and confirms equality with the direct-product-closed set. The other program checks class-stabilizer transitivity independently. Orbit canonicalization yields the 12 representatives and sizes in RESULT.md; both programs pass.

## Originality — PASS with residual historical uncertainty
The closest primary source, Marrow and Misseldine, *On Schur Rings Over Semigroups* (arXiv:2601.09940; initially public 2026-01-14), gives the multiplication-only definition, an automorphic construction, a direct-product lower bound, and small-semigroup enumerations through order seven; its rectangular-band discussion explicitly notes that direct products need not be exhaustive. The new statement concerns order nine and gives the full count, 12 automorphism types, a converse automorphic realization, the complete class-count spectrum, and 17 genuinely non-product partitions. A distinct classification covering two-row rectangular bands cannot imply the three-row square case. Queries of public mathematical literature and semantic mathematical records using exact band, Schur-ring, orbit, class-sum, and enumeration terminology did not show equivalent coverage. The absence of a retrieved result is not proof of priority, and further unindexed classifications remain possible.

## Mathematical value — PASS
This is the first square rectangular band with both factors of size at least three, outside the published order-at-most-seven census and outside the two-row family. The exhaustive classification describes all algebraically admissible partitions, not an arbitrary sample: 42 labeled objects, exactly 12 natural symmetry types, and no nonautomorphic examples. The difference between 25 direct-product constructions and the complete 42 illustrates the central gap raised by the motivating paper, while the explicit representatives and coefficient criterion give concrete benchmarks for general rectangular-band classification.

## Risks and limits
The proof includes a finite exhaustive certificate for 21,147 partitions, not a hand-derived general formula for larger bands. The converse automorphic classification is only established for the three-by-three band. Absolute publication priority and independent validation have not been certified.

Self-review: passed. Independent audit: not yet performed.
