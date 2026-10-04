# Mod-2 homology of the Pappus matching complex
## Finding
For the Pappus graph \(P\), the ordinary matching complex \(\mathcal M(P)\) has reduced mod-\(2\) homology concentrated in degree \(5\): \(\widetilde H_5(\mathcal M(P);\mathbb F_2)\cong \mathbb F_2^{40}\), and \(\widetilde H_i(\mathcal M(P);\mathbb F_2)=0\) for every integer \(i\ne 5\).

## Assumptions and scope
The Pappus graph is taken in its standard 18-vertex cubic form, equivalently the graph with LCF description \([5,7,-7,7,-7,-5]^3\). Its ordinary matching complex \(\mathcal M(P)\) is the simplicial complex whose vertices are graph edges and whose simplices are pairwise vertex-disjoint sets of graph edges. Homology is reduced simplicial homology over \(\mathbb F_2\).

## Proof
The supplied verifier constructs the graph from the LCF description, obtaining 18 vertices, 27 distinct edges, and degree 3 at every vertex. It then exhaustively branches over all 27 graph edges, including an edge exactly when neither endpoint has already been used. This is a bijective enumeration of all matchings. The numbers of matchings of sizes \(0,1,\ldots,9\) are
\[
1,27,297,1719,5643,10557,10737,5319,1026,42.
\]
Thus the nonempty face vector in simplex dimensions \(0,\ldots,8\) is
\[
(27,297,1719,5643,10557,10737,5319,1026,42).
\]
As an independent enumeration check, a memoized vertex-deletion recurrence for the matching polynomial reproduces the same ten coefficients.

For the augmented simplicial chain complex over \(\mathbb F_2\), exact bitset Gaussian elimination gives boundary ranks in simplex dimensions \(0,\ldots,8\)
\[
(1,26,271,1448,4195,6362,4335,984,42).
\]
Hence \(\widetildeeta_d=f_d-r_d-r_{d+1}\), with the final next-boundary rank equal to zero. The resulting reduced Betti vector is
\[
(0,0,0,0,0,40,0,0,0),
\]
which proves the claim. As a separate consistency check, the ordinary Euler characteristic is \(-39\), so the reduced Euler characteristic is \(-40\), agreeing with concentration of 40 generators in odd degree 5.

## Verification
Run `python3 verify_pappus_matching.py`. The script uses only the Python standard library, reconstructs the graph and every simplex, independently recomputes the matching-count vector by a vertex-deletion recurrence, performs exact \(\mathbb F_2\) boundary elimination, checks the Euler characteristic, and terminates with `VERIFY_OK`.

## Relationship to prior work
Donovan and Scoville develop star-cluster and discrete-Morse methods for ordinary matching complexes and compute explicit homotopy types for paths, cycles, centipedes, and Dutch windmills. Their paper has primary MSC 57Q70 and first appeared publicly on 2022-07-27. Its inspected matching-complex section does not treat the Pappus graph. Bayer, Goeckner, and Jelić Milutinović classify when graph matching complexes are homology manifolds; the checked abstract/full-page material does not state the Pappus graph computation. Exact web and published-finding corpus searches for the Pappus matching complex, its Levi-graph alias, and the degree-5 rank 40 claim did not locate a source stating this result. The Pappus graph is a canonical cubic symmetric graph and the Levi graph of the Pappus configuration, so this supplies an exact topological benchmark outside the structured families treated in the anchor paper.

## Limitations
The result determines reduced homology only over \(\mathbb F_2\). It does not assert an integral homology classification, torsion-freeness, a wedge-of-spheres homotopy type, simple connectivity, or a minimality statement. Literature searches cannot rule out an obscure or unindexed prior computation under a different graph-complex presentation.

## References
Connor Donovan and Nicholas A. Scoville, “Star clusters in the matching, Morse, and generalized complex of discrete Morse functions,” New York Journal of Mathematics 29 (2023), 1393–1412; arXiv:2207.13780.

Margaret Bayer, Bennet Goeckner, and Marija Jelić Milutinović, “Manifold Matching Complexes,” Mathematika 66 (2020), 973–1002.

Wolfram MathWorld, “Pappus Graph,” identifying the standard cubic symmetric 18-vertex graph and its LCF representation.
