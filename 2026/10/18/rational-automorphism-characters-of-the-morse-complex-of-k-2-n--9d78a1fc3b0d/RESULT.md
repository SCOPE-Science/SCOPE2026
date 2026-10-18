# Rational automorphism characters of the Morse complex of \(K_{2,n}\)

## Finding
For every integer \(n\ge 2\), let \(G=K_{2,n}\) have left vertices \(a,b\) and right vertices \(u_1,\ldots,u_n\), and let \(X=\mathcal M(G)\) be the ordinary simplicial complex of acyclic discrete Morse matchings of the graph. The natural subgroup \(H=C_2\times S_n\) acts by exchanging \(a,b\) and permuting the right vertices. For \(\sigma\in S_n\), write \(f(\sigma)\) for its number of fixed points and \(t(\sigma)\) for its number of cycles of length two. Then reduced rational homology vanishes outside degree \(n\), and the full character of the degree-\(n\) representation is
\[
\chi_n(s^e,\sigma)=\operatorname{sgn}(\sigma)\begin{cases}
f(\sigma)^2-1,&e=0,\\
(-1)^n\bigl(f(\sigma)-2t(\sigma)-1\bigr),&e=1,
\end{cases}
\]
where \(s\) exchanges the left vertices. In particular, its dimension is \(n^2-1\).

An equivalent complete rational-module description is
\[
\widetilde H_n(X;\mathbb Q)\cong
\operatorname{sgn}_{S_n}\otimes\left[
\varepsilon^n\otimes\bigl(\widetilde P_n\oplus\textstyle\bigwedge^2P_n\bigr)
\oplus\varepsilon^{n+1}\otimes U_n\right].
\]
Here \(P_n=\mathbb Q^n\) is the natural permutation representation of \(S_n\), \(\widetilde P_n=P_n/\mathbb Q(1,\ldots,1)\), \(U_n\) is the permutation representation on unordered pairs of distinct right vertices, and \(\varepsilon\) is the nontrivial one-dimensional representation of \(C_2\). The tensor products implicitly inflate representations from their respective factors. This is a rational representation statement, not an integral lattice classification.

## Assumptions and scope
A vertex of \(X\) is an incidence pair \((v,e)\), where \(e\) is an edge incident to the vertex \(v\) of \(G\). A simplex is a set of incidence pairs using each cell at most once and forming an acyclic discrete vector field; equivalently, orient each selected edge away from its matched vertex, require outdegree at most one at each graph vertex, and prohibit directed cycles. Write \(A_i=(a,au_i)\), \(B_i=(b,bu_i)\), \(X_i=(u_i,au_i)\), and \(Y_i=(u_i,bu_i)\). The only directed cycle obstructions are the directed four-cycles \(\{A_i,Y_i,B_j,X_j\}\) for \(i\ne j\). Thus a face uses at most one \(A_i\), at most one \(B_j\), at most one of \(X_i,Y_i\) at each right vertex, and no incidence cell twice, subject to those four-cycle obstructions. The group action permutes incidence pairs and preserves faces.

## Proof
The nonequivariant sphere-wedge classification for this graph family is established by the shellability and homotopy calculation for directed forests of complete bipartite graphs: reversing all directed arrows identifies its directed-forest complex equivariantly with \(X\). In particular, Jojić's Corollary 3.1 with the bipartition sizes \(2,n\) yields \(X\simeq\bigvee^{n^2-1}S^n\), so only \(\widetilde H_n(X;\mathbb Q)\) remains. We now compute its character directly, without requiring an equivariant shelling.

For \(g\in H\), sum over all \(g\)-invariant faces \(F\), including the empty face, the signed quantity
\[
Z(g)=\sum_{gF=F}(-1)^{|F|}\operatorname{sgn}(g\mid F).
\]
The sign is the permutation sign on the selected vertices of the simplicial complex. The reduced simplicial Lefschetz identity and concentration of homology in degree \(n\) give \(\chi_n(g)=(-1)^{n+1}Z(g)\). More importantly, selecting an entire orbit of size \(d\) of incidence-pair vertices contributes \((-1)^d(-1)^{d-1}=-1\) to \(Z\). Thus the alternating sum can be evaluated by admissible whole-orbit choices.

First suppose \(g=(1,\sigma)\). Let \(c\) be the total number of cycles of \(\sigma\), and \(f=f(\sigma)\). When neither left vertex has an outgoing arrow, every cycle of right vertices permits exactly three invariant local states (all empty, all pointing to \(a\), or all pointing to \(b\)), with aggregate weight \(1-1-1=-1\); hence its contribution is \((-1)^c\). Exactly one left vertex with an outgoing arrow must point to a fixed right vertex. At that vertex the remaining choices (empty or the other leftward arrow) cancel, so this class contributes zero. If both left vertices have outgoing arrows, they point to two fixed right vertices (possibly the same). For each ordered pair of fixed vertices the local sum equals \((-1)^{c-1}\): for the same target, the target has no outgoing arrow and removes one former factor \(-1\); for different targets, the only admissible choices for the two target right vertices are neither, the first permitted arrow, or the second permitted arrow (both together would close a directed four-cycle), giving weight \(1-1-1=-1\) in place of their previous product \(({-1})^2\). Thus
\[
Z(1,\sigma)=(-1)^c+f^2(-1)^{c-1}=(-1)^{c-1}(f^2-1).
\]
Since \(\operatorname{sgn}(\sigma)=(-1)^{n-c}\), the asserted no-swap character follows.

Now suppose \(g=(s,\sigma)\). Invariance forces the two left vertices to have outgoing arrows either both or neither. Let \(r\) count the even-length cycles of \(\sigma\). With neither outgoing, an odd-length cycle of right vertices permits only the empty state, whereas an even-length cycle admits the empty state and two alternating whole-arrow orbits, with combined weight \(1-1-1=-1\). The contribution is \((-1)^r\). With both outgoing, a pair \(A_i,B_j\) is invariant exactly when \(j=\sigma(i)\) and \(i=\sigma(j)\); consequently its target lies in a fixed-point cycle or in a two-cycle. Each fixed point contributes \(-(-1)^r\) because its two outgoing left arrows form one selected orbit and its right arrow is absent. Each two-cycle gives two possible outgoing left-arrow orbits; neither allows the other alternating right-arrow orbit, which would close a directed four-cycle. Replacing that cycle's former factor \(-1\) by the two possibilities of weight \(-1\) each contributes \(+2(-1)^r\). Summing these disjoint possibilities gives
\[
Z(s,\sigma)=(-1)^r\bigl(1-f(\sigma)+2t(\sigma)\bigr).
\]
Every even cycle contributes an odd permutation sign, so \((-1)^r=\operatorname{sgn}(\sigma)\). Applying the Lefschetz identity yields the swap character.

Finally, \(\widetilde P_n\), \(\bigwedge^2 P_n\), and \(U_n\) have respective \(S_n\)-characters \(f-1\), \(\binom f2-t\), and \(\binom f2+t\). Their displayed \(C_2\)-weighting therefore has the same character on both kinds of group elements. Finite-dimensional rational representations of finite groups are semisimple and are determined by their characters, proving the module decomposition.

## Verification
The accompanying standalone standard-library script `verify_equivariant_k2n.py` enumerates every acyclic partial incidence matching from its definition for \(2\le n\le6\), evaluates orientation signs for every conjugacy-class representative of \(S_n\) and both values of the left swap, and compares all \(56\) resulting characters with the formula. Its augmented-face counts are \(45,216,945,3888,15309\), respectively. For \(2\le n\le5\) it also independently computes exact reduced mod-two boundary ranks in every dimension, recovering rank \(n^2-1\) only in degree \(n\). All tests complete with `VERIFY_OK`. The finite enumeration checks the formulas in small cases; the proof above handles every \(n\ge2\).

## Relationship to prior work
Jojić (2012) identifies the same directed-forest complex and proves shellability and the sphere-wedge homotopy type for complete bipartite graphs, in particular the nonequivariant \(n^2-1\) sphere count. A later publicly available calculation gives that same nonequivariant classification using a different discrete-Morse argument. Lin and Scoville (2019) determine automorphism groups of Morse complexes, rather than the induced homology representations. Scoville (2026) develops new structural methods for Morse complexes of simplices and records the general action of graph automorphisms on the construction. None of those results supplies the signed character values or the rational \(C_2\times S_n\)-module decomposition asserted here. The character cannot be inferred from the dimension of the homology or from the existence of the group action alone.

## Limitations
This is a rational homology representation classification for the specified natural subgroup \(C_2\times S_n\), not an integral module, full equivariant homotopy, or equivariant stable splitting theorem. When \(n=2\), the graph has extra automorphisms interchanging its two bipartition classes, which are not part of the stated subgroup. The mathematical novelty claim is qualified by the possibility of an unindexed equivalent character computation. The already-known sphere-wedge classification is expressly used as an input, not presented as a new result.

## References
1. N. A. Scoville, “The complex of discrete Morse matchings of the \(n\)-simplex: homotopy types and structural results,” arXiv:2604.18172v1, first public 2026-04-20, primary MSC2020 05E45 and 57Q70, https://arxiv.org/html/2604.18172v1.
2. D. Jojić, “Complexes of directed trees of complete multipartite graphs,” *Publications de l'Institut Mathématique* 92(106) (2012), 43–51, DOI:10.2298/PIM1206043J, https://doiserbia.nb.rs/ft.aspx?id=0350-13021206043J.
3. M. Lin and N. A. Scoville, “On the automorphism group of the Morse complex,” arXiv:1904.10907, first public 2019-04-24, https://arxiv.org/abs/1904.10907.
4. N. A. Scoville and M. C. B. Zaremsky, “Higher connectivity of the Morse complex,” arXiv:2004.10481, first public 2020-04-22, https://arxiv.org/abs/2004.10481.
