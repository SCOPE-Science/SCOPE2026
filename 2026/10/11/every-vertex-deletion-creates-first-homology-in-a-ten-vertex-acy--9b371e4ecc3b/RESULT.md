# Every vertex deletion creates first homology in a ten-vertex acyclic complex
## Finding
Let \(X\) be the ten-vertex two-dimensional simplicial complex with the 31 triangular facets printed by Lutz. The source gives \(f(X)=(10,40,31)\) and identifies \(X\) as \(\mathbb Z\)-acyclic and noncontractible. For every vertex \(v\), the induced deletion \(X-v\) is connected, satisfies \(H_2(X-v;\mathbb Q)=0\), and has nonzero first rational homology. In the source labeling,
\[
\beta_1(X-v;\mathbb Q)=
\begin{{cases}}
3,&v\in\{{1,2,3,4,5\}},\\
2,&v\in\{{6,7,8\}},\\
1,&v\in\{{9,10\}}.
\end{{cases}}
\]
Hence every vertex is essential for rational acyclicity, and the deletion defect multiset is \(\{{3,3,3,3,3,2,2,2,1,1\}}\).

## Assumptions and scope
The complex is defined exactly by the 31 source facets on vertices \(1,\ldots,10\). The new assertion concerns reduced rational homology after deleting one vertex at a time. It does not assert that the deletion complexes have torsion-free integral homology, nor does it classify their fundamental or simple-homotopy types. The noncontractibility of the undeleted complex is a cited premise from the source, while its rational acyclicity is independently replayed from the printed facets.

## Proof
The verifier reconstructs every edge and triangle from the 31 facets. For a vertex set \(S\), it builds the oriented simplicial boundary matrices \(\partial_1:C_1(X[S];\mathbb Q)\to C_0(X[S];\mathbb Q)\) and \(\partial_2:C_2(X[S];\mathbb Q)\to C_1(X[S];\mathbb Q)\), and computes their ranks by exact Gaussian elimination over \(\mathbb Q\).

For the full complex this gives face vector \( (10,40,31) \) and rational Betti vector \( (1,0,0) \). For each of the ten sets \(S=V(X)\setminus\{v\}\), the computation gives \(\beta_0=1\), \(\beta_2=0\), and the stated positive value of \(\beta_1\). This is exhaustive because every vertex deletion is explicitly evaluated.

There is also a direct numerical check. If \(e_v\) is the number of edges incident with \(v\) and \(t_v\) the number of triangles incident with \(v\), then the deletion has Euler characteristic \(\chi(X-v)=1-e(X-v)+t(X-v)\). Since the exact chain calculation gives connectedness and vanishing \(H_2(-;\mathbb Q)\), one has \(\beta_1(X-v;\mathbb Q)=t_v-e_v+1\). The ten incidence pairs reproduce the same profile.

## Verification
Run `python verify.py` with a standard Python interpreter. The expected first line is:

`VERIFY_OK f=10,40,31 full_betti_Q=1,0,0 deletion_b1_multiset=3x5,2x3,1x2`

The remaining lines print, for each source-labeled vertex, its edge and triangle incidence degrees, the deletion first Betti number, and the deletion edge and triangle counts. All linear algebra uses exact rational arithmetic.

## Relationship to prior work
Björner and Lutz's preprint and Lutz's dissertation introduce the acyclic noncontractible complex in the course of constructing a small triangulation related to the Poincaré homology sphere; the dissertation prints the exact 31-facet presentation and the face vector used here. The inspected source passage establishes global acyclicity and noncontractibility but does not state the ten single-vertex deletion homology groups or their \(5+3+2\) rank stratification. A later exact-object journal version is bibliographically known, but its full text was not relied on for a whole-document noncoverage claim. The closest published-finding comparison found in focused searches studies an unrelated twelve-vertex collapsible ball and a mod-two acyclic deletion landscape, so it does not imply this rational deletion theorem.

## Limitations
The deletion theorem is over \(\mathbb Q\). It neither rules out torsion in integral deletion homology nor identifies the homotopy type of any deletion. The result is a property of this particular labeled ten-vertex complex; it is not a lower bound for all acyclic noncontractible complexes. A residual originality risk remains from unindexed historical computations and from portions of the corresponding journal article not inspected at statement level.

## References
1. A. Björner and F. H. Lutz, *Simplicial manifolds, bistellar flips and a 16-vertex triangulation of the Poincaré homology 3-sphere*, preprint dated 14 February 1999; later Experimental Mathematics 9 (2000), 275–289, DOI 10.1080/10586458.2000.10504652.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices and Vertex-Transitive Group Actions*, Shaker Verlag, 1999, ISBN 3-8265-6450-2; exact ten-vertex facet presentation and acyclicity discussion in the inspected passage.
3. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1, 18 June 2005; MSC context including 57Q15.
