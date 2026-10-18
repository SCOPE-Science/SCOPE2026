# Scientific review: thirty-six-vertex Schrijver independence-complex homology

## Correctness — PASS
The graph is specified by lexicographically ordered cyclically stable five-subsets of a twelve-cycle and disjointness adjacency. The included verifier constructs all 1,519,600 augmented faces and an acyclic Forman matching of 759,796 pairs, leaving exactly six six-cells and two eight-cells. An independent deletion–closed-neighborhood recurrence reproduces the complete face-count polynomial. The full Hasse incidence orientation (12,264,696 cover relations) admits an exhaustive topological sort, confirming that the matching is acyclic, not merely producing numerically plausible Betti numbers. The empty face is paired, so the Morse CW model contains one basepoint. Since no consecutive positive-dimensional Morse cells occur, all integral cellular differentials vanish, yielding the claimed free homology and five-connectivity.

## Originality — PASS
The closest exact-family treatment is Braun's *Independence Complexes of Stable Kneser Graphs* (arXiv:0912.0720v1; Theorems 1.4–1.5 and Section 4). It identifies the homotopy problem for \(SG_{n,2}\), but computes \(SG_{2,k}\) and the *distinct* auxiliary family \(E_{2n+2}\), not the thirty-six-vertex complex here. Braun and Zeckner (arXiv:1102.1984v1) concern neighborhood complexes, a different construction. The comparison with an available published result distinguishes the twenty-five-vertex \(SG_{4,2}\) result from this thirty-six-vertex \(SG_{5,2}\) statement. Feng and Wang (arXiv:2404.10566v1) investigate ordinary Kneser graphs rather than this stable induced subgraph. Exact-parameter, alias, and stronger-coverage searches returned no covering claim; the remaining possibility of an unindexed exact computation is explicitly acknowledged, not treated as disproved.

## Mathematical value — PASS
This is an exact integral calculation in a canonical family explicitly identified as topologically difficult in the primary literature. The smallest new higher-parameter test after a known twenty-five-vertex Schrijver case exhibits two widely separated nonzero reduced homology degrees, both torsion-free, and a surprisingly small Morse CW model on a 1.52-million-face complex. It supplies concrete homotopy-theoretic constraints for subsequent study of the family and does not depend on an arbitrary restriction or a claimed general conjecture.

## Limitations
The result is about one graph only. The eight-cell attaching maps are not determined; no complete sphere-wedge homotopy type is claimed. The proof is a finite exact certificate requiring substantial RAM. Comparisons cannot rule out literature omitted by search indexes or a later unindexed independent discovery; no external scientific audit was conducted.

Self-review: passed. Independent audit: not yet performed.
