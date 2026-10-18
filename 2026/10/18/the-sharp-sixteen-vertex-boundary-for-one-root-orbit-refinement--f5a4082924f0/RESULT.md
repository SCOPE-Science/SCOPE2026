# The sharp sixteen-vertex boundary for one-root orbit refinement of finite abelian Cayley graphs

## Finding
For every finite abelian group \(A\) of order strictly less than \(16\), and every inverse-closed subset \(S\subseteq A\setminus\{0\}\), ordinary counting colour refinement on the undirected simple Cayley graph \(\operatorname{Cay}(A,S)\), with one vertex individually coloured, stabilizes at **exactly the automorphism-orbit partition fixing that vertex**. At order \(16\) this fails: the Shrikhande graph, realized as \(\operatorname{Cay}(\mathbb Z_4^2,S)\) for \(S=\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\}\), has a stable rooted partition of sizes \(1,6,9\), but the nine-vertex class contains at least two different rooted automorphism orbits. Thus the least possible order of such an obstruction within finite undirected abelian Cayley graphs is exactly \(16\).

The order-sixteen example is classical and is *not* claimed as newly discovered. The new finite statement is the exhaustive lower bound on all groups and connection sets of smaller order.

## Assumptions and scope
A graph has vertices \(A\) and distinct vertices \(a,b\) adjacent exactly when \(b-a\in S\). No connectedness or generation assumption is imposed; the empty and complete graphs are included. Refinement begins with \(\{r\}\) and \(A\setminus\{r\}\) in different colours and repeatedly replaces the colour of each vertex by its previous colour and the multiset of neighbours' previous colours. Its stable classes are compared with the orbits of \(\operatorname{Aut}(\operatorname{Cay}(A,S))_r\). The claim is only about this **one-root orbit partition**; it does not assert graph identification, full Tinhofer behavior, or connectedness.

## Proof
**Reduction to a finite, exhaustive classification.** Translating the group by \(-r\) gives a graph automorphism taking any distinguished root \(r\) to \(0\). By the classification of finite abelian groups, the complete list of group types of orders below \(16\) is
\[
\begin{gathered}
\{1\};\ C_2;\ C_3;\ C_4,C_2^2;\ C_5;\ C_6;\ C_7;\\
C_8,C_4\times C_2,C_2^3;\ C_9,C_3^2;\ C_{10};\ C_{11};\\
C_{12},C_6\times C_2;\ C_{13};\ C_{14};\ C_{15}.
\end{gathered}
\]
For each type, inversion partitions nonzero group elements into one- or two-element classes. A simple undirected Cayley connection set is precisely a union of these classes, so enumerating every subset of inversion classes covers **every** permitted graph, including disconnected cases. The included enumeration and independent checker jointly establish the following exhaustive statement: for every stable rooted refinement cell \(C\) and every \(u,v\in C\), there is an explicit vertex permutation \(\pi\) such that \(\pi(0)=0\), \(\pi(u)=v\), and \(\pi\) preserves every graph adjacency and nonadjacency. In fact it is sufficient to construct permutations taking a fixed representative of each cell to all other members.

The file `cayley_certificates.json` records such automorphism permutations for all \(821\) group-and-connection-set cases, comprising \(4936\) separately checked witness permutations. The standard-library checker recomputes the graph and refinement partitions, verifies exhaustion and checks every recorded permutation against the full adjacency matrix. Every automorphism preserves refinement colours, while these certificates show transitivity on every stable colour class; hence colour classes equal the required root-stabilizer orbits in every case.

The enumeration counts by group order are: order \(1:1\), \(2:2\), \(3:2\), \(4:12\), \(5:4\), \(6:8\), \(7:8\), \(8:176\), \(9:32\), \(10:32\), \(11:32\), \(12:192\), \(13:64\), \(14:128\), \(15:128\). These count connection sets **with multiplicity across presentations**, not graph isomorphism types. They sum to \(821\).

**An obstruction at sixteen.** In \(\mathbb Z_4\times\mathbb Z_4\), use the six generators above. Direct enumeration of common neighbours establishes the strongly regular parameters \((16,6,2,2)\). Thus refinement rooted at \((0,0)\) stabilizes with the three cells comprising the root, its six neighbours, and its nine nonneighbours. For a nonneighbour \(v\), the set of common neighbours of \(v\) and the root has exactly two elements. In three of the nine cases those two vertices are **nonadjacent**; in the other six they are **adjacent**. This adjacency relation is preserved by every rooted automorphism, so the nine-vertex refinement class contains at least two rooted automorphism orbits. The script `check_exception16.py` proves every asserted count directly from the sixteen-by-six group construction. It follows that \(16\) is the exact minimum order.

## Verification
Run `python enumerate_cayley.py cayley_certificates.json` to regenerate the finite search certificates; this script uses NetworkX only to find candidate automorphism maps, then checks those maps. Run `python check_certificates.py cayley_certificates.json` to independently reconstruct and verify all \(821\) cases and all \(4936\) permutations using only the Python standard library. Run `python check_exception16.py` for an independent arithmetic and adjacency check of the sixteen-vertex obstruction. All three commands were executed successfully on the files delivered in this package. The checker provides a finite exhaustive proof because the group list and inversion-subset enumeration are complete and every finite witness is independently validated; the outputs alone, without the exhaustive source and certificates, would not be enough.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky (first posted 2015-02-04) provide the classical background on colour-refinement orbits, individualization and related graph properties. Kluge (first posted 2022-04-03), especially Section 4, proves exact rooted classes for Cayley graphs of **prime** order and provides a sixteen-vertex abelian Cayley failure. Neither inspected result asserts the exhaustive all-abelian lower bound through order fifteen. The present claim deliberately excludes novelty for the upper-bound example and concerns only the missing sharp minimum.

## Limitations
This is an exhaustive finite boundary, not an all-order classification and not a graph-isomorphism identification theorem. The certificate assumes the conventional classification of finite abelian groups and exact integer arithmetic. Full scholarly priority could be affected by an earlier specialized low-order abelian Cayley census not located in the inspected literature. The results have undergone only self-review, not independent scientific audit.

## References
1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public version 2015-02-04), https://arxiv.org/abs/1502.01255 ; especially the individualization and orbit discussion.
2. L. Kluge, *Combinatorial refinement on circulant graphs*, arXiv:2204.01054 (first public version 2022-04-03), https://arxiv.org/abs/2204.01054 ; especially Section 4 and its order-sixteen example.
