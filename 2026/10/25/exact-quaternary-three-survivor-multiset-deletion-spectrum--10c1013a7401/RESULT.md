# Exact quaternary three-survivor multiset deletion spectrum

## Finding
For every integer \(n\ge5\), let \(S_4(n,n-3)\) be the maximum number of multisets of size \(n\) over four symbols such that any \(n-3\) deleted symbols can be uniquely corrected. Then
\[
\boxed{S_4(n,n-3)=\begin{cases}6,&n=5,\\5,&6\le n\le8,\\4,&n\ge9.\end{cases}}
\]
The entire spectrum is attained by explicit codes, and the exceptional six-word optimum at \(n=5\) is forced by a triangle-free compatibility structure among light multiplicity vectors. All lengths \(n\ge5\) are covered, not merely a finite checked range.

## Assumptions and scope
Fix the alphabet \(\Sigma=\{0,1,2,3\}\). A word is an **unordered** multiset represented by its multiplicity vector \(x=(x_0,x_1,x_2,x_3)\in\mathbb Z_{\ge0}^4\), with \(\sum_i x_i=n\). A deletion reduces one coordinate by one. Distinct codewords \(x,y\) possess a common possible output of length three if and only if their multiset intersection
\[
I(x,y)=\sum_{i=0}^3\min(x_i,y_i)
\]
is at least three. Consequently, correcting up to \(n-3\) deletions is **equivalent** to \(I(x,y)\le2\) for every pair of distinct codewords. The same equivalence holds for exactly \(n-3\) deletions, because a common longer output has a common three-element submultiset.

Call a vector *heavy* at index \(i\) when \(x_i\ge3\), and *light* when every coordinate is at most two. This is the four-symbol, three-survivor regime; the result does not concern ordered-string deletion shadows or a five-symbol alphabet.

## Proof
**1. Heavy-coordinate packing.** For any two admissible distinct codewords \(x,y\), the index sets \(H(x)=\{i:x_i\ge3\}\) and \(H(y)=\{i:y_i\ge3\}\) are disjoint: if they shared \(i\), then \(I(x,y)\ge3\). Since four coordinates are available, at most **four** codewords may have nonempty heavy-coordinate sets. Indeed, select one heavy coordinate from each such codeword; the selections must be distinct.

**2. The range \(n\ge9\).** A light vector has total size at most \(2+2+2+2=8\). Hence when \(n\ge9\) every codeword is heavy, and the preceding packing argument gives an upper bound four. The four constant multisets \(ne_0,ne_1,ne_2,ne_3\) have pairwise intersections zero and attain the bound.

**3. The range \(6\le n\le8\).** If \(x,y\) are light, then each coordinate is at most two. Using \(\min(a,b)\ge a+b-2\) for \(0\le a,b\le2\),
\[
I(x,y)\ge\sum_{i=0}^3(x_i+y_i-2)=2n-8\ge4.
\]
Thus no two light vectors can be simultaneous codewords; there are at most four heavy codewords and one light codeword, giving the bound five. It is attained by the four constant vectors and, respectively for \(n=6,7,8\), the additional light vectors \((2,2,1,1)\), \((2,2,2,1)\), \((2,2,2,2)\). The extra vector intersects each constant vector in at most two elements.

**4. The exceptional case \(n=5\).** Every light vector is a permutation of either \(A=(0,1,2,2)\) or \(B=(2,1,1,1)\). First, a vector of type \(B\) is incompatible with every other light vector. By permuting symbols take \(B=(2,1,1,1)\). For any other light vector \(y\), if \(y_0\ge1\), then at least two of \(y_1,y_2,y_3\) are positive (their sum is at least three, with each at most two), so \(I(B,y)\ge1+2=3\). If \(y_0=0\), the last three coordinates sum to five and all are positive, again giving \(I(B,y)\ge3\).

It therefore suffices, when considering two or more light codewords, to examine type \(A\). Fix one such vector as \(x=(0,1,2,2)\), using a symbol permutation. Suppose \(y\) is another light vector with \(I(x,y)\le2\). The condition reads \(\min(1,y_1)+y_2+y_3\le2\). Since \(y_0\le2\), \(y_0+y_1+y_2+y_3=5\), and all coordinates are at most two, this is possible only when \(y_0=y_1=2\) and \(y_2+y_3=1\). (If \(y_0\le1\), the remaining coordinates total at least four and the intersection is at least three; if \(y_0=2\) and \(y_1\le1\), it is also at least three.) Thus the **only** two compatible choices for \(y\) are \((2,2,0,1)\) and \((2,2,1,0)\). These two candidates intersect in four symbols and so cannot coexist. It follows that every valid family has at most two light codewords, and hence has size at most \(4+2=6\).

Finally, the six vectors
\[
\mathcal C_5=\{(5,0,0,0),(0,5,0,0),(0,0,5,0),(0,0,0,5),(0,1,2,2),(2,2,0,1)\}
\]
are pairwise compatible: constants are disjoint, each of the last two vectors meets any constant in at most two symbols, and the last two have intersection exactly two. Therefore six is attained. Together with the constructions in steps 2–3, this completes the proof for every \(n\ge5\).

## Verification
Run `python verify.py` (Python 3 standard library only) in the same folder. The checker enumerates all four-coordinate compositions for \(n=5,6,7,8,9\), counts light vectors and compatible pairs, tests the absence of a compatible light triple at \(n=5\), verifies the two exact neighbors of \((0,1,2,2)\), checks explicit optimal codes, and independently checks every possible three-symbol output against those codes for \(5\le n\le20\). Expected output is included in `verification_output.txt`. The infinite bounds are established by the symbolic arguments above, not by finite enumeration. Exhaustive light-pair counts are \(12,0,0,0,0\) at lengths \(5,6,7,8,9\).

## Relationship to prior work
Kreindel, Essayag, and Zabokritskiy [1] define the same unordered-multiset deletion code model and consider exactly the regime \(t=n-3\). Their Section 3.5 supplies a general Reiman-style upper-bound theorem (for \(n\ge q+2\)), and Section 3.6 provides recursive bounds; neither is the exact, all-\(n\ge5\), four-symbol staircase proved here. In particular, their Theorem 9 applies to \(q=4\) only when \(n\ge6\), whereas the present exceptional six-word case occurs at \(n=5\).

A published, explicit ternary result [4] proves \(S_3(n,n-3)=4\) at \(n=5,6\) and three thereafter; this does not imply the four-symbol spectrum. The quaternary case has a genuinely different light-vector geometry: two, rather than just one, light words may coexist at the first nontrivial length. The companion multiset study [2] concerns general constructions and deletion-ball geometry, and the earlier discrete-simplex/lattice framework [3] supplies general bounds rather than this exact specialization. Comparisons also covered the equivalent formulation as a constant-sum, nonnegative-integer \(\ell_1\)-packing with pairwise distance at least \(n-2\): on a fixed-sum simplex, half the \(\ell_1\) distance equals \(n-I(x,y)\).

## Limitations
This statement concerns precisely four symbols, output size three, and lengths \(n\ge5\); it does not determine maximum codes for other alphabet sizes or all parameters. The theorem determines optimal **cardinalities**, not the classification of every optimal code. Finite checker results corroborate, but do not certify, the unbounded symbolic theorem. A historical-priority risk remains that a pre-existing short-distance packing table or an unindexed discrete-simplex source may contain an equivalent extremal profile under different notation. No independent external scientific audit is claimed.

## References
1. A. Kreindel, I. B. Essayag, A. L. Zabokritskiy, “Multiset Deletion-Correcting Codes: Bounds and Constructions,” arXiv:2601.05636 (first public 2026-01-09), especially Sections 2 and 3.5–3.6. https://arxiv.org/abs/2601.05636
2. “Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes,” arXiv:2603.18322 (2026), https://arxiv.org/abs/2603.18322
3. M. Kovačević and V. Y. F. Tan, “Codes in the Space of Multisets—Coding for Permutation Channels with Impairments,” arXiv:1612.08837 (2016), https://arxiv.org/abs/1612.08837
4. “Exact ternary multiset deletion codes when three multiset elements survive,” 2026, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ternary-multiset-deletion-codes-when-three-multiset-elemen--d3a62a71c505
