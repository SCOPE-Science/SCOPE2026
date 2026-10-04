# Four further good-abundancy cases for the layered-number open question

## Finding
Let \(a_i\) denote the least positive integer with abundancy index \(I(n)=\sigma(n)/n\ge i\), and let \(g_i\) denote the least such integer additionally satisfying \(i\mid\sigma(n)\). For each \(i\in\{14,15,16,17\}\),
\[
a_i=g_i.
\]
A uniform witness is
\[
(q_{14},q_{15},q_{16},q_{17})=(83,149,127,13633),
\]
with \(q_i\parallel a_i\) and \(q_i\equiv-1\pmod i\).

## Assumptions and scope
The exact values of \(a_i\) for \(14\le i\le17\) are taken from OEIS A023199 in its colossally-abundant representation
\[
a_{14}=c(2621)\cdot710,\quad
a_{15}=c(4567)\cdot\frac{2}{21},\quad
a_{16}=c(8011)\cdot\frac{1}{2},\quad
a_{17}=c(13999)\cdot1630,
\]
where \(c(p)\) is the smallest colossally abundant number containing the prime \(p\). The multiplicities used below are read from OEIS A073751, whose ordered prime factors multiply to successive colossally abundant numbers. The claim is only about equality \(a_i=g_i\); it does not assert that these numbers are \(i\)-layered.

## Proof
Jokar defines good \(i\)-abundant integers by the two conditions \(I(n)\ge i\) and \(i\mid\sigma(n)\), and therefore always has \(a_i\le g_i\). It is enough to prove \(i\mid\sigma(a_i)\).

For \(i=14\), A073751 places the first occurrence of \(83\) at position \(37\), its second at position \(572\), and the first occurrence of \(2621\) at position \(425\). Thus \(83\parallel c(2621)\), and the multiplier \(710\) does not contain \(83\). Hence \(83\parallel a_{14}\). Since \(83+1=84\) is divisible by \(14\), multiplicativity of \(\sigma\) gives \(14\mid\sigma(a_{14})\).

For \(i=15\), the first occurrence of \(149\) is at position \(52\), its second at position \(1500\), and the first occurrence of \(4567\) is at position \(673\). Thus \(149\parallel c(4567)\); multiplying by \(2/21\) leaves its exponent unchanged. Since \(149+1=150\), we get \(15\mid\sigma(a_{15})\).

For \(i=16\), the first occurrence of \(127\) is at position \(47\), its second at position \(1145\), while \(8011\) first occurs at position \(1072\). Thus \(127\parallel c(8011)\), and division by \(2\) does not affect that exponent. Since \(127+1=128\), we get \(16\mid\sigma(a_{16})\).

For \(i=17\), the A073751 block from positions \(1687\) through \(1727\) contains \(13633\) exactly once, at position \(1687\), and ends with the first occurrence of \(13999\) at position \(1727\). Hence \(13633\parallel c(13999)\); the multiplier \(1630=2\cdot5\cdot163\) does not affect it. Since \(13633+1=13634=17\cdot802\), we get \(17\mid\sigma(a_{17})\).

Therefore every \(a_i\) in the stated range is itself good \(i\)-abundant. Since \(a_i\) is already the least \(i\)-abundant integer, \(g_i=a_i\).

## Verification
The accompanying `verify.py` checks the four congruences, the source-position inequalities that force exponent one, and that the correcting rational multipliers do not contain any witness prime. It prints `VERIFY_OK` on success.

## Relationship to prior work
Jokar's 2022 paper proves \(a_i=g_i\) for \(1\le i\le13\) except \(i=5\), then asks whether \(a_i=g_i\) for every positive integer other than \(5\). The proof above extends exactly the same prime-witness mechanism through the next four available exact values, \(i=14,15,16,17\). Searches for the equality at these four indices, the four witness primes, and the open-question terminology did not locate a prior statement of this extension.

## Limitations
This is a finite extension, not a resolution of the open question for all \(i\). The exact \(a_i\) inputs are external tabulated facts; this note verifies the new divisibility implication from those facts rather than recomputing the global minimality of \(a_i\). OEIS A073751 notes a general conjectural issue about prime ratios of consecutive colossally abundant numbers, while also reporting that prime ratios have been verified for the first \(10^7\) terms; only positions at most \(1727\) are used here.

## References
1. F. Jokar, “On \(k\)-layered numbers,” arXiv:2207.09053v1, 19 July 2022.
2. OEIS A023199, “\(a(n)\) is the least \(k\) with \(\sigma(k)\ge nk\),” especially the exact formulas for \(a(14),\ldots,a(17)\).
3. OEIS A073751, ordered prime factors whose cumulative products give colossally abundant numbers, including its b-file and computation notes.
