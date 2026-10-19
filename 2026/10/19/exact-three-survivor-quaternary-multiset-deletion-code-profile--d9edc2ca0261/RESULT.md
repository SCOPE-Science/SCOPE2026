# Exact three-survivor quaternary multiset deletion-code profile

## Finding
For an alphabet of four symbols and every integer \(n\ge 5\), let \(S_4(n,n-3)\) be the maximum cardinality of a code of unordered multisets, each containing \(n\) symbols, that corrects up to \(n-3\) deletions. Then
\[
S_4(n,n-3)=
\begin{cases}
6,&n=5,\\
5,&6\le n\le8,\\
4,&n\ge9.
\end{cases}
\]
In particular, the four pure-symbol multisets first become optimal at \(n=9\). All bounds are attained by explicit codes given below.

## Assumptions and scope
An unordered multiset is its multiplicity vector \(x=(x_1,x_2,x_3,x_4)\) with nonnegative integer coordinates and \(\sum_{i=1}^4x_i=n\). A deletion subtracts one from a positive coordinate. All codewords have the same length \(n\), and the channel may delete any number of symbols not exceeding \(n-3\). Different transmitted multisets must never produce the same received multiset.

For two vectors define their intersection size
\[
I(x,y)=\sum_{i=1}^4\min\{x_i,y_i\}.
\]
They share a possible three-symbol output if and only if \(I(x,y)\ge3\). Thus the necessary and sufficient code condition is
\[
I(x,y)\le 2\quad\text{for every two distinct codewords }x,y.
\]
Indeed, any common output obtained using fewer deletions has size at least three, and therefore contains a common three-symbol submultiset; conversely a common three-symbol submultiset is obtained using exactly \(n-3\) deletions.

## Proof
Call a coordinate *heavy* when its value is at least three, and call a vector *light* if all four coordinates are at most two. In a valid code, no two different vectors can be heavy in the same coordinate: otherwise their intersection size is at least three. Assigning one heavy coordinate to each non-light codeword is consequently injective, so there are **at most four non-light codewords**.

If \(x,y\) are light and have coordinate sum \(n\), the identity
\[
I(x,y)=2n-\sum_{i=1}^4\max\{x_i,y_i\}
\]
and the inequalities \(\max\{x_i,y_i\}\le2\) give
\[
I(x,y)\ge 2n-8.
\]
For \(n\ge6\), two light vectors therefore have intersection at least four, and a valid code contains **at most one light vector**. If \(n\ge9\), there is no light vector at all because the sum of its coordinates would be at most eight. This proves the upper bounds five for \(6\le n\le8\) and four for \(n\ge9\).

It remains to handle \(n=5\). If two distinct light vectors \(x,y\) are compatible, then \(I(x,y)\le2\), so
\[
\sum_i\max\{x_i,y_i\}=10-I(x,y)\ge8.
\]
The left side is at most eight, hence it equals eight and every coordinatewise maximum equals two. A length-five light vector can contain at most two coordinates equal to two. Between \(x\) and \(y\), each of the four coordinates must equal two in at least one vector. Therefore each has exactly two coordinates equal to two, and their sets of such coordinates are complementary two-element sets. Any third light vector compatible with \(x\) would be forced to have its two coordinates equal to two on the complementary set, namely the two-coordinates of \(y\). Compatibility with \(y\) instead forces the complementary set of \(y\), a contradiction. Consequently there are at most two light codewords when \(n=5\), proving the upper bound six.

For the matching lower bounds, first take the four pure vectors \(ne_1,ne_2,ne_3,ne_4\), where \(e_i\) denotes the corresponding unit vector. Their pairwise intersections are zero. For \(n=5\), add
\[
(2,2,1,0)\quad\text{and}\quad(0,1,2,2).
\]
Their mutual intersection has size two, and each intersects every pure vector in at most two. For \(n=6,7,8\), respectively add just one of
\[
(2,2,1,1),\quad(2,2,2,1),\quad(2,2,2,2).
\]
Each has every coordinate at most two. For \(n\ge9\), use only the four pure vectors. These constructions meet all the corresponding upper bounds, proving the formula. \(\square\)

## Verification
Run `python check.py` using Python 3.9 or later. The script explicitly generates every nonnegative four-coordinate integer composition of each length \(5,6,7,8,9\), checks the displayed constructions against all pairwise overlaps, constructs the exact compatibility graph, and uses a greedy-coloring branch-and-bound algorithm to exclude cliques one larger than the claimed optimum. Its deterministic output is recorded in `check_output.txt`. The mathematical heavy/light proof establishes the infinite \(n\ge9\) range without reliance on computation.

## Relationship to prior work
Kreindel, Essayag, and Zabokritskiy (arXiv:2601.05636, initial public version January 9, 2026) formalize this model and prove general bounds for retaining three symbols, particularly in Section 3.5. Their examined statements do not provide the sharp four-symbol values for \(n\ge5\). Kovačević and Tan (arXiv:1612.08837) establish the general multiset-code geometry and deletion-distance equivalence; the investigated portions do not provide this parameter profile. The length-four single-deletion regime and the three-symbol alphabet have separate known results; neither is part of the novelty claim here.

The present statement is an exact determination of the *four-symbol, three-survivor* profile for every length at least five, including the sharp transition to the pure-symbol optimum. It is not a claim of a general formula for arbitrary alphabets in the short-length regime.

## Limitations
No classification of all maximum codes is asserted. The result does not determine the short-length profile for alphabets of five or more symbols, nor does it address ordered-string deletion codes. A complete survey of unpublished and unindexed literature has not been established. The proof is elementary and self-contained once the standard overlap characterization is specified; the auxiliary finite computation is a reproducibility check, not a substitute for the proof.

## References
1. A. Kreindel, I. B. Essayag, and A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636, first public January 9, 2026. https://arxiv.org/abs/2601.05636
2. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels With Impairments*, arXiv:1612.08837, first public December 28, 2016; IEEE Transactions on Information Theory 64 (2018), 5156–5169. https://arxiv.org/abs/1612.08837
