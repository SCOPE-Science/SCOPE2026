# The first gap in binary Parikh-matrix subsequence-universality spectra

## Finding
Fix the binary alphabet \(\Sigma=\{a,b\}\). For integers \(A,B\ge0\) and \(0\le C\le AB\), let \(\mathcal P(A,B,C)\) be the words having precisely \(A\) letters \(a\), precisely \(B\) letters \(b\), and precisely \(C\) scattered occurrences of \(ab\). These are the fibers of the binary Parikh matrix (equivalently the binary subsequence-count deck through length two). Every such fiber is nonempty. Let \(\iota(w)\) be the greatest \(k\ge0\) for which every length-\(k\) binary word is a scattered subsequence of \(w\), and define its attainable spectrum by
\[
\mathcal S(A,B,C)=\{\iota(w):w\in\mathcal P(A,B,C)\}.
\]

**Theorem (sharp first noninterval fiber).** For every \(A+B\le7\), the spectrum \(\mathcal S(A,B,C)\) is an integer interval. For \(A+B=8\), the unique noninterval fiber is
\[
(A,B,C)=(4,4,8),\qquad \mathcal S(4,4,8)=\{2,4\}.
\]
It comprises exactly eight words: six have index \(4\), two have index \(2\), and none has index \(3\). Thus length eight is the least possible length at which an entire intermediate subsequence-universality index can be missing between the minimum and maximum within one binary Parikh-matrix class.

## Assumptions and scope
Subsequence occurrences respect increasing positions and need not be contiguous. The ambient alphabet remains \(\{a,b\}\), even for unary source words. The statement concerns **every** nonempty binary Parikh-matrix fiber with total length at most eight; it does not assert a description of all spectra at greater lengths. The condition \(0\le C\le AB\) is necessary and sufficient for existence, by arranging the two letters in reverse order and swapping adjacent unlike letters one at a time.

An *arch* is the shortest prefix containing both alphabet symbols, deleted greedily and repeatedly; the residual suffix contains at most one distinct symbol. The number of arches equals \(\iota(w)\): each arch contributes a selectable occurrence of either symbol to every length-\(k\) subsequence, while choosing the opposite of the unique symbol absent from each remaining part constructs an absent subsequence of length one greater than the arch count. This standard arch characterization is also verified directly, independently of that fact, by the checker below.

## Proof
**1. No gaps when index four is impossible.** Every arch contains at least two letters, so \(2\iota(w)\le A+B\). If some member of a fixed fiber has index at least \(2\), then the four patterns \(aa,ab,ba,bb\) all occur in that member. Consequently \(A,B\ge2\), \(0<C<AB\), since \(ab\) and \(ba\) partition the \(AB\) cross-letter pairs. Conversely, these three inequalities guarantee that **every** member contains all four length-two patterns, hence every member has index at least \(2\). Therefore no nonempty fixed fiber whose maximum index is at most \(3\) can have a gap: the attainable indices lie in \(\{0,1,2,3\}\), and a maximum of at least two forces the minimum to be at least two. If its maximum is at most one, only one index can occur because \(A=0\) or \(B=0\) forces zero and \(A,B>0\) forces at least one. In particular all fibers with \(A+B\le7\) have interval spectra.

**2. Reduction at length eight.** If a length-eight word has index \(4\), its four arches must each have exactly length two and exhaust the word. Thus it has exactly four copies of each symbol and is a concatenation of four blocks, each either `ab` or `ba`. For a pair of distinct blocks, the first block contributes exactly one scattered \(ab\) pair with the second. The six inter-block pairs therefore contribute \(\binom42=6\); every `ab` block contributes one further pair. Writing \(t\) for the number of `ab` blocks,
\[
A=B=4,\qquad C=6+t,\qquad 0\le t\le4.
\]
These five fibers all have index-four representatives. In each, all members have index at least \(2\), since \(0<C<16\). No other length-eight fiber can have a noninterval spectrum by Step 1.

**3. Four neighboring fibers have intermediate representatives.** The following words each have \(A=B=4\), the indicated \(C\), and exactly three greedy arches:

| \(C\) | Witness with \(\iota=3\) |
|---:|---|
| 6 | `abbabbaa` |
| 7 | `ababbbaa` |
| 9 | `aabbbaba` |
| 10 | `aabbabba` |

Since these fibers also contain index-four words and no index is below two, each has an interval spectrum (whether or not index two itself is attained).

**4. Exact exceptional fiber.** Every word with four `a` letters has a unique decomposition
\[
w=b^{x_0}a b^{x_1}a b^{x_2}a b^{x_3}a b^{x_4},\qquad x_j\ge0.
\]
Its four `b` letters and eight scattered `ab` occurrences mean
\[
\sum_{j=0}^4 x_j=4,\qquad \sum_{j=0}^4 jx_j=8.
\]
These equations have exactly the following eight solutions, shown together with their words and arch counts:

| \((x_0,x_1,x_2,x_3,x_4)\) | Word | \(\iota\) |
|---|---|---:|
| \((0,0,4,0,0)\) | `aabbbbaa` | 2 |
| \((0,1,2,1,0)\) | `ababbaba` | 4 |
| \((0,2,0,2,0)\) | `abbaabba` | 4 |
| \((0,2,1,0,1)\) | `abbabaab` | 4 |
| \((1,0,1,2,0)\) | `baababba` | 4 |
| \((1,0,2,0,1)\) | `baabbaab` | 4 |
| \((1,1,0,1,1)\) | `babaabab` | 4 |
| \((2,0,0,0,2)\) | `bbaaaabb` | 2 |

For completeness, the exhaustion is a tiny integer-partition argument, not an appeal to unchecked sampling: the \(x_j\) encode a partition of eight fitting inside a \(4\)-by-\(4\) rectangle. Its possible weakly decreasing positive part lists are \((4,4)\), \((4,3,1)\), \((4,2,2)\), \((4,2,1,1)\), \((3,3,2)\), \((3,3,1,1)\), \((3,2,2,1)\), \((2,2,2,2)\). These are exhaustive: split by the largest part (four, three, or two), list the remaining parts summing to eight with at most four parts and bound four. Each list corresponds to one listed tuple.

Alternatively, six index-four words arise by choosing exactly two of the four blocks to be `ab`, giving \(\binom42=6\), and the remaining two words visibly have two arches: `aabbbbaa` has arch decomposition `aab` / `bbba` / `a`? This segmentation is not claimed as a greedy decomposition; the greedy algorithm directly yields index two. In detail, it extracts `aab` then `bbba`, leaving `a`, while `bbaaaabb` extracts `bba` then `aaab`, leaving `b`. Thus the spectrum is exactly \(\{2,4\}\) and the first-gap classification follows.

## Verification
The standalone `verify.py` enumerates every word of lengths \(0\) through \(8\), computes the Parikh-matrix parameters, and independently calculates the index (i) by testing all length-\(k\) binary patterns for scattered-subsequence occurrence and (ii) by greedy arch extraction. It checks their agreement on all \(511\) words and groups them into all \(255\) distinct realized \((n,A,B,C)\) fibers. The **only** noninterval fiber is \((8,4,4,8)\), with spectrum \(\{2,4\}\). It independently counts partitions in a bounding rectangle, enumerates the eight exceptional words, and verifies all four index-three witnesses above. The included `verification_output.txt` is the recorded stdout. The computation checks finite claims, while Steps 1–4 above provide the mathematical proof of completeness.

## Relationship to prior work
Fazekas, Huang, and Mercaş (arXiv:2610.06717v1; first public 2026-10-05) characterize existential and universal subsequence universality for classes specified by \(A,B,C\). Their endpoint questions determine whether a class contains any \(k\)-universal word and whether all its words are \(k\)-universal. The new assertion asks a distinct, finer question: **which exact indices occur between these endpoints?** In particular, the endpoints two and four do not imply that three is absent. The first-hole and unique-minimal-fiber classification is therefore not a corollary of endpoint bounds alone.

Richomme (arXiv:2510.07159v1) describes binary binomial-equivalence classes through partitions; that correspondence underlies the short exhaustive argument above, but neither an arch-index spectrum nor the sharp first noninterval class is stated in the examined text. A published finite-length binary universality generating function counts words aggregated across all Parikh-matrix fibers; taking its marginals cannot determine a conditional gap at fixed \(A,B,C\). Earlier counts for avoidance of individual scattered patterns are not, without additional argument, complete spectra of all binary subsequences. These relationships limit the novelty claim to the *joint*, fiber-specific spectrum and first obstruction.

## Limitations
Only the first possible gap and its uniqueness through length eight are determined; there is no asserted formula for the entire spectrum at every larger length. The exhaustive checker is corroborating evidence, not a replacement for the structural completeness proof. Full literature comparison substantially reduces but cannot eliminate the risk of a differently formulated or unindexed prior example or theorem; no independent scientific audit is claimed here.

## References
1. Szilárd Zsolt Fazekas, Xinhao Huang, Robert Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717v1, first posted 2026-10-05. https://arxiv.org/abs/2610.06717
2. Gwenaël Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159v1, first posted 2025-10-08. https://arxiv.org/abs/2510.07159
3. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, 2023, DOI:10.4230/LIPIcs.ISAAC.2023.4.
4. *Closed-form law for binary subsequence universality*, published mathematical research record (2026-10-04), public title as given, 2026-10-04.
