# A vertex-essential \(5\)-sphere in the generalized Petersen independence complex

## Finding
Let \(G=GP(9,2)\) be the generalized Petersen graph with outer vertices \(u_i\), inner vertices \(v_i\), and indices \(i\in\mathbb Z/9\mathbb Z\). Its ordinary independence complex \(K=\operatorname{Ind}(G)\) satisfies
\[
K\simeq S^5,\qquad \widetilde H_5(K;\mathbb Z)\cong\mathbb Z.
\]
**Every one-vertex induced deletion is simplicially collapsible**: for every \(x\in V(G)\), the induced subcomplex \(K[V(G)\setminus\{x\}]\) collapses to a point. Consequently, for every proper vertex subset \(W\subsetneq V(G)\), the inclusion-induced map
\[
\widetilde H_5(K[W];\mathbb Z)\longrightarrow\widetilde H_5(K;\mathbb Z)
\]
is zero. All eighteen graph vertices are therefore necessary to support any cycle representing a nonzero ambient integral fifth-homology class. Under the natural dihedral action \(D_9\) on the graph, the rank-one integral homology module is trivial on rotations and is multiplied by \(-1\) under reflections.

## Assumptions and scope
The graph is simple and has the eighteen labeled vertices \(u_i=i\) and \(v_i=9+i\), for \(0\le i\le8\), with exactly the edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+2}\}\), indices modulo nine. A face of \(K\) is any subset containing no graph edge. The empty face participates only in the augmented face-poset matching. All homotopy and homology assertions are about this one finite graph, not the entire generalized Petersen family.

## Proof
**Finite face enumeration.** Enumerate all \(2^{18}\) binary masks, retain exactly those containing no edge, and order them numerically. Including the empty face there are \(2461\) faces. The numbers of nonempty faces in dimensions \(0,1,2,3,4,5,6\) are respectively
\[
(18,126,438,801,747,303,27).
\]
In particular the complex is six-dimensional; the sphere dimension asserted here is a homotopy dimension, not its combinatorial dimension.

**Acyclic matching and the sphere.** Given a total order \(\pi\) of the eighteen vertices, start with all available faces (including the empty face). Sequentially for each vertex \(a\) in \(\pi\), pair any as-yet-unpaired face \(\sigma\) not containing \(a\) with \(\sigma\cup\{a\}\), if both are present, processing eligible lower faces in increasing binary-mask order. Remove each pair from further consideration. To test acyclicity, orient every codimension-one Hasse edge from its upper face to its lower face, except matched edges, which are oriented upwards. A topological sort of this directed graph must visit every face.

For the vertex order \((0,1,\ldots,17)\), the exhaustive check gives \(1230\) matched pairs and one unpaired face, of cardinality six (mask `101648`). The directed Hasse graph is acyclic on all \(2461\) faces. The empty face is matched with a vertex. Dropping just that empty-face pair yields the usual finite acyclic discrete-Morse matching with one critical vertex and one critical five-simplex. The resulting Morse CW complex has one zero-cell and one five-cell, with no possible nontrivial attaching map; hence \(K\simeq S^5\), including the claimed integral homology.

**Actual elementary collapses after either type of vertex deletion.** There are two natural rotational vertex orbits, the nine outer and nine inner vertices. For deletion of \(u_0\), take the order
`(17,13,4,3,6,10,11,8,9,16,14,15,1,5,2,0,12,7)`.
The induced complex has \(1878\) faces including the empty face. All of them form \(939\) matching pairs, with an acyclic directed Hasse graph. For deletion of \(v_0\), use
`(6,14,15,16,9,8,2,17,11,12,5,0,10,1,3,13,4,7)`.
This complex has \(1874\) faces including the empty face, all comprising \(937\) matching pairs; its directed Hasse graph is also acyclic. In both cases, omit the matched pair containing the empty face to leave one vertex critical. A separate deterministic free-face-elimination check realizes the matchings as **\(938\)** and **\(936\)** genuine elementary simplicial collapses, respectively, leaving exactly one vertex. Rotations of the graph carry each representative deletion to all eight others of its type. Thus all eighteen one-vertex deletions collapse.

For any proper \(W\), choose \(x\notin W\). The inclusion \(K[W]\hookrightarrow K\) factors through \(K[V\setminus\{x\}]\), whose positive-degree reduced homology vanishes. This proves the universal support statement without assuming that \(K[W]\) itself is contractible.

**The dihedral orientation character.** The graph automorphisms \(r:u_i\mapsto u_{i+1},v_i\mapsto v_{i+1}\) and \(s:u_i\mapsto u_{-i},v_i\mapsto v_{-i}\) generate the natural dihedral action. For a permutation \(g\), compute the reduced Lefschetz number by summing \((-1)^d\) times the signed trace on \(d\)-simplices, including the augmented degree \(-1\). Only \(\widetilde H_5(K;\mathbb Z)\) is nonzero, so \(\widetilde L(g)=-\operatorname{tr}(g\mid\widetilde H_5)\). Nonidentity rotations have no fixed nonempty independent set under the one-step generator, giving \(\widetilde L(r)=-1\). For reflection \(s\), the signed chain traces in augmented degrees \((-1,0,1,2,3,4,5,6)\) are \((1,2,-6,-10,9,11,-3,-1)\), giving \(\widetilde L(s)=1\). Therefore \(r\) acts by \(+1\) and \(s\) by \(-1\). The verifier directly checks the resulting sign character for all eighteen dihedral elements.

## Verification
Run `python3 verify_gp92.py` with Python 3 and no third-party dependencies. It reconstructs all faces and matching pairs from the graph definition, verifies the directed Hasse graphs are acyclic by exhaustive topological sorting, constructs actual free-face collapse sequences for the two representative deletions, checks the rotational/reflection graph symmetries and computes signed simplicial Lefschetz traces. The executable source is included alongside this document, and none of its inputs depend on external records.

## Relationship to prior work
Barmak's 2010 *Star clusters in independence complexes of graphs* proves that the independence complex of any triangle-free graph is homotopy equivalent to a suspension (Theorem 3.4). This applies to the present graph but neither specifies a five-sphere nor determines its vertex-deletion collapsibility and dihedral orientation character. Fox, Gera, and Stănică (2012), *The Independence Number for the Generalized Petersen Graphs*, prove the independence-number formula \(\alpha(GP(n,2))=\lfloor4n/5\rfloor\) for \(n\ge5\). For \(n=9\) this gives \(\alpha=7\), agreeing with the seven-vertex maximal independent sets in the face enumeration, but does not determine the homotopy, collapse, or group action. Calculations for \(GP(10,2)\) concern a different graph and do not imply this result.

## Limitations
The claim concerns homotopy equivalence rather than a triangulated PL-homeomorphism to a sphere. It asserts that proper induced subcomplexes carry no *ambient* nonzero fifth-homology class; it does not assert that every proper induced subcomplex is itself contractible. It gives no recurrence or classification for other \(GP(n,k)\). The finite exhaustive proof is reproducible but no independent human or third-party mathematical audit has been performed.

## References
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, initial public version 2010-07-02, https://arxiv.org/pdf/1007.0418.
- J. Fox, R. Gera, P. Stănică, *The Independence Number for the Generalized Petersen Graphs*, Ars Combinatoria **103** (2012), 439–451, https://combinatorialpress.com/article/ars/Volume%20103/volume-103-paper-37.pdf.
