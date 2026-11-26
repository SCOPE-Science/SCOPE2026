# Rank polynomials for induced-path convexity on cographs and the first nonunimodal trivially perfect graph

## Finding

For a finite simple cograph \(G\), let \(F_G(z)=\sum_S z^{|S|}\), where \(S\subseteq V(G)\) is closed under adding the middle vertex of any induced three-vertex path whose endpoints belong to \(S\). The entire \(F_G\) is computable by a binary cotree recurrence, using the clique polynomial \(K_G\) alongside \(F_G\). Given the cotree, this requires \(O(n^2)\) integer arithmetic operations for \(n=|V(G)|\), without a bit-complexity assertion.

Within the subclass of trivially perfect graphs, every \(F_G\) on at most four vertices is unimodal. On five vertices the only nonunimodal example up to isomorphism is \(K_{1,4}\), with coefficients \((1,5,4,6,4,1)\) in ascending size. The contributions are the induced-path cotree recurrence and this smallest-order uniqueness result. The star polynomial and its elementary shape consequences below serve as background, not separate contributions.

## Assumptions and scope

Graphs may be disconnected. A set \(S\) meets the convexity condition exactly when \(N(v)\cap S\) is a clique for each \(v\notin S\). This differs from the all-path \(P_3\) condition \(|N(v)\cap S|\le1\). Empty sets are counted in both \(F_G\) and \(K_G\), the latter enumerating cliques by size. Cographs are built by disjoint union and complete join, equivalently are induced-\(P_4\)-free. The trivially perfect graphs additionally exclude induced \(C_4\); they are built by disjoint union and adjoining universal vertices. Their induced-path convexity is a convex geometry: the known characterization for connected graphs extends componentwise, since closure is componentwise and an anti-exchange violation would have to be in a single component.

## Proof of the recurrence

For the empty graph both polynomials are \(1\), and for a singleton both are \(1+z\). For nonempty \(A,B\), disjoint union gives
\[
F_{A\sqcup B}=F_AF_B,\qquad K_{A\sqcup B}=K_A+K_B-1.
\]
Convexity is tested componentwise and each nonempty clique lies on one side. For the complete join write \(a=|V(A)|, b=|V(B)|\), \(D_X=F_X-K_X\), and \(e_X=1\) for a complete graph and \(0\) otherwise. Then
\[
K_{A\vee B}=K_AK_B,\qquad
F_{A\vee B}=K_AK_B+e_Bz^bD_A+e_Az^aD_B+(1-e_A)(1-e_B)z^{a+b}.
\]
Indeed, the selected set restricts to a convex set on each side. If the selected part in \(A\) contains two nonadjacent vertices then no vertex of \(B\) can be omitted, since every omitted vertex there would be an excluded middle. The symmetric statement applies to a selected nonclique in \(B\). If both parts are cliques they join to a clique. If just one is a nonclique the other must be its whole side, which must be complete. If both are noncliques the selected set is the whole graph with both sides noncomplete. Conversely these four disjoint alternatives are valid: internal paths are handled by the restrictions, while any induced path crossing the join has nonadjacent endpoints on one side, which forces all vertices of the other side to be included.

At a binary node with child sizes \(a,b\ge1\), convolutions cost \(O(ab)\) arithmetic operations and all other coefficient work costs \(O(a+b)=O(ab)\). Completeness is tracked using the two child flags (a nontrivial disjoint union is incomplete; a join is complete exactly when both children are complete). The sum of \(ab\) over nodes is \(\binom n2\), since each distinct pair of leaves contributes exactly at its lowest common ancestor.

## Proof of the first-obstruction claim

On a star, selecting the center allows an arbitrary set of leaves, and omitting it allows at most one leaf. Hence \(F_{K_{1,d}}=1+dz+z(1+z)^d\), also an immediate specialization of earlier weighted all-path counting on block graphs, since stars are triangle-free. The coefficient list is unimodal for \(d=1,2,3\), and for \(d\ge4\) has the strict valley \(d+1>d<\binom d2\). For completeness it is log-concave precisely for \(d\le2\): those two lists directly pass the inequalities, whereas \(d^2<(d+1)\binom d2\) for \(d\ge3\).

For a graph \(H\), the universal extension satisfies \(F_{K_1\vee H}=K_H+zF_H\). Every connected trivially perfect graph of order at least two is such an extension in the same class. At orders up to three the possibilities are complete graphs, disjoint unions of complete graphs, and \(P_3\), with the latter having coefficients \((1,3,2,1)\). Extending each of the four three-vertex graphs gives the four connected sequences at order four:
\[
(1,4,3,3,1),\quad(1,4,4,3,1),\quad(1,4,5,2,1),\quad(1,4,6,4,1).
\]
The disconnected four-vertex cases are all products of binomial clique factors except \(P_3\sqcup K_1\), which has coefficients \((1,4,5,3,1)\).

At order five the possible connected graphs are universal extensions of the nine four-vertex graphs other than \(P_4,C_4\). Applying the universal-extension formula gives the following complete table:

| Sorted degrees of the four-vertex graph | Coefficients after extension |
|:--|:--|
| \((0,0,0,0)\) | \((1,5,4,6,4,1)\) |
| \((0,0,1,1)\) | \((1,5,5,6,4,1)\) |
| \((0,1,1,2)\) | \((1,5,6,5,3,1)\) |
| \((1,1,1,1)\) | \((1,5,6,6,4,1)\) |
| \((0,2,2,2)\) | \((1,5,7,7,4,1)\) |
| \((1,1,1,3)\) | \((1,5,7,3,3,1)\) |
| \((1,2,2,3)\) | \((1,5,8,5,3,1)\) |
| \((2,2,3,3)\) | \((1,5,9,7,2,1)\) |
| \((3,3,3,3)\) | \((1,5,10,10,5,1)\) |

Only the first row, the star, fails unimodality. A disconnected graph on five vertices contains at most one noncomplete connected component, since such components have order at least three. Its remaining components give a binomial factor. Multiplication of a nonnegative unimodal coefficient sequence by \(1+z\) preserves unimodality: the new first differences are \(a_i-a_{i-2}\) with zeros outside the old range, hence are nonnegative up to the old peak and nonpositive from two steps after it; the one intervening difference can have either sign. Repeating for the binomial factor completes the proof.

## Verification and related work

The companion `verify.py` enumerates subsets using the excluded-middle condition and compares with the cotree rules on the 6,039 labelled cographs through order six. It checks the 462 labelled trivially perfect graphs through order five, with exactly five labelled nonunimodal stars. These bounded checks also test the star shape inequalities for \(1\le d\le11\); the proofs above are not finite extrapolations.

Gutiérrez, Protti and Tondato give the structural characterization of induced-path convex geometries. Dourado, Penso and Rautenbach study the hull number, a different invariant. Dourado, Grippo, Lin and Protti count all-path \(P_3\)-convex sets, including scalar counts for threshold graphs. The earlier three-state multivariate all-path recurrence for block graphs gives the star polynomial by specializing to the bridge blocks of a star and setting all vertex weights equal. It does not count induced-path convex sets on general cographs; in particular a triangle can trigger the all-path condition but not the induced-path one. The star formula and the shape checks specific to that formula are not claimed as new. Equivalent earlier formulas for the full induced-path recurrence or the first-obstruction classification remain a literature-coverage risk.

## References

1. M. Gutiérrez, F. Protti and S. B. Tondato, *Convex geometries over induced paths with bounded length*, arXiv:2203.05588; Discrete Mathematics 346 (2023), 113133.
2. M. C. Dourado, L. D. Penso and D. Rautenbach, *The hull number in the convexity of induced paths of order 3*, Theoretical Computer Science 906 (2022), 52–63, DOI 10.1016/j.tcs.2022.01.004.
3. M. C. Dourado, L. N. Grippo, M. C. Lin and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706.
4. *A three-state multivariate \(P_3\)-convexity polynomial for block graphs*, Resultary, 2026-10-13, record `af818a6c215c`.
