# Twenty-one minimal Heawood homology carriers and their Fano-plane relations

## Finding
Let \(H\) be the point-line incidence (Heawood) graph of the Fano plane, \(K=\operatorname{Ind}(H)\) its independence complex, and \(\mathbb F_2\) the coefficient field. The twenty-one induced ten-vertex subcomplexes that carry a nonzero class of \(\widetilde H_3(K;\mathbb F_2)\) are **exactly** those obtained by deleting two distinct point vertices and the two line vertices nonincident to both. Each of their induced graphs is \(C_8\sqcup K_2\).

For **every** vertex subset \(S\subseteq V(H)\), the inclusion induces an injection
\[
\widetilde H_3(K[S];\mathbb F_2)\longrightarrow \widetilde H_3(K;\mathbb F_2).
\]
The global target has dimension six. The complete distribution of the dimensions of these images, with columns giving their dimensions, is:

| \(|S|\) | dimension 0 | dimension 1 | dimension 2 | dimension 3 | dimension 6 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 14 | 0 | 0 | 0 | 0 |
| 2 | 91 | 0 | 0 | 0 | 0 |
| 3 | 364 | 0 | 0 | 0 | 0 |
| 4 | 1001 | 0 | 0 | 0 | 0 |
| 5 | 2002 | 0 | 0 | 0 | 0 |
| 6 | 3003 | 0 | 0 | 0 | 0 |
| 7 | 3432 | 0 | 0 | 0 | 0 |
| 8 | 3003 | 0 | 0 | 0 | 0 |
| 9 | 2002 | 0 | 0 | 0 | 0 |
| 10 | 980 | 21 | 0 | 0 | 0 |
| 11 | 280 | 84 | 0 | 0 | 0 |
| 12 | 21 | 42 | 28 | 0 | 0 |
| 13 | 0 | 0 | 0 | 14 | 0 |
| 14 | 0 | 0 | 0 | 0 | 1 |

For distinct Fano points \(p,q\), write \(c_{pq}\) for the unique nonzero class in the image of the corresponding ten-vertex carrier (and set \(c_{pq}=c_{qp}\)). These **twenty-one classes are pairwise distinct and span all six dimensions** of \(\widetilde H_3(K;\mathbb F_2)\). Exactly twenty-eight triples of distinct classes sum to zero. They are precisely
\[
 c_{pq}+c_{pr}+c_{ps}=0
 \quad\Longleftrightarrow\quad
 \{p,q,r,s\}=P\setminus L
\]
for a Fano line \(L\), where the four points on the right are distinct, \(P\) denotes the seven-point set, and three carrier classes share the distinguished point \(p\). Every triple of distinct carrier classes with zero sum arises in this way, and each of the seven lines has four choices of distinguished point.

## Assumptions and scope
Identify the seven Fano points with the nonzero three-bit vectors \(P=\mathbb F_2^3\setminus\{0\}\). Identify the seven lines with the nonzero three-bit covectors \(a\), where the line is \(L_a=\{p\in P:a\cdot p=0\}\). Thus point vertex \(p\) and line vertex \(a\) are adjacent in \(H\) if and only if \(a\cdot p=0\). This is a simple, bipartite fourteen-vertex graph with twenty-one edges. A face of \(K[S]\) is a subset of \(S\) containing no incident point-line pair. All reduced homology and assertions of injectivity in this finding use **mod-two coefficients**; no analogous integral or odd-characteristic support theorem is asserted.

For a pair of distinct points \(p,q\), there are exactly two lines \(a\) which contain neither point. Let \(S_{pq}\) consist of the other ten graph vertices: remove \(p,q\) and those two lines. A carrier means a vertex set whose induced independence complex maps nontrivially to the global third homology. The classification is of *vertex supports of nonzero classes*, not of minimum numbers of oriented tetrahedra in a cycle.

## Proof
**The carrier geometry.** The unique Fano line through \(p,q\) contains a third point \(r\). Removing \(p,q\) and the two lines avoiding them leaves a graph in which \(r\) and the line through \(p,q\) form an isolated edge. Its other four point vertices and four line vertices each have degree two. This eight-vertex component is a simple two-regular bipartite graph. It cannot contain a four-cycle, since the Fano incidence graph has girth six; hence it is a single eight-cycle. Thus \(H[S_{pq}]\cong C_8\sqcup K_2\). There are twenty-one distinct unordered point pairs and therefore twenty-one such ten-vertex supports.

**Boundary construction.** Index graph vertices by integers \(0,\ldots,13\), the first seven for points and the next seven for lines. Enumerate each of the \(2^{14}\) subsets and retain it precisely if it contains no incidence edge. The numbers of faces of cardinality \(0,\ldots,7\) are
\[
(1,14,70,154,147,56,14,2).
\]
Over \(\mathbb F_2\), define the boundary of every \((j+1)\)-element face to be the sum of its \(j\)-element subfaces. Encode each column as a bit vector with one bit per indexed row face; Gaussian elimination using the highest nonzero pivot is exact. In degrees three and four the resulting ranks are
\[
\operatorname{rank}\partial_3=97,\qquad
\operatorname{rank}\partial_4=44,
\]
with \(147\) four-vertex faces. The inclusions \(\partial_3\partial_4=0\) hold column by column. Hence \(\dim\widetilde H_3(K;\mathbb F_2)=147-97-44=6\).

**Induced-subcomplex inclusions, not just Betti numbers.** For each of all \(16{,}384\) subsets \(S\), restrict the boundary columns to those whose entire vertex set lies in \(S\). Compute a basis for \(\ker\partial_3(K[S])\) by the standard elimination-with-column-bookkeeping algorithm. Compute its third Betti number by subtracting the rank of \(\partial_4(K[S])\). Independently of this local quotient, reduce every kernel generator modulo the **global** column space of \(\partial_4(K)\), then take the rank of the reduced generators. This last rank is exactly the dimension of the image of \(H_3(K[S])\to H_3(K)\), because all local three-cycles are also global three-cycles. For every \(S\), the computed local Betti number and image rank are equal, proving injectivity; the exhaustive histogram is stated above. In particular every set of at most nine vertices has zero third homology, and only the twenty-one geometrically described ten-vertex supports have nonzero third homology.

**Relations of the carrier classes.** Each ten-vertex carrier has local and image dimensions one. Reduce one nonboundary kernel generator from each carrier against a *fixed* global echelon basis of \(\operatorname{im}\partial_4(K)\). This fixes an unambiguous binary representative of \(c_{pq}\) in the quotient, without any orientation choice. The twenty-one remainders are nonzero and pairwise unequal; their column rank is six. Enumerating the \(\binom{21}{3}=1330\) distinct triples of remainders finds exactly twenty-eight with zero binary sum. Enumerating the seven Fano lines and, for each, the four distinguished points in its four-point complement produces exactly the same twenty-eight triples, proving both directions of the displayed equivalence. This enumeration also rules out any additional three-term relation, including triples not sharing a point.

These are finite exhaustive proofs: the list of possible vertex subsets, face boundaries, quotient remainders and triples is complete, and each operation is an exact field operation. There is no extrapolation from sampled graphs or parameters.

## Verification
Run `python3 verify.py` from this package. The standard-library verifier reconstructs the twenty-one incidence edges, all face sets, mod-two boundaries and kernel bases. It tests all \(16{,}384\) induced vertex sets (not only the minimum cases), checks the equality of local and image dimensions for each, checks the complete dimension histogram, verifies the graph type for all twenty-one minimal carriers, and checks every one of the \(1330\) candidate three-term relations. The recorded output is in `verification_output.txt` and ends with `VERIFY_OK`. The verifier uses explicit integer bitsets and exact XOR Gaussian elimination; neither numerical tolerance nor a precomputed homology table is used. A second standard-library implementation, `crosscheck.py`, computes every induced inclusion using independent stacked-boundary rank identities rather than enumerating local kernel representatives; its output `crosscheck_output.txt` ends with `CROSSCHECK_OK` and agrees for all 16,384 subsets. The embedded checkers and their outputs support exact computational verification, not independent peer review.

## Relationship to prior work
Barmak's 2010 star-cluster study develops topological methods for independence complexes but does not evaluate induced-support persistence of the Heawood graph. Tsukuda's incidence-graph/Alexander-duality theorem relates homotopy types in general; it does not give maps from all induced subcomplexes into the ambient complex or the twenty-one carrier classes and their ternary relations. Perarnau and Perkins analyze the Heawood independence polynomial and extremality for cubic graphs of girth at least five, rather than homology supports. Published calculations of \(\operatorname{Ind}(H)\simeq\bigvee^6 S^3\), the cyclic order-seven action, and the exceptional \(168\)-element group character establish global homotopy or representation information. None of these statements determines the all-subsets support filtration or identifies the twenty-eight relations among minimum carriers; those are the subject here. The similarly named Fano cap complex is a different seven-vertex object, and results on graph particle configurations are also inapplicable to these induced independence subcomplexes.

## Limitations
This is a single fourteen-vertex graph, with coefficients in \(\mathbb F_2\) and degree-three homology only. The number ten is a **vertex-support** minimum, not a simplex-count systole. The indicated twenty-eight circuits classify only dependencies involving exactly three of the twenty-one classes; longer linear relations exist because the span has dimension six and no full circuit classification is claimed. Although all induced-subcomplex maps in this one homological degree are injective, no universal injectivity principle for incidence graphs or higher-order planes is inferred. As with any finite literature comparison, differently indexed equivalent work remains a possibility; independent mathematical auditing has not been performed.

## References
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first publicly posted 2010-07-02, https://arxiv.org/abs/1007.0418.
- S. Tsukuda, *Independence complexes and incidence graphs*, *Contributions to Discrete Mathematics* 12 (2017), 28–46, https://doi.org/10.55016/ojs/cdm.v12i1.62277.
- G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth*, arXiv:1611.01474v1, first posted 2016-11-04, https://arxiv.org/abs/1611.01474.
- *The Heawood independence complex is a wedge of six three-spheres*, publicly indexed mathematical result (2026-10-04), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-heawood-independence-complex-is-bigvee-6-s-3--dbd95019d1e2.
- *The exceptional rational homology representation of the Heawood independence complex*, publicly indexed mathematical result (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-exceptional-rational-homology-representation-of-the-heawood--213fded46807.
- *Cyclic symmetry on Heawood independence homology*, publicly indexed mathematical result (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-cyclic-symmetry-on-heawood-independence-homology--d926cd684526.
