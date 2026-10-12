# Scientific self-review

## Correctness — PASS

The theorem specifies the standard binary extended Hamming parity-check columns, defines both window conventions, and handles all \(m\ge2\). At width two the counting identity is exact because syndromes split by parity. The linear and cyclic telescoping arguments separately exclude full adjacent-difference coverage. For the explicit primitive ordering, the internal differences are all distinct and miss the single label \(\Delta\); the head and cyclic tail edges are repetitions. The separated-by-two identity produces exactly this missing label in an ordinary three-window. The index \(q-2-t\) is within \([0,q-4]\), including the boundary \(m=2\). The extracted `verify.py` independently checks finite dimensions \(2\) through \(8\); a finite test is not substituted for the all-dimensional proof.

## Originality — PASS, with residual uncertainty

Sac Himelfarb and Schwartz's full 2026 manuscript introduces the metric and gives the length-eight positive example; its Theorem 17 is a general counting bound, not an all-length constructive classification. The all-length sharp one-hole count and two-to-three-window lift are not consequences of their specific example. Searches of exact claims, aliases involving consecutive XOR differences/terraces, related syndrome and burst coding papers, and indexed findings did not locate a covering statement. A historical near-terrace formulation remains a genuine residual risk, particularly because only abstract-level material for one related group-ordering article was available. Absence from searches alone is not taken as proof of novelty.

## Mathematical value — PASS

Burst covering controls localized parity-check access, so the least feasible window length and the exact syndrome deficit are natural code invariants, not arbitrary instance statistics. The newly introduced 2026 setting explicitly motivates understanding more families. This theorem gives the optimal radius for an infinite classical family, a uniform constructive ordering, the sharp obstruction for every ordering, and the explicit identity showing how a single longer window closes the gap. It does not claim new burst-error correction or a classification of all optimal permutations.

## Independent validation

Self-review: passed. Independent audit: not yet performed.
