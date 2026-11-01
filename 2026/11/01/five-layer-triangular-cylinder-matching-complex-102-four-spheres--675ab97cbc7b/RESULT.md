# Five-layer triangular-cylinder matching complex: \(102\) four-spheres and its full symmetry character

## Finding
Let \(G=C_3\square P_5\) be the Cartesian product of a triangle with a five-vertex path. Let \(M(G)\) be the *ordinary matching complex*: vertices are the edges of \(G\), and simplices are collections of pairwise vertex-disjoint edges. Then there is an integral homotopy equivalence
\[
|M(G)|\simeq \bigvee^{102}S^4.
\]
In particular, \(\widetilde H_4(M(G);\mathbb Z)\cong\mathbb Z^{102}\), while all other reduced integral homology vanishes.

More precisely, the full automorphism group of \(G\) is \(S_3\times C_2\), with \(S_3\) permuting the three row labels and \(C_2\) reversing the path coordinate. If \(\tau\) is this reversal, the rational homology character on conjugacy classes of \(S_3\) (identity, transposition, three-cycle) is
\[
\begin{array}{c|rrr}
&1&(12)&(123)\\\hline
\operatorname{tr}_{\widetilde H_4}(g)&102&0&0\\
\operatorname{tr}_{\widetilde H_4}(g\tau)&12&2&0
\end{array}.
\]
Writing \(T\), \(A\) and \(V\) for the trivial, alternating and two-dimensional standard rational representations of \(S_3\), and \(\varepsilon\) for the nontrivial character of \(C_2\), this determines the entire rational representation:
\[
\begin{aligned}
\widetilde H_4(M(G);\mathbb Q)\cong{}&10(T\boxtimes 1)\oplus7(T\boxtimes\varepsilon)\\
&\oplus9(A\boxtimes1)\oplus8(A\boxtimes\varepsilon)\\
&\oplus19(V\boxtimes1)\oplus15(V\boxtimes\varepsilon).
\end{aligned}
\]
This claim is confined to the specified five-layer cylindrical graph; no corresponding all-length formula is asserted.

## Assumptions and scope
Use the undirected simple graph with vertex set \(\{(r,c):r\in\{0,1,2\},\ 0\leq c\leq4\}\). Edges join \((r,c)\) to \(((r+1)\bmod3,c)\), and \((r,c)\) to \((r,c+1)\) when \(c<4\). Thus \(G\) has fifteen vertices, twenty-seven edges, five triangular layers, and twelve longitudinal edges. The matching complex includes the empty simplex as usual, but the discrete-Morse face poset below consists of nonempty faces. Coefficients for the homotopy and homology claims are integral, and the representation decomposition is over \(\mathbb Q\). No triangle is filled in the graph itself.

## Proof
**Exhaustive face construction.** Order the twenty-seven edges lexicographically by their sorted endpoint pairs, where the first coordinate is the row. Assign indices \(0,\ldots,26\). Identify a face with its twenty-seven-bit edge mask. Begin with the empty mask, and process each edge in order: retain the existing matchings and adjoin the new edge to every matching whose previously used vertices are disjoint from its endpoints. This yields every matching exactly once. The resulting dimension vector is
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)
=(27,279,1399,3558,4338,2100,276).
\]
There are \(11977\) nonempty faces. Independently, a vertex-deletion recurrence for the matching polynomial gives coefficients \((1,27,279,1399,3558,4338,2100,276)\), confirming the face census without using the simplex enumeration.

**A complete acyclic matching.** On the nonempty face poset take the fixed pivot sequence
```
2,1,3,25,6,23,24,16,22,12,21,15,7,10,18,17,14,11,8,5,20,19,4,9,13,0,26
```
For each successive pivot \(p\), list currently unmatched faces \(\sigma\) not containing edge \(p\) in ascending integer-mask order. Whenever \(\sigma\cup\{p\}\) also remains unmatched, pair these two faces and remove both from consideration. This is an unambiguous, reproducible matching on the full Hasse diagram, not a sampled search. The procedure makes \(5937\) disjoint face pairs and leaves one critical zero-simplex and exactly \(102\) critical four-simplices, with none in any other dimension.

To check the critical acyclicity condition, orient each unmatched cover relation from the higher-dimensional face to its codimension-one face, and reverse precisely the \(5937\) matched cover relations. The entire directed graph has \(11977\) vertices and \(55209\) directed incidences. Kahn's topological-sort algorithm removes all \(11977\) vertices, establishing that this graph is acyclic. Since the certificate constructs *every* face, incidence and matching pair from the stated graph and pivot sequence, this is an exhaustive finite proof of the acyclic-matching premise. The complete executable certificate is `verify.py`.

By the discrete-Morse theorem, \(M(G)\) is homotopy equivalent to a CW complex with one zero-cell, \(102\) four-cells and no other cells. Every four-cell attaching map has target the zero-skeleton (a single point), and is nullhomotopic. Hence the resulting space is the wedge of \(102\) four-spheres, proving the integral homotopy assertion. No inference from a finite sample to an infinite graph family is involved.

**Full symmetry group.** The only triangles in \(G\) are its five column triangles, and the two end triangles consist exactly of degree-three vertices. Therefore every graph automorphism induces either the identity or reversal of the five-column path. Once its permutation of one end triangle has been selected, adjacency along the unique longitudinal matching determines its action on all columns, so the entire group is \(S_3\times C_2\).

**Character calculation.** For each of the twelve group elements, compute its permutation of the twenty-seven graph edges. In the oriented simplicial chain complex, a setwise fixed matching contributes the sign of its induced permutation of selected edges. Including the augmentation in degree minus one, the reduced Lefschetz number is the alternating sum of these signed fixed-face traces. Since reduced homology is concentrated in even degree four, the reduced Lefschetz number equals the trace on \(\widetilde H_4\). The direct signed face calculation gives the six class-character values displayed in the finding.

There is an independent orbit computation. A matching fixed by a graph automorphism is a union of full edge-permutation orbits, each of which must itself consist of pairwise disjoint edges. Distinct permitted orbits cannot meet at a graph vertex. If such a matching uses \(k\) permitted orbits, its contribution to the reduced Lefschetz sum is \((-1)^{k-1}\), *including the empty matching with \(k=0\)*. The signed independent-set sum over the permitted orbit-conflict graph reproduces every class-character value without using the signed simplex chain enumeration. Finally, inner products against the irreducible characters of \(S_3\times C_2\), using \(S_3\) conjugacy class sizes \(1,3,2\), give the six multiplicities \(10,7,9,8,19,15\) in the stated order. Their dimension check is \(10+7+9+8+2(19+15)=102\).

## Verification
Run `python3 verify.py` from the directory containing the embedded file. No third-party Python packages are required. The program asserts: graph edge and vertex counts; every matching face and its independently computed matching-polynomial count; the full face vector; Euler characteristic; all matching pairs and their distinctness; all \(55209\) codimension-one relations and a full acyclicity topological sort; critical-cell dimensions; all twelve signed Lefschetz characters; an independent fixed-edge-orbit calculation of the same twelve traces; and all six irreducible multiplicities. A successful replay prints:
```
VERIFY_OK edges=27 faces=11977 incidences=55209 pairs=5937 critical=(1 in degree 0, 102 in degree 4) symmetry=all_12_automorphisms
```
The finite graph and the complete matching algorithm, not previously generated output files, are the checker's inputs. The proof uses the standard discrete-Morse and Lefschetz theorems after these exact combinatorial premises are established.

## Relationship to prior work
Chauhan, Sharma and Shukla (arXiv:2609.27366, first public September 23, 2026) study matching complexes of the **open rectangular** grids \(P_3\square P_n\), proving sharp connectivity and recording low-width homology and homotopy information. The present graph \(C_3\square P_5\) has an extra edge closing each three-vertex column into a triangle, so it is not their grid, and their stated results do not imply either the homotopy or automorphism character here. Earlier rectangular-grid computations and the 2021 claimed three-row all-length homotopy result (subsequently withdrawn for a proof gap) concern the same open-grid distinction.

Bayer, Jelić Milutinović and Vega (arXiv:2211.12559; *Discrete Mathematics*, 2023) prove sphere-wedge results for polygonal **line tilings** whose successive cycles share edges. Here the five column triangles are edge-disjoint and connected by three separate longitudinal edges between consecutive columns. Their polygonal-line theorem therefore has different hypotheses and does not furnish this exact classification. Published matching-complex calculations of other small graphs, including the four-by-four rectangular grid and the cuboctahedral graph, concern nonisomorphic objects and do not imply the present statement. No exact covering result was located in the primary text and indexed claim searches performed; this absence is not a proof of publication priority.

## Limitations
This is one exact finite graph calculation with a full exhaustive reproducible acyclic-Morse certificate; it is not an infinite-family theorem, a description of \(C_3\square P_n\) for arbitrary \(n\), or a result about *perfect* matching complexes. The representation splitting is rational and does not specify an integral direct-sum decomposition. Novelty could be affected by an unindexed calculation. The mathematical verification and comparison are not an independent audit.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366 (first public 2026-09-23), https://arxiv.org/abs/2609.27366.
2. M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, *Discrete Mathematics* **346** (2023), article 113428, https://doi.org/10.1016/j.disc.2023.113428.
3. B. Braun, W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, *Electronic Journal of Combinatorics* **24** (2017), P4.18, https://doi.org/10.37236/6212.
4. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* **134** (1998), 90–145.
