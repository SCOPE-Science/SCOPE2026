# The McGee graph independence complex is a five-sphere

## Finding
For the McGee graph \(G\), the unique cubic \((3,7)\)-cage, the ordinary independence complex has the integral homotopy type
\[
\operatorname{Ind}(G)\simeq S^5.
\]
In particular, \(\widetilde H_5(\operatorname{Ind}(G);\mathbb Z)\cong\mathbb Z\) and all other reduced integral homology groups vanish. The claim is a homotopy equivalence, not merely a homology calculation.

## Assumptions and scope
The finite simple graph \(G\) has vertices \(\{0,\ldots,23\}\). It contains the \(24\) cycle edges \(\{i,i+1\pmod{24}\}\), and for every \(i\), also the undirected chord \(\{i,i+s_i\pmod{24}\}\), where \(s_i\) is the cyclic repetition of \((12,7,-7)\) eight times. The entry \(12\) can equivalently be written \(-12\) modulo \(24\), so this is the familiar McGee LCF representation. Duplicated chord descriptions are combined as one undirected edge. The resulting graph has \(24\) vertices, \(36\) edges, every degree equal to \(3\), and girth \(7\).

A face of \(\operatorname{Ind}(G)\) is a vertex subset containing no adjacent pair. The empty face is included for face enumeration but is **not** a cell in the ordinary matching whose homotopy type is asserted. The highest-dimensional faces have size \(10\) and dimension \(9\).

## Proof
The file `mcgee_verify.py` is an executable exhaustive certificate. First construct all independent sets by starting with the empty set and, for each vertex \(v=0,\ldots,23\), adding \(v\) to every previously constructed face that has no neighbor of \(v\). The total counts by face size \(k=0,\ldots,10\) are
\[
(a_0,a_1,\ldots,a_{10})=(1,24,240,1304,4212,8328,10024,7072,2668,424,8).
\]
There are therefore \(34{,}304\) nonempty faces. The code checks that there are no duplicate faces, and verifies the graph's degree and girth.

Define an elementary matching on the augmented face set as follows. Visit the vertices \(v=0,1,\ldots,23\) in that order. At stage \(v\), for every as-yet-unmatched face \(F\) not containing \(v\), match \(F\) with \(F\cup\{v\}\) whenever both are independent and currently unmatched. Iterate over faces in the deterministic order of their construction. The empty face is initially paired with \(\{0\}\); remove this sole pair so that the matching is on the **ordinary nonempty** face poset, with \(\{0\}\) critical.

The resulting matching contains exactly \(17{,}151\) distinct pairs. Its only unmatched faces are the vertex \(\{0\}\), of dimension \(0\), and the six-element independent set \(\{2,5,12,14,17,21\}\), of dimension \(5\). Every pair is checked to be a face/coface incidence of codimension one.

To prove acyclicity, orient every codimension-one incidence of nonempty faces downward, reversing precisely the matched incidences. Exhaustively construct all \(197{,}768\) such directed edges. Kahn's topological-sorting algorithm visits **all** \(34{,}304\) faces, with no directed cycle. Thus the finite matching is acyclic by the face-poset criterion of discrete Morse theory. This is a complete finite proof certificate; it is not a statistical test.

Discrete Morse theory yields a homotopy-equivalent CW complex with exactly one \(0\)-cell and one \(5\)-cell, and no others. The attaching map of the single \(5\)-cell has codomain a point and is necessarily constant. The CW complex is therefore homeomorphic to \(S^5\), proving the claim.

## Verification
Execute `python3 mcgee_verify.py` to reproduce the entire matching, critical-cell identities, and complete acyclicity topological sort. Execute `python3 mcgee_independent.py` to reproduce the face vector using an independent deletion recurrence and fixed-cardinality enumeration, and to construct all boundary maps over \(\mathbb F_2\) by exact bitset elimination. The independent chain calculation finds the only nonzero reduced mod-two Betti number is \(\widetilde\beta_5=1\). This chain check is corroboration, **not** the basis of the integral homotopy assertion.

As a useful boundary comparison for existing general results, the graph contains the induced nine-cycle with cyclic vertex order \((0,1,8,7,6,18,17,16,23)\); this is verified by checking each cycle vertex has exactly its two listed cycle neighbors among those nine vertices.

## Relationship to prior work
Barmak's 2010 star-cluster theorem proves that the independence complex of any triangle-free graph is homotopy equivalent to a suspension. It does not determine the suspension space or establish the exact \(S^5\) type for the McGee graph. The graph has girth \(7\), hence is triangle-free, so that theorem applies but is strictly weaker for the claimed conclusion.

Kim's theorem for graphs without an induced cycle of length divisible by \(3\) cannot imply this claim: the explicitly verified induced nine-cycle violates that hypothesis. Work on categorical products of complete graphs and generalized Mycielskians of complete graphs treats different graph families; the McGee graph has \(24\) vertices and degree \(3\), excluding the listed complete-graph product and Mycielskian classification families.

Existing calculations for the independence complexes of the Heawood and dodecahedral graphs concern different graphs and do not imply the McGee claim. Targeted searches for the McGee graph, its cage and LCF descriptions, complementary clique-complex formulation, and exact homotopy and homology statements did not identify a directly covering result. This negative search is not a proof of worldwide novelty.

## Limitations
The theorem concerns exactly the McGee graph and its *ordinary* independence complex, not other \((3,g)\)-cages, arbitrary cubic graphs, graph matching complexes, or arbitrary induced subgraphs. Its proof is exhaustive and executable for the stated finite complex; it makes no claim about infinite families. Unindexed or otherwise inaccessible equivalent research remains a bibliographic risk. The accompanying review is not an independent audit.

## References
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first publicly submitted 2010-07-02), in particular Theorems 3.4 and 3.5. https://arxiv.org/pdf/1007.0418
- E. W. Weisstein, *McGee Graph*, MathWorld (graph description, unique cage, LCF form). https://mathworld.wolfram.com/McGeeGraph.html
- J. Kim, *The homotopy type of the independence complex of graphs with no induced cycles of length divisible by 3*, arXiv:2101.07131v3, Theorem 1.1. https://arxiv.org/html/2101.07131v3
- S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, Contributions to Discrete Mathematics 16 (2021), 74–92, doi:10.55016/ojs/cdm.v16i3.71284. https://cdm.ucalgary.ca/article/download/71284/55559/225284
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic cellular matchings and Morse reduction).
