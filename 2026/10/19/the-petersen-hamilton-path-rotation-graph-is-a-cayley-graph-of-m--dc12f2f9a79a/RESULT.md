# The Petersen Hamilton-path rotation graph is a Cayley graph of \(\mathfrak S_5\)

## Finding
Let \(P=KG(5,2)\) be the Petersen graph, whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent when the subsets are disjoint. Identify an undirected Hamiltonian path with its reversal. Construct the rotation graph \(\mathcal R(P)\) on all such paths, putting an edge between two paths precisely when one is obtained from the other by a single elementary Pósa rotation at **either** endpoint.

**Theorem.** The natural \(\mathfrak S_5\)-action on the 120 undirected Hamiltonian paths is simply transitive, and \(\mathcal R(P)\) is the right Cayley graph
\[
\mathcal R(P)\cong\operatorname{Cay}\!\left(\mathfrak S_5,\{\alpha,\alpha^{-1},\beta,\gamma\}\right),
\quad\alpha=(1\,2\,3\,4),\quad\beta=(1\,4),\quad\gamma=(0\,1)(3\,4).
\]
Consequently this rotation graph is connected, four-regular, has 120 vertices and 240 edges, and has diameter exactly six. Its distance-sphere sizes about **every** vertex are
\[
(1,4,11,25,39,29,11).
\]
In addition, all 120 Hamiltonian paths have nonadjacent endpoints: each of the 30 nonadjacent vertex pairs is the endpoint pair of exactly four paths, while no adjacent pair occurs.

## Assumptions and scope
Everything here concerns the ordinary, simple Petersen graph and **undirected spanning paths modulo reversal**. In a path \(v_0,v_1,\ldots,v_9\), a rotation about the endpoint \(v_9\) chooses an index \(0\le i\le7\) for which \(v_iv_9\) is an edge, deletes \(v_iv_{i+1}\), inserts \(v_iv_9\), and reverses the resulting tail:
\[
(v_0,\ldots,v_i,v_9,v_8,\ldots,v_{i+1}).
\]
The symmetric operation at \(v_0\) is also allowed. Distinct normalized resulting paths define adjacency; there are no loops, multiple edges, arbitrary edge switches, or changes to the underlying vertex set. A generator permutation is recorded as its action on \(\{0,1,2,3,4\}\); multiplication \(g s\) means applying \(s\) first, then \(g\).

Use lexicographic vertex indices \(0,\ldots,9\) for the pairs
\[
01,02,03,04,12,13,14,23,24,34,
\]
where, in this one indexing display, a two-digit entry denotes an unordered pair, not a number. With these indices, fix the Hamiltonian path
\[
p=(0,9,4,2,8,5,3,7,6,1).
\]

## Proof
**1. Exact Hamilton-path count.** For a fixed terminal vertex \(t\), let \(F_t(v,B)\) denote the number of simple paths beginning at \(v\), using precisely the vertices in \(\{v\}\cup B\), and finishing at \(t\). For a subset \(B\) disjoint from \(\{v\}\), the exact recurrence is
\[
F_t(v,\varnothing)=[v=t],\qquad F_t(v,B)=\sum_{w\in N_P(v)\cap B} F_t(w,B\setminus\{w\}).
\]
It follows by partitioning such paths according to their first edge; it has no probabilistic or truncation assumption. Using the explicit disjointness adjacency in \(KG(5,2)\), its complete ten-vertex evaluation yields
\[
F_1\bigl(0,V(P)\setminus\{0\}\bigr)=4,\qquad
F_7\bigl(0,V(P)\setminus\{0\}\bigr)=0.
\]
The computation is independently checked by direct enumeration of all ten-vertex permutations in `verify_independent.py`. The group \(\mathfrak S_5\) acts transitively on the 30 unordered pairs of **nonadjacent** Petersen vertices (pairs of two-subsets meeting in one symbol), and separately on the 15 unordered **adjacent** pairs (disjoint two-subsets). Therefore exactly \(30\cdot4+15\cdot0=120\) undirected Hamiltonian paths exist. For the first displayed endpoint pair, the four complete paths are listed in `cayley_certificate.json` and checked independently.

**2. Simple transitivity.** The natural action on two-subsets preserves all edges and therefore all paths. The orbit of \(p\) has 120 elements. Indeed, an element fixing the ordered path \(p\) fixes all ten distinct two-subsets and hence all five labels; an element reversing \(p\) would exchange the endpoint pairs \(\{0,1\}\) and \(\{0,2\}\), so it must fix label \(0\), exchange labels \(1\) and \(2\), and preserve \(\{3,4\}\). But then it cannot send the second vertex of \(p\), namely \(\{3,4\}\), to the penultimate vertex \(\{1,4\}\). Thus the undirected-path stabilizer is trivial. The orbit, of order \(|\mathfrak S_5|=120\), is the entire set found in step 1.

**3. Generators of elementary rotations.** Each endpoint of \(p\) has three graph neighbors, exactly one being its adjacent vertex on the path, and the other two internal to the path: the opposite endpoints are not adjacent by step 1. Hence two elementary rotations are possible at each endpoint. Directly substituting the indexed pairs in the rotation formula gives **four distinct** neighboring undirected paths, namely the images of \(p\) under
\[
\alpha=(1\,2\,3\,4),\quad\alpha^{-1}=(1\,4\,3\,2),\quad\beta=(1\,4),\quad\gamma=(0\,1)(3\,4).
\]
In the same order, the four **reversal-normalized** neighbor paths (using the indices above) are `1,6,7,3,5,8,0,9,4,2`; `0,9,4,2,8,5,1,6,7,3`; `1,6,7,0,9,4,2,8,5,3`; and `0,9,1,6,7,3,5,8,2,4`. Each can be checked directly from the ten listed two-subsets and the displayed rotation formula. The action commutes with the rotation operation, so the four neighbors of \(g p\) are exactly \(g\alpha p\), \(g\alpha^{-1}p\), \(g\beta p\), and \(g\gamma p\). Under the identification \(g\leftrightarrow g p\), this is exactly the asserted right Cayley graph. The cycle \(\alpha\) and the transposition \(\beta\) generate the symmetric group on \(\{1,2,3,4\}\); the product of \(\gamma\) with the available transposition \((3\,4)\) gives \((0\,1)\). They therefore generate all \(\mathfrak S_5\), proving connectedness without reliance on a connectivity computation.

**4. Exact diameter and sphere distribution.** Breadth-first search in the explicitly defined four-generator Cayley graph, starting at the identity, yields successive sphere sizes \(1,4,11,25,39,29,11\) and no vertices beyond distance six. The recurrence for exact shortest distances is \(d(e)=0\) and \(d(h)=1+\min_{s\in\{\alpha,\alpha^{-1},\beta,\gamma\}}d(hs)\) for any nonidentity \(h\), interpreted by graph breadth-first exploration. The complete 120-row distance-and-neighbor certificate is `cayley_certificate.json`, verified row by row by `verify_posa.py`. In particular, there are eleven vertices at distance six, proving the lower bound as well as the upper bound. Right-Cayley vertex transitivity gives the same profile at every vertex.

## Verification
Run the two separate standard-library programs from the same directory as `cayley_certificate.json`:

```sh
python3 verify_posa.py
python3 verify_independent.py
```

The first evaluates the endpoint recurrence, enumerates all 120 label permutations, verifies the four generators and exact distances, and verifies **every row** of the certificate. The second independently enumerates undirected Hamilton paths by brute-force vertex permutations, constructs the endpoint-rotation graph without using group generators or the certificate, checks four-regularity and 240 edges, and performs a breadth-first search from every one of the 120 paths. Both must reproduce the asserted component, size, and distance statistics. The certificate uses lexicographic two-subset indices defined above, and contains the entire Cayley vertex/adjacency/distance census.

## Relationship to prior work
Pósa rotations are a classical Hamiltonicity technique; this note does **not** claim to introduce them. Oberdorf, Ferguson, Jacobsen, and Kondev (2005 preprint; 2006 journal version) describe the equivalent endpoint *backbite* move for Hamiltonian walks on square lattices, and illustrate a small reconfiguration graph of square-grid walks. Their underlying graph and classification differ from the Petersen graph. Frieze and Pittel (2011 preprint) use Pósa rotations in random-graph path arguments. Kazazi (arXiv:2610.05068v1, 2026) studies exactly the same abstract backbite reconfiguration graph, proving connectivity under a spanning squared-path hypothesis and constructing disconnected examples; its full text contains no Petersen-specific claim or Cayley classification. Its sufficient hypothesis cannot hold here because a squared ten-vertex path has internal degree four while the Petersen graph is cubic. Standard Petersen-graph catalogues give its \(\mathfrak S_5\) automorphism group and non-Hamiltonicity, which alone do not determine the full Hamilton-path rotation graph or its Cayley generators and diameter. The claimed contribution is specifically the **complete Petersen rotation-graph identification and metric classification**.

## Limitations
This theorem is finite and specific to the Petersen graph; no general connectedness theorem for Pósa rotation graphs is claimed. Although the two exhaustive implementations are mathematically complete for ten vertices, they are not third-party certification. Historical priority may be affected by older, unindexed backbite or Hamilton-path transition tables, particularly data unavailable in full text. A proof of the finite distance profile depends on the included fully specified enumeration; no hand-only derivation of those seven coefficients is claimed.

## References
- L. Pósa, *Hamiltonian Circuits in Random Graphs*, Discrete Mathematics **14** (1976), 359–364, DOI `10.1016/0012-365X(76)90068-6` (rotation method).
- R. Oberdorf, A. Ferguson, J. L. Jacobsen and J. Kondev, *Secondary Structures in Long Compact Polymers*, arXiv:`cond-mat/0508094v1`, first posted 2005-08-03; Physical Review E **74** (2006), 051801, DOI `10.1103/PhysRevE.74.051801` (backbite definition and grid examples).
- A. Frieze and B. Pittel, *On a sparse random graph with minimum degree three: Likely Pósa sets are large*, arXiv:`1107.4944v1`, first posted 2011-07-25 (Pósa-rotation context).
- A. Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*, arXiv:`2610.05068v1`, first posted 2026-10-04 (exact backbite-reconfiguration formalism; dense/spanning-squared-path hypotheses, with no Petersen case).
- A. E. Brouwer, *Petersen graph*, online graph catalogue, `https://aeb.win.tue.nl/graphs/Petersen.html` (Petersen automorphisms and basic properties).
- D. A. Holton and J. Sheehan, *The Petersen Graph*, Cambridge University Press, 1993 (background monograph; no complete full-text comparison asserted).
