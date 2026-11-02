# Self-review: simultaneous cyclic minima

## Correctness — PASS

The statement uses primitive binary necklaces and the alternating convention in which comparison at the first mismatching **one-based odd** position is ordinary and at an even position is reversed, matching the formal definition in Hendrian et al. The case with a circular \(00\) has incompatible prefixes \(00\) and \(01\). The first unequal gaps \(a<b\) are distinguished at position \(a+2\), which proves the odd-gap condition. The only tie possible for three zeroes is handled at position \(2a+3\). Counting anchored gap tuples yields the two rational generating functions and the exact unique-odd-minimum subfamily. Fixed-\(k\) asymptotics follow from a single order-\(k\) pole; the positive-density bound follows from a circular no-adjacent-zero count and the exponential rarity of periodic words. The verifier checks direct rotations rather than the same proof algorithm. Limit: finite enumeration does not prove the all-length assertions; the displayed argument supplies those.

## Originality — PASS, with residual priority risk

Hendrian et al. (arXiv:2403.02636, first public 2024-03-05) treat alternating-order word recognition, factorization and rotation algorithms and report factorization experiments; their results compute canonical representatives but do not count when they agree with the ordinary representative. Dolce–Restivo–Reutenauer (arXiv:1812.04515, first public 2018-12-11), including its alternating-order sections and remarks, treat generalized Lyndon factorization, not fixed-content comparison of two minima. Reutenauer's earlier general order and homographic Galois-number theory supplies definitions and algorithms, not the present coincidence statistics. The classical primitive necklace count only counts one representative per orbit and does not imply the intersection formula. Specific published-record and sequence-index searches found no matching claim. This does not eliminate a possible unindexed equivalent, alternate formulation or overlooked source; a separate priority check remains desirable.

## Mathematical value — PASS

Ordinary and alternating cyclic minima are the canonical orderings underlying ordinary and alternating Burrows–Wheeler variants. Their exact agreement is a natural stability question not settled by an algorithm for either minimum separately. The theorem gives an exact classification and rational generating functions in two first nontrivial fixed-content layers, an exact enumerated subfamily for arbitrary fixed content, and the asymptotically opposite behaviors of half-agreement at fixed zero count and exponentially negligible agreement at positive density. This is a structural relationship between two normalizations, rather than an arbitrary finite slice or renamed classical necklace formula.

## Limitations and priority

The general exact all-length count for four or more zeroes is not claimed. The intermediate density regime is untreated. Closest prior works and precise scope distinctions appear in `RESULT.md`, and actual literature comparisons with residual uncertainty are documented in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
