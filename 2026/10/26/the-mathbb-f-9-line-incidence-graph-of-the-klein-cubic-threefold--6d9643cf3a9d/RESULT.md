# The \(\mathbb F_9\)-line incidence graph of the Klein cubic threefold

## Finding
Let \(X\subset\mathbb P^4_{\mathbb F_3}\) be the Klein cubic threefold defined by
\[
F(x_0,\ldots,x_4)=\sum_{i\in\mathbb Z/5\mathbb Z}x_i^2x_{i+1}=0.
\]
Construct the graph \(G_9\) having as vertices all projective lines \(L\subset X\) defined over \(\mathbb F_9\), with an edge for each pair of distinct lines having a geometric point in common. Then \(G_9\) is connected and has \(82\) vertices, \(350\) edges, and \(190\) three-cycles. Its degree distribution is
\[
\#\{L:\deg_{G_9}(L)=d\}=\begin{cases}5&d=4,\\20&d=6,\\15&d=8,\\32&d=10,\\10&d=12,\\0&\text{otherwise}.\end{cases}
\]
The \(10\) vertices defined over \(\mathbb F_3\) induce precisely \(C_5\sqcup5K_1\). The order-five coordinate shift fixes exactly two vertices of \(G_9\); the corresponding lines are skew, exchanged by the \(\mathbb F_3\)-Frobenius, and have degree \(10\).

## Assumptions and scope
All projective lines mean \(\mathbb F_9\)-rational two-dimensional vector subspaces of \(\mathbb F_9^5\), not just lines containing rational points. Intersection of two such lines is tested over an algebraic closure, equivalently by vector-space rank over \(\mathbb F_9\). The base field is exactly characteristic three, and the quadratic extension is represented by \(\mathbb F_3[\alpha]/(\alpha^2+1)\); the polynomial \(t^2+1\) is irreducible over \(\mathbb F_3\).

The cubic is smooth: its partial derivatives are \(2x_i x_{i+1}+x_{i-1}^2\). If one coordinate of a common gradient zero vanishes, the preceding coordinate also vanishes; iterating yields the zero vector, impossible projectively. If every coordinate is nonzero, putting \(u_i=x_i^2x_{i+1}\) gives \(2u_i+u_{i-1}=0\), whence all \(u_i\) are equal in characteristic three; on \(F=0\) their sum \(5u_i=2u_i\ne0\), a contradiction.

## Proof
Every two-dimensional subspace of \(\mathbb F_9^5\) has a unique reduced row-echelon \(2\times5\) matrix \((a;b)\). Such matrices are exhausted by choosing two pivot columns and assigning all permitted free entries one of the nine field elements. The number is
\[
{5\brack2}_9=\frac{(9^5-1)(9^5-9)}{(9^2-1)(9^2-9)}=605242.
\]
The line spanned by \(a,b\) lies on \(X\) precisely when the four coefficients of \(F(sa+tb)\) vanish. They are, with indices modulo five,
\[
\begin{aligned}
 c_{30}&=\sum_i a_i^2a_{i+1},\\
 c_{21}&=\sum_i\bigl(a_i^2b_{i+1}+2a_ib_ia_{i+1}\bigr),\\
 c_{12}&=\sum_i\bigl(b_i^2a_{i+1}+2a_ib_ib_{i+1}\bigr),\\
 c_{03}&=\sum_i b_i^2b_{i+1}.
\end{aligned}
\]
This necessary and sufficient test selects exactly \(82\) of the \(605242\) matrices. This finite count is independently checkable by the complete, deterministic `klein_q9_certificate.py` provided here; the script implements the nine-element field's addition and multiplication tables from its defining quotient, and iterates over every RREF matrix without randomness or sampling.

For each pair of the \(82\) selected matrices, the projective lines intersect exactly if the stacked four-row matrix has rank \(3\) (the rank is \(4\) if they are skew). Elementary row reduction over \(\mathbb F_9\) computes the \(82\times82\) symmetric adjacency relation. Exhausting the \(3321\) unordered pairs gives \(350\) edges and degree counts \(5,20,15,32,10\) at degrees \(4,6,8,10,12\), respectively. For each edge \(\{i,j\}\), count common neighbors; dividing the sum by \(3\) yields \(190\) triangles. Breadth-first search reaches every vertex. Restricting to matrices with entries in \(\mathbb F_3\) gives exactly \(10\) vertices, with one five-cycle and five isolates.

There is also a representation-theoretic explanation for the **exactly two** invariant lines. Let \(\sigma\) cyclically permute the five homogeneous coordinates. Since \(3\nmid5\), its five-dimensional permutation representation is semisimple. Over \(\mathbb F_9\), the polynomial \(T^5-1\) factors as the linear factor \(T-1\) and two distinct irreducible quadratic factors: \(\operatorname{ord}_5(9)=2\). Consequently there are exactly two \(\sigma\)-invariant two-planes \(W_+,W_-\) over \(\mathbb F_9\). After extending scalars to include a primitive fifth root \(\zeta\), the eigenweights on each of these planes are \(\zeta\) and \(\zeta^{-1}\) or \(\zeta^2\) and \(\zeta^{-2}\), respectively. All monomials of degree three on such a plane have nonzero \(\mathbb Z/5\)-weight, so no invariant homogeneous cubic restricts nontrivially to it. Thus \(F\) vanishes on both planes. The two modules are distinct direct summands of the permutation representation, so the corresponding lines are skew. Raising \(\zeta\) to the third power exchanges the two eigenweight pairs; thus Frobenius exchanges their lines. Their graph degrees are \(10\), computed by the same exhaustive adjacency test.

The graph construction and all counts are therefore exact finite algebra, not an extrapolation from sample points.

## Verification
Run `python3 klein_q9_certificate.py` in the same directory. The script uses only the Python standard library. It asserts the exact field operations, \(605242\) RREF matrices, \(82\) contained lines, \(350\) incidences, the complete degree histogram, \(190\) triangles, graph connectivity, the base-field induced graph, and the automorphism/Frobenius action. Its terminal output ends in `VERIFY_OK` only if every assertion passes. A fresh execution for this result returned `VERIFY_OK`.

## Relationship to prior work
Roulleau's geometric studies of the Klein cubic/Fano surface establish the intrinsic Fano geometry; Okazaki–Yamauchi determine its modularity and global cohomological L-function. These data, combined with the general Fano cohomology formula discussed by Roulleau, cover rational line **counts** over finite extensions in principle. They do **not** determine whether each specific pair of rational lines meets, the degree spectrum, the \(190\) triangles, or the two distinguished cyclically invariant rational lines. Bayar–Akça analyze the \(\mathrm{PG}(4,3)\) lines and related configurations, so the ten base-field lines and their induced five-cycle plus isolates are contextual rather than the main originality claim. This calculation concerns the entire quadratic-extension incidence graph and the invariant two-plane structure.

## Limitations
The result is a finite-field incidence description for one explicit characteristic-three model; it does not classify incidence schemes over arbitrary extensions or establish a new general theorem for Fano surfaces. The stated graph counts are verified by exhaustive exact RREF enumeration, whose code and tested assertions are supplied; no purely closed-form combinatorial derivation of the complete degree distribution is claimed. A specialized finite-geometric source expressing equivalent quadratic-extension data under another name could exist despite the literature comparisons. No independent scientific audit has been performed.

## References
1. X. Roulleau, *The Fano surface of the Klein cubic threefold*, arXiv:1001.4853 (first public arXiv version 2010-01-27).
2. T. Okazaki and T. Yamauchi, *On the modularity of the Klein cubic threefold*, arXiv:1008.2052 (2010).
3. X. Roulleau, *On the Fano surface of a smooth cubic threefold*, arXiv:1304.4076 (2013).
4. A. Bayar and Z. Akça, *A Note on k-Secant Lines of the Klein Cubic Threefold in PG(4,3)*, DOI:10.18185/erzifbed.1556681 (published 2025-12-31).
