# Spectral-symmetry classification and exact orientation census for bouquets of cycles

## Finding

Let \(B(\ell_1,\ldots,\ell_k)\) be the finite simple graph obtained by identifying one vertex of each of \(k\ge1\) cycles, with integer cycle lengths \(\ell_i\ge3\), and leaving all other vertices distinct. Orient every edge in exactly one direction. For an orientation \(D\), define the Hermitian adjacency matrix \(H(D)\) by \(H_{uv}=\zeta\) for an arc \(u\to v\), \(H_{vu}=\overline\zeta\), and \(H_{uv}=0\) for nonedges, where \(\zeta=\exp(\mathrm{i}\pi/3)\). Call \(D\) spectrally symmetric when the multiset of real eigenvalues of \(H(D)\) equals its negative.

For every odd integer \(s\ge3\), let \(k_s\) be the number of cycles of length \(s\). Choose an arbitrary cyclic traversal of each cycle, and let \(g_i\) be the product of its Hermitian edge entries along that traversal. For an odd cycle, its real cycle weight \(w_i=g_i+\overline{g_i}\) is either \(1\) or \(-2\).

**Classification.** The orientation \(D\) is spectrally symmetric if and only if, for every odd length \(s\), exactly \(k_s/3\) of the cycles of length \(s\) have weight \(-2\), and exactly \(2k_s/3\) have weight \(1\). Orientations of even cycles are arbitrary. In particular, a spectrally symmetric orientation exists if and only if every \(k_s\) is divisible by \(3\).

**Exact census.** Distinguishing every edge and both arc directions, the number of spectrally symmetric orientations is zero unless every odd \(k_s\) is a multiple of three. Otherwise it is

\[
2^{\sum_{s\,\mathrm{even}}s k_s}
\prod_{s\,\mathrm{odd}}
\binom{k_s}{k_s/3}
\left(\frac{2^s-2}{3}\right)^{k_s/3}
\left(\frac{2^{s+1}+2}{3}\right)^{2k_s/3}.
\]

Empty products equal \(1\). Thus bouquets of three triangles have exactly \(216\) qualifying orientations out of \(512\), bouquets of three pentagons have exactly \(14520\) out of \(32768\), while any bouquet with one or two pentagons and any number of triangles cannot be spectrally symmetric.

## Assumptions and scope

Graphs are finite, simple, with exactly one common hub, and no overlap among the cycles away from that hub. An orientation places one arc on each undirected edge; there are no undirected double arcs. Edge orientations are counted as labelled assignments, without quotienting by graph automorphisms or global arc reversal. All formulae hold for arbitrary \(k\ge1\), arbitrary cycle lengths at least three, repeated lengths, and both parities. No assertion is made for general cactus graphs whose cycles are attached at different vertices.

## Proof

**1. A characteristic-polynomial identity.** Let \(P_0(X)=1\), \(P_1(X)=X\), and recursively \(P_m(X)=XP_{m-1}(X)-P_{m-2}(X)\) for \(m\ge2\). These are characteristic polynomials of paths with \(m\) vertices; orientation edge phases can be removed by diagonal unitary conjugation on any tree. For each cycle put \(Q_i(X)=P_{\ell_i-1}(X)\). With the hub first, the remaining matrix is a block diagonal union of weighted paths of sizes \(\ell_i-1\). Schur complement at the hub yields the rational-function identity

\[
\det(XI-H(D))=
\left(\prod_{i=1}^k Q_i(X)\right)
\left[X-\sum_{i=1}^k
\frac{2P_{\ell_i-2}(X)+w_i}{Q_i(X)}\right].
\tag{1}
\]

To verify the numerator for the \(i\)-th path, the inverse of its tridiagonal \(XI-H\) matrix has diagonal entries \(P_{\ell_i-2}/Q_i\) at either endpoint and an endpoint-to-endpoint entry whose phase is the product of the path edge phases divided by \(Q_i\). The two hub edges contribute two identical diagonal terms and two conjugate through-path terms; their total phase is \(g_i+\overline{g_i}=w_i\). Equation (1) is first valid away from roots of the \(Q_i\), hence holds identically as a polynomial equality after clearing denominators.

**2. Isolation by cycle length.** Each \(P_m\) has parity \((-1)^m\), i.e. \(P_m(-X)=(-1)^mP_m(X)\). Thus \(X\) and every \(2P_{\ell_i-2}/Q_i\) are odd rational functions. If \(\ell_i\) is even, then \(1/Q_i\) is odd; if \(\ell_i\) is odd, \(1/Q_i\) is even. Therefore, after dividing (1) by \(\prod_i Q_i(X)\), the deviation from its required parity is exactly the even rational function

\[
-\sum_{s\,\mathrm{odd}}\frac{W_s}{P_{s-1}(X)},
\qquad W_s=\sum_{i:\,\ell_i=s}w_i.
\tag{2}
\]

A real Hermitian matrix has symmetric eigenvalue multiset exactly when its characteristic polynomial has parity \((-1)^{|V|}\). Since the product of \(Q_i\) has definite parity, the preceding observation proves symmetry if and only if the rational expression in (2) vanishes identically.

The rational functions \(1/P_{s-1}(X)\), for distinct odd \(s\), are linearly independent over the constants. Indeed, let \(s_0\) be the smallest index with nonzero coefficient in a finite purported relation. As \(X\to+\infty\), the \(s_0\)-term has leading order \(X^{-(s_0-1)}\), whereas all later terms are of strictly smaller order, a contradiction. Therefore (2) vanishes if and only if every \(W_s=0\).

**3. Two possible weights and their balancing condition.** On an odd cycle, write \(g_i=\zeta^{t_i}\), where \(t_i\) is the number of forward-oriented edges minus the number of backward-oriented edges on a chosen traversal. Because \(t_i\) is odd, \(2\cos(t_i\pi/3)\) equals either \(1\) or \(-2\). If \(a_s\) denotes the number of weight \(-2\) cycles among the \(k_s\) cycles of a fixed odd length, then

\[
W_s=(k_s-a_s)-2a_s=k_s-3a_s.
\]

Hence \(W_s=0\) exactly when \(a_s=k_s/3\). This proves the classification, and also the necessity of \(3\mid k_s\). The sufficiency includes the even-cycle case because their contributions have the requisite odd parity regardless of orientation.

**4. Counting all labelled orientations.** For one odd cycle of length \(s\), let \(a\) be its number of orientations with weight \(-2\), and \(b\) the number with weight \(1\). Clearly \(a+b=2^s\). Summing all cycle weights over orientations independently edge by edge yields

\[
-2a+b=\sum_D(g(D)+\overline{g(D)})
=(\zeta+\overline\zeta)^s+(\zeta+\overline\zeta)^s=2,
\]

since \(\zeta+\overline\zeta=1\). Solving gives \(a=(2^s-2)/3\) and \(b=(2^{s+1}+2)/3\). For the \(k_s\) distinguished cycles, choose which \(k_s/3\) receive weight \(-2\); multiply independent orientation counts. Every even cycle of length \(s\) contributes \(2^s\) choices. Independence of the edge sets completes the stated product formula. The numbers \(a,b\) are strictly positive for every odd \(s\ge3\), so the divisibility criterion also guarantees existence.

## Verification

The accompanying standalone `verify.py` uses exact arithmetic in the integral ring generated by \(\zeta\), satisfying \(\zeta^2=\zeta-1\). It computes full matrix characteristic polynomials using the exact Faddeev–LeVerrier procedure and independently computes (1) using integral path-polynomial recurrences. The script checked equality and the parity criterion for \(880\) explicitly generated oriented bouquets. It also exhaustively enumerated all \(512\) orientations of the three-triangle bouquet and obtained \(216\) symmetric ones, and independently enumerated one-cycle weights for lengths \(3\), \(5\), \(7\), and \(9\). All checks passed (`VERIFY_OK`). Other listed multi-cycle checks sample orientations and are not exhaustive. Run with `python3 verify.py` from the directory containing this document. The infinite-dimensional parameter statement is established by the proof, not by enumeration.

## Relationship to prior work

Akbari, Aloni, Levit, Mohar and Xia [1] introduce the spectral-symmetry problem for the sixth-root Hermitian adjacency matrix, prove triangle-balance constraints and a one-sum closure theorem requiring suitable **already** spectrally symmetric pieces. A single odd cycle is not individually symmetric, and the new length-by-length cancellation criterion for multiple such cycles, including its exact orientation count, is not a stated consequence of that one-sum closure theorem. The triangle case agrees with the necessary two-to-one transitive/directed triangle ratio of [1] but proves sufficiency here and extends that phenomenon to every odd length without cross-length cancellation.

Li and Yu [2, Theorems 2.6–2.8] provide general Hermitian characteristic-polynomial coefficient formulas and vertex/cycle deletion recurrences. Such generic identities can be used to derive the underlying determinant, but do not directly state the divisibility-by-three criterion, the separation by individual odd cycle lengths, or the closed orientation count. Equation (1) is derived here directly by a Schur complement. Mohar [3] provides the foundational sixth-root matrix theory. These dependencies and overlaps are expressly acknowledged; this theorem is a specialization and explicit classification, not a claim to invent Hermitian characteristic recurrences.

## Limitations

This result concerns a bouquet with **one** shared vertex, not arbitrary intersecting cycles or arbitrary cactus graphs. The enumerator counts labelled edge orientations, not isomorphism types. A second proof from general gain-graph coefficient recurrences might recover the same result; no claim of independent foundational theory is made. Bibliographic searches cannot exclude unindexed equivalent results, and no independent mathematical review has been performed.

## References

[1] S. Akbari, J. Aloni, M. Levit, B. Mohar and S. Xia, *Spectrally symmetric orientations of graphs*, arXiv:2512.08049, first submitted 2025-12-08, revised 2026-09-09. https://arxiv.org/abs/2512.08049 .

[2] X. Li and Y. Yu, *Hermitian adjacency matrix of the second kind for mixed graphs*, arXiv:2102.03760, especially Theorems 2.6–2.8. https://arxiv.org/abs/2102.03760 .

[3] B. Mohar, *A new kind of Hermitian matrices for digraphs*, arXiv:1909.10878. https://arxiv.org/abs/1909.10878 .
