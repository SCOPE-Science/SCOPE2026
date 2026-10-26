# A quarter-deck obstruction for triangle-tiling polynomial reconstruction

## Finding

For every integer \(\ell\ge2\), put \(X_1=P_{\ell+1}\sqcup P_{\ell-1}\) and \(X_2=P_{\ell}\sqcup P_{\ell}\). For a simple graph \(X\), define \(T(X)\) by retaining every edge \(uv\in E(X)\) and adding one new vertex \(w_{uv}\) adjacent exactly to \(u\) and \(v\). Then \(T(X_1)\) and \(T(X_2)\) have the same \(\ell\)-deck but different \(K_3\)-tiling polynomials. Their common order is \(N=4\ell-2\), so the asymptotic reconstruction constant \(c_{K_3}\) for the triangle-tiling polynomial is at least \(1/4\).

Here the \(s\)-deck is the multiset of isomorphism types of induced \(s\)-vertex subgraphs. The \(K_3\)-tiling polynomial is \(m_{K_3}(G,z)=\sum_{j\ge0}(-1)^j p_{K_3}(G,j)z^{|V(G)|-3j}\), where \(p_{K_3}(G,j)\) counts sets of \(j\) vertex-disjoint triangles. The constant \(c_{K_3}\) is the infimum of asymptotic deck fractions sufficient to reconstruct this polynomial, in the sense specified in Kim and Lee's Problem 6.1.

## Assumptions and scope

All graphs are finite and simple. \(P_t\) denotes the path on \(t\) vertices; \(P_1\) is an isolated vertex. The construction \(T(X)\) is used only for forests of maximum degree at most two. The conclusion is a lower bound on the asymptotic reconstruction constant, not an exact value; the known general upper bound for \(K_3\) is \(2/3\).

## Proof

**1. The source pair has equal \(\ell\)-decks.** The graphs \(X_1\) and \(X_2\) both have \(2\ell\) vertices and \(2\ell-2\) edges. Every path component has at least \(\ell-1\) vertices. Theorem 1.7 of Spinoza and West states that two maximum-degree-two graphs with the same order and size have the same \(s\)-deck when every path component has at least \(s-1\) vertices and every cycle has more than \(s\) vertices. Applying it with \(s=\ell\) gives \(D_{\ell}(X_1)=D_{\ell}(X_2)\).

**2. Deck-transfer lemma.** For any simple graph \(X\) and any \(s\ge2\), the \(s\)-deck of \(T(X)\) is determined by the \(s\)-deck of \(X\). To see this, choose an \(s\)-vertex set in \(T(X)\), split it into original vertices \(U\subseteq V(X)\) and selected edge-vertices \(W\subseteq E(X)\), and write \(a=|U|\), \(b=|W|=s-a\). Its induced graph consists of \(X[U]\), selected edge-vertices on edges internal to \(U\) (each adds a common neighbor to the edge endpoints), selected edge-vertices on cut edges (each adds a leaf at its endpoint in \(U\)), and selected edge-vertices for edges wholly outside \(U\) (isolated vertices). For fixed \(X[U]\), the number of choices in each class is a polynomial of total degree at most \(b\) in the full degrees of vertices of \(U\), with coefficients determined by \(s\), \(X[U]\), and \(m=|E(X)|\). Every degree monomial of total degree at most \(b\) counts ordered choices of at most \(b\) incident edges; their outside endpoints, together with \(U\), occupy at most \(a+b=s\) vertices. Thus its aggregate over all \(U\) of each induced type is determined by counts of induced subgraphs of \(X\) on at most \(s\) vertices. Those counts are determined by the \(s\)-deck, and \(m\) is determined by the \(2\)-deck. Hence the \(s\)-deck of \(T(X)\) is determined by the \(s\)-deck of \(X\). Applying the lemma to Step 1 gives \(D_{\ell}(T(X_1))=D_{\ell}(T(X_2))\).

**3. The triangle-tiling polynomials differ.** Since \(X_1\) and \(X_2\) are forests, every triangle in \(T(X_i)\) is exactly one of the triangles formed by an edge \(uv\in E(X_i)\) and its new vertex \(w_{uv}\). Two such triangles are vertex-disjoint exactly when their corresponding edges in \(X_i\) are disjoint. Therefore \(p_{K_3}(T(X_i),j)\) equals the number of \(j\)-edge matchings of \(X_i\), for every \(j\). The matching polynomials of \(X_1\) and \(X_2\) differ in their perfect-matching coefficient: if \(\ell\) is even, \(X_1\) has no perfect matching and \(X_2\) has exactly one; if \(\ell\) is odd, \(X_1\) has exactly one and \(X_2\) has none. Hence their triangle-tiling polynomials differ.

**4. Asymptotic consequence.** Each \(X_i\) has \(2\ell\) vertices and \(2\ell-2\) edges, so \(T(X_i)\) has \(N=4\ell-2\) vertices. Since \(\ell/N\to1/4\), for every \(c<1/4\) one can choose \(\varepsilon>0\) with \(c+\varepsilon<1/4\); for all sufficiently large \(\ell\), \(\lfloor(c+\varepsilon)N\rfloor<\ell\). Equal \(\ell\)-decks imply equal decks at every smaller size, so the two graphs are indistinguishable from that many-vertex deck despite different triangle-tiling polynomials. No \(c<1/4\) can satisfy the reconstruction property.

## Verification

The path-pair hypotheses were checked against Theorem 1.7 of Spinoza and West. The deck-transfer lemma was reconstructed from the partition of selected vertices into original vertices and edge-vertices; its key degree-polynomial has degree at most the number of selected edge-vertices, so the required outside witnesses fit within an \(s\)-vertex induced subgraph. The triangle correspondence is exact because the source graphs are forests. The parity cases give an explicit coefficient separating the two tiling polynomials. No computation is used as a substitute for the infinite argument.

## Relationship to prior work

Kim and Lee prove that the \(F\)-tiling polynomial of an \(n\)-vertex graph is reconstructible from its \(\lfloor (|V(F)|-1)n/|V(F)|\rfloor+1\)-deck, and explicitly ask for the optimal asymptotic fraction \(c_F\). Their theorem gives \(c_{K_3}\le2/3\) but does not provide the lower bound established here. Spinoza and West supply the equal-deck pair of path forests; the new step is transferring that indistinguishability through \(T\) while converting matchings into triangle packings.

## Limitations

This proves only \(1/4\le c_{K_3}\le2/3\); it does not determine \(c_{K_3}\). The deck-transfer lemma is stated for finite simple graphs and the defined edge-vertex expansion. The argument gives an infinite family of obstructions, not a classification of all extremal deck-equivalent pairs.

## References

1. D. Kim and H. Lee, *Reconstructing hypergraph matching polynomials*, arXiv:2501.19081v1, first posted 2025-01-31, especially Theorem 1.4, Corollary 1.6, and Problem 6.1. https://arxiv.org/abs/2501.19081
2. H. Spinoza and D. B. West, *Reconstruction from k-decks for graphs with maximum degree 2*, arXiv:1609.00284v1, first posted 2016-09-01, especially Theorem 1.7 and Corollary 2.5. https://arxiv.org/abs/1609.00284
