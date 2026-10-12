# Scientific review of an exact run-limited cyclic cover theorem

## Correctness — PASS
The edge-covering-walk equivalence and explicit strong connectivity reduction are elementary and cover all \(n\ge3\). The sharp lower bound follows from integral surplus–deficit path decomposition and the first equal pair index. The constructive injection from source vertices to deficit vertices is recovered from the last equal pair of the endpoint, yielding exactly optimal extra edge traversals. A Fibonacci recurrence determines their sum. The \(n=2\) case is separately witnessed by `0011`. Both included independent programs passed for their specified ranges, but the proof is valid for all integers in the claim.

## Originality — PASS (with residual risk)
Moreno–Matamala's 2007 paper addresses *lexicographic* minimum among exact-once restricted cycles. Tan–Shallit (2013) define the relevant general shortest circular witness and prove bounds without this all-length dictionary-specific Lucas value. Chee et al. (2024) optimize maximum distinct-window RLL cycles, not shortest complete repeated-window covers. Searches for cyclic covering walks, forbidden triples, run-limited postman tours and Lucas/Fibonacci exact costs found no same-claim statement. The inaccessible original conference edition and unindexed prior computations remain possible overlap risks; search absence alone is not proof of priority.

## Value — PASS
The run-two binary language has no exact-once universal cyclic cover when \(n\ge4\), making minimum unavoidable factor repetition a natural invariant. The result determines this redundancy and a realizing construction *for every order*, with a nontrivial path-bijection proof; it is neither a known numerical table nor an arbitrary finite restriction. It does not count all optimum tours or generalize to other run limits.

## Verification and limits
Included `construct.py` and `independent_optimality.py` use different constructions and algorithms. They replay exact finite instances but do not replace the infinite proof. Bibliographic uncertainty and scope restrictions remain as described in the accompanying result and structured audit.

Self-review: passed. Independent audit: not yet performed.
