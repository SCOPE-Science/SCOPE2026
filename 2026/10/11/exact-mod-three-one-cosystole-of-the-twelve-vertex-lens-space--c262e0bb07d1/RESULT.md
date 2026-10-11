# Exact mod-three one-cosystole of the twelve-vertex lens space
## Finding
Let \(K=L(3,1)_{12}\) be the 12-vertex proper simplicial triangulation of the lens space \(L(3,1)\) listed by Lutz, with
\[
f(K)=(12,66,108,54).
\]
For a simplicial \(1\)-cocycle \(z\in Z^1(K;\mathbf F_3)\), define its edge weight \(\operatorname{wt}(z)\) to be the number of edges on which \(z\) is nonzero. Then
\[
\min\{\operatorname{wt}(z):[z]\ne 0\in H^1(K;\mathbf F_3)\}=28.
\]
Moreover, each of the two nonzero classes in \(H^1(K;\mathbf F_3)\cong\mathbf F_3\) has exactly \(18\) weight-\(28\) representatives. Negation pairs the two classes and preserves edge support, so there are exactly \(18\) minimum supports. Under the published simplicial automorphism group \(S_3\), these supports form four orbits of sizes \(3,3,6,6\).

## Assumptions and scope
All chains and cochains in the claim use coefficients in \(\mathbf F_3\). Edges and triangles are oriented by increasing vertex order. The object is the exact labeled 12-vertex complex whose 54 tetrahedra are listed in `source_facets.txt`; this list is transcribed from the public primary source. The invariant is a cochain Hamming weight on this fixed triangulation, not a metric systole of the underlying lens space and not an assertion about all triangulations of \(L(3,1)\).

## Proof
The facet list generates all \(66\) edges and \(108\) triangles. Let \(\partial_1:C_1\to C_0\) and \(\partial_2:C_2\to C_1\) be the simplicial boundary maps. Exact row reduction modulo \(3\) gives
\[
\operatorname{rank}(\partial_1)=11,\qquad \operatorname{rank}(\partial_2)=54.
\]
Hence
\[
\dim_{\mathbf F_3}H^1(K;\mathbf F_3)=(66-54)-11=1.
\]

An explicit nonzero cocycle \(z_0\) of weight \(28\) is supplied by `verifier.py`; its nonzero values, with coefficient \(2\) interpreted as \(-1\), are checked triangle-by-triangle against the cocycle equations. Appending \(z_0\) to the row space of \(\partial_1\) raises its rank from \(11\) to \(12\), so \([z_0]\ne0\).

Every representative of \([z_0]\) is uniquely of the form \(z_0+\delta p\) after normalizing the vertex potential by \(p(1)=0\). There are exactly
\[
3^{11}=177{,}147
\]
such normalized potentials. Exhausting them gives minimum weight \(28\), attained exactly \(18\) times. Since the only other nonzero cohomology class is \(-[z_0]\), negation gives a support-preserving bijection between the minimum representatives of the two classes. Thus the projective nonzero cohomology class has exactly \(18\) minimum edge supports.

Finally, the two published generators
\[
(1\,2)(3\,6)(4\,5)(7\,8)(10\,11),\qquad
(1\,3\,5)(2\,4\,6)(7\,8\,9)(10\,11\,12)
\]
generate a six-element group preserving the full facet list. Direct action on the \(18\) minimum supports yields four orbits of sizes \(3,3,6,6\).

## Verification
`verifier.py` uses only the Python standard library. It decodes the 54 tetrahedra, rebuilds the full face set, performs exact Gaussian elimination over \(\mathbf F_3\), verifies the displayed cocycle, exhausts all \(3^{11}\) normalized coboundary shifts, checks the complete weight enumerator, reconstructs the six published automorphisms, and verifies the four support-orbit sizes. Its recorded output begins with `VERIFY_OK` and reports `cosystole_edge_weight=28`, `minimum_supports=18`, and `minimum_support_S3_orbits=3,3,6,6`.

## Relationship to prior work
Lutz's public paper gives the exact 12-vertex triangulation, its face vector, its lens-space identification, and its \(S_3\) symmetry, but it does not discuss cocycles, cohomology, or cosystolic weight. Datta's later review reproduces the same tetrahedron list and records \(H_1(L(3,1);\mathbb Z)\cong\mathbb Z/3\), which implies the existence of mod-three degree-one cohomology but does not determine the minimum cochain support or its multiplicity. A prior exact-object result with opaque identifier `d2bff23c-bad3-4cad-84e8-caa6f4dc8833` concerns shortest nonzero homology cycles in the same triangulation; cycle length does not imply minimum cocycle Hamming weight because the two optimizations live in different chain/cochain quotient spaces.

## Limitations
The result is specific to this labeled 12-vertex triangulation and coefficient field \(\mathbf F_3\). It does not claim optimality among all triangulations of \(L(3,1)\), nor a general lens-space formula. Originality searches cannot exclude an unindexed historical computation of the same finite cohomology coset. The symmetry-orbit statement concerns edge supports; it does not classify minimum cocycles up to all possible cochain equivalences beyond coboundaries and scalar negation.

## References
1. Frank H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1, 18 June 2005. The exact \(L(3,1)_{12}\) facet list and \(S_3\) generators appear in the section on small 3-manifolds.
2. Basudeb Datta, *Minimal Triangulations of Manifolds*, Journal of the Indian Institute of Science 87:4 (2007), Example 3.7, reproducing the 12-vertex \(L(3,1)\) complex and its basic homology.
