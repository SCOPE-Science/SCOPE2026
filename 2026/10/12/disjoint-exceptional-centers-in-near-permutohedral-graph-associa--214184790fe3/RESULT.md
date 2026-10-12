# Disjoint exceptional centers in near-permutohedral graph associahedral toric varieties

## Finding

**Theorem (disjoint-exceptional-center characterization and integral cohomology).** Let \(n\ge3\), let \(G\) be a connected simple graph with vertex set \([n]\), and let \(X_G\) be the smooth projective graph-associahedral toric variety with fan the graphical nested fan. Let \(Y_n=X_{K_n}\), the permutohedral toric variety. The canonical toric birational morphism \(\pi_G:Y_n\to X_G\) has **pairwise disjoint exceptional prime divisors if and only if the complement \(\overline G\) is a matching** (possibly the empty matching).

In that case, if \(\overline G\) consists of \(r\) edges, with \(0\le r\le\lfloor n/2\rfloor\), the map is the blowup of exactly \(r\) disjoint, smooth, torus-invariant centers, each of complex codimension two and each isomorphic to \(Y_{n-2}\). Consequently, with \(A_m(t)=\sum_{k=0}^{m-1}A(m,k)t^k\) the Eulerian descent polynomial of the symmetric group on \(m\) letters,

\[
\sum_{k=0}^{n-1}\operatorname{rank}_{\mathbb Z}H^{2k}(X_G;\mathbb Z)t^k
=A_n(t)-rtA_{n-2}(t).
\]

The odd integral cohomology is zero and the even integral cohomology is torsion-free. In particular,
\[
\chi_{\mathrm{top}}(X_G)=n!-r(n-2)!,\qquad
\operatorname{rank}\operatorname{Pic}(X_G)=2^n-n-1-r.
\]

## Assumptions and scope

All varieties are complex smooth projective toric varieties associated with the stated **standard nested fans**. The graph \(G\) is connected, finite, simple, and has \(n\ge3\) labeled vertices. Its complement is taken on the same vertex set. A matching is a set of edges with no common endpoint; the empty set is permitted. The claimed cohomology polynomial applies only in the complement-matching case; the characterization of pairwise disjoint exceptional prime divisors applies to every connected simple \(G\). The term \(Y_1\) denotes a point (used only when \(n=3\)). A smooth center of codimension two is counted with its reduced scheme structure.

For a nonempty proper subset \(I\subsetneq[n]\), let \(u_I\) be the image of \(\sum_{i\in I}e_i\) in the quotient lattice \(N=\mathbb Z^n/\mathbb Z(1,\ldots,1)\). The rays of the fan of \(X_G\) are indexed by those \(I\) for which \(G[I]\) is connected. A set of rays forms a cone exactly when the corresponding proper nonempty connected subsets constitute a graphical tubing: two members are nested or disjoint, and any disjoint members have disconnected union. For \(Y_n\), every nonempty proper subset is a ray and cones correspond to chains.

## Proof

**1. Exceptional divisors and the graph criterion.** The braid fan (the fan of \(Y_n\)) refines the nested fan of \(G\), so the identity on \(N\) induces the proper toric birational morphism \(\pi_G\). Its exceptional prime divisors are exactly the toric invariant divisors \(D_I\) for proper nonempty subsets \(I\) such that \(G[I]\) is disconnected, because those and only those braid-fan rays are absent from the target fan. On the braid fan, \(D_I\cap D_J\ne\varnothing\) for distinct indices if and only if \(I\subsetneq J\) or \(J\subsetneq I\), since its cones correspond to chains. Thus the exceptional divisors are pairwise disjoint precisely when the disconnected proper induced subsets form an antichain under inclusion.

If \(\overline G\) is a matching, the **only** disconnected proper induced subsets are the matched pairs: for any subset of at least three vertices, each vertex has at most one nonneighbor, and the induced graph is connected (any nonadjacent pair has a common neighbor in the subset). Matched pairs are mutually incomparable.

Conversely, suppose that \(\overline G\) is not a matching. Then two of its edges have a common endpoint, say \(ab\) and \(ac\). The induced sets \(I=\{a,b\}\) and \(J=\{a,b,c\}\) are disconnected, with \(I\subsetneq J\): within \(G[J]\), the vertex \(a\) is isolated. As \(G\) is connected, \(n\ge4\), so \(J\subsetneq[n]\). Thus \(D_I\) and \(D_J\) intersect. This proves the equivalence including the boundary case \(n=3\), where no connected graph has a nonmatching complement.

**2. Blowups and identification of centers.** Assume \(\overline G\) consists of disjoint pairs \(\{a_i,b_i\}\), \(1\le i\le r\). Adding one of these missing edges to \(G\) enlarges its graphical building set only by the two-element subset \(\{a_i,b_i\}\), since every subset of at least three vertices was already connected. The new nested fan is the star subdivision of the two-dimensional smooth cone \(\sigma_i=\operatorname{cone}(u_{\{a_i\}},u_{\{b_i\}})\), introducing the primitive ray \(u_{\{a_i,b_i\}}=u_{\{a_i\}}+u_{\{b_i\}}\). Hence this step is the ordinary toric blowup of the invariant smooth codimension-two center \(Z_i=V(\sigma_i)\). For distinct matching pairs the two cones cannot lie in any common fan cone: a singleton from one pair is adjacent in \(G\) to every singleton in the other, so they are incompatible as disjoint tubes. Therefore the centers are pairwise disjoint, and these star subdivisions commute.

Fix one pair \(\{a,b\}\), and put \(R=[n]\setminus\{a,b\}\). A proper tube compatible with both singleton tubes \(\{a\}\) and \(\{b\}\), other than the singletons, must contain both \(a\) and \(b\). Indeed, a nonempty tube disjoint from both is adjacent to each singleton; and a tube containing just one of them, together with some vertex in \(R\), is adjacent to the other singleton. The permitted additional tubes are precisely \(\{a,b\}\cup U\), where \(\varnothing\ne U\subsetneq R\); each is connected because both \(a\) and \(b\) are adjacent to all vertices in \(R\). Compatible families of these additional tubes are chains in \(U\). The quotient lattice \(N/(\mathbb Zu_{\{a\}}+\mathbb Zu_{\{b\}})\) identifies canonically with \(\mathbb Z^R/\mathbb Z(1,\ldots,1)\), and the quotient ray indexed by \(\{a,b\}\cup U\) becomes \(u_U\). Thus the star fan of \(\sigma_i\) is the full braid fan on \(n-2\) labels. The center is \(Z_i\cong Y_{n-2}\). Each has dimension \(n-3\) in the ambient dimension \(n-1\), hence codimension two.

**3. Cohomology and Picard group.** For a blowup of a smooth variety along a smooth codimension-two center \(Z\), the integral blowup decomposition gives \(H^{j}(\operatorname{Bl}_Z X;\mathbb Z)\cong H^j(X;\mathbb Z)\oplus H^{j-2}(Z;\mathbb Z)\) as graded abelian groups. The centers here are disjoint, so these extra summands add. Smooth complete toric varieties have torsion-free integral cohomology in even degrees and zero in odd degrees. The permutohedral toric variety \(Y_m\) has \(P_{Y_m}(t)=A_m(t)\), the classical Eulerian \(h\)-polynomial. Applying the codimension-two formula to \(Y_n\to X_G\) yields \(A_n(t)=P_{X_G}(t)+rtA_{n-2}(t)\), proving the displayed polynomial and group assertions. At \(t=1\), the polynomial yields \(n!-r(n-2)!\). Finally \(X_G\) has \((2^n-2)-r\) rays, so its Picard rank equals its ray count minus \(n-1\), namely \(2^n-n-1-r\). This completes the proof.

## Verification

The included `near_permutohedral_checker.py` uses only the Python standard library; run `python3 near_permutohedral_checker.py`. It checks the disconnected-set antichain characterization for **all 770 connected labeled simple graphs on three, four, or five vertices**. Independently of the fan blowup calculation, it enumerates maximal tubings using vertex-root recursion, forms every tubing face, computes the simple-polytope \(h\)-polynomial from its \(f\)-vector, and compares with \(A_n(t)-rtA_{n-2}(t)\) for all \(3\le n\le7\) and all permitted \(r\) (16 parameter cases). The large case \(n=7,r=3\) has Betti vector \((1,117,1113,2218,1113,117,1)\) and Euler characteristic \(4680\). The code prints `ALL_CHECKS_PASSED` on success. These finite checks are regression tests, not proofs for all \(n\); the all-parameter result rests on the chain-fan and toric blowup arguments above.

## Relationship to prior work

Postnikov–Reiner–Williams develop general graph-associahedron/nestohedron nested complexes, stellar subdivisions, and \(h\)-polynomials (notably their Sections 6, 8, 10, and 14); that broad machinery is prior art. Da Rosa–Jensen–Ranganathan develop the graph-associahedral blowup construction and its relationship with Losev–Manin/Hassett compactifications. Suyama constructs the graph nested toric fans and classifies Fano and weak Fano cases, with primary MSC 14M25. None of the inspected results states the exact **if-and-only-if characterization** of a disjoint exceptional locus for the permutohedral-to-graph-associahedral contraction together with the identification of every center as a smaller permutohedral variety. The Eulerian deficit is presented as a consequence of that geometric classification, **not** as a claim to have invented Eulerian \(h\)-polynomials or the general blowup formula.

## Limitations

The disjoint-center factorization and displayed cohomological formulas are asserted only when the complement graph is a matching; arbitrary connected graphs can have intersecting exceptional divisors and more complicated contractions. The direct-sum statement is about graded integral groups, not a canonical isomorphism of cohomology rings. This is a self-review, with no independent audit or claim of exhaustive global literature coverage. General nested-fan and blowup results could allow an independent derivation; the assessed point is the explicit graph-theoretic classification and uniformly identified centers.

## References

1. Rodrigo Ferreira da Rosa, David Jensen, Dhruv Ranganathan, *Toric graph associahedra and compactifications of* \(M_{0,n}\), arXiv:1411.0537 (first public 2014-11-03); https://arxiv.org/html/1411.0537v2 .
2. Yusuke Suyama, *Toric Fano varieties associated to finite simple graphs*, arXiv:1604.08440 (first public 2016-04-28; primary MSC 14M25), https://arxiv.org/html/1604.08440v1 .
3. Alexander Postnikov, Victor Reiner, Lauren Williams, *Faces of generalized permutohedra*, arXiv:math/0609184 (first public 2006-09-06), https://arxiv.org/html/math/0609184v2 .
