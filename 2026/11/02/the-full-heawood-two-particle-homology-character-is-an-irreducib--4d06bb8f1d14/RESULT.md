# The full Heawood two-particle homology character is an irreducible six plus the graph-cycle eight
## Finding
Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane, let \(B_2(H)=\operatorname{UConf}_2(|H|)\), and let \(G=\operatorname{Aut}(H)\cong\operatorname{PGL}_2(7)\) act by moving both unordered particles. Put \(W=H_1(|H|;\mathbb Q)\), the eight-dimensional graph-cycle representation. Then there exists a six-dimensional **absolutely irreducible rational** representation \(E\) such that
\[
H_1(B_2(H);\mathbb Q)\cong W,\qquad H_2(B_2(H);\mathbb Q)\cong W\oplus E.
\]
Both \(W\) and \(E\) are irreducible and nonisomorphic as rational and complex representations of the full group of order \(336\). The character of \(E\) is uniquely specified by the following complete conjugacy-class table (the two final rows are distinct classes). A \(1\) in the duality column means that an automorphism interchanges points and lines.

| Element order | Class size | Duality | \(\chi_W\) | \(\chi_E\) | \(\chi_{H_2}\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | 8 | 6 | 14 |
| 2 | 21 | 0 | 0 | -2 | -2 |
| 2 | 28 | 1 | -2 | 0 | -2 |
| 3 | 56 | 0 | -1 | 0 | -1 |
| 4 | 42 | 0 | 0 | 2 | 2 |
| 6 | 56 | 1 | 1 | 0 | 1 |
| 7 | 48 | 0 | 1 | -1 | 0 |
| 8 | 42 | 1 | 0 | 0 | 0 |
| 8 | 42 | 1 | 0 | 0 | 0 |

In integral homology, \(H_1(B_2(H);\mathbb Z)\cong\mathbb Z^8\oplus\mathbb Z/2\), \(H_2(B_2(H);\mathbb Z)\cong\mathbb Z^{14}\), and there is no positive-degree homology above degree two. The torsion phenomenon in first graph-braid homology is covered by earlier general work and is not the novelty claimed here.

The rational quotient Betti vectors in degrees \(0,1,2\) are \((1,0,0)\) for the full \(G\), \((1,2,2)\) for a seven-cycle subgroup, and \((1,3,6)\) for a point-line polarity involution. The distinguishing contribution is the **complete full-group homology character**, not a nonequivariant rank alone.

## Assumptions and scope
Identify the seven Fano points and seven line normals with nonzero vectors \(p,n\in\mathbb F_2^3\), with an incidence edge when \(p\cdot n=0\). Take points numbered \(0,\ldots,6\), then lines numbered \(7,\ldots,13\). Every graph edge is oriented from its point to its line. The point-line polarity sends \(p\) to line \(p\) and vice versa. A linear map \(A\in\mathrm{GL}_3(\mathbb F_2)\) acts by \(p\mapsto Ap\) and \(n\mapsto (A^{-1})^Tn\); these and polarity give all \(336\) automorphisms. The homology is ordinary singular homology of the unordered **two-point** configuration space, not Borel–Moore, sign-local-system, or ordered configuration homology. Coefficients are \(\mathbb Q\) for representations and \(\mathbb Z\) for the stated abelian groups.

## Proof
**1. Finite and functorial cell model.** The Heawood graph is simple, connected, cubic, and of girth \(6\), hence satisfies the two-point sufficient-subdivision conditions of the Abrams–Prue–Scrimshaw model. Its unordered configuration space deformation retracts onto the finite cubical complex with cells consisting of unordered pairs of graph cells with disjoint closures. Its zero-cells are unordered distinct graph vertices; its one-cells consist of an oriented graph edge together with a vertex not on that edge; its two-cells consist of unordered pairs of edges with disjoint endpoints. The chain-group ranks are
\[
(\operatorname{rank} C_0,\operatorname{rank} C_1,\operatorname{rank} C_2)=(91,252,168).
\]
If an oriented edge is \(e=[u,v]\), the one-cell \((e,w)\) has boundary \((v,w)-(u,w)\). For disjoint oriented edges \(e=[u,v]\) and \(f=[a,b]\), ordered by fixed edge index, the two-cell \((e,f)\) has boundary
\[
(f,v)-(f,u)-(e,b)+(e,a).
\]
These orientations define integer matrices \(d_1,d_2\) with \(d_1d_2=0\). The action of a graph automorphism on edge factors carries the endpoint-orientation signs, and reordering the two edges in a square contributes the additional Koszul sign.

**2. Exact ranks and integral groups.** The cubical one-skeleton is connected, so \(\mathrm{rank}\,d_1=90\). Exact integral unimodular row/column elimination on \(d_2\) produces \(153\) unit Smith factors, followed by a remaining rank-one matrix all of whose entries are \(0\) or \(\pm2\) and with entry gcd equal to \(2\). Its Smith nonzero factors are therefore \(153\) copies of \(1\) and one \(2\), giving \(\mathrm{rank}\,d_2=154\). Since \(C_3=0\), the integral second homology is the free rank-\(14\) kernel of \(d_2\). The first homology is free of rank \(252-90-154=8\) with a single order-two summand; this uses that \(\mathrm{im}\,d_1\) is free, hence the torsion of \(\mathrm{coker}\,d_2\) equals that of \(\ker d_1/\mathrm{im}\,d_2\).

**3. Identify the degree-one representation.** There is a natural \(G\)-equivariant chain map from the cubical configuration complex to the graph chain complex: on vertices, \(\{u,v\}\mapsto u+v\); on a one-cell \((e,w)\), send it to its oriented edge \(e\); and send every two-cell to zero. This commutes with boundaries because each square's two moving-edge contributions cancel. The exact augmented rank computation \(\mathrm{rank}[d_1;P_1]-\mathrm{rank}d_1=8\) shows that the induced image in graph first homology has rank eight. Both groups have rational rank eight, so this induces the claimed \(G\)-equivariant isomorphism in degree one.

**4. Compute the full degree-two character.** For each of all \(336\) symmetries \(g\), count graph vertices and signed fixed graph edges to obtain \(\chi_W(g)=1-\operatorname{tr}(g\mid C_0(H))+\operatorname{tr}(g\mid C_1(H))\). Independently enumerate fixed configuration zero-cells, signed fixed one-cells, and signed fixed squares. Their alternating trace is the Lefschetz number \(L(g)\), so the only potentially nonzero homology degrees give
\[
\chi_{H_2}(g)=L(g)-1+\chi_W(g).
\]
Conjugacy grouping under all generated permutations produces the nine classes and exact character table in the finding. This enumerates every group element, not just selected generators.

**5. Irreducibility and quotient consequences.** The finite-group character inner product is \(\langle\chi,\psi\rangle=|G|^{-1}\sum_g\chi(g)\psi(g)\). The table gives
\[
\langle\chi_W,\chi_W\rangle=1,\quad
\langle\chi_{H_2},\chi_W\rangle=1,\quad
\langle\chi_{H_2}-\chi_W,\chi_{H_2}-\chi_W\rangle=1.
\]
Thus \(W\) is irreducible, occurs exactly once in degree two, and its complementary six-dimensional character is another irreducible. The values are integral and arise from actual rational chain actions, hence the decomposition is over \(\mathbb Q\). Neither positive-degree character has a trivial summand. For any finite-group action, rational homology of the orbit space is the invariant part of homology. Character averages give respectively \((b_1,b_2)=(0,0)\), \((2,2)\), and \((3,6)\) for the full group, a subgroup of order seven, and the displayed polarity.

## Verification
Run `python3 HEAWOOD_CHECK.py` from the package directory using standard-library Python 3.9 or newer. The checker reconstructs all signed boundary columns, confirms \(d_1d_2=0\), computes ranks modulo two and three, performs actual unimodular integer elimination through \(153\) unit pivots and verifies the final rank-one order-two block. It verifies the graph projection has full eight-dimensional image, independently generates all \(336\) automorphisms and nine conjugacy classes, checks their signed traces element by element, proves the stated inner-product equalities, and checks all quotient dimensions. Exact result marker: `HEAWOOD_2CONFIG_FULL_336_CHARACTER_AND_INTEGRAL_SMITH_OK`. No numerical approximation, randomized enumeration, or external mathematical software is needed.

## Relationship to prior work
Ko and Park's general first-homology description already explains the characteristic two torsion of graph braid groups; no new general torsion theorem is asserted. Abrams–Prue–Scrimshaw and Alvarado-Garduño–González provide the discrete cell-model equivalence, not this character table. An and Knudsen (first posted August 24, 2020) give degree-two generation results for **planar** graphs and a nonplanar counterexample; their theorem does not determine the Heawood space, which is nonplanar. Existing indexed calculations for the ordered Heawood two-point mod-two homology (ranks \(16\) and \(29\)) and for twisted Borel–Moore unordered graph configurations concern different homology theories and do not imply this ordinary rational \(G\)-module classification. A published Heawood matching-complex homology representation concerns a different simplicial space. The comparison is about mathematical statements, not keyword overlap.

## Limitations
Only two **unordered** particles on the fixed Fano-plane incidence graph are treated. The decomposition concerns rational representations, not an explicit integral splitting of the rank-fourteen top lattice. The integral groups and finite characters are exact; no cup-product or higher-particle representation is claimed. Published broad topological frameworks can motivate or in principle compute related groups but do not supply the explicit full-group character table in the material inspected. An unindexed equivalent calculation remains a bibliographic risk, and no independent external audit has been performed.

## References
1. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first version August 24, 2020), particularly Theorem 1.1 and Example 6.8. https://arxiv.org/abs/2008.10371
2. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648 (first version January 13, 2011), especially Theorem 3.16. https://arxiv.org/abs/1101.2648
3. O. Alvarado-Garduño and J. González, *Abrams' stabilization theorem for no-k-equal configuration spaces on graphs*, arXiv:2407.07854 (July 10, 2024), Theorem 1.2. https://arxiv.org/abs/2407.07854
4. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (2009). https://arxiv.org/abs/0909.5511
