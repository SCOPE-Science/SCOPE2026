# Four symmetry orbits exhaust the mod-two one-systoles of the 16-vertex real projective four-space
## Finding
Let \(K\) be Lutz's 16-vertex triangulation \(RP^4_{16}\) of \(\mathbb{RP}^4\), in Balagopalan's \(K_6\) labeling. Exactly 230 vertex triples are missing triangles. The boundary of every missing triangle represents the unique nonzero class in \(H_1(K;\mathbf F_2)\). Consequently the simple mod-two combinatorial homology 1-systole has edge length 3 and has exactly 230 unoriented minimizers. Under the full \(S_6\) automorphism group these minimizers form exactly four orbits: 20 all-letter triangles represented by \(\{A,B,D\}\), 60 two-letter/one-bisection triangles represented by \(\{C,E,3\}\), 90 one-letter/two-bisection triangles represented by \(\{D,3,8\}\), and 60 all-bisection triangles represented by \(\{1,4,5\}\).

## Assumptions and scope
Use the 16-vertex combinatorial 4-manifold \\(K=RP^4_{{16}}\\) in the \\(K_6\\) description of Balagopalan. The six letter vertices are \\(A,B,C,D,E,F\\); the ten numeric vertices \\(0,\\ldots,9\\) are the ten bisections of \\(K_6\\). The fifteen edges of \\(K_6\\) carry the four-element labels

`AB:0123 AC:0456 BC:0789 AD:1489 BD:1567 CD:2347 AE:2579 BE:2468 CE:1358 DE:0369 AF:3678 BF:3459 CF:1269 DF:0258 EF:0147`.

The thirty facets in the small orbit consist of a letter vertex together with the four numeric labels on an incident edge. The 120 facets in the large orbit are generated, for distinct letters \\(v,v',v''\\), by the two letters \\(v,v'\\) together with the three numeric labels in \\(e(v,v'')\\setminus e(v,v')\\). This reconstructs the published complex exactly and yields face vector \\(f=(16,120,330,375,150)\\).

A *missing triangle* is a three-vertex set whose three edges lie in \\(K\\) but whose 2-simplex does not. Because the one-skeleton is complete, this is simply a vertex triple that is not a triangular face. The simple mod-two combinatorial homology 1-systole is the minimum number of edges in a simple edge cycle carrying a nonzero class of \\(H_1(K;\\mathbf F_2)\\).

## Proof
The complete graph on 16 vertices has 120 edges. Over \\(\\mathbf F_2\\), the boundary map from the 330 triangular faces has rank 104. The boundary map from edges to vertices has rank 15, so its kernel has dimension \\(120-15=105\\). Hence
\[
\\dim_{{\\mathbf F_2}}H_1(K;\\mathbf F_2)=105-104=1.
\]

There are \\(\\binom{{16}}{{3}}=560\\) vertex triples and 330 triangular faces, hence exactly 230 missing triangles. A direct reduction of all 230 triangle-boundary vectors modulo the 104-dimensional 2-boundary space gives the same nonzero residue each time. There is also a compact cocycle certificate. Fix \\(A\\), put \\(w(Ax)=0\\) for every other vertex \\(x\\), and for an edge \\(xy\\) not incident with \\(A\\) put \\(w(xy)=1\\) exactly when \\(\\{{A,x,y\\}}\\) is a missing triangle. The resulting cochain has support on 45 edges. Exhaustive substitution shows that its sum around every one of the 330 face triangles is zero and its sum around every one of the 230 missing triangles is one. Thus \\(w\\) is a 1-cocycle detecting every missing triangle boundary.

A simple simplicial cycle has at least three edges. Every three-edge simple cycle is the boundary of a vertex triple. It is null-homologous when that triple is a face, and the preceding cocycle calculation shows that it is nonzero when the triple is missing. Therefore the systolic edge length is exactly 3 and the 230 missing triangles are exactly all minimizers.

For the symmetry classification, each numeric vertex is recovered from the printed edge labels as an unordered partition of the six letters into two 3-sets. Every one of the 720 permutations of the letters therefore acts canonically on all 16 vertices. Exhaustive verification shows that every such permutation preserves all 150 facets. Its action on the 230 missing triangles has four orbits, distinguished by the number of letter vertices. Their sizes and representatives are respectively \\(20:\\{A,B,D\\}\\), \\(60:\\{C,E,3\\}\\), \\(90:\\{D,3,8\\}\\), and \\(60:\\{1,4,5\\}\\). Lutz identifies this \\(S_6\\) action as the full automorphism group, so these are the full symmetry orbits.

## Verification
The accompanying `verify.py` reconstructs the facets from the published \\(K_6\\) mnemonic rather than from a precomputed face table. It then checks the face vector, computes the two relevant mod-two ranks, evaluates the explicit cocycle on all 560 triples, reconstructs the ten bisections, verifies all 720 induced permutations on all facets, and exhausts the missing-triangle orbits. Its expected terminal line is:

`VERIFY_OK f=16,120,330,375,150 H1_F2=1 missing3=230 essential3=230 cocycle_weight=45 systole=3 orbit_sizes=20,60,90,60 reps=ABD,CE3,D38,145`

These are finite exhaustive checks of the complete 16-vertex complex, not sampled experiments.

## Relationship to prior work
Lutz's 1999 dissertation gives the 16-vertex triangulation of \\(\\mathbb{{RP}}^4\\), its face vector, its 2-neighborliness, the \\(S_6\\) automorphism group, and the two facet orbits. Lutz's arXiv survey `math/0506372v1` records the 16-vertex triangulation and its vertex minimality. Balagopalan's `arXiv:1409.6149v2` gives the explicit \\(K_6\\) mnemonic used here and again records the \\(S_6\\) symmetry and the 30-plus-120 facet decomposition.

The inspected exact-object sources do not state the number 230 of missing triangles as homology representatives, do not assert that every missing triangle detects the nonzero mod-two first-homology class, and do not give the four systolic \\(S_6\\)-orbits. Searches phrased in terms of missing triangles, induced cycles, mod-two homology, systoles, and symmetry-orbit counts found no statement implying this classification.

## Limitations
The result concerns simple edge cycles and mod-two first homology of this one labeled triangulation; it does not classify longer representatives or integral one-cycles. The orbit computation uses the full automorphism group \\(S_6\\) recorded for this complex. An unindexed older computation could still contain the same finite census. The 1999 dissertation is an earlier source for the object but the inspected bibliographic evidence supplied only a year, not a day; the metadata therefore uses 2005-06-18, the earliest exact day-specific public date verified here, rather than inventing a day for the dissertation.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices and Vertex-Transitive Group Actions*, dissertation, TU Berlin, 1999. Relevant section: the 16-vertex triangulation \\(RP^4_{{16}}\\), its face vector, 2-neighborliness, \\(S_6\\) automorphisms, and facet orbits.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1, submitted 2005-06-18.
3. S. Balagopalan, *On a vertex-minimal triangulation of \\(RP^4\\)*, arXiv:1409.6149v2. Relevant material: the \\(K_6\\) mnemonic, 16-vertex quotient, and 30-plus-120 facet decomposition.
