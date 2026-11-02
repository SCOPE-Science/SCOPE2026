# Scientific review: centre of finite rook power monoids

## Correctness
PASS. The centrality obstruction uses single-point partial identities to exclude every moved arrow; invariance under conjugation by full permutations then forces complete rank layers. Conversely, rank-layer products with an arbitrary partial injection are identical on both sides because restrictions of any given size can be realized by choosing a domain or image subset with the same outside-complement capacity. Intersection cardinalities prove the exact product law. The idempotent classification follows from closure under rank decrement; a complement-union argument gives the exact powers of a single layer and the sharp exponent. `verify.py`, run on the present standalone file, produced `VERIFY_OK` with exhaustive centrality enumeration for base sizes 1 and 2, direct candidate/product checks for size 3, and rank-index checks through size 9.

## Originality
PASS with historical-priority qualification. Primary full-text comparison: Liu–Tringali, arXiv:2610.29525v1 (2026-10-21), proves inverse-semigroup power-monad rigidity using localizers; it does not imply the centre or rank-set multiplication without the new argument. Liu–Tringali, arXiv:2606.01917v1, treats the unit group/global isomorphisms. Tringali, arXiv:2602.15754v3, surveys factorization and rigidity. Konieczny's 2020 centralizer abstract concerns individual partial bijections inside the inverse monoid, not the centre of its nonempty power monoid. Searches for centre/center, power semigroup/semigroup of complexes, symmetric inverse/rook monoid, central subsets, and sharp aperiodicity did not reveal a direct covering theorem. Lack of indexing or accessible older treatments remains a real risk; search absence is not a proof of priority.

## Mathematical value
PASS. This completely describes a natural characteristic submonoid in an important infinite family of finite inverse-semigroup power monoids: every central element, multiplication, number of idempotents, and exact uniform stabilization identity. It distinguishes centrality of subsets from centrality of individual maps and shows that a commutative centre need not be a band. The exact exponent and rank product law support further structural and algorithmic study of semigroup power constructions.

## Scope and limits
The empty subset is excluded, while the empty partial bijection is included as an underlying monoid element. The general proof applies to all integers \(n\ge1\); exhaustive finite computations alone do not establish that generality. The theorem does not handle arbitrary inverse semigroups or infinitely many underlying points. Originality rests on compared published formulations and may be defeated by an unindexed equivalent prior result. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
