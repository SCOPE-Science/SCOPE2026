# Eight homotopy types among the fifteen regular nine-vertex tournament neighborhood complexes

## Finding
Let \(T\) range through all tournaments on nine vertices in which every vertex has outdegree four. Write \(\mathcal N^+(T)\) for the directed out-neighborhood complex: a nonempty set \(\sigma\subseteq V(T)\) is a simplex if and only if a vertex \(v\) exists with \(v\to w\) for every \(w\in\sigma\). The fifteen isomorphism classes of regular tournaments on nine vertices have exactly **eight distinct integral homotopy types**. In the order of the fifteen adjacency strings in `rt9_source.txt`, the complete classification is:

| Catalogue index (zero-based) | \(f_0,f_1,f_2,f_3\) | Homotopy type of \(\mathcal N^+(T)\) |
|---:|:---:|:---|
| 0 | 9, 31, 31, 9 | \(S^1\) |
| 1 | 9, 36, 36, 9 | \(S^1\) |
| 2 | 9, 35, 34, 9 | \(S^1\vee S^1\) |
| 3 | 9, 36, 33, 9 | \(\bigvee^{4}S^1\) |
| 4 | 9, 33, 33, 9 | \(S^1\) |
| 5 | 9, 33, 33, 9 | \(S^1\) |
| 6 | 9, 36, 36, 9 | \(S^1\) |
| 7 | 9, 34, 36, 9 | \(S^2\) |
| 8 | 9, 31, 35, 9 | \(\bigvee^{3}S^2\) |
| 9 | 9, 34, 35, 9 | \(S^1\vee S^2\) |
| 10 | 9, 34, 32, 9 | \(\bigvee^{3}S^1\) |
| 11 | 9, 36, 30, 9 | \(\bigvee^{7}S^1\) |
| 12 | 9, 36, 35, 9 | \(S^1\vee S^1\) |
| 13 | 9, 35, 35, 9 | \(S^1\) |
| 14 | 9, 27, 27, 9 | \(S^1\) |

The index-9 tournament has reduced integral homology in **both** degrees one and two; the index-7 and index-8 tournaments have only second homology. Every complex in this complete regular-nine census has torsion-free integral homology.

## Assumptions and scope
A tournament has exactly one directed arc between every two distinct vertices. Regularity on nine vertices means outdegree four (and indegree four) at every vertex. Following the convention of the exhaustive catalogue of regular tournaments provided by Brendan McKay, each of the fifteen input lines records the 36 entries of the upper triangle of the adjacency matrix in row-major order. At position \((i,j)\) with \(0\le i<j\le8\), a one denotes the arc \(i\to j\), and a zero denotes \(j\to i\). The complex has maximal simplices given by the nine four-element out-neighborhoods; its faces are their downward closure. The catalogue supplies the known exhaustive enumeration of isomorphism classes; the attached calculation independently checks the fifteen encoded representatives are regular and pairwise nonisomorphic but does not reconstruct the catalogue's underlying global enumeration of all labeled tournaments.

## Proof
**Finite face reconstruction.** Decode each catalogue line into nine four-element out-neighborhood masks. For each such mask, include every nonempty submask. All generated complexes have nine vertices and nine three-dimensional facets. The fifteen face vectors are the ones displayed in the table. The attached `verify.py` independently tests all outdegrees and the pairwise nonisomorphism of the fifteen graphs by a backtracking isomorphism search.

**Acyclic discrete-Morse certificates.** Each of the fifteen complexes has a complete matching of the nonempty face poset, recorded as integer-bitmask pairs in `certificate.json`. The verifier checks (i) every matched pair is a face and an immediate coface, (ii) all nonempty faces occur exactly once, either in a pair or as critical, and (iii) the directed Hasse diagram, oriented upward on matched incidences and downward otherwise, contains no directed cycle. Thus each matching is a valid discrete-Morse matching and yields a CW complex with exactly the recorded critical cells. The critical-cell multiplicities \((c_0,c_1,c_2,c_3)\) are \((1,b_1,b_2,0)\), where \((b_1,b_2)\) are, respectively, the pair of exponents of \(S^1\) and \(S^2\) in the table. Across the fifteen complexes, the certificate contains 616 disjoint matched pairs and 46 critical cells, partitioning all 1,278 nonempty faces. The verifier checks every Hasse incidence, not merely a sample.

**Homotopy identification.** If \(c_2=0\), the Morse CW complex has one zero-cell and \(c_1\) one-cells, and is exactly a wedge of \(c_1\) circles. If \(c_1=0\), it has one zero-cell and \(c_2\) two-cells, and is exactly a wedge of \(c_2\) two-spheres. There is only one remaining case, index 9, with one critical cell in each of dimensions zero, one and two. In that case the unique two-cell is attached to a circle by some integer degree \(d\). Exact rational simplicial boundary ranks give \(\dim_{\mathbb Q}H_2=1\), forcing \(d=0\). Every degree-zero map from a circle to a circle is null-homotopic, so the Morse CW complex is \(S^1\vee S^2\). This establishes all fifteen *integral homotopy equivalences*, not just equalities of field Betti numbers.

**Exhaustiveness over the stated class.** McKay's catalogue gives exactly fifteen isomorphism representatives of regular nine-vertex tournaments. The checker verifies their pairwise nonisomorphism and every finite topological certificate, so the table accounts for every regular nine-vertex tournament, up to isomorphism. The eight distinct homotopy types are determined by their differing homology ranks in degrees one and two; repetitions in the table are genuine homotopy coincidences.

## Verification
From the directory containing the files, run `python3 verify.py`. The program requires only Python's standard library, the fifteen source adjacency strings in `rt9_source.txt`, and the complete matching certificate in `certificate.json`. It recomputes every simplex, checks all 616 matched pairs and every Hasse incidence for acyclicity, and reconstructs signed simplicial boundary matrices. It separately computes all boundary ranks by exact rational Gaussian elimination and by bitset elimination over \(\mathbb F_2\). The ranks agree in every dimension for each representative and yield the stated homology. The output is reproduced in `verification_output.txt`; the verification is reproducible directly from the accompanying input data and code, without relying on that output log.

## Relationship to prior work
Dochtermann and Singh introduced and analyzed directed out-/in-neighborhood complexes and their equivalence to directed edge Hom complexes, and give a homology table for tournaments on five vertices. Their general vanishing bounds and constructed sphere examples do not identify the fifteen regular nine-vertex types. Govc's tournament homotopy census classifies *directed flag complexes*, whose simplices are transitively oriented subtournaments, rather than simplices lying within a common out-neighborhood. Its classifications therefore do not imply this theorem. Published records describing a six-vertex tournament neighborhood census and torsion-freeness through seven vertices likewise have strictly smaller vertex ranges. The result depends on an existing exhaustive catalogue for the graph isomorphism classes but supplies new homotopy calculations and certificates for the distinct neighborhood complexes.

## Limitations
Completeness depends on the externally published assertion that the supplied catalogue exhausts the regular nine-vertex tournaments; the standalone verifier checks only regularity and pairwise nonisomorphism of its representatives. This result establishes homotopy types only at nine vertices, not a uniform formula for tournaments of all odd orders. It does not compute equivariant homotopy types, directed flag complexes, or higher directed Hom complexes. A matching unindexed prior calculation is not logically excluded by literature searches. The proof and finite certificates are subject to independent mathematical review, which has not been performed.

## References
1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, first submitted 2021-08-24, especially Definition 4.1, Theorem 4.3, Table 1 and Section 7. https://arxiv.org/abs/2108.10948
2. B. D. McKay, *Combinatorial Data: Digraphs*, section “Regular and Semi-regular Tournaments”; the complete fifteen-line order-nine catalogue. https://users.cecs.anu.edu.au/~bdm/data/digraphs.html and https://users.cecs.anu.edu.au/~bdm/data/rt9.txt
3. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333, first submitted 2020-06-09, Section 3 (a distinct simplicial-complex construction). https://arxiv.org/abs/2006.05333
