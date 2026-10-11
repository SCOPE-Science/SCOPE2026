# A sharp five-vertex homology-support threshold for the seven-vertex torus
## Finding
Let \(K=T_{7,1,2}\) be the Datta--Upadhyay seven-vertex torus on \(\mathbb Z/7\mathbb Z\), with faces \(\{i,i+2,i+3\}\) and \(\{i,i+1,i+3\}\). For every vertex set \(S\subseteq V(K)\), let \(r(S)\) be the \(\mathbf F_2\)-rank of the image of \(H_1(K[S];\mathbf F_2)\to H_1(K;\mathbf F_2)\). Then the complete rank distribution by \(|S|\) is: ranks \(0\) on the unique empty set; rank \(0\) on all \(7\) one-sets and all \(21\) two-sets; on three-sets, rank \(0\) for the \(14\) faces and rank \(1\) for the \(21\) empty triangles; on four-sets, rank \(1\) for \(21\) sets and rank \(2\) for \(14\) sets, with \(r(S)=2\) exactly when the complementary three-set is a face; and every five-, six-, or seven-vertex set has rank \(2\). Moreover, the \(21\) empty triangles represent the three nonzero classes of \(H_1(K;\mathbf F_2)\cong\mathbf F_2^2\) exactly seven times each. Consequently, five is the least integer \(k\) such that every \(k\)-vertex induced subcomplex surjects onto \(H_1(K;\mathbf F_2)\).

## Assumptions and scope
The complex is the published cyclic triangulation \(T_{7,1,2}\). Vertices are represented by \(0,1,\ldots,6\) modulo \(7\), and its fourteen triangular faces are obtained from
\[
\{i,i+2,i+3\},\qquad \{i,i+1,i+3\},\qquad i\in\mathbb Z/7\mathbb Z.
\]
All homology and image ranks in the finding use coefficients in \(\mathbf F_2\). For \(S\subseteq V(K)\), \(K[S]\) denotes the induced subcomplex.

## Proof
The published face formula gives a complete one-skeleton: every pair of vertices is an edge. Hence the \(1\)-cycle space of the complete graph on any nonempty vertex set \(S\) is generated over \(\mathbf F_2\) by boundaries of triangles on \(S\). Indeed, after choosing one vertex \(v\in S\), each cycle is a sum of the triangles \(\partial\{v,a,b\}\). Therefore the image of \(H_1(K[S];\mathbf F_2)\) in global first homology is exactly the span, modulo global triangular boundaries, of the boundaries of all three-subsets of \(S\).

For \(K\), the complete graph has \(21\) edges and connected cycle-space dimension \(21-7+1=15\). Exact binary elimination on the fourteen face boundaries gives boundary rank \(13\), so
\[
\dim_{\mathbf F_2}H_1(K;\mathbf F_2)=15-13=2.
\]
Among the \(35\) three-subsets, the fourteen published faces reduce to zero and the other twenty-one triangle boundaries reduce to exactly three nonzero quotient classes, with multiplicities \(7,7,7\). These are therefore all three nonzero elements of \(\mathbf F_2^2\).

It remains only a finite complete classification of vertex sets. Exact reduction of every one of the \(2^7=128\) induced vertex sets gives

| \(|S|\) | image-rank distribution |
|---:|---|
| \(0\) | \(1\) set of rank \(0\) |
| \(1\) | \(7\) sets of rank \(0\) |
| \(2\) | \(21\) sets of rank \(0\) |
| \(3\) | \(14\) sets of rank \(0\), \(21\) of rank \(1\) |
| \(4\) | \(21\) sets of rank \(1\), \(14\) of rank \(2\) |
| \(5\) | \(21\) sets of rank \(2\) |
| \(6\) | \(7\) sets of rank \(2\) |
| \(7\) | \(1\) set of rank \(2\) |

For every four-set, the same exhaustive reduction verifies the sharper equivalence: its image has rank \(2\) if and only if its complementary three-set is one of the fourteen faces. This proves the stated distribution and the sharp five-vertex threshold.

## Verification
The standalone `verify.py` rebuilds \(T_{7,1,2}\) from the published modular face formula rather than from a copied facet table. It performs exact bit-vector Gaussian elimination over \(\mathbf F_2\), verifies the global first-homology dimension, classifies all twenty-one empty triangles in the quotient, and exhausts all \(128\) vertex subsets. The replay output is:

`VERIFY_OK H1dim=2 empty_triangles=21 classes=7,7,7 layers=0:0x1;1:0x7;2:0x21;3:0x14,1x21;4:1x21,2x14;5:2x21;6:2x7;7:2x1 complement4=face_iff_rank2 threshold=5`

## Relationship to prior work
Datta and Upadhyay define the family \(T_{n,1,k}\), prove that it triangulates the torus, and identify \(T_{7,1,2}\) among the small weakly regular examples. Lutz records Möbius' seven-vertex torus as the unique seven-vertex torus and emphasizes its neighborly complete one-skeleton. General tightness theory says that a neighborly closed surface is tight over characteristic two, so every induced-subcomplex homology map is injective. That general theorem does not determine the image ranks, the three nonzero global classes carried by empty triangles, their exact \(7,7,7\) multiplicities, or the four-set complement criterion proved here.

Focused searches for the exact object together with "empty triangles", "missing triangles", "induced subcomplex", "homology support", and "first homology image rank" found no statement implying this complete rank spectrum. A recent published computation on the same triangulation concerns contiguity classes of simplicial self-maps; it does not classify homology carried by induced vertex subsets.

## Limitations
The finding is only about \(\mathbf F_2\)-homology and does not classify integral homology classes of the empty triangles. It concerns the unique seven-vertex torus up to combinatorial isomorphism and makes no corresponding assertion for larger torus triangulations. Search absence is not a proof of novelty; an unindexed older computation of the same local rank spectrum remains a residual risk.

## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433v1, first public 2004-03-25. The paper gives the defining formula for \(T_{n,1,k}\) and lists primary MSC 57Q15.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1, first public 2005-06-18. Section on two-manifolds records Möbius' seven-vertex neighborly torus and the uniqueness of the seven-vertex torus type.
3. B. Bagchi, B. Datta, and J. Spreer, *Tight triangulations of closed 3-manifolds*, arXiv:1412.0412v1, first public 2014-12-01. Its introduction recalls that closed neighborly surfaces are tight in characteristic two and defines tightness through injectivity on homology of all induced subcomplexes.
