# Exact optimal outer-independent two-rainbow labelings of products of cliques

## Finding

Let \(G=K_m\times K_n\) be the categorical (tensor/direct) product of two complete graphs on labeled vertex sets, with \(m,n\ge2\). Put \(s=\min\{m,n\}\) and \(t=\max\{m,n\}\). An outer-independent two-rainbow dominating function (OI2RD function) assigns each vertex one of \(\varnothing,\{1\},\{2\},\{1,2\}\), makes the empty-labeled vertices independent, and gives every empty-labeled vertex neighbors whose label union is \(\{1,2\}\). Its weight is the sum of the label sizes. Let \(\gamma_{\mathrm{oir2}}(G)\) be the minimum weight, and let \(M(m,n)\) count **all** attaining functions, distinguishing vertices and the two colors.

The exact minimum and multiplicity are
\[
\gamma_{\mathrm{oir2}}(K_m\times K_n)=
\begin{cases}
4,&(s,t)=(2,2)\text{ or }(2,3),\\
mn-t,&\text{otherwise};
\end{cases}
\]
\[
M(m,n)=
\begin{cases}
36,&(s,t)=(2,2),\\
48,&(s,t)=(2,3),\\
c(s,t)\bigl(2^{(s-1)t}-2-2t(2^{s-1}-1)\bigr),&\text{otherwise},
\end{cases}
\qquad
c(s,t)=\begin{cases}2s,&s=t,\\s,&s<t.\end{cases}
\]

Moreover, outside the two exceptional dimension pairs, every minimum function is obtained uniquely as follows. Choose one full coordinate fiber of maximum size \(t\) and label it empty. Assign a singleton color, either \(\{1\}\) or \(\{2\}\), to each remaining vertex. When the empty fiber is a row of \(K_s\times K_t\), each color must occur in **at least two distinct columns** of the remaining \((s-1)\)-by-\(t\) matrix; the transpose condition applies when the empty fiber is a column. There are no double-colored vertices in these optima.

For example, \(M(2,4)=12\), \(M(3,3)=264\), \(M(3,4)=690\), and \(M(4,4)=32304\). For fixed \(s\ge2\) and \(t\to\infty\) with \(s<t\), the exact formula implies \(M(s,t)\sim s2^{(s-1)t}\): almost every singleton two-color assignment outside a maximum empty fiber is feasible.

## Assumptions and scope

The categorical product has vertex set \([m]\times[n]\), with distinct vertices \((i,j)\) and \((i',j')\) adjacent exactly when \(i\ne i'\) **and** \(j\ne j'\). Only simple complete factors of order at least two are considered. Coordinate vertices and the color names are distinguishable; permutations are not quotiented out. The two-color set \(\{1,2\}\) counts as a weight-two label. This is not the ordinary (non-outer-independent) rainbow-domination problem.

## Proof

**1. All maximum independent sets are full coordinate fibers.** If an independent set has vertices in two different rows, those two must be in the same column (else they are adjacent). Every further vertex not in that column would have to share a row with both of those vertices to avoid adjacency, which is impossible. Thus any independent set lies in one row or one column. Hence its maximum size is \(t\). If \(s<t\), maximum independent sets are precisely the \(s\) rows of length \(t\). If \(s=t\), they are the \(s\) rows and the \(s\) columns, all distinct.

**2. The general lower bound and equality rigidity.** For any OI2RD function, let \(z\) be the number of empty labels and \(d\) the number of double labels \(\{1,2\}\). Every other label is a singleton, so its weight is exactly \(mn-z+d\). By Step 1, \(z\le t\), giving the lower bound \(mn-t\). Equality holds if and only if \(z=t\) and \(d=0\). Therefore every function attaining this lower bound has one full empty maximum fiber and singleton colors elsewhere.

**3. The exact rainbow condition on the remaining matrix.** Take a full empty row in \(K_s\times K_t\). The neighbors of its vertex in column \(j\) are exactly the cells outside both that row and column \(j\). Thus the rainbow condition holds at all empty vertices if and only if each color occurs in at least two distinct columns of the \((s-1)\)-by-\(t\) singleton-color matrix. Necessity follows by deleting the unique column containing a color if its support occupies at most one column; sufficiency follows since deleting any one column cannot erase a color supported in two columns. For a maximum empty column in the balanced case, transpose the coordinates. Such a matrix exists when \(s\ge3\): put color \(1\) in one nonempty row and color \(2\) in another. It also exists when \(s=2\) and \(t\ge4\): use color \(1\) in two columns and color \(2\) in all remaining columns. Consequently the lower bound in Step 2 is attained for all nonexceptional pairs.

**4. Counting the optimal matrices.** Let \(a=s-1\) and \(t\ge3\). Among the \(2^{at}\) binary-colored \(a\)-by-\(t\) matrices, those in which color \(1\) is supported in at most one column number \(1+t(2^a-1)\): the all-color-\(2\) matrix, or a specified nonempty set of color-\(1\) positions in a unique column. The same number fail for color \(2\). These two bad families are disjoint for \(t\ge3\), since at least three nonempty columns cannot be covered by the union of two single-column color supports. Therefore the number of good matrices is
\[
B(a,t)=2^{at}-2\bigl(1+t(2^a-1)\bigr).
\]
Each maximum empty fiber gives precisely \(B(s-1,t)\) minima. Multiplying by the \(s\) possible fibers when \(s<t\), or the \(2s\) possible fibers when \(s=t\), gives the stated formula. No function is counted twice because its set of empty vertices uniquely determines its fiber.

**5. The \((2,3)\) exception.** The graph \(K_2\times K_3\) is a six-cycle \(C_6\). Its independent sets have size at most three; if a function had weight three, it would require three empty vertices forming one bipartition class and three singleton-colored positive vertices in the other. Each empty vertex would require its two neighbors to have different colors. This would require each pair among the three positive vertices to have different colors, impossible with two colors. Weight four is attainable, and every weight-four function belongs to one of the following disjoint cases:

* Exactly three empty labels and one double label. The empty set is one of the two bipartition classes, the double label occupies one of the three positive vertices, and the other two positive vertices must have opposite singleton colors. This yields \(2\cdot3\cdot2=12\) functions.
* Exactly two empty labels and no double labels. There are nine unordered independent pairs on \(C_6\), six at cyclic distance two and three at distance three. For each pair, requiring both neighbors of each empty vertex to have distinct singleton colors imposes two independent opposite-color constraints on the other four vertices. Thus there are exactly four assignments per pair, giving \(9\cdot4=36\).

The total is \(12+36=48\).

**6. The \((2,2)\) exception.** The product \(K_2\times K_2\) is the disjoint union of two edges. On an isolated edge, the minimum OI2RD weight is two, attained either by labeling both endpoints with one of two singleton colors (four assignments), or by labeling one endpoint empty and the other \(\{1,2\}\) (two assignments). Hence that edge has six minimum functions. Additivity across the two components yields minimum weight four and \(6^2=36\) functions.

These cases exhaust every pair \(m,n\ge2\), proving both formulas and all structural assertions.

## Verification

The included standalone `check.py` uses explicit adjacency for the categorical product, independent graph-level feasibility testing, and no external libraries. Its complete four-symbol enumeration confirms the minimum and count at dimensions \((2,2)\), \((2,3)\), \((2,4)\), and \((3,3)\). A separate exhaustive two-color matrix enumeration checks the column-support count in sixteen additional parameter pairs. It also verifies 179 explicit large-parameter optimum witnesses. Running `python3 check.py` prints `VERIFY_OK`. The infinite classification and inclusion-exclusion identity are mathematical proofs; the finite tests are corroboration, not a substitute.

## Relationship to prior work

Samadi and Soltankhah, *Further results on outer independent 2-rainbow dominating functions of graphs* (first posted 2022-08-03, arXiv:2208.02340), established general direct-product bounds and discussed products of complete graphs in their Theorem 3.1. Their result does not enumerate all minimum functions or give the two-color matrix classification. The generic vertex-cover lower bound and the earlier values on cycles and complete graphs appear in Mansouri and Mojdeh (2020); in particular the exceptional six-cycle minimum is consistent with their cycle formula. Cabrera-Martínez (2022) studies related bounds and other graph operations. The scalar minimum alone does not imply the exact number of attaining labelings or the small-dimensional multiplicities. The distinction between ordinary two-rainbow and outer-independent two-rainbow domination, and between the categorical and Cartesian products, is essential.

## Limitations

This theorem enumerates **minimum-weight** functions, not all feasible functions of higher weight, and it concerns only two complete factors with both orders at least two. It does not classify labelings modulo graph automorphisms or exchange of the colors. A literature search cannot exclude unindexed prior equivalences, and an independent audit or publication-priority determination has not been performed.

## References

1. B. Samadi and N. Soltankhah, *Further results on outer independent 2-rainbow dominating functions of graphs*, arXiv:2208.02340 (first version 2022-08-03), especially Section 3.1 and Theorem 3.1. https://arxiv.org/abs/2208.02340
2. Z. Mansouri and D. A. Mojdeh, *Outer independent rainbow dominating functions in graphs*, Opuscula Mathematica 40 (2020), 599–615, especially Observations 2.2 and 2.3. https://doi.org/10.7494/OpMath.2020.40.5.599
3. A. Cabrera-Martínez, *A Note on Outer-Independent 2-Rainbow Domination in Graphs*, Mathematics 10 (2022), 2287, related bounds and operations. https://doi.org/10.3390/math10132287
