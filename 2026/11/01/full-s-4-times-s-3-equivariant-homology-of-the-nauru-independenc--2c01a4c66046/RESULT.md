# Full \(S_4\times S_3\)-equivariant homology of the Nauru independence complex

## Finding
Let \(G=GP(12,5)\) be the Nauru graph, and let \(K=\operatorname{Ind}(G)\) be its ordinary simplicial independence complex. Regard \(G\) as the Cayley graph on \(S_4\) with edges \(h\sim h(1\,i)\), for \(i\in\{2,3,4\}\). Its full automorphism group is \(S_4\times S_3\), where the action of \((a,b)\) on a vertex \(h\in S_4\) is \(h\mapsto ahb^{-1}\), with \(b\) fixing the letter \(1\).

Write \(P_4=\mathbb Q^4\) for the natural permutation module of \(S_4\), \(\varepsilon_4\) and \(\varepsilon_3\) for the sign characters of \(S_4\) and \(S_3\), and \(\boxtimes\) for the external tensor product. Then
\[
\boxed{\widetilde H_5(K;\mathbb Q)\cong(\varepsilon_4\otimes P_4)\boxtimes\varepsilon_3,\qquad
\widetilde H_6(K;\mathbb Q)\cong\varepsilon_4\boxtimes\mathbf1.}
\]
Every other reduced rational homology group vanishes. In Specht notation, the degree-five module is \((S^{(2,1,1)}\oplus S^{(1,1,1,1)})\boxtimes S^{(1,1,1)}\), and the degree-six module is \(S^{(1,1,1,1)}\boxtimes S^{(3)}\).

Consequently the full group fixes no nonzero reduced rational homology class, while its subgroup \(A_4\times A_3\) fixes precisely one dimension each in degrees \(5\) and \(6\). The ordinary quotient by the full group has vanishing positive rational homology and is connected, hence is rationally acyclic.

## Assumptions and scope
The graph has distinct vertices \(u_i,v_i\), with \(i\in\mathbb Z/12\mathbb Z\), and exactly the edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+5}\). A simplex of \(K\) is a subset of vertices containing no adjacent pair. Homology is ordinary reduced simplicial homology over \(\mathbb Q\), without particle configurations, graph edge matchings, or any alternate meaning of independence.

The displayed direct-product identification is fixed by an explicit Cayley labeling. The first factor acts by left multiplication on permutations and the second by inverse right multiplication. The factors are not interchangeable: their signs have different effects in the two homological degrees. The claim is specific to this graph; it does not assert an equivariant classification for all permutation star graphs.

## Proof
**1. Identification of the full group.** Label the vertices of the star Cayley graph by the 24 permutations of four letters. The map between its permutation-lexicographic vertex indices and the above generalized-Petersen indices is

`(0,18,22,8,4,14,12,6,10,20,16,2,17,7,11,13,21,3,5,19,23,1,9,15)`.

The standalone verifier checks each of the 36 undirected adjacencies under this map. Left multiplication by \(S_4\) preserves the generating-set Cayley edges. Right multiplication by \(S_3\) fixing letter \(1\) preserves them because it permutes the three generating transpositions by conjugation. These commuting actions produce 144 distinct graph automorphisms. For the reverse inequality, mark one vertex and distinguish its three neighbors. Successive neighbor-color refinements distinguish all 24 vertices after five rounds; hence an automorphism fixing the marked vertex and its neighbors pointwise is the identity. Thus the full automorphism group has at most \(24\cdot3!\) elements, proving the asserted equality.

**2. Rational homology concentration.** Enumerating independent subsets in the \(GP(12,5)\) presentation gives the nonempty face counts in dimensions \(0\) through \(11\):
\[
(24,240,1304,4212,8328,10036,7176,2964,752,156,24,2).
\]
On the augmented face poset, process vertices in increasing order and pair each remaining eligible lower face missing the current vertex with the face obtained by adjoining that vertex. This yields 17,605 pairs and exactly six unpaired five-simplices and three unpaired six-simplices. Orient a Hasse edge upward for each matched pair, downward otherwise. Direct topological sorting verifies that the resulting 35,219-node, 205,680-incidence directed graph is acyclic. Hence the reduced Morse chain complex has only six generators in degree five and three in degree six.

Eliminating matched signed incidences in ascending-vertex orientation produces the exact integral Morse boundary
\[
\partial_6=\begin{pmatrix}
1&1&0\\0&0&0\\0&0&0\\1&0&-1\\1&0&-1\\0&0&0
\end{pmatrix}.
\]
The first column is the second minus the third, and the minor on rows \(1,4\) and columns \(2,3\) has determinant \(-1\). The boundary therefore has rank two over \(\mathbb Q\); the reduced rational Betti numbers are \(4\) in degree five and \(1\) in degree six, and zero otherwise. The matching is not asserted to be equivariant; it is used solely to verify these dimensions.

**3. Exact reduced Lefschetz character.** Fix \((a,b)\in S_4\times S_3\) and let \(f(h)=ahb^{-1}\) permute the 24 graph vertices. Let \(\mathcal C_f\) be the collection of vertex-orbits of \(f\) whose union of vertices is an independent set of \(G\). A simplex fixed setwise by \(f\) is the union of a subset \(J\subseteq\mathcal C_f\) with independent union. If \(r=|J|\), the oriented simplex contributes \((-1)^{r+1}\) to the reduced alternating trace of the chain complex; this includes the empty face. The reduced simplicial Lefschetz formula therefore gives the exact character difference
\[
\Delta(a,b):=\operatorname{tr}(f_*|\widetilde H_6)-\operatorname{tr}(f_*|\widetilde H_5)
=-\sum_{\substack{J\subseteq\mathcal C_f\\\bigcup J\ \mathrm{independent}}}(-1)^{|J|}.
\]
This is a finite signed enumeration of stable orbit-unions, not an assumption about individual homology actions. It is invariant under conjugacy. Write the \(S_4\) cycle types in the order \((1^4),(2\,1^2),(2^2),(3\,1),(4)\) and the \(S_3\) cycle types in the order \((1^3),(2\,1),(3)\). Exhausting all 144 pairs and grouping by conjugacy produces
\[
\begin{array}{c|rrr}
& (1^3)&(2\,1)&(3)\\\hline
(1^4)&-3&5&-3\\
(2\,1^2)&1&-3&1\\
(2^2)&1&1&1\\
(3\,1)&0&2&0\\
(4)&-1&-1&-1
\end{array}.
\]

**4. Recovering the graded representations.** Use the ordinary character tables of \(S_4\) and \(S_3\). Exact character inner products, weighted by the reciprocal centralizer orders, yield
\[
\Delta=(\varepsilon_4\boxtimes\mathbf1)
-\bigl(S^{(2,1,1)}\boxtimes\varepsilon_3\bigr)
-(\varepsilon_4\boxtimes\varepsilon_3).
\]
Since \(\dim\widetilde H_6=1\), that homology must afford one of the four one-dimensional rational characters of \(S_4\times S_3\). Of these, only \(\varepsilon_4\boxtimes\mathbf1\) makes \(\chi_5=\chi_6-\Delta\) a nonnegative integral combination of irreducible characters. Therefore the latter equals \((S^{(2,1,1)}\oplus\varepsilon_4)\boxtimes\varepsilon_3\). As \(S^{(2,1,1)}\cong\varepsilon_4\otimes S^{(3,1)}\) and \(P_4\cong\mathbf1\oplus S^{(3,1)}\), the displayed representation formulas follow.

**5. Quotients.** The two displayed modules have no full-group invariant vector. Over \(\mathbb Q\), finite-group averaging after barycentric subdivision identifies the homology of the ordinary quotient with invariant homology. For \(A_4\times A_3\), both sign twists become trivial; the four-point permutation module has one invariant line, and the degree-six line is also invariant. This proves the asserted quotient/invariant consequences.

## Verification
Run `python3 verification/verify.py` using Python 3 and its standard library. It recomputes independent subsets, the full augmented matching and Hasse acyclicity, the signed integral Morse boundary, the explicit Cayley-to-Petersen isomorphism, the full group-order bound, all 144 reduced Lefschetz traces, and the fifteen exact rational character inner products. The recorded output is `verification/output.txt`, ending with `VERIFY_OK`.

The finite calculation is exhaustive: 35,219 augmented faces, 17,605 Morse pairs, 144 group elements, and fifteen conjugacy classes. The script needs neither a previously generated matrix nor an external database.

## Relationship to prior work
Barmak's 2010 star-cluster work establishes general suspension properties of triangle-free graph independence complexes, not an \(S_4\times S_3\)-equivariant homology character for this graph. Eppstein's 2007 description identifies the Nauru graph with the four-point permutation star Cayley graph and records its 144 automorphisms, but does not calculate homology. A published finite calculation establishes the nonequivariant Nauru homotopy type \(\bigvee^4S^5\vee S^6\). Its full result was inspected: the present result refines its two rational Betti numbers to the complete, distinct group representations, rather than reasserting the underlying wedge decomposition.

The signed Lefschetz enumeration is a standard tool, but neither that tool nor the nonequivariant sphere count determines the above multiplicities without the explicit full-group calculation. The identified comparisons do not imply the exact graded modules. An equivalent unindexed equivariant computation cannot be excluded by database searches.

## Limitations
This is a finite graph-specific equivariant result; no representation formula for all permutation-star Cayley graphs is proved. Rational representations are identified; no integral equivariant module splitting is claimed. The signed Morse incidence cancellation and finite character enumeration are certified by a standalone executable rather than a short closed-form case-free expression. Prior work's nonequivariant homotopy type is not claimed as new, and independent mathematical review has not been performed.

## References
1. D. Eppstein, *The many faces of the Nauru graph*, public post 2007-12-12. https://11011110.github.io/blog/2007/12/12/many-faces-of.html
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, publicly submitted 2010-07-02. https://arxiv.org/abs/1007.0418
3. *The Nauru independence complex is a wedge of four five-spheres and one six-sphere*, published result and executable finite proof, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-nauru-independence-complex-is-bigvee-4-s-5-vee-s-6--7c319734d8d8
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
