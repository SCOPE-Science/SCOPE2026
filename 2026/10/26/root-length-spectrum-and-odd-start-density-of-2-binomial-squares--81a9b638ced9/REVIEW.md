# Independent mathematical audit

## correctness

PASS

For equal-length binary factors, all scattered subsequence counts of length≤2 are determined by number K of ones and first weighted moment M=Σj w_j. For odd m=2h+1 an even start has odd total one-count, preventing equal halves; at odd i=2a+1, exact K and M equations force source factor 0^(h+1)1^(h+1) or complement, and the Thue–Morse fixed point has no 000/111, so h≤1. Explicit literal squares witness m=1,3. For even m=2h, substitution images of length-h source factors have equal 2-binomial signature precisely when source counts match; h even works at 0, h odd works at a=2(2^k−h)+1 using popcount(2^k−h)=k−popcount(h−1), with chosen parity k. Primitive substitution pair/triple factor-frequency equations give frequency 1/12 for the two m=3 source patterns and the odd-index factor. Independently tested exact compact signatures, all even roots 2..512, no odd roots 5..65 in the first 32768 letters, and 6000 odd start positions, observing 2730/32763 ≈1/12. The all-length result rests on the symbolic proof, not bounded sampling.

## originality

PASS

The established k-binomial-complexity literature concerns scattered subsequence classes, and abelian-square literature concerns a coarser repetition notion; neither inspected full result resolves consecutive factor equality and the precise even/odd spectrum. The claim makes a genuine new adjacency/position classification.

## value

PASS

Determining which 2-binomial repetition lengths actually occur in a canonical automatic word is a natural complete combinatorics-on-words classification, distinct from class complexity and ordinary/abelian squares. The sharp parity split, constructive all-even witnesses, and exact odd-root location density provide structural information reusable in binomial-repetition research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
