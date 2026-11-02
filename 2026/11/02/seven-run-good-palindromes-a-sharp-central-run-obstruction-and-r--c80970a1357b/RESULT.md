# Seven-run good palindromes: a sharp central-run obstruction and rational enumeration

## Finding

A binary word is **good** when it contains no contiguous factor of the form \(u\overline u\), where \(|u|\ge2\) and \(\overline u\) is obtained by interchanging zero and one. For all positive integers \(a,b,c,d\), consider the palindrome
\[
 W=0^a1^b0^c1^d0^c1^b0^a.
\]
It is good if and only if one of these **disjoint** conditions holds:

1. \(a=c=1,\ b\ge3,\ d\in\{1\}\cup\{3,4,\ldots\}\).
2. \(b=d=1,\ c\ge3,\ a\ge1\).
3. \(b=c=1,\ a\ge1,\ d>2a\).

For the number \(A_n\) of all good binary palindromes of length \(n\) having exactly seven maximal runs, including both binary complements, the **complete length generating function** is
\[
\sum_{n\ge0} A_n z^n
=2\left(\frac{z^{10}}{1-z^2}\left(z+\frac{z^3}{1-z}\right)
+\frac{z^{11}}{(1-z^2)^2}
+\frac{z^9}{(1-z)(1-z^4)}\right).
\]
Its first nonzero values, at lengths \(9,10,\ldots,21\), are \(2,2,6,2,12,6,16,8,22,12,26,14,32\). At the shortest length \(9\), the two words are \(010111010\) and its complement.

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\). A **run** means a maximal contiguous constant block; all four integer parameters are positive, ensuring exactly seven runs. Factors are linear, not circular or scattered. Antisquares of order one (the factors \(01\) and \(10\)) are allowed; those of every order at least two are forbidden. The enumeration counts separate binary complements and does not quotient by rotation or reversal. The infinite-parameter theorem does not claim a classification of all good palindromes with more than seven runs.

## Proof

**1. Short obstructions.** The four order-two antisquares are \(0011,1100,0110,1001\). The first two occur if and only if adjacent runs have lengths at least two; thus in the run-length sequence \((a,b,c,d,c,b,a)\) we require
\[
\min(a,b)=\min(b,c)=\min(c,d)=1.
\]
The latter two order-two antisquares occur if and only if some *interior* run has length exactly two, so \(b,c,d\ne2\). The order-three minimal antisquares are \(010101\) and \(101010\). Under these order-two restrictions, a six-symbol alternating factor occurs exactly when \(b=c=d=1\), because all other admissible cases have a long central or neighboring interior run. Therefore \(b=c=d=1\) is excluded.

**2. Exhaustive run split.** Subject to those short restrictions, there are three possible configurations: \(b\ge3\), which forces \(a=c=1\); \(c\ge3\), which forces \(b=d=1\); or \(b=c=1\), where \(d\ne2\) and the excluded alternating case removes \(d=1\). These three configurations are pairwise disjoint.

**3. All longer obstructions.** The published classification of *minimal antisquares* [1, Theorem 11] states that, beyond orders two and three, the minimal forbidden factors are exactly the cyclic rotations of
\[
R_k=0^k101^k01,\qquad k\ge3.
\]
Every forbidden antisquare contains a minimal one. A rotation of \(R_k\) has one long block of zeros and one long block of ones, each of length \(k\); only a block cut by the rotation's endpoints may split into two end pieces. In configuration 1, all zero-runs have length one; no rotated \(R_k\) fits, since at least one zero block in such a rotation has length at least two. In configuration 2, the same argument applies to one-runs. In configuration 3, the only one-run of length at least two is the central block \(1^d\). A rotated \(R_k\) fitting inside \(W\) must therefore use this whole central block as its unsplit long one-run: \(k=d\), while the long zero-run of total length \(d\) is split, possibly with an empty end, between the two outer zero-runs. Such an occurrence exists if and only if the two end-runs can provide a combined \(d\) zeros, or \(d\le2a\). Explicitly, choose an integer \(t\) with \(0\le t\le a\) and \(0\le d-t\le a\) and take the factor \(0^t101^d010^{d-t}\), a cyclic rotation of \(R_d\). Thus goodness in configuration 3 is equivalent to the sharp strict inequality \(d>2a\). This proves the classification, including all orders without a finite-enumeration assumption.

**4. Generating function.** Every seven-run palindrome has a unique maximal-run parameter tuple, and swapping zero and one gives a distinct word of the same length. In configuration 1, the length is \(2b+d+4\); summing over \(b\ge3\) and \(d\in\{1\}\cup[3,\infty)\) gives \(z^{10}(z+z^3/(1-z))/(1-z^2)\). In configuration 2, length \(2a+2c+3\) with \(a\ge1,c\ge3\) gives \(z^{11}/(1-z^2)^2\). In configuration 3, length \(2a+d+4\) with \(a\ge1,d\ge2a+1\) gives \(z^9/((1-z)(1-z^4))\). Summing and multiplying by two gives the claimed rational function.

## Verification

The standalone script `verify.py`, included alongside this note, tests the analytic criterion independently against literal full-length antisquare enumeration for all \(9^4=6561\) parameter quadruples with \(1\le a,b,c,d\le9\). It also exhaustively enumerates **all** binary palindromes of each length \(1\le n\le26\), retains those with exactly seven runs, and checks their literal avoidance status against the closed-form length count. Coefficients from the three structural families were compared for lengths \(1\le n\le60\). The recorded program output is `VERIFY_OK quadruples=6561 full_palindrome_lengths=26 coefficient_lengths=60`. These finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Baranwal, Currie, Mol, Ochem, Rampersad and Shallit [1] determine **all** minimal binary antisquares (their Theorem 11) and derive the unrestricted growth exponent of good words. This result explicitly uses that general forbidden-factor theorem, but solves a different exact symmetry-restricted enumeration problem: the first palindromic run stratum where a long minimal obstruction can occur, with a new strict central-length versus doubled boundary-length condition and a rational enumerator. Ng, Ochem, Rampersad and Shallit [2] study simultaneous square/antisquare avoidance bounds and do not present this palindromic parameter classification in the material examined. Neither paper's stated general theorems give the displayed three-family length count without additional run-position and generating-function analysis.

## Limitations

This is not a new classification of minimal antisquares; that nonstandard ingredient is imported from [1]. The source theorem gives an algorithmic forbidden-pattern description for arbitrary binary words and is therefore closely related; the claimed contribution is the explicit sharp seven-run palindrome specialization and its full enumeration. No classification beyond seven runs, asymptotic for all good palindromes, or independent audit is asserted. The literature comparison cannot eliminate an unlocated equivalent specialization.

## References

[1] A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223, first posted 2022-09-19; Discrete Mathematics & Theoretical Computer Science 25:2 (2023), Theorem 11 and Section 7. https://arxiv.org/abs/2209.09223

[2] T. Ng, P. Ochem, N. Rampersad, J. Shallit, *New Results on Pseudosquare Avoidance*, arXiv:1904.09157, first posted 2019-04-19, Section 2. https://arxiv.org/abs/1904.09157
