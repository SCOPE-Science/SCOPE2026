# Cuboctahedral dissociation homotopy and the complete octahedral homology character

## Finding

Let \(Q_3\) be the three-cube, \(C=L(Q_3)\) its cuboctahedral line graph, and \(X=\operatorname{Ind}_2(C)\) the two-independence (dissociation) simplicial complex. Then
\[
X\simeq\bigvee^{32}S^3.
\]
For the full automorphism group \(G=\operatorname{Aut}(C)\cong S_4\times C_2\), write \(V_\lambda\) for the rational Specht representation of \(S_4\) indexed by \(\lambda\vdash4\), and \(V_\lambda^\pm\) for its extension on which central inversion acts as \(\pm1\). The complete representation on reduced rational homology is
\[
\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong{}&
2V_{(4)}^+\oplus3V_{(3,1)}^+\oplus3V_{(2,2)}^+\oplus V_{(2,1,1)}^+\oplus V_{(1,1,1,1)}^+\\
&\oplus V_{(4)}^-\oplus V_{(3,1)}^-\oplus2V_{(2,2)}^-\oplus V_{(2,1,1)}^-.
\end{aligned}
\]
All other reduced homology groups vanish. In particular, the central-inversion eigenspaces have dimensions \(21\) and \(11\), and the quotient has
\[
\widetilde H_i(X/G;\mathbb Q)\cong\begin{cases}\mathbb Q^2,&i=3,\\0,&i\ne3.\end{cases}
\]

## Assumptions and scope

The cube has vertex set \(\{0,1,\ldots,7\}\) with its ordinary three-bit adjacency, and the cuboctahedral graph has twelve vertices, each the edge \(\{a,b\}\) of the cube with \(a\mathbin\oplus b\in\{1,2,4\}\). Distinct cuboctahedral vertices are adjacent if their cube edges share an endpoint. A face \(U\) belongs to \(X\) precisely when the induced graph \(C[U]\) has maximum degree at most one, equivalently each connected component has one or two vertices. Also equivalently, \(U\) contains none of the \(56\) forbidden triples \(\{v,a,b\}\) where \(a,b\) are distinct neighbors of \(v\) in \(C\). Thus \(X\) is the hypergraph independence complex of this natural forbidden-triple hypergraph. The empty set is a face but is not counted among nonempty cells.

## Proof

**Exact integral homotopy.** Index the twelve cube edges lexicographically as in the accompanying executable checker. A subset mask \(m\) is admitted exactly when every present vertex \(i\) satisfies \(\lvert N_C(i)\cap m\rvert\le1\). Exhaustive enumeration of all \(4096\) masks gives exactly \(455\) nonempty faces, with \(f\)-vector \((12,66,164,177,36)\). An independent forbidden-triple test gives precisely the same face set.

Apply sequential coordinate matchings in the exact edge-index order
\[
(2,10,4,6,7,3,11,9,5,8,0,1).
\]
At each stage match any still-unmatched face not containing coordinate \(v\) with its still-unmatched extension by \(v\), when that extension belongs to the complex. The standalone code explicitly constructs all \(211\) pairs, and orients the entire face-poset Hasse diagram downward except for paired cover relations, which are reversed. A topological-sort traversal visits all \(455\) vertices of this directed graph, with exactly \(1512\) cover incidences, proving that this is an acyclic matching. Its only unmatched simplices are one vertex and exactly \(32\) simplices of dimension three. The integral discrete Morse theorem constructs a homotopy-equivalent CW complex with one zero-cell and thirty-two three-cells and no cells of other positive dimensions. All attaching maps are forced to be constant, so it is the indicated wedge of three-spheres. This is an integral homotopy proof, independent of any field-homology computation.

**The full symmetry group.** Every cube automorphism has the form \(x\mapsto a\mathbin\oplus\pi(x)\), where \(a\) is a three-bit translation and \(\pi\in S_3\) permutes bit coordinates; there are \(8\cdot6=48\) such maps. The eight maximal triangular cliques of \(C\) are exactly the three edges incident at each cube vertex. Their intersection graph recovers \(Q_3\), proving that every automorphism of \(C\) comes from a cube automorphism. The four unoriented cube body diagonals carry a faithful rotation-group action \(S_4\); the central antipodal transformation \(x\mapsto x\mathbin\oplus7\) gives the complementary \(C_2\) factor. Write \(\delta(g)=\det(g)\in\{+1,-1\}\), in the geometric signed-permutation representation, to indicate the central factor.

**Rational character.** For any graph automorphism \(g\), its simplicial Lefschetz number is the signed sum over its setwise-fixed nonempty faces: each fixed face contributes \((-1)^{\dim F}\) times the sign of the permutation that \(g\) induces on that face's ordered vertices. Since \(X\) has only \(H_0\cong\mathbb Q\) and \(\widetilde H_3\cong\mathbb Q^{32}\), the degree-three trace is \(\chi_3(g)=1-L(g)\). The checker evaluates all \(48\) maps, grouping by the cycle type of the permutation of four body diagonals and by \(\delta\). The computed values are:

| Diagonal cycle type | Class size for each \(\delta\) | \(\chi_3\) for \(\delta=+1\) | \(\chi_3\) for \(\delta=-1\) |
| --- | ---: | ---: | ---: |
| \((1,1,1,1)\) | 1 | 32 | 10 |
| \((2,1,1)\) | 6 | 4 | 2 |
| \((2,2)\) | 3 | 8 | 2 |
| \((3,1)\) | 8 | -1 | 1 |
| \((4)\) | 6 | 0 | -2 |

Taking ordinary rational character inner products with the five \(S_4\) irreducibles, separately for the two central signs, gives multiplicities \((2,3,3,1,1)\) for the even part and \((1,1,2,1,0)\) for the odd part, in the partition order \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\). Their dimensions sum to \(21+11=32\), as required.

Finally, barycentric subdivision makes the finite simplicial group action admissible. Over \(\mathbb Q\), finite-group coinvariants are exact, so the rational homology of the orbit complex is the invariant part of the homology of \(X\). The representation contains two trivial even constituents, giving the quotient calculation.

## Verification

Run the packaged standard-library Python program with `python3 checks/cubocta_dissociation_verify.py`. It implements both simplex-membership criteria, the exact matching and complete acyclicity test, an independent computation of mod-two boundary ranks, all \(48\) full-group simplicial maps, signed fixed-face Lefschetz numbers, and character inner products. The expected records, saved in `checks/replay_output.txt`, include the \(f\)-vector, \(211\) matching pairs, \(33\) critical cells, \(1512\) Hasse incidences, mod-two boundary ranks \((11,55,109,36)\), all ten rational character values, and `ALL_CHECKS_PASS`. No external Python packages, databases, stochastic choices, or previously computed chains are required.

## Relationship to prior work

Conant and Thistlethwaite [1] define hypergraph independence complexes (Definition 3) and sequential acyclic discrete vector fields (Section 4), treating cube-face hypergraphs and Alexander-dual theta complexes. The present hypergraph has as vertices **cube edges**, and its forbidden triples are incident-edge triples or paths in their line graph; it is not the cube-vertex face hypergraph investigated in [1]. Deshpande and Singh [2] develop two-independence topology for complete multipartite, fully whiskered, path, cycle and perfect-ary-tree graph families, and give the sequential matching theorem. The cuboctahedral line graph is none of these. The dissociation-set literature [3] studies maximum induced degree-one vertex sets; an optimization result alone does not determine the topology or its symmetry representation. Related computations of the ordinary matching complex of the cuboctahedron and of its cut and distance complexes concern different definitions and do not imply the results here. No definitive exhaustive publication-priority claim is made.

## Limitations

Only this single finite graph and the parameter two are classified. The representation is determined over \(\mathbb Q\), not as an integral group-module lattice. The integral torsion and homotopy type of the quotient are not determined. The computational proof is exhaustive for the explicitly defined \(455\)-face complex, but it does not constitute a uniform theorem for other line graphs or polyhedra. An equivalent unpublished or unindexed calculation may exist; independent mathematical validation has not been performed.

## References

[1] J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, first submitted 2008-08-05, arXiv:0808.0739, especially Definitions 1–3 and Sections 4–6. https://arxiv.org/abs/0808.0739

[2] P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, first submitted 2020-01-15, arXiv:2001.05448, especially Sections 2–5. https://arxiv.org/abs/2001.05448

[3] Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366, doi:10.1016/j.dam.2011.04.023. https://doi.org/10.1016/j.dam.2011.04.023
