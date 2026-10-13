# Proper conflict-free coloring polynomial of crown graphs

## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) denote the crown graph with matched nonedges \(a_i b_i\), for every integer \(n\ge3\). For every integer \(q\ge0\), let \(P_n(q)\) be the number of **proper conflict-free colorings** \(\varphi:V(\operatorname{Cr}_n)\to[q]\), where colors need not all be used and each vertex's *open* neighborhood contains a color occurring exactly once.

Put \(S_{m,r}=m![x^m](e^x-1)^r\), \(B_{m,r}=m![x^m](e^x-1-x)^r\), and \(E_{m,r}=r m B_{m-1,r-1}\) when \(m,r\ge1\), with \(E_{m,r}=0\) otherwise. Put \(H_{m,r}=m!/2^r\) when \(m=2r\), and \(H_{m,r}=0\) otherwise. Coefficients are taken in formal power series, with \(0^0=1\) in the constant-series convention. For \(s\ge0\) define
\[
U^{(s)}_{m,r}=\begin{cases}
S_{m,r}-B_{m,r}-E_{m,r}+H_{m,r},&s=0,\\
S_{m,r}-B_{m,r},&s=1,\\
S_{m,r},&s\ge2.
\end{cases}
\]
Then the **entire counting polynomial** is exactly
\[
\boxed{P_n(q)=\sum_{s=0}^{\min(n,q)}\binom ns(q)_s
\sum_{\substack{0\le r,t\le n-s\\r+t\le q-s}}
\binom{q-s}{r}\binom{q-s-r}{t}
U^{(s)}_{n-s,r}U^{(s)}_{n-s,t}.}
\]
Here \((q)_s=q(q-1)\cdots(q-s+1)\), with \((q)_0=1\). In particular, the polynomial gives every exact finite palette count, not just the minimum number of colors.

For four available labeled colors, the formula sharpens to a complete rigidity classification:
\[
\boxed{P_4(4)=384,\qquad P_n(4)=24\binom n2\quad(n\ge5).}
\]
For \(n\ge5\), every proper conflict-free four-coloring, and no others, selects exactly two distinct matched nonedges, assigns one common color to each pair, and colors all remaining vertices on each shore monochromatically, using two further shore-exclusive colors. At \(n=4\), three mutually exclusive classes have respectively \(216,144,24\) labeled colorings: no color shared between shores, exactly two shared colors, or all four colors shared.

## Assumptions and scope
All graphs are finite and simple; \(n\ge3\), \(q\ge0\). The shores of \(\operatorname{Cr}_n\) are \(A=\{a_i:1\le i\le n\}\) and \(B=\{b_i:1\le i\le n\}\), with \(a_i b_j\in E\) precisely when \(i\ne j\). A coloring is proper when adjacent vertices have different colors, and is conflict-free when every vertex has a uniquely colored neighbor in its open neighborhood. The palette \([q]\) consists of \(q\) distinct labeled colors; no surjectivity is imposed.

All numbers in the displayed formula are nonnegative integers, since each \(U^{(s)}_{m,r}\) counts surjective functions on a fixed set of \(m\) vertices to a fixed palette of \(r\) labeled colors subject to an explicit singleton condition. The expression defines the unique polynomial in \(q\) agreeing with these values for all nonnegative integers \(q\).

## Proof
**Step 1: shared colors.** A color occurring on both shores can occur only on a single pair \(\{a_i,b_i\}\): any differently indexed opposite-shore occurrences are adjacent; any third occurrence would be adjacent to one of the pair. Thus every shared color uniquely determines one of the missing matching edges, and no pair supports more than one shared color. Let \(s\) denote the number of such shared colors. Choosing their indices and distinct assigned colors gives \(\binom ns(q)_s\) possibilities.

**Step 2: palettes and the puncture condition.** Delete those \(s\) matched pairs and call the remaining number of vertices on each shore \(m=n-s\). Each other color is used either only on \(A\) or only on \(B\). Choose an \(r\)-color exclusive palette for \(A\) and a disjoint \(t\)-color exclusive palette for \(B\); this gives \(\binom{q-s}{r}\binom{q-s-r}{t}\) choices. Every chosen exclusive color must appear at least once on its shore, so the remaining color assignments are surjective.

For any vertex \(a_i\), its neighborhood is \(B\setminus\{b_i\}\), and likewise with shores exchanged. The conflict-free condition therefore says **every puncture of either shore's color multiset has some singleton color**. If \(s\ge2\), the \(s\) shared, individually singleton colors guarantee this, even when one is punctured; every surjection on the remaining shore is permissible. If \(s=1\), puncturing the sole shared-color occurrence leaves a uniquely colored neighbor precisely when at least one exclusive color has multiplicity one. For \(s=0\), every puncture has a singleton if and only if (i) the original shore has at least two singleton color classes, or (ii) the shore has no singleton class and every color class has size exactly two. Indeed, a puncture can destroy at most one existing singleton, and in the absence of any singleton a puncture creates one exactly when its containing class has size two. A shore with exactly one singleton fails when that vertex is punctured.

**Step 3: labeled partitions.** The number of surjections of \(m\) labeled vertices onto \(r\) labeled colors is \(S_{m,r}\). Those with no singleton fibers are counted by \(B_{m,r}\), using the exponential generating factor \(e^x-1-x\) for classes of size at least two. Those with exactly one singleton fiber are counted by \(E_{m,r}=r m B_{m-1,r-1}\), choosing its color and its unique vertex. The all-doubleton case exists only when \(m=2r\), with \(H_{m,r}=m!/2^r\) assignments: distribute the vertices into \(r\) labeled pairs. Consequently the number of permitted surjections for each value of \(s\) is exactly \(U^{(s)}_{m,r}\) as defined. The cases do not overlap. Multiplying the independent shore counts and summing over all shared pairs and exclusive palettes proves the boxed polynomial identity for every \(n\ge3\), \(q\ge0\).

**Step 4: optimal four-color rigidity.** Suppose \(q=4\) and \(n\ge5\). If \(s=0\), each shore would have at most two available exclusive colors, which cannot meet the puncture condition on five or more vertices. If \(s=1\), each shore has at least \(n-1\ge4\) exclusive-colored vertices and needs an exclusive singleton: thus at least two distinct exclusive colors per shore, requiring at least five colors overall. If \(s\ge3\), there are unpaired vertices on both shores but at most one remaining color, so such colorings are improper. Therefore \(s=2\). The two remaining exclusive colors must each be used on a different shore; each shore's \(n-2\) unmatched vertices are monochromatic. This is sufficient because every neighborhood sees at least one of the two shared singleton colors. There are \(\binom n2\) pair choices, \((4)_2=12\) assignments of shared colors to the two ordered-by-index pairs, and two assignments of the remaining colors to shores, giving \(24\binom n2\).

At \(n=4\), the same \(s=2\) construction yields \(24\binom42=144\). Two further possibilities arise. With \(s=0\), each shore must partition its four vertices into two doubletons with two exclusive colors. Choose two of the four palette colors for \(A\), and independently assign its four indexed vertices into two labeled doubletons, and do the same for \(B\): \(\binom42\binom42\binom42=216\). With \(s=4\), all four indexed pairs have distinct shared colors, producing \(4!=24\). The preceding puncture conditions exclude \(s=1\) and \(s=3\), so \(P_4(4)=144+216+24=384\).

## Verification
Two independent standalone programs are included. `verify_polynomial.py` uses binomial convolution recurrences to compute the quantities \(S_{m,r}\) and \(B_{m,r}\), avoiding formal-series software. It checks the specified four-color formula for every \(4\le n\le12\), and computes full palette counts through \(q=7\) for orders through 10. `verify_exhaustive.cpp`, which does not use the convolution formula, enumerates every one of 28,666,423 labeled candidate maps in fourteen \((n,q)\) profiles and tests each relevant graph edge and open neighborhood directly; its counts agree with the formula. Both programs' exact outputs are included. These finite tests support, but do not replace, the proof for all orders and palettes.

## Relationship to prior work
The proper conflict-free open-neighborhood condition originates with Fabrici, Lužar, Rindošová and Soták (2022). Pradhan and Sharma (arXiv:2608.10874, first public 2026-08-11) recently investigated the complexity and algorithms of its decision version on graph classes. A published 2026 crown-graph result establishes \(\chi_{\mathrm{pcf}}(\operatorname{Cr}_n)=4\) for \(n\ge4\) and proves the shared-color-pair restriction. Both are prior input, not new claims here. The counting polynomial and complete four-color rigidity, including the exceptional \(n=4\) count, determine information not given by the existing minimum-color formula. Previously studied complete-multipartite optimal-color counts concern complete multipartite adjacency, not deleted-matching crown graphs. No general complexity theorem or previously known minimum-color bound is used to claim novelty.

## Limitations
The theorem is about **ordinary** proper conflict-free colorings with respect to open neighborhoods and labeled full-vertex palettes; it does not apply unchanged to partial, list, fractional, odd, or closed-neighborhood colorings. Its exact expression involves finite sums and partial Bell numbers rather than a simplified closed product for general \(q\). The proof makes no claim about counting complexity for general graphs or about colorings of arbitrary matchings-deleted complete bipartite graphs. Novelty is based on literature and record comparisons, not a guarantee against unindexed equivalent research. Independent external validation has not been conducted.

## References
1. D. Pradhan and V. Sharma, “Complexity and algorithms for proper conflict-free coloring in graphs,” arXiv:2608.10874v1, publicly posted 2026-08-11, https://arxiv.org/abs/2608.10874.
2. “Proper conflict-free chromatic number of crown graphs,” published 2026-09-30, https://github.com/published-finding corpus/2026/tree/main/2026/9/30/SCOPE-exact-proper-conflict-free-chromatic-number-of-crown-graphs--24fe2313d105. The shared-color lemma and minimum-color formula are credited here.
3. I. Fabrici, B. Lužar, S. Rindošová and R. Soták, “Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods,” arXiv:2202.02570 (2022), https://arxiv.org/abs/2202.02570.
4. J. Ahn, S. Im and S.-i. Oum, “The proper conflict-free \(k\)-coloring problem and the odd \(k\)-coloring problem are NP-complete on bipartite graphs,” arXiv:2208.08330.
