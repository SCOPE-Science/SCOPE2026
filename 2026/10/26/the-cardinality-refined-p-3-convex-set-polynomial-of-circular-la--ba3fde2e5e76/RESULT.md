# The cardinality-refined \(P_3\)-convex-set polynomial of circular ladders

## Finding

For an integer \(n\ge3\), let \(R_n=C_n\square K_2\) be the *circular ladder* (or prism) with two labeled \(n\)-cycles and corresponding rungs. A vertex set \(S\subseteq V(R_n)\) is \(P_3\)-convex when every vertex outside \(S\) has at most one neighbor in \(S\). Define
\[
 A_n(z)=\sum_{S\subseteq V(R_n):\ S\text{ is }P_3\text{-convex}}z^{|S|}.
\]
Put
\[
 q_2(t,z)=1-zt+zt^2
\]
and
\[
 q_5(t,z)=1-(1+z+z^2)t+(z^2+z^3)t^2-(z+z^2)t^3+2z^3t^4+z^3t^5.
\]
Then the **complete cardinality-refined enumeration**, for every simple circular ladder of circumference at least three, is
\[
 \boxed{\displaystyle
 \sum_{n\ge3} A_n(z)t^n=-t\frac{\partial}{\partial t}\log\bigl(q_2(t,z)q_5(t,z)\bigr)
 -(1+2z+z^2)t-(1+2z^2+z^4)t^2.}
\]
Here the logarithm is interpreted over \(\mathbb Q[z][[t]]\), while its displayed logarithmic derivative has coefficients in \(\mathbb Z[z][[t]]\); the formula is an exact formal power-series identity, not an analytic approximation. In particular,
\[
 A_3(z)=1+6z+3z^2+2z^3+z^6,
 \quad A_4(z)=1+8z+16z^2+6z^4+z^8.
\]
The sequence of total numbers \(A_n(1)\) starts \(13,32,69,157,361,824,1894,4379\) for \(n=3,\ldots,10\). The denominator has degree seven in the circumference variable, so all cardinality coefficients obey an explicit uniform linear recurrence of order at most seven, obtained from \(q_2q_5\).

The same theorem gives the maximum size of a **proper** \(P_3\)-convex set and the number of sets attaining it:
\[
 \boxed{\begin{array}{c|c|c}
 n&\max\{|S|:S\subsetneq V(R_n),\ S\text{ is }P_3\text{-convex}\}&\text{number of maximizers}\\ \hline
 3&3&2\\
 4&4&6\\
 n\ge5&2n-4&n
 \end{array}}
\]
For \(n\ge5\) the maximizers are exactly the complements of the \(n\) rectangular four-cycles formed by successive rungs. For \(n=4\), two further maximizers are the complements of the two four-vertex rim cycles; for \(n=3\), both maximizers are complements of the two triangular rim cycles.

## Assumptions and scope

All graphs are finite, undirected, simple, with labeled vertices. The cycle \(C_n\) has \(n\ge3\) vertices; no case with a doubled edge or loop is included. The labeling fixes the two layers and every column, so the enumeration counts distinct vertex subsets, not orbits under rotation, reflection, or layer exchange. Both the empty and the full subset are counted, at weights zero and \(2n\), respectively.

The \(P_3\)-convexity used here is the closure under *all* three-vertex paths, not exclusively induced three-vertex paths. In the cubic graph \(R_n\), the complement \(T=V(R_n)\setminus S\) of a convex set is either empty or induces minimum degree at least two: each vertex in \(T\) has three neighbors in \(R_n\) and must have at most one neighbor outside \(T\). This equivalent formulation is also useful in two-neighbor bootstrap percolation: the convex sets are precisely its closed infected configurations.

## Proof

**1. Local compatibility and a finite transfer.** Enumerate columns around the cycle by \(i\in\mathbb Z/n\mathbb Z\), and let the two vertices in column \(i\) have membership bits \((a_{i,0},a_{i,1})\in\{0,1\}^2\), where one means membership in \(S\). Encode this ordered pair by \(a_i=a_{i,0}+2a_{i,1}\in\{0,1,2,3\}\). For any three column codes \((a,b,c)\), write \(a_r,b_r,c_r\) for their row-\(r\) bits, \(r\in\{0,1\}\). The central column is locally valid exactly when, for each \(r\),
\[
 b_r=0\quad\Longrightarrow\quad a_r+c_r+b_{1-r}\le1. \tag{1}
\]
Indeed these are exactly the three neighbors of its row-\(r\) vertex. Thus a cyclic sequence \((a_0,\dots,a_{n-1})\) is valid if and only if (1) holds for each cyclic triple \((a_{i-1},a_i,a_{i+1})\). Its contribution to \(A_n(z)\) is \(z^{\sum_i\operatorname{popcount}(a_i)}\).

Adjacent *nonzero unequal* column codes can never occur in a valid sequence: if the codes are \(1\) and \(2\), or either of these and \(3\), one of the two columns has an excluded row vertex adjacent both to its selected rung mate and to a selected vertex in the neighboring column, violating (1). Consequently no cyclic valid sequence contains any of the six adjacent ordered pairs \((1,2),(1,3),(2,1),(2,3),(3,1),(3,2)\).

Use the following ten allowed adjacent-code pairs as states, in this order:
\[
 (0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(2,0),(2,2),(3,0),(3,3).
\]
Make a transition from \((a,b)\) to \((b,c)\) precisely when (1) holds and give that transition the weight \(z^{\operatorname{popcount}(b)}\). The complete weighted transition table follows. The indicated weight applies to every destination in its row.

| State | Successor states | Weight |
|---|---|---|
| `(0,0)` | `(0,0)`, `(0,1)`, `(0,2)`, `(0,3)` | \(1\) |
| `(0,1)` | `(1,0)`, `(1,1)` | \(z\) |
| `(0,2)` | `(2,0)`, `(2,2)` | \(z\) |
| `(0,3)` | `(3,0)`, `(3,3)` | \(z^2\) |
| `(1,0)` | `(0,0)`, `(0,2)` | \(1\) |
| `(1,1)` | `(1,0)`, `(1,1)` | \(z\) |
| `(2,0)` | `(0,0)`, `(0,1)` | \(1\) |
| `(2,2)` | `(2,0)`, `(2,2)` | \(z\) |
| `(3,0)` | `(0,0)` | \(1\) |
| `(3,3)` | `(3,0)`, `(3,3)` | \(z^2\) |

Let \(M(z)\) be the explicit \(10\times10\) matrix represented by this table, with rows indexed by sources and columns indexed by destinations. For \(n\ge3\), the cyclic word and the closed walk of length \(n\) with its *labeled initial state* determine each other bijectively; every code occurs once in the transition weight. It follows that
\[
 A_n(z)=\operatorname{tr}(M(z)^n),\qquad n\ge3. \tag{2}
\]
This trace does *not* quotient by a cycle symmetry or introduce a factor of \(n\): the fixed labeled column zero specifies the initial state.

**2. Exact characteristic computation.** Straight polynomial elimination on the ten rows given above yields
\[
 \det(I-tM(z))=q_2(t,z)q_5(t,z).\tag{3}
\]
This is a finite polynomial identity over \(\mathbb Z[t,z]\). Every matrix entry needed to reconstruct and verify (3) is explicitly listed, and the standalone `verify.py` evaluates both sides symbolically and tests their exact equality. In particular no numerical determinant or extrapolation is used to infer (3).

For any finite square matrix \(M\) over a commutative polynomial ring, the formal power-series identity
\[
 -t\,\partial_t\log\det(I-tM)=\sum_{n\ge1}\operatorname{tr}(M^n)t^n
\]
comes from the formal identity \(\log\det(I-tM)=\operatorname{tr}\log(I-tM)\). The first two formal trace coefficients from (3) are \(1+2z+z^2\) and \(1+2z^2+z^4\), respectively. These terms do not represent the two simple prism graphs (which are undefined for circumferences one and two) and are explicitly subtracted. Combining (2) and (3) proves the displayed generating function for all \(n\ge3\).

**3. Largest proper convex sets.** Let \(S\subsetneq V(R_n)\) be convex and \(T=V(R_n)\setminus S\). The induced graph \(R_n[T]\) has minimum degree at least two, so it contains a cycle. Every cycle in \(R_3\) has length at least three, and every cycle in \(R_n\) for \(n\ge4\) has length at least four. Thus \(|T|\ge3\) in the triangular prism and \(|T|\ge4\) otherwise. Every shortest cycle is itself a permissible choice of \(T\), because its vertices each have two neighbors on the cycle, making its complement \(P_3\)-convex. Equality forces \(T\) to be the vertex set of a shortest cycle. There are precisely two triangles in \(R_3\); precisely six four-cycles in \(R_4\) (four rectangular faces and two rims); and precisely \(n\) four-cycles for \(n\ge5\), all rectangular faces. This proves the extremal part, including the exceptional counts.

## Verification

The accompanying standalone `verify.py` reconstructs the local rule and both ten-state and sixteen-state matrices, checks the polynomial determinant identity exactly using symbolic arithmetic, and compares the generating-function coefficients with transfer-matrix traces. It also directly enumerates every labeled vertex subset of \(R_n\) for \(3\le n\le9\) using independently constructed graph-neighborhood lists, without invoking the local column test. Polynomial coefficients agree in every case. Further transfer and recurrence comparisons cover \(3\le n\le20\), including the maximum-proper-cardinality coefficients. The recorded output is `verify_output.txt` and ends in `VERIFY_OK`.

The proof of the infinite-family generating function is the algebraic transfer identity and the bijection above. Finite enumeration is corroboration rather than an inference about unbounded \(n\).

## Relationship to prior work

Dourado, Grippo, Lin and Protti's March 2026 paper *Counting \(P_3\)-convex sets in graphs* proves general extremal and complexity results, gives a linear-time counting algorithm on trees and threshold graphs, derives an unrefined recurrence for paths, and gives exact-exponential algorithms for arbitrary graphs. Inspection of its full 27-page paper did not identify a prism-family cardinality polynomial, a rational circumference generating function, or the complete size distribution claimed here. The existence of an algorithm that can count a graph does not itself supply the closed uniform formula (3).

Brešar and Valencia-Pabón's 2019 *On the \(P_3\)-hull number of Hamming graphs*, Theorem 1, proves that **connected** \(P_3\)-convex sets in Cartesian products factor as products of convex subsets of their factors. This concerns connected sets and does not count the disconnected convex subsets included in \(A_n(z)\); it neither gives (2) nor implies the stated refined enumeration without additional analysis.

Borges and Nascimento's 2026 study *\(P_3\)-convex partitions in Cartesian product and strong product of graphs* concerns partitioning all vertices into multiple convex blocks, a different requirement from counting each individual convex subset (whose complement need not be convex). Its accessible abstract does not state a complete single-subset polynomial, although the inaccessible full paper leaves a possible bibliographic overlap risk.

The definition of \(P_3\)-convexity, the general Cartesian-product structural theorem, formal transfer matrices and logarithmic determinant identities are established mathematical tools; they are not presented as new. The claimed contribution is their evaluated, nontrivial full cardinality distribution and extremal consequence for the circular-ladder family.

## Limitations

The result is specific to labeled simple circular ladders \(C_n\square K_2\) with \(n\ge3\). It does not supply closed formulas for arbitrary Cartesian products, general bounded-treewidth graphs, or convex-set orbits under graph automorphisms. The 2026 partition proceeding could be inspected only at the abstract level; inaccessible or unindexed earlier papers might contain an equivalent formula. The proof has received a self-review but no independent mathematical audit or formal certification.

## References

1. M. C. Dourado, L. N. Grippo, M. C. Lin and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1, first submitted 2026-03-05. https://arxiv.org/pdf/2603.04706
2. B. Brešar and M. Valencia-Pabón, *On the \(P_3\)-hull number of Hamming graphs*, 2019, especially Theorem 1. https://lipn.univ-paris13.fr/~valenciapabon/papers/P_3-convexity-RV2.pdf
3. T. N. Borges and J. R. Nascimento, *\(P_3\)-convex partitions in Cartesian product and strong product of graphs*, SBPO proceedings, 2026, abstract accessible at https://proceedings.science/sbpo-2026/papers/p3-convex-partitions-in-cartesian-product-and-strong-product-of-graphs?lang=en
