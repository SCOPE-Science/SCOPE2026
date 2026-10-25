# A characteristic-two homology jump for three particles on \(K_{3,3}\)

## Finding

Let \(X=\operatorname{UConf}_3(|K_{3,3}|)\) be the space of unordered configurations of three pairwise distinct points on the geometric complete bipartite graph \(K_{3,3}\). Its rational Betti vector is

\[
(\dim_{\mathbb Q}H_i(X;\mathbb Q))_{i=0}^3=(1,4,8,0),
\]

whereas its mod-two Betti vector is

\[
(\dim_{\mathbb F_2}H_i(X;\mathbb F_2))_{i=0}^3=(1,5,9,0).
\]

Consequently, the finitely generated abelian group \(H_1(X;\mathbb Z)\) has exactly one cyclic 2-primary torsion summand, while \(H_2(X;\mathbb Z)\) has no 2-primary torsion. The exponent of the 2-primary summand in \(H_1\), and any odd-primary torsion, are not determined here.

## Assumptions and scope

The graph is the one-dimensional CW complex \(|K_{3,3}|\), with six original vertices and nine edges. Configurations are unordered and collision-free. Homology coefficients are either \(\mathbb Q\), \(\mathbb F_2\), or \(\mathbb Z\) as explicitly indicated. The claim concerns three particles only; it does not assert a formula for \(\operatorname{UConf}_n(|K_{3,3}|)\) at other values of \(n\), nor does it determine the full integral homology groups.

## Proof

Subdivide each of the nine edges of \(K_{3,3}\) once. The resulting graph has 15 vertices and 18 edges. Each path between distinct essential vertices has length at least two edges, and each cycle has length at least eight. Thus the standard discretized cubical configuration model applies for three particles: its cells are unordered sets of three vertices or open edges whose closures are pairwise disjoint, and it is homotopy equivalent to \(X\).

A \(k\)-cell is specified by \(k\) edges with pairwise disjoint endpoints and \(3-k\) vertices outside those endpoints. Direct enumeration gives the chain-group ranks

\[
(C_0,C_1,C_2,C_3)=(455,1404,1386,432).
\]

Orient every edge from its lower-numbered endpoint to its higher-numbered endpoint, and orient a product cell by increasing edge index. The boundary of a cell with ordered edge factors \(e_1,\ldots,e_k\) is the alternating sum of the endpoint faces, with the usual endpoint signs. The accompanying standalone script enumerates these cells, constructs the integer boundary matrices, and checks \(\partial_{k-1}\partial_k=0\) over \(\mathbb Z\).

Exact sparse elimination using rational arithmetic gives

\[
(\operatorname{rank}_{\mathbb Q}\partial_1,\operatorname{rank}_{\mathbb Q}\partial_2,\operatorname{rank}_{\mathbb Q}\partial_3)=(454,946,432).
\]

Exact elimination over \(\mathbb F_2\) gives

\[
(\operatorname{rank}_{\mathbb F_2}\partial_1,\operatorname{rank}_{\mathbb F_2}\partial_2,\operatorname{rank}_{\mathbb F_2}\partial_3)=(454,945,432).
\]

Subtracting adjacent boundary ranks from the chain-group ranks yields the two Betti vectors stated above. Both calculations give Euler characteristic \(5\), matching the alternating sum of the cell counts. Finally, the universal coefficient theorem gives

\[
\dim_{\mathbb F_2}H_i(X;\mathbb F_2)=\dim_{\mathbb Q}H_i(X;\mathbb Q)+t_2(H_i(X;\mathbb Z))+t_2(H_{i-1}(X;\mathbb Z)),
\]

where \(t_2(A)\) is the number of cyclic 2-primary summands of a finitely generated abelian group \(A\), and \(t_2(H_0)=0\). The degree-one difference is one, so \(t_2(H_1)=1\). The degree-two difference is also one, which then forces \(t_2(H_2)=0\). The calculation does not determine the exponent of the summand in \(H_1\).

## Verification

The reproducibility artifact is `artifacts/verify_k33.py`. It uses only the Python standard library, exact `Fraction` arithmetic for ranks over \(\mathbb Q\), and integer bitsets for ranks over \(\mathbb F_2\). The script checks the cell counts, all three boundary ranks over each coefficient field, the integral chain condition, the Betti vectors, and the Euler characteristic. Its expected terminal line is `VERIFY_OK`.

## Relationship to prior work

Published work on graph configuration spaces provides the discretized cubical model and discrete-Morse methods for graph braid spaces. The two-particle study of Barnett and Farber includes the complete bipartite graph \(K_{3,3}\), but its explicit calculations concern two particles and its cohomology-algebra theorem is for planar graphs. The present claim concerns three unordered particles on the nonplanar graph \(K_{3,3}\). The general discrete-Morse treatment of Farley and Sabalka provides methods and dimension bounds, rather than this specific coefficient-field comparison. The exact computation below is therefore a finite, object-specific benchmark, not a claim of a general formula.

## Limitations

No Smith normal form is computed. In particular, the exponent of the unique 2-primary summand in \(H_1(X;\mathbb Z)\) is unknown here, and no conclusion is made about odd-primary torsion. The result does not determine the integral homology groups completely, the cohomology ring, the homotopy type, or the behavior for any other particle count. The novelty assessment is limited to the literature and database comparisons recorded in the accompanying review metadata; an unlocated computation may exist.

## References

1. K. Barnett and M. Farber, “Topology of configuration space of two particles on a graph, I,” *Algebraic & Geometric Topology* 9 (2009), 593–624. First public version: arXiv:0903.2180, 12 March 2009. DOI: 10.2140/agt.2009.9.593.
2. D. Farley and L. Sabalka, “Discrete Morse theory and graph braid groups,” *Algebraic & Geometric Topology* 5 (2005), 1075–1109. arXiv:math/0410539.
3. P. Prue and T. Scrimshaw, “Abrams’s stable equivalence for graph braid groups,” arXiv:0909.5511, 30 September 2009.
4. B. H. An, G. C. Drummond-Cole, and B. Knudsen, “Subdivisional Spaces and Graph Braid Groups,” *Documenta Mathematica* 24 (2019), 1513–1583. DOI: 10.4171/DM/709.
