# Exact odd chromatic number and optimal-coloring count for complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete \(r\)-partite graph with \(r\ge 2\) and every \(n_i\ge 1\). Let
\[
o=\left|\{i:n_i	ext{ is odd}\}ight|.
\]
For the neighborhood-parity odd chromatic number introduced by Petruševski and Škrekovski,
\[
\chi_o(G)=r+\max\{0,2-o\}.
\]
Thus a complete multipartite graph needs exactly its ordinary chromatic number when at least two parts have odd order, one extra color when exactly one part has odd order, and two extra colors when all parts have even order.

There is also an exact count of optimal color-class partitions, up to permutation of color names. Writing \(U(G)\) for that number,
\[
U(G)=
egin{cases}
1, & o\ge 2,\
\displaystyle\sum_{i:n_i	ext{ even}}2^{n_i-2}, & o=1,\
\displaystyle\sum_{1\le i<j\le r}2^{n_i+n_j-4}, & o=0.
\end{cases}
\]
Consequently, if the optimal palette has \(k=\chi_o(G)\) labeled colors and every color is required to be used, the number of optimal labeled odd colorings is \(k!\,U(G)\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The parts \(V_1,\ldots,V_r\) of \(K_{n_1,\ldots,n_r}\) are all nonempty, and \(r\ge2\), so every vertex is non-isolated. An odd coloring means a proper vertex coloring in which, for every vertex, some color occurs an odd number of times in its open neighborhood. The statement concerns this neighborhood-parity notion, not the unrelated use of “odd coloring” for partitions into odd induced subgraphs.

## Proof
In every proper coloring of a complete multipartite graph, a color can occur in at most one part, because vertices in distinct parts are adjacent. Call a part \(V_i\) **active** if at least one color class contained in \(V_i\) has odd cardinality.

Fix a vertex \(v\in V_i\). Its open neighborhood is exactly \(V(G)\setminus V_i\). Since colors used in different parts are disjoint, a color appears an odd number of times in \(N(v)\) exactly when it is an odd-sized color class in some part \(V_j\) with \(j
e i\). Hence all vertices of \(V_i\) satisfy the odd-neighborhood condition if and only if there is an active part distinct from \(V_i\).

Therefore a proper coloring is odd if and only if at least two parts are active. Indeed, two active parts suffice because every part has an active part outside it; conversely, if there are zero active parts then no vertex has an odd neighbor-color multiplicity, while if there is exactly one active part then vertices inside that part have no active part outside it.

If \(n_i\) is odd, every partition of \(V_i\) into color classes has at least one odd-sized class, because the sum of the class sizes is odd. Thus every odd-order part is automatically active, even when monochromatic. If \(n_i\) is even, a monochromatic \(V_i\) is inactive, while making it active requires at least two colors and two suffice: split \(V_i\) into classes of sizes \(1\) and \(n_i-1\), both odd.

Every proper coloring already needs at least one distinct color per part, so it needs at least \(r\) colors. If \(o\ge2\), two parts are automatically active and the monochromatic-per-part coloring is odd, giving \(\chi_o(G)=r\). If \(o=1\), exactly one more even part must be activated, costing one extra color, giving \(\chi_o(G)=r+1\). If \(o=0\), two even parts must be activated, costing two extra colors, giving \(\chi_o(G)=r+2\). This proves the formula for \(\chi_o(G)\).

For the enumeration, optimality forces exactly the minimum number of color classes. If \(o\ge2\), each part is monochromatic, yielding one color-class partition. If \(o=1\), exactly one even part \(V_i\) is split into two odd blocks. An even set of size \(n_i\) has \(2^{n_i-1}\) odd subsets, and complementary odd subsets define the same unordered bipartition, so there are \(2^{n_i-2}\) such splits. Summing over the even parts gives the middle formula.

If \(o=0\), the two extra color classes cannot both be placed in one part: then only that part could be active, which fails the odd condition on its own vertices. Hence two distinct parts \(V_i,V_j\) are each split into two odd blocks. Their choices are independent and contribute \(2^{n_i-2}2^{n_j-2}=2^{n_i+n_j-4}\). Summing over unordered pairs gives the final formula. Labeling the \(k\) color classes bijectively by a fixed \(k\)-color palette multiplies the unlabeled count by \(k!\).

## Verification
The proof is purely combinatorial and reduces the problem to the number of active parts. A standalone exhaustive checker in `verify.py` independently enumerates all colorings for every ordered part tuple with \(r\in\{2,3\}\), \(n_i\in\{1,2,3\}\), and at most seven vertices. It checks both minimality of the stated \(\chi_o\) and the exact labeled optimal-coloring count. The checker reports `ALL_CHECKS_PASSED cases=32`.

## Relationship to prior work
Petruševski and Škrekovski introduced neighborhood-parity odd coloring in arXiv:2112.13710 and the corresponding 2022 Discrete Applied Mathematics paper. Caro, Petruševski, and Škrekovski developed basic structural properties in arXiv:2201.03608. Dujmović, Morin, and Odak studied odd colorings of graph products in arXiv:2202.12882. Liu, Dou, and Yang later determined exact values for several Cartesian-product families in DOI:10.3934/math.2026056. The present theorem gives an exact baseline on the classical complete multipartite family and, in addition, enumerates all optimal color-class partitions.

For the bipartite specialization \(K_{m,n}\), the formula gives \(\chi_o=2\) when both \(m,n\) are odd, \(\chi_o=3\) when exactly one is even, and \(\chi_o=4\) when both are even, recovering \(\chi_o(C_4)=4\) from the foundational examples.

## Limitations
The result is specific to complete multipartite graphs and uses their rigid property that colors cannot be shared between distinct parts. It does not directly extend to arbitrary multipartite subgraphs. The novelty assessment is best-of-knowledge based on targeted current literature searches and corpus comparison; absence from those searches is not a proof that no equivalent statement exists in an unindexed or differently worded source. The exhaustive computation checks small instances only; the general theorem rests on the proof above.

## References
1. M. Petruševski and R. Škrekovski, *Colorings with neighborhood parity condition*, arXiv:2112.13710, first public version 27 December 2021; Discrete Applied Mathematics 321 (2022), 385–391, DOI:10.1016/j.dam.2022.07.018.
2. Y. Caro, M. Petruševski, and R. Škrekovski, *Remarks on odd colorings of graphs*, arXiv:2201.03608, 10 January 2022; Discrete Applied Mathematics 321 (2022), 392–401, DOI:10.1016/j.dam.2022.07.024.
3. V. Dujmović, P. Morin, and S. Odak, *Odd Colourings of Graph Products*, arXiv:2202.12882, 25 February 2022.
4. B. Liu, Q. Dou, and F. Yang, *The odd coloring of some Cartesian product graphs*, AIMS Mathematics 11 (2026), 1311–1331, DOI:10.3934/math.2026056.
