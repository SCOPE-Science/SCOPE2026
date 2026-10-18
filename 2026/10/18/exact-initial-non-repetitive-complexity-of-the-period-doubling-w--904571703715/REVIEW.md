# Scientific review

## Correctness — PASS

The binary fixed point obeys the two decimation identities \(p_{2j}=0\) and \(p_{2j+1}=1-p_j\). Because length-at-least-four factors contain a \(1\) and all \(1\)s occur at globally odd positions, factors from opposite starting parities cannot coincide. Even-start factors of lengths \(2m\) and \(2m+1\) encode exactly a length-\(m\) factor of the original word. Odd-start factors encode length \(m\) and \(m+1\), respectively. The monotonicity of the initial collision index in factor length proves that the even class collides first, giving an exact induction for both the first collision and its unique earlier partner. The three base lengths are checked directly. Executed literal-factor verification confirmed the formula at all lengths through \(256\) and eighteen larger diagnostic lengths through \(8192\). Computation is supplementary to the infinite proof.

## Originality — PASS with residual risk

Nicholson–Rampersad's accessible full article determines initial non-repetitive complexity for the Thue–Morse, Fibonacci, and Tribonacci sequences, but does not state the period-doubling result. OEIS A366462 and A367184 offer important related results: global longest windows of unique factors, and dyadic prefix attainment. In particular, the dyadic observation is acknowledged as previously covered in substantial part. Their results do not provide an all-positive-length exact prefix-collision formula with both collision indices. Published research searches also found a period-doubling string-attractor theorem, a different invariant whose conclusion does not imply the prefix repetition threshold. Searches cannot establish absolute uniqueness; a hidden or unindexed equivalent formulation remains possible.

## Mathematical value — PASS

The quantity is a natural named complexity invariant, and the theorem gives its complete exact function—not just computed values or a small extension of a table—for a canonical automatic word. The law is discontinuous at the two dyadic subscales, identifies the first repeated pair at every length, and gives sharp distinct asymptotic lower and upper ratios. The proof's parity-decimation argument explains the phenomenon and quantitatively distinguishes this word from the known Thue–Morse initial-repetition law. These are natural structural facts about early factor recurrence, rather than arbitrary parameter slices.

## Limits

No assertion is made about the maximum length of a factor-distinct window at arbitrary positions or about every repetition in the word. Relevant database tables and indexed results were inspected, but unindexed equivalents remain a possibility.

Self-review: passed. Independent audit: not yet performed.
