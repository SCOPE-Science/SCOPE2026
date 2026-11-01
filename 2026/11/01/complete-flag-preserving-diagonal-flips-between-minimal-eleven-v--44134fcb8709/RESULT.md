# Complete flag-preserving diagonal flips between minimal eleven-vertex projective-plane triangulations

## Finding
Let \(G_1,G_2\) be the eleven-vertex graphs encoded in standard graph6 notation by `JCpdUg{[ap_` and ``JCp`eikYa|?``, respectively, and put \(K_i=\operatorname{Ind}(G_i)\). In both cases the vertices are indexed \(0,\ldots,10\). Their independence complexes are flag triangulations of the real projective plane, each with face vector \((11,30,20)\).

**Theorem (complete flag-flip incidence).** The flag-preserving diagonal flips of \(K_1\), specified by their removed edges and the opposite new diagonals, are exactly
\[
\begin{array}{c|c}
\text{removed}&\text{inserted}\\\hline
(0,8)&(1,9)\\
(1,6)&(3,8)\\
(2,3)&(1,4)\\
(4,5)&(3,9)\\
(7,9)&(4,8)
\end{array}
\]
Those of \(K_2\) are exactly
\[
\begin{array}{c|c}
\text{removed}&\text{inserted}\\\hline
(0,2)&(1,10)\\
(0,9)&(5,10)\\
(2,7)&(4,10)\\
(7,9)&(8,10)
\end{array}
\]
Every allowed flip from \(K_1\) produces a complex isomorphic to \(K_2\), and every allowed flip from \(K_2\) produces a complex isomorphic to \(K_1\). The automorphism groups have orders \(10\) and \(8\), respectively, and each acts transitively on its own allowed flips. Hence the complete isomorphism-class graph of flag-preserving diagonal flips on eleven-vertex flag real-projective-plane triangulations consists of precisely two vertices joined by an edge, without loops; the two representatives have respectively five and four *labeled* allowed flips, all in one symmetry orbit. The already-known existence of one flip between these examples is not claimed as new.

## Assumptions and scope
Here a diagonal flip means the standard two-dimensional \(2\)-to-\(2\) bistellar move: for two triangles \(\{a,b,c\}\) and \(\{a,b,d\}\) incident to the edge \(\{a,b\}\), replace them by \(\{a,c,d\}\) and \(\{b,c,d\}\), removing edge \(\{a,b\}\) and adding \(\{c,d\}\), without changing the vertex set. A flip is **flag-preserving** if the resulting abstract simplicial complex is the clique complex of its one-skeleton. The counts of five and four distinguish possible removed edges on the stated labeled representatives; they are not five or four distinct isomorphism classes.

The two graph6 strings encode **complement** graphs of the one-skeleta, since faces of \(\operatorname{Ind}(G_i)\) are independent vertex subsets. The representation uses the standard graph6 order of pairs \((i,j)\), \(0\le i<j<11\), sorted first by \(j\), then by \(i\). The eleven-vertex minimum is established in earlier work [1]. The completeness among isomorphism types uses the eleven-vertex graph census [2] together with the connected-complement argument below.

## Proof
**A local flag-flip criterion.** Let \(K\) be a two-dimensional flag triangulation of a closed surface, with one-skeleton \(H\). Any edge \(\{a,b\}\) has exactly two incident triangles, with distinct opposite vertices \(c,d\). They cannot be adjacent in \(H\), since then \(a,b,c,d\) would span a forbidden four-vertex clique in the two-dimensional flag complex. Write \(N_H(u)\) for its open neighborhood. The diagonal flip is flag-preserving **if and only if**
\[
N_H(c)\cap N_H(d)=\{a,b\}.
\]
Indeed, deleting edge \(ab\) removes exactly triangles \(abc\) and \(abd\); adjoining edge \(cd\) creates triangles indexed by the common neighbors of \(c,d\). Exactly the two prescribed new triangles appear if and only if the intersection above has precisely those two vertices. In this case, no new four-clique arises: its required vertices would comprise \(c,d\) and two adjacent common neighbors, but the only two common neighbors \(a,b\) have just been made nonadjacent. All remaining cliques are unchanged. Conversely, any third common neighbor would produce an unintended triangular face, so the flip could not preserve the prescribed flag triangulation.

**Finite but exhaustive application.** Standard graph6 decoding gives each complex exactly \(11\) vertices and \(30\) edges, with \(20\) triangular cliques and no four-cliques. At every vertex, its link is a single cycle. For **every one of the 30 edges** of each one-skeleton, determine the two opposite vertices of its incident triangles, then compute the common-neighbor intersection. The local criterion passes on exactly the five \(K_1\) edges and four \(K_2\) edges displayed above. On each of the remaining \(25\), respectively \(26\), edges it fails because the two opposite vertices have a third common neighbor. The certificate `flag_flip_certificate.json` supplies both the complete adjacency data by graph6, the nine allowed-edge/opposite-pair records, and explicit eleven-point permutations witnessing an isomorphism of each flipped graph with the other representative.

The same certificate contains all \(10\) automorphisms of \(K_1\) and all \(8\) automorphisms of \(K_2\). Complete degree-and-adjacency backtracking independently counts every graph automorphism and matches the listed permutations; their images of any one allowed edge exhaust the five or four allowed edges. The two complexes are not isomorphic: their vertex degree multisets differ, as can be read directly from the graphs. This proves the exact counts, the one-orbit assertions, and the absence of self-flips.

**Why there are no further eleven-vertex types.** A closed flag triangulation of the real projective plane is Cohen–Macaulay over \(\mathbb Q\) (its rational first homology vanishes and vertex links are circles), but not shellable (a pure shellable two-complex is a wedge of two-spheres and cannot have the integral first-homology torsion of the projective plane). Its complement graph must be connected: if disconnected, the flag complex would split as a nontrivial join; a closed connected two-dimensional triangulated surface that splits nontrivially as such a join must be a two-sphere, by examining dimensions and vertex links. Thus it falls under the exhaustive census [2], which reports exactly two connected eleven-vertex graphs with Cohen–Macaulay, nonshellable independence complexes over \(\mathbb Q\), namely the two graph6 representatives. Consequently no additional isomorphism types can contribute vertices or edges to the minimal flag-flip graph.

## Verification
Run `python3 verify.py` with `flag_flip_certificate.json` in the same directory; no nonstandard Python packages are required. The checker decodes graph6, constructs all triangular cliques directly from the adjacency relation, validates the face vector, verifies each link is a cycle and no four-cliques exist, and checks **all 30 edges of each complex** with the common-neighbor criterion. It also directly verifies every post-flip triangle set, each of the nine explicit graph-isomorphism permutations, every listed automorphism, and the exact totals of all graph automorphisms through exhaustive degree-constrained permutation backtracking. It exits successfully only when the outcome is exactly five and four allowed flips, with one automorphism orbit for each and group orders ten and eight. Its successful execution returned `VERIFY_OK`. The finite enumeration is exhaustive because all edge candidates and all automorphism permutations are checked, rather than sampled.

## Relationship to prior work
Bibby, Odesky, Wang, Wang, Zhang, and Zheng [1, Example 3.1 and Table 1] explicitly construct the two triangulations and exhibit **one** bistellar flip between them; this existence and their vertex-minimality are prior results. Their example does not enumerate all legal *flag-preserving* flips or the asymmetric five-versus-four incidence and its complete automorphism orbit structure. Van Tuyl [2] gives the exhaustive eleven-vertex Cohen–Macaulay/nonshellable graph classification, providing a way to conclude completeness of the minimal flag-projective-plane flip graph; it does not give its incidence counts. The new assertion is precisely the **complete local move classification and its symmetry**, including the exclusion of every other candidate flip. The standard local bistellar-move definition is classical. No originality is claimed for the published triangulations, their homeomorphism types, or the previously exhibited flip.

## Limitations
The theorem concerns flag-preserving diagonal flips at the **minimal eleven-vertex level** on the real projective plane. It does not address flag stellar subdivisions, non-flag intermediate triangulations, flips at larger vertex counts, or metric geometry. The result is an exact finite structural classification, not a new general homotopy classification. The primary 2026 paper's complete PDF was not accessible during comparison; its openly available author-maintained data and topological descriptions were inspected instead. Equivalent unindexed earlier enumerations remain a risk. Independent validation has not been performed.

## References
[1] C. Bibby, A. Odesky, M. Wang, S. Wang, Z. Zhang, H. Zheng, *Minimal flag triangulations of lower-dimensional manifolds*, arXiv:1909.03303, first publicly available September 2019, Example 3.1, Figure 1 and Table 1. https://arxiv.org/pdf/1909.03303

[2] A. Van Tuyl, *Minimal examples of Cohen–Macaulay independence complexes that fail to be shellable or vertex decomposable*, arXiv:2610.09926, first posted October 7, 2026. Source graph6 data and author explanations: https://github.com/vantuyl/minimal-cm and https://vantuyl.github.io/minimal-cm/ .
