# The Heawood-to-\(C_5\) Hom complex is a circle
## Finding
Let \(H\) be the Heawood graph, realized as the point-line incidence graph of the Fano plane, and let \(C_5\) be the loopless five-cycle. Then \(\operatorname{Hom}(H,C_5)\simeq S^1\). Its \(0\)-skeleton consists of exactly \(3300\) graph homomorphisms \(H\to C_5\); its \(1\)-skeleton is connected, has exactly \(11340\) edges, and has graph diameter \(35\).

The \(1\)-skeleton is the single-vertex recoloring graph: two homomorphisms are adjacent exactly when they differ at one vertex of \(H\). Thus the quantitative statement also says that every \(C_5\)-coloring of the Heawood graph can be reconfigured to every other one by valid single-vertex changes, and that the largest shortest-path distance between two such colorings is \(35\).

## Assumptions and scope
The Heawood graph \(H\) is represented as the bipartite incidence graph of the Fano plane. Its point vertices are \(p_i\) and its line vertices are \(\ell_i\), for \(i\in\mathbb Z/7\mathbb Z\), with \(p_j\) incident to \(\ell_i\) exactly when \(j-i\in\{0,1,3\}\). The target \(C_5\) has vertex set \(\mathbb Z/5\mathbb Z\) and edges between residues differing by \(\pm1\).

Here \(\operatorname{Hom}(H,C_5)\) is the standard graph Hom complex. The homotopy statement uses the cycle-codomain criterion of Fujii, Iwamasa, Kimura, Nozaki and Suzuki. No assertion is made for other cubic cages, other odd cycles, or equivariant Hom-complex structure.

## Proof
The finite part of the proof is exhaustive. The verifier reconstructs the Fano incidence graph, checks that it has \(14\) vertices, \(21\) edges and degree \(3\) at every vertex, and verifies that every pair of points lies on exactly one common line. It then recursively enumerates every function \(V(H)\to V(C_5)\) that preserves adjacency. The recursion branches over all five target values for each source vertex and rejects a branch only when an already assigned edge violates the \(C_5\) adjacency relation. Exactly \(3300\) homomorphisms survive.

For each surviving homomorphism, every legal change at one source vertex is generated directly. This produces the complete \(1\)-skeleton of \(\operatorname{Hom}(H,C_5)\), with \(11340\) undirected edges. Breadth-first search visits all \(3300\) vertices from one start, so the Hom complex has one connected component. Breadth-first search from every vertex gives diameter \(35\) and radius \(35\).

It remains to identify the homotopy type of the unique component. Consider the homomorphism \(f\) that maps every Fano point to \(0\) and every Fano line to \(1\). For the orientation \(\vec H_f\) of Fujii et al., every incidence edge points from its point endpoint to its line endpoint, because \(f(\ell)-f(p)=1\pmod 5\). Hence \(\vec H_f\) is acyclic. Theorem 5.1 of arXiv:2408.04802 says that the connected component containing such an \(f\) is homotopy equivalent to a circle. Since the exhaustive recoloring graph is connected, that component is the whole Hom complex, proving
\[
\operatorname{Hom}(H,C_5)\simeq S^1.
\]

## Verification
Run `python3 verify_heawood_c5_hom.py` beside `verification_data.json`. The script uses only the Python standard library. It reconstructs \(H\) from the Fano incidence rule, enumerates all \(3300\) homomorphisms, regenerates all \(11340\) recoloring edges, verifies connectivity, runs all-source breadth-first searches to check diameter and radius \(35\), and checks a complete topological ordering of \(\vec H_f\). A successful replay ends with `HEAWOOD_C5_HOM_VERIFY_OK`.

The reconfiguration-degree distribution is also checked independently inside the replay: \(210\) vertices have degree \(4\), \(700\) have degree \(5\), \(840\) have degree \(6\), \(980\) have degree \(8\), \(420\) have degree \(9\), \(140\) have degree \(11\), and \(10\) have degree \(14\).

## Relationship to prior work
Fujii, Iwamasa, Kimura, Nozaki and Suzuki prove that for every connected graph \(G\) and cycle \(C_k\), the complex \(\operatorname{Hom}(G,C_k)\) is a disjoint union, up to homotopy, of points and circles. Their Theorem 5.1 gives a criterion for the type of a component containing a specified homomorphism. Those results do not determine how many components occur for the Heawood graph, whether its \(3300\) \(C_5\)-colorings all reconfigure together, or the diameter of that recoloring graph. Full-text inspection of that paper found no occurrence of “Heawood” or “Fano”.

Wrochna gives a polynomial-time algorithm for the homomorphism-reconfiguration problem when the target contains no \(4\)-cycle, which includes \(C_5\). That algorithmic theorem establishes decidability of reachability but does not state the Heawood instance, its complete connectedness, the count \(3300\), the diameter \(35\), or the homotopy type of the whole complex.

Earlier work of Čukić and Kozlov determines Hom complexes when both source and target are cycles. The Heawood graph is not a cycle, so that family does not imply the present instance. Targeted searches under the Heawood, Fano-incidence, \(C_5\)-coloring, Hom-complex and reconfiguration formulations found no equivalent or stronger published statement.

## Limitations
This is an exact finite result for one canonical graph-target pair. The homotopy step invokes the published cycle-codomain theorem rather than reconstructing its universal-cover argument from scratch. The finite enumeration and diameter calculation are exhaustive, but they do not yield a family theorem for incidence graphs or cages. Literature search cannot exclude an unindexed computation stated under different terminology.

## References
1. S. Fujii, Y. Iwamasa, K. Kimura, Y. Nozaki, A. Suzuki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are cycles*, arXiv:2408.04802v1, first public 2024-08-09; J. Appl. Comput. Topol. 9 (2025), Article 21, DOI 10.1007/s41468-025-00219-7.
2. M. Wrochna, *Homomorphism Reconfiguration via Homotopy*, SIAM J. Discrete Math. 34 (2020), 328–350, DOI 10.1137/17M1122578.
3. S. L. Čukić, D. N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, Discrete Comput. Geom. 36 (2006), 313–329.
