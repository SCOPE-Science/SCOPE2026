# Cycle-divisibility determinant characters of isolated rooted-forest complexes

## Finding
For every integer \(m\ge 3\), let \(Y_m\) have as vertices the ordered arcs \((u,v)\) with \(u,v\in[m]\), \(u\ne v\). Its faces are exactly the sets of arcs forming a directed rooted forest (each vertex has at most one incoming arc and there are no directed cycles), **and having at least one isolated vertex** in the underlying undirected forest. Coordinate relabeling makes \(Y_m\) an \(S_m\)-complex.

If a permutation \(g\in S_m\) has cycle lengths \(\lambda_1,\ldots,\lambda_c\), label the cycles by \([c]\). For any \(I\subseteq[c]\), form a weighted Laplacian \(L_I=(l_{ij})_{i,j\in I}\) by
\[
 l_{ij}=\begin{cases}-\lambda_j,&i\ne j\text{ and }\lambda_j\mid\lambda_i,\\0,&i\ne j\text{ and }\lambda_j\nmid\lambda_i,\end{cases}
 \qquad l_{ii}=\sum_{j\in I\setminus\{i\},\,\lambda_j\mid\lambda_i}\lambda_j.
\]
Interpret the determinant of a zero-by-zero matrix as one. The **complete rational homology character** is
\[
\boxed{\operatorname{tr}\bigl(g\mid\widetilde H_{m-3}(Y_m;\mathbb Q)\bigr)
=(-1)^{m-2}\sum_{\varnothing\ne J\subseteq[c]}(-1)^{|J|+1}\det\bigl(\mathbf1-L_{[c]\setminus J}\bigr).}
\]
All other reduced rational homology groups vanish. The dimension is
\[
\dim\widetilde H_{m-3}(Y_m;\mathbb Q)=m-1+\sum_{j=2}^{m-1}\binom mj(j-1)^{j-1}.
\]
This finite determinant expression depends only on the cycle type of \(g\), hence determines the complete rational \(S_m\)-module character. For example, when \(m=4\), its values on the conjugacy classes of types \((1,1,1,1)\), \((2,1,1)\), \((2,2)\), \((3,1)\), and \((4)\) are respectively \(25,-3,1,1,1\). For an \(m\)-cycle the value is \((-1)^{m-2}\).

## Assumptions and scope
A directed rooted forest is a directed graph that has no directed cycle and for which each non-root vertex has exactly one incoming edge, with roots having none. The empty arc set is a face. “Isolated” requires neither incoming nor outgoing arcs; being merely a root is not enough. All vertex labels, all permutations, and every integer \(m\ge3\) are included. There is no assumption on the lengths or multiplicities of the permutation cycles.

This is the canonical vertex–edge-pair subcomplex called \(Y_n\) (with \(m=n+1\)) in Theorem 9.5 of Knudson and Owens–White [1]. Its rational representation is the subject here. No claim of an equivariant collapse or an equivariant representation identity for the full strong matching complex is made.

## Proof
**Homological degree.** Theorem 9.5 of [1] identifies the indicated isolated-forest complex and proves that it has the homotopy type of a wedge of spheres in degree \(m-3\). Its integral reduced homology is therefore free and concentrated in that degree. On rewriting the number of spheres given there with \(n=m-1\), one obtains the stated dimension. The remaining proof computes the action, not merely the dimension.

**Fixed forests as forests of permutation cycles.** Write a directed forest by its parent map \(p:[m]\to[m]\cup\{\bot\}\): a root has parent \(\bot\), and any other vertex \(v\) has an arc \((p(v),v)\). Invariance under \(g\) is equivalent to \(p(gv)=g p(v)\). Consequently a whole cycle \(i\) of length \(\lambda_i\) consists either of roots or of non-roots whose parents lie on a single cycle \(j\). In the latter case necessarily \(\lambda_j\mid\lambda_i\), and there are exactly \(\lambda_j\) equivariant parent maps between these two distinct cycles. A cycle cannot use itself as its parent-cycle: such a map creates an ordinary directed cycle. More generally, directed acyclicity of the original parent map is equivalent to acyclicity of the resulting parent graph on cycle indices. For if a quotient directed cycle exists, composing its finitely many equivariant phase maps eventually returns to its starting original vertex; conversely a directed cycle in the original forest projects to a directed closed walk and hence to a quotient cycle.

Thus invariant rooted forests are weighted rooted forests of a directed graph on \([c]\), with possible edge \(i\to j\) of weight \(\lambda_j\) precisely when \(i\ne j\) and \(\lambda_j\mid\lambda_i\). The orientation is toward the root of each component.

**Signed Lefschetz weights.** If the quotient forest has \(s\) non-root cycle indices, the induced permutation on the arc vertices of the corresponding simplex has one orbit of length \(\lambda_i\) for each non-root index \(i\). Combining the simplicial sign \((-1)^{|E|}\) and the orientation sign of the action on arcs gives
\[
(-1)^{\sum_{i\text{ non-root}}\lambda_i}
\prod_{i\text{ non-root}}(-1)^{\lambda_i-1}=(-1)^s.
\]
The augmented signed Lefschetz number therefore equals the negative of the sum of these weights, including the empty face.

**The determinant and the isolated-vertex restriction.** For any subset \(I\) of quotient vertices, the directed matrix–forest theorem applied with signed edge weights \(-\lambda_j\) shows that
\[
\det(\mathbf1-L_I)=\sum_{F\text{ rooted quotient forest on }I}(-1)^{|E(F)|}\prod_{i\to j\in F}\lambda_j.
\]
One direct proof adjoins a sink with a unit-weight edge from every quotient vertex to the sink and applies the directed matrix–tree determinant expansion; deleting sink edges identifies its arborescences with rooted forests and preserves the weights. Negative weights are valid since this is a polynomial identity.

A vertex isolated in an invariant original forest occurs with every vertex of its \(g\)-cycle isolated, and a cycle-index vertex is isolated exactly when it has no incoming and no outgoing edge in the quotient forest. To impose **at least one isolated cycle index**, perform inclusion–exclusion over all nonempty subsets \(J\subseteq[c]\) forced to be isolated. The remaining forest lies wholly on \([c]\setminus J\), so its weighted sum is exactly \(\det(\mathbf1-L_{[c]\setminus J})\). This proves that the augmented Lefschetz number is
\[
\widetilde\Lambda(g;Y_m)=-\sum_{\varnothing\ne J\subseteq[c]}(-1)^{|J|+1}\det(\mathbf1-L_{[c]\setminus J}).
\]
By the first paragraph, only reduced degree \(m-3\) survives; the simplicial Lefschetz identity therefore gives \(\widetilde\Lambda(g;Y_m)=(-1)^{m-3}\operatorname{tr}(g\mid\widetilde H_{m-3}(Y_m;\mathbb Q))\). Rearrangement yields the boxed formula for every permutation. Characteristic-zero semisimplicity then guarantees that these traces determine the rational module up to isomorphism.

## Verification
The standalone standard-library program `verify.py` constructs all rooted forests by enumerating acyclic parent maps, filters for an isolated original vertex, and computes signed fixed-simplex Lefschetz traces without using cycle-divisibility determinants. A second routine evaluates the closed formula by exact integer Bareiss determinants. It compared all conjugacy-class representatives for \(m=3,4,5,6\) and four further representatives for \(m=7\), totaling 30 cases. It also computed the augmented mod-two simplicial boundary ranks for \(m=3,4,5\), finding top reduced Betti numbers \(5,25,189\) and no other reduced homology in those cases. Execution from the packaged file returned `VERIFY_OK`. The calculations are finite checks of a theorem proved uniformly above.

## Relationship to prior work
Knudson and Owens–White [1, Theorem 9.5] construct this subcomplex and determine its nonequivariant sphere-wedge homotopy type and rank. The present character formula uses the same object but distinguishes permutation actions whose Betti numbers agree. Kozlov [2] studies complexes of directed trees; Bernardi and Klivans [3] develop rooted-forest matrix-tree enumeration. The determinant identity for weighted quotient cycle forests is used here as an input to a new signed equivariant Lefschetz calculation with the *isolated-vertex* condition. Deshpande and Sawant [4] study directed **linear** forests, a different facial condition. No checked source establishes the displayed all-cycle-type homology character. Equivalence to an unindexed calculation remains possible.

## Limitations
The theorem concerns the canonical isolated-vertex rooted-forest **subcomplex** and rational homology representations. It does not establish an equivariant equivalence with the full strong discrete Morse matching complex, integral module decompositions, or equivariant homotopy splittings. The character formula is exact but not simplified into explicit Specht multiplicities for general \(m\); those can in principle be recovered from standard character tables. Its originality comparison is bounded by accessible literature, and independent audit has not occurred.

## References
[1] Kevin P. Knudson and Abigail Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844, first posted 2026-09-06, especially Section 9 and Theorem 9.5. https://arxiv.org/pdf/2609.06844

[2] Dmitry N. Kozlov, *Complexes of Directed Trees*, Journal of Combinatorial Theory A 88 (1999), 112–122, DOI:10.1006/jcta.1999.2984.

[3] Olivier Bernardi and Caroline J. Klivans, *Directed Rooted Forests in Higher Dimension*, Electronic Journal of Combinatorics 23(4), P4.35 (2016), arXiv:1512.07757. https://arxiv.org/html/1512.07757v4

[4] Priyavrat Deshpande and Rutuja Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936, 2026-02-16. https://arxiv.org/abs/2602.14936
