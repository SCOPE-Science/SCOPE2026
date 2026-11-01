# Three first unresolved three-color cycle-product independence homotopy types

## Finding

For the categorical (tensor) graph product \(G_m=C_m\times K_3\), the ordinary independence complexes at the three smallest cycle lengths \(m\ge 7\) not divisible by three have exact integral homotopy types
\[
\begin{aligned}
\operatorname{Ind}(G_7)&\simeq S^3\vee\bigvee^3 S^4,\\
\operatorname{Ind}(G_8)&\simeq S^4\vee\bigvee^3 S^5,\\
\operatorname{Ind}(G_{10})&\simeq\bigvee^3 S^5\vee S^6.
\end{aligned}
\]
Every reduced integral homology group is therefore free abelian, with the ranks and degrees visible from the wedge decompositions. In particular these three cases answer affirmatively the torsion-freeness question of Antolín Camarena and Carnero Bravo, Question 24 (2023), for the first three previously unresolved cycle lengths in the three-color subfamily. These are **three finite classifications**, not an all-parameter theorem.

## Assumptions and scope

For \(m\in\{7,8,10\}\), the undirected simple graph \(G_m\) has vertices \((i,a)\in\mathbb Z/m\mathbb Z\times\{0,1,2\}\), and edges precisely when the cycle positions differ by \(\pm1\) modulo \(m\) and the colors differ. A face of \(\operatorname{Ind}(G_m)\) is any nonempty set of such vertices containing no graph edge. In particular this is the **categorical**, not Cartesian or strong, graph product. We equip every simplex with increasing vertex orientation under the bijection \((i,a)\mapsto3i+a\). The topological statements concern ordinary, non-equivariant, integral homotopy type.

## Proof

The file `verify_cycle_products.py` is a complete, finite constructive certificate. For each of \(m=7,8,10\), represent each face as the integer bitmask of its vertices. Begin with the empty face and process the \(3m\) vertices in increasing order, adjoining vertex \(v\) to each face whose members are all nonadjacent to \(v\). Induction on the vertex index proves that this enumerates **every** independent subset once and nothing else. It finds respectively **5,281**, **18,721**, and **216,257** nonempty faces. An independent cyclic eight-state transfer count based on the three-color layer subsets gives exactly the same totals, including the empty face.

Form the following explicit face-poset matching. For vertex indices \(v=0,1,\ldots,3m-1\) in order, match every still-unmatched face \(\sigma\) omitting \(v\) to \(\sigma\cup\{v\}\), provided both currently remain unmatched, then remove those two faces from later matching stages. The empty face is excluded from this matching. This algorithm selects **2,635**, **9,353**, and **108,121** disjoint pairs, respectively. Orient each Hasse incidence from higher to lower dimensional face, reversing exactly the matched incidences. The checker constructs indegrees from **all** incidences and performs Kahn topological sorting; it visits all faces, respectively checking **25,221**, **104,568**, and **1,502,070** incidences. Thus the directed Hasse graphs are acyclic and the matchings satisfy Forman's acyclic-matching criterion.

The unmatched critical cells are exactly: one vertex, four three-cells and six four-cells for \(m=7\); one vertex, six four-cells and eight five-cells for \(m=8\); one vertex, eight five-cells and six six-cells for \(m=10\). By discrete Morse theory each simplicial complex is homotopy equivalent to a CW complex with precisely these cells and **no others**. In particular, the CW complexes are simply connected and their first possible positive-dimensional cells occur in dimensions at least three.

The remaining integral cellular differential is computed by exact signed gradient-path elimination. For a cell \(s\) in the lower of the two positive dimensions, define its projection \(P(s)\) to the free group on critical cells of that dimension. Critical cells project to their own basis vectors; cells matched as upper cells project to zero. If \(s\) is matched as a lower face with \(u\), of one greater dimension, and \(\epsilon(t,u)\in\{\pm1\}\) is the oriented incidence number, set
\[
P(s)=-\epsilon(s,u)\sum_{\substack{t\subset u,\ |t|=|s|,\\ t\ne s}}\epsilon(t,u)P(t).
\]
Acyclicity ensures these recursions terminate and compute the integer Morse boundary. Apply \(P\) to the ordinary oriented boundary of each critical top-dimensional cell. The resulting differential matrices have shapes \(4\times6\), \(6\times8\), and \(8\times6\) and exact ranks **3**, **5**, and **5**. In each case a rank-sized square submatrix has determinant \(\pm1\): using zero-based row and column indices, respectively rows \((0,1,3)\), columns \((0,1,3)\), determinant \(-1\); rows \((0,1,2,3,4)\), columns \((1,2,3,4,5)\), determinant \(+1\); and rows \((1,2,3,4,5)\), columns \((0,1,2,3,4)\), determinant \(+1\). These certificates prove that every nonzero Smith invariant factor is one.

Writing \(d\) for the lower positive critical dimension, the only attaching maps are the boundaries of the \((d+1)\)-cells in \(\pi_d(\bigvee S^d)\cong\mathbb Z^r\) for \(d\ge3\). The Hurewicz isomorphism identifies these homotopy classes with the integral columns above. Unimodular row/column changes are induced by homotopy equivalences of sphere wedges and degree transformations of attaching spheres; the unit diagonal attachments cancel. The remaining null attachments yield the three wedge types stated in the finding.

## Verification

Execute `python3 verify_cycle_products.py` using the Python 3 standard library. It recreates graph edges, independently checks the face counts by an eight-state transfer computation, tests that every enumerated face is independent, constructs all matching pairs, topologically sorts every directed Hasse incidence, reconstructs each integral Morse matrix, calculates its exact rational rank with rational arithmetic and exhibits its stated unit maximal-rank minor using fraction-free integer determinants. Separately, the program reduces **the original unreduced simplicial boundary matrices** over \(\mathbb F_2\) in every dimension. The resulting reduced mod-two Betti numbers are \((b_3,b_4)=(1,3)\), \((b_4,b_5)=(1,3)\), and \((b_5,b_6)=(3,1)\) for the three lengths, respectively, and vanish elsewhere. `verification_output.txt` records a successful execution. The mod-two check is independent corroboration; it is not used to infer the integral Smith factors or homotopy type.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (2023 preprint, 2024 publication) compute the homotopy types of \(\operatorname{Ind}(C_m\times K_n)\) for cycle lengths divisible by three and for lengths four and five, and give a general sphere-wedge/**possible Moore space** description for the remaining lengths (Theorems 22–23). In the paragraph following Theorem 23 they explicitly list the present three graph products among examples whose free homology is nonzero in two consecutive degrees, then ask whether all such products have torsion-free integral homology (Question 24). Those observations do **not** supply their full integral homotopy types or exclude Moore summands. The present exact matrices establish the stronger finite wedge classifications. Goyal, Shukla and Singh (2019) treat products of complete graphs and a graph-perturbation suspension operation, not these cyclic products. Carnero Bravo (2025) classifies products **with a path factor**, not these cycle-by-clique products.

A separately published exact result gives \(\operatorname{Ind}(C_7\times K_4)\simeq\bigvee^3S^3\vee\bigvee^6S^4\), but does not imply the three-color case or the other two cycle lengths. The results here do not assert that previously available computations lacked homology information; they add complete integral attaching maps and resulting homotopy decompositions.

## Limitations

Only the three explicitly listed finite graphs are classified. No claim is made for other cycle lengths, other colors, a natural symmetry module, a uniform all-parameter matching, or a solution of Question 24 in general. The proof is an exhaustive finite certificate, with the entirety of each face complex and its Hasse incidences checked; unlike a finite sample it is exhaustive **for these fixed graphs**, but says nothing directly about untested lengths. No independent external audit has been performed. Search coverage cannot rule out equivalent results in unindexed publications or unpublished computational records.

## References

- S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019), especially Section 3. https://arxiv.org/pdf/1905.06926
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v1 (2023-07-23), Theorems 22–23, Question 24, pp. 25–27, and *Homology, Homotopy and Applications* **26** (2024). https://arxiv.org/pdf/2307.12401
- A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457 (2025), Sections 3–5. https://arxiv.org/pdf/2505.06457
- *A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors*, public mathematical research record (2026). https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-a-torsion-free-mixed-dimensional-sphere-wedge-for-the-seven-cycl--50b8be4e4c8f/RESULT.md
