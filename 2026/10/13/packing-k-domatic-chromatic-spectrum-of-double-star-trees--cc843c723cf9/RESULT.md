# Packing \(k\)-domatic chromatic spectrum of double-star trees

## Finding
For integers \(a,b\ge1\), let \(D_{a,b}\) be the double-star tree with two adjacent centers and respectively \(a\) and \(b\) pendant leaves. Put \(N=a+b+2\). Its packing \(k\)-domatic chromatic number is
\[
\chi_{\rho,k}(D_{a,b})=\begin{cases}
3,&1\le k\le3,\\
k,&4\le k\le N,\ k\in\{a+2,b+2\},\\
k+1,&4\le k\le N,\ k\notin\{a+2,b+2\},\\
+\infty,&k>N.
\end{cases}
\]
Thus, beyond three broadcast-dominating classes, a palette with exactly one color per class is possible only at two center-degree-determined values (one if \(a=b\)); every other feasible class number needs exactly one more color.

## Assumptions and scope
All graphs are finite, simple, undirected, and nonempty. A packing coloring is a map \(f:V(G)\to\{1,\dots,t\}\) such that distinct vertices of equal label \(i\) have graph distance greater than \(i\). A nonempty set \(B\subseteq V(G)\) is a broadcast-dominating part of \(f\) when every vertex \(v\in V(G)\) has some \(w\in B\) with \(d(v,w)\le f(w)\). A packing \(k\)-domatic coloring has a partition of all vertices into \(k\) nonempty broadcast-dominating parts; its chromatic number \(\chi_{\rho,k}\) is the least permitted palette bound \(t\), with value \(+\infty\) when impossible. Colors need not all occur. The theorem assumes two nonempty pendant sides, equivalently that the tree has diameter three. We also regard \(k=1\) as the ordinary packing-chromatic requirement, because the whole vertex set is automatically broadcast-dominating.

## Proof
Write \(U,V\) for the centers and \(A,B\) for the pendant sets of respective sizes \(a,b\). The graph has diameter three. The packing coloring labeling every leaf \(1\), \(U\) with \(2\), and \(V\) with \(3\) uses three colors and admits three broadcast-dominating parts: the set of all leaves and the singleton sets \(\{U\},\{V\}\). Indeed every vertex has a leaf within distance one, while both centers have eccentricity two. Merging parts proves the upper bound three for \(k=1,2,3\). The induced four-vertex path gives ordinary packing chromatic number at least three, so equality follows for these values.

For the remaining cases \(k\ge4\), first note that any two vertices with the same label \(i\ge3\) would have distance at most three, so they cannot share a label. Call the vertices labeled at least two **anchors**. There are at most \(t-2\) anchors of label at least three; label two can occur at most twice. If twice, the two vertices must be pendant leaves on opposite sides, since only those pairs are at distance three. Distinct broadcast-dominating parts composed only of label-one vertices cannot both exist: each such part is a dominating set using radius one, but two disjoint dominating independent sets would have an edge between them, whereas all label-one vertices form an independent set. Furthermore, no independent dominating set avoiding both opposite-side leaves exists. To see this, every independent dominating set of \(D_{a,b}\) is one of the following three sets: all leaves, \(\{U\}\cup B\), or \(\{V\}\cup A\). Each meets any pair of opposite-side leaves.

Suppose a packing \(k\)-domatic coloring uses \(t<k\) colors. With at most one label-two vertex, the number of anchors is at most \(t-1\le k-2\), forcing at least two label-one-only parts, impossible. With two label-two vertices, the number of anchors is at most \(t\le k-1\), forcing at least one label-one-only part; the above independent-dominating classification rules this out. Therefore \(t\ge k\).

Now suppose \(t=k\). If two label-two vertices exist, they are opposite-side leaves. If there is a label-one-only part, the independent dominating classification again gives a contradiction. Otherwise each of the \(k\) parts contains exactly one anchor: the two label-two leaves and \(k-2\) higher-labeled vertices. To dominate the label-two leaf attached to \(V\), the broadcast part containing the label-two leaf attached to \(U\) must also contain the center \(V\), labeled one: no other label-one vertex is within the leaf's radius-two coverage, and its own label-two vertex is at distance three. Symmetrically the other label-two part must contain \(U\), labeled one. But the two adjacent centers cannot both have label one. Hence there can be at most one label-two vertex.

With one label-two vertex there are at most \(k-1\) anchors and, as before, at most one label-one-only part. Exactly \(k-1\) anchors and exactly one such part are therefore necessary. That label-one-only part must contain every label-one vertex (a distinct label-one vertex cannot be dominated by another label-one vertex because the entire label-one color class is independent). Consequently each anchor is the sole vertex of its part, so the unique label-two anchor must broadcast-dominate on its own. It must be one of the two centers, the only vertices of eccentricity two. The common label-one class must be an independent dominating set. Its complement consists exactly of the anchors, and hence has size \(k-1\). The three independent dominating sets listed above have complements of size \(2\), \(a+1\), and \(b+1\); since \(k\ge4\), this forces \(k\in\{a+2,b+2\}\).

Conversely if \(k=a+2\), label \(U\) and all leaves in \(B\) by one, label \(V\) by two, and give the \(a\) leaves in \(A\) distinct labels \(3,\ldots,a+2\). The parts \(\{U\}\cup B\), \(\{V\}\), and the singleton \(A\)-leaves give \(k\) broadcast-dominating parts. The case \(k=b+2\) is symmetric. Thus \(t=k\) is possible precisely at these exceptions.

For any other \(4\le k\le N\), choose \(N-k\) leaves and color them one; color \(U\) two; label each of the remaining \(k-1\) vertices with a different color from \(3\) through \(k+1\). The part containing \(U\) and all label-one leaves broadcast-dominates (the center alone reaches distance two), and each higher-labeled vertex singleton broadcast-dominates (diameter three). The labels constitute a packing coloring: all color-one vertices are pairwise nonadjacent and all higher labels are unique. This supplies \(\chi_{\rho,k}\le k+1\), with the lower bound already proved. Finally, a partition into more than \(N\) nonempty parts does not exist.

## Verification
A dependency-free verifier, `verify_double_star.py`, independently constructs and checks the claimed colorings and partitions for every ordered pair \(1\le a,b\le14\) and every \(2\le k\le a+b+2\). It tests packing constraints, broadcast domination, group partitioning, and palette bound. Its separate exhaustive state search for \(a,b\le4\), \(a+b\le6\), decides whether \(k\) colors suffice for every \(3\le k\le N\), up to symmetry among colors at least three. The recorded program output appears in `verification_output.txt`. Finite tests corroborate but do not replace the all-parameter proof above.

## Relationship to prior work
Brešar, Ferme, and Hu [1] define the packing \(k\)-domatic chromatic number, prove general bounds and examples, and analyze paths and cycles as well as subdivided double stars. Their general diameter-two observations do not cover the diameter-three trees here; their path theorem covers the particular four-vertex path \(D_{1,1}\), which is expressly not asserted to be a new case. Kristiana et al. [2] study *ordinary* packing colorings of double stars (in particular their three-color value), not the partition into multiple broadcast-dominating parts. This theorem gives the all-parameter exact spectrum for the nondegenerate double-star family.

## Limitations
The theorem concerns only double stars with both leaf sets nonempty and the specified broadcast-part definition; it makes no claim for larger-diameter trees or variant domatic notions. The finite verification bounds are explicitly limited, and independent external audit has not been performed. Searches of currently accessible literature do not exclude an unindexed equivalent treatment.

## References
[1] B. Brešar, J. Ferme, and S. Hu, *Partitioning an S-packing coloring into broadcast dominating sets*, arXiv:2610.03477v1, first posted 2026-10-02, https://arxiv.org/abs/2610.03477 .

[2] Kristiana et al., *On The Packing k-Coloring of Some Family Trees*, *Statistics, Optimization & Information Computing*, doi:10.19139/soic-2310-5070-2047, https://doi.org/10.19139/soic-2310-5070-2047 .
