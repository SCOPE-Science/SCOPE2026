# Elementwise fixed-point topology of the seven-by-seven torus Rips three-sphere

## Finding

Let \(T=(\mathbb Z/7\mathbb Z)^2\), with metric
\[
d((x,y),(u,v))=\min(|x-u|,7-|x-u|)+\min(|y-v|,7-|y-v|),
\]
where the coordinate differences are taken in \(\{0,\ldots,6\}\). Let \(K=\operatorname{VR}_{\le4}(T)\), the flag simplicial complex of subsets with pairwise distances at most four. Its coordinate-dihedral symmetry group is \(G=(D_7\times D_7)\rtimes C_2\), of order \(392\), where the final involution exchanges coordinates. For every \(g\in G\), the geometric fixed-point space \(|K|^{\langle g\rangle}\) is classified as follows.

Write \(I\) for the identity transformation of one cyclic coordinate, \(R\) for any nonidentity rotation, and \(F\) for any reflection. For an element acting separately on the two coordinates, the **unordered** pair of types determines its fixed-point homotopy type:

| Coordinate types | Geometric fixed-point homotopy type |
| --- | --- |
| \((I,I)\) | \(S^3\) |
| \((I,R)\) | \(S^1\) |
| \((R,R)\) | empty |
| \((I,F)\) | \(S^2\) |
| \((R,F)\) | \(S^0\) |
| \((F,F)\) | \(S^1\) |

For a coordinate-exchanging element
\[
g(x,y)=(\varepsilon_1y+a,\varepsilon_2x+b),\qquad
\varepsilon_1,\varepsilon_2\in\{1,-1\},\quad a,b\in\mathbb Z/7\mathbb Z,
\]
let \(h(t)=\varepsilon_1\varepsilon_2t+\varepsilon_1b+a\), the action of \(g^2\) on the first coordinate. Then \(|K|^{\langle g\rangle}\) has type \(S^1\) if \(h=I\), is empty if \(h=R\), and has type \(S^0\) if \(h=F\). These cases exhaust the \(392\) elements, with respective type counts \(1\) of \(S^3\), \(14\) of \(S^2\), \(75\) of \(S^1\), \(182\) of \(S^0\), and \(120\) empty.

As a consequence, the full integral top-homology character is
\[
\operatorname{tr}\!\left(g\mid\widetilde H_3(K;\mathbb Z)\right)=\varepsilon_1\varepsilon_2
\]
for both coordinate-preserving and coordinate-exchanging elements written with the displayed coordinate signs. Thus exchanging coordinates alone acts by \(+1\), and each coordinate reflection reverses the generator.

## Assumptions and scope

The input is the **inclusive** graph shortest-path metric on the odd \(7\)-cycle product, not a Euclidean or maximum-product metric. The statement concerns fixed points of **individual group elements** (equivalently their generated cyclic subgroups), not arbitrary subgroups or an asserted equivariant equivalence with a join of circles. Fixed points refer to the geometric realization, including barycenters of permuted simplices, and not merely fixed vertices.

## Proof

**1. The identity case.** Adams, Adetowubo, Barriga-Acosta, Feng and Sterling prove in Section 7 of arXiv:2502.07134v2 that \(K\simeq S^3\), using integral homology and connectivity. This applies to the identical inclusive metric and is the imported nonequivariant premise, not an originality claim.

**2. Exact orbit-complex model.** A symmetry \(g\) permutes the \(49\) vertices. Partition the vertex set into its cycles \(\mathcal O(g)\). Retain an orbit \(O\) exactly when all pairs of vertices in \(O\) are at metric distance at most four. Declare a collection of retained orbits to be a face exactly when their union is a simplex of \(K\). Call the resulting simplicial complex \(L_g\). The affine map sending the vertex \(O\) to the barycenter \(|O|^{-1}\sum_{x\in O}x\) induces a piecewise-linear homeomorphism \(|L_g|\cong |K|^{\langle g\rangle}\). Indeed every point of a simplicial realization has a unique support simplex; invariance forces the support to be a union of complete vertex orbits with coefficients constant on each orbit. Conversely, such nonnegative coefficients parameterize precisely \(|L_g|\). This handles all higher-order symmetries and barycentric fixed points.

**3. Exact finite classification.** The attached standard-library Python program `CHECKER.py` derives the coordinate permutation, computes the orbit list and its pairwise compatibility graph, and enumerates **all** cliques as faces of \(L_g\). It visits every \(g\) from the \(2\cdot2\cdot7\cdot7\cdot2=392\) parameter combinations. For each nonidentity element, it performs explicit elementary simplicial collapses \((\sigma,\tau)\) where \(\sigma\) has the unique maximal coface \(\tau\) and \(\dim\tau=\dim\sigma+1\); the program tests the relevant coface condition at every step. The terminal complex is independently recognized by verifiable simplicial conditions: zero faces for the empty set; exactly two isolated vertices for \(S^0\); a connected two-regular graph for \(S^1\); or a connected two-dimensional triangulation whose every vertex link is a single cycle, every edge is in two triangles, and whose Euler characteristic is two, for \(S^2\). By the classification of compact connected surfaces, the last case is a two-sphere. The proof uses no probabilistic or sampled inference: the loop covers every one of the finitely many claimed symmetries. In every case the code checks the predicted type and independently checks its Euler characteristic through the alternating clique count.

The exhaustive run produces the face-type counts \((1,14,75,182,120)\) above. The largest fixed orbit complex among nonidentity elements has \(9,214\) nonempty faces, all explicitly generated; the other ones are smaller. `CHECKER_OUTPUT.json` contains the completed reproducibility summary. Both artifacts are included as exact bytes.

**4. Homology character.** The published homotopy equivalence yields \(H_0(K;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z\), with all other reduced integral homology zero. The simplicial Lefschetz formula gives
\[
\chi(|K|^{\langle g\rangle})=1-\operatorname{tr}\!\left(g\mid\widetilde H_3(K;\mathbb Z)\right).
\]
The empty set and odd-dimensional spheres have Euler characteristic zero; both \(S^0\) and \(S^2\) have Euler characteristic two. The classification therefore gives trace \(+1\) precisely when the product of coordinate signs is positive and \(-1\) otherwise. Since the homology group is rank-one integral, this determines the complete representation.

## Verification

Run `python3 CHECKER.py` in the extracted artifact directory with Python 3.9 or newer. No external Python packages, data, network connections or third-party programs are required. Every affine operation is checked to be an isometry of all \(49\) points; every resulting orbit complex is exhaustively enumerated; elementary collapse pairs are constructed, verified by immediate-superface accounting, and removed; surface vertex links, connectivity and Euler characteristic are checked. A second direct alternating simplex count checks the Euler characteristic before collapsing. A successful run explicitly reports all \(392\) cases and no discrepancies. `CHECKER_OUTPUT.json` records the exact machine-readable outcome, including counts and representative collapse statistics. Finite exactness applies to this specified \(49\)-point complex; it does not imply similar classifications in other torus sizes or scale parameters.

## Relationship to prior work

Adams et al., *Vietoris–Rips complexes of torus grids* (arXiv:2502.07134, first posted February 10, 2025), establish \(K\simeq S^3\) and discuss potential three-sphere/Heegaard behavior, but do not determine these individual geometric fixed-point spaces or the coordinate-dihedral integral character. The present classification builds on their nonequivariant result, rather than repeating it. Zhang and Wang, *Non-maximal persistence in Vietoris–Rips complexes of torus grids* (Zenodo record 22096716, 2026), study maps between different filtration scales; those maps do not determine fixed sets at one scale. Coyle and Akhmedov's 2025 work addresses embedded lattice points under a Euclidean flat-torus metric rather than this \(\ell_1\) graph metric. No equivalence between their results and the stated symmetry-fixed classification was found in the material checked.

## Limitations

Only fixed loci of individual elements of the specified natural group are classified; fixed loci of arbitrary subgroups, the full equivariant homotopy type, and all torus-grid parameters outside the displayed case remain open here. The nonequivariant \(S^3\) input is a previously published computationally supported theorem; the supplied finite checker independently establishes the additional fixed-locus claims under that premise, not a new proof of the ambient homotopy type. No independent scientific audit has been performed. Potential unindexed equivalent results remain a residual originality risk.

## References

1. Henry Adams, Adenike Yeside Adetowubo, Hector Barriga-Acosta, Ziqin Feng, John Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v2 (2025), especially Sections 1, 7 and 8. https://arxiv.org/pdf/2502.07134
2. Dongming Zhang and Qihang Wang, *Non-maximal persistence in Vietoris–Rips complexes of torus grids*, Zenodo record 22096716 (2026). https://zenodo.org/records/22096716
3. Samuel Coyle and Anar Akhmedov, *The Vietoris–Rips Complex for Embedded Lattice Points in the Torus*, University of Minnesota poster (2025). https://conservancy.umn.edu/bitstreams/9bbdde60-0477-447d-9c17-038c8aaa8894/download
