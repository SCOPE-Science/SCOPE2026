# Dual mutual-visibility coloring of crown cones
## Finding
For every integer \(n\ge2\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) and \(G_n=K_1\vee\operatorname{Cr}_n\), with universal hub \(h\). A dual mutual-visibility set \(X\) containing \(h\) exists exactly when \(X\) contains one endpoint from each deleted matching pair and, writing \(p=|X\cap A|\), \(1\le p\le n-1\), \(p\ne2\), and \(n-p\ne2\). Hence \(\chi_{\mu_d}(G_n)=\infty\) exactly for \(n=3\), while \(\chi_{\mu_d}(G_n)=2\) for \(n=2\) and every \(n\ge4\). The number of dual sets containing \(h\) is \(\sum_{1\le p\le n-1,\ p\ne2,\ n-p\ne2}\binom{n}{p}\).

Thus the wheel \(C_6\vee K_1=G_3\) is the unique infinite case in this cone-over-crown family. For \(n\ge5\), the hub-set count simplifies to \(2^n-2-2\binom{n}{2}\); for \(n=4\) it is \(8\).

## Assumptions and scope
Graphs are finite, simple, connected, and nontrivial. Write the crown shores as \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with deleted matching \(a_i b_i\), and adjoin a universal hub \(h\). Two vertices are \(X\)-visible if some shortest path has no internal vertex in \(X\). A dual set requires this for pairs both in \(X\) and pairs both outside \(X\); \(\chi_{\mu_d}\) is the minimum number of dual sets in a vertex partition, or \(\infty\) if none exists.

## Proof
Assume \(h\in X\). Each matched nonedge \(a_i b_i\) has the unique length-two geodesic \(a_i h b_i\). Hence its endpoints cannot lie on the same side of \(X\): exactly one endpoint from each matched pair lies in \(X\).

Put \(p=|X\cap A|\) and \(q=n-p\). For two selected \(A\)-vertices \(a_i,a_j\), the hub route is blocked. An unblocked length-two route exists exactly through some \(b_k\notin X\) with \(k\notin\{i,j\}\); after the matched-pair split, these available \(b_k\) correspond exactly to selected \(A\)-indices. Thus selected \(A\)-pairs are all visible exactly when \(p=1\) or \(p\ge3\), so \(p\ne2\). Symmetrically \(q\ne2\). For two \(A\)-vertices outside \(X\), visibility requires at least one available \(b_k\notin X\), which is equivalent to \(p\ge1\); symmetrically \(q\ge1\). Unmatched cross-shore pairs are adjacent. This proves the criterion and its sufficiency.

Every admissible set is determined by the \(p\) indices whose \(A\)-endpoint is chosen, giving the binomial sum. The allowed set of \(p\) is empty exactly for \(n=3\); \(p=1\) works for \(n=2\) and every \(n\ge4\).

If admissible \(X\) exists, let \(Y=V(G_n)\setminus X\). Since \(h\notin Y\), every nonadjacent pair not involving \(h\) has a shortest two-edge path through \(h\) whose internal vertex lies outside \(Y\), and pairs involving \(h\) are adjacent. Hence \(Y\) is total mutual-visible and therefore dual, so \(\{X,Y\}\) is a dual two-coloring. One color fails because every matched pair is nonadjacent and its hub geodesic is blocked by the full vertex set. For \(n=3\), no dual set contains \(h\), hence no dual coloring exists.

## Verification
The standalone verifier exhausts every hub-containing subset for \(2\le n\le8\), tests dual visibility directly from common-neighbor geodesics, compares with the proved criterion, checks a two-class witness when allowed, and checks the one-color obstruction. It returned:

`ALL CHECKS PASSED; n_range=2..8; hub_containing_subsets=87376; counts={2: 2, 3: 0, 4: 8, 5: 10, 6: 32, 7: 84, 8: 198}`

This is a finite stress test only; the universal statement is proved above.

## Relationship to prior work
Babu, Jakovac, Kuziak, Lakshmanan S., and Yero introduce dual mutual-visibility coloring in arXiv:2609.31427v1. Their inspected full text says the general characterization of graphs with infinite dual mutual-visibility chromatic number remains open and gives \(C_6\vee K_1\) as an example whose hub belongs to no dual set. Since \(C_6=\operatorname{Cr}_3\), that \(n=3\) member is prior coverage. The new content is the exact criterion for every \(n\), the proof that this is the unique obstruction in the whole crown-cone family, and the exact hub-set count.

Bujtás, Klavžar, and Tian study dual visibility spectra and polynomials, including \(K_{n,n}\), but their inspected open-access text contains no crown, join, or perfect-matching-deletion cone theorem. Searches under crown, deleted-perfect-matching, bipartite-Kneser, cone, apex, and universal-vertex aliases found no statement implying this classification.

## Limitations
The theorem is specific to \(K_1\vee(K_{n,n}-M_n)\). It does not characterize arbitrary cones or all diameter-two graphs. The \(n=3\) infinite case is prior literature; novelty is the all-parameter structural classification and count. Very recent or unindexed equivalent work remains a residual risk.

## References
1. S. Babu, M. Jakovac, D. Kuziak, A. Lakshmanan S., I. G. Yero, “A variety of the mutual-visibility coloring problem for graphs,” arXiv:2609.31427v1, 2026.
2. C. Bujtás, S. Klavžar, J. Tian, “Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets,” Aequationes Mathematicae 99 (2025), 1883–1901, DOI:10.1007/s00010-025-01197-y.
