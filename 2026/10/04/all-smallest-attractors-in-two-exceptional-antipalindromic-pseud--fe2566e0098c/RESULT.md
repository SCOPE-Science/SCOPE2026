# All smallest attractors in two exceptional antipalindromic pseudostandard families
## Finding
Let \(E\) be the binary antimorphism that reverses a word and complements each bit. Starting from the empty word, let \(P(\delta_1\cdots\delta_n)\) be obtained by successively appending \(\delta_k\) and taking the shortest \(E\)-palindromic closure. For every integer \(n\ge 3\), define
\[
A_n=P(0^n)=(01)^n,
\qquad
B_n=P(01^{n-1})=0(1100)^{n-1}1.
\]
Positions are indexed from \(0\).

The smallest string attractors of \(A_n\) are exactly the pairs \(\{i,j\}\) satisfying
\[
0\le i<j\le 2n-1,
\qquad i\not\equiv j\pmod 2,
\qquad \{i,j\}\ne\{0,2n-1\}.
\]
Consequently \(A_n\) has exactly \(n^2-1\) smallest attractors.

The smallest string attractors of \(B_n\) are exactly the pairs \(\{i,j\}\) satisfying
\[
1\le i<j\le 4n-4,
\qquad j-i\equiv 2\pmod 4,
\]
except for \(\{1,4n-5\}\) and \(\{2,4n-4\}\). Consequently \(B_n\) has exactly \(2n(n-2)\) smallest attractors.

## Assumptions and scope
A string attractor of a finite word is a set of positions such that every nonempty factor has at least one occurrence whose interval contains an attractor position. The finding concerns the two finite binary directive families \(0^n\) and \(01^{n-1}\), the two families governing the exceptional cases in Theorem 8 of Dvořáková--Hendrychová for antipalindromic prefixes of generalized pseudostandard words. It classifies every minimum attractor, not only the minimum cardinality.

The theorem is stated for \(n\ge3\). At the small boundary \(n=2\), the first formula still gives three minimum attractors for \(A_2=0101\), whereas \(B_2=011001\) has the two minimum attractors \(\{1,3\}\) and \(\{2,4\}\); the displayed formula \(2n(n-2)\) is therefore intentionally not asserted there.

## Proof
For the directive \(0^n\), after the first step the closure is \(01\). If \(A_k=(01)^k\), appending \(0\) and then one forced complementary symbol \(1\) gives the shortest antipalindrome, so \(A_{k+1}=(01)^{k+1}\).

For the directive \(01^{n-1}\), one obtains \(B_2=011001\). If \(B_k=0(1100)^{k-1}1\), appending the next directive symbol \(1\) creates a prefix ending in \(11\). An antipalindrome has even length. A one-symbol completion is impossible: the first/last complementary condition would force the new last symbol to be \(1\), after which the second and penultimate symbols would both be \(1\), contradicting antipalindromic symmetry. Appending the forced suffix \(001\) after that directive symbol yields
\[
B_{k+1}=B_k1001=0(1100)^k1,
\]
which is antipalindromic, so it is the shortest closure.

For \(A_n\), any attractor must meet occurrences of the one-letter factors \(0\) and \(1\); hence a two-position attractor must use opposite parities. Every factor of length at least two has all occurrences starting in one parity class, with successive starts two positions apart. Since the occurrence intervals have length at least two, their union is an interval. The factor \(10\) has occurrence union \([1,2n-2]\), so the opposite-parity endpoint pair \(\{0,2n-1\}\) fails. Conversely, for every other opposite-parity pair, no factor occurrence union can avoid both selected positions: the only way the complement of such an interval could contain an opposite-parity pair at both ends is the excluded endpoint pair. Thus the stated criterion is exact. There are \(n^2\) opposite-parity pairs, so removing one gives \(n^2-1\).

Now write \(N=4n-2\) for \(B_n\). It is the length-\(N\) prefix of the period-four word \((0110)^{\infty}\). Its length-two factors are \(00,01,10,11\). The occurrence intervals of \(00\) and \(11\) are disjoint and lie in the interior positions \(1,\ldots,N-2\), so a two-position attractor must use two interior positions. For an interior position, the length-two factors whose occurrence intervals contain it are determined by its residue modulo four:
\[
0:\{00,01\},\quad
1:\{01,11\},\quad
2:\{11,10\},\quad
3:\{10,00\}.
\]
Thus two interior positions hit all four length-two factors exactly when their residues are opposite, equivalently when their difference is \(2\) modulo \(4\).

Among such opposite-residue pairs, the factor \(0011\) has occurrence intervals whose union is exactly \([3,N-4]\). The only opposite-residue pairs lying wholly outside this interval are
\[
\{1,N-3\}=\{1,4n-5\},
\qquad
\{2,N-2\}=\{2,4n-4\},
\]
so these two pairs fail.

It remains to prove that every other candidate succeeds. One-letter and two-letter factors are already covered. For length-three factors, a direct residue check in the period-four word suffices: the uncovered interior positions for \(001\) have residues only \(2\), apart from the initial positions \(1,2\); for \(011\) they have residues only \(3\), apart from the terminal position \(N-2\); and for \(100\) and \(110\) they occupy only one residue class. No opposite-residue pair is contained in any of these uncovered sets. For every factor of length at least four, all its occurrences start in a single residue class modulo four. Successive starts are four apart, so their intervals overlap or abut; the first start is at most \(3\), and the final occurrence ends at least at \(N-4\). Hence its occurrence union contains \([3,N-4]\). Every candidate except the two excluded pairs meets that central interval, proving sufficiency.

Finally, both \(A_n\) and \(B_n\) contain both binary symbols, so no singleton can hit occurrences of both one-letter factors. The classified pairs therefore are smallest attractors. In \(B_n\), each residue class occurs \(n-1\) times among the interior positions. Opposite residue classes contribute \(2(n-1)^2\) pairs; deleting the two failures gives
\[
2(n-1)^2-2=2n(n-2).
\]

## Verification
The bundled `verify.py` reconstructs the generalized pseudostandard prefixes from the antipalindromic-closure definition and independently enumerates every distinct factor and its complete occurrence-position mask. It then enumerates all position pairs and tests the string-attractor definition directly.

For \(2\le n\le14\), it compares this brute-force result with the claimed closed-form pair descriptions while simultaneously checking the closure identities. It then stress-tests the closed-form words independently through \(n=40\). It also verifies that no singleton is an attractor. The recorded run terminates with `VERIFY_OK A_n=2..40 B_n=2..40 exact_pair_classification`.

The computation is corroboration, not a replacement for the all-\(n\) proof above.

## Relationship to prior work
Dvořáková and Hendrychová define string attractors for generalized pseudostandard/Rote sequences and prove, in their Theorem 8, sharp conditions governing the canonical attractor for nonempty antipalindromic prefixes. In particular, the directive prefixes \(0^n\) and \(01^{n-1}\) are exactly the two boundary patterns relevant to the size-two exceptional behavior considered here. Their theorem supplies minimum-size/canonical-attractor information but does not enumerate every minimum position pair for these two families or give the multiplicities \(n^2-1\) and \(2n(n-2)\).

A later study by Banbara et al. completely characterizes smallest attractors for Fibonacci and period-doubling words and emphasizes that the number of distinct smallest attractors can be a finer descriptor even when minimum size agrees. That work concerns different word families. OEIS A339668 counts binary words of each length whose minimum attractor size is two; it does not count all minimum attractor position sets of an individual word.

Targeted searches for the exact pair criteria, the two polynomial multiplicities, periodic-word aliases, pseudostandard aliases, and broader all-smallest-attractor classifications found no inspected statement implying this result. This absence is evidence of the search performed, not a proof of novelty.

## Limitations
The theorem classifies only the two stated antipalindromic directive families; it does not classify all generalized pseudostandard prefixes, all Rote factors, or all binary words with minimum attractor size two. It does not claim a new minimum-cardinality bound for these families; its contribution is the complete set and exact multiplicity of smallest attractors.

The originality comparison cannot exclude an unindexed thesis, unpublished computation, or differently phrased prior enumeration. The finite verifier does not establish the universal quantifier without the written residue/interval proof.

## References
1. L. Dvořáková and V. Hendrychová, “String attractors of Rote sequences,” arXiv:2308.00850v1, first public version 2023-08-01.
2. M. Banbara et al., “The Smallest String Attractors of Fibonacci and Period-Doubling Words,” CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.33.
3. OEIS A339668, “Number of binary strings of length n having minimum string-attractor size 2.”
