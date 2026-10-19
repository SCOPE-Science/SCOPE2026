# Scientific review

## Correctness

PASS. The four-state substitution is derived from the Rudin–Shapiro binary recurrence. Its eight-pair adjacency closure is exhaustive for the fixed point. Expanding all pairs to 16 coded letters proves the absence of any shared length-eight factor between even and odd positions. The parity-constrained decimation of identical factors is reconstructed separately for both starting parities; the strict inequality before \(2R(\lceil n/2\rceil)\) rules out every earlier collision. The initial cases are exactly checked and an even-index prefix match attains the lower bound at every induction step. An executable independent generator and finite substring scan support the arithmetic and certificate.

## Originality

PASS on the inspected record, not a uniqueness certification. Nicholson–Rampersad (arXiv:1507.08206, 2015) study initial non-repetitive complexity but treat the Thue–Morse, Fibonacci and Tribonacci cases, not Rudin–Shapiro. Lü–Chen–Wen–Wu (arXiv:1606.06935, 2016) study Rudin–Shapiro abelian complexity, which cannot determine precise exact-factor collisions. Focused literature searches and published research-result searches detected no equivalent theorem or stronger result implying the claimed first-repetition law. Previously accessible findings concern other invariants and word families. Residual risk: an equivalent result may appear in unindexed literature or in a different invariant's formulation.

## Mathematical value

PASS. A classical automatic sequence receives a complete all-length exact formula for a prefix-sensitive complexity invariant introduced specifically to distinguish local and global factor diversity. The theorem also identifies the uniquely earlier occurrence and proves the sharp liminf/limsup oscillation. The eight-factor parity recognizer supplies a structural reason for the result; it is not a recitation of numerical counts or a routine consequence of known abelian complexity.

## Limits

No result is asserted for shifted scans or generalized Rudin–Shapiro families. Primary full-text comparisons cover the relevant initial non-repetitive and abelian complexity papers; remaining unknown equivalent literature cannot be ruled out. The computational checks are finite, but the proof is a complete induction.

Self-review: passed. Independent audit: not yet performed.
