# Same-model scientific review

## Correctness
PASS. The direct pair-majority proof checks the quantifiers, cardinality, and nonprincipality. The finite statement is reduced exactly to maximum cliques in the subset compatibility graph. The standard-library verifier enumerates every maximal clique for \(3\le n\le10\), re-derives all codegree-three pairs, and checks exact set equality between enumerated maximizers and the claimed constructions. Boundary orders \(n=3,4,5,6\) and the first nonprincipal case \(n=7\) were included rather than inferred from a trend.

## Originality
PASS on a best-of-knowledge basis. The closest primary source is Keevash's 2026 preprint, which states the Simonovits--Sós conjecture, notes the fixed-3AP star, and proves a weaker universal density bound. The foundational 1986 Chung--Graham--Frankl--Shearer paper is the older source to which that conjecture is attributed. Targeted searches for exact small-order values, equality cases, codegree-three pairs, and the pair-majority construction did not locate a matching or stronger result.

## Value
PASS. Besides closing the conjectured optimum for eight consecutive small orders, the construction demonstrates a qualitatively different equality mechanism from a fixed 3AP and works for every \(n\ge7\). This constrains the form of any eventual stability or equality theorem.

## Closest literature
- Peter Keevash, *A non-trivial bound for 3AP-intersecting families*, arXiv:2609.18870v1 (2026).
- F. R. K. Chung, R. L. Graham, P. Frankl, J. B. Shearer, *Some intersection theorems for ordered sets and graphs*, JCTA 43 (1986), 23--37.

## Scientific limitations
The exhaustive classification stops at \(n=10\). No upper bound beyond the known conjectural target is claimed for larger \(n\), and no completeness claim for equality types is made for \(n\ge11\). The \(n=10\) census has not received independent implementation-level replication. Novelty is necessarily best-of-knowledge.

Same-model review: passed. Independent audit: not yet performed.
