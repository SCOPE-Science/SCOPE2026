# Sharp component-sensitive sorting-supersequence bounds at ply two

## Finding

Let \(\mathcal I\) be any family of \(n\ge 1\) distinctly labelled, nonempty bounded open intervals on the real line, with pairwise distinct endpoints and ply at most two. Let \(c\) be the number of connected components of the graph joining intersecting intervals. There exists a word in the interval labels of length at most
\[
2n-c
\]
that contains as a scattered subsequence the labels sorted by their realized points for **every** choice of one point in each interval, with distinct realized coordinates. This worst-case bound is **sharp for every pair of integers** \(1\le c\le n\): some such interval family requires at least \(2n-c\) letters in every sorting-supersequence.

More generally, let \(P\) be a finite poset of width at most two, with \(n\) elements and \(i(P)\) unordered incomparable pairs. A word of length precisely \(n+i(P)\) can be constructed that contains **every** linear extension of \(P\) as a scattered subsequence. This is a constructive universal upper bound, not a claim of shortest possible length for each individual poset.

## Assumptions and scope

A sorting-supersequence of \(\mathcal I\) is a finite word on the distinct interval labels that contains the increasing order of the realized labels as a subsequence for every strict realization. The *ply* is the largest number of intervals covering one point. The intersection graph has one vertex per interval and an edge for each intersecting pair. A subsequence may omit letters but may not reorder those retained. The poset \(P\) of an interval family orders \(I\prec J\) when the right endpoint of \(I\) is strictly left of the left endpoint of \(J\). Distinct endpoints avoid tangency and endpoint ties; strict realizations are obtained by choosing pairwise distinct points.

The component-sensitive theorem includes disconnected families and isolated intervals. It does not assume unit-length intervals. No statement of optimality for each individual input family is made.

## Proof

**1. Two-chain slot construction.** By the width-two chain decomposition theorem, partition a finite poset \(P\) into two chains
\[
A=(a_1\prec\cdots\prec a_r),\qquad B=(b_1\prec\cdots\prec b_s).
\]
Either chain is allowed to be empty. For each \(a\in A\), define
\[
\ell(a)=\#\{b\in B:b\prec a\},\qquad
u(a)=s-\#\{b\in B:a\prec b\}.
\]
Because \(B\) is a chain, its elements preceding \(a\) form an initial segment and those succeeding \(a\) form a terminal segment. Thus \(0\le\ell(a)\le u(a)\le s\), and the elements incomparable with \(a\) are exactly those strictly after position \(\ell(a)\) and up through position \(u(a)\) in \(B\). In particular, their number is \(u(a)-\ell(a)\).

For slots \(j=0,1,\ldots,s\), write down, in increasing \(A\)-chain order, all \(a\in A\) with \(\ell(a)\le j\le u(a)\), and then append \(b_{j+1}\) when \(j<s\). Call the resulting word \(W\). Every linear extension of \(P\) lists \(B\) in chain order. An occurrence of \(a\in A\) within such an extension has exactly \(j\) elements of \(B\) before it, where \(\ell(a)\le j\le u(a)\). For each slot select that occurrence of \(a\) from \(W\); within a given slot, the selected \(A\)-letters occur in their prescribed chain order. Retaining all \(B\)-letters embeds the complete extension in \(W\). The word length is exactly
\[
|W|=s+\sum_{a\in A}(u(a)-\ell(a)+1)=n+i(P),
\]
because all incomparable pairs cross the two chains.

**2. The interval intersection graph is a forest.** Intervals have the Helly property: if three intervals pairwise intersect, all three meet at one point. Ply at most two therefore forbids triangles. There is also no induced cycle of length at least four. Indeed, choose an interval \(I\) in any proposed induced cycle whose right endpoint is least; each of its two cycle neighbors has its left endpoint before the right endpoint of \(I\) and its own right endpoint after that endpoint. The two neighbors consequently intersect one another, giving a forbidden chord. Hence the graph is acyclic. If its vertex count is \(n\) and its component count is \(c\), its edge count is \(n-c\).

Intervals in a pairwise nonintersecting color class form a chain in left-to-right order under \(\prec\). Bipartition the forest, obtaining a decomposition into two chains. The incomparable pairs of the interval order are precisely the intersecting pairs. Applying Step 1 gives a word containing every linear extension, hence every realizable strict sorting order, of length
\[
n+i(P)=n+(n-c)=2n-c.
\]
This also provides a finite constructive procedure: build the overlap forest, two-color it, sort each color class, compute slot bounds, and emit the word.

**3. Lower-bound path and charging argument.** For any integer \(m\ge 2\), take the \(m\) intervals
\[
I_j=(2j,2j+3),\qquad j=0,1,\ldots,m-1.
\]
Their overlap graph is a path. Their possible increasing orders include \(0,1,\ldots,m-1\), as well as the permutation obtained by swapping labels \(i\) and \(i+1\) and leaving all other labels in order, for each \(0\le i<m-1\). To see the latter directly, choose realized points \(2j+1\) outside the swapped pair and choose \(2i+11/4\) in interval \(I_i\) and \(2i+9/4\) in interval \(I_{i+1}\); all required inequalities hold.

Suppose \(W\) embeds all those permutations. Fix one embedding of the identity at word positions
\[
p_0<p_1<\cdots<p_{m-1}.
\]
For edge \(i\), fix an embedding of the order with \(i+1\) before \(i\), using positions \(q_{i+1}<q_i\) for those two labels. If \(q_{i+1}<p_{i+1}\), charge edge \(i\) to the occurrence of label \(i+1\) at position \(q_{i+1}\), strictly earlier than its fixed identity occurrence. Otherwise \(q_{i+1}\ge p_{i+1}>p_i\); hence \(q_i>p_i\), so charge the edge to the occurrence of label \(i\) at position \(q_i\), strictly later than its identity occurrence. Every charged occurrence is outside the identity embedding. Distinct edges receive distinct charges: an early extra occurrence of label \(j\) can only be charged by edge \(j-1\), whereas a late extra occurrence of that label can only be charged by edge \(j\). Thus the \(m-1\) edges force at least \(m-1\) extra letters in addition to the \(m\) embedded identity letters. Therefore \(|W|\ge2m-1\). Equality follows from Step 2.

For arbitrary \(1\le c\le n\), set \(m=n-c+1\) and use one path of \(m\) intervals together with \(c-1\) isolated intervals placed far away. If \(m=1\), take \(n\) disjoint intervals. Restricting any sorting-supersequence to the path labels costs at least \(2m-1\) letters when \(m\ge2\), and each remaining isolated label costs at least one letter. Therefore \(|W|\ge (2m-1)+(c-1)=2n-c\), as claimed. For \(m=1\), the lower bound \(n=2n-c\) is immediate. The upper construction attains all these bounds. \(\square\)

## Verification

The supplementary standalone `checker.py` and `checker_output.txt` give finite independent corroboration. The checker exhaustively enumerates every pairing of distinct ordered endpoints for \(1\le n\le6\), filters ply-two instances, constructs the two-chain word, and tests every linear extension for subsequence containment and the asserted word length. It processes 11,464 pairings, including 364 ply-two instances and 2,090 linear extensions. A separate breadth-first shortest-word computation for families of disjoint adjacent transpositions reproduces the path lower bound at \(2\le m\le7\). It prints `ALL_CHECKS_PASSED`. The infinite theorem is established by the preceding proof, not by these finite checks.

Reproduce with `python3 checker.py` from the directory containing the supplementary files. The checker uses Python's standard library and has no external dependencies.

## Relationship to prior work

Löffler and Raichel (arXiv:2601.19453, publicly posted January 27, 2026) introduced sorting-supersequences as preprocessing structures. Their Definitions 1–2 specify sorting-supersequences and ply. Their Theorem 6 gives a general \(O(n\Delta^2)\) construction, and their Theorem 5 gives an \(O(n\Delta)\) smooth construction for unit intervals. In particular, Figure 2 explicitly depicts a ply-two family requiring one interval label many times. The present theorem sharpens the **worst-case numerical length bound** for all ply-two families, with the exact component dependence and a matching obstruction. It does not inherit or establish the smoothness guarantee of their unit-interval construction.

Radomirović (2012) studies universal words containing *all permutations* of an alphabet, whereas here the obligatory permutations are constrained by an interval order or a width-two poset. Neither general all-permutation construction implies the present sharp component-sensitive length bound.

## Limitations

The equality \(2n-c\) is a worst-case extremal value for each \((n,c)\); individual interval families may have shorter valid words. For a general width-two poset, \(n+i(P)\) is a constructed upper length, not necessarily an optimal shortest length. The argument assumes distinct endpoints and at most two intervals meeting at any point. It says nothing about ply at least three, smooth sorting-supersequences, the computational model for extracting a sorted sequence, or minimal supersequences of unrelated arbitrary word sets. This is a mathematical proof with finite cross-checks and no independent external validation.

## References

1. M. Löffler and B. Raichel, *Preprocessing Uncertain Data into Supersequences for Sorting and Gaps*, arXiv:2601.19453v1, first posted January 27, 2026, https://arxiv.org/abs/2601.19453. Definitions 1–2, Theorems 5–6, Figure 2, and Section 3.
2. R. Radomirović, *A Construction of Short Sequences Containing All Permutations of a Set as Subsequences*, Electronic Journal of Combinatorics **19**(4) (2012), P31, https://doi.org/10.37236/2859. Introduction and universal-word construction.
