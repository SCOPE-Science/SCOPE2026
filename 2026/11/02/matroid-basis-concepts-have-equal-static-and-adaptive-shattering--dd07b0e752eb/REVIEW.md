# Scientific review: matroid basis shattering

**Correctness — PASS.** Shattered supports are exactly sets independent in both the matroid and its dual: basis extension proves sufficiency for every labeling. Edmonds' intersection min-max formula supplies the exact invariant. Direct computation of the two minors' rank formulas yields the deletion-contraction identity, making every nonconstant query an optimal root by induction. The code independently verifies the dimensions and root identity for 1,347 distinct small binary matroids plus a ten-element imbalanced example. Finite enumeration corroborates, but does not replace, the all-matroid proof.

**Originality — PASS within the material compared.** Dedicated published-finding corpus and literature searches for matroid base shattering, common dual independence, Edmonds' formula, VC dimension and Littlestone dimension found no equal or dominating theorem. The principal matroid-bases primary source addresses cardinality constraints on intersections of two bases rather than shattering of a single basis family; the inspected general Littlestone paper lacks a matroid-basis theorem. Historical priority remains incompletely verified, especially in older matroidal set-system literature.

**Value — PASS.** A natural broad class has exactly equal static and adaptive shattering dimensions, characterized by a classical, polynomial-time-computable matroid intersection invariant. The every-eligible-root optimality property and precise contrast with rank/corank are structural features, not a routine recomputation of an isolated numerical example.

**Closest literature and limitations.** Lendl–Peis–Timmermans (arXiv:1907.04741) studies constrained intersection of two matroid bases; Chase–Freitag–Reyzin (arXiv:2310.04812) develops general query-learning theory; Guingona et al. (arXiv:2109.04805) concerns zero sets; Manurangsi–Rubinstein (arXiv:1705.09517) treats computational hardness on general classes. No independent scientific audit or exhaustive older-literature comparison has been performed. The result is restricted to membership queries on matroid bases.

Self-review: passed. Independent audit: not yet performed.
