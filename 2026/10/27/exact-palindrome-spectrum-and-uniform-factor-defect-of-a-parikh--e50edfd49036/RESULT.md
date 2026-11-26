# Sharp palindrome saturation threshold for a Parikh-collinear fixed point

## Finding

Let \(f(0)=010011\), \(f(1)=1001\), and let \(w=f^\omega(0)\). The least length \(L\) such that every contiguous factor of \(w\) of length at least \(L\) contains every palindromic factor of \(w\) is **172**. Equivalently, for the palindromic defect \(D(v)=|v|+1-|\operatorname{Pal}(v)|\), with the empty word included in \(\operatorname{Pal}(v)\),
\[
D(v)=|v|-37\qquad (|v|\ge 172).
\]
The equality fails for a factor of length 171: the factor starting at zero-based offset 325 in \(f^4(00)\) does not contain `01100101001110010100110`.

## Assumptions and scope

The alphabet is \(\{0,1\}\). Factors are contiguous and counted by distinct word value, not by occurrence. The fixed point is one-sided. The threshold is for this particular morphism only and concerns **every** factor of the specified length, not only prefixes or factors starting at substituted block boundaries.

## Proof

Every binary bigram appears in the prefix \(f(0)\) (including `00` at offset 2). Since \(w=f^k(w)\), every \(f^k(ab)\) for a binary bigram \(ab\) occurs in \(w\). Conversely, for any \(n\le\min(|f^k(0)|,|f^k(1)|)\), a length-\(n\) window meets at most two consecutive level-\(k\) blocks: to meet three it would have to contain the entire middle block and an extra symbol on both sides. Therefore, with both sides denoting sets of distinct factors,
\[
 \operatorname{Fac}_n(w)=\bigcup_{a,b\in\{0,1\}}\operatorname{Fac}_n(f^k(ab)).
\]

For \(k=3\) the two letter-block lengths are 150 and 100. Use the identity through length 25 and compare each factor with its reversal. The respective palindrome counts are 3 at lengths 3 and 13, 1 at length 12, 2 at lengths \(1,2,4,5,6,7,8,9,10,11,15,17,19,21,23\), and 0 at the remaining lengths through 25. In particular, a longer palindrome would have a palindromic center of length 24 or 25, which is impossible. This reproduces the known complete catalogue of 37 distinct nonempty palindromes and verifies that `01100101001110010100110` belongs to it.

For \(k=4\) the two letter-block lengths are 750 and 500. The identity now includes length 172. Enumerate the 1,329, 1,079, 1,079 and 829 starts, respectively, of 172-letter windows in \(f^4(00),f^4(01),f^4(10),f^4(11)\). For each palindrome \(p\) of the known catalogue and each start \(j\), take the first occurrence of \(p\) at a position \(i\ge j\) in the corresponding pair word. In all 4,316 windows and for all 37 palindromes, this occurrence exists and \(i+|p|\le j+172\). The exact finite test is given in `verify.py`. By the factor identity, these comparisons prove saturation at length 172, and every longer factor contains a length-172 window. The explicit 171-letter witness in the Finding fails the test for the stated length-23 palindrome. Since it occurs in \(w\), no threshold of 171 or less works. The defect formula follows by adding the empty palindrome to the 37 nonempty ones.

## Verification

Run `python3 verify.py` in the directory containing this file. It reconstructs the known catalogue directly from the four level-three pair words (no stored catalogue is required), checks all 159,692 palindrome–window comparisons at length 172, and verifies the length-171 counterexample by substring search. The finite factor identity above is the reason this computation applies to the entire infinite word.

## Relationship to prior work and limitations

Rigo, Stipulanti and Whiteland introduced this example in their study of automaticity and abelian complexity. The [complete palindrome catalogue](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-complete-palindromic-factor-language-of-an-aperiodic-parikh-coll--8966df486b3f/RESULT.md) already gives the spectrum and the level-three factor reduction; neither is claimed as a contribution here. A coarse saturation bound also follows readily from that certificate: both level-three letter words contain all 37 palindromes, so a factor of length at least 299 contains a full such block. The exact threshold requires occurrence information: the factor language describes which palindromes occur, not how long an interval can omit one. The sharp bound determines exactly the onset of the uniform defect identity. It does not describe the defect of every shorter factor or establish thresholds for other morphisms.

## Reference

M. Rigo, M. Stipulanti and M. A. Whiteland, *Automaticity and Parikh-collinear Morphisms*, WORDS 2023, LNCS 13899, 247–260, https://orbi.uliege.be/handle/2268/302523.
