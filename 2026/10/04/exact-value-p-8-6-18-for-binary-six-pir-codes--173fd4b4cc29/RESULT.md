# Exact value \(P(8,6)=18\) for binary six-PIR codes
## Finding
Let \(P(s,k)\) be the minimum block length of a binary linear \(k\)-PIR code storing \(s\) information bits. Then
\[
P(8,6)=18.
\]
The previously published bounds were \(17\le P(8,6)\le18\). The new lower bound excludes length \(17\); the published length-\(18\) construction supplies the matching upper bound.

## Assumptions and scope
A binary linear code with generator matrix \(G\in\mathbb F_2^{s\times n}\) is \(k\)-PIR when, for every information vector \(e_i\), there are \(k\) pairwise disjoint coordinate sets whose corresponding columns of \(G\) sum to \(e_i\). The argument concerns this standard linear PIR-code definition. It does not address nonlinear PIR encoders or recovery models with different disjointness requirements.

Kurz and Yaakobi proved that every binary \(k\)-PIR code has minimum Hamming distance at least \(k\), and their small-parameter table gives the bounds \(17\le P(8,6)\le18\). Therefore a hypothetical length-\(17\) example would have to be a binary linear \([17,8,6]\) code.

## Proof
The optimal binary \([17,8,6]\) code is unique up to equivalence. This is recorded in the complete classification of optimal binary dimension-eight codes; the unique class may be represented by the binary quadratic-residue code generated cyclically by
\[
g(x)=1+x+x^3+x^6+x^8+x^9.
\]
It is therefore enough to show that no choice of information basis makes this code six-PIR.

Let \(C\) be this \([17,8,6]\) code and let \(C^\perp\) be its dual. Direct enumeration of the \(512\) dual words gives
\[
d(C^\perp)=5,
\]
with exactly \(34\) dual words of weight \(5\). More sharply, every pair of coordinate positions is contained in either two or three of those weight-\(5\) supports; in particular, no pair lies in five such supports.

Suppose six pairwise disjoint recovery sets \(R_1,\ldots,R_6\) existed for one nonzero target vector under some generator basis. For \(i\ne j\), the indicator vector of \(R_i\triangle R_j\) lies in \(C^\perp\), because the two recovery sets have the same column sum. As the recovery sets are disjoint,
\[
|R_i|+|R_j|=|R_i\triangle R_j|\ge5.
\]
Their total size is at most \(17\). Sorting their six positive sizes, these inequalities force the unique pattern
\[
(2,3,3,3,3,3).
\]
Indeed, a smallest size \(1\) forces the other five sizes to be at least \(4\), while a smallest size at least \(3\) makes the total at least \(18\); hence the smallest size is \(2\), every other size is at least \(3\), and equality in the total bound forces the displayed pattern.

Let \(A\) be the size-\(2\) recovery set and \(B_1,\ldots,B_5\) the size-\(3\) sets. For every \(j\), the disjoint union \(A\cup B_j\) is the support of a weight-\(5\) word of \(C^\perp\). These five supports are distinct and all contain the same coordinate pair \(A\), contradicting the verified fact that a pair is contained in at most three weight-\(5\) dual supports. Thus the unique \([17,8,6]\) code cannot be six-PIR under any information basis.

Consequently \(P(8,6)\ge18\). Combining this with the published length-\(18\) construction yields \(P(8,6)=18\).

## Verification
The standalone verifier reconstructs the cyclic representative from \(g(x)\), checks rank \(8\), enumerates all \(256\) primal codewords and verifies minimum distance \(6\), enumerates all \(512\) dual codewords and verifies dual minimum distance \(5\), counts the \(34\) dual weight-\(5\) words, and checks all \(136\) coordinate pairs. Exactly \(68\) pairs occur in two weight-\(5\) supports and \(68\) pairs occur in three. It also exhausts the elementary six-size inequality and confirms that \((2,3,3,3,3,3)\) is the only possible size pattern.

The finite computation certifies the obstruction inside the unique length-\(17\) code class. The length-\(18\) upper bound is an inspected published construction/result rather than a computation reproduced here.

## Relationship to prior work
Kurz and Yaakobi introduced the notation \(P(s,k)\), state the minimum-distance lower bound, and list \(17\le P(8,6)\le18\) in their small-parameter table; their first public arXiv version is dated 2020-01-10. Thus the exact value was not supplied there.

Bouyukliev, Jaffe, and Vavrek determined the minimum lengths of binary dimension-eight codes with prescribed distance. A later complete enumeration of optimal binary codes by Bouyuklieva and Dzhumalieva-Stoeva records that the optimal \([17,8,6]\) code is unique up to equivalence. The present argument uses that classification to turn the PIR lower-bound question into a small dual-incidence obstruction.

Targeted searches for the exact parameter, six-PIR aliases, the \([17,8,6]\) code, quadratic-residue recovery sets, and coding-theoretic obstruction formulations did not reveal a prior statement of \(P(8,6)=18\). This is evidence of non-coverage, not a proof that no unindexed prior observation exists.

## Limitations
The exact conclusion depends on the published uniqueness classification of binary \([17,8,6]\) codes and on the previously published length-\(18\) PIR upper bound. The package independently verifies the representative code and the new lower-bound obstruction, but it does not re-enumerate all equivalence classes of binary \([17,8,6]\) codes or reproduce the authors' length-\(18\) construction. An unindexed or differently phrased prior derivation remains a residual originality risk.

## References
1. S. Kurz and E. Yaakobi, “PIR Codes with Short Block Length,” arXiv:2001.03433, first public version 2020-01-10; later Designs, Codes and Cryptography 89 (2021), 559–587.
2. I. Bouyukliev, D. B. Jaffe, and V. Vavrek, “The smallest length of eight-dimensional binary linear codes with prescribed minimum distance,” IEEE Transactions on Information Theory 46 (2000), 1539–1544, DOI 10.1109/18.850690.
3. S. Bouyuklieva and M. Dzhumalieva-Stoeva, “Optimal Linear Codes and Their Hulls,” Mathematics 13 (2025), 2491, DOI 10.3390/math13152491.
