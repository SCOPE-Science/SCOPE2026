# Strong-odd coloring polynomial and parity transition of crown graphs

## Finding
Let \(H_n=K_{n,n}-M\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matching \(M=\{a_ib_i:1\le i\le n\}\), for every integer \(n\ge3\). Write \(SO_{H_n}(q)\) for the number of proper strong-odd colorings using \(q\) named available colors, with unused colors permitted. Then
\[
SO_{H_n}(q)=\sum_{s=0}^n\binom ns(q)_{\underline{2n-s}}+\mathbf{1}_{\{n\text{ even}\}}\left[2(q)_{\underline{n+1}}+(q)_{\underline{2}}\right].
\]
Here \((q)_{\underline{k}}=q(q-1)\cdots(q-k+1)\) for nonnegative integers \(q,k\), equals one for \(k=0\), and is zero when \(k>q\). The formula holds for all integers \(q\ge0\).

The strong-odd chromatic number therefore has the parity transition
\[
\chi_{\mathrm{so}}(H_n)=\begin{cases} n,&n\text{ odd},\\2,&n\text{ even}.\end{cases}
\]
Every coloring class is one vertex; one deleted-matching pair \(\{a_i,b_i\}\); or, only when \(n\) is even, all of \(A\) or all of \(B\). The last two types of global colorings not accounted for by a matched-pair partition are completely classified below.

## Assumptions and scope
All graphs are finite, simple, and undirected. A coloring is *proper* when adjacent vertices have different colors; it is *strong odd* when, for each vertex \(v\) and color \(c\), the number of neighbors of \(v\) colored \(c\) is either zero or odd. Color names are distinguished in \(SO_{H_n}(q)\), and colors may be unused. An unlabeled coloring partition is a partition of vertices into nonempty color classes, without assigning color names. No result is asserted for \(n<3\) or for arbitrary matching-deleted bipartite graphs.

## Proof
**Step 1: classify one color class.** A nonempty subset \(S\) can be a class in a proper strong-odd coloring if and only if it is independent and \(\lvert N(v)\cap S\rvert\) is either zero or odd for every vertex \(v\). If \(S\) meets both bipartition classes, properness of coloring forces every cross-side pair in \(S\) to be a missing edge. Since these missing edges form a matching, \(S=\{a_i,b_i\}\) for exactly one \(i\). These classes satisfy the parity test: each vertex sees either zero or one of their vertices.

If \(S\subseteq A\), write \(t=\lvert S\rvert\). Each \(b_i\) has \(t-1\) neighbors in \(S\) when \(a_i\in S\) and \(t\) when \(a_i\notin S\). For \(2\le t<n\), some vertices of both kinds exist, and both counts are positive; consecutive positive integers cannot both be odd. When \(t=1\), all nonzero counts equal one, so every singleton is valid. When \(t=n\), all nonzero counts equal \(n-1\), which is odd precisely when \(n\) is even. The identical argument holds with \(A\) and \(B\) interchanged. This proves the complete class classification and shows each listed class is feasible.

**Step 2: count partitions lacking full-side classes.** Such a partition independently chooses a subset \(I\subseteq[n]\) of indices for which \(\{a_i,b_i\}\) is a two-vertex class; its other vertices form singletons. If \(\lvert I\rvert=s\), there are \(\binom ns\) possibilities and exactly \(2n-s\) classes. Injectively assigning color names from a palette of \(q\) colors gives \((q)_{\underline{2n-s}}\) colorings.

**Step 3: count partitions using a full side.** This is possible only when \(n\) is even. If \(A\) is monochromatic, \(B\) must consist of singletons or one entire class \(B\), because no matched pair can coexist with all of \(A\) in one class. Symmetrically for \(B\). The two disjoint partition families where exactly one side is monochromatic give \(2(q)_{\underline{n+1}}\) named colorings. The partition into exactly the two full sides gives \((q)_{\underline2}\). These three families are disjoint and exhaust the extra cases. Adding the terms establishes the stated formula.

**Step 4: minimum number of colors.** For odd \(n\), all classes have size at most two; covering \(2n\) vertices requires at least \(n\) classes, attained by the \(n\) distinct missing-edge pairs. For even \(n\), two full sides are each valid color classes and are adjacent to each other, so exactly two colors are needed. The proof holds for all \(n\ge3\).

## Verification
The included stand-alone Python verifier independently enumerates every candidate color class by adjacency-bitmask tests for \(3\le n\le9\); enumerates unlabeled color partitions using a separate recursive enumeration; checks the formula on palettes through \(q=2n+2\); and directly enumerates \(1,201,518\) labeled color assignments on selected small cases. It reports \(349,497\) checked nonempty graph subsets and `ALL_OK`. Execute `python verify.py` in the directory containing the embedded file. The finite computation is not the proof of the universal claim: the class classification and disjoint enumeration above provide that proof.

## Relationship to prior work
Kwon and Park (2024) introduced and studied proper strong-odd colorings in the graph-theoretic sense used here. Caro, Petruševski, Škrekovski, and Tuza (2024) proved general properties of the same invariant, including comparison to square-graph coloring. The first term above is **not a new ordinary chromatic polynomial**: for \(n\ge3\), the square \(H_n^2\) has all possible edges except the \(n\) deleted-matching pairs, and its chromatic polynomial is \(\sum_s\binom ns(q)_{\underline{2n-s}}\). The contribution here is the complete enumeration of proper strong-odd colorings beyond these square-graph colorings, including the parity-dependent extra partitions and the exact total.

The related literature on odd-independent vertex classes establishes general bounds, but does not in the inspected material supply the displayed crown-graph counting identity. In particular, neighborhood-parity odd coloring without the stronger requirement on *each* occurring neighborhood color is a distinct invariant and is not substituted for strong-odd coloring here.

## Limitations
The proof covers crown graphs only for \(n\ge3\). The even-order minimum-color phenomenon has been observed in related calculations; the claimed contribution is the **entire named-coloring polynomial and exact class partition description**, not an assertion of first discovery of the isolated even-order scalar value. Literature discovery cannot rule out an unindexed equivalent enumeration. There has been self-review but no independent audit or validation. Exhaustive computations cover finite instances only.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs* (first public 22 January 2024), arXiv:2401.11653, https://arxiv.org/abs/2401.11653 .
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs* (first public 3 October 2024), arXiv:2410.02336, https://arxiv.org/abs/2410.02336 .
3. Y. Caro et al., *The odd independence number of graphs I: Foundations and classical classes* (first public September 2025), arXiv:2509.20763, https://arxiv.org/abs/2509.20763 .
