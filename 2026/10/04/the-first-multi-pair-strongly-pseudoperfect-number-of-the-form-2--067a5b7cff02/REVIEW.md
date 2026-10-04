# Same-model review

## Correctness
PASS. For \(n=2^a p\), complementary closure partitions the divisor set into the \(a+1\) pairs \((2^i,p2^{a-i})\). Subtracting any omitted union from \(\sigma(n)=(2^{a+1}-1)(p+1)\) gives the reversible identity \(M-A_I=p(1+B_I)\). The cutoff requires only \(a\le11\), and exact enumeration checks every mask in that complete range. The boundary \(11776=2^9\cdot23\) has exactly one admissible mask, \(I=\{4,6\}\), so uniqueness is not inferred from a partial search.

## Originality
PASS with residual bibliographic risk. Wang--Zelinsky (2026) is the same-object source: it defines strongly pseudoperfect numbers, lists \(352\) with the one omitted pair \((8,44)\), and proves a Mersenne-prime rigidity theorem for \(2^k p\), but does not state the binary-mask criterion or the \(11776\) cutoff. Aryan et al. (2024) completely treat the strongly 2-near-perfect \(2^k p\) subcase, so the \(|I|=1\) specialization is prior coverage and is not claimed as new. Targeted searches for the exact number, the two-pair cutoff, binary-mask formulations, and the pair \(352,11776\) did not locate the accepted theorem. Unindexed or differently phrased prior work remains possible.

## Value
PASS. Strongly pseudoperfect representations are constrained by complementary pairing, and the one-pair \(2^k p\) regime already has a dedicated classification. The exact first point where this regime breaks is therefore a natural structural cutoff. The theorem both identifies that first transition and supplies a global exact reduction that can be reused for larger searches or further structure.

## Closest literature and limitations
The closest direct predecessor is Aryan--Madhavani--Parikh--Slattery--Zelinsky (2024), whose strong 2-near condition means exactly one complementary pair is omitted. Wang--Zelinsky (2026) supplies the current definition, early data, and the Mersenne-prime branch. The accepted theorem does not classify all \(2^a p\) cases in closed form, and its minimality statement is restricted to this two-prime-support, odd-prime-exponent-one slice.

Same-model review: passed. Independent audit: not yet performed.
