# One-vertex-fault Hamilton laceability in four exceptional cubic symmetric girth-six graphs

## Finding
Consider the four cubic symmetric graphs of girth six distinguished in the classification of Kutnar and Marušič: the Heawood graph \(H\), Möbius–Kantor graph \(M\), Pappus graph \(P\), and Desargues graph \(D\). All four are Hamilton-laceable: for every pair of opposite-part vertices there is a spanning path with those endpoints.

For a bipartite graph \(G\) with equally sized parts, call a deleted vertex \(v\) **universally path-tolerant** if every pair of *distinct* vertices in the bipartition class opposite to \(v\) are endpoints of a Hamilton path in \(G-v\). A graph is **hyper-Hamilton-laceable** if it is Hamilton-laceable and every vertex is universally path-tolerant, following the definition of Araki.

**Theorem.** The graphs \(H,P,D\) are hyper-Hamilton-laceable. The graph \(M\) is Hamilton-laceable but not hyper-Hamilton-laceable. For every \(v\in V(M)\), exactly one unordered pair \(\{a,b\}\) in the class opposite to \(v\) fails to be joined by a Hamilton path in \(M-v\). This pair has the intrinsic, and uniquely characterizing, distance signature
\[
d_M(v,a)=d_M(v,b)=3,\qquad d_M(a,b)=4.
\]
All other admissible deleted-vertex endpoint pairs work. No assertion is made about all cubic symmetric graphs beyond these four specified examples.

## Assumptions and scope
Graphs are finite, simple and undirected. Vertices are labeled for reproducible certificates, not to identify isomorphism classes. Use the following exact adjacency models:

* Heawood: vertices \(p_i,\ell_j\), indices in \(\mathbb Z/7\mathbb Z\), with \(p_{j+t}\sim\ell_j\) for \(t\in\{0,1,3\}\). Encode \(p_i=i\) and \(\ell_j=7+j\).
* Möbius–Kantor: \(G(8,3)\), with \(u_i=i\), \(w_i=8+i\) for \(0\le i<8\), and edges \(u_i u_{i+1},u_iw_i,w_iw_{i+3}\), indices modulo \(8\).
* Pappus: points \(p_{x,y}\) and nonvertical affine lines \(\ell_{m,b}\) over \(\mathbb F_3\), incident when \(y=mx+b\). Encode \(p_{x,y}=3x+y\), \(\ell_{m,b}=9+3m+b\).
* Desargues: \(G(10,3)\), using the preceding generalized-Petersen edge definition with \(10\) instead of \(8\).

Each listed graph is connected, cubic, bipartite, and vertex-transitive; these facts are also verifiable from the explicit finite adjacency data and automorphism certificates in `witness_certificate.json`. In the chosen labeling vertex \(0\) is a point/rim vertex. `opposite_part` lists precisely the vertices of odd distance from \(0\).

## Proof
The proof is a finite certificate with a small independent negative obstruction. The certificate provides, for each of the four graphs:

1. For every opposite-part vertex \(z\), a Hamilton path in the full graph from \(0\) to \(z\). This proves Hamilton laceability for one starting vertex.
2. For every unordered pair \(\{a,b\}\) of distinct opposite-part vertices other than \(\{10,14\}\) in the Möbius–Kantor case, a Hamilton path from \(a\) to \(b\) in the graph with vertex \(0\) removed. In the three other cases there are no exceptions.
3. For each vertex \(v\), an explicit adjacency-preserving permutation taking \(0\) to \(v\). Applying such a permutation to the paths in (1)–(2) transports the claims to every possible starting or deleted vertex. These permutations can exchange the bipartition classes, which is necessary when the removed vertex moves between parts.

`verify_certificate.py` independently constructs all four adjacency sets, verifies every supplied permutation and every path (adjacent successive vertices, no repetitions, correct endpoints, and exactly the required vertex set), and checks that each graph has precisely the listed certificate coverage. Thus the positive cases are constructive finite proofs rather than probabilistic experiments.

Here is an independent proof of the sole impossibility. In \(M=G(8,3)\), delete vertex \(0\) and suppose that a Hamilton path \(Q\) from \(10\) to \(14\) remains. Vertices \(1,7,8\), being the three neighbors of the deleted vertex, have degree two in \(M-0\) and are not endpoints of \(Q\); hence both of their remaining edges must belong to \(Q\). Let \(S\) be the unused edges of \(M-0\). They lie in the subgraph on the twelve vertices outside \(\{0,1,7,8\}\). On that twelve-vertex set, every vertex except \(10,14\) has degree exactly one in \(S\), and \(10,14\) each have degree exactly two in \(S\). That induced subgraph has exactly fifteen edges. Exhausting its \(2^{15}\) edge subsets under these degree constraints produces exactly **six** admissible unused-edge sets. For each of the six, \((M-0)-S\) has exactly two connected components, never a Hamilton path. The complete elementary enumeration and connectedness tests are implemented in `verify_certificate.py`, independently of the separate subset-DP code. This contradiction excludes \(\{10,14\}\).

The distance vector from \(0\), also independently checked against adjacency, has five vertices at distance three: \(3,5,10,12,14\). Their only mutual-distance-four pair is \(\{10,14\}\). Hence the exceptional pair is characterized intrinsically, and the vertex-transitivity certificates establish that the same unique exception occurs at every deleted vertex.

## Verification
Run `python3 verify_certificate.py` alongside `witness_certificate.json`. This uses only the standard library; it checks every positive path, automorphism, and the six-case nonexistence obstruction and returns `ALL_VERIFY_OK`.

A separately implemented exhaustive Hamilton-path counter is `independent_dp.cpp`. Compile and run with `g++ -std=c++17 -O3 independent_dp.cpp -o independent_dp && ./independent_dp`. Its bitmask recurrence is
\[
F_{S\cup\{w\}}(w)\mathrel{+}=F_S(u)
\]
for every graph edge \(uw\) with \(u\in S\), \(w\notin S\), seeded at a singleton start state. It tests both the full graph and all deleted-vertex endpoint pairs at root \(0\). The four missing-pair counts are respectively \(0,1,0,0\), with the sole zero corresponding to \(\{10,14\}\) in \(M\). Its smallest positive number of paths after a deletion is respectively \(2,2,4,4\). Full recorded command outputs are provided in `witness_verification.txt` and `dp_verification.txt`.

Optional regeneration of the explicit witness data uses `python3 generate_certificate.py` with NetworkX installed; regeneration is not needed to verify the included certificates.

## Relationship to prior work
Araki (2006) defines hyper-Hamilton laceability and establishes it for Cayley graphs generated by transpositions of symmetric groups, a different family that does not imply the present four-graph classification. Pensaert's 2002 thesis studies ordinary Hamilton paths in generalized Petersen graphs and explicitly treats \(G(10,3)\) as Hamilton-laceable; its general result does not give the one-vertex-deletion criterion. Kutnar and Marušič (2009) isolate exactly these four exceptional cubic symmetric girth-six graphs within their structural classification; their abstract describes symmetry and covering classifications, not fault-tolerant Hamilton paths. Direct searches and comparison against accessible mathematical records did not identify a theorem that implies this joint fault-tolerance classification.

## Limitations
This theorem is exact only for the four named graphs, not for all cubic symmetric graphs, all generalized Petersen graphs, or multiple simultaneous vertex failures. No independent external audit or publication-priority certification has been performed. Prior-literature coverage has residual uncertainty, particularly the complete text of Kutnar and Marušič (2009), which was not accessible without additional authorization. That source is relevant to the natural choice of the four graphs, but its accessible abstract does not describe the present path criterion. The computer-assisted parts are fully finite, deterministic and independently inspectable; they are not extrapolated to infinite families.

## References
1. T. Araki, *Hyper hamiltonian laceability of Cayley graphs generated by transpositions*, Networks 48 (2006), 121–124. DOI: `10.1002/net.20126`. First published 2006-08-01.
2. W. P. J. Pensaert, *Hamilton Paths in Generalized Petersen Graphs*, University of Waterloo master's thesis (2002), available at `https://uwspace.uwaterloo.ca/bitstreams/7cc61092-4ed6-4c50-8ce7-eca31cf98db4/download` (48 pages; inspected definitions, result, constructions and conclusion).
3. K. Kutnar and D. Marušič, *A complete classification of cubic symmetric graphs of girth 6*, Journal of Combinatorial Theory, Series B 99 (2009), 162–184. DOI: `10.1016/j.jctb.2008.06.001` (abstract inspected; complete text unavailable).
4. H. H. Glover and D. Marušič, *Hamiltonicity of cubic Cayley graphs*, Journal of the European Mathematical Society 9 (2007), 775–787. DOI: `10.4171/JEMS/96` (abstract inspected; proves a different ordinary Hamiltonicity claim).
