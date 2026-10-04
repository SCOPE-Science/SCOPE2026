# Exact ternary multiset deletion codes when three multiset elements survive
## Finding
For every integer \(n\ge 5\), let \(S_3(n,n-3)\) denote the largest size of a ternary length-\(n\) multiset code correcting \(n-3\) deletions. Then
\[
S_3(n,n-3)=\begin{cases}
4,&n\in\{5,6\},\\
3,&n\ge 7.
\end{cases}
\]
Thus the recent general certificate bound \(S_3(n,n-3)\le 6\), valid from \(n\ge5\), is not tight in the ternary case.

## Assumptions and scope
Represent a ternary multiset of cardinality \(n\) by a multiplicity vector \(x=(x_0,x_1,x_2)\in\mathbb Z_{\ge0}^3\) with \(x_0+x_1+x_2=n\). For two such vectors define the multiset-intersection size
\[
\iota(x,y)=\sum_{i=0}^2\min(x_i,y_i).
\]
Correcting \(n-3\) deletions is equivalent to requiring \(\iota(x,y)\le2\) for every two distinct codewords. The result concerns exactly the ternary alphabet and exactly the extremal regime in which the received multiset has cardinality three.

## Proof
For a composition \(x\), define its heavy-coordinate set
\[
H(x)=\{i\in\{0,1,2\}:x_i\ge3\}.
\]
If two codewords \(x\) and \(y\) had a common heavy coordinate \(i\), then \(\iota(x,y)\ge\min(x_i,y_i)\ge3\), contradicting the code condition. Hence the nonempty sets \(H(x)\) occurring in a code are pairwise disjoint subsets of a three-element set, so there are at most three codewords with nonempty heavy-coordinate set.

For \(n\ge7\), every composition of \(n\) into three nonnegative parts has a coordinate at least \(3\). Therefore every codeword has nonempty \(H(x)\), and the preceding disjointness argument gives \(|\mathcal C|\le3\). The three constant words \((n,0,0)\), \((0,n,0)\), and \((0,0,n)\) have pairwise intersection size zero, so equality holds.

For \(n=6\), the only composition with \(H(x)=\varnothing\) is \((2,2,2)\). Thus a code contains at most three words with nonempty heavy-coordinate set and at most this one additional heavy-free word, giving \(|\mathcal C|\le4\). Equality is attained by
\[
\{(6,0,0),(0,6,0),(0,0,6),(2,2,2)\}.
\]
Each constant word intersects \((2,2,2)\) in exactly two elements, and the constants are mutually disjoint.

For \(n=5\), the heavy-free compositions are exactly the three permutations of \((2,2,1)\). Any two distinct such permutations have intersection size four, so a valid code contains at most one heavy-free word. Again there are at most three codewords with nonempty heavy-coordinate set, hence \(|\mathcal C|\le4\). Equality is attained by
\[
\{(5,0,0),(0,5,0),(0,0,5),(2,2,1)\},
\]
whose pairwise intersection sizes are at most two. This proves the formula for every \(n\ge5\).

## Verification
The supplied `verify.py` independently enumerates all ternary multiplicity vectors at \(n=5\) and \(n=6\), checks the two four-word witnesses, and exhaustively verifies that no five-word family satisfies the pairwise intersection constraint at either length. It also checks the heavy-free classifications used at \(n=5\) and \(n=6\) and verifies the heavy-coordinate condition on a finite consistency range. These finite checks are supplementary: the proof above establishes the unbounded statement for all \(n\ge7\) by the pigeonhole and disjoint-heavy-coordinate argument.

## Relationship to prior work
Kreindel, Essayag, and Zabokritskiy study precisely this multiset deletion model. Their current preprint states that when \(t=n-3\), distinct codewords must have multiset intersection at most two, and proves the certificate bound
\[
S_q(n,n-3)\le q+\binom q2\qquad(n\ge q+2).
\]
For \(q=3\) this gives \(S_3(n,n-3)\le6\) for \(n\ge5\), whereas the result here gives the exact values \(4,4,3,3,\ldots\). The same paper's exact ternary benchmark section concerns one deletion rather than the growing-deletion regime \(t=n-3\).

The earlier framework of Kovačević and Tan identifies multiset codes with lattice-like codes in the discrete simplex and develops general constructions and bounds. Targeted searches under the deletion notation, discrete-simplex formulation, intersection formulation, and equivalent minimum-distance formulation did not locate this ternary exact piecewise formula. The closest indexed results concerned asymptotic sequence-deletion codes, traceability codes, and other unrelated finite coding problems, none implying this statement.

## Limitations
The theorem is specific to alphabet size three and received-multiset size three. It does not classify all extremal codes up to alphabet permutation, and it does not determine \(S_q(n,n-3)\) for \(q\ge4\). A residual originality risk is that the same elementary extremal fact could appear in older discrete-simplex or lattice-code literature under different notation; targeted searches for those equivalent formulations found no covering statement.

## References
1. Avraham Kreindel, Isaac Barouch Essayag, and Aryeh Lev Zabokritskiy (Yohananov), “Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results,” arXiv:2601.05636v2, 2026. First public version posted 2026-01-09.
2. Mladen Kovačević and Vincent Y. F. Tan, “Codes in the Space of Multisets—Coding for Permutation Channels with Impairments,” arXiv:1612.08837, 2016; later published in IEEE Transactions on Information Theory.
