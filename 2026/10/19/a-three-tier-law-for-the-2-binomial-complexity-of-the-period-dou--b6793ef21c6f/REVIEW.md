# Scientific review

**Correctness — PASS.** Every length-\(2m\) factor of the period-doubling fixed point is an even-position or odd-position lift of a length-\(m\) factor. Both lift types occur for every source factor. Counting scattered `01` pairs gives the exact affine transfer \(T_B=\binom z2+2z(m-z)-2t\) and \(T_A=T_B+z\); the new zero count is \(2m-z\). The five length-three base factors are complete. Odd outer-tier zero counts force disjoint images by parity, doubling each tier; the even middle tier's two images merge into one arithmetic progression, adding precisely one value. This proves all parameters. Independent finite substitution and sliding-factor tests return `VERIFY_OK`, but infinite correctness rests on the proved induction.

**Originality — PASS against inspected primary and database evidence.** Rigo–Salimov (2013) introduces the invariant and treats other morphic words. Parreau–Rigo–Rowland–Vandomme (2015) studies a different, contiguous 2-abelian invariant. Lejeune (2021, thesis Section 4.5, pp. 115–116) supplies the closest period-doubling analysis: an exact equality criterion at dyadic lengths, strict non-equality elsewhere, and a chart of values through length 70; it explicitly says the function could not be precisely computed. Those results do not imply the exact all-\(k\) non-dyadic formula or the three-tier progression. Targeted database searches yielded no covering statement. Risk: an equivalent exact ray may appear in other unindexed research.

**Mathematical value — PASS.** This is an exact infinite family in an incompletely characterized automatic-word complexity function. The three-tier geometry explains a non-obvious linear-plus-logarithmic growth law and describes which scattered-pair statistics coexist with each zero count. It goes beyond re-evaluating a known finite table or the previously solved power-of-two cases.

**Limitations.** No arbitrary-length formula, no independent scientific audit, and no assertion that a search proves global priority.

Self-review: passed. Independent audit: not yet performed.
