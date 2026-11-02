# Size-refined \(P_3\)-convex sets on cyclic prisms

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the labelled two-row cyclic prism. A subset \(S\subseteq V(G_n)\) is \(P_3\)-convex if every vertex outside \(S\) has at most one neighbor in \(S\). Define its full cardinality enumerator
\[
F_n(x)=\sum_{S\text{ is }P_3\text{-convex}}x^{|S|}.
\]
Put \(C_n(y)=y^{2n}F_n(y^{-1})\), with \(C_n(0)=1\). Define
\[
P_2(z,y)=1-yz+y^3z^2
\]
and
\[
\begin{aligned}
P_5(z,y)={}&1-(1+y+y^2)z+(y+y^2)z^2\\
&-(y^4+y^5)z^3+2y^5z^4+y^7z^5.
\end{aligned}
\]
Then the exact all-size, all-length enumerator is
\[
\boxed{\sum_{n\ge1}C_n(y)z^n=-z\frac{\partial}{\partial z}\log\big(P_2(z,y)P_5(z,y)\big).}
\]
The summation on the left uses the transfer-matrix extension at lengths \(1,2\); its coefficients for all genuine simple prisms \(n\ge3\) equal the defined graph enumerators. In particular, the numbers of convex sets for \(n=3,4,5,6,7,8\) are respectively \(13,32,69,157,361,824\).

For \(n\ge10\), the first ten coefficients counting the complementary vertices \(T=V(G_n)\setminus S\) are
\[
([y^j]C_n(y))_{j=0}^{9}=
\left(1,0,0,0,n,0,n,0,\frac{n(n-3)}2,2n\right).
\]
Thus there are no proper convex sets missing exactly \(5\) or \(7\) vertices once \(n\ge10\), whereas the numbers missing \(4\), \(6\), \(8\) and \(9\) vertices have the indicated exact formulas. At \(y=1\), the full counts grow as \(\lambda^n(1+o(1))\), where \(\lambda\approx2.31240391\) is the unique dominant positive root of
\[
t^5-3t^4+2t^3-2t^2+2t+1=0.
\]

## Assumptions and scope
Every graph is finite, undirected, simple and labelled. The two cycle rows are distinguished and cycle vertices have positions in \(\mathbb Z/n\mathbb Z\). Only \(n\ge3\) is asserted as a graph theorem. The empty set and full vertex set are included in the enumerator; complements with no vertices are allowed and vacuously have minimum induced degree at least two. This is ordinary \(P_3\)-convexity using every two-edge path, not induced-path-only convexity. The variable \(y\) records the size of the complement and \(x\) records the size of the convex set. No quotient by rotations or row exchange is taken.

## Proof
**Complement formulation.** Since \(G_n\) is cubic, for any \(S\subseteq V(G_n)\) the condition that each vertex outside \(S\) have at most one neighbor in \(S\) is equivalent to every vertex of \(T=V(G_n)\setminus S\) having at least two neighbors in \(T\). Hence \(C_n(y)\) counts induced subgraphs of minimum degree at least two, weighted by their vertex count. This equivalence includes \(T=\varnothing\).

**Finite local automaton.** Encode the intersection of \(T\) with column \(i\) by \(b_i\in\{0,1,2,3\}\), where its two binary digits indicate inclusion of upper and lower vertices. For three successive column states \(a,b,c\), let \(g(a,b,c)\) be true precisely when, for both row positions \(r\in\{0,1\}\), a selected bit in the middle column has at least two selected neighbors among its vertical partner and its same-row neighbors in the preceding and following columns. Explicitly, for every selected middle bit \(r\), require
\[
\mathbf1_{r\in a}+\mathbf1_{r\in c}+\mathbf1_{1-r\in b}\ge2.
\]
Let \(M(y)\) be the \(16\times16\) matrix whose rows and columns are ordered pairs \((a,b)\) of these four states, with
\[
M_{(a,b),(b',c)}(y)=
\begin{cases}y^{\operatorname{popcount}(c)},&b=b'\text{ and }g(a,b,c),\\0,&\text{otherwise}.\end{cases}
\]
Then \(C_n(y)=\operatorname{tr}(M(y)^n)\) for every \(n\ge3\). Indeed closed transfer walks correspond bijectively to column-labelled cyclic words, with one factor of \(y\) for each selected complement vertex, and the local test holds at every vertex. Crucially, each cyclic word contributes once, not once per rotation.

**Exact determinant.** Six states of the transfer digraph lie on no directed cycle, so they contribute unit factors to \(\det(I-zM(y))\). The remaining directed-cycle states, indexed numerically by \(4a+b\), are \(0,3,5,7,10,11,12,13,14,15\). Expanding the determinant of the explicitly defined ten-state principal matrix gives the finite polynomial identity
\[
\det(I-zM(y))=P_2(z,y)P_5(z,y).
\]
This expansion is reproduced as an exact integer-coefficient, ten-row subset determinant in the accompanying verifier; it does not rely on a numerical eigensolver. For a matrix over the polynomial ring, the formal identity
\[
-z\,\frac{\partial}{\partial z}\log\det(I-zM)
=\sum_{n\ge1}\operatorname{tr}(M^n)z^n
\]
follows from the formal power series expansion of \(\log(I-zM)\). Together these identities establish the claimed two-variable generating function for every \(n\ge3\).

**Sparse top layers and growth.** Extracting \(y\)-coefficients of the displayed rational expression gives, in particular,
\[
[y^5]\sum_{n\ge1}C_n(y)z^n=2z^3(z^2+3),\qquad
[y^7]\sum_{n\ge1}C_n(y)z^n=2z^4(z^3+10z+4).
\]
Analogous rational coefficient extraction through \(y^9\), or the exactly specified determinant identity, yields the ten-term row displayed above for all \(n\ge10\). At \(y=1\), the nonzero transfer spectrum has characteristic factors \(t^2-t+1\) and \(t^5-3t^4+2t^3-2t^2+2t+1\). The ten-state cyclic transfer component is strongly connected and has self-loops, hence is primitive; Perron--Frobenius theory gives the simple strictly dominant positive eigenvalue \(\lambda\). The trace is the sum of eigenvalue powers, so its leading coefficient is exactly one.

## Verification
Run `python3 artifacts/verify.py` using only the Python standard library. It computes the ten-state determinant by exact signed subset expansion and checks its complete bivariate coefficient dictionary against the claimed product. Independently, for each \(3\le n\le8\), it enumerates all \(2^{2n}\) labelled vertex subsets, tests the original outside-neighbor definition directly on the prism's adjacency lists, and compares the entire cardinality distribution with the transfer recursion. It also verifies the sparse top-coefficient formulas for \(10\le n\le18\). The finite enumeration checks are diagnostics; the proof for unbounded \(n\) is the local correspondence and exact determinant.

## Relationship to prior work
Dourado, Grippo, Lin and Protti (arXiv:2603.04706, first public version 2026-03-05) establish general complexity and extremal facts about counting \(P_3\)-convex sets and derive an unweighted recurrence for paths. Their publicly accessible manuscript covers tree and threshold-graph algorithms and general exact counting, but does not supply this size-refined cyclic-prism polynomial or its two-factor determinant. Earlier work on \(P_3\) hull numbers of Cartesian graph products concerns minimum generating sets, not counting every convex set at every cardinality. The present result is a concrete exact specialization; no universal counting algorithm or general bounded-treewidth transfer method is claimed as new.

## Limitations
The theorem applies to unweighted two-row cyclic prisms only. The transfer determinant is a specialized finite computation, not a closed formula for arbitrary cubic or Cartesian-product graphs. Although exact to all lengths, the result is not a new complexity bound for general graphs. Potential differently named enumerations in bootstrap percolation or statistical-mechanics literature remain a historical-priority risk. No independent audit has been performed.

## References
1. M. C. Dourado, L. N. Grippo, M. C. Lin and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706, first posted 2026-03-05. https://arxiv.org/abs/2603.04706
2. E. M. M. Coelho et al., *On the \(P_3\)-hull number of some products of graphs*, Discrete Applied Mathematics (2018), DOI:10.1016/j.dam.2018.04.024. https://doi.org/10.1016/j.dam.2018.04.024
