# Five vertices are the first local fingerprint separating Lutz’s boundary-isomorphic balls
## Finding
Let \(B_a\) and \(B_b\) be the two twelve-vertex, thirty-seven-facet simplicial \(3\)-balls obtained from Lutz’s ball \(B_{12,38}^3\) by deleting the free facets \(2457\) and \(34610\), respectively. For \(1\le k\le12\), let \(\Phi_k(B)\) be the multiset, over all \(k\)-element vertex sets \(S\), of the pair consisting of the induced-subcomplex \(f\)-vector \(f(B[S])\) and the ordinary mod-two Betti vector \(\beta_{\mathbb F_2}(B[S])\). Then \(\Phi_k(B_a)=\Phi_k(B_b)\) for \(k=1,2,3,4\), while \(\Phi_5(B_a)\ne\Phi_5(B_b)\). Thus five is the least vertex-cardinality at which this label-invariant local induced-subcomplex fingerprint distinguishes the two balls. At \(k=5\) exactly six profile multiplicities differ, each by one: \(B_a\) has one extra occurrence of \(((5,10,4),(1,2,0))\), \(((5,9,4),(1,1,0))\), and \(((5,8,1),(1,3,0))\), while \(B_b\) has one extra occurrence of \(((5,8,2),(1,2,0))\), \(((5,9,2),(1,3,0))\), and \(((5,10,5),(1,1,0))\).

## Assumptions and scope
The two complexes are the labeled balls in Frank H. Lutz, *Small Examples of Non-Constructible Simplicial Balls and Spheres*, obtained from the published thirty-eight-facet ball by deleting the free tetrahedra \\(2457\\) and \\(34610\\). For a vertex set \\(S\\), \\(B[S]\\) denotes the induced subcomplex. Its \\(f\\)-vector records the number of nonempty faces in each dimension, and \\(\\beta_{\\mathbb F_2}\\) is the ordinary Betti vector over \\(\\mathbb F_2\\). The fingerprint \\(\\Phi_k\\) forgets vertex labels and retains only the multiset of these local pairs.

The claim concerns only these two finite complexes and this explicitly defined fingerprint. It does not assert that five vertices are minimal for every possible isomorphism invariant, nor that the six profile shifts determine either ball uniquely among all simplicial balls.

## Proof
The published facet list of \\(B_{12,38}^3\\) gives thirty-eight tetrahedra. Removing \\(2457\\) gives \\(B_a\\); removing \\(34610\\) gives \\(B_b\\). Direct face enumeration gives the same full \\(f\\)-vector \\((12,58,84,37)\\) for both balls.

For each \\(k\\in\\{{1,2,3,4,5\\}}\\), enumerate all \\(\\binom{{12}}{{k}}\\) vertex sets. For each set, intersect every tetrahedron with it, close under taking nonempty faces, count faces by dimension, and compute mod-two homology by exact Gaussian elimination on the simplicial boundary matrices. The resulting multisets have respectively \\(1,2,5,14\\) distinct profiles for \\(k=1,2,3,4\\), and the two multisets agree in every one of those four cases. At \\(k=5\\), each side has \\(38\\) distinct profiles across all \\(792\\) vertex sets, and their multiplicity difference is supported on exactly the six pairs stated in the finding. Consequently the first disagreement is at \\(k=5\\).

As an independent consistency check on the identification of the pair, the boundary of each ball has twenty triangles, and the permutation \\((2\,3)(5\,6)(7\,10)(8\,12)(9\,11)\\) sends the boundary of \\(B_a\\) exactly to the boundary of \\(B_b\\). Since \\(\\Phi_5\\) is invariant under simplicial isomorphism and differs, the calculation also independently certifies that the two balls themselves are not simplicially isomorphic.

## Verification
The bundled `verify.py` uses only the Python standard library. It reconstructs every induced subcomplex used above, computes boundary-matrix ranks over \\(\\mathbb F_2\\), checks the full face and homology data of the two balls, verifies the explicit boundary isomorphism, proves equality of \\(\\Phi_k\\) for \\(k\\le4\\), and checks the complete six-entry difference at \\(k=5\\).

A successful replay prints a single line beginning `VERIFY_OK` and includes `profiles_equal_k=1..4` and `first_difference_k=5`.

## Relationship to prior work
Lutz introduced the pair as strongly nonshellable, nonconstructible, nonrealizable simplicial \\(3\\)-balls with isomorphic boundaries but nonisomorphic interiors. The preprint gives their common parent \\(B_{12,38}^3\\), the two free facets, and the complete facet table. It does not state the induced-subcomplex profile threshold or the six five-vertex profile shifts proved here.

Benedetti and Lutz later studied the parent ball \\(B_{12,38}\\) in connection with collapsibility and evasiveness. That work provides a closely related exact-object check, but its vertex-deletion analysis concerns the parent ball and does not imply equality of the two thirty-seven-facet balls through four-vertex induced fingerprints or their first five-vertex separation.

Focused searches for the exact pair, induced-subcomplex fingerprints, five-vertex local profiles, and equivalent \\(f\\)-vector/Betti formulations found no statement implying the result. Search absence is not a proof of novelty; the remaining risk is an unindexed computation of these two complexes.

## Limitations
This is a finite exact classification for one canonical pair. The invariant is deliberately local and label-free, but it is not claimed to be complete for simplicial isomorphism in general. Homology is computed only over \\(\\mathbb F_2\\). The scientific conclusion is the exact minimal \\(k\\) for this specified fingerprint and the listed six multiplicity shifts.

## References
1. F. H. Lutz, *Small Examples of Non-Constructible Simplicial Balls and Spheres*, ZIB Report 03-28 (2003); arXiv:math/0309149; later SIAM J. Discrete Math. 18 (2004), 103–109, DOI: 10.1137/S0895480103430521.
2. B. Benedetti and F. H. Lutz, *Knots in Collapsible and Non-Collapsible Balls*, arXiv:1303.2070; Electron. J. Combin. 20(3) (2013), #P31, DOI: 10.37236/3319.
