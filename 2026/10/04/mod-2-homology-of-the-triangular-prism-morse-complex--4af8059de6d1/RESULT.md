# Mod-\(2\) homology of the triangular-prism Morse complex
## Finding
For the triangular prism graph \(P=C_3\mathbin{\square}K_2\), let \(\mathcal M(P)\) be the Morse complex whose simplices are acyclic discrete vector fields on \(P\). Then its reduced mod-\(2\) homology is concentrated in degree \(4\): \(\widetilde H_4(\mathcal M(P);\mathbb F_2)\cong\mathbb F_2^{64}\), while \(\widetilde H_i(\mathcal M(P);\mathbb F_2)=0\) for every \(i\ne4\).

## Assumptions and scope
The triangular prism graph is \(P=C_3\mathbin{\square}K_2\), with vertices \(0,1,2\) on one triangle, \(3,4,5\) on the other, and vertical edges \(03,14,25\). A vertex of \(\mathcal M(P)\) is a primitive vector field \((v,e)\) with \(v\) incident to \(e\). A simplex is a set of such pairs with no reused vertex or edge and no closed nontrivial \(V\)-path. Coefficients are \(\mathbb F_2\).

## Proof
For a graph, direct each chosen matched edge from its matched vertex to its other endpoint. Because matched vertices and edges are distinct, a closed nontrivial \(V\)-path is exactly a directed cycle in this partial functional digraph. Thus the simplices can be enumerated exactly by checking distinct matched vertices, distinct matched edges, and absence of directed cycles.

Exhaustive enumeration gives the simplex counts by cardinality \(k\):
\[
(1,18,126,428,705,450),
\]
including the empty simplex first; there are no cardinality-6 simplices. Independently, choose an undirected forest of \(P\). For each nontrivial tree component on \(s\) vertices, a compatible acyclic matching is determined by one of the \(s\) choices of unmatched root. Summing the products of component sizes over all edge-forests reproduces the same face counts.

For the augmented simplicial boundary over \(\mathbb F_2\), the exact ranks from cardinality \(k\) to \(k-1\) are
\[
(1,17,109,319,386)\qquad(k=1,2,3,4,5).
\]
Therefore the reduced Betti ranks in dimensions \(0\) through \(4\) are
\[
(18-1-17,\ 126-17-109,\ 428-109-319,\ 705-319-386,\ 450-386)=(0,0,0,0,64).
\]
This proves the claim.

## Verification
The supplied verifier reconstructs all simplices directly from primitive vector fields and independently reconstructs the face counts from undirected forests and root choices. It builds every augmented boundary matrix, verifies \(\partial^2=0\), computes each rank both from column vectors and from the transposed row representation, checks the graph has \(9\) edges and maximum degree \(3\), and terminates with `VERIFY_OK`.

## Relationship to prior work
Scoville and Zaremsky define this Morse complex and prove that for a graph \(\Gamma\), if \(|E(\Gamma)|\ge m d(\Gamma)+1\), then \(\mathcal M(\Gamma)\) is \((m-1)\)-connected. For the triangular prism, \(|E(P)|=9\) and \(d(P)=3\), so their theorem supplies simple connectivity at \(m=2\) but does not determine the degree-four mod-\(2\) homology. Exact searches for triangular-prism, prism-graph, and directed-forest formulations did not locate a checked source stating the rank \(64\). Courtney's thesis studies directed-forest complexes of Cayley graphs and is a plausible neighboring source; the institutional full text was inaccessible, so possible coverage there is retained as a residual originality risk rather than treated as evidence of absence.

## Limitations
The claim concerns only homology with \(\mathbb F_2\) coefficients for this one graph. No integral-homology, torsion, homotopy-type, minimality, or all-prism statement is asserted. Search failure does not prove novelty, and the inaccessible Cayley-graph thesis remains a specific literature risk.

## References
1. Nicholas A. Scoville and Matthew C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, first version 2020-04-22. Primary MSC 55U05.
2. Kennedy Courtney, *The Directed Forest Complex of Cayley Graphs*, Boise State University M.S. thesis, 2020, DOI 10.18122/td/1684/boisestate.
