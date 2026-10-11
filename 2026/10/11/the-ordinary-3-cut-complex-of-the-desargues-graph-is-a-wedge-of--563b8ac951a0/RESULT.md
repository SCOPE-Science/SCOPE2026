# The ordinary \(3\)-cut complex of the Desargues graph is a wedge of \(111\) sixteen-spheres
## Finding
Let \(D=G(10,3)\) be the Desargues graph on vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). For the ordinary \(3\)-cut complex \(\Delta_3(D)\), whose facets are complements of disconnected induced three-vertex sets,
\[
\Delta_3(D)\simeq\bigvee^{111}S^{16}.
\]

## Assumptions and scope
The graph is the standard generalized Petersen graph \(G(10,3)\). The cut complex is the ordinary cut complex of Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue, not the total cut complex. The claim concerns this single finite graph and does not assert shellability or a classification of cubic graphs.

## Proof
The verifier reconstructs \(D\), checks that it is cubic with girth \(6\), and enumerates all induced three-vertex sets. Exactly \(60\) triples are connected and \(1080\) are disconnected. It also directly checks every four-vertex set contains a disconnected triple. Hence every face of size at most \(16\) occurs, and the top-dimensional faces are exactly the \(1080\) seventeen-vertex complements of disconnected triples. Thus \(\Delta_3(D)\) has dimension \(16\).

Apply sequential element matchings in the vertex order \(u_0,\ldots,u_9,v_0,\ldots,v_9\): at stage \(x\), pair each still-unmatched face not containing \(x\) with its union with \(x\) whenever both are faces. A sequence of element matchings is acyclic, as used explicitly for cut complexes in the cited primary source. Exhaustive replay gives \(524096\) matched pairs and leaves exactly one critical \(0\)-cell and \(111\) critical \(16\)-cells, with no other critical cells. Forman's discrete Morse theorem therefore gives a CW complex with one vertex and only \(111\) cells in dimension \(16\), which is precisely \(\bigvee^{111}S^{16}\).

## Verification
`verify.py` independently reconstructs the graph, computes girth, classifies all \(1140\) triples, verifies the complete lower skeleton condition over all \(4845\) four-subsets, constructs all \(1048304\) nonempty faces, replays the sequential element matching, and checks the critical-cell counts. The face vector is
\[
(20,190,1140,4845,15504,38760,77520,125970,167960,184756,167960,125970,77520,38760,15504,4845,1080).
\]
Its Euler characteristic is \(112\), so the reduced Euler characteristic is \(111\), agreeing with the Morse result. The digest of the sorted critical top-cell masks is `686fcf8e6826ee297ec9dc6f85dc9447006126414381e7377b4c78cb141672f8`.

## Relationship to prior work
The primary source defines ordinary cut complexes, proves the complete-skeleton criterion and gives a general two-degree homology bound under that criterion. Its table of exact families includes complete multipartite graphs, cycles, squared cycles, clique prisms, trees, and threshold graphs; a full-text search finds no Desargues occurrence. The source also distinguishes ordinary cut complexes from total cut complexes. published-finding corpus searches for the Desargues graph, its alias \(G(10,3)\), ordinary \(3\)-cut complexes, and the exact wedge count found no statement implying this homotopy type. The closest records concern total cut complexes of other graphs or unrelated Desargues invariants.

## Limitations
The result is specific to the Desargues graph. It does not establish shellability, a general theorem for cubic graphs, or an independent audit. The discrete-Morse acyclicity step uses the standard theorem that sequential element matchings are acyclic; the finite matching itself is completely replayed by the verifier.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1, first posted 2023-04-26; SIAM J. Discrete Math. 38 (2024), DOI 10.1137/23M1569034. Primary MSC listed first: 57M15.
