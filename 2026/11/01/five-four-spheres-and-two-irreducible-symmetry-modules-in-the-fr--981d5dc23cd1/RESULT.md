# Five four-spheres and two irreducible symmetry modules in the Franklin dissociation complex

## Finding

Let \(F\) be the Franklin graph on vertices \(V=\{0,1,\ldots,11\}\), with undirected cycle edges \(\{i,i+1\}\) (indices modulo \(12\)) and chords \(\{i,i+5\}\) for even \(i\), or \(\{i,i-5\}\) for odd \(i\). The resulting edge set contains exactly \(18\) edges. Define \(X=\operatorname{Ind}_2(F)\) as the simplicial complex whose faces are vertex subsets inducing connected components of size at most \(2\), equivalently induced maximum degree at most one (the dissociation complex).

**Integral homotopy theorem:**
\[
X\simeq\bigvee^{5}S^{4},\qquad
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}\mathbb Z^5,&j=4,\\0,&j\ne4.\end{cases}
\]

**Full symmetry theorem:** The graph automorphism group \(G=\operatorname{Aut}(F)\) has \(48\) elements. The central involution \(z(i)=i+6\pmod{12}\) acts on \(H_4(X;\mathbb Q)\) with \(+1\) and \(-1\) eigenspaces of dimensions \(3\) and \(2\), respectively. Each eigenspace is absolutely irreducible for \(G\). The full rational character \(\chi(g)=\operatorname{tr}(g_*\mid H_4(X;\mathbb Q))\) is determined by the complete table below, where vertex cycle type refers to the permutation of the twelve graph vertices:

| Vertex cycle type | Additional condition | Number of elements | \(\chi\) |
| --- | --- | ---: | ---: |
| \(1^{12}\) | identity | 1 | 5 |
| \(1^8 2^2\) | — | 3 | -3 |
| \(1^4 2^4\) | — | 3 | 1 |
| \(2^6\) | not \(z\) | 12 | -1 |
| \(2^6\) | \(z\) | 1 | 1 |
| \(2^2 4^2\) | — | 12 | 1 |
| \(3^4\) | — | 8 | -1 |
| \(6^2\) | — | 8 | 1 |

In particular, \(H_4(X;\mathbb Q)^G=0\). For the topological orbit space, \(\widetilde H_j(X/G;\mathbb Q)=0\) for every integer \(j\).

## Assumptions and scope

All edges are unordered, all vertex indices are reduced modulo \(12\), and simplicial homology uses its usual oriented integral chain complex. The face poset excludes the empty face; this is the ordinary (unaugmented) discrete-Morse convention. A vertex subset is a face if and only if no chosen vertex has two chosen neighbors, equivalently none of the \(36\) connected three-vertex wedges of the graph is fully selected. Statements concern precisely this graph and parameter \(2\); the quotient conclusion is over \(\mathbb Q\), not over \(\mathbb Z\).

## Proof

**1. Exact face set.** For each integer mask from \(1\) through \(4095\), the predicate \(\deg_{F[S]}(v)\le1\) for every chosen vertex \(v\) is equivalent to forbidding all connected three-vertex paths (wedges). The two predicates agree for all \(4096\) masks. Counting by cardinality yields the nonempty face vector \((12,66,184,264,168,28)\), hence \(722\) nonempty faces.

**2. Integral homotopy.** Take the vertex order
\[
(7,11,0,8,5,6,3,10,4,1,9,2).
\]
At each listed vertex \(v\), within the still-unmatched faces, match every remaining face not containing \(v\) to its union with \(\{v\}\) whenever both are remaining. This specifies exactly \(358\) distinct covering pairs. To check acyclicity without an unproved matching lemma, orient each matched Hasse cover from lower to upper face and each unmatched cover from upper to lower face. The directed Hasse graph has \(722\) vertices and \(2748\) edges; exhaustive topological sorting visits all \(722\) vertices, so it is acyclic. Exactly six critical faces remain: one vertex and five four-dimensional simplices. Discrete Morse theory gives a CW model with one \(0\)-cell and five \(4\)-cells and no other cells. Every \(4\)-cell therefore attaches to the sole point by a constant map, proving \(X\simeq\bigvee^{5} S^4\) integrally.

**3. Automorphisms and signed traces.** Exhaustive adjacency-preserving bijection search on the twelve vertices returns exactly \(48\) graph automorphisms. Its recursive search considers every injective partial map respecting both adjacency and nonadjacency, hence no automorphisms are omitted. For each \(g\in G\), the signed simplicial Lefschetz number is
\[
L(g)=\sum_{\substack{\varnothing\ne \sigma\in X\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g\vert_{\sigma}).
\]
The only nonzero rational homology groups are \(H_0=\mathbb Q\) and \(H_4=\mathbb Q^5\), so the Hopf trace formula gives \(\chi(g)=L(g)-1\). For every automorphism and every invariant face, two independent sign calculations agree: inversion parity of its image ordering and parity of the induced permutation's cycle decomposition. The complete character table is the one displayed above.

**4. Irreducibility and quotient.** The shift \(z(i)=i+6\) is central in the enumerated group, and \(\chi(z)=1\). Thus the central eigenspace dimensions are \((5+1)/2=3\) and \((5-1)/2=2\). Their characters are \(\chi_{\pm}(g)=(\chi(g)\pm\chi(gz))/2\). Exact enumeration gives
\[
\frac{1}{48}\sum_{g\in G}\chi_{+}(g)^2
=\frac{1}{48}\sum_{g\in G}\chi_{-}(g)^2=1,
\qquad
\frac{1}{48}\sum_{g\in G}\chi_{+}(g)\chi_{-}(g)=0.
\]
The character inner-product criterion over \(\mathbb C\) proves each nonzero rational eigenspace absolutely irreducible. Independently \(\frac1{48}\sum_g\chi(g)=0\), so there are no invariant fourth-homology classes. Finite-group rational transfer (or invariant chains after barycentric subdivision) identifies the rational homology of the orbit space with invariant rational homology. The quotient is connected, completing the orbit-space assertion.

## Verification

Run `python3 verify.py` with Python \(3\) and no third-party modules. The code independently compares two face predicates over all \(4096\) subsets; enumerates every matching pair, Hasse cover, and graph automorphism; checks Hasse acyclicity by topological sorting; compares two fixed-face orientation signs; calculates all \(48\) character values and irreducibility inner products; and computes independent mod-two simplicial boundary ranks. The exact expected output is included as `verify_output.txt`. In particular the mod-two Betti ranks are \((1,0,0,0,5,0)\) in degrees \(0\) through \(5\), serving only as corroboration: the integral homotopy conclusion comes from the full acyclic matching.

## Relationship to prior work

The hypergraph independence-complex framework of Conant and Thistlethwaite (first public source 2008-08-05) supplies an archive-era conceptual route: \(X\) is the independence complex of the three-uniform hypergraph of connected vertex triples of \(F\). Their theta-complex calculations do not give this homotopy or character. Deshpande and Singh's full higher-independence classifications concern complete multipartite, whiskered, cycle and tree families rather than the Franklin graph. The later chordal-graph results are inapplicable because the Franklin graph contains induced four-cycles. Indexed results on Franklin-graph matching complexes operate on **edges**, whereas this dissociation complex operates on **vertices**. Results about dissociation numbers measure maximal set cardinalities, not the topology or representation of the entire face complex. No inspected prior theorem implies the joint homotopy-and-character claim.

## Limitations

This is a finite-graph calculation, not a classification of all cubic graphs or higher parameters. The result does not determine the integral homology, simple homotopy type or homotopy type of the quotient \(X/G\). The absence of an indexed matching statement is not proof of worldwide publication priority. No independent mathematical audit has been performed. The 2008 anchor date belongs to the cited general hypergraph framework, not to any purported prior publication of the present Franklin-specific computation.

## References

1. James Conant and Oliver Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739, first public 2008-08-05. https://arxiv.org/abs/0808.0739
2. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first public 2020-01-15. https://arxiv.org/html/2001.05448v2
3. Fred M. Abdelmalek and collaborators, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863. https://arxiv.org/abs/2106.10863
4. Eric W. Weisstein, *Franklin Graph*, MathWorld. https://mathworld.wolfram.com/FranklinGraph.html
5. *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics (2011). https://doi.org/10.1016/j.dam.2011.04.023
