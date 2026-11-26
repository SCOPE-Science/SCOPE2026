# Order-two quasi-Galois centers of the Wiman sextic and the Tutte–Coxeter graph

## Finding

Let \(C\subset\mathbf P^2_{\mathbf C}\) be the smooth Wiman sextic with its classical Valentiner action. For any \(P\in\mathbf P^2\), let \(G[P]\) be the group of automorphisms of \(C\) preserving the projection \(\pi_P\) from \(P\), in the sense that \(\pi_P\circ\sigma=\pi_P\). If \(|G[P]|=2\), write \(\tau_P\) for its involution and \(\ell_P\) for the fixed line of \(\tau_P\).

The 45 centers with \(|G[P]|=2\) are exactly the quadruple points of the Wiman reflection arrangement. Their distinct fixed lines are exactly the 45 lines of the arrangement. For distinct centers \(P,Q\),
\[
P\in\ell_Q \quad\Longleftrightarrow\quad \tau_P\tau_Q=\tau_Q\tau_P.
\]
No center is on its own fixed line. Every center lies on four lines and every line contains four centers.

More precisely, the simple commuting graph on the 45 involutions is the line graph of the Tutte–Coxeter graph, the duad–syntheme Levi graph of \(GQ(2,2)\). The center–axis incidence graph is its **bipartite double cover**: it has separate copies of the 45 labels for centers and lines, and every commuting pair contributes the two cross-incidences. Identifying the center and line with the same label and merging parallel edges recovers the simple commuting graph. Thus the Levi graph itself has 30 vertices, the commuting graph has 45, and the bipartite incidence graph has 90.

The 30 Klein four-subgroups of \(A_6\) give reflection triangles: the three centers of a subgroup are the vertices and their three axes are the opposite sides. The triangles split into two \(A_6\)-orbits of 15, indexed by duads and by synthemes respectively. Each center is in one triangle of each type.

## Proof

**Automorphisms and projection centers.** The Valentiner group preserves the smooth Wiman sextic \(\Phi_6=0\) and acts faithfully as \(A_6\) [1, §§2.3, 2.5 and proof of Proposition 7.4]. The genus of a smooth plane sextic is 10, so the Hurwitz bound \(84(10-1)=756\) leaves only orders 360 and 720 for the full automorphism group. To exclude 720, Riemann–Hurwitz would require
\[
2h-2+\sum_{i=1}^b (1-1/e_i)=1/40,
\]
where \(h\) is the quotient genus and the \(e_i\ge2\) are branch orders. If \(h\ge1\), the left side is zero or at least \(1/2\). If \(h=0\), \(b\ge5\) also gives at least \(1/2\), while \(b=4\) gives zero or at least \(1/6\), and \(b\le2\) gives a nonpositive value. For \(b=3\) write the orders as \(a\le b'\le c\). If \(a\ge3\), a positive value is at least \(1/12\); if \(a=2,b'\ge4\), a positive value is at least \(1/20\). The pair \(a=b'=2\) is impossible, and with \((a,b')=(2,3)\) the positive values are \(1/42\) for \(c=7\) or at least \(1/24\) for \(c\ge8\). None is \(1/40\). Hence \(\operatorname{Aut}(C)=A_6\).

Every automorphism of this smooth plane curve is projective [2, §2, before Fact 2.4]. A nontrivial projective involution has a fixed line and an isolated fixed point \(P\): after scaling a linear representative has eigenvalues \(1,1,-1\), with \(P\) the \(-1\)-eigenline. The involution preserves every line through \(P\), so belongs to \(G[P]\). The order of this group divides the degree of \(\pi_P\) by the function-field tower through the fixed field. The projection degree is 5 if \(P\in C\) and 6 otherwise, by intersection with a general line through \(P\). Since \(|G[P]|\) is even it is 2 or 6. The group \(G[P]\) is cyclic [2, Fact 2.4] and \(A_6\) has no element of order 6 (both possible cycle types in \(S_6\) are odd). Thus every involution gives a center with group of order 2. Conversely the nontrivial member of an order-two \(G[P]\) has isolated fixed point \(P\) [2, Fact 2.4 and Corollary 2.5]. Different involutions therefore have different centers. The involutions of \(A_6\) are the 45 double transpositions. They form one conjugacy class: an odd conjugator in \(S_6\) can be adjusted using the swap of the involution's two fixed symbols. Bauer et al. [1, §2.3] identify the orbit of an involution's fixed line as the 45 Wiman lines, so the axis labeling is likewise bijective.

**Incidence and the line graph.** If \(P\in\ell_Q\), then \(\tau_Q\) fixes \(P\) and maps the projection pencil at \(P\) to itself. Conjugation by \(\tau_Q\) consequently preserves \(G[P]\), hence fixes its unique involution. Conversely, a projectivity commuting with \(\tau_P\) preserves its unique isolated fixed point. For \(P\ne Q\), if \(\tau_Q\) fixes \(P\) then \(P\) lies on \(\ell_Q\). The fixed point \(Q\) does not lie on its own axis. This gives the cross-incidences of the bipartite double cover.

A duad is a pair of symbols in a six-set and a syntheme is a partition of that set into three duads. The involution \((ab)(cd)\) labels the edge from its fixed duad \(\{e,f\}\) to the syntheme \(\{\{a,b\},\{c,d\},\{e,f\}\}\), where an edge denotes containment. This is a bijection. Two involutions having either endpoint in common commute. To see these are all the possibilities, an involution commuting with \((12)(34)\) preserves its fixed set \(\{5,6\}\) and its unordered pair of nontrivial orbits \(\{\{1,2\},\{3,4\}\}\). If it fixes 5 and 6 individually, the other double transpositions are \((13)(24)\) and \((14)(23)\); if it swaps 5 and 6, the remaining single transposition must be \((12)\) or \((34)\). The corresponding four neighbors share precisely the duad or the syntheme of \((12)(34)\). This proves the line-graph identification and four-regularity. Every center is therefore a quadruple point of the full 45-line arrangement; [1, §2.3] counts exactly 45 such points, so the two sets coincide.

**Reflection triangles.** At every vertex of the cubic duad–syntheme graph the three incident flags label the nontrivial elements of a Klein four-group. For a fixed duad these are the three double transpositions on its complement. For a fixed syntheme these are the products of two of its three disjoint pair swaps. Every commuting pair belongs to one such star and generates its Klein four-group. There are 15 duads and 15 synthemes; the classes give distinct orbits because the shared duad or shared syntheme property is preserved by conjugation. On either class the full symmetric group acts transitively; the stabilizer of a duad or a syntheme contains an odd swap, so \(A_6\) is already transitive. Each flag belongs to the two stars at its endpoints.

For each subgroup, take the lifts of its involutions with eigenvalues \(1,1,-1\), hence trace 1. If two of these projectivities commute, conjugating one lift by the other changes it only by a scalar, and trace 1 makes that scalar 1. They are commuting diagonalizable matrices and admit a simultaneous eigenbasis. The three isolated fixed points are distinct, hence they are the three coordinate points in this basis; each axis is the line through the other two. This realizes the two star classes as the two orbits of reflection triangles.

## Verification and scope

The supplied finite verifier `artifacts/verify.py` enumerates the exact \(A_6\) permutation model, including the 45 labels, their commuting adjacency, the flag bijection and the two triangle orbits. It verifies the group combinatorics, not smoothness or the projective geometry. The proof above establishes the passage from those combinatorics to the complex curve. No classification for other sextics is asserted.

The Wiman lines, multiple-point census and classical line/quadruple incidence were known. The claim here is the identification with quasi-Galois projection centers, the precise commuting and double-cover description in the duad–syntheme model, and the two triangle classes in that model. The arrangement results of [2] for sextics treat order three, not this order-two description. Classical Valentiner sources may describe some of this geometry using pole and mirror terminology.

## References

1. T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu and T. Szemberg, *Negative curves on symmetric blowups of the projective plane, resurgences and Waldschmidt constants*, arXiv:1609.08648.
2. S. Fukasawa, K. Miura and T. Takahashi, *Quasi-Galois points, II: Arrangements*, arXiv:2211.16033v1. Fact 2.4 and Corollary 2.5 there summarize the relevant projection results of their Part I, *Quasi-Galois points, I: Automorphism groups of plane curves*, Tohoku Math. J. 71 (2019), 487–494.
